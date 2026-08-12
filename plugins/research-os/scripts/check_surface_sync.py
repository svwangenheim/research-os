#!/usr/bin/env python3
"""
check_surface_sync.py - keep the documentation's picture of the plugin honest.

Every README that says "43 skills" or lists one table row per agent is a claim
about disk. Those claims drift the moment something is added or retired, and
they drift silently, because nothing reads them. Disk is the ground truth here;
the prose is checked against it.

Two checks:

  1. Count assertions. Any "N skills", "N specialized agents", "N-rule
     backbone" phrasing in the tracked README files must match the number of
     files on disk. Counts stated about an upstream project (clo-author's
     13-rule backbone, engram's agents) are about someone else's tree and are
     skipped - see UPSTREAM_MARKERS.
  2. Enumerative table rows. A markdown table introduced by
     `<!-- surface-sync-table: skills -->` must carry exactly one data row per
     skill on disk. Missing and extra rows are reported by name. This is the
     drift a count check cannot see: the total stays right while the rows say
     something else.

Ground truth:
    skills  plugins/research-os/skills/*/SKILL.md
    agents  plugins/research-os/agents/*.md      (README.md excluded)
    rules   plugins/research-os/rules/*.md       (README.md excluded)
    hooks   plugins/research-os/hooks/*.py + *.sh

Usage:
    python check_surface_sync.py [--repo-root PATH] [--verbose]

Exit codes:
    0  documentation matches disk
    1  drift
    2  the script itself failed
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import NamedTuple

SURFACES = ("skills", "agents", "rules", "hooks")

# READMEs whose count assertions and tables are enforced.
TRACKED_DOCS = (
    "README.md",
    "plugins/research-os/README.md",
    "plugins/research-os/skills/README.md",
    "plugins/research-os/rules/README.md",
    "plugins/research-os/hooks/README.md",
)

SINGULAR = {"skills": "skill", "agents": "agent", "rules": "rule", "hooks": "hook"}
PLURAL = {value: key for key, value in SINGULAR.items()}

# "43 skills", "27 specialized agents", "the plugin's 12 hook scripts".
COUNT_RE = re.compile(
    r"\b(?P<n>\d+)\s+(?P<filler>(?:[A-Za-z][\w'-]*\s+){0,2})"
    r"(?P<noun>skills?|agents?|rules?|hooks?)\b"
)
# "clo-author's 13-rule backbone", "a 7-hook harness".
HYPHEN_COUNT_RE = re.compile(r"\b(?P<n>\d+)-(?P<noun>skill|agent|rule|hook)\b")

# A count sitting next to one of these is a statement about another project's
# tree, not about ours.
UPSTREAM_MARKERS = re.compile(
    r"\b(clo-author|pedro|pedrohcgs|hugo|upstream|engram|ARS|academic-research-skills"
    r"|obsidian-second-brain|his|her|their)\b",
    re.IGNORECASE,
)
LOOKBACK_CHARS = 60

TABLE_MARKER_RE = re.compile(r"<!--\s*surface-sync-table:\s*(\w+)\s*-->")
FENCE_RE = re.compile(r"^\s*(```+|~~~+)")


class Issue(NamedTuple):
    doc: str
    line: int
    message: str


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def strip_fenced_blocks(text: str) -> str:
    """Blank out fenced code blocks, preserving line numbers."""
    out: list[str] = []
    fence: str | None = None
    for line in text.splitlines():
        match = FENCE_RE.match(line)
        if fence is None:
            if match:
                fence = match.group(1)[:3]
                out.append("")
                continue
            out.append(line)
        else:
            if match and match.group(1).startswith(fence):
                fence = None
            out.append("")
    return "\n".join(out)


# --- Ground truth -----------------------------------------------------------


def inventory(plugin_root: Path) -> dict[str, list[str]]:
    """The names on disk, per surface, sorted."""
    skills = sorted(p.parent.name for p in plugin_root.glob("skills/*/SKILL.md"))
    agents = sorted(p.stem for p in plugin_root.glob("agents/*.md") if p.name != "README.md")
    rules = sorted(p.stem for p in plugin_root.glob("rules/*.md") if p.name != "README.md")
    hooks = sorted(
        p.name
        for p in list(plugin_root.glob("hooks/*.py")) + list(plugin_root.glob("hooks/*.sh"))
    )
    return {"skills": skills, "agents": agents, "rules": rules, "hooks": hooks}


# --- Check 1: count assertions ----------------------------------------------


def is_upstream_context(text: str, start: int) -> bool:
    """
    Whose tree is this count about? Only text earlier on the same line counts:
    an upstream mentioned in the previous sentence says nothing about the next
    one, and treating it as scope would silently swallow real drift.
    """
    line_start = text.rfind("\n", 0, start) + 1
    window = text[max(line_start, start - LOOKBACK_CHARS) : start]
    return bool(UPSTREAM_MARKERS.search(window))


def line_of(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def check_counts(doc_path: Path, rel: str, counts: dict[str, int]) -> list[Issue]:
    issues: list[Issue] = []
    text = strip_fenced_blocks(read_text(doc_path))

    for match in COUNT_RE.finditer(text):
        noun = match.group("noun")
        surface = noun if noun in counts else PLURAL.get(noun)
        if surface is None or is_upstream_context(text, match.start()):
            continue
        stated = int(match.group("n"))
        if stated != counts[surface]:
            issues.append(
                Issue(
                    rel,
                    line_of(text, match.start()),
                    f'"{match.group(0).strip()}" but disk has {counts[surface]} {surface}',
                )
            )

    for match in HYPHEN_COUNT_RE.finditer(text):
        surface = PLURAL[match.group("noun")]
        if is_upstream_context(text, match.start()):
            continue
        stated = int(match.group("n"))
        if stated != counts[surface]:
            issues.append(
                Issue(
                    rel,
                    line_of(text, match.start()),
                    f'"{match.group(0)}" but disk has {counts[surface]} {surface}',
                )
            )
    return issues


# --- Check 2: enumerative table rows ----------------------------------------


def cell_name(cell: str) -> str:
    """The item name inside a table cell, stripped of markdown decoration."""
    value = cell.strip()
    value = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", value)  # links
    value = value.replace("`", "").replace("*", "")
    return value.strip().strip("/").strip()


def normalise(name: str, surface: str) -> str:
    """Compare a documented name against a disk name on equal terms."""
    value = name.strip().lower()
    if surface == "hooks":
        return value
    value = value.removesuffix(".md").removesuffix(".py").removesuffix(".sh")
    return value.strip("/")


def table_after(lines: list[str], start: int) -> tuple[list[str], int]:
    """
    The first markdown table at or after `start`; returns (data rows, end).
    Prose between the marker and the table is skipped over, so a marker can
    carry an introductory sentence.
    """
    index = start
    while index < len(lines) and not lines[index].lstrip().startswith("|"):
        index += 1
    rows: list[str] = []
    while index < len(lines) and lines[index].lstrip().startswith("|"):
        rows.append(lines[index])
        index += 1
    if len(rows) < 2:
        return [], index
    return rows[2:], index  # drop the header row and the separator


def check_tables(doc_path: Path, rel: str, disk: dict[str, list[str]]) -> tuple[list[Issue], int]:
    text = strip_fenced_blocks(read_text(doc_path))
    lines = text.splitlines()
    issues: list[Issue] = []
    tables = 0

    for number, line in enumerate(lines):
        marker = TABLE_MARKER_RE.search(line)
        if not marker:
            continue
        surface = marker.group(1)
        if surface not in disk:
            issues.append(
                Issue(rel, number + 1, f"unknown surface-sync-table surface `{surface}`")
            )
            continue
        tables += 1
        rows, _ = table_after(lines, number + 1)
        if not rows:
            issues.append(
                Issue(rel, number + 1, f"`{surface}` table marker with no table under it")
            )
            continue

        documented = {
            normalise(cell_name(row.strip().strip("|").split("|")[0]), surface)
            for row in rows
            if row.strip().strip("|").split("|")[0].strip()
        }
        expected = {normalise(name, surface) for name in disk[surface]}
        for missing in sorted(expected - documented):
            issues.append(Issue(rel, number + 1, f"`{surface}` table is missing `{missing}`"))
        for extra in sorted(documented - expected):
            issues.append(
                Issue(rel, number + 1, f"`{surface}` table lists `{extra}`, which is not on disk")
            )
    return issues, tables


# --- Driver -----------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass

    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument(
        "--repo-root",
        type=str,
        default=str(Path(__file__).resolve().parents[3]),
        help="Repository root (defaults to the tree this script ships in).",
    )
    parser.add_argument(
        "--verbose", action="store_true", help="Also report documents that matched."
    )
    args = parser.parse_args(argv)

    repo_root = Path(args.repo_root).expanduser().resolve()
    plugin_root = repo_root / "plugins" / "research-os"
    if not plugin_root.is_dir():
        print(f"plugin not found under {repo_root}", file=sys.stderr)
        return 2

    disk = inventory(plugin_root)
    counts = {surface: len(names) for surface, names in disk.items()}
    print("on disk: " + "  ".join(f"{counts[s]} {s}" for s in SURFACES))

    issues: list[Issue] = []
    tables_seen = 0
    for rel in TRACKED_DOCS:
        doc_path = repo_root / rel
        if not doc_path.is_file():
            print(f"  [skip] {rel} (not present)")
            continue
        try:
            found = check_counts(doc_path, rel, counts)
            table_issues, tables = check_tables(doc_path, rel, disk)
        except OSError as exc:
            print(f"  [skip] {rel} ({exc})")
            continue
        issues += found + table_issues
        tables_seen += tables
        if args.verbose and not found and not table_issues:
            print(f"  [ok] {rel}")

    if tables_seen == 0:
        print(
            "\nnote: no `<!-- surface-sync-table: ... -->` markers found. Row parity is "
            "unenforced until the READMEs carry them."
        )

    if not issues:
        print("\nsurface sync: PASS")
        return 0

    print(f"\nsurface sync: FAIL ({len(issues)})")
    for issue in sorted(issues):
        print(f"  {issue.doc}:{issue.line}: {issue.message}")
    return 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:  # noqa: BLE001 - a checker crash is exit 2, not a traceback
        print(f"check_surface_sync.py failed: {exc}", file=sys.stderr)
        sys.exit(2)
