#!/usr/bin/env python3
"""
Render the current week as a self-contained HTML dashboard, with each calendar
block carrying its project's live state.

The point is not to reproduce Outlook. Outlook already shows
"MFMOD fixes, 10:30-18:00". This shows that block *plus* "F4 still open and
blocking; next: Phase 4 of the Epic 6 plan" -- the calendar answering "what am I
walking into" instead of merely "what is scheduled".

Freshness model, stated honestly: a static page cannot reach Microsoft 365 --
that connector only exists inside a Claude session. So /week fetches the
calendar into `_brain/.calendar-cache.json` and this renders from that cache,
stamping "as of <time>" prominently. Staleness is visible rather than pretended
away, and the page never touches the network.

Usage:
    python generate_week_dashboard.py --root <vault>
    python generate_week_dashboard.py --root <vault> --week 2026-08-10
"""

from __future__ import annotations

import argparse
import html
import json
import sys
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))

from project_state_scan import ProjectState, scan_all  # noqa: E402
from wiki_quality_check import force_utf8_console  # noqa: E402
from reconcile_week import load_role_budgets, monday_of, resolve_event_role  # noqa: E402

CALENDAR_CACHE = ".calendar-cache.json"
DAY_START, DAY_END = 8, 20  # hours shown in the grid
PX_PER_HOUR = 46

CATEGORY_CLASS: dict[str, str] = {
    "Work Blocker": "work",
    "Self-imposed Deadline": "selfdl",
    "External Deadline": "extdl",
    "External Appointment": "extappt",
    "Private Appointment": "private",
    "DZ": "dz",
}


@dataclass
class Event:
    subject: str
    start: datetime | None
    end: datetime | None
    categories: list[str]
    is_all_day: bool
    project: str | None
    location: str
    role: str | None

    @property
    def css_class(self) -> str:
        for category in self.categories:
            if category in CATEGORY_CLASS:
                return CATEGORY_CLASS[category]
        return "other"

    @property
    def hours(self) -> float:
        if self.is_all_day or not self.start or not self.end:
            return 0.0
        return max(0.0, (self.end - self.start).total_seconds() / 3600)


def parse_dt(value: Any) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(str(value).replace("Z", ""))
    except ValueError:
        return None


def load_events(brain_root: Path) -> tuple[list[Event], str | None]:
    path = brain_root / CALENDAR_CACHE
    if not path.is_file():
        return [], None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return [], None

    events = [
        Event(
            subject=str(raw.get("subject") or "(no subject)"),
            start=parse_dt(raw.get("start")),
            end=parse_dt(raw.get("end")),
            categories=list(raw.get("categories") or []),
            is_all_day=bool(raw.get("is_all_day")),
            project=raw.get("project") or None,
            location=str(raw.get("location") or ""),
            role=raw.get("role") or None,
        )
        for raw in data.get("events", [])
    ]
    return events, data.get("fetched_at")


def esc(value: Any) -> str:
    return html.escape(str(value if value is not None else ""))


def state_by_slug(states: list[ProjectState]) -> dict[str, ProjectState]:
    return {s.slug: s for s in states}


def project_detail(state: ProjectState | None) -> str:
    """The line that makes this dashboard worth opening."""
    if state is None:
        return ""
    bits: list[str] = []
    if state.pipeline_stage:
        bits.append(f"stage: {esc(state.pipeline_stage)}")
    if state.dirty_count:
        bits.append(f"<b>{state.dirty_count} uncommitted</b>")
    if state.unpushed_count:
        bits.append(f"<b>{state.unpushed_count} unpushed</b>")
    if state.last_commit_subject:
        bits.append(f"last: {esc(state.last_commit_subject[:60])}")
    return '<div class="pdetail">' + " &middot; ".join(bits) + "</div>" if bits else ""


CSS = """
:root{--ivory:#faf9f5;--paper:#fff;--slate:#141413;--clay:#d97757;
--g100:#f0eee6;--g200:#e6e3da;--g300:#d1cfc5;--g500:#87867f;--g700:#3d3d3a;
--work:#7c5cbf;--selfdl:#b8860b;--extdl:#b33d3d;--extappt:#4d7c5a;
--private:#9b7fb8;--dz:#4a6fa5;--other:#87867f;
--serif:ui-serif,Georgia,'Times New Roman',serif;
--sans:system-ui,-apple-system,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;
--mono:ui-monospace,'SF Mono',Menlo,Consolas,monospace;--radius:10px}
@media (prefers-color-scheme:dark){:root{--ivory:#1a1917;--paper:#222220;--slate:#e8e6e0;
--g100:#2a2926;--g200:#333230;--g300:#4a4945;--g500:#9a998f;--g700:#c8c6be;--clay:#e0896a;
--work:#a68bd9;--selfdl:#d4a72c;--extdl:#d46a6a;--extappt:#6fa07d;--private:#b79ccf;--dz:#6b8fc4}}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
body{background:var(--ivory);color:var(--slate);font-family:var(--sans);line-height:1.5;
padding:26px 18px 70px;-webkit-font-smoothing:antialiased}
.wrap{max-width:1280px;margin:0 auto}
h1{font-family:var(--serif);font-size:28px;font-weight:600;letter-spacing:-.02em}
.stamp{font-family:var(--mono);font-size:12px;color:var(--g500);margin-top:5px}
.stamp.stale{color:var(--extdl);font-weight:600}
.legend{display:flex;flex-wrap:wrap;gap:13px;margin:18px 0;font-size:12px;color:var(--g700)}
.legend span{display:flex;align-items:center;gap:5px}
.dot{width:10px;height:10px;border-radius:3px}
.dot.work{background:var(--work)}.dot.selfdl{background:var(--selfdl)}
.dot.extdl{background:var(--extdl)}.dot.extappt{background:var(--extappt)}
.dot.private{background:var(--private)}.dot.dz{background:var(--dz)}.dot.other{background:var(--other)}
.budget{display:flex;flex-wrap:wrap;gap:10px;margin-bottom:20px}
.bcard{background:var(--paper);border:1px solid var(--g200);border-radius:var(--radius);
padding:10px 14px;min-width:150px}
.bcard .r{font-family:var(--mono);font-size:11px;color:var(--g500);text-transform:uppercase}
.bcard .h{font-family:var(--serif);font-size:19px;font-weight:600;margin:2px 0 5px}
.bcard .track{height:5px;background:var(--g100);border-radius:3px;overflow:hidden}
.bcard .track i{display:block;height:100%;background:var(--clay)}
.bcard .track i.over{background:var(--extdl)}
.grid{display:grid;grid-template-columns:52px repeat(7,1fr);gap:5px;
background:var(--paper);border:1px solid var(--g200);border-radius:var(--radius);
padding:12px;overflow-x:auto}
.hd{font-family:var(--mono);font-size:11px;color:var(--g500);text-align:center;
padding-bottom:7px;border-bottom:1px solid var(--g200)}
.hd b{display:block;font-family:var(--serif);font-size:15px;color:var(--slate);font-weight:600}
.hd.today b{color:var(--clay)}
.hours{display:flex;flex-direction:column}
.hours div{font-family:var(--mono);font-size:10px;color:var(--g500);text-align:right;
padding-right:6px;border-top:1px solid var(--g100)}
.col{position:relative;border-left:1px solid var(--g100)}
.allday{font-size:10.5px;background:var(--g100);border-radius:4px;padding:2px 5px;
margin-bottom:3px;color:var(--g700);font-family:var(--mono)}
.ev{position:absolute;left:2px;right:2px;border-radius:6px;padding:4px 6px;overflow:hidden;
color:#fff;font-size:11.5px;line-height:1.3}
.ev.work{background:var(--work)}.ev.selfdl{background:var(--selfdl)}
.ev.extdl{background:var(--extdl)}.ev.extappt{background:var(--extappt)}
.ev.private{background:var(--private)}.ev.dz{background:var(--dz)}.ev.other{background:var(--other)}
.ev b{display:block;font-weight:600}
.ev .tm{font-family:var(--mono);font-size:9.5px;opacity:.85}
.pdetail{margin-top:3px;font-size:10px;opacity:.95;border-top:1px solid rgba(255,255,255,.35);padding-top:3px}
.empty{background:var(--paper);border:1px dashed var(--g300);border-radius:var(--radius);
padding:30px;text-align:center;color:var(--g500)}
.empty code{font-family:var(--mono);color:var(--clay);font-size:12.5px}
"""


def render_budgets(
    budgets: dict[str, float], events: list[Event], states: list[ProjectState]
) -> str:
    if not budgets:
        return ""
    booked: dict[str, float] = {}
    for event in events:
        if "Work Blocker" not in event.categories:
            continue
        role = resolve_event_role(
            {"role": event.role, "project": event.project}, states
        )
        booked[role] = booked.get(role, 0.0) + event.hours

    cards: list[str] = []
    for role, budget in sorted(budgets.items()):
        spent = booked.get(role, 0.0)
        pct = min(100.0, (spent / budget * 100) if budget else 0.0)
        over = " over" if budget and spent > budget else ""
        cards.append(
            f'<div class="bcard"><div class="r">{esc(role)}</div>'
            f'<div class="h">{spent:.1f} / {budget:.0f}h</div>'
            f'<div class="track"><i class="{over.strip()}" style="width:{pct:.0f}%"></i></div></div>'
        )
    return f'<div class="budget">{"".join(cards)}</div>'


def render_grid(week_start: datetime, events: list[Event], states: dict[str, ProjectState]) -> str:
    days = [week_start + timedelta(days=i) for i in range(7)]
    today = datetime.now().date()

    header = ['<div class="hd"></div>']
    for day in days:
        klass = "hd today" if day.date() == today else "hd"
        header.append(f'<div class="{klass}">{day:%a}<b>{day.day}</b></div>')

    hours_col = ['<div class="hours">']
    for hour in range(DAY_START, DAY_END):
        hours_col.append(f'<div style="height:{PX_PER_HOUR}px">{hour:02d}</div>')
    hours_col.append("</div>")

    columns: list[str] = []
    for day in days:
        same_day = [
            e for e in events if e.start and e.start.date() == day.date() and not e.is_all_day
        ]
        all_day = [e for e in events if e.is_all_day and e.start and e.start.date() == day.date()]

        blocks: list[str] = [
            f'<div class="allday">{esc(e.subject)}</div>' for e in all_day
        ]
        for event in sorted(same_day, key=lambda e: e.start):
            start_h = event.start.hour + event.start.minute / 60
            end_h = (event.end.hour + event.end.minute / 60) if event.end else start_h + 1
            top = (max(start_h, DAY_START) - DAY_START) * PX_PER_HOUR
            height = max(20.0, (min(end_h, DAY_END) - max(start_h, DAY_START)) * PX_PER_HOUR - 3)
            detail = project_detail(states.get(event.project)) if event.project else ""
            blocks.append(
                f'<div class="ev {event.css_class}" style="top:{top:.0f}px;height:{height:.0f}px">'
                f'<b>{esc(event.subject)}</b>'
                f'<span class="tm">{event.start:%H:%M}'
                f'{"-" + format(event.end, "%H:%M") if event.end else ""}</span>'
                f"{detail}</div>"
            )
        columns.append(
            f'<div class="col" style="height:{(DAY_END - DAY_START) * PX_PER_HOUR}px">'
            f'{"".join(blocks)}</div>'
        )

    return (
        f'<div class="grid">{"".join(header)}'
        f'{"".join(hours_col)}{"".join(columns)}</div>'
    )


def render_page(
    week_start: datetime,
    events: list[Event],
    states: list[ProjectState],
    budgets: dict[str, float],
    fetched_at: str | None,
    stamp: str,
) -> str:
    legend = "".join(
        f'<span><i class="dot {css}"></i>{label}</span>'
        for label, css in CATEGORY_CLASS.items()
    )

    stale_class = ""
    if fetched_at:
        try:
            age_h = (datetime.now() - datetime.fromisoformat(fetched_at)).total_seconds() / 3600
            freshness = f"calendar as of {fetched_at} ({age_h:.0f}h ago)"
            if age_h > 36:
                stale_class = " stale"
                freshness += " - STALE, run /week"
        except ValueError:
            freshness = f"calendar as of {fetched_at}"
    else:
        freshness = "no calendar data cached - run /week to pull it"
        stale_class = " stale"

    body = (
        render_budgets(budgets, events, states)
        + f'<div class="legend">{legend}</div>'
        + render_grid(week_start, events, state_by_slug(states))
        if events
        else '<div class="empty"><p>No calendar events cached for this week.</p>'
        "<p style=\"margin-top:9px\">Run <code>/week</code> to pull the calendar "
        "(read-only) and regenerate this page.</p></div>"
    )

    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Week of {week_start:%Y-%m-%d}</title><style>{CSS}</style></head>
<body><div class="wrap">
<h1>Week of {week_start:%d %B %Y}</h1>
<div class="stamp{stale_class}">generated {esc(stamp)} &middot; {esc(freshness)}</div>
{body}
</div></body></html>"""


def main(argv: list[str] | None = None) -> int:
    force_utf8_console()
    parser = argparse.ArgumentParser(description="Render the current week as an HTML dashboard.")
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--week", help="Monday of the week to render (YYYY-MM-DD).")
    parser.add_argument("--out", type=Path)
    parser.add_argument("--stamp")
    args = parser.parse_args(argv)

    brain_root = args.root if args.root.name == "_brain" else args.root / "_brain"
    if not brain_root.is_dir():
        print(f"error: no _brain directory at {brain_root}", file=sys.stderr)
        return 1

    week_start = (
        datetime.strptime(args.week, "%Y-%m-%d") if args.week else monday_of(datetime.now())
    )
    events, fetched_at = load_events(brain_root)
    states = scan_all(brain_root, ("active",), since=None)
    budgets = load_role_budgets(brain_root)
    stamp = args.stamp or datetime.now().strftime("%Y-%m-%d %H:%M")

    out_path = args.out or (brain_root / "week.html")
    out_path.write_text(
        render_page(week_start, events, states, budgets, fetched_at, stamp), encoding="utf-8"
    )
    print(f"Wrote {out_path} ({len(events)} event(s), week of {week_start:%Y-%m-%d})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
