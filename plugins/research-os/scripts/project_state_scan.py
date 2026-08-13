#!/usr/bin/env python3
"""
Scan every tracked project's real state, fast, without touching the filesystem
more than necessary.

Why this exists, concretely: the project repos live under OneDrive with
Files-On-Demand. Measured on 2026-08-11, `git status` in the Microsimulation
repo takes 0.7s while a *depth-2* `find` over the same tree takes 3.8s for 68
files -- roughly 20x slower than local, because directory traversal can hydrate
cloud placeholders. An agent exploring nine project roots by globbing is
therefore I/O-bound for minutes and looks hung. The first attempt at a
reach-fixed morning brief did exactly that and blocked for 25 minutes on 2.4
seconds of CPU.

So the scanning is done here, deterministically, using git's own index (fast)
and a handful of reads at known paths (bounded) -- never a recursive glob. The
model then narrates this output instead of discovering it. That is also the
house rule from docs/09: the engine owns the numbers, the model narrates them.

Consumed by: morning-brief, nightly-consolidation, pending-sweep, and the week
dashboard.

Usage:
    python project_state_scan.py --root <vault>
    python project_state_scan.py --root <vault> --format json
    python project_state_scan.py --root <vault> --since midnight
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from resolve_project_paths import (  # noqa: E402  (needs sys.path above)
    ProjectRecord,
    load_projects,
    resolve_brain_root,
)
from wiki_quality_check import force_utf8_console  # noqa: E402

GIT_TIMEOUT = 30  # seconds; OneDrive is slow but git's index is not
DIRTY_SAMPLE = 8


@dataclass
class ProjectState:
    slug: str
    title: str
    role_hint: str
    path: str
    is_git: bool
    branch: str | None = None
    last_commit: str | None = None
    last_commit_date: str | None = None
    last_commit_subject: str | None = None
    dirty_count: int = 0
    dirty_sample: list[str] = field(default_factory=list)
    unpushed_count: int = 0
    has_remote: bool = False
    commits_since: int = 0
    pipeline_stage: str | None = None
    note_updated: str | None = None
    errors: list[str] = field(default_factory=list)


def run_git(path: Path, args: list[str], strip: bool = True) -> str | None:
    """Run a git command in `path`. Returns stdout, or None on failure.

    Never raises: a routine must survive one unreachable or corrupt repo.

    `strip=False` matters for `status --porcelain`, whose format is a
    two-column status field followed by a space -- so an unmodified-in-index
    entry legitimately *begins* with a space (` M path`). Stripping the whole
    output silently eats that leading space on the first line only, which then
    shifts the path slice by one and reports `bmad-output/...` for what is
    really `_bmad-output/...`. A truncated path in a loss-risk report is worse
    than no report.
    """
    try:
        result = subprocess.run(
            # core.quotePath=false keeps umlauts readable: without it git emits
            # `F\303\266rderprogramme` for `Förderprogramme`, and half these
            # repos are German.
            ["git", "-C", str(path), "-c", "core.quotePath=false", *args],
            capture_output=True,
            text=True,
            # Decode as UTF-8 explicitly. With text=True alone Python uses the
            # locale encoding (cp1252 here), which turns git's UTF-8 output into
            # mojibake -- `Förderprogramme` became `FÃ¶rderprogramme`. errors is
            # lenient because a filename must never crash a sweep.
            encoding="utf-8",
            errors="replace",
            timeout=GIT_TIMEOUT,
            check=False,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    if result.returncode != 0:
        return None
    return result.stdout.strip() if strip else result.stdout


def parse_porcelain(output: str) -> list[str]:
    """Extract paths from `git status --porcelain` v1 output.

    Each line is `XY<space>PATH`; renames appear as `PATH -> NEWPATH`, where the
    destination is the one that matters.
    """
    paths: list[str] = []
    for line in output.split("\n"):
        if len(line) < 4:
            continue
        path = line[3:]
        if " -> " in path:
            path = path.split(" -> ", 1)[1]
        paths.append(path.strip().strip('"'))
    return paths


def read_pipeline_stage(path: Path) -> str | None:
    """Read pipeline.current_stage from passport.yaml, if the project has one.

    A direct read at a known path -- no search. Projects on the BMAD workflow
    (Microsimulation, Macro-Fiscal) legitimately have no passport; that is not
    an error and must not be reported as one.
    """
    passport = path / "passport.yaml"
    if not passport.is_file():
        return None
    try:
        for line in passport.read_text(encoding="utf-8", errors="replace").split("\n"):
            stripped = line.strip()
            if stripped.startswith("current_stage:"):
                value = stripped.split(":", 1)[1].strip()
                return value.strip("\"'").split("#")[0].strip()
    except OSError:
        return None
    return None


def infer_role_hint(record: ProjectRecord) -> str:
    """Guess the role from the path. A hint for the audit, not a source of truth.

    The authoritative role lives on procedure notes; this only helps the first
    pass of /workflow-audit group things sensibly before anyone has said so.
    """
    lowered = (record.resolved or "").lower()
    if "sven privat" in lowered or "phd" in lowered:
        return "phd"
    if "dezernat zukunft" in lowered or "bmad-mmm" in lowered:
        return "dz-modelling"
    return "unknown"


def scan_project(record: ProjectRecord, since: str | None) -> ProjectState:
    path = Path(record.resolved) if record.resolved else None
    state = ProjectState(
        slug=record.slug,
        title=record.title,
        role_hint=infer_role_hint(record),
        path=record.resolved or "",
        is_git=record.is_git,
        note_updated=None,
    )

    if path is None or not path.is_dir():
        state.errors.append("path does not exist on this machine")
        return state

    state.pipeline_stage = read_pipeline_stage(path)

    if not record.is_git:
        state.errors.append("not a git repository - no routine can commit or track it")
        return state

    state.branch = run_git(path, ["rev-parse", "--abbrev-ref", "HEAD"])

    log_line = run_git(path, ["log", "-1", "--format=%h%x1f%ad%x1f%s", "--date=short"])
    if log_line and "\x1f" in log_line:
        parts = log_line.split("\x1f")
        state.last_commit, state.last_commit_date, state.last_commit_subject = (
            parts[0],
            parts[1],
            parts[2] if len(parts) > 2 else "",
        )

    porcelain = run_git(path, ["status", "--porcelain"], strip=False)
    if porcelain:
        entries = parse_porcelain(porcelain)
        state.dirty_count = len(entries)
        state.dirty_sample = entries[:DIRTY_SAMPLE]

    remotes = run_git(path, ["remote"])
    state.has_remote = bool(remotes)
    if state.has_remote:
        ahead = run_git(path, ["rev-list", "--count", "@{u}..HEAD"])
        if ahead and ahead.isdigit():
            state.unpushed_count = int(ahead)

    if since:
        recent = run_git(path, ["log", f"--since={since}", "--oneline"])
        state.commits_since = len([ln for ln in (recent or "").split("\n") if ln.strip()])

    return state


def scan_all(brain_root: Path, statuses: tuple[str, ...], since: str | None) -> list[ProjectState]:
    records = [r for r in load_projects(brain_root) if r.status in statuses]
    return [scan_project(record, since) for record in records]


def render(states: list[ProjectState], since: str | None) -> str:
    if not states:
        return "No project notes found."

    lines = ["# Project state", ""]
    for state in states:
        lines.append(f"## {state.title}")
        lines.append(f"  slug: {state.slug}   role(hint): {state.role_hint}")
        lines.append(f"  path: {state.path or '(none recorded)'}")

        if state.errors:
            for err in state.errors:
                lines.append(f"  !! {err}")
            lines.append("")
            continue

        if state.pipeline_stage:
            lines.append(f"  pipeline stage: {state.pipeline_stage}")
        else:
            lines.append("  pipeline stage: (no passport.yaml - not a research-os pipeline project)")

        lines.append(
            f"  branch: {state.branch}   last commit: {state.last_commit} "
            f"({state.last_commit_date}) {state.last_commit_subject}"
        )

        if state.dirty_count:
            sample = ", ".join(state.dirty_sample)
            more = "" if state.dirty_count <= DIRTY_SAMPLE else f" (+{state.dirty_count - DIRTY_SAMPLE} more)"
            lines.append(f"  UNCOMMITTED: {state.dirty_count} file(s) - {sample}{more}")
        if state.unpushed_count:
            lines.append(f"  UNPUSHED: {state.unpushed_count} commit(s) ahead of upstream")
        if not state.has_remote:
            lines.append("  no git remote configured")
        if since:
            lines.append(f"  commits since {since}: {state.commits_since}")
        lines.append("")

    dirty = [s for s in states if s.dirty_count]
    if dirty:
        lines.append("## Loss risk (uncommitted work), worst first")
        for state in sorted(dirty, key=lambda s: -s.dirty_count):
            lines.append(f"  - {state.slug}: {state.dirty_count} file(s)")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    force_utf8_console()
    parser = argparse.ArgumentParser(description="Scan tracked projects' git and pipeline state.")
    parser.add_argument("--root", type=Path, required=True, help="Vault root or _brain directory.")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--status", default="active", help='Statuses to scan, or "all".')
    parser.add_argument(
        "--since",
        help='Also count commits since this git date spec (e.g. "midnight", "7 days ago").',
    )
    args = parser.parse_args(argv)

    brain_root = resolve_brain_root(args.root)
    if not brain_root.is_dir():
        print(f"error: no _brain directory at {brain_root}", file=sys.stderr)
        return 1

    if args.status.strip().lower() == "all":
        statuses = tuple({r.status for r in load_projects(brain_root)})
    else:
        statuses = tuple(s.strip() for s in args.status.split(",") if s.strip())

    states = scan_all(brain_root, statuses, args.since)

    if args.format == "json":
        print(json.dumps([asdict(s) for s in states], indent=2))
    else:
        print(render(states, args.since))
    return 0


if __name__ == "__main__":
    sys.exit(main())
