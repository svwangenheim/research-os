#!/usr/bin/env python3
"""
Shared reader for a research-os project's `passport.yaml` state ledger.

Extracted from generate_dashboard.py so the dashboard and the graph router read
the passport through exactly one parser. A second, divergent parser is the drift
this module exists to prevent.

PyYAML is used when available; otherwise a targeted line parser handles the
passport's regular structure (see templates/passport.yaml). Stdlib-only by
default -- no hard dependency.

Nothing here writes. The passport is edited in place by skills and agents; run
provenance lives in 00_admin/process/runs.jsonl (see scripts/graph.py).
"""

from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Any

__all__ = [
    "find_project_root",
    "load_passport",
    "stage_scores",
    "dotted_get",
]


def find_project_root(start: str | os.PathLike[str] | None = None) -> Path:
    """Walk up from `start` to the nearest folder holding passport.yaml or CLAUDE.md."""
    origin = Path(start or os.getcwd()).resolve()
    p = origin
    while p != p.parent:
        if (p / "passport.yaml").exists() or (p / "CLAUDE.md").exists():
            return p
        p = p.parent
    return origin


def load_passport(root: Path) -> dict[str, Any]:
    """Load `root/passport.yaml`. Prefers PyYAML; falls back to a targeted line
    parser for the fields consumers need (meta, research, pipeline,
    literature_corpus, sessions, integrity). Returns {} when absent."""
    pf = Path(root) / "passport.yaml"
    if not pf.exists():
        return {}
    text = pf.read_text(encoding="utf-8", errors="replace")
    try:
        import yaml  # type: ignore

        data = yaml.safe_load(text)
        return data if isinstance(data, dict) else {}
    except Exception:
        return _fallback_passport(text)


def _scalar(raw: str) -> Any:
    v = raw.strip()
    if v in ("null", "~", ""):
        return None
    if v in ("[]", "{}"):
        return []
    if (v.startswith('"') and v.endswith('"')) or (v.startswith("'") and v.endswith("'")):
        return v[1:-1]
    if re.fullmatch(r"-?\d+", v):
        return int(v)
    return v


def _fallback_passport(text: str) -> dict[str, Any]:
    """Minimal, defensive parser for the passport's regular structure.
    Handles top-level scalars/sections, inline flow maps under pipeline.stages,
    and simple block lists of mappings (literature_corpus, sessions)."""
    data: dict[str, Any] = {
        "meta": {},
        "research": {},
        "pipeline": {"stages": {}},
        "literature_corpus": [],
        "sessions": [],
        "integrity": {},
    }

    # Top-level scalar sections: meta:, research:, integrity:
    for section in ("meta", "research", "integrity"):
        m = re.search(rf"^{section}:\s*$(.*?)(?=^\S|\Z)", text, re.MULTILINE | re.DOTALL)
        if not m:
            continue
        for line in m.group(1).split("\n"):
            km = re.match(r"\s{2}(\w+):\s*(.*)", line)
            if km:
                data[section][km.group(1)] = _scalar(km.group(2).split("#")[0])

    # pipeline.current_stage
    cs = re.search(r"^\s{2}current_stage:\s*(.*)", text, re.MULTILINE)
    if cs:
        data["pipeline"]["current_stage"] = _scalar(cs.group(1).split("#")[0])

    # pipeline.stages.<name>: { status: "...", score: ..., gate: ... }
    for sm in re.finditer(r"^\s{4}(\w+):\s*\{([^}]*)\}", text, re.MULTILINE):
        stage: dict[str, Any] = {}
        for kv in re.finditer(r"(\w+):\s*([^,]+)", sm.group(2)):
            stage[kv.group(1)] = _scalar(kv.group(2))
        data["pipeline"]["stages"][sm.group(1)] = stage

    # Block lists of mappings: literature_corpus, sessions
    for key in ("literature_corpus", "sessions"):
        lm = re.search(rf"^{key}:\s*(\[\])?\s*$(.*?)(?=^\S|\Z)", text, re.MULTILINE | re.DOTALL)
        if not lm or lm.group(1) == "[]":
            continue
        items: list[dict[str, Any]] = []
        current: dict[str, Any] | None = None
        for line in lm.group(2).split("\n"):
            im = re.match(r"\s+-\s+(\w+):\s*(.*)", line)
            km = re.match(r"\s+(\w+):\s*(.*)", line)
            if im:
                if current:
                    items.append(current)
                current = {im.group(1): _scalar(im.group(2).split(" #")[0])}
            elif km and current is not None:
                current[km.group(1)] = _scalar(km.group(2).split(" #")[0])
        if current:
            items.append(current)
        data[key] = items

    return data


def stage_scores(passport: dict[str, Any]) -> dict[str, int]:
    """Numeric scores from `pipeline.stages`, keyed by stage name.
    Stages with a null or non-numeric score are omitted."""
    stages = ((passport.get("pipeline") or {}).get("stages") or {})
    scores: dict[str, int] = {}
    for name, st in stages.items():
        score = (st or {}).get("score")
        if isinstance(score, bool):
            continue
        if isinstance(score, (int, float)):
            scores[name] = int(score)
    return scores


def dotted_get(passport: dict[str, Any], path: str) -> Any:
    """Read a dotted path (e.g. "research.question", "integrity.unresolved").
    Returns None when any segment is missing."""
    node: Any = passport
    for part in path.split("."):
        if not isinstance(node, dict) or part not in node:
            return None
        node = node[part]
    return node
