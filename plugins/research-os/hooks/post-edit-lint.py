#!/usr/bin/env python3
"""
PostToolUse hook - mechanical lint of analysis scripts after Write/Edit.

Replaces post-edit-lint.sh, which read `$CLAUDE_TOOL_ARG_FILE_PATH` - a legacy
environment variable Claude Code no longer sets. The old hook therefore never
ran, which meant INV-14 .. INV-19 (rules/content-invariants.md) had no
write-time enforcement at all: violations were only caught later, as
coder-critic deductions. This version parses the hook JSON on stdin, which is
the actual contract.

Scope: R / Python / Julia files under `03_analysis/scripts/`. Templates,
examples and anything inside `.claude/` are skipped - the linter encodes
research-code standards, not plugin-code standards.

Output contract (PostToolUse, exit 0): JSON on stdout carrying a
`systemMessage` (shown to the user) and `hookSpecificOutput.additionalContext`
(injected into Claude's context, so the coder can fix findings immediately
rather than waiting for the critic). Silent when the file lints clean.

Advisory only: this hook never blocks. Fail-open on any error.

Hook Event: PostToolUse (matcher: Write|Edit|MultiEdit)
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

CODE_SUFFIXES = {".R", ".r", ".py", ".jl"}
SCOPE_MARKER = "03_analysis/scripts"

# One report per file per interval; a burst of edits to the same script is one
# nudge, not five.
THROTTLE_SECONDS = 120

SUMMARY_RE = re.compile(
    r"^Total issues:\s+(\d+)\s+\(HIGH:\s*(\d+),\s*MEDIUM:\s*(\d+),\s*LOW:\s*(\d+)\)",
    re.MULTILINE,
)


def state_dir() -> Path:
    """Session-scoped state directory, keyed by project (matches sibling hooks)."""
    project_dir = os.environ.get("CLAUDE_PROJECT_DIR", "")
    digest = hashlib.md5(project_dir.encode()).hexdigest()[:8] if project_dir else "default"
    path = Path.home() / ".claude" / "sessions" / digest
    path.mkdir(parents=True, exist_ok=True)
    return path


def edited_path(hook_input: dict) -> str:
    """The file this tool call wrote, or '' when the call touched no file."""
    tool_input = hook_input.get("tool_input") or {}
    value = tool_input.get("file_path")
    return value if isinstance(value, str) else ""


def in_scope(file_path: str) -> bool:
    """True for analysis scripts only - not plugin code, templates or examples."""
    if Path(file_path).suffix not in CODE_SUFFIXES:
        return False
    normalized = file_path.replace("\\", "/")
    if "/.claude/" in normalized:
        return False
    return SCOPE_MARKER in normalized


def throttled(file_path: str) -> bool:
    """True when this file was already reported inside the throttle window."""
    path = state_dir() / "post-edit-lint-state.json"
    try:
        state = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        state = {}

    now = time.time()
    if now - state.get(file_path, 0) < THROTTLE_SECONDS:
        return True

    state[file_path] = now
    try:
        path.write_text(json.dumps(state), encoding="utf-8")
    except OSError:
        pass
    return False


def run_linter(file_path: str) -> str | None:
    """Run lint-scripts.sh on one file; None when no shell or the run failed."""
    linter = Path(__file__).resolve().parent / "lint-scripts.sh"
    if not linter.is_file():
        return None

    shell = shutil.which("bash") or shutil.which("sh")
    if not shell:
        return None

    try:
        completed = subprocess.run(
            [shell, str(linter), file_path],
            capture_output=True,
            text=True,
            # The linter emits UTF-8 em-dashes; without this Python decodes with
            # the Windows locale codepage and the findings arrive as mojibake.
            encoding="utf-8",
            errors="replace",
            timeout=8,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    return completed.stdout


def parse_counts(report: str) -> tuple[int, int, int, int]:
    """(total, high, medium, low) from the linter's summary block."""
    match = SUMMARY_RE.search(report)
    if not match:
        return (0, 0, 0, 0)
    return tuple(int(group) for group in match.groups())  # type: ignore[return-value]


def findings_only(report: str) -> str:
    """The per-file findings, without the banner and summary scaffolding."""
    lines: list[str] = []
    for line in report.splitlines():
        if line.startswith("=== LINT REPORT") or line.startswith("--- Summary"):
            continue
        if line.startswith(("Files scanned:", "Total issues:", "Status:")):
            continue
        if line.strip():
            lines.append(line)
    return "\n".join(lines)


def main() -> int:
    try:
        hook_input = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError, OSError):
        return 0

    file_path = edited_path(hook_input)
    if not file_path or not in_scope(file_path):
        return 0
    if not Path(file_path).is_file():
        return 0
    if throttled(file_path):
        return 0

    report = run_linter(file_path)
    if not report:
        return 0

    total, high, medium, low = parse_counts(report)
    if total == 0:
        return 0

    name = Path(file_path).name
    detail = findings_only(report)

    json.dump(
        {
            "systemMessage": (
                f"lint: {name} - {total} issue(s) "
                f"(HIGH {high}, MEDIUM {medium}, LOW {low})"
            ),
            "hookSpecificOutput": {
                "hookEventName": "PostToolUse",
                "additionalContext": (
                    f"Mechanical lint of {file_path} found {total} issue(s) against the "
                    f"code invariants in rules/content-invariants.md (INV-14 .. INV-19): "
                    f"HIGH {high}, MEDIUM {medium}, LOW {low}. Fix HIGH findings before "
                    f"moving on - coder-critic deducts for each of these.\n\n{detail}"
                ),
            },
        },
        sys.stdout,
    )
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)  # fail open - a hook bug must never block the session
