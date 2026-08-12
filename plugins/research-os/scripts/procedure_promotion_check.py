#!/usr/bin/env python3
"""
Decide, mechanically, whether a procedure has earned promotion to a skill.

The workflow layer's second rule: promotion is computed, not remembered. A
procedure that has proven itself should not wait for someone to notice it. This
script evaluates five gates against a procedure note's own frontmatter and body
and reports which ones pass.

    procedure := how *this* researcher does something, judgment calls included
    skill     := machinery any researcher could run

The gates encode exactly that difference:

    runs            >= MIN_RUNS recorded executions        (it is real, not aspirational)
    stable          steps unchanged across the last 2 runs (it has stopped moving)
    contract        inputs + outputs + done_when present   (it has an interface)
    forks_resolved  every decision point is a rule or ask-user
    generic         nothing person/employer-specific outside the Config block

All five pass -> `promotion: ready`. Nothing here writes: /procedure owns the
frontmatter flip and the SKILL.md draft, and shipping still takes a human
confirm. This script only ever reports.

Usage:
    python procedure_promotion_check.py --root <vault>
    python procedure_promotion_check.py --root <vault> --format json
    python procedure_promotion_check.py --root <vault> --name <slug>
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))

from wiki_quality_check import is_empty, parse_frontmatter  # noqa: E402  (needs sys.path above)
from wiki_quality_check import force_utf8_console  # noqa: E402

MIN_RUNS = 3
STABLE_RUNS = 2

# Markers that a step is still person- or employer-specific. Deliberately
# narrow: the test is "would a second researcher have to rewrite this line",
# and a path or a colleague's name is the clearest signal of that.
SPECIFIC_PATTERNS: tuple[tuple[str, str], ...] = (
    (r"[A-Za-z]:[\\/]", "absolute filesystem path"),
    (r"(?i)onedrive", "OneDrive reference"),
    (r"(?i)dezernat\s*zukunft|\bDZ\b", "employer-specific reference"),
    (r"(?i)\bsven\b", "person-specific reference"),
    (r"(?i)\bsoep\b|\beuromod\b", "institution-specific dataset/tool"),
)

DECISION_ROW_RE = re.compile(r"^\|(?!\s*[-: ]+\|)(.+)\|(.+)\|(.+)\|\s*$")


@dataclass
class Gate:
    name: str
    passed: bool
    detail: str


@dataclass
class ProcedureVerdict:
    slug: str
    title: str
    role: str
    automation: str
    promotion_declared: str
    gates: list[Gate] = field(default_factory=list)

    @property
    def eligible(self) -> bool:
        return all(gate.passed for gate in self.gates)

    @property
    def blocked_by(self) -> list[str]:
        return [gate.name for gate in self.gates if not gate.passed]


def section(body: str, heading: str) -> str:
    """Return the text under a `## heading`, up to the next `## `."""
    pattern = re.compile(
        rf"^##\s+{re.escape(heading)}\s*$(.*?)(?=^##\s|\Z)",
        re.MULTILINE | re.DOTALL | re.IGNORECASE,
    )
    match = pattern.search(body)
    return match.group(1) if match else ""


def strip_comments(text: str) -> str:
    """Drop HTML comments -- template guidance is not user content."""
    return re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)


def gate_runs(fm: dict[str, Any]) -> Gate:
    raw = fm.get("runs")
    try:
        runs = int(raw)
    except (TypeError, ValueError):
        runs = 0
    return Gate(
        "runs",
        runs >= MIN_RUNS,
        f"{runs} recorded run(s), need {MIN_RUNS}",
    )


def gate_stable(body: str) -> Gate:
    """Steps unchanged across the last STABLE_RUNS entries of the run log.

    The run log records a steps_hash per run; if the last two agree, the
    procedure has stopped being rewritten and is safe to freeze into a skill.
    """
    log = section(body, "Run log")
    hashes = re.findall(r"steps_hash[:=]\s*([0-9a-f]{6,})", log, re.IGNORECASE)
    if len(hashes) < STABLE_RUNS:
        return Gate(
            "stable",
            False,
            f"only {len(hashes)} hashed run(s) in the log, need {STABLE_RUNS}",
        )
    recent = hashes[-STABLE_RUNS:]
    unchanged = len(set(recent)) == 1
    return Gate(
        "stable",
        unchanged,
        "steps unchanged across the last 2 runs"
        if unchanged
        else "steps changed between the last 2 runs",
    )


def gate_contract(fm: dict[str, Any]) -> Gate:
    missing = [key for key in ("inputs", "outputs", "done_when") if is_empty(fm.get(key))]
    return Gate(
        "contract",
        not missing,
        "complete" if not missing else f"missing: {', '.join(missing)}",
    )


def gate_forks_resolved(body: str) -> Gate:
    """Every row in the Decision points table needs a non-placeholder rule."""
    table = strip_comments(section(body, "Decision points"))
    rows = [
        (match.group(2).strip(), match.group(3).strip())
        for line in table.split("\n")
        if (match := DECISION_ROW_RE.match(line.strip()))
    ]
    # Keep a row if it asks a real question. The RULE cell is deliberately NOT
    # used to filter -- an empty rule is precisely what this gate must catch,
    # so filtering on it would drop the only rows that matter.
    data_rows = [
        rule
        for question, rule in rows
        if question and question.lower() not in ("the question", "question")
    ]
    if not data_rows:
        return Gate("forks_resolved", True, "no decision points declared")
    # `ask-user` IS a resolution -- it declares the fork permanently human, which
    # is a legitimate thing for a skill to do. Only an empty cell blocks: that
    # means nobody has decided yet.
    empty = [rule for rule in data_rows if rule in ("", "TBD", "?")]
    return Gate(
        "forks_resolved",
        not empty,
        f"{len(data_rows) - len(empty)}/{len(data_rows)} decision points resolved"
        if not empty
        else f"{len(empty)} decision point(s) with no rule at all",
    )


def gate_generic(body: str) -> Gate:
    """Nothing person- or employer-specific in the Steps, outside Config."""
    steps = strip_comments(section(body, "Steps"))
    hits: list[str] = []
    for pattern, label in SPECIFIC_PATTERNS:
        if re.search(pattern, steps):
            hits.append(label)
    return Gate(
        "generic",
        not hits,
        "steps are portable"
        if not hits
        else f"specifics in Steps (move to Config): {', '.join(sorted(set(hits)))}",
    )


def evaluate(path: Path) -> ProcedureVerdict | None:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    fm, body = parse_frontmatter(text)
    if fm.get("note_type") != "procedure":
        return None

    verdict = ProcedureVerdict(
        slug=path.stem,
        title=str(fm.get("title") or path.stem),
        role=str(fm.get("role") or ""),
        automation=str(fm.get("automation") or ""),
        promotion_declared=str(fm.get("promotion") or "draft"),
    )
    verdict.gates = [
        gate_runs(fm),
        gate_stable(body),
        gate_contract(fm),
        gate_forks_resolved(body),
        gate_generic(body),
    ]
    return verdict


def load_verdicts(brain_root: Path, name: str | None = None) -> list[ProcedureVerdict]:
    folder = brain_root / "procedures"
    if not folder.is_dir():
        return []
    verdicts: list[ProcedureVerdict] = []
    for path in sorted(folder.glob("*.md")):
        if path.name.lower() == "readme.md":
            continue
        if name and path.stem != name:
            continue
        if (verdict := evaluate(path)) is not None:
            verdicts.append(verdict)
    return verdicts


def render(verdicts: list[ProcedureVerdict]) -> str:
    if not verdicts:
        return "No procedure notes found in _brain/procedures/."

    lines = ["# Procedure promotion status", ""]
    ready = [v for v in verdicts if v.eligible and v.promotion_declared != "promoted"]
    others = [v for v in verdicts if not v.eligible]
    promoted = [v for v in verdicts if v.promotion_declared == "promoted"]

    if ready:
        lines.append(f"## Ready for promotion ({len(ready)})")
        for verdict in ready:
            lines.append(f"  - {verdict.slug} ({verdict.role}) - all five gates pass")
        lines.append("")
        lines.append("  Run `/procedure promote <slug>` to draft the SKILL.md.")
        lines.append("")

    if others:
        lines.append(f"## Still maturing ({len(others)})")
        for verdict in others:
            lines.append(f"\n  {verdict.slug} ({verdict.role or 'no role'})")
            for gate in verdict.gates:
                mark = "PASS" if gate.passed else "----"
                lines.append(f"    [{mark}] {gate.name}: {gate.detail}")
        lines.append("")

    if promoted:
        lines.append(f"## Already promoted ({len(promoted)})")
        for verdict in promoted:
            lines.append(f"  - {verdict.slug}")
        lines.append("")

    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    force_utf8_console()
    parser = argparse.ArgumentParser(
        description="Report which procedures have earned promotion to skills."
    )
    parser.add_argument("--root", type=Path, required=True, help="Vault root or _brain directory.")
    parser.add_argument("--name", help="Evaluate a single procedure by slug.")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args(argv)

    brain_root = args.root if args.root.name == "_brain" else args.root / "_brain"
    if not brain_root.is_dir():
        print(f"error: no _brain directory at {brain_root}", file=sys.stderr)
        return 1

    verdicts = load_verdicts(brain_root, args.name)

    if args.format == "json":
        payload = [
            {**asdict(v), "eligible": v.eligible, "blocked_by": v.blocked_by} for v in verdicts
        ]
        print(json.dumps(payload, indent=2))
    else:
        print(render(verdicts))
    return 0


if __name__ == "__main__":
    sys.exit(main())
