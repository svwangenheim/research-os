#!/usr/bin/env python3
"""
Load and validate the research-os pipeline graph (graph/pipeline.json).

The graph is a static spec: nodes, their requirements, and what they produce.
Edges are DERIVED from requires/produces so no dependency is ever declared
twice. See graph/schema.md for the field and predicate reference.

Nothing here touches project state -- that is graph_eval.py's job.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

__all__ = ["Node", "Graph", "load_graph", "default_graph_path"]

WORK = "work"
GATE = "gate"
ROUTER = "router"
AMBIENT = "ambient"
KINDS = (WORK, GATE, ROUTER, AMBIENT)

# Edge kinds that constitute a real data dependency. `advises` is advisory and
# `route` is a loop-back; including either would make staleness chase the
# revision cycle around forever.
DEPENDENCY_EDGES = ("score", "gate", "artifact")


def _dedupe(items) -> tuple[str, ...]:
    """Stable de-duplication -- two nodes can be joined by both a score edge and
    an artifact edge, and that is one dependency, not two."""
    seen: list[str] = []
    for item in items:
        if item not in seen:
            seen.append(item)
    return tuple(seen)


@dataclass(frozen=True)
class Node:
    """One node of the pipeline graph. Immutable; mirrors one rules/permissions.md entry."""

    id: str
    kind: str
    skill: str
    phase: str | None = None
    agents: tuple[str, ...] = ()
    critic: str | None = None
    parallel_group: str | None = None
    requires: tuple[dict[str, Any], ...] = ()
    produces: tuple[dict[str, Any], ...] = ()
    gate: dict[str, Any] | None = None
    when: dict[str, Any] | None = None
    routes: tuple[dict[str, Any], ...] = ()
    advises: tuple[str, ...] = ()
    ready_when: tuple[dict[str, Any], ...] = ()
    scope: str | None = None
    weight: float | None = None
    optional: bool = False
    blocking: bool = False
    terminal: bool = False
    summary: str = ""

    @property
    def is_ambient(self) -> bool:
        return self.kind == AMBIENT

    @property
    def produced_files(self) -> tuple[str, ...]:
        return tuple(p["file"] for p in self.produces if "file" in p)


@dataclass(frozen=True)
class Graph:
    """The whole pipeline: nodes plus the edges derived from their predicates."""

    version: int
    nodes: tuple[Node, ...]
    edges: tuple[tuple[str, str, str], ...] = field(default=())  # (src, dst, kind)

    def by_id(self, node_id: str) -> Node | None:
        for n in self.nodes:
            if n.id == node_id:
                return n
        return None

    def parents(self, node_id: str) -> tuple[str, ...]:
        """Data dependencies only. `advises` is advisory and `route` is a
        control-flow loop-back, so neither is a dependency."""
        return _dedupe(src for src, dst, kind in self.edges
                       if dst == node_id and kind in DEPENDENCY_EDGES)

    def children(self, node_id: str) -> tuple[str, ...]:
        return _dedupe(dst for src, dst, kind in self.edges
                       if src == node_id and kind in DEPENDENCY_EDGES)

    def routes_to(self, node_id: str) -> tuple[str, ...]:
        return _dedupe(dst for src, dst, kind in self.edges if src == node_id and kind == "route")

    def routes_from(self, node_id: str) -> tuple[str, ...]:
        return _dedupe(src for src, dst, kind in self.edges if dst == node_id and kind == "route")

    def descendants(self, node_id: str) -> tuple[str, ...]:
        """Transitive children, in stable order. Cycle-safe."""
        seen: list[str] = []
        stack = list(self.children(node_id))
        while stack:
            nid = stack.pop(0)
            if nid in seen:
                continue
            seen.append(nid)
            stack.extend(self.children(nid))
        return tuple(seen)

    @property
    def pipeline_nodes(self) -> tuple[Node, ...]:
        return tuple(n for n in self.nodes if not n.is_ambient)


# ---------- Predicate walking ----------

def walk_predicates(preds: tuple[dict[str, Any], ...] | list[dict[str, Any]]):
    """Yield every leaf predicate, flattening any_of / all_of combinators."""
    for p in preds or ():
        if "any_of" in p:
            yield from walk_predicates(p["any_of"])
        elif "all_of" in p:
            yield from walk_predicates(p["all_of"])
        else:
            yield p


# ---------- Loading ----------

def default_graph_path() -> Path:
    """graph/pipeline.json, resolved relative to this file's plugin root."""
    return Path(__file__).resolve().parent.parent / "graph" / "pipeline.json"


def _node_from_dict(raw: dict[str, Any]) -> Node:
    return Node(
        id=raw["id"],
        kind=raw["kind"],
        skill=raw.get("skill", ""),
        phase=raw.get("phase"),
        agents=tuple(raw.get("agents") or ()),
        critic=raw.get("critic"),
        parallel_group=raw.get("parallel_group"),
        requires=tuple(raw.get("requires") or ()),
        produces=tuple(raw.get("produces") or ()),
        gate=raw.get("gate"),
        when=raw.get("when"),
        routes=tuple(raw.get("routes") or ()),
        advises=tuple(raw.get("advises") or ()),
        ready_when=tuple(raw.get("ready_when") or ()),
        scope=raw.get("scope"),
        weight=raw.get("weight"),
        optional=bool(raw.get("optional", False)),
        blocking=bool(raw.get("blocking", False)),
        terminal=bool(raw.get("terminal", False)),
        summary=raw.get("summary", ""),
    )


def derive_edges(nodes: tuple[Node, ...]) -> tuple[tuple[str, str, str], ...]:
    """Edges from predicates only -- never hand-listed. Three exact rules:
    (1) score/gate predicates naming a node id, (2) file requirements whose glob
    equals another node's produced glob, (3) ambient `advises`."""
    ids = {n.id for n in nodes}
    produced_by: dict[str, list[str]] = {}
    for n in nodes:
        for pattern in n.produced_files:
            produced_by.setdefault(pattern, []).append(n.id)

    edges: list[tuple[str, str, str]] = []

    def add(src: str, dst: str, kind: str) -> None:
        if src != dst and (src, dst, kind) not in edges:
            edges.append((src, dst, kind))

    for node in nodes:
        for pred in walk_predicates(node.requires):
            if "score" in pred:
                src = pred["score"].get("node")
                if src in ids:
                    add(src, node.id, "score")
            elif "gate" in pred:
                if pred["gate"] in ids:
                    add(pred["gate"], node.id, "gate")
            elif "file" in pred:
                for src in produced_by.get(pred["file"], []):
                    add(src, node.id, "artifact")
        for target in node.advises:
            if target in ids:
                add(node.id, target, "advises")
        for route in node.routes:
            if route.get("to") in ids:
                add(node.id, route["to"], "route")

    return tuple(edges)


def load_graph(path: Path | str | None = None) -> Graph:
    """Read and structurally validate the graph. Raises ValueError on a bad spec."""
    p = Path(path) if path else default_graph_path()
    raw = json.loads(p.read_text(encoding="utf-8"))
    nodes = tuple(_node_from_dict(n) for n in raw.get("nodes", []))
    _validate(nodes)
    return Graph(version=int(raw.get("version", 1)), nodes=nodes, edges=derive_edges(nodes))


def _validate(nodes: tuple[Node, ...]) -> None:
    if not nodes:
        raise ValueError("graph has no nodes")

    seen: set[str] = set()
    ids = {n.id for n in nodes}
    for n in nodes:
        if n.id in seen:
            raise ValueError(f"duplicate node id: {n.id}")
        seen.add(n.id)
        if n.kind not in KINDS:
            raise ValueError(f"{n.id}: unknown kind {n.kind!r} (expected one of {KINDS})")
        if not n.is_ambient and not n.phase:
            raise ValueError(f"{n.id}: non-ambient nodes need a phase")
        for target in n.advises:
            if target not in ids:
                raise ValueError(f"{n.id}: advises unknown node {target!r}")
        for route in n.routes:
            if route.get("to") not in ids:
                raise ValueError(f"{n.id}: routes to unknown node {route.get('to')!r}")
        for pred in walk_predicates(n.requires):
            _validate_predicate(n.id, pred, ids)


_PREDICATE_KEYS = {
    "file", "score", "passport", "gate", "overall", "all_components",
    "file_contains", "wiki_pending_push",
}


def _validate_predicate(node_id: str, pred: dict[str, Any], ids: set[str]) -> None:
    keys = set(pred) & _PREDICATE_KEYS
    if not keys:
        raise ValueError(f"{node_id}: predicate {pred!r} has no known kind ({sorted(_PREDICATE_KEYS)})")
    if "score" in pred and pred["score"].get("node") not in ids:
        raise ValueError(f"{node_id}: score predicate names unknown node {pred['score'].get('node')!r}")
    if "gate" in pred and pred["gate"] not in ids:
        raise ValueError(f"{node_id}: gate predicate names unknown node {pred['gate']!r}")
