---
name: workflow-audit
description: Inventory and score the recurring work across all your roles, so the highest-leverage processes can become procedures. Evidence-prefilled, then a conversation. Use on "workflow audit", "what should I automate", or before building procedures.
argument-hint: "[--refresh | --role <phd|dz-modelling|dz-outreach|admin>]"
allowed-tools: Read, Grep, Glob, Bash, ToolSearch
---

# Workflow Audit

Step 1 of the workflow layer: find out what you actually do, then rank it by how
much of it can be handed over.

**Input:** `$ARGUMENTS` — optional flags to re-run the evidence pass or restrict the audit to one role. Omitted, it audits every role.

**Output:** `_brain/workflow-audit.md` — a scored inventory. The top entries
become the first cohort of procedures via `/automate new`.

This runs **once properly**, then gets refreshed occasionally (`--refresh`
re-runs the harvest and re-scores, preserving your corrections). It is not a
routine.

---

## Why this is evidence-prefilled

Memory under-reports recurring work. People remember the interesting things they
did and forget the twelve small repeatable ones that eat the week — which are
exactly the automatable ones. So the machine brings the list and you correct it.

That inverts the usual cost: you spend the session **ruling on** an inventory
rather than **generating** one.

---

## Phase 1 — Evidence harvest (autonomous, no questions)

Gather first. Do not ask anything yet.

```bash
python "${CLAUDE_PLUGIN_ROOT}/scripts/project_state_scan.py" --root <vault> --since "28 days ago" --format json
```

**Critical performance constraint:** the project repos are on OneDrive with
Files-On-Demand, where directory traversal runs ~20x slower than local. Use the
scan above and targeted `git log`; **never** recursively glob inside a project
root. A previous unattended run that explored freely blocked for 25 minutes.

Sources, in order of value:

| Source | What it reveals |
|---|---|
| `git log --since="28 days ago" --format="%ad %s" --date=short` per project | the work that produced artifacts — commit *subjects* cluster into recurring task types |
| `_brain/daily/*.md`, `_brain/weekly/*.md` | what was worked on, what recurred, what got flagged repeatedly |
| project `Orientation` blocks and `00_admin/process/journal.md` | the shape of each project's own loop |
| Outlook calendar (read-only) via `ToolSearch` | **recurring meetings** — the single largest category of work that leaves no git trace |
| `_brain/learning/`, `_brain/synthesis/` | processes described in passing but never written down |

Cluster commit subjects and calendar recurrences into **candidate tasks**. A
candidate is a *type* of work ("triage a new paper into the wiki"), never a
single instance ("read Barbieri 2023").

Produce a draft inventory: task, observed frequency, evidence links, guessed
role. Expect 15–30 candidates. Do not score yet.

## Phase 2 — The interview (Socratic, conversational)

**This is a conversation, not a form.** Follow the house interview style used by
`/discover interview`:

- Ask in plain text, **one or two questions at a time**, and wait.
- **Do not use `AskUserQuestion`.**
- Be curious, not prescriptive. Draw out how the work is actually done.
- Build each question on the last answer.
- Know when to stop — if a role is clear after four or five exchanges, move on.

Open by showing the draft inventory for **one role at a time**, not all at once.
Then work through three passes per role.

`--role <phd|dz-modelling|dz-outreach|admin>` narrows the audit to a single role
and runs the three passes for that one only. Use it when returning to finish a
role left half-done, or when only one part of the work has changed. Without it,
every role is walked in turn.

The three passes:

**Pass A — correct the list.** "Here's what the evidence says you do repeatedly
in `<role>`. What's wrong, what's missing, what's actually two different
things?"

**Pass B — surface the invisible work.** This is the part evidence cannot reach,
and it is usually half the week. Ask about it directly:
reading and literature triage · thinking and design time · supervision and
supervisor prep · co-author and colleague coordination · teaching · seminars and
talks · reviewing for others · outreach and press · admin, funding, ethics,
reimbursements.

**Pass C — find the veto.** For anything touching sensitive data, ask what must
never be automated, and why. Record the reason, not just the flag.

**PhD is interviewed now**, not deferred. Four PhD designs are already active
(job insecurity, housing insecurity, parcel couriers, judges × local shocks) and
have their own recurring loops — lit triage, design filtering, estimation runs,
critic passes. Write those from current practice; the run log corrects them in
place as the PhD formally begins.

## Phase 3 — Score and rank

```
clone_score = (frequency_wt × time_per_run × repeatability × traceability) / judgment_load
```

Each component 1–5, scored **from the conversation, not invented**. Record every
component separately — re-weighting later must never require re-interviewing.

| Component | 1 | 5 |
|---|---|---|
| `frequency_wt` | a few times a year | daily |
| `time_per_run` | minutes | a full day |
| `repeatability` | improvised each time | identical steps every time |
| `traceability` | Claude can neither see the inputs nor verify the output | fully observable and checkable |
| `judgment_load` (divisor) | mechanical | irreducible research judgment |

Normalize to 0–100 for readability. **The ranking is a prompt for discussion, not
a verdict** — a task's score says how *clonable* it is, never how *valuable*.

### The veto flag is not a low score

Some work must never be automated whatever it scores. The reference case is
**AD-5**: Claude must never read, process, log, or cache real SOEP microdata in
any form. Vetoed work gets `automation: vetoed` and a permanent `veto_reason`,
and a low score would *not* be an adequate substitute — scores get recomputed,
vetoes must survive that.

High `judgment_load` is a different thing: identification decisions, referee
responses, and design choices score high because they are the researcher's
actual job. They are not automation targets and that is not a defect.

## Phase 4 — Write `_brain/workflow-audit.md`

```markdown
---
title: "Workflow Audit"
note_type: workflow-audit
updated: "<YYYY-MM-DD>"
---

# Workflow Audit — <YYYY-MM-DD>

## Method
<!-- harvest window, what was interviewed, what is inferred vs. stated -->

## Inventory

### <role>

| Task | Freq | Time | Repeat | Trace | Judgment | Score | Automation | Evidence |
|---|---|---|---|---|---|---|---|---|

## The first cohort
<!-- top ~8 by score, excluding vetoed — these become procedures -->

## Vetoed — never automate
<!-- task, and the reason, stated in full -->

## Open questions
<!-- anything the interview could not settle -->
```

Mark clearly which rows are **stated** by the user and which are **inferred**
from evidence — a later reader must be able to tell.

## Phase 5 — Hand off

Report the top cohort and offer: *"Shall we write the first of these as a
procedure?"* → `/automate new <task>`. Do not write procedures in this skill.

## Guardrails

Do not:
- ask before harvesting — arriving empty-handed is the failure this skill exists to avoid
- use `AskUserQuestion` for the interview — it is a conversation
- recursively glob inside project roots — it is slow enough to hang the session
- score a component the user never gave you evidence or an answer for — leave it null and say so
- treat a high score as a recommendation, or a low one as a dismissal
- let a veto be represented as a low score
- write procedure notes here — that is `/automate new`
- defer the PhD role because it "starts in October"
