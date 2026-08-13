#!/usr/bin/env python3
"""
R2 -- "whenever new data is included, ask before touching it, and remember
the ruling." A real gate, unlike the ambient dialogue triggers: it can
actually block a tool call, not just nudge.

Two halves, one file, dispatched on hook_event_name:

  PreToolUse (Read|Glob|Grep) -- classify the target path via
    capture_policy.py (the same classifier that gates the observation layer
    and passes the AD-5 canary). A data-file extension or a path the
    project's own deny-list covers, not yet in the read-consent ledger,
    returns permissionDecision: "ask" -- a REAL permission prompt shown to
    the human, not a conversational guess by Claude. Code and markdown are
    never touched by this gate at all.

  PostToolUse (same matcher) -- if a gated path's tool call actually
    succeeded, that only happened because the human approved the PreToolUse
    "ask" (or it was already allowed some other way). Record "granted" for
    that path's containing directory, scoped to the project, so the SAME
    directory never asks again. This is what makes "remember the ruling"
    real rather than a hope about how permission caching behaves -- the
    ledger is this script's own, read and written only here.

A denied prompt fires no PostToolUse (the tool never ran), so nothing gets
recorded and the next attempt asks again -- there is deliberately no
"remember denial" path yet; marking a directory permanently denied is a
manual edit to the ledger (documented in its own header) rather than an
inferred one, since inferring permanent denial from a single "no" risks
locking out a path the user only meant to defer.

Ledger: vault/_brain/read-consent.yaml (mirrors automation-consent.yaml's
shape: project -> directory -> granted).

Fail-open on any internal error (never brick a session over this gate);
fail-CLOSED specifically when a project's OWN deny-config is unreadable,
matching capture_policy.py's existing rule -- a broken deny-list must not
silently become "no denials".

Hook events: PreToolUse, PostToolUse (matcher: Read|Glob|Grep).
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

try:
    from capture_policy import Capture, decide, find_project_root
except ImportError:
    Capture = None  # type: ignore[assignment]
    decide = None  # type: ignore[assignment]
    find_project_root = None  # type: ignore[assignment]

GATED_TOOLS = {"Read", "Glob", "Grep"}
LEDGER_REL = Path("_brain") / "read-consent.yaml"


def vault_root() -> Path | None:
    """Resolve the vault root the same way the scheduled routines do --
    fixed for this machine, matching _common.ps1's $VaultRoot."""
    fixed = Path(r"C:\Users\dzsve\research-os\vault")
    if fixed.is_dir():
        return fixed
    return None


def extract_path(payload: dict[str, Any]) -> str:
    tool_input = payload.get("tool_input") or {}
    for key in ("file_path", "path", "pattern"):
        value = tool_input.get(key)
        if isinstance(value, str) and value:
            return value
    return ""


def ledger_path() -> Path | None:
    root = vault_root()
    return (root / LEDGER_REL) if root else None


def load_ledger() -> dict[str, dict[str, str]]:
    path = ledger_path()
    if path is None or not path.is_file():
        return {}
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return {}
    # Hand-rolled, stdlib-only, matching save_grant()'s own writer exactly:
    #   projects:
    #     "<project>":
    #       "<directory>": granted
    # A naive split on the first ":" breaks here specifically because a
    # Windows directory value itself contains a colon (`C:\Users\...`), so the
    # QUOTED KEY is matched explicitly (up to its closing quote) and only the
    # text after that closing quote is treated as the `: value` separator.
    project_line = re.compile(r'^  "([^"]*)":\s*$')
    directory_line = re.compile(r'^    "([^"]*)":\s*(\S+)\s*$')

    ledger: dict[str, dict[str, str]] = {}
    current_project: str | None = None
    for line in text.split("\n"):
        if not line.strip() or line.strip().startswith("#"):
            continue
        if (match := project_line.match(line)) is not None:
            current_project = match.group(1)
            ledger.setdefault(current_project, {})
        elif (match := directory_line.match(line)) is not None and current_project:
            ledger[current_project][match.group(1)] = match.group(2)
    return ledger


def save_grant(project_name: str, directory: str) -> None:
    path = ledger_path()
    if path is None:
        return
    ledger = load_ledger()
    ledger.setdefault(project_name, {})[directory] = "granted"

    lines = [
        "# R2 read-consent ledger -- see hooks/data-consent.py",
        "#",
        "# project -> directory -> granted. A directory only appears here after a",
        "# human approved a real permission prompt for a data file inside it -- this",
        "# file is not meant to be pre-populated speculatively.",
        "#",
        "# To PERMANENTLY deny a directory (never ask, never allow), add it by hand",
        "# with value 'denied' -- this script only ever writes 'granted' itself.",
        "",
        "projects:",
    ]
    for project_name_key, directories in sorted(ledger.items()):
        lines.append(f'  "{project_name_key}":')
        for directory_key, verdict in sorted(directories.items()):
            lines.append(f'    "{directory_key}": {verdict}')
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    except OSError:
        pass


def ledger_verdict(project_name: str, directory: str) -> str | None:
    ledger = load_ledger()
    return ledger.get(project_name, {}).get(directory)


def gate(payload: dict[str, Any]) -> dict[str, Any] | None:
    """PreToolUse: return a permissionDecision block, or None to allow silently.

    Three-way split on capture_policy's own classification, and it matters:

      CONTENT   -- code/docs. Never gated at all.
      METADATA  -- a data-file extension, but NOT on any project deny-list.
                   This is R2's actual case ("new/unfamiliar data") -- ask,
                   then remember if approved.
      REDACTED  -- the project's OWN AD-5-style deny-list already covers this
                   path (e.g. Microsimulation's SOEP/data/**). This is a
                   STRONGER, pre-existing rule than R2 -- DENY outright,
                   unconditionally, never "ask". Asking would let a human
                   habitually click approve past a hard deny, which is
                   exactly the breach Epic 7.2 closed. A deny-listed path is
                   never something R2's "remember the ruling" should be able
                   to override.
    """
    if decide is None:
        return None

    raw_path = extract_path(payload)
    if not raw_path:
        return None

    verdict = decide(raw_path)
    if verdict.capture.value == "content":
        return None

    project_root = find_project_root(Path(raw_path))
    project_name = project_root.name if project_root else "unknown"
    directory = str(Path(raw_path).resolve().parent) if project_root else raw_path

    if verdict.capture.value == "redacted":
        return {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": (
                    f"Denied by this project's own deny-list ({verdict.code}) -- this is an "
                    f"AD-5-style hard rule, not a per-directory ask. It cannot be approved past; "
                    f"the deny-list itself (.claude/settings.json) is where this would change."
                ),
            }
        }

    remembered = ledger_verdict(project_name, directory)
    if remembered == "granted":
        return None
    if remembered == "denied":
        return {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": (
                    f"This directory was previously marked denied in read-consent.yaml "
                    f"({directory}). Edit the ledger by hand to change this."
                ),
            }
        }

    reason = (
        f"New or unfamiliar data ({verdict.code}). R2: Claude asks before reading data "
        f"it hasn't been explicitly cleared to read, every time, in every project. "
        f"Approving this will remember the directory ({directory}) for next time."
    )
    return {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "ask",
            "permissionDecisionReason": reason,
        }
    }


def record_if_gated(payload: dict[str, Any]) -> None:
    """PostToolUse: the call already happened (i.e. was approved). Remember it.

    Never records a grant for a REDACTED path, even defensively -- that
    classification is the AD-5-style hard deny from gate() above, and no
    code path should ever be able to turn it into "granted".
    """
    if decide is None:
        return

    raw_path = extract_path(payload)
    if not raw_path:
        return

    verdict = decide(raw_path)
    if verdict.capture.value in ("content", "redacted"):
        return

    project_root = find_project_root(Path(raw_path))
    project_name = project_root.name if project_root else "unknown"
    directory = str(Path(raw_path).resolve().parent) if project_root else raw_path

    if ledger_verdict(project_name, directory) is None:
        save_grant(project_name, directory)


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0
    if not isinstance(payload, dict):
        return 0

    if payload.get("tool_name") not in GATED_TOOLS:
        return 0

    event = str(payload.get("hook_event_name") or "")
    if event == "PreToolUse":
        decision = gate(payload)
        if decision is not None:
            json.dump(decision, sys.stdout)
    elif event == "PostToolUse":
        record_if_gated(payload)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:  # noqa: BLE001 - fail open, never brick a session over this gate
        sys.exit(0)
