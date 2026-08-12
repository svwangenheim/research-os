#!/usr/bin/env python3
"""
Stop hook - write the session record instead of asking someone to.

Replaces `stop-push-nudge.py`, which only printed a reminder. The reminder was
the weak half of the design: the bookkeeping that survives compaction is the
whole point, and making it depend on remembering to type a command means it
happens on the sessions that went smoothly and not on the ones that didn't.
The system does the bookkeeping; you do the research.

On each Stop, when the working tree has changed since the last auto-entry, it
appends a structured entry to `00_admin/process/sessions/YYYY-MM-DD_auto.md`:

  - timestamp and the number of files touched
  - the change-set itself (git status --porcelain, capped)
  - current pipeline stage and integrity state from `passport.yaml`
  - active plan and status from `00_admin/process/plans/`
  - unchecked "to push back" items from `wiki-links.md`

It writes to `00_admin/process/sessions/`, NOT to `journal.md`. Per
rules/logging.md the journal carries one entry per agent invocation with a
score and a verdict; a change-set record is a different thing and would
dilute it. `sessions/` is where logging.md already puts longer per-session
notes.

Throttled on the hash of `git status --porcelain`, so a quiet turn writes
nothing and a burst of edits writes one entry.

Hook Event: Stop
Fail-open: any error exits 0. Never blocks.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

MAX_LISTED_FILES = 30

STAGE_RE = re.compile(r"^\s*current_stage:\s*[\"']?([\w-]+)", re.MULTILINE)
UNRESOLVED_EMPTY_RE = re.compile(r"^\s*unresolved:\s*\[\s*\]\s*$", re.MULTILINE)
UNRESOLVED_ITEMS_RE = re.compile(r"^\s*unresolved:\s*$\n(\s+-\s+\S)", re.MULTILINE)
PLAN_STATUS_RE = re.compile(
    r"^\s*\**\s*status\s*\**\s*:\s*\**\s*(draft|approved|completed|implemented|in[ -]?progress)",
    re.IGNORECASE | re.MULTILINE,
)


def state_dir() -> Path:
    project_dir = os.environ.get("CLAUDE_PROJECT_DIR", "")
    digest = hashlib.md5(project_dir.encode()).hexdigest()[:8] if project_dir else "default"
    path = Path.home() / ".claude" / "sessions" / digest
    path.mkdir(parents=True, exist_ok=True)
    return path


def git(project_dir: str, *args: str) -> str:
    try:
        result = subprocess.run(
            ["git", "-C", project_dir, *args],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=5,
        )
    except (OSError, subprocess.SubprocessError):
        return ""
    return result.stdout if result.returncode == 0 else ""


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


def passport_state(project_dir: Path) -> tuple[str | None, str | None]:
    """(current_stage, integrity summary) from passport.yaml, or (None, None)."""
    passport = find_up(project_dir, "passport.yaml")
    if passport is None:
        return None, None
    try:
        text = passport.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None, None
    match = STAGE_RE.search(text)
    stage = match.group(1) if match else None

    # Absence of an `integrity:` block means the gate has never run, which is
    # not the same as "has unresolved items" - reporting the latter would put a
    # false alarm on every project before its first /peer-review.
    if UNRESOLVED_EMPTY_RE.search(text):
        integrity = "clean"
    elif UNRESOLVED_ITEMS_RE.search(text):
        integrity = "has unresolved items"
    else:
        integrity = None
    return stage, integrity


def active_plan(project_dir: Path) -> str | None:
    plans = project_dir / "00_admin" / "process" / "plans"
    if not plans.is_dir():
        return None
    files = sorted(plans.glob("*.md"), key=lambda f: f.stat().st_mtime, reverse=True)
    for plan in files[:3]:
        try:
            text = plan.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        match = PLAN_STATUS_RE.search(text)
        value = match.group(1).lower() if match else "in-progress"
        if value.startswith(("completed", "implemented")):
            continue
        status = (
            "APPROVED" if value.startswith("approved")
            else "DRAFT" if value.startswith("draft")
            else "in-progress"
        )
        return f"{plan.name} ({status})"
    return None


def unpushed_items(project_dir: Path) -> list[str]:
    """Unchecked `- [ ]` items under the 'To push back' heading of wiki-links.md."""
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
            if item and not item.startswith("<"):  # skip the template placeholder
                items.append(item)
    return items


def main() -> int:
    try:
        hook_input = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError, OSError):
        hook_input = {}

    if hook_input.get("stop_hook_active"):
        return 0  # don't recurse

    project_dir = os.environ.get("CLAUDE_PROJECT_DIR") or hook_input.get("cwd") or ""
    if not project_dir or not Path(project_dir).is_dir():
        return 0

    status = git(project_dir, "status", "--porcelain")
    if not status.strip():
        return 0  # nothing changed, nothing to record

    status_hash = hashlib.md5(status.encode()).hexdigest()
    state_path = state_dir() / "session-journal-state.json"
    try:
        previous = json.loads(state_path.read_text(encoding="utf-8")).get("last_hash")
    except (OSError, ValueError):
        previous = None
    if status_hash == previous:
        return 0  # this exact change-set is already recorded

    root = Path(project_dir)
    sessions = root / "00_admin" / "process" / "sessions"
    try:
        sessions.mkdir(parents=True, exist_ok=True)
    except OSError:
        return 0

    today = datetime.now().strftime("%Y-%m-%d")
    log_file = sessions / f"{today}_auto.md"
    is_new = not log_file.exists()

    changed = [line for line in status.splitlines() if line.strip()][:MAX_LISTED_FILES]
    stage, integrity = passport_state(root)
    plan = active_plan(root)
    pending = unpushed_items(root)

    lines: list[str] = []
    if is_new:
        lines.append(f"# Session Log - {today} (auto)\n")
        lines.append(
            "_Written by the Stop hook on each meaningful change-set. Narrative notes and "
            "decisions belong alongside this, in `journal.md` or a handoff note - this file "
            "records what changed, not why._\n"
        )
    lines.append(f"\n## {datetime.now().strftime('%H:%M')} - {len(changed)} file(s) touched")
    if stage:
        header = f"\n**Stage:** {stage}"
        if integrity:
            header += f"  |  **Integrity:** {integrity}"
        lines.append(header)
    if plan:
        lines.append(f"\n**Active plan:** {plan}")
    lines.append("\n**Changed:**")
    lines.extend(f"- `{line.strip()}`" for line in changed)
    if pending:
        lines.append(f"\n**Unpushed durable knowledge ({len(pending)}):**")
        lines.extend(f"- {item[:100]}" for item in pending[:5])
        lines.append("\nRun `/wiki-push` to route them.")
    lines.append("")

    try:
        with open(log_file, "a", encoding="utf-8") as handle:
            handle.write("\n".join(lines) + "\n")
    except OSError:
        return 0

    try:
        state_path.write_text(json.dumps({"last_hash": status_hash}), encoding="utf-8")
    except OSError:
        pass

    note = f"[session-journal] {len(changed)} change(s) -> {log_file.name}"
    if pending:
        note += f"; {len(pending)} item(s) awaiting /wiki-push"
    sys.stderr.write(note + "\n")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)  # fail open
