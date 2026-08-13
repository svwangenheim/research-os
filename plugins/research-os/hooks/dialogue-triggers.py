#!/usr/bin/env python3
"""
Fire the research pipeline's Socratic beats at the right moments, instead of
waiting to be summoned.

The machinery already exists and is good -- /discover's interview style, the
eight-beat dialogue grammar, /wiki-pull, /learn, /recall. What was missing is
that every one of them waits for the user to type a command. `skill-router.md`
says "start every research session with /wiki-pull"; `_brain/profile.md` says all
code Claude writes must be explained so the user learns alongside it. Both are
instructions to a model that may or may not remember. Hooks fire every time.

Two rules, both inherited from the hooks already in this directory:

  1. AMBIENT OFFER, NEVER A BLOCK. engram-session-start.sh says "ambient, never
     nagging"; stop-push-nudge.py says "an OFFER, never an auto-write". A
     trigger opens a dialogue. It never makes a research judgment, never edits,
     and never blocks a tool call.

  2. AN ANNOYANCE BUDGET. At most N offers per session, and a dismissed trigger
     goes quiet for a day. Auto-prompting's real failure mode is becoming
     nagware and being switched off wholesale -- the budget is what keeps the
     feature alive.

Registry: ../state/dialogue-triggers.json (human doc: ../rules/dialogue-triggers.md)

Hook events: SessionStart, PostToolUse, Stop. Always exits 0. Degrades to
silence on any error -- a broken trigger must never cost the user a session.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

CYAN = "\033[0;36m"
DIM = "\033[2m"
NC = "\033[0m"

STATE_DIRNAME = ".research-os"
STATE_FILENAME = "dialogue-trigger-state.json"


def plugin_root() -> Path | None:
    root = os.environ.get("CLAUDE_PLUGIN_ROOT")
    if root:
        return Path(root)
    here = Path(__file__).resolve().parent.parent
    return here if (here / "state").is_dir() else None


def load_registry(root: Path) -> dict[str, Any]:
    path = root / "state" / "dialogue-triggers.json"
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def state_path() -> Path:
    """Per-session bookkeeping. Kept out of the vault -- it is scratch, not knowledge."""
    base = os.environ.get("TEMP") or os.environ.get("TMPDIR") or "/tmp"
    return Path(base) / STATE_DIRNAME / STATE_FILENAME


def load_state() -> dict[str, Any]:
    try:
        return json.loads(state_path().read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def save_state(state: dict[str, Any]) -> None:
    try:
        path = state_path()
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(state), encoding="utf-8")
    except OSError:
        pass


def session_id(payload: dict[str, Any]) -> str:
    return str(payload.get("session_id") or os.environ.get("CLAUDE_SESSION_ID") or "unknown")


def budget_exhausted(registry: dict[str, Any], state: dict[str, Any], sid: str) -> bool:
    limit = int(registry.get("budget", {}).get("max_prompts_per_session", 2))
    return int(state.get("sessions", {}).get(sid, 0)) >= limit


def snoozed(registry: dict[str, Any], state: dict[str, Any], trigger_id: str) -> bool:
    hours = float(registry.get("budget", {}).get("snooze_hours_after_dismiss", 24))
    last = state.get("snoozed", {}).get(trigger_id)
    if not last:
        return False
    try:
        return (time.time() - float(last)) < hours * 3600
    except (TypeError, ValueError):
        return False


def record_fire(state: dict[str, Any], sid: str, trigger_id: str) -> None:
    state.setdefault("sessions", {})
    state["sessions"][sid] = int(state["sessions"].get(sid, 0)) + 1
    state.setdefault("fired", {})[trigger_id] = time.time()


def project_dir(payload: dict[str, Any]) -> Path:
    raw = payload.get("cwd") or os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()
    return Path(raw)


def find_passport(start: Path) -> Path | None:
    """Walk up looking for passport.yaml.

    Bounded to six levels, matching stop-push-nudge.py. Projects that legitimately
    have no passport (the BMAD-based Microsimulation and Macro-Fiscal repos) must
    produce silence, never an error -- absence is a valid state, not a defect.
    """
    current = start.resolve()
    for _ in range(6):
        candidate = current / "passport.yaml"
        if candidate.is_file():
            return candidate
        if current == current.parent:
            break
        current = current.parent
    return None


def read_stage(passport: Path) -> str | None:
    try:
        for line in passport.read_text(encoding="utf-8", errors="replace").split("\n"):
            stripped = line.strip()
            if stripped.startswith("current_stage:"):
                return stripped.split(":", 1)[1].strip().strip("\"'").split("#")[0].strip()
    except OSError:
        return None
    return None


# Fallback only, used when the graph router (graph_ready_summary) is unreachable.
# The graph is the source of truth for "what's next" -- see graph/pipeline.json
# and graph/schema.md. This table predates it and assumes one linear next step
# per stage, which is exactly the assumption the graph exists to drop (a stage
# can have several ready nodes, or none, independent of which stage is "current").
NEXT_STAGE_SKILL = {
    "discovery": ("/strategize", "design the identification strategy"),
    "strategy": ("/analyze", "implement the strategy in code"),
    "analysis": ("/write", "draft the sections from the results"),
    "writing": ("/peer-review", "run the referees and the integrity gate"),
    "review": ("/revise", "classify the referee comments and respond"),
    "revision": ("/submit", "journal targeting and the replication package"),
}


def graph_ready_summary(passport: Path) -> tuple[bool, str | None]:
    """(graph_reachable, ready_summary). Keeps this ambient nudge from
    disagreeing with `/research-os-help` and `graph.py next`, which both read
    the same graph -- this hook must not carry a second, independent opinion
    about pipeline sequencing.

    The two failure shapes are distinct on purpose: `(False, None)` means the
    graph could not be evaluated (missing module, corrupt file) -- fall back to
    the old hint. `(True, None)` means the graph WAS evaluated and nothing
    required is ready -- that is a real answer, not a gap, and must not be
    papered over with the stale one-skill-per-stage guess."""
    root = plugin_root()
    if root is None:
        return False, None
    try:
        scripts_dir = str(root / "scripts")
        if scripts_dir not in sys.path:
            sys.path.insert(0, scripts_dir)
        from graph_eval import State, all_states, build_context  # noqa: PLC0415
        from graph_spec import load_graph  # noqa: PLC0415

        graph = load_graph(root / "graph" / "pipeline.json")
        ctx = build_context(passport.parent, graph)
        required = sorted(
            {s.node.skill for s in all_states(ctx) if s.state is State.READY and not s.optional and s.node.skill}
        )
        return True, (" and ".join(required) if required else None)
    except Exception:
        return False, None


def offer(lines: list[str]) -> None:
    """Print an ambient offer. Two lines at most -- this is a nudge, not a lecture.

    Kept ASCII-only: this writes straight to the user's console, which on Windows
    may still be on a legacy codepage where an em-dash arrives as a replacement
    character. A nudge that renders as mojibake reads as a bug.
    """
    try:
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass
    for line in lines[:2]:
        print(f"{CYAN}{line}{NC}", file=sys.stderr)


def handle_session_start(payload: dict[str, Any]) -> tuple[str, list[str]] | None:
    passport = find_passport(project_dir(payload))
    if passport is None:
        return None
    stage = read_stage(passport)
    if not stage:
        return None
    hint = NEXT_STAGE_SKILL.get(stage, ("", ""))[1]
    return (
        "session-anchor",
        [
            f"research-os | stage: {stage}" + (f" | next: {hint}" if hint else ""),
            "Run /wiki-pull to load what you already know before starting.",
        ],
    )


def handle_post_tool_use(payload: dict[str, Any]) -> tuple[str, list[str]] | None:
    tool_input = payload.get("tool_input") or {}
    raw_path = tool_input.get("file_path") or tool_input.get("path") or ""
    if not raw_path:
        return None
    path = Path(str(raw_path))
    posix = path.as_posix()

    if path.name == "passport.yaml":
        stage = read_stage(path) if path.is_file() else None
        if not stage:
            return None

        graph_reachable, ready = graph_ready_summary(path)
        if graph_reachable:
            if not ready:
                return None  # the graph has a real answer: nothing required is ready yet
            return (
                "stage-transition",
                [
                    f"Stage is now '{stage}'. Ready: {ready}.",
                    "Say the word and I'll open it; no need to look up the command.",
                ],
            )
        if stage in NEXT_STAGE_SKILL:
            # Graph unreachable (module missing, corrupt passport) -- degrade to
            # the old single-guess hint rather than going silent.
            skill, what = NEXT_STAGE_SKILL[stage]
            return (
                "stage-transition",
                [
                    f"Stage is now '{stage}'. Next: {skill} - {what}.",
                    "Say the word and I'll open it; no need to look up the command.",
                ],
            )
        return None

    if "03_analysis/scripts" in posix:
        return (
            "learn-alongside",
            [
                "New analysis code - want me to walk through what it does?",
                "Your profile asks for an economics-student-level explanation, jargon defined.",
            ],
        )
    return None


def has_uncommitted_work(project_dir: Path) -> bool:
    """Pure git, deliberately -- this is what makes the trigger fire
    identically for a research-os project and a BMAD one (Microsimulation,
    Macro-Fiscal). No passport.yaml, no pipeline stage read; just the
    working tree. Bounded timeout, fails to False (never nags on an error)."""
    try:
        result = subprocess.run(
            ["git", "-C", str(project_dir), "status", "--porcelain"],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=10,
            check=False,
        )
    except (OSError, subprocess.SubprocessError):
        return False
    return result.returncode == 0 and bool(result.stdout.strip())


def handle_stop(payload: dict[str, Any]) -> tuple[str, list[str]] | None:
    """The audit's top-scored real gap: 'checkpoint every session with work' --
    evidenced verbatim in a real session (Job Insecurity, mined 2026-08-12):
    'lets stop here for today. do /research-os:git-workflow &
    /research-os:checkpoint & /research-os:wiki-push for all of todays
    findings'. Nothing previously reminded you to run that ritual; this does,
    once, at Stop, only when the working tree actually says something happened."""
    project = project_dir(payload)
    if not has_uncommitted_work(project):
        return None
    return (
        "session-close-needed",
        [
            "Uncommitted work in this project -- want the session-close ritual?",
            "git-workflow -> checkpoint -> wiki-push (or /automate run phd-session-close).",
        ],
    )


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0
    if not isinstance(payload, dict):
        return 0

    root = plugin_root()
    if root is None:
        return 0

    registry = load_registry(root)
    if not registry.get("enabled", False):
        return 0

    event = str(payload.get("hook_event_name") or "")
    handlers = {
        "SessionStart": handle_session_start,
        "PostToolUse": handle_post_tool_use,
        "Stop": handle_stop,
    }
    handler = handlers.get(event)
    if handler is None:
        return 0

    try:
        result = handler(payload)
    except Exception:  # noqa: BLE001 - a trigger must never break a session
        return 0
    if result is None:
        return 0

    trigger_id, lines = result

    enabled_ids = {
        t.get("id") for t in registry.get("triggers", []) if t.get("enabled", True)
    }
    if trigger_id not in enabled_ids:
        return 0

    state = load_state()
    sid = session_id(payload)
    if budget_exhausted(registry, state, sid) or snoozed(registry, state, trigger_id):
        return 0

    offer(lines)
    record_fire(state, sid, trigger_id)
    save_state(state)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:  # noqa: BLE001 - degrade to silence, always
        sys.exit(0)
