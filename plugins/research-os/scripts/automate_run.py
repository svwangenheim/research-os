#!/usr/bin/env python3
"""
Parse a procedure into an execution plan. Never executes anything itself.

This is the piece that never existed under the old procedure/skill split: a
procedure was documentation, and becoming runnable required passing five gates
that nothing could ever satisfy. There is no gate now. A procedure is runnable
the moment it validates against the template, and this script is what makes
"runnable" concrete: it turns the Steps section into an ordered plan the
`/automate` skill actually walks.

Why the runner returns a PLAN instead of executing shell commands itself: tool
permission enforcement (and the R2 data-consent gate, `hooks/data-consent.py`)
lives in Claude's own tool layer. A script that shelled out on its own would be
a second, unaudited execution path running outside that enforcement -- exactly
the kind of side door AD-5 exists to prevent. So this script reads, classifies,
and orders; `/automate run` is what actually acts, step by step, using its own
tools, which keeps every read and every mutation inside the one place that's
actually gated.

Runner semantics (identical interactively and on a schedule):
    [ai]        the skill executes this step itself
    [human]     STOP -- ask, then wait. A scheduled run stops here too and
                leaves a note; it does not guess.
    [external]  the skill orchestrates it (invoke the named tool/skill/BMAD
                workflow) but the actual system does the work
    [veto]      REFUSE, unconditionally. No plan is emitted past this step.

This is what makes R1 ("strategic/design/identification questions are never
solo") structural rather than aspirational: tag the step [human], and the
runner cannot execute it alone, ever, regardless of how it was invoked.

Usage:
    python automate_run.py --root <vault> --name <procedure> [--dry-run]
    python automate_run.py --root <vault> --name <procedure> --record-run \\
        --stopped-at <n> --deviations "<text>"   # called by the skill after execution
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import asdict, dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))

from wiki_quality_check import STEP_ACTOR_TAGS, force_utf8_console, parse_frontmatter  # noqa: E402

RUN_LOG_START = "<!-- @generated:start run-log -->"
RUN_LOG_END = "<!-- @generated:end -->"

STEP_RE = re.compile(r"^(\d+)\.\s+(.*)$")
CALL_RE = re.compile(r"`([^`]+)`")

ACTOR_ORDER = {"ai": 0, "external": 1, "human": 2, "veto": 3}


@dataclass
class PlanStep:
    number: int
    text: str
    actor: str  # ai | human | external | veto | unspecified
    calls: list[str] = field(default_factory=list)

    @property
    def is_stop(self) -> bool:
        return self.actor in ("human", "veto")


@dataclass
class Plan:
    name: str
    title: str
    role: str
    automation: str
    veto_reason: str
    draft: bool
    steps: list[PlanStep]
    stop_at: int | None  # 1-indexed step number the runner must stop before, if any
    refused: bool         # a [veto] step exists and was reached in order

    @property
    def executable_steps(self) -> list[PlanStep]:
        """Steps the runner performs before the first stop, in order."""
        if self.stop_at is None:
            return self.steps
        return [s for s in self.steps if s.number < self.stop_at]


def find_procedure(brain_root: Path, name: str) -> Path | None:
    folder = brain_root / "procedures"
    candidate = folder / f"{name}.md"
    if candidate.is_file():
        return candidate
    if not folder.is_dir():
        return None
    for path in folder.glob("*.md"):
        if path.name.lower() == "readme.md":
            continue
        fm, _ = parse_frontmatter(path.read_text(encoding="utf-8", errors="replace"))
        if fm.get("note_type") == "procedure" and str(fm.get("name") or "") == name:
            return path
    return None


def section(body: str, heading: str) -> str:
    match = re.search(
        rf"^##\s+{re.escape(heading)}\s*$(.*?)(?=^##\s|\Z)",
        body,
        re.MULTILINE | re.DOTALL | re.IGNORECASE,
    )
    return match.group(1) if match else ""


def parse_steps(body: str, known_calls: list[str]) -> list[PlanStep]:
    """`known_calls` is the procedure's own declared `calls:` frontmatter list.

    A step's backtick-wrapped spans are cross-referenced against it, rather
    than treated as calls on their own -- prose routinely backtick-wraps
    config values and command names being described (or explicitly warned
    against, e.g. "never `Bash run_in_background`"), and matching every
    backtick span unconditionally displayed those as if the step were
    invoking them.
    """
    text = re.sub(r"<!--.*?-->", "", section(body, "Steps"), flags=re.DOTALL)
    steps: list[PlanStep] = []
    for line in text.split("\n"):
        match = STEP_RE.match(line.strip())
        if not match:
            continue
        raw = match.group(2).strip()
        actor = "unspecified"
        for tag in STEP_ACTOR_TAGS:
            if tag in raw:
                actor = tag.strip("[]")
                raw = raw.replace(tag, "").strip()
                break
        backticked = set(CALL_RE.findall(raw))
        calls = [c for c in known_calls if c in backticked or c in raw]
        steps.append(PlanStep(int(match.group(1)), raw, actor, calls))
    return steps


def build_plan(path: Path) -> Plan:
    fm, body = parse_frontmatter(path.read_text(encoding="utf-8", errors="replace"))
    known_calls = fm.get("calls") or []
    if not isinstance(known_calls, list):
        known_calls = [str(known_calls)]
    steps = parse_steps(body, known_calls)

    stop_at: int | None = None
    refused = False
    if fm.get("automation") == "vetoed":
        refused = True
        stop_at = steps[0].number if steps else 1
    else:
        for step in steps:
            if step.actor == "veto":
                refused = True
                stop_at = step.number
                break
            if step.actor == "human":
                stop_at = step.number
                break
            if step.actor == "unspecified":
                # An unclassified step is not "ai" by default -- the runner
                # cannot decide who runs it, so it stops rather than guessing.
                stop_at = step.number
                break

    return Plan(
        name=str(fm.get("name") or path.stem),
        title=str(fm.get("title") or path.stem),
        role=str(fm.get("role") or ""),
        automation=str(fm.get("automation") or "assisted"),
        veto_reason=str(fm.get("veto_reason") or ""),
        draft=bool(fm.get("draft", True)) if not isinstance(fm.get("draft"), str) else fm.get("draft") == "true",
        steps=steps,
        stop_at=stop_at,
        refused=refused,
    )


def render_plan(plan: Plan) -> str:
    if not plan.steps:
        return f"# {plan.title}\n\nNo steps written yet -- nothing to run."

    lines = [f"# Execution plan: {plan.title}", ""]
    if plan.draft:
        lines.append("**DRAFT** -- this procedure has not been corrected on a real run yet.")
    if plan.refused:
        reason = plan.veto_reason or "a [veto] step was reached"
        lines.append(f"**REFUSED** -- {reason}. No steps will execute.")
        lines.append("")
        return "\n".join(lines)

    for step in plan.steps:
        marker = {
            "ai": "[ai]     ",
            "human": "[human]  ",
            "external": "[external]",
            "veto": "[veto]   ",
            "unspecified": "[??]     ",
        }[step.actor]
        stop = "  <-- STOPS HERE" if (plan.stop_at == step.number) else ""
        calls = f"  calls: {', '.join(step.calls)}" if step.calls else ""
        lines.append(f"  {step.number}. {marker} {step.text}{calls}{stop}")

    lines.append("")
    if plan.stop_at is not None:
        stopped = next(s for s in plan.steps if s.number == plan.stop_at)
        if stopped.actor == "unspecified":
            lines.append(
                f"Step {plan.stop_at} has no actor tag -- the runner cannot classify it "
                f"and will not guess. Tag it [ai]/[human]/[external]/[veto] and re-run."
            )
        else:
            if plan.stop_at == 1:
                lines.append("Runner stops immediately at step 1 -- no steps execute first.")
            else:
                lines.append(f"Runner executes steps 1-{plan.stop_at - 1}, then stops at step {plan.stop_at}.")
    else:
        lines.append(f"All {len(plan.steps)} step(s) execute without stopping.")
    return "\n".join(lines)


def record_run(path: Path, stopped_at: int | None, deviations: str, ran_by: str) -> bool:
    """Append one run-log entry inside the @generated markers. Never touches
    anything outside them -- the same boundary discipline as the weekly
    reconciler's block, verified there to be byte-identical outside it.

    Returns False (and writes nothing) if the note has no run-log markers --
    e.g. a hand-edited note that dropped them. The caller must not report
    success when this happens.
    """
    text = path.read_text(encoding="utf-8", errors="replace")
    start = text.find(RUN_LOG_START)
    end = text.find(RUN_LOG_END)
    if start == -1 or end == -1 or end < start:
        return False

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    stop_note = f"stopped at step {stopped_at}" if stopped_at else "completed"
    entry = f"- {timestamp} ({ran_by}) {stop_note}"
    if deviations:
        entry += f" -- deviation: {deviations}"

    inner = text[start + len(RUN_LOG_START):end]
    new_inner = inner.rstrip("\n") + "\n" + entry + "\n"
    updated = text[: start + len(RUN_LOG_START)] + new_inner + text[end:]
    path.write_text(updated, encoding="utf-8")
    return True


def main(argv: list[str] | None = None) -> int:
    force_utf8_console()
    parser = argparse.ArgumentParser(description="Build (and optionally log) a procedure execution plan.")
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--name", required=True, help="The procedure's name: field (== its filename).")
    parser.add_argument("--dry-run", action="store_true", help="Print the plan only (default behaviour).")
    parser.add_argument("--record-run", action="store_true", help="Append a run-log entry after execution.")
    parser.add_argument("--stopped-at", type=int, help="Step number the run stopped at, if any.")
    parser.add_argument("--deviations", default="", help="Free text: what differed from the note.")
    parser.add_argument("--ran-by", default="interactive", help='"interactive" or "scheduled".')
    args = parser.parse_args(argv)

    brain_root = args.root if args.root.name == "_brain" else args.root / "_brain"
    path = find_procedure(brain_root, args.name)
    if path is None:
        print(f"error: no procedure named {args.name!r} in {brain_root / 'procedures'}", file=sys.stderr)
        return 1

    plan = build_plan(path)

    if args.record_run:
        if record_run(path, args.stopped_at, args.deviations, args.ran_by):
            print(f"Run recorded in {path}")
            return 0
        print(f"error: {path} has no run-log markers -- nothing recorded", file=sys.stderr)
        return 1

    print(render_plan(plan))
    return 0


if __name__ == "__main__":
    sys.exit(main())
