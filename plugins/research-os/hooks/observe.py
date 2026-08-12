#!/usr/bin/env python3
"""
Observe sessions so the workflow layer can learn how work actually happens.

Why a hook and not a skill: skills fire when the model judges they should --
roughly 50-80% of the time. Hooks fire every time. Procedure discovery needs the
complete record of what recurs, and a sampled record systematically misses the
boring repeated work that is exactly what should be automated.

Why this is safe to run in a repo governed by AD-5: it does not decide for
itself what to record. Every path goes through `scripts/capture_policy.py`,
which resolves each project's OWN `.claude/settings.json` deny rules BEFORE
anything is opened, treats data-file content as unconditionally forbidden, and
fails closed on any error. This hook never opens a file at all -- it records
tool metadata and the capture verdict, nothing more.

What is recorded, per event:
    timestamp, session id, project id, tool name, the capture verdict, and the
    safe path (which is a `<redacted:reason>` marker whenever the real path
    could itself leak a respondent or wave identifier).

What is never recorded:
    file contents, tool output bodies, or any path the project denies.

Storage: ${XDG_DATA_HOME:-~/.local/share}/ecc-homunculus/projects/<hash>/observations.jsonl
Kept outside ~/.claude so Claude Code's sensitive-path guard does not block writes.

Hook events: PreToolUse, PostToolUse. Always exits 0, always silent.
"""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

try:
    from capture_policy import Capture, decide, find_project_root
except ImportError:  # policy missing -> observe nothing. Never guess.
    Capture = None  # type: ignore[assignment]
    decide = None  # type: ignore[assignment]
    find_project_root = None  # type: ignore[assignment]

MAX_PROMPT_CHARS = 2000
CONFIG_NAME = "observer-config.json"


def data_root() -> Path:
    override = os.environ.get("CLV2_HOMUNCULUS_DIR")
    if override and Path(override).is_absolute():
        return Path(override)
    xdg = os.environ.get("XDG_DATA_HOME")
    base = Path(xdg) if xdg else Path.home() / ".local" / "share"
    return base / "ecc-homunculus"


def observer_enabled(root: Path) -> bool:
    """Off unless explicitly switched on.

    Deliberately opt-in. This writes a durable log of what the user does, in
    repos holding restricted microdata; enabling that must be a decision
    somebody made, never a default that arrived with an update.
    """
    path = root / CONFIG_NAME
    try:
        return bool(json.loads(path.read_text(encoding="utf-8")).get("enabled", False))
    except (OSError, json.JSONDecodeError, AttributeError):
        return False


def project_id(project_root: Path | None) -> tuple[str, str]:
    """(hash, human name). Prefers the git remote so the id is portable."""
    if project_root is None:
        return "global", "global"
    remote = None
    try:
        result = subprocess.run(
            ["git", "-C", str(project_root), "remote", "get-url", "origin"],
            capture_output=True, text=True, timeout=5, check=False,
        )
        if result.returncode == 0 and result.stdout.strip():
            remote = result.stdout.strip()
    except (OSError, subprocess.SubprocessError):
        pass
    key = remote or str(project_root.resolve())
    return hashlib.sha256(key.encode("utf-8")).hexdigest()[:12], project_root.name


def extract_path(payload: dict[str, Any]) -> str:
    tool_input = payload.get("tool_input") or {}
    for key in ("file_path", "path", "notebook_path"):
        if value := tool_input.get(key):
            return str(value)
    return ""


def observe(payload: dict[str, Any]) -> dict[str, Any] | None:
    if decide is None:
        return None

    tool = str(payload.get("tool_name") or "")
    raw_path = extract_path(payload)

    record: dict[str, Any] = {
        "ts": time.time(),
        "event": str(payload.get("hook_event_name") or ""),
        "session": str(payload.get("session_id") or ""),
        "tool": tool,
    }

    if raw_path:
        # Permission resolution happens here, before anything is read -- and
        # nothing in this hook ever reads the file regardless.
        verdict = decide(raw_path)
        record["capture"] = verdict.capture.value
        record["path"] = verdict.safe_path
        record["reason"] = verdict.log_reason

    if (prompt := payload.get("prompt")) and isinstance(prompt, str):
        record["prompt"] = prompt[:MAX_PROMPT_CHARS]

    if command := (payload.get("tool_input") or {}).get("command"):
        # A command line is metadata about the work, but it can name a denied
        # path. Run it through the same policy and drop it if it does.
        text = str(command)
        if decide(text).capture is Capture.REDACTED:
            record["command"] = "<redacted:references-denied-path>"
        else:
            record["command"] = text[:400]

    return record


def append(record: dict[str, Any], root: Path, project_root: Path | None) -> None:
    pid, name = project_id(project_root)
    directory = root / "projects" / pid
    try:
        directory.mkdir(parents=True, exist_ok=True)
        record["project"] = name
        with (directory / "observations.jsonl").open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    except OSError:
        pass


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0
    if not isinstance(payload, dict):
        return 0

    root = data_root()
    if not observer_enabled(root):
        return 0

    record = observe(payload)
    if record is None:
        return 0

    raw_path = extract_path(payload)
    project_root = find_project_root(Path(raw_path)) if raw_path and find_project_root else None
    append(record, root, project_root)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:  # noqa: BLE001 - observation must never cost a session
        sys.exit(0)
