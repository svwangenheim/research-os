# Scheduled agents

Four routines keep the second brain and wikis current without manual prompting.
They follow the plan's automation principle: **detection is autonomous; mutation
is bounded and supervised.** A scheduled run never canonicalizes a wiki, never
creates calendar events, and never writes into `_brain/` beyond what the named
skill already does deterministically — anything needing judgment is drafted or
flagged for a human confirm.

## How to instantiate

These are **specs**, not live jobs. Register them with the `/schedule` skill
(cloud cron routines) or, on a machine that stays on, `/loop`. Times are local.
Set them up once; edit the crons to taste. To register, run `/schedule` and give
it each routine's cron + prompt below.

Requires: a registered vault (`~/.claude/vaults.json`) for the vault-aware runs;
Microsoft 365 / Slack connectors for comms + calendar (degrade gracefully if
absent).

## The four routines

### 1. Morning brief — `0 9 * * *` (daily 09:00) — READ-ONLY

> Read-only morning brief. Do not modify any file. Report, in a few lines:
> what's pending across my active projects (scan each project's `passport.yaml`
> `pipeline.current_stage` and open plan items), the single next step per project,
> any due engram reviews (`/recall` would clear them — just say how many), and
> today's calendar if the Microsoft 365 connector is authorized. No writes.

### 2. Nightly consolidation — `0 22 * * *` (daily 22:00) — BOUNDED MUTATION

> Run the deterministic half of `/daily-summary`: for each project touched today,
> commit today's work locally (never push, never PR) and write/update today's
> `_brain/daily/<YYYY-MM-DD>.md`. Then **flag, don't do**: list any durable
> knowledge that looks unpushed (unchecked items in `wiki-links.md`) and any
> contradictions noticed — leave `/wiki-push` and wiki canonicalization for me.
> Do not touch the thematic wikis.

### 3. Weekly review + planning — `30 16 * * 5` (Fri 16:30) — DRAFT

> Run `/weekly-planning` in draft mode: review this week's `_brain/daily/*.md`,
> draft `_brain/weekly/<Monday>.md` (last week's check-off, this week's goals,
> open work timeslots, and Questions for next week). **Propose** calendar blocks
> but do not create them — leave the proposed blocks in the note for me to confirm.

### 4. Weekly vault-health audit — `0 15 * * 5` (Fri 15:00, before planning) — READ-ONLY

> Read-only audit. Run:
> `python "${CLAUDE_PLUGIN_ROOT}/scripts/wiki_quality_check.py" --root "<vault root>"`
> (covers every wiki + the `_brain/` personal layer) and report the findings
> grouped by wiki and for `_brain/` (frontmatter gaps, catalog-invisible project
> notes, stale active projects, duplicates, broken links, index/log staleness).
> Also surface any `WIKI-PENDING` sources. Do not remediate — this is a report I
> act on (via `/wiki-maintain` for wikis, `/checkpoint` for project notes).

## Guardrails (all routines)

- No autonomous wiki canonicalization, merging, or synthesis — that stays
  command-invoked and verifier-gated.
- No calendar events created without a human confirm.
- No pushes or PRs — nightly commits locally only.
- Reports and drafts are the output; the human decides what to act on.
