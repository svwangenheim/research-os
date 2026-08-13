#!/usr/bin/env python3
"""
Claude Code status line for research-os projects.

Claude Code pipes a JSON session snapshot to stdin and renders whatever this
prints. The two fields worth having that no generic status line carries are the
pipeline stage and the integrity-gate state - the two things you would
otherwise run `/research-os-help` to learn.

Renders:
    [MODE]  model  @ branch +N  stage:analysis  gate:PASS  ctx 42%

Every field degrades independently: outside a research-os project the stage and
gate fields simply disappear, and a probe that fails is omitted rather than
rendered as an error. A status line that breaks the prompt is worse than no
status line, so the whole body is defensive and the fallback is a bare model
name.

Wire it up in ~/.claude/settings.json:

    "statusLine": {
      "type": "command",
      "command": "python \"C:/.../plugins/research-os/scripts/statusline.py\""
    }
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

MODE_BADGES = {
    "bypassPermissions": "BYPASS",
    "acceptEdits": "AUTO-EDIT",
    "plan": "PLAN",
    "default": "PROMPT",
    "auto": "AUTO",
    "dontAsk": "DONT-ASK",
}

STAGE_RE = re.compile(r"^\s*current_stage:\s*[\"']?([\w-]+)", re.MULTILINE)
UNRESOLVED_EMPTY_RE = re.compile(r"^\s*unresolved:\s*\[\s*\]\s*$", re.MULTILINE)
UNRESOLVED_ITEMS_RE = re.compile(r"^\s*unresolved:\s*$\n(\s+-\s+\S)", re.MULTILINE)


def git(cwd: str, *args: str) -> str:
    try:
        result = subprocess.run(
            ["git", "-C", cwd, *args],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=3,
        )
    except (OSError, subprocess.SubprocessError):
        return ""
    return result.stdout.strip() if result.returncode == 0 else ""


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


def project_fields(cwd: str) -> list[str]:
    """Pipeline stage and integrity state, when inside a research-os project."""
    passport = find_up(Path(cwd), "passport.yaml")
    if passport is None:
        return []
    try:
        text = passport.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return []

    fields: list[str] = []
    match = STAGE_RE.search(text)
    if match:
        fields.append(f"stage:{match.group(1)}")

    if UNRESOLVED_EMPTY_RE.search(text):
        fields.append("gate:clean")
    elif UNRESOLVED_ITEMS_RE.search(text):
        fields.append("gate:BLOCKED")
    return fields


def context_field() -> str | None:
    """Context estimate, written by hooks/context-monitor.py."""
    project_dir = os.environ.get("CLAUDE_PROJECT_DIR", "")
    digest = hashlib.md5(project_dir.encode()).hexdigest()[:8] if project_dir else "default"
    path = Path.home() / ".claude" / "sessions" / digest / "context-pct.txt"
    try:
        value = path.read_text(encoding="utf-8").strip()
    except OSError:
        return None
    return f"ctx {value}%" if value.isdigit() else None


def main() -> int:
    try:
        snapshot = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError, OSError):
        snapshot = {}

    mode = snapshot.get("permission_mode") or "?"
    model = (snapshot.get("model") or {}).get("display_name") or "?"
    cwd = (snapshot.get("workspace") or {}).get("current_dir") or os.getcwd()

    parts = [f"[{MODE_BADGES.get(mode, mode)}]", model]

    branch = git(cwd, "branch", "--show-current")
    if branch:
        field = f"@ {branch}"
        dirty = git(cwd, "status", "--porcelain")
        count = len([line for line in dirty.splitlines() if line.strip()])
        if count:
            field += f" +{count}"
        parts.append(field)

    parts.extend(project_fields(cwd))

    context = context_field()
    if context:
        parts.append(context)

    sys.stdout.write("  ".join(parts))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        # Never break the prompt.
        sys.stdout.write("[research-os]")
        sys.exit(0)
