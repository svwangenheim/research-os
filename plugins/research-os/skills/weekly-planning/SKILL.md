---
name: weekly-planning
description: End-of-week routine — reviews what was planned last week against what actually happened (from _brain/daily/), checks in on new projects, sets this week's goals and open work timeslots, and creates non-conflicting color-coded Microsoft 365 calendar blockers (if authorized; degrades gracefully otherwise). Use at the end of a work week, or when the user says "weekly planning", "plan my week", "weekly review", or similar.
argument-hint: "[none — fully conversational]"
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, ToolSearch
---

# Weekly Planning

End-of-week review and next-week planning, rolled into the second brain.

## Step 1 — Gather the week's record

Read every `_brain/daily/*.md` for the past 7 days. Read the most recent
`_brain/weekly/*.md`, if one exists — it holds last week's stated goals and
timeslots, the thing this session checks off.

If no prior weekly file exists (first run), skip Step 2 and go straight to
Step 3 — there's nothing to check off yet.

## Step 2 — Check off last week's plan

**Conversational, not a checklist form.** Walk through last week's stated
goals one or two at a time: "Last week you planned to `<goal>` — how did
that go?" Accept free-text status (done / partial / dropped / still
ongoing), not just a binary checkbox. Let the daily entries inform the
conversation rather than asking the user to reconstruct everything from
memory — e.g. "I see commits in `<project>` on Tuesday and Thursday related
to this."

## Step 3 — New projects

Ask directly: "Any new projects to start tracking this week?" If yes and the
project doesn't exist yet, point to `/create-project`; this skill doesn't
scaffold projects itself.

## Step 4 — Set this week's goals and timeslots

Two distinct things, both conversational:
1. **Goals to finish this week** — concrete, project-tied where possible.
2. **Open work timeslots** — blocks of general project time with no fixed
   deliverable, not just goal-deadlines. Ask roughly how much of each kind
   the user wants this week rather than assuming a ratio.

## Step 5 — Calendar blockers (best-effort, graceful)

Use `ToolSearch` to look for an available Microsoft 365 calendar tool.
Requires the M365 connector authorized in claude.ai's connector settings —
cannot be done from within a skill.

- **If found:**
  1. Read the existing calendar for the coming week first — don't create
     anything until you know what's already there.
  2. Propose blocks for each goal/timeslot from Step 4, checked against
     existing events for conflicts. Assign a distinct color per category
     (e.g. goal-deadline work vs. open project time vs. admin) — ask the
     user's preferred mapping once, then reuse it in later runs (record it
     in `_brain/profile.md`'s standing context if not already there).
  3. Confirm the proposed blocks with the user before creating them — show
     day/time/color, don't create silently.
- **If not found:** say so once, write the goals/timeslots into the weekly
  file anyway (Step 6), and note that calendar blocks weren't created.

## Step 6 — Write the weekly file

`_brain/weekly/<YYYY-MM-DD>.md`, dated to the Monday of the week being
planned. Also capture a few forward-looking questions for next week, biased
toward contradictions noticed, entities that keep co-occurring but aren't
linked, and next actions left unnamed. The canonical layout is the shipped
template `${CLAUDE_PLUGIN_ROOT}/templates/brain-notes/weekly_template.md`;
the block below is the same content, inline as a fallback:

```markdown
---
title: "Weekly Plan — week of <YYYY-MM-DD>"
note_type: weekly
updated: "<YYYY-MM-DD>"
---

# Week of <YYYY-MM-DD>

## Last week's check-off
- <goal> — <done/partial/dropped, with the free-text note>

## This week's goals
- <goal>

## Open work timeslots
- <timeslot description>

## Calendar
- <blocks created, or "not created — connector not authorized / declined">

## Questions for next week
- <open threads for future-me: contradictions noticed, entities that keep co-occurring but aren't linked, next actions left unnamed>
```

## Step 7 — Report

Summarize what was checked off, this week's goals/timeslots, and calendar
status.

## Guardrails

Do not:
- reduce last week's check-off to a binary checkbox — the free-text status
  is the point, it's what makes next week's planning informed
- create calendar events without showing the proposed blocks first
- create a second weekly file for the same week — update the existing one
- assume a color mapping the user hasn't actually confirmed once
- scaffold a new project directly — hand off to `/create-project`
