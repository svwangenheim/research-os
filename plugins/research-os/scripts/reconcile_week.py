#!/usr/bin/env python3
"""
Keep the weekly plan current between Fridays.

The weekly file used to be written once and left to rot: by Wednesday its goals
no longer matched the calendar, and anything the morning brief noticed died in a
log instead of updating the plan it invalidated.

This script rewrites exactly one region of that file -- the block between

    <!-- @generated:start week-state -->
    <!-- @generated:end -->

-- and never touches a byte outside it. That boundary is the whole safety story:
goals, the check-off, and the open timeslots stay human-owned, so an unattended
routine can reconcile the plan without ever being able to rewrite your thinking.
The same marker convention already governs project-note Orientation blocks.

Arithmetic (hours booked, budget remaining, days to deadline) is computed here,
not narrated by a model -- the house rule from docs/09: the engine owns the
numbers.

Usage:
    python reconcile_week.py --root <vault>
    python reconcile_week.py --root <vault> --check    # report, write nothing
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))

from project_state_scan import ProjectState, scan_all  # noqa: E402
from wiki_quality_check import parse_frontmatter  # noqa: E402
from wiki_quality_check import force_utf8_console  # noqa: E402

BLOCK_START = "<!-- @generated:start week-state -->"
BLOCK_END = "<!-- @generated:end -->"
CALENDAR_CACHE = ".calendar-cache.json"

# Which Outlook categories count as real work against a role budget. Meetings
# and appointments are commitments but not project hours, so they are reported
# separately rather than silently inflating the burn-down.
WORK_CATEGORIES = ("Work Blocker",)


@dataclass
class WeekFile:
    path: Path
    text: str
    week_start: str


def monday_of(day: datetime) -> datetime:
    return day - timedelta(days=day.weekday())


def find_week_file(brain_root: Path, today: datetime) -> WeekFile | None:
    """The weekly note for the current week, if it exists. Never creates one --
    authoring a week's plan is /weekly-planning's job, not the reconciler's."""
    week_start = monday_of(today).strftime("%Y-%m-%d")
    path = brain_root / "weekly" / f"{week_start}.md"
    if not path.is_file():
        return None
    try:
        return WeekFile(path, path.read_text(encoding="utf-8", errors="replace"), week_start)
    except OSError:
        return None


def load_calendar(brain_root: Path) -> dict[str, Any]:
    """Read the calendar cache written by /week.

    A plain script cannot reach Microsoft 365 -- that connector lives inside a
    Claude session -- so the skill fetches and caches, and this reads. The cache
    carries its own fetched_at so staleness is always visible rather than
    assumed away.
    """
    path = brain_root / CALENDAR_CACHE
    if not path.is_file():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def load_role_budgets(brain_root: Path) -> dict[str, float]:
    """Weekly hour targets per role, from the `roles:` block in profile.md."""
    path = brain_root / "profile.md"
    if not path.is_file():
        return {}
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return {}

    budgets: dict[str, float] = {}
    in_block = False
    for line in text.split("\n"):
        stripped = line.strip()
        if stripped.startswith("<!-- roles:"):
            in_block = True
            continue
        if in_block:
            if stripped.startswith("-->"):
                break
            if ":" in stripped:
                key, _, value = stripped.lstrip("- ").partition(":")
                try:
                    budgets[key.strip()] = float(value.strip().split()[0])
                except (ValueError, IndexError):
                    continue
    return budgets


def event_hours(event: dict[str, Any]) -> float:
    if event.get("is_all_day"):
        return 0.0
    try:
        start = datetime.fromisoformat(str(event["start"]))
        end = datetime.fromisoformat(str(event["end"]))
    except (KeyError, ValueError):
        return 0.0
    return max(0.0, (end - start).total_seconds() / 3600.0)


def resolve_event_role(event: dict[str, Any], states: list[ProjectState]) -> str:
    """Which role's budget an event spends against.

    Three sources, most authoritative first: a `role` the caching skill wrote
    onto the event; the role of the project the event is linked to; otherwise
    unassigned. Without this the burn-down silently reports zero for every role
    while the week fills up, which is worse than showing nothing.
    """
    explicit = event.get("role")
    if explicit:
        return str(explicit)

    project = event.get("project")
    if project:
        for state in states:
            if state.slug == project:
                return state.role_hint if state.role_hint != "unknown" else "unassigned"
    return "unassigned"


def booked_hours_by_role(
    calendar: dict[str, Any], states: list[ProjectState] | None = None
) -> dict[str, float]:
    booked: dict[str, float] = defaultdict(float)
    for event in calendar.get("events", []):
        categories = event.get("categories") or []
        if not any(c in WORK_CATEGORIES for c in categories):
            continue
        booked[resolve_event_role(event, states or [])] += event_hours(event)
    return dict(booked)


def calendar_changes(calendar: dict[str, Any]) -> list[str]:
    """Events added, moved or cancelled since the snapshot the plan was written against."""
    previous = {e.get("id"): e for e in calendar.get("previous_events", []) if e.get("id")}
    current = {e.get("id"): e for e in calendar.get("events", []) if e.get("id")}
    if not previous:
        return []

    changes: list[str] = []
    for event_id, event in current.items():
        old = previous.get(event_id)
        if old is None:
            changes.append(f"NEW: {event.get('subject')} - {event.get('start')}")
        elif old.get("start") != event.get("start"):
            changes.append(
                f"MOVED: {event.get('subject')} - {old.get('start')} -> {event.get('start')}"
            )
    for event_id, old in previous.items():
        if event_id not in current:
            changes.append(f"GONE: {old.get('subject')} - was {old.get('start')}")
    return changes


DEADLINE_CATEGORIES = ("Self-imposed Deadline", "External Deadline")
COMMITMENT_LOOKAHEAD_DAYS = 14


def load_life_admin(brain_root: Path) -> list[tuple[datetime, str]]:
    """Optional, personal, deliberately outside Outlook: a flat list of
    `- YYYY-MM-DD: description` lines in `_brain/life-admin.md`. Read if
    present; absence is normal, not an error -- nothing here is invented.
    """
    path = brain_root / "life-admin.md"
    if not path.is_file():
        return []
    entries: list[tuple[datetime, str]] = []
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return []
    for line in text.split("\n"):
        stripped = line.strip()
        if not stripped.startswith("- "):
            continue
        rest = stripped[2:]
        date_part, sep, desc = rest.partition(":")
        if not sep:
            continue
        try:
            date = datetime.strptime(date_part.strip()[:10], "%Y-%m-%d")
        except ValueError:
            continue
        entries.append((date, desc.strip()))
    return entries


def upcoming_commitments(
    calendar: dict[str, Any], brain_root: Path, today: datetime
) -> list[tuple[datetime, str, str]]:
    """Everything with a date attached in the next COMMITMENT_LOOKAHEAD_DAYS,
    across DZ + PhD + life -- one system, per the explicit scope decision
    that a sweep seeing only one of them systematically overstates available
    time. Returns (date, description, source) sorted by date.

    Deadlines are read from the calendar's OWN categories (`Self-imposed
    Deadline`, `External Deadline`) rather than a free-text scanner over
    project notes -- no project currently has a structured deadline field,
    and guessing dates out of prose is exactly the kind of unreliable
    heuristic this system tries to avoid elsewhere (see project_state_scan.py
    preferring git's index over a directory walk).
    """
    horizon = today + timedelta(days=COMMITMENT_LOOKAHEAD_DAYS)
    commitments: list[tuple[datetime, str, str]] = []

    for event in calendar.get("events", []):
        categories = event.get("categories") or []
        if not any(c in DEADLINE_CATEGORIES for c in categories):
            continue
        start = event.get("start")
        if not start:
            continue
        try:
            when = datetime.fromisoformat(str(start).replace("Z", ""))
        except ValueError:
            continue
        if today <= when <= horizon:
            commitments.append((when, str(event.get("subject") or "(untitled)"), "calendar"))

    for when, description in load_life_admin(brain_root):
        if today <= when <= horizon:
            commitments.append((when, description, "life-admin"))

    return sorted(commitments, key=lambda c: c[0])


def has_time_booked_before(
    deadline: datetime, calendar: dict[str, Any], today: datetime
) -> bool:
    """Any Work Blocker between today and the deadline counts -- this does
    not try to link a specific block to a specific deadline (nothing in the
    calendar schema ties them together); it answers the coarser, still
    useful question: is ANY work time booked before this lands at all."""
    for event in calendar.get("events", []):
        if "Work Blocker" not in (event.get("categories") or []):
            continue
        start = event.get("start")
        if not start:
            continue
        try:
            when = datetime.fromisoformat(str(start).replace("Z", ""))
        except ValueError:
            continue
        if today <= when < deadline:
            return True
    return False


def drift_flags(
    states: list[ProjectState],
    calendar: dict[str, Any],
    budgets: dict[str, float],
    booked: dict[str, float],
    today: datetime,
    brain_root: Path | None = None,
) -> list[str]:
    """The point of reconciling: what the plan now gets wrong."""
    flags: list[str] = []

    if brain_root is not None:
        for when, description, source in upcoming_commitments(calendar, brain_root, today):
            days_out = (when.date() - today.date()).days
            if not has_time_booked_before(when, calendar, today):
                flags.append(
                    f"[{source}] '{description}' due in {days_out}d ({when:%Y-%m-%d}) - "
                    f"no work time booked before it"
                )

    for role, budget in sorted(budgets.items()):
        spent = booked.get(role, 0.0)
        if budget and spent > budget:
            flags.append(f"{role}: {spent:.1f}h booked against a {budget:.0f}h budget - over by {spent - budget:.1f}h")
        elif budget and spent == 0 and today.weekday() >= 2:
            flags.append(f"{role}: {budget:.0f}h budgeted but nothing booked, and it is already {today:%A}")

    heavy = [s for s in states if s.dirty_count >= 10]
    for state in sorted(heavy, key=lambda s: -s.dirty_count):
        flags.append(
            f"{state.slug}: {state.dirty_count} uncommitted files - loss risk, run /pending"
        )

    unpushed = [s for s in states if s.unpushed_count]
    for state in unpushed:
        flags.append(f"{state.slug}: {state.unpushed_count} commit(s) unpushed")

    for state in states:
        if any("not a git repository" in err for err in state.errors):
            flags.append(f"{state.slug}: not a git repo - invisible to every routine")

    fetched = calendar.get("fetched_at")
    if fetched:
        try:
            age_h = (today - datetime.fromisoformat(str(fetched))).total_seconds() / 3600
            if age_h > 36:
                flags.append(f"calendar cache is {age_h:.0f}h old - run /week to refresh")
        except ValueError:
            pass
    else:
        flags.append("no calendar data cached - run /week to pull it")

    return flags


def render_block(
    states: list[ProjectState],
    calendar: dict[str, Any],
    budgets: dict[str, float],
    today: datetime,
    brain_root: Path | None = None,
) -> str:
    booked = booked_hours_by_role(calendar, states)
    lines = [
        BLOCK_START,
        "",
        f"## Week state (as of {today:%Y-%m-%d %H:%M})",
        "",
        "*Machine-written. Everything outside this block is yours and is never touched.*",
        "",
    ]

    changes = calendar_changes(calendar)
    lines.append("### Calendar changes since the plan was written")
    lines.extend([f"- {c}" for c in changes] if changes else ["- None detected."])
    lines.append("")

    lines.append("### Newly observed commitments (inbox - promote by hand)")
    inbox = [
        f"- {e.get('subject')} ({e.get('start')})"
        for e in calendar.get("events", [])
        if e.get("is_new_since_plan")
    ]
    lines.extend(inbox or ["- None."])
    lines.append("")

    lines.append(f"### Deadlines in the next {COMMITMENT_LOOKAHEAD_DAYS} days (DZ + PhD + life)")
    if brain_root is not None:
        commitments = upcoming_commitments(calendar, brain_root, today)
        if commitments:
            for when, description, source in commitments:
                booked_flag = "time booked" if has_time_booked_before(when, calendar, today) else "**NOTHING BOOKED**"
                lines.append(f"- {when:%Y-%m-%d} [{source}] {description} - {booked_flag}")
        else:
            lines.append("- None found (calendar deadline categories + `_brain/life-admin.md`).")
    else:
        lines.append("- Skipped -- no brain root given.")
    lines.append("")

    lines.append("### Role-hour burn-down")
    if budgets:
        lines.append("")
        lines.append("| Role | Booked | Budget | Left |")
        lines.append("|---|---|---|---|")
        for role, budget in sorted(budgets.items()):
            spent = booked.get(role, 0.0)
            lines.append(f"| {role} | {spent:.1f}h | {budget:.0f}h | {budget - spent:.1f}h |")
    else:
        lines.append("- No `roles:` budgets set in `_brain/profile.md` - add them to enable this.")
    lines.append("")

    lines.append("### Drift flags")
    flags = drift_flags(states, calendar, budgets, booked, today, brain_root)
    lines.extend([f"- {f}" for f in flags] if flags else ["- Nothing drifting."])
    lines.append("")
    lines.append(BLOCK_END)
    return "\n".join(lines)


def splice(text: str, block: str) -> tuple[str, bool]:
    """Replace the generated block, or append it if the file has none yet."""
    start = text.find(BLOCK_START)
    end = text.find(BLOCK_END)
    if start == -1 or end == -1 or end < start:
        separator = "" if text.endswith("\n") else "\n"
        return text + separator + "\n" + block + "\n", False
    return text[:start] + block + text[end + len(BLOCK_END):], True


def main(argv: list[str] | None = None) -> int:
    force_utf8_console()
    parser = argparse.ArgumentParser(description="Reconcile the current weekly plan in place.")
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--check", action="store_true", help="Report only; write nothing.")
    parser.add_argument("--date", help="Override today (YYYY-MM-DD), for tests.")
    args = parser.parse_args(argv)

    brain_root = args.root if args.root.name == "_brain" else args.root / "_brain"
    if not brain_root.is_dir():
        print(f"error: no _brain directory at {brain_root}", file=sys.stderr)
        return 1

    today = datetime.strptime(args.date, "%Y-%m-%d") if args.date else datetime.now()

    week = find_week_file(brain_root, today)
    if week is None:
        monday = monday_of(today).strftime("%Y-%m-%d")
        print(f"No weekly file for the week of {monday}. Run /weekly-planning first.")
        return 0

    states = scan_all(brain_root, ("active",), since=None)
    calendar = load_calendar(brain_root)
    budgets = load_role_budgets(brain_root)

    block = render_block(states, calendar, budgets, today, brain_root)
    updated, replaced = splice(week.text, block)

    if args.check:
        print(block)
        print(f"\n[check] would {'replace' if replaced else 'append'} the block in {week.path}")
        return 0

    if updated == week.text:
        print(f"No change to {week.path}")
        return 0

    week.path.write_text(updated, encoding="utf-8")
    print(f"{'Replaced' if replaced else 'Appended'} week-state block in {week.path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
