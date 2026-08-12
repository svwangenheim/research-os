#!/usr/bin/env python3
"""
wiki_quality_check.py - advisory quality checker for research-os thematic wikis.

Two-layer model aware: checks the Claude-maintained thematic wikis
(`<wiki>/00_inbox .. 90_synthesis`) and, in --root or --brain mode, the
personal `_brain/` layer (frontmatter gaps, catalog-invisible project notes,
stale active projects). Engram's non-markdown state under `_brain/learning/`
is ignored.

Usage:
    python wiki_quality_check.py --vault <path/to/one/wiki>
    python wiki_quality_check.py --root  <path/to/vault/root>
    python wiki_quality_check.py --brain <path/to/vault/_brain>

--vault checks a single wiki folder (must contain 10_sources/).
--root checks every wiki registered in ~/.claude/vaults.json; if that
registry does not exist, falls back to scanning the immediate subdirectories
of <path> for anything that looks like a wiki (has a 10_sources/ folder).

Stdlib-only (no PyYAML). Frontmatter is read with a lightweight line-based
parser, not a full YAML parser - good enough for the flat key/scalar/list
shapes research-os note templates actually use (same philosophy as the
targeted-regex extraction in hooks/pre-compact.py).

This is an advisory tool: it always exits 0. Findings are for a human or an
agent (wiki-maintain) to act on, never a hard gate.
"""

from __future__ import annotations

import argparse
import difflib
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

WIKI_SUBDIRS = (
    "00_inbox",
    "10_sources",
    "20_summaries",
    "30_concepts",
    "40_methods",
    "50_datasets",
    "60_people_institutions",
    "90_synthesis",
)

# folder name -> accepted note_type values for that folder
FOLDER_NOTE_TYPES: dict[str, tuple[str, ...]] = {
    "20_summaries": ("summary", "source_summary"),
    "30_concepts": ("concept",),
    "40_methods": ("method",),
    "50_datasets": ("dataset",),
    "60_people_institutions": ("entity",),
    "90_synthesis": ("synthesis",),
}

# folder name -> required frontmatter keys (checked for presence + non-empty)
REQUIRED_FIELDS: dict[str, tuple[str, ...]] = {
    "20_summaries": ("title", "authors", "year", "proximity", "tags", "updated"),
    "30_concepts": ("title", "summary", "tags", "updated"),
    "40_methods": ("title", "summary", "tags", "updated"),
    "50_datasets": ("title", "summary", "tags", "updated"),
    "60_people_institutions": ("title", "entity_type", "updated"),
    "90_synthesis": ("title", "summary", "updated"),
}

# folders whose notes participate in the canonical-duplicate scan
CANONICAL_DUPE_FOLDERS = ("30_concepts", "40_methods", "50_datasets", "60_people_institutions")

# folders whose notes are checked for orphan/weak wikilinking
CORE_LINK_FOLDERS = (
    "20_summaries",
    "30_concepts",
    "40_methods",
    "50_datasets",
    "60_people_institutions",
    "90_synthesis",
)

# _brain/ (personal layer) checks
BRAIN_FOLDERS = ("projects", "procedures", "thoughts", "learning", "synthesis", "daily", "weekly")

BRAIN_FOLDER_NOTE_TYPES: dict[str, tuple[str, ...]] = {
    "projects": ("project",),
    "procedures": ("procedure",),
    "thoughts": ("thought",),
    "learning": ("learning",),
    "synthesis": ("synthesis",),
    "daily": ("daily",),
    "weekly": ("weekly",),
}

# folder -> required frontmatter keys (presence + non-empty)
BRAIN_REQUIRED_FIELDS: dict[str, tuple[str, ...]] = {
    "projects": ("title", "status", "updated"),
    "procedures": ("title", "role", "trigger", "automation", "updated"),
    "thoughts": ("title", "updated"),
    "learning": ("title", "confidence", "updated"),
    "synthesis": ("title", "updated"),
    "daily": ("updated",),
    "weekly": ("updated",),
}

BRAIN_STALE_DAYS = 120  # an 'active' project note untouched this long is flagged

# Closed enums for procedure notes. A typo here silently breaks the Dataview
# catalog and the promotion check, so it is caught at audit time instead.
PROCEDURE_ROLES = ("phd", "dz-modelling", "dz-outreach", "admin")
PROCEDURE_AUTOMATION = ("manual", "assisted", "scheduled", "vetoed")
PROCEDURE_PROMOTION = ("draft", "maturing", "ready", "promoted")
STEP_ACTOR_TAGS = ("[ai]", "[human]", "[external]", "[veto]")

MIN_SUMMARY_WORDS = 120  # below this, a summary body is "thin"
DUPLICATE_TITLE_RATIO = 0.80  # difflib ratio threshold for "possible duplicate"
WEAK_LINK_MAX_TOTAL = 1  # in-degree + out-degree <= this counts as "weak"

FRONTMATTER_RE = re.compile(r"^---[ \t]*\r?\n(.*?)\r?\n---[ \t]*\r?\n", re.DOTALL)
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
KEY_LINE_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*):[ \t]*(.*)$")
LIST_ITEM_RE = re.compile(r"^[ \t]+-[ \t]*(.*)$")


# ---------------------------------------------------------------------------
# Frontmatter parsing (regex/line-based - no PyYAML)
# ---------------------------------------------------------------------------


def _strip_quotes(raw: str) -> str:
    s = raw.strip()
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "\"'":
        return s[1:-1]
    return s


def _split_top_level(s: str) -> list[str]:
    """Split a comma-separated inline list, respecting quoted substrings."""
    parts: list[str] = []
    current: list[str] = []
    in_quote: str | None = None
    for ch in s:
        if in_quote:
            current.append(ch)
            if ch == in_quote:
                in_quote = None
            continue
        if ch in "\"'":
            in_quote = ch
            current.append(ch)
            continue
        if ch == ",":
            parts.append("".join(current))
            current = []
            continue
        current.append(ch)
    if current:
        parts.append("".join(current))
    return [p for p in parts if p.strip() != ""]


def _parse_scalar(raw: str) -> Any:
    s = raw.strip()
    if s == "" or s in ("~", "null", "Null", "NULL"):
        return None
    if s == "[]":
        return []
    if s.startswith("[") and s.endswith("]"):
        inner = s[1:-1].strip()
        return [_strip_quotes(p) for p in _split_top_level(inner)] if inner else []
    return _strip_quotes(s)


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    """Parse a note's YAML-ish frontmatter block into a flat dict, plus the body.

    Supports scalars, quoted scalars, inline lists (`[a, b]`), and block
    lists (`key:` followed by indented `- item` lines). That covers every
    shape used by the templates in vault/_templates/ and the notes ingested
    so far. Anything stranger is left as a raw string rather than raising.
    """
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text
    body = text[match.end():]
    lines = match.group(1).split("\n")
    data: dict[str, Any] = {}
    i = 0
    while i < len(lines):
        key_match = KEY_LINE_RE.match(lines[i])
        if not key_match:
            i += 1
            continue
        key, rest = key_match.group(1), key_match.group(2)
        if rest.strip() != "":
            data[key] = _parse_scalar(rest)
            i += 1
            continue
        items: list[str] = []
        j = i + 1
        while j < len(lines):
            item_match = LIST_ITEM_RE.match(lines[j])
            if not item_match:
                break
            items.append(_strip_quotes(item_match.group(1)))
            j += 1
        data[key] = items if items else None
        i = j if items else i + 1
    return data, body


def is_empty(value: Any) -> bool:
    if value is None:
        return True
    if isinstance(value, str):
        return value.strip() == ""
    if isinstance(value, list):
        return len(value) == 0
    return False


# ---------------------------------------------------------------------------
# Note model
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Note:
    path: Path
    rel: str  # path relative to the wiki root, forward slashes
    folder: str  # immediate subfolder name, e.g. "30_concepts"
    stem: str  # filename without extension, lowercased
    frontmatter: dict[str, Any]
    body: str
    outlinks: tuple[str, ...]  # normalized (lowercased, stem-only) targets
    mtime: float


def normalize_link_target(raw: str) -> str:
    """[[30_concepts/Foo Bar.md]] / [[foo-bar]] / [[foo-bar#Section]] -> 'foo bar'."""
    target = raw.strip()
    target = target.split("/")[-1].split("\\")[-1]
    if target.lower().endswith(".md"):
        target = target[:-3]
    return target.strip().lower()


def load_note(wiki_root: Path, path: Path) -> Note | None:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    frontmatter, body = parse_frontmatter(text)
    outlinks = tuple(sorted({normalize_link_target(m) for m in WIKILINK_RE.findall(body)}))
    rel = path.relative_to(wiki_root).as_posix()
    folder = path.relative_to(wiki_root).parts[0] if len(path.relative_to(wiki_root).parts) > 1 else ""
    try:
        mtime = path.stat().st_mtime
    except OSError:
        mtime = 0.0
    return Note(
        path=path,
        rel=rel,
        folder=folder,
        stem=path.stem.lower(),
        frontmatter=frontmatter,
        body=body,
        outlinks=outlinks,
        mtime=mtime,
    )


def load_wiki_notes(wiki_root: Path) -> list[Note]:
    """Load every .md file under the wiki, skipping README.md (folder docs, not notes)."""
    notes: list[Note] = []
    for md_path in sorted(wiki_root.rglob("*.md")):
        if md_path.name.lower() == "readme.md":
            continue
        note = load_note(wiki_root, md_path)
        if note is not None:
            notes.append(note)
    return notes


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------


@dataclass
class Finding:
    kind: str  # "gap" | "thin" | "dup" | "dup-alias" | "orphan" | "weak" | "broken" | "stale"
    rel: str
    detail: str


def check_required_fields(note: Note) -> list[Finding]:
    required = REQUIRED_FIELDS.get(note.folder)
    if required is None:
        return []
    missing = [key for key in required if is_empty(note.frontmatter.get(key))]
    accepted_types = FOLDER_NOTE_TYPES.get(note.folder, ())
    note_type = note.frontmatter.get("note_type")
    if accepted_types and note_type not in accepted_types:
        missing.append(f"note_type (found {note_type!r}, expected one of {accepted_types})")
    if not missing:
        return []
    return [Finding("gap", note.rel, f"missing/empty frontmatter: {', '.join(missing)}")]


def check_summary_depth(note: Note) -> list[Finding]:
    if note.folder != "20_summaries":
        return []
    findings: list[Finding] = []
    word_count = len(note.body.split())
    if word_count < MIN_SUMMARY_WORDS:
        findings.append(
            Finding("thin", note.rel, f"body is only {word_count} words (< {MIN_SUMMARY_WORDS}) - looks like an abstract, not a detailed summary")
        )
    has_source_files = not is_empty(note.frontmatter.get("source_files"))
    mentions_source_in_body = bool(re.search(r"source file", note.body, re.IGNORECASE))
    if not has_source_files and not mentions_source_in_body:
        findings.append(Finding("gap", note.rel, "no source_files in frontmatter and no 'Source file' reference in body"))
    return findings


def normalize_title(raw: str) -> str:
    s = raw.lower()
    s = re.sub(r"[^a-z0-9 ]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def check_duplicates(notes: list[Note]) -> list[Finding]:
    findings: list[Finding] = []
    by_folder: dict[str, list[Note]] = {}
    for note in notes:
        if note.folder in CANONICAL_DUPE_FOLDERS:
            by_folder.setdefault(note.folder, []).append(note)

    for folder_notes in by_folder.values():
        titles = [normalize_title(str(n.frontmatter.get("title") or n.stem)) for n in folder_notes]
        alias_sets = [
            {normalize_title(a) for a in (n.frontmatter.get("aliases") or []) if isinstance(a, str)}
            for n in folder_notes
        ]
        seen_pairs: set[tuple[int, int]] = set()
        for i, note_a in enumerate(folder_notes):
            for j in range(i + 1, len(folder_notes)):
                note_b = folder_notes[j]
                pair = (i, j)
                if pair in seen_pairs:
                    continue
                if titles[i] in alias_sets[j] or titles[j] in alias_sets[i] or (alias_sets[i] & alias_sets[j]):
                    findings.append(Finding("dup-alias", note_a.rel, f"alias overlap with {note_b.rel}"))
                    seen_pairs.add(pair)
                    continue
                ratio = difflib.SequenceMatcher(None, titles[i], titles[j]).ratio()
                if ratio >= DUPLICATE_TITLE_RATIO:
                    findings.append(Finding("dup", note_a.rel, f"title similarity {ratio:.2f} with {note_b.rel}"))
                    seen_pairs.add(pair)
    return findings


def build_link_graph(notes: list[Note]) -> tuple[dict[str, int], dict[str, int], dict[str, set[str]]]:
    """Return (out_degree, in_degree, stem_to_files) keyed by rel path / stem."""
    stem_to_files: dict[str, set[str]] = {}
    for note in notes:
        stem_to_files.setdefault(note.stem, set()).add(note.rel)

    out_degree: dict[str, int] = {}
    in_degree: dict[str, int] = {n.rel: 0 for n in notes}
    for note in notes:
        out_degree[note.rel] = len(note.outlinks)
        for target in note.outlinks:
            for target_rel in stem_to_files.get(target, ()):
                if target_rel != note.rel:
                    in_degree[target_rel] = in_degree.get(target_rel, 0) + 1
    return out_degree, in_degree, stem_to_files


def check_orphans_and_weak_links(notes: list[Note]) -> list[Finding]:
    out_degree, in_degree, _ = build_link_graph(notes)
    findings: list[Finding] = []
    for note in notes:
        if note.folder not in CORE_LINK_FOLDERS:
            continue
        out_d = out_degree.get(note.rel, 0)
        in_d = in_degree.get(note.rel, 0)
        total = out_d + in_d
        if total == 0:
            findings.append(Finding("orphan", note.rel, "0 outgoing, 0 incoming wikilinks"))
        elif total <= WEAK_LINK_MAX_TOTAL:
            findings.append(Finding("weak", note.rel, f"only {total} total wikilink(s) (out={out_d}, in={in_d})"))
    return findings


def collect_external_stems(brain_path: Path) -> frozenset[str]:
    """Stems of every note under _brain/ (excluding README.md), lowercased.

    Obsidian resolves [[bare-name]] wikilinks vault-wide, not scoped to a
    subfolder - a wiki summary that links to a project note living in
    _brain/projects/ resolves fine in the real graph even though _brain/ is
    outside this wiki's own tree. Without this, every such cross-layer link
    (common after a project note is lifted into _brain/) reads as "broken"
    even though it isn't. _brain/'s own content is never quality-checked by
    this tool - only its filenames are used, purely to avoid this false
    positive in check_broken_links.
    """
    if not brain_path.is_dir():
        return frozenset()
    return frozenset(
        p.stem.lower() for p in brain_path.rglob("*.md") if p.name.lower() != "readme.md"
    )


def check_broken_links(notes: list[Note], known_external_stems: frozenset[str] = frozenset()) -> list[Finding]:
    """One Finding per (file, missing target) pair. detail carries the raw
    target first (before ' | ') so render_report can group by target -
    a handful of systemic dangling links (e.g. a moved project note) is a
    very different situation from many one-off typos."""
    _, _, stem_to_files = build_link_graph(notes)
    findings: list[Finding] = []
    for note in notes:
        for target in note.outlinks:
            if target not in stem_to_files and target not in known_external_stems:
                findings.append(Finding("broken", note.rel, f"{target} | [[{target}]] not found anywhere in the wiki"))
    return findings


def check_index_log_staleness(wiki_root: Path, wiki_name: str, notes: list[Note]) -> list[Finding]:
    findings: list[Finding] = []
    summaries = [n for n in notes if n.folder == "20_summaries"]
    if not summaries:
        return findings

    index_path = _first_existing(wiki_root / "index.md", wiki_root.parent / "index.md")
    log_path = _first_existing(wiki_root / "log.md", wiki_root.parent / "log.md")

    if index_path is not None:
        index_text = index_path.read_text(encoding="utf-8", errors="replace")
        if "```dataview" in index_text and wiki_name not in index_text:
            findings.append(Finding("stale", str(index_path), f"'{wiki_name}' not mentioned in any Dataview FROM clause - wiki may be missing from the cross-wiki index"))
    else:
        findings.append(Finding("stale", wiki_name, "no index.md found (checked wiki folder and its parent)"))

    if log_path is not None:
        log_text = log_path.read_text(encoding="utf-8", errors="replace")
        recent = sorted(summaries, key=lambda n: n.mtime, reverse=True)[:5]
        unreferenced = [n.rel for n in recent if n.stem not in log_text.lower() and n.path.stem not in log_text]
        if unreferenced:
            findings.append(Finding("stale", str(log_path), f"{len(unreferenced)} recently-modified summar(y/ies) not referenced: {', '.join(unreferenced)}"))
    else:
        findings.append(Finding("stale", wiki_name, "no log.md found (checked wiki folder and its parent)"))

    return findings


def _first_existing(*candidates: Path) -> Path | None:
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    return None


# ---------------------------------------------------------------------------
# Per-wiki orchestration + reporting
# ---------------------------------------------------------------------------


@dataclass
class WikiReport:
    name: str
    path: Path
    counts: dict[str, int]
    findings: list[Finding]


def check_one_wiki(wiki_path: Path, known_external_stems: frozenset[str] = frozenset()) -> WikiReport:
    name = wiki_path.name
    notes = load_wiki_notes(wiki_path)
    counts = {folder: sum(1 for n in notes if n.folder == folder) for folder in WIKI_SUBDIRS}

    findings: list[Finding] = []
    for note in notes:
        findings.extend(check_required_fields(note))
        findings.extend(check_summary_depth(note))
    findings.extend(check_duplicates(notes))
    findings.extend(check_orphans_and_weak_links(notes))
    findings.extend(check_broken_links(notes, known_external_stems))
    findings.extend(check_index_log_staleness(wiki_path, name, notes))

    return WikiReport(name=name, path=wiki_path, counts=counts, findings=findings)


def _render_broken_links(items: list[Finding]) -> list[str]:
    """Group broken-link findings by target - one recurring dangling target
    (e.g. a project note moved out of the wiki) reads as one line, not N."""
    by_target: dict[str, list[str]] = {}
    for item in items:
        target = item.detail.split(" | ", 1)[0]
        by_target.setdefault(target, []).append(item.rel)

    lines: list[str] = []
    for target, files in sorted(by_target.items(), key=lambda kv: len(kv[1]), reverse=True):
        if len(files) >= 3:
            lines.append(f"  - [[{target}]] missing - referenced from {len(files)} files, e.g. {files[0]}, {files[1]}, ...")
        else:
            for rel in files:
                lines.append(f"  - {rel} - [[{target}]] not found anywhere in the wiki")
    return lines


def render_report(report: WikiReport) -> str:
    lines: list[str] = []
    lines.append(f"\n## Wiki: {report.name}  ({report.path})")
    counts_str = "  ".join(f"{folder}={report.counts.get(folder, 0)}" for folder in WIKI_SUBDIRS)
    lines.append(f"Counts: {counts_str}")

    by_kind: dict[str, list[Finding]] = {}
    for finding in report.findings:
        by_kind.setdefault(finding.kind, []).append(finding)

    sections = [
        ("gap", "Required-field / frontmatter gaps"),
        ("thin", "Thin summaries"),
        ("dup", "Duplicate-candidate titles (canonical folders)"),
        ("dup-alias", "Duplicate-candidate aliases (canonical folders)"),
        ("orphan", "Orphan notes (no incoming or outgoing wikilinks)"),
        ("weak", "Weakly-linked notes"),
        ("broken", "Broken wikilinks"),
        ("stale", "Index / log staleness"),
    ]
    total_findings = 0
    for kind, title in sections:
        items = by_kind.get(kind, [])
        total_findings += len(items)
        if not items:
            continue
        lines.append(f"\n### {title} ({len(items)})")
        if kind == "broken":
            lines.extend(_render_broken_links(items))
        else:
            for item in items:
                lines.append(f"  - {item.rel} - {item.detail}")

    if total_findings == 0:
        lines.append("\nNo issues found. Wiki is verifier-clean.")
    else:
        lines.append(f"\nTotal findings for {report.name}: {total_findings}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# _brain/ personal-layer checks
# ---------------------------------------------------------------------------


def load_brain_notes(brain_root: Path) -> list[Note]:
    """Load notes from the six _brain/ content folders (top level only).

    Skips READMEs, the frozen synthesis archive (a subfolder, so not globbed),
    and engram's non-markdown state under learning/.
    """
    notes: list[Note] = []
    for folder in BRAIN_FOLDERS:
        folder_path = brain_root / folder
        if not folder_path.is_dir():
            continue
        for md_path in sorted(folder_path.glob("*.md")):
            if md_path.name.lower() in ("readme.md", "pending-topics.md"):
                continue
            note = load_note(brain_root, md_path)
            if note is not None:
                notes.append(note)
    return notes


def _parse_iso_date(raw: Any) -> Any:
    from datetime import datetime as _dt

    if not isinstance(raw, str):
        return None
    try:
        return _dt.strptime(raw.strip()[:10], "%Y-%m-%d")
    except ValueError:
        return None


def check_brain_note(note: Note) -> list[Finding]:
    required = BRAIN_REQUIRED_FIELDS.get(note.folder, ())
    missing = [key for key in required if is_empty(note.frontmatter.get(key))]
    accepted = BRAIN_FOLDER_NOTE_TYPES.get(note.folder, ())
    note_type = note.frontmatter.get("note_type")
    if accepted and note_type not in accepted:
        missing.append(f"note_type (found {note_type!r}, expected one of {accepted})")
    if not missing:
        return []
    return [Finding("gap", note.rel, f"missing/empty frontmatter: {', '.join(missing)}")]


def check_brain_orphans(notes: list[Note]) -> list[Finding]:
    """Project notes lacking `note_type: project` are invisible to the
    Dataview catalog (index.md queries WHERE note_type = 'project')."""
    findings: list[Finding] = []
    for note in notes:
        if note.folder == "projects" and note.frontmatter.get("note_type") != "project":
            findings.append(
                Finding("orphan", note.rel, "no `note_type: project` frontmatter - invisible to the index.md catalog")
            )
    return findings


def check_brain_staleness(notes: list[Note], today: Any = None) -> list[Finding]:
    from datetime import datetime as _dt

    today = today or _dt.now()
    findings: list[Finding] = []
    for note in notes:
        if note.folder != "projects":
            continue
        if note.frontmatter.get("status") not in (None, "active"):
            continue
        updated = _parse_iso_date(note.frontmatter.get("updated"))
        if updated is None:
            continue
        age = (today - updated).days
        if age > BRAIN_STALE_DAYS:
            findings.append(Finding("stale", note.rel, f"active project note not updated in {age} days (> {BRAIN_STALE_DAYS})"))
    return findings


def check_procedure_note(note: Note) -> list[Finding]:
    """Procedure-specific integrity checks.

    Three things break a procedure silently, so all three are caught here:
    a value outside a closed enum (invisible to the Dataview catalog), a step
    with no actor tag (unclear who runs it, so it can never be promoted), and a
    veto without a reason (an unexplained veto decays into an ignored one).
    """
    if note.frontmatter.get("note_type") != "procedure":
        return []

    findings: list[Finding] = []
    rel = note.rel
    fm = note.frontmatter

    enum_checks = (
        ("role", PROCEDURE_ROLES),
        ("automation", PROCEDURE_AUTOMATION),
        ("promotion", PROCEDURE_PROMOTION),
    )
    for key, allowed in enum_checks:
        value = fm.get(key)
        if not is_empty(value) and value not in allowed:
            findings.append(
                Finding("procedure", rel, f"{key}: {value!r} is not one of {allowed}")
            )

    if fm.get("automation") == "vetoed" and is_empty(fm.get("veto_reason")):
        findings.append(
            Finding("procedure", rel, "automation: vetoed but no veto_reason - a veto must say why")
        )

    untagged = untagged_steps(note.body)
    if untagged:
        preview = "; ".join(untagged[:3])
        findings.append(
            Finding(
                "procedure",
                rel,
                f"{len(untagged)} step(s) with no actor tag {STEP_ACTOR_TAGS}: {preview}",
            )
        )

    return findings


def untagged_steps(body: str) -> list[str]:
    """Numbered steps under `## Steps` that carry no actor tag.

    Only the Steps section is scanned -- numbered lists elsewhere in the note
    (failure modes, notes to self) are prose, not executable steps.
    """
    lines = body.split("\n")
    in_steps = False
    untagged: list[str] = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("## "):
            in_steps = stripped.lower().startswith("## steps")
            continue
        if not in_steps or not stripped:
            continue
        if not re.match(r"^\d+\.\s+\S", stripped):
            continue
        if not any(tag in stripped for tag in STEP_ACTOR_TAGS):
            untagged.append(stripped[:60])
    return untagged


@dataclass
class BrainReport:
    path: Path
    counts: dict[str, int]
    findings: list[Finding]


def check_brain(brain_path: Path) -> BrainReport:
    notes = load_brain_notes(brain_path)
    counts = {folder: sum(1 for n in notes if n.folder == folder) for folder in BRAIN_FOLDERS}
    findings: list[Finding] = []
    for note in notes:
        findings.extend(check_brain_note(note))
        findings.extend(check_procedure_note(note))
    findings.extend(check_brain_orphans(notes))
    findings.extend(check_brain_staleness(notes))
    return BrainReport(path=brain_path, counts=counts, findings=findings)


def render_brain_report(report: BrainReport) -> str:
    lines: list[str] = [f"\n## Personal brain: _brain/  ({report.path})"]
    counts_str = "  ".join(f"{folder}={report.counts.get(folder, 0)}" for folder in BRAIN_FOLDERS)
    lines.append(f"Counts: {counts_str}")

    by_kind: dict[str, list[Finding]] = {}
    for finding in report.findings:
        by_kind.setdefault(finding.kind, []).append(finding)

    sections = [
        ("gap", "Frontmatter gaps"),
        ("orphan", "Catalog-invisible project notes"),
        ("stale", "Stale active project notes"),
        ("procedure", "Procedure defects"),
    ]
    total = 0
    for kind, title in sections:
        items = by_kind.get(kind, [])
        total += len(items)
        if not items:
            continue
        lines.append(f"\n### {title} ({len(items)})")
        for item in items:
            lines.append(f"  - {item.rel} - {item.detail}")
    lines.append("\nNo issues found in _brain/." if total == 0 else f"\nTotal findings for _brain/: {total}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Registry resolution
# ---------------------------------------------------------------------------


def load_registry(registry_path: Path) -> dict[str, Any] | None:
    if not registry_path.is_file():
        return None
    try:
        return json.loads(registry_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Warning: could not parse {registry_path}: {exc}", file=sys.stderr)
        return None


def discover_wikis_from_registry(registry: dict[str, Any]) -> list[Path]:
    wikis = registry.get("wikis", {})
    paths: list[Path] = []
    for entry in wikis.values():
        path_str = entry.get("path") if isinstance(entry, dict) else None
        if path_str:
            paths.append(Path(path_str))
    return paths


def discover_wikis_by_scanning(root: Path) -> list[Path]:
    if not root.is_dir():
        return []
    found: list[Path] = []
    for child in sorted(root.iterdir()):
        if not child.is_dir() or child.name.startswith((".", "_")):
            continue
        if (child / "10_sources").is_dir():
            found.append(child)
    return found


def resolve_root_wikis(root: Path) -> list[Path]:
    registry = load_registry(Path.home() / ".claude" / "vaults.json")
    if registry is not None:
        wikis = discover_wikis_from_registry(registry)
        if wikis:
            return wikis
        print("Warning: ~/.claude/vaults.json has no 'wikis' entries; falling back to directory scan.", file=sys.stderr)
    return discover_wikis_by_scanning(root)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Advisory quality checker for research-os thematic wikis. Always exits 0.",
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--vault", type=str, help="Path to a single wiki folder (contains 10_sources/, 20_summaries/, ...).")
    group.add_argument("--root", type=str, help="Path to the vault root; checks every registered wiki, plus _brain/ if present.")
    group.add_argument("--brain", type=str, help="Path to the vault's _brain/ folder; checks the personal layer only.")
    return parser


def force_utf8_console() -> None:
    """Make stdout/stderr safe for non-ASCII content.

    Windows consoles (PowerShell/cmd) often default to a legacy codepage that
    cannot encode note titles, German umlauts, or an arrow in a wiki-links
    item. Reconfigure defensively so a printable-character issue never crashes
    an advisory tool. Shared by every script in this directory -- see the
    sibling modules that import it.
    """
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass


def main(argv: list[str] | None = None) -> int:
    force_utf8_console()

    parser = build_arg_parser()
    args = parser.parse_args(argv)

    if args.vault:
        wiki_path = Path(args.vault).expanduser().resolve()
        if not wiki_path.is_dir():
            print(f"'{wiki_path}' is not a directory - nothing to check.")
            return 0
        if not (wiki_path / "10_sources").is_dir():
            print(f"Warning: '{wiki_path}' has no 10_sources/ - this may not be a wiki folder. Checking anyway.")
        # _brain/ is normally a sibling of the wiki folder (both live under the
        # vault root) - collect its stems so cross-layer links don't false-positive.
        external_stems = collect_external_stems(wiki_path.parent / "_brain")
        report = check_one_wiki(wiki_path, external_stems)
        print(f"wiki_quality_check - single-wiki mode ({wiki_path})")
        print(render_report(report))
        return 0

    if args.brain:
        brain_path = Path(args.brain).expanduser().resolve()
        if not brain_path.is_dir():
            print(f"'{brain_path}' is not a directory - nothing to check.")
            return 0
        print(f"wiki_quality_check - brain mode ({brain_path})")
        print(render_brain_report(check_brain(brain_path)))
        return 0

    root_path = Path(args.root).expanduser().resolve()
    wiki_paths = resolve_root_wikis(root_path)
    print(f"wiki_quality_check - root mode ({root_path})")
    if not wiki_paths:
        print("No registered wikis found (checked ~/.claude/vaults.json, then scanned the root for 10_sources/ folders).")
        return 0

    external_stems = collect_external_stems(root_path / "_brain")
    print(f"Checking {len(wiki_paths)} wiki(s): {', '.join(p.name for p in wiki_paths)}")
    reports = [check_one_wiki(p, external_stems) for p in wiki_paths if p.is_dir()]
    for report in reports:
        print(render_report(report))

    brain_path = root_path / "_brain"
    if brain_path.is_dir():
        print(render_brain_report(check_brain(brain_path)))

    print("\n## Totals across all wikis")
    for report in reports:
        print(f"  {report.name}: {len(report.findings)} finding(s)")
    print(f"  Grand total: {sum(len(r.findings) for r in reports)} finding(s) across {len(reports)} wiki(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
