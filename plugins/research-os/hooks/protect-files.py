#!/usr/bin/env python3
"""
PreToolUse hook - block accidental edits to protected files.

Replaces protect-files.sh, which shelled out to `jq` for JSON parsing. `jq` is
not present by default on Windows, so on a fresh machine the guard failed
silently and every protected file was writable. This version uses the stdlib.

Two other changes, both faithful to the original intent:
  * The modern PreToolUse decision protocol (exit 0 + a `permissionDecision`
    JSON object on stdout) instead of `exit 2` + stderr. Same block, but the
    reason reaches Claude as a structured decision rather than a stray message.
  * Glob patterns are matched with fnmatch, so `strategy-memo-*.md` behaves the
    same way it did under bash's `[[ == ]]`.

The deny-list is intentionally basename-based: these files are single-writer
artifacts (a state ledger, a settings file, a scored report) that should be
updated by the skill that owns them, not edited ad hoc mid-session.

Hook Event: PreToolUse (matcher: Edit|Write|MultiEdit)
Fail-open: any error exits 0 with no decision, i.e. allow.
"""

from __future__ import annotations

import fnmatch
import json
import sys
from pathlib import Path

# Protected basenames. passport.yaml is the single state ledger (it replaced
# clo-author's pipeline-state.json / SESSION_REPORT.md / MEMORY.md), so it is
# guarded the same way settings.json is.
PROTECTED_PATTERNS = (
    "settings.json",
    "passport.yaml",
    "strategy-memo-*.md",
    "referee-report-*.md",
    "quality-score-*.json",
)

FILE_TOOLS = {"Edit", "Write", "MultiEdit"}


def deny(reason: str) -> None:
    """Emit the PreToolUse deny decision."""
    json.dump(
        {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": reason,
            }
        },
        sys.stdout,
    )


def main() -> int:
    try:
        hook_input = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError, OSError):
        return 0

    if hook_input.get("tool_name") not in FILE_TOOLS:
        return 0

    tool_input = hook_input.get("tool_input") or {}
    file_path = tool_input.get("file_path")
    if not isinstance(file_path, str) or not file_path:
        return 0

    basename = Path(file_path).name
    for pattern in PROTECTED_PATTERNS:
        if fnmatch.fnmatch(basename, pattern):
            deny(
                f"Protected file: {basename}. This artifact is owned by the skill that "
                f"produces it - update it through that skill, or remove the pattern from "
                f"hooks/protect-files.py if the protection is no longer wanted."
            )
            return 0

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)  # fail open
