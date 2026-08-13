#!/usr/bin/env python3
"""
PostToolUse hook - flag manuscript claims that just went stale.

The integrity gate (rules/quality.md 3) traces every claim in `passport.yaml`
`claim_manifest` back to a real evidence origin. But it only runs at
`/peer-review` and `/submit`. So between those two points you can edit the
script that produced Table 2 and carry on writing against a number that no
longer exists, and nothing says a word until the gate fires days later.

This hook closes that window. The moment an analysis script or an output
artifact changes, it reports how many claims depend on it and are therefore
potentially STALE, and points at `/peer-review --replicate`.

It is a notifier, not a writer: it never edits `passport.yaml`. Recording a
status is the verifier's job, and the passport is a single-writer artifact
(see hooks/protect-files.py). Telling you early costs nothing and cannot be
wrong in a damaging way; silently rewriting state from a hook can.

Matching is on the project-relative path, not the basename - otherwise
`scripts/R/clean.R` and `scripts/py/clean.py` reconcile each other, and
`clean.R` spuriously matches `data_clean.R`.

Hook Event: PostToolUse (matcher: Write|Edit|MultiEdit)
Output: exit 0 + JSON with `systemMessage` and `additionalContext`.
Fail-open: any error exits 0, silently.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path

# Analysis inputs and outputs. A claim can go stale because the code changed or
# because the output it reads changed.
WATCHED = re.compile(
    r"(^|/)03_analysis/scripts/.*\.(R|r|py|jl|do)$"
    r"|(^|/)03_analysis/output/"
    r"|(^|/)02_data/cleaned/"
)

THROTTLE_SECONDS = 300

# A claim_manifest entry spans several lines; we only need `id` and
# `evidence_origin`. A line-based scan avoids a PyYAML dependency, which the
# other stdlib-only scripts in this plugin also deliberately avoid.
ID_RE = re.compile(r"^\s*-\s+id:\s*[\"']?([^\"'\s]+)")
ORIGIN_RE = re.compile(r"^\s*evidence_origin:\s*[\"']?([^\"'\n]+?)[\"']?\s*$")


def state_dir() -> Path:
    project_dir = os.environ.get("CLAUDE_PROJECT_DIR", "")
    digest = hashlib.md5(project_dir.encode()).hexdigest()[:8] if project_dir else "default"
    path = Path.home() / ".claude" / "sessions" / digest
    path.mkdir(parents=True, exist_ok=True)
    return path


def find_passport(start: Path) -> Path | None:
    """Walk up for a project passport, the way the other hooks find wiki-links.md."""
    current = start.resolve()
    for _ in range(6):
        candidate = current / "passport.yaml"
        if candidate.is_file():
            return candidate
        if current == current.parent:
            break
        current = current.parent
    return None


def relative_to_project(file_path: str, project_dir: str) -> str:
    """Project-relative POSIX path, falling back to the basename."""
    try:
        rel = Path(file_path).resolve().relative_to(Path(project_dir).resolve())
        return rel.as_posix()
    except (ValueError, OSError):
        return Path(file_path).name


def dependent_claims(passport: Path, changed: str) -> list[str]:
    """Claim ids whose evidence_origin references the changed path."""
    try:
        text = passport.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return []

    basename = Path(changed).name
    hits: list[str] = []
    current_id: str | None = None

    for line in text.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("#"):
            continue  # the template's commented-out example is not a real claim
        match = ID_RE.match(line)
        if match:
            current_id = match.group(1)
            continue
        match = ORIGIN_RE.match(line)
        if match and current_id:
            origin = match.group(1).strip()
            # `analysis:03_analysis/scripts/R/03_analyze.R` or `data:02_data/...`.
            # Accept the full relative path, or the basename when the passport
            # recorded a shorter form.
            if changed in origin or (basename and basename in origin):
                hits.append(current_id)
            current_id = None
    return hits


def throttled(key: str) -> bool:
    path = state_dir() / "claim-reconcile-state.json"
    try:
        state = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        state = {}
    now = time.time()
    if now - state.get(key, 0) < THROTTLE_SECONDS:
        return True
    state[key] = now
    try:
        path.write_text(json.dumps(state), encoding="utf-8")
    except OSError:
        pass
    return False


def main() -> int:
    try:
        hook_input = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError, OSError):
        return 0

    tool_input = hook_input.get("tool_input") or {}
    file_path = tool_input.get("file_path")
    if not isinstance(file_path, str) or not file_path:
        return 0
    if not WATCHED.search(file_path.replace("\\", "/")):
        return 0

    project_dir = os.environ.get("CLAUDE_PROJECT_DIR") or hook_input.get("cwd") or ""
    if not project_dir:
        return 0

    passport = find_passport(Path(project_dir))
    if passport is None:
        return 0  # not a research-os project, or no ledger yet

    changed = relative_to_project(file_path, project_dir)
    if throttled(changed):
        return 0

    claims = dependent_claims(passport, changed)
    if not claims:
        return 0

    shown = ", ".join(claims[:6]) + ("..." if len(claims) > 6 else "")
    json.dump(
        {
            "systemMessage": (
                f"{changed} changed - {len(claims)} claim(s) may be STALE [{shown}]. "
                f"Re-verify with /peer-review --replicate."
            ),
            "hookSpecificOutput": {
                "hookEventName": "PostToolUse",
                "additionalContext": (
                    f"A tracked analysis input ({changed}) was just modified. "
                    f"{len(claims)} claim(s) in passport.yaml claim_manifest depend on it "
                    f"and are now potentially stale: {shown}. Before presenting, citing, or "
                    f"committing those numbers, re-run /peer-review --replicate so the "
                    f"integrity gate re-traces them. Do not assume the manuscript is correct "
                    f"and the code stale, or the reverse - one of the two must change, and "
                    f"which one is an empirical question."
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
        sys.exit(0)  # fail open
