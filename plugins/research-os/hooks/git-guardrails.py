#!/usr/bin/env python3
"""
PreToolUse hook - always-on guardrails for destructive git and hardcoded paths.

Complements `session-guard.py`, which enforces `/careful` and `/freeze`. Those
are opt-in and session-scoped: you have to remember to turn them on. This hook
is unconditional, and deliberately covers a narrower set - only operations that
destroy work irrecoverably, plus one convention (blanket staging) that is how
raw data and credentials usually end up in a commit.

Two checks, by tool:

  Bash - deny destructive git:
    git reset --hard          discards uncommitted work with no recovery
    git clean -f / -fd / -fdx deletes UNTRACKED files, including data not yet committed
    git push --force          rewrites remote history (--force-with-lease is allowed)
    git add -A / --all / .    blanket staging; how data and secrets get committed
    git checkout|restore -- . mass discard of working-tree changes

  Write/Edit/MultiEdit - hardcoded machine paths in analysis code:
    An absolute home path (/Users/x, /home/x, C:\\Users\\x) written into a
    .R/.py/.jl/.do/.Rmd/.qmd file breaks the replication package. This is
    INV-16 in rules/content-invariants.md, which until now was only enforced
    after the fact as a coder-critic deduction. Warn by default; set
    RESEARCH_OS_STRICT_PATHS=1 to deny outright (recommended while working in
    restricted-data directories - see rules/confidential-data.md).

Bypass: run the command yourself in a terminal outside Claude Code. That is
deliberate - the guard should cost a deliberate action, not a flag.

Hook Event: PreToolUse (matcher: Bash|Write|Edit|MultiEdit)
Protocol: exit 0 + a `permissionDecision` object on stdout.
Fail-open: any error exits 0 with no decision, i.e. allow.
"""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

# Optional git GLOBAL options that can sit between `git` and the subcommand:
# `git -C <dir>`, `git -c k=v`, `--git-dir=`, `--work-tree=`, `--no-pager`.
# Without this prefix, `git -C /repo reset --hard` bypasses every rule below.
_GLOBAL_OPTS = (
    r"(?:-C\s+\S+\s+|-c\s+\S+\s+|--git-dir(?:=\S+\s+|\s+\S+\s+)|"
    r"--work-tree(?:=\S+\s+|\s+\S+\s+)|--no-pager\s+|--paginate\s+|-p\s+)*"
)

# (pattern, what it does, what to do instead)
GIT_DENY: tuple[tuple[re.Pattern[str], str, str], ...] = (
    (
        re.compile(r"\bgit\s+" + _GLOBAL_OPTS + r"reset\s+--hard\b"),
        "git reset --hard discards uncommitted work irrecoverably.",
        "Use `git stash` (recoverable), or reset specific paths.",
    ),
    (
        re.compile(r"\bgit\s+" + _GLOBAL_OPTS + r"clean\b.*(--force\b|(?<![\w-])-[a-z]*f)"),
        "git clean -f deletes UNTRACKED files - including data and outputs not yet committed.",
        "Inspect with `git clean -n` first, then delete specific paths by hand.",
    ),
    (
        re.compile(r"\bgit\s+" + _GLOBAL_OPTS + r"push\b.*(--force(?![\w-])|(?<!-)\s-f\b)"),
        "git push --force clobbers remote history.",
        "Use `git push --force-with-lease` if you genuinely must rewrite a branch.",
    ),
    (
        re.compile(r"\bgit\s+" + _GLOBAL_OPTS + r"add\s+(?:--\s+)?(-A\b|--all\b|\.(?:\s|$)|:/)"),
        "Blanket staging (git add -A / . / :/) can stage raw data, credentials, "
        "or local settings.",
        "Stage specific files: `git add path/to/file ...`.",
    ),
    (
        re.compile(r"\bgit\s+" + _GLOBAL_OPTS + r"(checkout|restore)\s+(--\s+)?\.(?:\s|$)"),
        "Mass discard of working-tree changes is irreversible.",
        "Discard specific files, or `git stash` to keep them recoverable.",
    ),
)

HARDCODED_PATH = re.compile(
    r"(/Users/[^/\s'\")]+|/home/[^/\s'\")]+|[A-Za-z]:\\{1,2}Users\\{1,2}[^\\\s'\"]+)"
)

# Analysis-code extensions only. Plugin code, docs and notebooks are out of scope:
# a hardcoded path in a hook is a machine detail, in an analysis script it is a
# replication failure.
CODE_SUFFIXES = {".R", ".r", ".py", ".jl", ".do", ".Rmd", ".qmd"}

FILE_TOOLS = {"Write", "Edit", "MultiEdit"}


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


def written_strings(tool_input: dict) -> list[str]:
    """Every string this call would turn into file content.

    Write carries `content`, Edit carries `new_string`, and MultiEdit carries a
    list of edits each with its own `new_string`. Checking only the first two
    silently misses every MultiEdit.
    """
    out: list[str] = []
    for key in ("content", "new_string"):
        value = tool_input.get(key)
        if isinstance(value, str):
            out.append(value)
    for edit in tool_input.get("edits") or []:
        value = (edit or {}).get("new_string")
        if isinstance(value, str):
            out.append(value)
    return out


def check_bash(command: str) -> bool:
    """Deny destructive git. Returns True when a decision was emitted."""
    for pattern, reason, alternative in GIT_DENY:
        if pattern.search(command):
            deny(
                f"Blocked by git-guardrails: {reason} {alternative} "
                f"(To override, run it yourself in a terminal outside Claude Code.)"
            )
            return True
    return False


def check_write(tool_input: dict) -> bool:
    """Warn or deny on hardcoded machine paths. True when a decision was emitted."""
    file_path = tool_input.get("file_path")
    if not isinstance(file_path, str) or Path(file_path).suffix not in CODE_SUFFIXES:
        return False

    for content in written_strings(tool_input):
        match = HARDCODED_PATH.search(content)
        if not match:
            continue
        message = (
            f"Hardcoded machine path '{match.group(0)}' in {Path(file_path).name} "
            f"breaks the replication package (INV-16). Use here() in R, "
            f"pathlib.Path in Python, joinpath(@__DIR__, ...) in Julia, or a "
            f"config variable."
        )
        if os.environ.get("RESEARCH_OS_STRICT_PATHS") == "1":
            deny(f"Blocked (RESEARCH_OS_STRICT_PATHS=1): {message}")
            return True
        sys.stderr.write(f"[git-guardrails] WARNING: {message}\n")
        return False  # one finding per call is enough
    return False


def main() -> int:
    try:
        hook_input = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError, OSError):
        return 0

    tool = hook_input.get("tool_name", "")
    tool_input = hook_input.get("tool_input") or {}

    if tool == "Bash":
        command = tool_input.get("command")
        if isinstance(command, str) and command:
            check_bash(command)
        return 0

    if tool in FILE_TOOLS:
        check_write(tool_input)
        return 0

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)  # fail open
