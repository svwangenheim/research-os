---
name: week
description: Refresh the live week view - pull the calendar (read-only), reconcile the weekly plan's machine-owned block, and regenerate week.html with project state inside each block. Use on "week", "what's my week", "refresh the dashboard", or after the calendar changes.
argument-hint: "[--no-calendar] [--week YYYY-MM-DD]"
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, ToolSearch
---

# Week

Keeps the week honest between Fridays. Three things, in order: pull the
calendar, reconcile the plan, regenerate the dashboard.

**Outputs:** `_brain/.calendar-cache.json` · the `week-state` block inside
`_brain/weekly/<monday>.md` · `_brain/week.html`

---

## Step 1 — Pull the calendar into the cache

A plain script cannot reach Microsoft 365; that connector only exists inside a
Claude session. So this skill is the fetcher and the scripts are the renderers.

Use `ToolSearch` for an Outlook calendar tool (`"outlook calendar"`). Then:

1. Search the current week, Monday 00:00 → Sunday 23:59 (or `--week`'s Monday).
2. Write `_brain/.calendar-cache.json`:

```json
{
  "fetched_at": "<ISO 8601 local time>",
  "week_start": "<YYYY-MM-DD>",
  "previous_events": [ ...the `events` array from the cache you are replacing... ],
  "events": [
    {
      "id": "<stable event id>",
      "subject": "...",
      "start": "2026-08-12T10:30:00",
      "end": "2026-08-12T18:00:00",
      "categories": ["Work Blocker"],
      "is_all_day": false,
      "location": "",
      "project": "<_brain/projects slug, or null>",
      "role": "<phd|dz-modelling|dz-outreach|admin, or null>"
    }
  ]
}
```

**Carry the old `events` array into `previous_events` before overwriting.** That
diff is what lets the reconciler report what moved — without it, "calendar
changes since the plan was written" is permanently empty.

**Linking `project` is the step that makes the dashboard worth opening.** Match
the event subject against project titles and slugs from
`_brain/projects/*.md`. Be conservative: a wrong link puts the wrong blockers on
the wrong block, which is worse than no link. Leave `null` when unsure.

Set `role` only when you are confident. Otherwise leave it `null` — the
reconciler derives it from the linked project.

**The connector is read-only for this account** (org policy blocks
`outlook_create_event`). Never attempt to create, move, or delete an event. If
the tool is unavailable or unauthorized, say so **once**, keep any existing
cache rather than truncating it, and continue to Steps 2–3 — a stale calendar
with a visible timestamp is far more useful than no dashboard.

With `--no-calendar`, skip this step entirely and re-render from the cache.

## Step 2 — Reconcile the weekly plan

```bash
python "${CLAUDE_PLUGIN_ROOT}/scripts/reconcile_week.py" --root <vault>
```

Rewrites **only** the `@generated:start week-state` block: calendar changes,
newly observed commitments, the role-hour burn-down, and drift flags.
Everything outside that block is yours and is never touched.

If there is no weekly file for this week, the script says so and stops. Offer
`/weekly-planning`; do not author a week's plan here.

**Never edit inside those markers by hand**, and never move the markers.

## Step 3 — Regenerate the dashboard

```bash
python "${CLAUDE_PLUGIN_ROOT}/scripts/generate_week_dashboard.py" --root <vault>
```

Writes `_brain/week.html` — the week grid coloured by Outlook category, with
each linked block carrying its project's live stage, uncommitted count,
unpushed count, and last commit.

## Step 4 — Report

Three or four lines, no more:

- what changed on the calendar since the last pull (or that nothing did)
- any drift flags the reconciler raised, especially loss risk
- the burn-down in one line: hours booked vs budget per role
- the dashboard path, and the cache's age if the fetch was skipped

Then stop. The dashboard is the artifact; do not re-describe it in prose.

---

## Who else calls this

`reconcile_week.py` and `generate_week_dashboard.py` are also invoked by
morning-brief (daily), pending-sweep, and weekly-planning — so the week stays
current without anyone running `/week`. Run it by hand when the calendar has
just changed and you want the view now.

## Guardrails

Do not:
- attempt any calendar write — read-only account, no exceptions
- fail the whole run because the connector is unavailable — cache staleness is visible, that is the design
- overwrite the cache without carrying `events` into `previous_events`
- guess a `project` link — leave it null
- edit anything inside the `@generated` markers
- author or restructure the weekly plan — that is `/weekly-planning`
- present the dashboard as live: it is a snapshot with a timestamp, and the timestamp is shown for a reason
