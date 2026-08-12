#!/usr/bin/env python3
"""
Render the procedure layer as a self-contained interactive HTML map.

Step 4 of the workflow layer. Two views:

  by role      -- what a week actually contains, grouped by hat. The view that
                  answers "can I hold a PhD and a think-tank job at once".
  by procedure -- each procedure's step flow, coloured by who executes each step.

Node colour carries automation status, extending the source guide's scheme with
a class it did not need and a researcher does:

  purple  Claude executes            [ai]
  yellow  human input required       [human]
  green   external tool or system    [external]
  red     VETOED -- never automate   [veto]
  grey    not yet specified

Self-contained by construction: no CDN, no fetch, no external font. The page is
opened from disk, often offline, and must never depend on the network.

Usage:
    python generate_procedure_map.py --root <vault>
    python generate_procedure_map.py --root <vault> --out <path.html>
"""

from __future__ import annotations

import argparse
import html
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))

from wiki_quality_check import parse_frontmatter  # noqa: E402  (needs sys.path above)
from wiki_quality_check import force_utf8_console  # noqa: E402

ACTOR_CLASSES: dict[str, tuple[str, str]] = {
    "[ai]": ("ai", "Claude executes"),
    "[human]": ("human", "Human input required"),
    "[external]": ("external", "External tool or system"),
    "[veto]": ("veto", "Vetoed - never automate"),
}

ROLE_LABELS: dict[str, str] = {
    "phd": "PhD",
    "dz-modelling": "DZ · Modelling",
    "dz-outreach": "DZ · Outreach",
    "admin": "Admin",
    "": "Unassigned",
}

STEP_RE = re.compile(r"^(\d+)\.\s+(.*)$")


@dataclass
class Step:
    number: int
    text: str
    actor: str  # css class: ai | human | external | veto | unspecified


def as_number(value: Any) -> float | None:
    """Coerce a frontmatter scalar to a number.

    parse_frontmatter is regex-based and returns every scalar as a string, so
    `clone_score: 72` arrives as "72" and sorting on it raises. Anything
    genuinely absent or non-numeric becomes None, which sorts last.
    """
    if value is None or isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    try:
        return float(str(value).strip())
    except (TypeError, ValueError):
        return None


@dataclass
class Procedure:
    slug: str
    title: str
    role: str
    trigger: str
    frequency: str
    clone_score: float | None
    automation: str
    veto_reason: str
    promotion: str
    runs: int
    steps: list[Step] = field(default_factory=list)

    @property
    def step_mix(self) -> dict[str, int]:
        mix: dict[str, int] = {}
        for step in self.steps:
            mix[step.actor] = mix.get(step.actor, 0) + 1
        return mix

    @property
    def automatable_share(self) -> float:
        """Share of steps Claude could run. The map's one honest summary number."""
        if not self.steps:
            return 0.0
        return sum(1 for s in self.steps if s.actor == "ai") / len(self.steps)


def section(body: str, heading: str) -> str:
    match = re.search(
        rf"^##\s+{re.escape(heading)}\s*$(.*?)(?=^##\s|\Z)",
        body,
        re.MULTILINE | re.DOTALL | re.IGNORECASE,
    )
    return match.group(1) if match else ""


def parse_steps(body: str) -> list[Step]:
    text = re.sub(r"<!--.*?-->", "", section(body, "Steps"), flags=re.DOTALL)
    steps: list[Step] = []
    for line in text.split("\n"):
        match = STEP_RE.match(line.strip())
        if not match:
            continue
        raw = match.group(2).strip()
        actor = "unspecified"
        for tag, (css_class, _) in ACTOR_CLASSES.items():
            if tag in raw:
                actor = css_class
                raw = raw.replace(tag, "").strip()
                break
        steps.append(Step(int(match.group(1)), raw, actor))
    return steps


def load_procedures(brain_root: Path) -> list[Procedure]:
    folder = brain_root / "procedures"
    if not folder.is_dir():
        return []
    procedures: list[Procedure] = []
    for path in sorted(folder.glob("*.md")):
        if path.name.lower() == "readme.md":
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        fm, body = parse_frontmatter(text)
        if fm.get("note_type") != "procedure":
            continue
        try:
            runs = int(fm.get("runs") or 0)
        except (TypeError, ValueError):
            runs = 0
        procedures.append(
            Procedure(
                slug=path.stem,
                title=str(fm.get("title") or path.stem),
                role=str(fm.get("role") or ""),
                trigger=str(fm.get("trigger") or ""),
                frequency=str(fm.get("frequency") or ""),
                clone_score=as_number(fm.get("clone_score")),
                automation=str(fm.get("automation") or "manual"),
                veto_reason=str(fm.get("veto_reason") or ""),
                promotion=str(fm.get("promotion") or "draft"),
                runs=runs,
                steps=parse_steps(body),
            )
        )
    return procedures


def esc(value: Any) -> str:
    return html.escape(str(value if value is not None else ""))


CSS = """
:root{--ivory:#faf9f5;--paper:#fff;--slate:#141413;--clay:#d97757;--oat:#e3dacc;
--g100:#f0eee6;--g200:#e6e3da;--g300:#d1cfc5;--g500:#87867f;--g700:#3d3d3a;
--ai:#7c5cbf;--human:#b8860b;--external:#4d7c5a;--veto:#b33d3d;--unspec:#9a998f;
--serif:ui-serif,Georgia,'Times New Roman',serif;
--sans:system-ui,-apple-system,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;
--mono:ui-monospace,'SF Mono',Menlo,Consolas,monospace;--radius:10px}
@media (prefers-color-scheme:dark){:root{--ivory:#1a1917;--paper:#222220;--slate:#e8e6e0;
--g100:#2a2926;--g200:#333230;--g300:#4a4945;--g500:#9a998f;--g700:#c8c6be;--oat:#3d3830;
--clay:#e0896a;--ai:#a68bd9;--human:#d4a72c;--external:#6fa07d;--veto:#d46a6a;--unspec:#7a7970}}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
body{background:var(--ivory);color:var(--slate);font-family:var(--sans);
line-height:1.55;padding:28px 20px 80px;-webkit-font-smoothing:antialiased}
.wrap{max-width:1100px;margin:0 auto}
h1{font-family:var(--serif);font-size:30px;font-weight:600;letter-spacing:-.02em}
.stamp{font-family:var(--mono);font-size:12px;color:var(--g500);margin-top:6px}
.tabs{display:flex;gap:6px;margin:22px 0 18px;border-bottom:1px solid var(--g300)}
.tabs button{font-family:var(--sans);font-size:14px;background:none;border:0;
border-bottom:2px solid transparent;padding:9px 14px;cursor:pointer;color:var(--g500)}
.tabs button.active{color:var(--clay);border-bottom-color:var(--clay);font-weight:600}
.legend{display:flex;flex-wrap:wrap;gap:14px;margin-bottom:22px;font-size:12.5px;color:var(--g700)}
.legend span{display:flex;align-items:center;gap:6px}
.dot{width:11px;height:11px;border-radius:3px;display:inline-block}
.dot.ai{background:var(--ai)}.dot.human{background:var(--human)}
.dot.external{background:var(--external)}.dot.veto{background:var(--veto)}
.dot.unspecified{background:var(--unspec)}
.role{margin-bottom:30px}
.role h2{font-family:var(--serif);font-size:20px;font-weight:600;margin-bottom:4px}
.role .meta{font-family:var(--mono);font-size:11.5px;color:var(--g500);margin-bottom:12px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(310px,1fr));gap:14px}
.card{background:var(--paper);border:1px solid var(--g200);border-radius:var(--radius);
padding:15px 16px}
.card.veto{border-color:var(--veto);border-width:1.5px}
.card h3{font-family:var(--serif);font-size:16px;font-weight:600;margin-bottom:5px}
.card .trig{font-size:12.5px;color:var(--g700);margin-bottom:9px}
.card .facts{font-family:var(--mono);font-size:11px;color:var(--g500);
display:flex;flex-wrap:wrap;gap:9px;margin-bottom:9px}
.bar{display:flex;height:7px;border-radius:4px;overflow:hidden;background:var(--g100)}
.bar i{display:block}
.bar i.ai{background:var(--ai)}.bar i.human{background:var(--human)}
.bar i.external{background:var(--external)}.bar i.veto{background:var(--veto)}
.bar i.unspecified{background:var(--unspec)}
.share{font-family:var(--mono);font-size:11px;color:var(--g500);margin-top:6px}
.vetoline{margin-top:9px;font-size:12px;color:var(--veto);border-top:1px solid var(--g200);padding-top:8px}
.proc{background:var(--paper);border:1px solid var(--g200);border-radius:var(--radius);
padding:18px 20px;margin-bottom:16px}
.proc h3{font-family:var(--serif);font-size:18px;font-weight:600}
.proc .sub{font-family:var(--mono);font-size:11.5px;color:var(--g500);margin:4px 0 14px}
ol.steps{list-style:none;counter-reset:s}
ol.steps li{counter-increment:s;position:relative;padding:7px 0 7px 42px;font-size:14px;
border-left:2px solid var(--g200);margin-left:11px}
ol.steps li::before{content:counter(s);position:absolute;left:-11px;top:8px;width:22px;height:22px;
border-radius:50%;color:#fff;font-family:var(--mono);font-size:11px;display:flex;
align-items:center;justify-content:center}
ol.steps li.ai::before{background:var(--ai)}
ol.steps li.human::before{background:var(--human)}
ol.steps li.external::before{background:var(--external)}
ol.steps li.veto::before{background:var(--veto)}
ol.steps li.unspecified::before{background:var(--unspec)}
ol.steps li.veto{background:color-mix(in srgb,var(--veto) 7%,transparent)}
.tag{font-family:var(--mono);font-size:10px;color:var(--g500);margin-left:7px}
.empty{background:var(--paper);border:1px dashed var(--g300);border-radius:var(--radius);
padding:28px;text-align:center;color:var(--g500)}
.empty code{font-family:var(--mono);font-size:12.5px;color:var(--clay)}
.hidden{display:none}
"""

JS = """
document.querySelectorAll('.tabs button').forEach(function(btn){
  btn.addEventListener('click', function(){
    document.querySelectorAll('.tabs button').forEach(function(b){b.classList.remove('active');});
    document.querySelectorAll('.view').forEach(function(v){v.classList.add('hidden');});
    btn.classList.add('active');
    document.getElementById(btn.dataset.view).classList.remove('hidden');
  });
});
"""


def render_bar(procedure: Procedure) -> str:
    if not procedure.steps:
        return '<div class="bar"></div>'
    total = len(procedure.steps)
    order = ("ai", "human", "external", "veto", "unspecified")
    mix = procedure.step_mix
    parts = [
        f'<i class="{key}" style="width:{mix[key] / total * 100:.1f}%"></i>'
        for key in order
        if mix.get(key)
    ]
    return f'<div class="bar">{"".join(parts)}</div>'


def render_role_view(procedures: list[Procedure]) -> str:
    by_role: dict[str, list[Procedure]] = {}
    for procedure in procedures:
        by_role.setdefault(procedure.role, []).append(procedure)

    blocks: list[str] = []
    for role in sorted(by_role, key=lambda r: (r == "", r)):
        items = sorted(by_role[role], key=lambda p: -(p.clone_score if p.clone_score is not None else -1))
        scored = [p.clone_score for p in items if p.clone_score is not None]
        avg = f"avg clone score {sum(scored) / len(scored):.0f}" if scored else "unscored"
        cards: list[str] = []
        for procedure in items:
            veto = " veto" if procedure.automation == "vetoed" else ""
            veto_line = (
                f'<div class="vetoline"><strong>VETOED</strong> &mdash; {esc(procedure.veto_reason)}</div>'
                if procedure.automation == "vetoed"
                else ""
            )
            cards.append(
                f'<div class="card{veto}"><h3>{esc(procedure.title)}</h3>'
                f'<div class="trig">{esc(procedure.trigger)}</div>'
                f'<div class="facts"><span>{esc(procedure.frequency or "?")}</span>'
                f'<span>score {esc(f"{procedure.clone_score:.0f}" if procedure.clone_score is not None else "-")}</span>'
                f'<span>{procedure.runs} run(s)</span><span>{esc(procedure.promotion)}</span></div>'
                f'{render_bar(procedure)}'
                f'<div class="share">{procedure.automatable_share * 100:.0f}% of steps automatable'
                f' &middot; {len(procedure.steps)} steps</div>{veto_line}</div>'
            )
        blocks.append(
            f'<div class="role"><h2>{esc(ROLE_LABELS.get(role, role))}</h2>'
            f'<div class="meta">{len(items)} procedure(s) &middot; {avg}</div>'
            f'<div class="grid">{"".join(cards)}</div></div>'
        )
    return "".join(blocks)


def render_procedure_view(procedures: list[Procedure]) -> str:
    blocks: list[str] = []
    for procedure in sorted(procedures, key=lambda p: (p.role, p.title)):
        if procedure.steps:
            steps_html = "".join(
                f'<li class="{step.actor}">{esc(step.text)}'
                f'<span class="tag">{step.actor}</span></li>'
                for step in procedure.steps
            )
            body = f'<ol class="steps">{steps_html}</ol>'
        else:
            body = '<div class="share">No steps written yet.</div>'
        blocks.append(
            f'<div class="proc"><h3>{esc(procedure.title)}</h3>'
            f'<div class="sub">{esc(ROLE_LABELS.get(procedure.role, procedure.role))} &middot; '
            f'trigger: {esc(procedure.trigger or "unspecified")} &middot; '
            f'{esc(procedure.automation)} &middot; {procedure.runs} run(s)</div>{body}</div>'
        )
    return "".join(blocks)


def render_empty() -> str:
    return (
        '<div class="empty"><p>No procedures yet.</p>'
        '<p style="margin-top:10px">Run <code>/workflow-audit</code> to find what you do '
        "repeatedly, then <code>/procedure new &lt;name&gt;</code> to write the first one.</p></div>"
    )


def render_page(procedures: list[Procedure], stamp: str) -> str:
    legend = "".join(
        f'<span><i class="dot {css}"></i>{label}</span>'
        for css, label in [
            ("ai", "Claude executes"),
            ("human", "Human input"),
            ("external", "External tool"),
            ("veto", "Vetoed - never automate"),
            ("unspecified", "Not yet specified"),
        ]
    )
    if procedures:
        views = (
            f'<div class="legend">{legend}</div>'
            f'<div id="v-role" class="view">{render_role_view(procedures)}</div>'
            f'<div id="v-proc" class="view hidden">{render_procedure_view(procedures)}</div>'
        )
        tabs = (
            '<div class="tabs">'
            '<button class="active" data-view="v-role">By role</button>'
            '<button data-view="v-proc">By procedure</button></div>'
        )
    else:
        views, tabs = render_empty(), ""

    total_steps = sum(len(p.steps) for p in procedures)
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Procedure Map</title><style>{CSS}</style></head>
<body><div class="wrap">
<h1>Procedure Map</h1>
<div class="stamp">as of {esc(stamp)} &middot; {len(procedures)} procedure(s) &middot; {total_steps} steps</div>
{tabs}{views}
</div><script>{JS}</script></body></html>"""


def main(argv: list[str] | None = None) -> int:
    force_utf8_console()
    parser = argparse.ArgumentParser(description="Render _brain/procedures/ as an HTML map.")
    parser.add_argument("--root", type=Path, required=True, help="Vault root or _brain directory.")
    parser.add_argument("--out", type=Path, help="Output path (default: <brain>/procedure-map.html).")
    parser.add_argument("--stamp", help="Override the generation timestamp (for reproducible tests).")
    args = parser.parse_args(argv)

    brain_root = args.root if args.root.name == "_brain" else args.root / "_brain"
    if not brain_root.is_dir():
        print(f"error: no _brain directory at {brain_root}", file=sys.stderr)
        return 1

    procedures = load_procedures(brain_root)
    stamp = args.stamp or datetime.now().strftime("%Y-%m-%d %H:%M")
    out_path = args.out or (brain_root / "procedure-map.html")
    out_path.write_text(render_page(procedures, stamp), encoding="utf-8")

    print(f"Wrote {out_path} ({len(procedures)} procedure(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main())
