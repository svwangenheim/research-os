#!/usr/bin/env python3
"""
SessionStart hook - inject a bounded digest of the knowledge layer.

The vault is well built and largely unread. Retrieval depended on remembering
to type `/wiki-pull`, which means it happened at the start of deliberate
research sessions and almost never during the ordinary work where the corpus
would actually have changed an answer. This hook makes the first fact about
every session "here is what you already know about this".

It is READ-ONLY and bounded. The digest is capped at MAX_LINES; if the vault is
large the counts stay and the listings are truncated, because an unbounded
digest would trade one problem (nobody reads the wiki) for a worse one (every
session starts with a wall of stale titles).

What it shows is stage-aware, driven by `passport.yaml` `pipeline.current_stage`:
a strategy session wants `40_methods/`, an analysis session wants `50_datasets/`,
a writing session wants `90_synthesis/` and `30_concepts/`. Showing all of them
at every stage is how a digest becomes noise.

Silent when: no registry, no resolvable wiki, or the vault is unreadable. A
missing knowledge layer is a normal state, not an error.

Hook Event: SessionStart (matcher: startup|resume|clear)
Output: exit 0 + JSON with `hookSpecificOutput.additionalContext`.
Fail-open: any error exits 0 with no output.
"""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

MAX_LINES = 40
MAX_ITEMS_PER_FOLDER = 6
MAX_PUSHBACK = 3

REGISTRY = Path.home() / ".claude" / "vaults.json"
LEGACY_POINTER = Path.home() / ".claude" / "VAULT_PATH"

STAGE_RE = re.compile(r"^\s*current_stage:\s*[\"']?([\w-]+)", re.MULTILINE)
MAIN_WIKI_RE = re.compile(r"^\s*main_wiki:\s*[\"']?([^\"'\s#]+)", re.MULTILINE)
SLUG_RE = re.compile(r"^\s*slug:\s*[\"']?([^\"'\s#]+)", re.MULTILINE)
UNRESOLVED_EMPTY_RE = re.compile(r"^\s*unresolved:\s*\[\s*\]\s*$", re.MULTILINE)
UNRESOLVED_ITEMS_RE = re.compile(r"^\s*unresolved:\s*$\n(\s+-\s+\S)", re.MULTILINE)

# Which folders matter at which stage. The fallback covers discovery and any
# stage not listed.
STAGE_FOCUS: dict[str, tuple[str, ...]] = {
    "discovery": ("30_concepts", "90_synthesis"),
    "strategy": ("40_methods", "30_concepts"),
    "analysis": ("50_datasets", "40_methods"),
    "writing": ("90_synthesis", "30_concepts"),
    "review": ("90_synthesis", "30_concepts"),
    "revision": ("90_synthesis", "30_concepts"),
    "submission": ("90_synthesis",),
}
DEFAULT_FOCUS = ("30_concepts", "40_methods")

COUNTED_FOLDERS = (
    ("30_concepts", "concepts"),
    ("40_methods", "methods"),
    ("50_datasets", "datasets"),
    ("20_summaries", "summaries"),
    ("90_synthesis", "synthesis"),
)


def find_up(start: Path, name: str, levels: int = 6) -> Path | None:
    current = start.resolve()
    for _ in range(levels):
        candidate = current / name
        if candidate.is_file():
            return candidate
        if current == current.parent:
            break
        current = current.parent
    return None


def load_registry() -> dict:
    try:
        return json.loads(REGISTRY.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def resolve_wiki(project_dir: Path, registry: dict) -> tuple[str | None, Path | None]:
    """The standard ladder from rules/wiki-integration.md, minus the interactive step.

    passport meta.main_wiki > .research-os-wiki pin > the registry's only wiki.
    A hook cannot ask, so where the ladder would prompt, it stays silent instead.
    """
    wikis = registry.get("wikis") or {}
    if not wikis:
        return None, None

    theme: str | None = None

    passport = find_up(project_dir, "passport.yaml")
    if passport is not None:
        try:
            match = MAIN_WIKI_RE.search(passport.read_text(encoding="utf-8", errors="replace"))
            if match and match.group(1) in wikis:
                theme = match.group(1)
        except OSError:
            pass

    if theme is None:
        pin = project_dir / ".research-os-wiki"
        if pin.is_file():
            try:
                text = pin.read_text(encoding="utf-8", errors="replace").strip()
                candidate = text.split(":", 1)[-1].strip() if ":" in text else text
                if candidate in wikis:
                    theme = candidate
            except OSError:
                pass

    if theme is None and len(wikis) == 1:
        theme = next(iter(wikis))

    if theme is None:
        return None, None

    raw = (wikis.get(theme) or {}).get("path")
    if not raw:
        return None, None
    path = Path(raw)
    return (theme, path) if path.is_dir() else (theme, None)


def folder_counts(wiki: Path) -> list[str]:
    parts: list[str] = []
    for folder, label in COUNTED_FOLDERS:
        directory = wiki / folder
        if not directory.is_dir():
            continue
        count = sum(
            1
            for f in directory.glob("*.md")
            if f.name.lower() not in ("readme.md", "_map.md")
        )
        if count:
            parts.append(f"{count} {label}")
    return parts


def map_entries(wiki: Path, folder: str, limit: int) -> list[str]:
    """Note titles for one folder, preferring the generated _map.md ledes."""
    directory = wiki / folder
    if not directory.is_dir():
        return []
    names = sorted(
        f.stem
        for f in directory.glob("*.md")
        if f.name.lower() not in ("readme.md", "_map.md")
    )
    return names[:limit]


def map_is_stale(wiki: Path) -> bool:
    """True when a note is newer than the generated _map.md catalogue.

    `_map.md` is what /wiki-pull reads first, and it is regenerated by the wiki
    skills - but a note edited directly in Obsidian bypasses all of them. Flag
    it rather than regenerating: this hook is read-only by contract, and a
    SessionStart hook that writes into the vault is a surprise nobody asked for.
    """
    catalogue = wiki / "_map.md"
    if not catalogue.is_file():
        return True
    try:
        cutoff = catalogue.stat().st_mtime
    except OSError:
        return False
    for note in wiki.rglob("*.md"):
        if note.name == "_map.md":
            continue
        try:
            if note.stat().st_mtime > cutoff:
                return True
        except OSError:
            continue
    return False


def pushback_items(project_dir: Path) -> list[str]:
    wiki_links = find_up(project_dir, "wiki-links.md")
    if wiki_links is None:
        return []
    try:
        text = wiki_links.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return []
    items: list[str] = []
    in_section = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.lower().startswith("## to push back"):
            in_section = True
            continue
        if in_section and stripped.startswith("## "):
            break
        if in_section and stripped.startswith("- [ ]"):
            item = stripped[len("- [ ]"):].strip()
            if item and not item.startswith("<"):
                items.append(item)
    return items


def project_header(project_dir: Path) -> tuple[str | None, str | None, str | None]:
    """(slug, stage, gate) from passport.yaml."""
    passport = find_up(project_dir, "passport.yaml")
    if passport is None:
        return None, None, None
    try:
        text = passport.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None, None, None
    slug = SLUG_RE.search(text)
    stage = STAGE_RE.search(text)
    if UNRESOLVED_EMPTY_RE.search(text):
        gate = "clean"
    elif UNRESOLVED_ITEMS_RE.search(text):
        gate = "BLOCKED"
    else:
        gate = None
    return (
        slug.group(1) if slug else None,
        stage.group(1) if stage else None,
        gate,
    )


def build_digest(project_dir: Path) -> str | None:
    registry = load_registry()
    theme, wiki = resolve_wiki(project_dir, registry)
    if theme is None or wiki is None:
        return None

    slug, stage, gate = project_header(project_dir)
    lines: list[str] = []

    head = "[research-os]"
    if slug:
        head += f" project: {slug}"
    if stage:
        head += f"  stage: {stage}"
    if gate:
        head += f"  integrity: {gate}"
    lines.append(head)

    counts = folder_counts(wiki)
    lines.append(f"main wiki: {theme}" + (f" - {' · '.join(counts)}" if counts else ""))

    focus = STAGE_FOCUS.get(stage or "", DEFAULT_FOCUS)
    for folder in focus:
        names = map_entries(wiki, folder, MAX_ITEMS_PER_FOLDER)
        if names:
            label = folder.split("_", 1)[-1]
            lines.append(f"  {label}: " + " · ".join(f"[[{n}]]" for n in names))

    pending = pushback_items(project_dir)
    if pending:
        lines.append(f"unpushed durable knowledge: {len(pending)} item(s)")
        for item in pending[:MAX_PUSHBACK]:
            lines.append(f"  - {item[:90]}")

    if map_is_stale(wiki):
        lines.append("_map.md is stale (notes edited since it was generated) - /wiki-maintain refreshes it.")

    lines.append(
        "Read the corpus before searching the web. /wiki-pull for the full read, "
        "/wiki-push to route the pending items."
    )

    if len(lines) > MAX_LINES:
        lines = lines[: MAX_LINES - 1] + ["  (digest truncated - run /wiki-pull for the full read)"]
    return "\n".join(lines)


def main() -> int:
    try:
        hook_input = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError, OSError):
        hook_input = {}

    project_dir = os.environ.get("CLAUDE_PROJECT_DIR") or hook_input.get("cwd") or ""
    if not project_dir or not Path(project_dir).is_dir():
        return 0

    digest = build_digest(Path(project_dir))
    if not digest:
        return 0

    json.dump(
        {
            "hookSpecificOutput": {
                "hookEventName": "SessionStart",
                "additionalContext": digest,
            }
        },
        sys.stdout,
    )
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)  # fail open
