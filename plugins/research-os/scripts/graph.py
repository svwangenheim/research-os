#!/usr/bin/env python3
"""
The research-os graph router.

Answers "what can I work on right now?" from the declared graph
(graph/pipeline.json) plus the project's actual state -- instead of walking a
seven-stage list. It RECOMMENDS; it never dispatches. Claude Code runs the
skills; this tells you which ones are runnable and why the rest are not.

    graph.py status [--json]     every node's computed state
    graph.py next  [--json]      the ready frontier, required work first
    graph.py why <node>          which requirement is missing
    graph.py stale [--json]      nodes whose declared inputs changed (advisory)
    graph.py record <node> --score N [--note "..."]   append a run to the ledger
    graph.py adopt [--dry-run]   backfill the ledger for a project that predates the graph
    graph.py dot   [--mermaid]   render the graph
    graph.py selftest            assert the graph matches rules/permissions.md

Stdlib only. Run from anywhere inside a project; the root is found by walking up
to the nearest passport.yaml / CLAUDE.md.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from graph_eval import (  # noqa: E402
    Context,
    NodeStatus,
    State,
    all_states,
    append_run,
    build_context,
    describe,
    node_state,
)
from graph_spec import Graph, load_graph  # noqa: E402
from passport import find_project_root  # noqa: E402

PERMISSIONS_RELPATH = Path("rules") / "permissions.md"

# Work the user should be told about first, in this order.
FRONTIER_ORDER = [State.READY, State.UNGATED, State.STALE, State.BLOCKED, State.DONE, State.NA]

MARKS = {
    State.DONE: "[x]",
    State.STALE: "[~]",
    State.UNGATED: "[!]",
    State.READY: "[ ]",
    State.BLOCKED: "[-]",
    State.NA: "[/]",
}


# ---------- Presentation ----------

def status_dict(st: NodeStatus) -> dict:
    return {
        "node": st.node.id,
        "kind": st.node.kind,
        "phase": st.node.phase,
        "skill": st.node.skill,
        "state": st.state.value,
        "optional": st.optional,
        "score": st.score,
        "parallel_group": st.node.parallel_group,
        "blocked_by": list(st.failures),
        "unknown": list(st.unknowns),
        "stale_inputs": list(st.stale_inputs),
    }


def cmd_status(ctx: Context, args: argparse.Namespace) -> int:
    states = all_states(ctx)
    if args.json:
        print(json.dumps({"root": str(ctx.root), "nodes": [status_dict(s) for s in states]}, indent=2))
        return 0

    print(f"project: {ctx.root}")
    by_state: dict[State, list[NodeStatus]] = {}
    for st in states:
        by_state.setdefault(st.state, []).append(st)

    for state in FRONTIER_ORDER:
        group = by_state.get(state) or []
        if not group:
            continue
        print(f"\n{state.value.upper()} ({len(group)})")
        for st in group:
            tag = " (optional)" if st.optional and state is State.READY else ""
            score = f" score {st.score}" if st.score is not None else ""
            print(f"  {MARKS[state]} {st.node.id:<16} {st.node.skill:<22}{score}{tag}".rstrip())
            for reason in st.failures[:2]:
                print(f"        needs: {reason}")
            for reason in st.unknowns[:1]:
                print(f"        unknown: {reason}")
            for path in st.stale_inputs[:2]:
                print(f"        changed: {path}")
    return 0


def cmd_next(ctx: Context, args: argparse.Namespace) -> int:
    states = all_states(ctx)
    ready = [s for s in states if s.state is State.READY]
    ungated = [s for s in states if s.state is State.UNGATED]
    stale = [s for s in states if s.state is State.STALE]

    required = [s for s in ready if not s.optional]
    optional = [s for s in ready if s.optional]

    if args.json:
        print(json.dumps({
            "required": [status_dict(s) for s in required],
            "optional": [status_dict(s) for s in optional],
            "ungated": [status_dict(s) for s in ungated],
            "stale": [status_dict(s) for s in stale],
        }, indent=2))
        return 0

    if not required and not optional and not ungated:
        print("Nothing is ready. Run `graph.py status` to see what is blocked.")
        return 0

    if ungated:
        print("AWAITING REVIEW — artifacts exist, the gate has not passed:")
        for st in ungated:
            note = st.failures[0] if st.failures else (st.unknowns[0] if st.unknowns else "")
            print(f"  {st.node.id:<16} {st.node.skill:<22} {note}")
        print()

    if required:
        print(f"READY — required ({len(required)}):")
        for i, st in enumerate(required, 1):
            par = _parallel_note(st, required, ctx.graph)
            print(f"  {i}. {st.node.skill:<22} {st.node.id}{par}")
            if st.node.summary:
                print(f"     {st.node.summary}")
        print()

    if optional:
        print(f"READY — optional ({len(optional)}):")
        for st in optional:
            reason = f"  ({st.unknowns[0]})" if st.unknowns else ""
            print(f"  - {st.node.skill:<22} {st.node.id}{reason}")
        print()

    if stale:
        print("STALE (advisory — inputs changed since the recorded run):")
        for st in stale:
            print(f"  ~ {st.node.id:<16} {', '.join(st.stale_inputs[:3])}")
    return 0


def _parallel_note(st: NodeStatus, ready: list[NodeStatus], graph: Graph) -> str:
    """Which other ready nodes may run concurrently with this one.

    Two simultaneously-ready nodes are concurrent unless an edge connects them —
    the graph-theoretic form of the fan-out permissions.md declares and the old
    linear router could never surface."""
    related = set(graph.parents(st.node.id)) | set(graph.children(st.node.id))
    peers = sorted(o.node.id for o in ready if o.node.id != st.node.id and o.node.id not in related)
    return f"   [parallel with {', '.join(peers)}]" if peers else ""


def cmd_why(ctx: Context, args: argparse.Namespace) -> int:
    node = ctx.graph.by_id(args.node)
    if node is None:
        known = ", ".join(n.id for n in ctx.graph.nodes)
        print(f"unknown node {args.node!r}. Known nodes: {known}", file=sys.stderr)
        return 2

    st = node_state(node, ctx)
    print(f"{node.id} — {st.state.value}{'  (optional)' if st.optional else ''}")
    if node.summary:
        print(f"  {node.summary}")
    print(f"  skill: {node.skill or '—'}")

    if st.state is State.NA and node.when:
        print(f"  not applicable: {describe(node.when)}")
        return 0

    if node.is_ambient:
        if not node.ready_when:
            print("  ready_when: (none declared — always ready)")
        for pred in node.ready_when:
            text = describe(pred)
            mark = "MISSING" if text in st.failures else "ok"
            print(f"    [{mark:>7}] {text}")
        return 0

    print("  requires:")
    for pred in node.requires:
        text = describe(pred)
        if text in st.failures:
            mark = "MISSING"
        elif text in st.unknowns:
            mark = "unknown"
        else:
            mark = "ok"
        print(f"    [{mark:>7}] {text}")

    if st.stale_inputs:
        print("  stale inputs (changed since the recorded run):")
        for path in st.stale_inputs:
            print(f"    ~ {path}")

    parents = ctx.graph.parents(node.id)
    if parents:
        print(f"  upstream: {', '.join(parents)}")
    children = ctx.graph.children(node.id)
    if children:
        print(f"  downstream: {', '.join(children)}")
    loops_in = ctx.graph.routes_from(node.id)
    if loops_in:
        print(f"  reachable by loop-back from: {', '.join(loops_in)}")
    advisors = [n.id for n in ctx.graph.nodes if node.id in n.advises]
    if advisors:
        print(f"  advised by: {', '.join(advisors)}")
    return 0


def cmd_stale(ctx: Context, args: argparse.Namespace) -> int:
    """Advisory only — always exits 0. Staleness informs; it never blocks."""
    stale = [s for s in all_states(ctx) if s.state is State.STALE]
    if args.json:
        print(json.dumps([status_dict(s) for s in stale], indent=2))
        return 0
    if not stale:
        print("Nothing stale.")
        return 0
    for st in stale:
        downstream = ctx.graph.descendants(st.node.id)
        print(f"{st.node.id}: inputs changed since the recorded run")
        for path in st.stale_inputs:
            print(f"  changed: {path}")
        if downstream:
            print(f"  also suspect: {', '.join(downstream)}")
    print("\n(advisory — nothing is blocked)")
    return 0


def _new_run_id() -> str:
    return f"r_{uuid.uuid4().hex[:12]}"


def _today() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def cmd_record(ctx: Context, args: argparse.Namespace) -> int:
    """Append a run to 00_admin/process/runs.jsonl. Append-only -- a receipt
    records what was true at run time and is never rewritten (docs/09 invariant
    3). This is what lets `graph.py stale` detect a later upstream edit."""
    node = ctx.graph.by_id(args.node)
    if node is None:
        known = ", ".join(n.id for n in ctx.graph.nodes)
        print(f"unknown node {args.node!r}. Known nodes: {known}", file=sys.stderr)
        return 2
    record = append_run(node, ctx, score=args.score, run_id=_new_run_id(), ts=_today(), note=args.note or "")
    print(f"recorded {node.id} — score {args.score} — {record['run_id']}")
    if record["inputs"]:
        print(f"  hashed {len(record['inputs'])} declared input file(s) for future staleness checks")
    print(f"  journal line: {record['ts']} — {node.id} scored {args.score} (run {record['run_id']})")
    return 0


def cmd_adopt(ctx: Context, args: argparse.Namespace) -> int:
    """Backfill the run ledger for a project that predates the graph layer.

    Infers 'already done' nodes from artifacts on disk + passport.pipeline.stages
    scores, and records a BASELINE hash of their currently-resolved inputs -- so
    staleness detection starts working from this point forward. It cannot know
    whether an upstream file was edited *before* adoption without invalidating
    work done against the old version; that gap is inherent to backfilling from
    a project that was never tracked, which is why this is an explicit,
    reviewable action and never runs implicitly."""
    states = all_states(ctx)
    done_or_stale = [s for s in states if s.state in (State.DONE, State.STALE)]
    candidates = [s for s in done_or_stale if s.node.id not in ctx.runs]
    already = [s for s in done_or_stale if s.node.id in ctx.runs]

    if not candidates:
        if already:
            print(f"Nothing to adopt — {len(already)} node(s) already have a run record.")
        else:
            print("Nothing to adopt — no completed nodes found on this project yet.")
        return 0

    verb = "Would adopt" if args.dry_run else "Adopting"
    print(f"{verb} {len(candidates)} node(s) as a staleness baseline:")
    for st in candidates:
        print(f"  {st.node.id:<16} score {st.score}")
    if already:
        print(f"\n(skipping {len(already)} already recorded: {', '.join(s.node.id for s in already)})")

    if args.dry_run:
        print("\n(dry run — nothing written. Re-run without --dry-run to write.)")
        return 0

    for st in candidates:
        append_run(st.node, ctx, score=st.score, run_id=_new_run_id(), ts=_today(),
                   note="adopted: baseline for staleness, not a real run")
    print(f"\nwrote {len(candidates)} record(s) to 00_admin/process/runs.jsonl")
    return 0


def cmd_dot(ctx: Context, args: argparse.Namespace) -> int:
    graph = ctx.graph
    states = {s.node.id: s.state for s in all_states(ctx)}
    if args.mermaid:
        print("graph LR")
        for node in graph.nodes:
            print(f'  {node.id.replace("-", "_")}["{node.id}<br/>{states[node.id].value}"]')
        for src, dst, kind in graph.edges:
            arrow = "-.->" if kind == "advises" else "-->"
            print(f'  {src.replace("-", "_")} {arrow} {dst.replace("-", "_")}')
        return 0
    print("digraph research_os {\n  rankdir=LR;\n  node [shape=box, fontname=\"monospace\"];")
    for node in graph.nodes:
        print(f'  "{node.id}" [label="{node.id}\\n{states[node.id].value}"];')
    for src, dst, kind in graph.edges:
        style = ' [style=dashed]' if kind == "advises" else ""
        print(f'  "{src}" -> "{dst}"{style};')
    print("}")
    return 0


# ---------- Selftest: the drift check ----------

def parse_permissions(path: Path) -> dict[str, dict[str, str]]:
    """Read rules/permissions.md into {agent: {FIELD: value}}. The narrative is
    authored for humans; this reads only the bolded field lines."""
    text = path.read_text(encoding="utf-8", errors="replace")
    entries: dict[str, dict[str, str]] = {}
    current: str | None = None
    for line in text.splitlines():
        heading = re.match(r"^##\s+([a-z0-9-]+)\s*$", line.strip())
        if heading:
            current = heading.group(1)
            entries[current] = {}
            continue
        field = re.match(r"^-\s+\*\*([A-Z_ ]+):\*\*\s*(.*)$", line.strip())
        if field and current:
            entries[current][field.group(1).strip()] = field.group(2).strip()
    return entries


def _weight_of(raw: str) -> float | None:
    m = re.search(r"([\d.]+)\s*%", raw or "")
    return float(m.group(1)) if m else None


def cmd_selftest(ctx: Context, args: argparse.Namespace) -> int:
    """Assert the graph and rules/permissions.md agree. This is the check that
    keeps the machine-readable spec and the prose from drifting apart -- the
    exact failure this whole layer exists to remove."""
    graph = ctx.graph
    plugin_root = Path(__file__).resolve().parent.parent
    perms = parse_permissions(plugin_root / PERMISSIONS_RELPATH)
    problems: list[str] = []

    for node in graph.pipeline_nodes:
        if node.kind == "gate":
            continue  # the integrity gate is specified in quality.md, not permissions.md
        entry = perms.get(node.id)
        if entry is None:
            problems.append(f"{node.id}: no entry in rules/permissions.md")
            continue
        phase = (entry.get("PHASE") or "").lower()
        if phase and node.phase and phase != node.phase:
            problems.append(f"{node.id}: PHASE {phase!r} in permissions.md, {node.phase!r} in graph")
        group = entry.get("PARALLEL_GROUP")
        if group and group != (node.parallel_group or ""):
            problems.append(f"{node.id}: PARALLEL_GROUP {group!r} vs {node.parallel_group!r}")
        critic = (entry.get("CRITIC") or "").split("—")[0].split("--")[0].strip()
        expected = node.critic or "None"
        if critic and critic.lower() != expected.lower():
            problems.append(f"{node.id}: CRITIC {critic!r} vs {expected!r}")
        weight = _weight_of(entry.get("QUALITY_WEIGHT", ""))
        if weight != node.weight:
            problems.append(f"{node.id}: QUALITY_WEIGHT {weight} vs {node.weight}")

    graph_ids = {n.id for n in graph.pipeline_nodes}
    for agent in perms:
        if agent not in graph_ids:
            problems.append(f"{agent}: in permissions.md but missing from the graph")

    # Every file requirement must be produced by some node, or be a declared
    # project input -- otherwise an edge is silently missing.
    produced = {p for n in graph.nodes for p in n.produced_files}
    from graph_spec import walk_predicates

    for node in graph.nodes:
        for pred in walk_predicates(node.requires):
            if "file" in pred and pred["file"] not in produced:
                problems.append(f"{node.id}: requires {pred['file']!r}, which no node produces")

    # Weights must renormalize to 100 once the conditional theorist is excluded.
    total = sum(n.weight for n in graph.pipeline_nodes if isinstance(n.weight, (int, float)) and not n.when)
    if abs(total - 100.0) > 0.01:
        problems.append(f"unconditional QUALITY_WEIGHTs sum to {total}, expected 100")

    for problem in problems:
        print(f"FAIL  {problem}")
    if problems:
        print(f"\n{len(problems)} problem(s).")
        return 1
    print(f"ok — {len(graph.nodes)} nodes, {len(graph.edges)} derived edges, "
          f"consistent with rules/permissions.md")
    return 0


# ---------- Entry point ----------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="graph.py", description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--project-root", default=None, help="default: nearest passport.yaml / CLAUDE.md")
    parser.add_argument("--graph", default=None, help="path to pipeline.json")
    sub = parser.add_subparsers(dest="command", required=True)

    p_status = sub.add_parser("status", help="every node's computed state")
    p_status.add_argument("--json", action="store_true")
    p_status.set_defaults(func=cmd_status)

    p_next = sub.add_parser("next", help="the ready frontier")
    p_next.add_argument("--json", action="store_true")
    p_next.set_defaults(func=cmd_next)

    p_why = sub.add_parser("why", help="which requirement is missing")
    p_why.add_argument("node")
    p_why.set_defaults(func=cmd_why)

    p_stale = sub.add_parser("stale", help="nodes whose declared inputs changed (advisory)")
    p_stale.add_argument("--json", action="store_true")
    p_stale.set_defaults(func=cmd_stale)

    p_record = sub.add_parser("record", help="append a run to 00_admin/process/runs.jsonl")
    p_record.add_argument("node")
    p_record.add_argument("--score", type=int, required=True)
    p_record.add_argument("--note", default="")
    p_record.set_defaults(func=cmd_record)

    p_adopt = sub.add_parser("adopt", help="backfill the ledger for a project that predates the graph")
    p_adopt.add_argument("--dry-run", action="store_true")
    p_adopt.set_defaults(func=cmd_adopt)

    p_dot = sub.add_parser("dot", help="render the graph")
    p_dot.add_argument("--mermaid", action="store_true")
    p_dot.set_defaults(func=cmd_dot)

    p_self = sub.add_parser("selftest", help="assert the graph matches rules/permissions.md")
    p_self.set_defaults(func=cmd_selftest)

    return parser


def main(argv: list[str] | None = None) -> int:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass

    args = build_parser().parse_args(argv)
    try:
        graph: Graph = load_graph(args.graph)
    except (OSError, ValueError) as exc:
        print(f"cannot load the graph: {exc}", file=sys.stderr)
        return 2
    root = Path(args.project_root).resolve() if args.project_root else find_project_root()
    ctx = build_context(root, graph)
    return args.func(ctx, args)


if __name__ == "__main__":
    raise SystemExit(main())
