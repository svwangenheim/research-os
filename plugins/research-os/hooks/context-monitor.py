#!/usr/bin/env python3
"""
PostToolUse hook - progressive context-usage nudges.

Long sessions drift, and the things worth keeping (a decision and why, a
durable finding) are exactly what auto-compaction discards first. This hook
watches approximate context usage and nudges once at each threshold, so the
save happens while the detail still exists rather than after it is gone.

The nudges point at `/checkpoint` and `/wiki-push`, which are where durable
knowledge actually lands in this system: `/checkpoint` persists session state
to `passport.yaml` and the process log, `/wiki-push` routes findings into the
vault. (Pedro Sant'Anna's original nudges at `/learn`; that is the right target
in a workflow whose durable layer is a skills directory, not ours.)

The percentage is a COARSE PROXY. When the hook receives a `transcript_path` we
estimate tokens from the transcript's size against CLAUDE_CONTEXT_WINDOW_TOKENS;
otherwise we fall back to counting tool calls. Neither is exact. Treat it as an
early-warning signal, not a gauge - and note the estimate is deliberately shown
with a "~" everywhere it surfaces.

Also writes the latest estimate to `context-pct.txt` so the status line can
display it without recomputing.

Hook Event: PostToolUse (matcher: Bash|Task)
Output: exit 0 + JSON with `systemMessage` and `additionalContext`.
Fail-open: any error exits 0, silently.
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
import time
from pathlib import Path

SAVE_THRESHOLDS = (40, 55, 65)
THRESHOLD_WARN = 80
THRESHOLD_CRITICAL = 90

# Below the warning threshold, don't recompute more than once a minute.
THROTTLE_SECONDS = 60

DEFAULT_CONTEXT_WINDOW_TOKENS = 1_000_000
DEFAULT_MAX_TOOL_CALLS = 400
APPROX_BYTES_PER_TOKEN = 4.0


def _env_int(name: str, default: int) -> int:
    try:
        value = int(os.environ.get(name, "") or default)
    except ValueError:
        return default
    return value if value > 0 else default


def state_dir() -> Path:
    project_dir = os.environ.get("CLAUDE_PROJECT_DIR", "")
    digest = hashlib.md5(project_dir.encode()).hexdigest()[:8] if project_dir else "default"
    path = Path.home() / ".claude" / "sessions" / digest
    path.mkdir(parents=True, exist_ok=True)
    return path


def read_cache() -> dict:
    try:
        return json.loads((state_dir() / "context-monitor-cache.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def save_cache(data: dict) -> None:
    try:
        (state_dir() / "context-monitor-cache.json").write_text(
            json.dumps(data, indent=2), encoding="utf-8"
        )
    except OSError:
        pass


def estimate_percentage(hook_input: dict) -> float:
    """Approximate context usage, 0-100. Coarse by construction."""
    window = _env_int("CLAUDE_CONTEXT_WINDOW_TOKENS", DEFAULT_CONTEXT_WINDOW_TOKENS)

    transcript = hook_input.get("transcript_path")
    if isinstance(transcript, str) and transcript:
        try:
            approx_tokens = os.path.getsize(transcript) / APPROX_BYTES_PER_TOKEN
            return min(approx_tokens / window * 100, 100)
        except OSError:
            pass

    cache = read_cache()
    calls = cache.get("tool_calls", 0) + 1
    cache["tool_calls"] = calls
    save_cache(cache)
    return min(calls / _env_int("CLAUDE_CONTEXT_MAX_TOOL_CALLS", DEFAULT_MAX_TOOL_CALLS) * 100, 100)


def throttled(percentage: float) -> bool:
    cache = read_cache()
    now = time.time()
    if percentage < THRESHOLD_WARN and (now - cache.get("last_check", 0)) < THROTTLE_SECONDS:
        return True
    cache["last_check"] = now
    save_cache(cache)
    return False


def mark_shown(key: str, value: object = True) -> None:
    cache = read_cache()
    if key == "save":
        shown = cache.get("shown_save", [])
        if value not in shown:
            shown.append(value)
        cache["shown_save"] = shown
    else:
        cache[f"shown_{key}"] = value
    save_cache(cache)


def emit(system_message: str, context: str) -> None:
    json.dump(
        {
            "systemMessage": system_message,
            "hookSpecificOutput": {
                "hookEventName": "PostToolUse",
                "additionalContext": context,
            },
        },
        sys.stdout,
    )


def main() -> int:
    try:
        hook_input = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError, OSError):
        hook_input = {}

    percentage = estimate_percentage(hook_input)

    try:
        (state_dir() / "context-pct.txt").write_text(f"{percentage:.0f}", encoding="utf-8")
    except OSError:
        pass

    if throttled(percentage):
        return 0

    cache = read_cache()
    shown_save = cache.get("shown_save", [])

    for threshold in SAVE_THRESHOLDS:
        if percentage >= threshold and threshold not in shown_save:
            emit(
                f"Context ~{percentage:.0f}% - if a durable finding emerged, "
                f"/checkpoint or /wiki-push it before auto-compaction.",
                f"Context usage is approximately {percentage:.0f}% (coarse proxy). If this "
                f"session produced a decision worth keeping or a finding that belongs in the "
                f"vault, run /checkpoint (session state) or /wiki-push (durable knowledge) "
                f"now - auto-compaction discards the detail that makes them worth writing.",
            )
            mark_shown("save", threshold)
            return 0

    if percentage >= THRESHOLD_CRITICAL and not cache.get("shown_critical"):
        emit(
            f"Context ~{percentage:.0f}% - auto-compact is close. "
            f"Finish the current task at full quality.",
            f"Context ~{percentage:.0f}% (coarse proxy); auto-compaction is approaching. "
            f"Complete the current task without cutting corners or skipping verification. "
            f"Make sure the active plan and the process log are on disk - the PreCompact hook "
            f"captures state, but it cannot reconstruct reasoning that was never written down.",
        )
        mark_shown("critical")
        return 0

    if percentage >= THRESHOLD_WARN and not cache.get("shown_warn"):
        emit(
            f"Context ~{percentage:.0f}% - auto-compact approaching; no rush.",
            f"Context ~{percentage:.0f}% (coarse proxy). Ensure the active plan and the "
            f"process log are current on disk before compaction.",
        )
        mark_shown("warn")
        return 0

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)  # fail open
