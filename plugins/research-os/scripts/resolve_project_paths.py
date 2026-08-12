#!/usr/bin/env python3
"""
Resolve the on-disk roots of every tracked project from the personal layer.

`vault/_brain/projects/*.md` is the single source of truth for where a project
lives: each note's `working_directory:` frontmatter field. This script turns
those notes into resolved, verified paths so that nothing else -- no scheduled
task, no PowerShell wrapper, no skill -- has to hardcode a path.

Why this exists: two of the three unattended runs before 2026-07-31 could not
reach the project repos at all, because the scheduled tasks only ever saw the
vault. Every routine now derives its `--add-dir` list from here instead.

Usage:
    python resolve_project_paths.py --root <vault>                # --add-dir args
    python resolve_project_paths.py --root <vault> --format list  # one path per line
    python resolve_project_paths.py --root <vault> --format json  # full records

Exit code is 0 even when some projects are unresolvable -- a routine must never
die because one note is missing a path. Pass --strict to exit 1 instead.
Diagnostics always go to stderr so stdout stays machine-consumable.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from wiki_quality_check import parse_frontmatter  # noqa: E402  (needs sys.path above)
from wiki_quality_check import force_utf8_console  # noqa: E402

DEFAULT_STATUSES = ("active",)


@dataclass(frozen=True)
class ProjectRecord:
    """One project note's view of where its work actually lives."""

    slug: str
    title: str
    status: str
    note: str
    declared: str | None
    resolved: str | None
    exists: bool
    is_git: bool
    main_wiki: str | None


def normalize_declared_path(raw: str) -> Path:
    """Turn a frontmatter path into something Path can resolve on this machine.

    Notes are written by hand and by several different skills, so the field
    arrives with either separator style (`c:/Users/...` or `c:\\Users\\...`)
    and sometimes with a trailing slash. Windows accepts forward slashes
    everywhere, so normalizing to them is enough -- no platform branching.
    """
    cleaned = raw.strip().replace("\\", "/").rstrip("/")
    return Path(cleaned).expanduser()


def load_project_note(path: Path) -> ProjectRecord | None:
    """Read one `_brain/projects/*.md` note. Returns None for non-project files."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None

    data, _ = parse_frontmatter(text)
    if data.get("note_type") != "project":
        return None

    declared = data.get("working_directory")
    declared = declared.strip() if isinstance(declared, str) and declared.strip() else None

    resolved: Path | None = None
    exists = False
    is_git = False
    if declared:
        resolved = normalize_declared_path(declared)
        exists = resolved.is_dir()
        is_git = exists and (resolved / ".git").exists()

    return ProjectRecord(
        slug=path.stem,
        title=str(data.get("title") or path.stem),
        status=str(data.get("status") or "unknown"),
        note=str(path),
        declared=declared,
        resolved=str(resolved) if resolved else None,
        exists=exists,
        is_git=is_git,
        main_wiki=data.get("main_wiki") or None,
    )


def load_projects(brain_root: Path) -> list[ProjectRecord]:
    """Load every project note under `_brain/projects/`, sorted by slug."""
    projects_dir = brain_root / "projects"
    if not projects_dir.is_dir():
        return []
    records = [
        record
        for note_path in sorted(projects_dir.glob("*.md"))
        if (record := load_project_note(note_path)) is not None
    ]
    return records


def resolve_brain_root(root: Path) -> Path:
    """Accept either the vault root or `_brain` itself, so callers can be sloppy."""
    if root.name == "_brain":
        return root
    return root / "_brain"


def report_gaps(records: list[ProjectRecord], statuses: tuple[str, ...]) -> list[str]:
    """Human-readable warnings: the reach problems this script exists to expose."""
    warnings: list[str] = []
    for record in records:
        if record.status not in statuses:
            continue
        if not record.declared:
            warnings.append(
                f"{record.slug}: status={record.status} but no working_directory "
                f"-- routines cannot reach it ({record.note})"
            )
        elif not record.exists:
            warnings.append(
                f"{record.slug}: working_directory does not exist on this machine "
                f"-- {record.declared}"
            )
    return warnings


def collapse_nested(paths: list[str]) -> list[str]:
    """Drop any path already covered by an ancestor in the same list.

    Some notes legitimately point at a parent of others -- `new-ideas` indexes
    the whole `Research Ideas` folder that four PhD projects sit inside. Granting
    both the parent and each child is redundant, so for directory-granting
    purposes only the outermost path is kept. Order is preserved.
    """
    resolved = [(p, Path(p).resolve()) for p in paths]
    kept: list[str] = []
    for raw, candidate in resolved:
        covered = any(
            other != candidate and other in candidate.parents for _, other in resolved
        )
        if not covered:
            kept.append(raw)
    return kept


def format_add_dir(records: list[ProjectRecord]) -> str:
    """Emit `--add-dir "<path>"` pairs for the `claude` CLI, space-separated.

    Quoted unconditionally: every real path here contains spaces, and one of
    them contains `e.V.` as well.
    """
    paths = collapse_nested([r.resolved for r in records if r.resolved])
    return " ".join(f'--add-dir "{p}"' for p in paths)


def main(argv: list[str] | None = None) -> int:
    force_utf8_console()
    parser = argparse.ArgumentParser(
        description="Resolve project roots from vault/_brain/projects/*.md frontmatter."
    )
    parser.add_argument(
        "--root",
        type=Path,
        required=True,
        help="Vault root (or the _brain directory itself).",
    )
    parser.add_argument(
        "--format",
        choices=("add-dir", "list", "json"),
        default="add-dir",
        help="Output shape. Default: add-dir, for the scheduled PowerShell wrappers.",
    )
    parser.add_argument(
        "--status",
        default="active",
        help='Comma-separated statuses to include, or "all". Default: active.',
    )
    parser.add_argument(
        "--include-missing",
        action="store_true",
        help="Include projects whose declared path is absent on this machine.",
    )
    parser.add_argument(
        "--collapse",
        action="store_true",
        help="Drop paths already covered by an ancestor (always on for add-dir).",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress the stderr warnings about unreachable projects.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit 1 if any in-scope project is unreachable.",
    )
    args = parser.parse_args(argv)

    brain_root = resolve_brain_root(args.root)
    if not brain_root.is_dir():
        print(f"error: no _brain directory at {brain_root}", file=sys.stderr)
        return 1

    all_records = load_projects(brain_root)
    statuses: tuple[str, ...]
    if args.status.strip().lower() == "all":
        statuses = tuple(sorted({r.status for r in all_records}))
    else:
        statuses = tuple(s.strip() for s in args.status.split(",") if s.strip())

    in_scope = [r for r in all_records if r.status in statuses]
    warnings = report_gaps(in_scope, statuses)

    selected = [r for r in in_scope if r.resolved and (r.exists or args.include_missing)]

    if warnings and not args.quiet:
        for line in warnings:
            print(f"warning: {line}", file=sys.stderr)

    if args.format == "add-dir":
        print(format_add_dir(selected))
    elif args.format == "list":
        paths = [r.resolved for r in selected if r.resolved]
        for path in collapse_nested(paths) if args.collapse else paths:
            print(path)
    else:
        payload = {
            "brain_root": str(brain_root),
            "statuses": list(statuses),
            "projects": [asdict(r) for r in (all_records if args.status == "all" else in_scope)],
            "reachable": [asdict(r) for r in selected],
            "warnings": warnings,
        }
        print(json.dumps(payload, indent=2))

    if args.strict and warnings:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
