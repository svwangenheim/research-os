#!/usr/bin/env python3
"""
Find everything across every project that is waiting to be committed, pushed, or
pushed back into the wiki -- and report it. This script never acts.

The split matters: **detection is autonomous, mutation is consented.** This
half sweeps and writes a queue; `/pending` presents that queue grouped by
project, asks once per project per action class, and records the answer in
`_brain/automation-consent.yaml` so it is never asked again for that project.

Action classes:
    commit     uncommitted changes in the working tree
    push       local commits ahead of an upstream
    wiki_push  unchecked "to push back" items in a project's wiki-links.md
    wiki_fix   findings from wiki_quality_check.py

Consent values: granted | ask | denied. Absent means ask.

Usage:
    python pending_actions.py --root <vault>              # write the queue
    python pending_actions.py --root <vault> --format json
    python pending_actions.py --root <vault> --dry-run    # print, write nothing
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))

from project_state_scan import ProjectState, scan_all  # noqa: E402
from wiki_quality_check import force_utf8_console  # noqa: E402

QUEUE_FILE = ".pending-actions.yaml"
CONSENT_FILE = "automation-consent.yaml"
ACTION_CLASSES = ("commit", "push", "wiki_push", "wiki_fix")
WIKI_LINKS_SCAN_DEPTH = 2  # project root and one level down; never a deep walk


@dataclass
class PendingItem:
    project: str
    action: str
    count: int
    detail: str
    consent: str = "ask"
    sample: list[str] = field(default_factory=list)


def load_consent(brain_root: Path) -> dict[str, dict[str, str]]:
    """Parse the consent ledger.

    Deliberately a tiny hand-rolled parser rather than a YAML dependency: the
    file's shape is fixed (project -> action -> value) and the engine stays
    stdlib-only. Anything unparseable degrades to `ask`, which is the safe
    direction -- a corrupt ledger must never silently grant.
    """
    path = brain_root / CONSENT_FILE
    if not path.is_file():
        return {}
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").split("\n")
    except OSError:
        return {}

    consent: dict[str, dict[str, str]] = {}
    current: str | None = None
    for line in lines:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        indent = len(line) - len(line.lstrip())
        stripped = line.strip()
        if not stripped.endswith(":") and ":" not in stripped:
            continue
        key, _, value = stripped.partition(":")
        key, value = key.strip(), value.strip().strip("\"'")
        if indent == 0 and not value:
            if key == "projects":
                continue
            current = key
            consent.setdefault(current, {})
        elif indent <= 2 and not value and key != "projects":
            current = key
            consent.setdefault(current, {})
        elif current and key in ACTION_CLASSES:
            consent[current][key] = value if value in ("granted", "ask", "denied") else "ask"
    return consent


def find_wiki_links(project_path: Path) -> list[Path]:
    """Locate wiki-links.md at the project root or one level down.

    Bounded on purpose: these repos are on OneDrive, where a recursive glob is
    slow enough to stall a routine.
    """
    found: list[Path] = []
    root_file = project_path / "wiki-links.md"
    if root_file.is_file():
        found.append(root_file)
    for child in project_path.iterdir() if project_path.is_dir() else []:
        if child.is_dir() and not child.name.startswith("."):
            candidate = child / "wiki-links.md"
            if candidate.is_file():
                found.append(candidate)
    return found


def unchecked_pushback_items(path: Path) -> list[str]:
    """Unchecked `- [ ]` items under a 'to push back' heading."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return []
    items: list[str] = []
    in_section = False
    for line in text.split("\n"):
        stripped = line.strip()
        if stripped.startswith("## "):
            in_section = "push back" in stripped.lower()
            continue
        if in_section and stripped.startswith("- [ ]"):
            item = stripped[5:].strip()
            if item and not item.startswith("<"):
                items.append(item)
    return items


def sweep(states: list[ProjectState], consent: dict[str, dict[str, str]]) -> list[PendingItem]:
    items: list[PendingItem] = []

    # A wiki-links.md belongs to exactly one project. `new-ideas` points at the
    # `Research Ideas` folder that four PhD projects live inside, so a naive
    # scan attributes each child's file to the parent as well and double-counts
    # every pending item. Deepest path wins: the most specific project owns it.
    claimed: set[Path] = set()
    by_depth = sorted(
        states, key=lambda s: len(Path(s.path).parts) if s.path else 0, reverse=True
    )

    for state in by_depth:
        project_consent = consent.get(state.slug, {})

        if state.dirty_count:
            items.append(
                PendingItem(
                    project=state.slug,
                    action="commit",
                    count=state.dirty_count,
                    detail=f"{state.dirty_count} uncommitted file(s) on {state.branch}",
                    consent=project_consent.get("commit", "ask"),
                    sample=state.dirty_sample,
                )
            )

        if state.unpushed_count:
            items.append(
                PendingItem(
                    project=state.slug,
                    action="push",
                    count=state.unpushed_count,
                    detail=f"{state.unpushed_count} commit(s) ahead of upstream",
                    consent=project_consent.get("push", "ask"),
                )
            )

        if state.path and Path(state.path).is_dir():
            for links in find_wiki_links(Path(state.path)):
                resolved = links.resolve()
                if resolved in claimed:
                    continue
                claimed.add(resolved)
                pending = unchecked_pushback_items(links)
                if pending:
                    items.append(
                        PendingItem(
                            project=state.slug,
                            action="wiki_push",
                            count=len(pending),
                            detail=f"{len(pending)} unpushed item(s) in {links.name}",
                            consent=project_consent.get("wiki_push", "ask"),
                            sample=pending[:5],
                        )
                    )

    return items


def render_queue(items: list[PendingItem], stamp: str) -> str:
    """The queue file. YAML-shaped and human-readable -- it gets reviewed."""
    lines = [
        "# Pending actions across all tracked projects.",
        "# Written by pending_actions.py; consumed by /pending. Detection only --",
        "# nothing here has been acted on. Consent lives in automation-consent.yaml.",
        f"swept_at: \"{stamp}\"",
        f"total: {len(items)}",
        "items:",
    ]
    if not items:
        lines.append("  []  # nothing pending")
        return "\n".join(lines) + "\n"

    for item in items:
        lines.append(f"  - project: \"{item.project}\"")
        lines.append(f"    action: {item.action}")
        lines.append(f"    count: {item.count}")
        lines.append(f"    consent: {item.consent}")
        lines.append(f"    detail: \"{item.detail}\"")
        if item.sample:
            lines.append("    sample:")
            lines.extend(f"      - \"{s}\"" for s in item.sample)
    return "\n".join(lines) + "\n"


def render_report(items: list[PendingItem]) -> str:
    if not items:
        return "Nothing pending across any tracked project."

    by_project: dict[str, list[PendingItem]] = {}
    for item in items:
        by_project.setdefault(item.project, []).append(item)

    lines = [f"# Pending actions ({len(items)} across {len(by_project)} project(s))", ""]
    for project in sorted(by_project, key=lambda p: -sum(i.count for i in by_project[p])):
        lines.append(f"## {project}")
        for item in by_project[project]:
            marker = {"granted": "[granted]", "denied": "[denied] ", "ask": "[ask]    "}[item.consent]
            lines.append(f"  {marker} {item.action}: {item.detail}")
            for sample in item.sample[:3]:
                lines.append(f"             - {sample}")
        lines.append("")

    to_ask = sorted({i.project for i in items if i.consent == "ask"})
    if to_ask:
        lines.append(f"Needs a consent decision: {', '.join(to_ask)}")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    force_utf8_console()
    parser = argparse.ArgumentParser(description="Sweep for pending actions. Never acts.")
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--dry-run", action="store_true", help="Print only; do not write the queue.")
    args = parser.parse_args(argv)

    brain_root = args.root if args.root.name == "_brain" else args.root / "_brain"
    if not brain_root.is_dir():
        print(f"error: no _brain directory at {brain_root}", file=sys.stderr)
        return 1

    states = scan_all(brain_root, ("active",), since=None)
    consent = load_consent(brain_root)
    items = sweep(states, consent)
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    if not args.dry_run:
        (brain_root / QUEUE_FILE).write_text(render_queue(items, stamp), encoding="utf-8")

    if args.format == "json":
        print(json.dumps({"swept_at": stamp, "items": [asdict(i) for i in items]}, indent=2))
    else:
        print(render_report(items))
        if not args.dry_run:
            print(f"\nQueue written to {brain_root / QUEUE_FILE}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
