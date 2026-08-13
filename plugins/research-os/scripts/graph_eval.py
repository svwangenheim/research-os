#!/usr/bin/env python3
"""
Evaluate the research-os pipeline graph against one project.

State is COMPUTED here, never stored: the filesystem, passport.yaml, and the
append-only run ledger are the inputs; node states are the output. Derived state
cannot desync from reality.

Predicates are three-valued, but UNKNOWN is narrow on purpose: it means "cannot
tell whether this node APPLIES" (an unset paper_type), not "the requirement has
not been met". A missing critic score is a definite FALSE -- the upstream node
has not cleared its gate. Widening UNKNOWN makes unstarted work masquerade as
optional-and-ready, which is the failure this module was corrected for.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any

from graph_spec import Graph, Node
from passport import dotted_get, load_passport

__all__ = [
    "Tri", "State", "Context", "build_context", "node_state", "NodeStatus", "evaluate",
    "RUNS_RELPATH", "declared_input_digests", "append_run",
]

RUNS_RELPATH = "00_admin/process/runs.jsonl"


class Tri(Enum):
    """Three-valued logic. UNKNOWN means 'not determinable', not 'no'."""

    TRUE = "true"
    FALSE = "false"
    UNKNOWN = "unknown"


class State(str, Enum):
    DONE = "done"
    STALE = "stale"
    UNGATED = "ungated"
    READY = "ready"
    BLOCKED = "blocked"
    NA = "n/a"


def tri_all(values: list[Tri]) -> Tri:
    if not values:
        return Tri.TRUE
    if Tri.FALSE in values:
        return Tri.FALSE
    if Tri.UNKNOWN in values:
        return Tri.UNKNOWN
    return Tri.TRUE


def tri_any(values: list[Tri]) -> Tri:
    if not values:
        return Tri.TRUE
    if Tri.TRUE in values:
        return Tri.TRUE
    if Tri.UNKNOWN in values:
        return Tri.UNKNOWN
    return Tri.FALSE


# ---------- Context ----------

@dataclass(frozen=True)
class Context:
    """Everything the evaluator reads. Built once per invocation."""

    root: Path
    graph: Graph
    passport: dict[str, Any]
    runs: dict[str, dict[str, Any]] = field(default_factory=dict)

    def matches(self, pattern: str) -> list[Path]:
        try:
            return sorted(self.root.glob(pattern))
        except (ValueError, OSError):
            return []

    def score(self, node_id: str) -> int | None:
        """A node's critic score: the run ledger first, then the passport stage
        it belongs to. The fallback is what makes the graph work on projects
        that predate it."""
        run = self.runs.get(node_id)
        if run and isinstance(run.get("score"), (int, float)):
            return int(run["score"])
        node = self.graph.by_id(node_id)
        if not node or not node.phase:
            return None
        stage = ((self.passport.get("pipeline") or {}).get("stages") or {}).get(node.phase) or {}
        score = stage.get("score")
        return int(score) if isinstance(score, (int, float)) and not isinstance(score, bool) else None


def load_runs(root: Path) -> dict[str, dict[str, Any]]:
    """Latest run record per node from the append-only ledger. Absent file -> {}."""
    ledger = Path(root) / RUNS_RELPATH
    if not ledger.exists():
        return {}
    runs: dict[str, dict[str, Any]] = {}
    for line in ledger.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            continue  # a torn line must not break routing
        node_id = record.get("node")
        if node_id:
            runs[node_id] = record
    return runs


def build_context(root: Path, graph: Graph) -> Context:
    return Context(root=Path(root), graph=graph, passport=load_passport(Path(root)), runs=load_runs(root))


# ---------- Predicate evaluation ----------

def _is_empty(value: Any) -> bool:
    return value is None or value == "" or value == [] or value == {}


def _file_pred(pred: dict[str, Any], ctx: Context) -> Tri:
    hits = ctx.matches(pred["file"])
    if not hits:
        return Tri.FALSE
    sections = pred.get("sections")
    if not sections:
        return Tri.TRUE
    for hit in hits:
        try:
            text = hit.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        if all(_has_heading(text, s) for s in sections):
            return Tri.TRUE
    return Tri.FALSE


def _has_heading(text: str, heading: str) -> bool:
    needle = heading.strip().lower()
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#") and needle in stripped.lstrip("#").strip().lower():
            return True
    return False


def _passport_pred(pred: dict[str, Any], ctx: Context) -> Tri:
    value = dotted_get(ctx.passport, pred["passport"])
    if "in" in pred or "not_in" in pred:
        if _is_empty(value):
            return Tri.UNKNOWN
        if "in" in pred:
            return Tri.TRUE if value in pred["in"] else Tri.FALSE
        return Tri.FALSE if value in pred["not_in"] else Tri.TRUE
    return Tri.FALSE if _is_empty(value) else Tri.TRUE


def _scored_components(ctx: Context) -> list[tuple[float, int]]:
    """(weight, score) for every node carrying a numeric weight and a score."""
    out: list[tuple[float, int]] = []
    for node in ctx.graph.pipeline_nodes:
        if not isinstance(node.weight, (int, float)) or isinstance(node.weight, bool):
            continue
        score = ctx.score(node.id)
        if score is not None:
            out.append((float(node.weight), score))
    return out


def _overall_pred(pred: dict[str, Any], ctx: Context) -> Tri:
    # Nothing scored means the threshold is not met -- a submission gate must
    # never pass vacuously.
    components = _scored_components(ctx)
    total_weight = sum(w for w, _ in components)
    if not components or total_weight <= 0:
        return Tri.FALSE
    weighted = sum(w * s for w, s in components) / total_weight
    return Tri.TRUE if weighted >= pred["overall"]["min"] else Tri.FALSE


def _all_components_pred(pred: dict[str, Any], ctx: Context) -> Tri:
    components = _scored_components(ctx)
    if not components:
        return Tri.FALSE
    return Tri.TRUE if all(s >= pred["all_components"]["min"] for _, s in components) else Tri.FALSE


def _file_contains_pred(pred: dict[str, Any], ctx: Context) -> Tri:
    spec = pred["file_contains"]
    for hit in ctx.matches(spec["file"]):
        try:
            if spec["pattern"] in hit.read_text(encoding="utf-8", errors="replace"):
                return Tri.TRUE
        except OSError:
            continue
    return Tri.FALSE


def _wiki_pending_push_pred(pred: dict[str, Any], ctx: Context) -> Tri:
    """TRUE when wiki-links.md's '## To push back to the wiki / brain' section
    has a real unchecked item. Mirrors hooks/session-journal.py's
    `unpushed_items` exactly (section-scoped, unchecked `- [ ]`, skips the
    `<placeholder>` template line) so the ambient wiki-push node and the Stop
    hook's nudge never disagree about what counts as pending."""
    for hit in ctx.matches(pred["wiki_pending_push"]["file"]):
        try:
            text = hit.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        in_section = False
        for line in text.splitlines():
            stripped = line.strip()
            if stripped.lower().startswith("## to push back"):
                in_section = True
                continue
            if in_section and stripped.startswith("## "):
                break
            if in_section and stripped.startswith("- [ ]"):
                item = stripped[len("- [ ]"):].strip()
                if item and not item.startswith("<"):
                    return Tri.TRUE
    return Tri.FALSE


def evaluate(pred: dict[str, Any], ctx: Context) -> Tri:
    """Three-valued evaluation of one predicate (combinators included)."""
    if "any_of" in pred:
        return tri_any([evaluate(p, ctx) for p in pred["any_of"]])
    if "all_of" in pred:
        return tri_all([evaluate(p, ctx) for p in pred["all_of"]])
    if "file" in pred:
        return _file_pred(pred, ctx)
    if "file_contains" in pred:
        return _file_contains_pred(pred, ctx)
    if "wiki_pending_push" in pred:
        return _wiki_pending_push_pred(pred, ctx)
    if "passport" in pred:
        return _passport_pred(pred, ctx)
    if "score" in pred:
        # An absent score is a definite "not met", not an unknown: the upstream
        # critic has not cleared that node, so this requirement fails.
        score = ctx.score(pred["score"]["node"])
        return Tri.TRUE if score is not None and score >= pred["score"]["min"] else Tri.FALSE
    if "gate" in pred:
        return _gate_passed(pred["gate"], ctx)
    if "overall" in pred:
        return _overall_pred(pred, ctx)
    if "all_components" in pred:
        return _all_components_pred(pred, ctx)
    return Tri.UNKNOWN


def _gate_passed(node_id: str, ctx: Context) -> Tri:
    node = ctx.graph.by_id(node_id)
    if node is None:
        return Tri.UNKNOWN
    return _gate_met(node, ctx)


def _gate_met(node: Node, ctx: Context) -> Tri:
    """Has this node cleared its own gate?"""
    if not node.gate:
        return Tri.TRUE
    if "min" in node.gate:
        score = ctx.score(node.id)
        return Tri.UNKNOWN if score is None else (Tri.TRUE if score >= node.gate["min"] else Tri.FALSE)
    if "passport_empty" in node.gate:
        produced = tri_any([evaluate(p, ctx) for p in node.produces])
        if produced is not Tri.TRUE:
            return produced
        return Tri.TRUE if _is_empty(dotted_get(ctx.passport, node.gate["passport_empty"])) else Tri.FALSE
    return Tri.UNKNOWN


# ---------- Staleness ----------

def file_digest(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return "sha256:" + h.hexdigest()[:16]


def declared_input_digests(node: Node, ctx: Context) -> dict[str, str]:
    """Hash of every file currently satisfying this node's `file` requirements.
    Content hashing, not mtime: git checkouts and touch-only edits are not changes."""
    from graph_spec import walk_predicates

    digests: dict[str, str] = {}
    for pred in walk_predicates(node.requires):
        if "file" not in pred:
            continue
        for hit in ctx.matches(pred["file"]):
            if not hit.is_file():
                continue
            try:
                digests[hit.relative_to(ctx.root).as_posix()] = file_digest(hit)
            except (OSError, ValueError):
                continue
    return digests


def append_run(node: Node, ctx: Context, score: int | None, run_id: str, ts: str, note: str = "") -> dict[str, Any]:
    """Append one record to the append-only run ledger. NEVER rewrites a prior
    line -- a receipt records what was true at run time (docs/09 invariant 3).
    Returns the record written."""
    record: dict[str, Any] = {
        "node": node.id,
        "run_id": run_id,
        "ts": ts,
        "score": score,
        "inputs": declared_input_digests(node, ctx),
    }
    if note:
        record["note"] = note
    ledger = Path(ctx.root) / RUNS_RELPATH
    ledger.parent.mkdir(parents=True, exist_ok=True)
    with ledger.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(record) + "\n")
    return record


def stale_inputs(node: Node, ctx: Context) -> list[str]:
    """Declared inputs whose content changed since this node's recorded run.
    No run record -> nothing is knowably stale."""
    run = ctx.runs.get(node.id)
    if not run or not isinstance(run.get("inputs"), dict):
        return []
    recorded: dict[str, str] = run["inputs"]
    current = declared_input_digests(node, ctx)
    changed = [p for p, digest in recorded.items() if current.get(p) != digest]
    changed += [p for p in current if p not in recorded]
    return sorted(set(changed))


# ---------- Node state ----------

@dataclass(frozen=True)
class NodeStatus:
    node: Node
    state: State
    optional: bool
    failures: tuple[str, ...] = ()
    unknowns: tuple[str, ...] = ()
    stale_inputs: tuple[str, ...] = ()
    score: int | None = None


def describe(pred: dict[str, Any]) -> str:
    """One-line, human-readable rendering of a predicate -- what `why` prints."""
    if "any_of" in pred:
        return " OR ".join(describe(p) for p in pred["any_of"])
    if "all_of" in pred:
        return " AND ".join(describe(p) for p in pred["all_of"])
    if "file" in pred:
        sections = pred.get("sections")
        base = pred["file"]
        return f"{base} with sections {', '.join(sections)}" if sections else base
    if "file_contains" in pred:
        return f"{pred['file_contains']['file']} containing {pred['file_contains']['pattern']!r}"
    if "wiki_pending_push" in pred:
        return f"{pred['wiki_pending_push']['file']} has an unchecked item to push back"
    if "passport" in pred:
        if "in" in pred:
            return f"passport {pred['passport']} in {pred['in']}"
        if "not_in" in pred:
            return f"passport {pred['passport']} not in {pred['not_in']}"
        return f"passport {pred['passport']} set"
    if "score" in pred:
        return f"{pred['score']['node']} score >= {pred['score']['min']}"
    if "gate" in pred:
        return f"{pred['gate']} gate passed"
    if "overall" in pred:
        return f"overall score >= {pred['overall']['min']}"
    if "all_components" in pred:
        return f"every scored component >= {pred['all_components']['min']}"
    return str(pred)


def _describe_gate(node: Node, result: Tri) -> str:
    """Why a node's own gate is unmet, in the gate's own terms."""
    if node.gate and "min" in node.gate:
        critic = node.gate.get("critic") or node.critic or "critic"
        return f"{critic} score below {node.gate['min']}"
    if node.gate and "passport_empty" in node.gate:
        return f"passport {node.gate['passport_empty']} is not empty"
    return f"gate unmet ({result.value})"


def node_state(node: Node, ctx: Context) -> NodeStatus:
    """Compute one node's state. Pure: same inputs, same answer."""
    applicability = evaluate(node.when, ctx) if node.when else Tri.TRUE
    if applicability is Tri.FALSE:
        return NodeStatus(node=node, state=State.NA, optional=True)
    optional = node.optional or node.is_ambient or applicability is Tri.UNKNOWN

    if node.is_ambient:
        unmet = [describe(p) for p in node.ready_when if evaluate(p, ctx) is Tri.FALSE]
        state = State.BLOCKED if unmet else State.READY
        return NodeStatus(node=node, state=state, optional=True, failures=tuple(unmet))

    # ANY declared artifact on disk means the node ran. permissions.md's PRODUCES
    # lists secondary outputs too (codebooks, extra figures) that a legitimate run
    # need not emit; requiring all of them would report finished work as unstarted.
    # The critic score, checked next, is the authoritative gate.
    produced = tri_any([evaluate(p, ctx) for p in node.produces]) if node.produces else Tri.FALSE
    if produced is Tri.TRUE:
        gate = _gate_met(node, ctx)
        if gate is Tri.TRUE:
            changed = stale_inputs(node, ctx)
            state = State.STALE if changed else State.DONE
            return NodeStatus(node=node, state=state, optional=optional,
                              stale_inputs=tuple(changed), score=ctx.score(node.id))
        # Artifacts exist but the gate is unmet: the work ran, it has not passed.
        critic = node.critic or "the gate"
        gate_note = _describe_gate(node, gate)
        return NodeStatus(
            node=node,
            state=State.UNGATED,
            optional=optional,
            failures=(gate_note,) if gate is Tri.FALSE else (),
            unknowns=() if gate is Tri.FALSE else (f"{critic} has not scored it yet",),
            score=ctx.score(node.id),
        )

    failures: list[str] = []
    unknowns: list[str] = []
    for pred in node.requires:
        result = evaluate(pred, ctx)
        if result is Tri.FALSE:
            failures.append(describe(pred))
        elif result is Tri.UNKNOWN:
            unknowns.append(describe(pred))

    state = State.BLOCKED if failures else State.READY
    return NodeStatus(node=node, state=state, optional=optional or bool(unknowns),
                      failures=tuple(failures), unknowns=tuple(unknowns), score=ctx.score(node.id))


def all_states(ctx: Context) -> list[NodeStatus]:
    return [node_state(n, ctx) for n in ctx.graph.nodes]
