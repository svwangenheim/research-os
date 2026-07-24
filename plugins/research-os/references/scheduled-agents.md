# Scheduled agents

Four routines keep the second brain and wikis current without manual prompting.
They follow the plan's automation principle: **detection is autonomous; mutation
is bounded and supervised.** A scheduled run never canonicalizes a wiki, never
creates calendar events, and never writes into `_brain/` beyond what the named
skill already does deterministically — anything needing judgment is drafted or
flagged for a human confirm.

## Cloud vs. local — why only two of these run unattended

`/schedule` creates **cloud** routines: each run spawns an isolated cloud
sandbox that clones a named GitHub repo and works only inside that clone. It
has no access to your local machine, so it cannot see local project folders
or commit into local project git repos. That makes only the two read-only
routines — **morning brief** and **weekly vault-health audit** — genuinely
runnable in the cloud, scoped to what a clone of the vault repo can see.

**Nightly consolidation** and **weekly review + planning** stay manual/local
for now: the former commits directly in local project repos and is
guardrailed to *never push* (a cloud sandbox's commit can't reach your local
disk at all, so faithfully honoring "local commits only" is only possible
from a local execution model); the latter reads per-project state that lives
outside the vault, which a cloud clone of the vault alone can't see. Both
can be run by hand any time (see below), or wired up later via `/loop` on a
machine that stays on, which does have local access.

Making all four fully cloud-native would require: pushing every project to
its own private repo, a registry file listing them so a routine's prompt can
discover which to clone, and redefining nightly consolidation's guardrail
from "commit locally, never push" to "commit and push to that project's own
private repo" — a real posture change (an unattended bot gets push access to
your project repos overnight) that hasn't been adopted here.

## The two cloud routines

Registered via `/schedule` against the private repo `svw-dz/research-os-vault`
(vault pushed there specifically to enable this). Cron is stored in UTC;
times below assume Europe/Berlin summer time (CEST, UTC+2) — adjust the cron
by an hour around DST changes if you want the local time to stay fixed.

### 1. Morning brief — `0 7 * * *` UTC (09:00 Europe/Berlin) — READ-ONLY, cloud

> Read-only morning brief, scoped to what the cloned vault repo can see (no
> access to local project-folder repos, so it cannot report per-project
> pipeline status — note that limitation in one line). Do not modify any
> file. Report in a few lines: any due spaced-repetition reviews (estimate
> from `_brain/learning/`'s FSRS state — just the count, don't run a
> review), anything unresolved or flagged in the last 1-2 days of
> `_brain/daily/*.md`, and any open goals/timeslots from the most recent
> `_brain/weekly/` note. No writes, no commits, no push.

### 2. Weekly vault-health audit — `0 13 * * 5` UTC (Fri 15:00 Europe/Berlin) — READ-ONLY, cloud

> Read-only audit of the cloned vault repo. Since the plugin's
> `wiki_quality_check.py` isn't available in this clone, perform the
> equivalent checks directly: frontmatter gaps, stale `_brain/projects/`
> notes, duplicate or near-duplicate pages, broken wikilinks, and whether
> `index.md`/`log.md` look stale relative to the newest content. Report
> findings grouped by wiki and for `_brain/`. Also surface any
> `WIKI-PENDING` sources. Do not remediate — this is a report to act on
> locally (via `/wiki-maintain` for wikis, `/checkpoint` for project notes).
> No writes.

## The two manual/local routines

Run these by hand (paste the prompt directly) whenever you want, or wire up
via `/loop` on a machine that stays on:

### 3. Nightly consolidation — `0 22 * * *` (daily 22:00 local) — BOUNDED MUTATION, manual/local

> Run the deterministic half of `/daily-summary`: for each project touched today,
> commit today's work locally (never push, never PR) and write/update today's
> `_brain/daily/<YYYY-MM-DD>.md`. Then **flag, don't do**: list any durable
> knowledge that looks unpushed (unchecked items in `wiki-links.md`) and any
> contradictions noticed — leave `/wiki-push` and wiki canonicalization for me.
> Do not touch the thematic wikis.

### 4. Weekly review + planning — `30 16 * * 5` (Fri 16:30 local) — DRAFT, manual/local

> Run `/weekly-planning` in draft mode: review this week's `_brain/daily/*.md`,
> draft `_brain/weekly/<Monday>.md` (last week's check-off, this week's goals,
> open work timeslots, and Questions for next week). **Propose** calendar blocks
> but do not create them — leave the proposed blocks in the note for me to confirm.

## Guardrails (all routines)

- No autonomous wiki canonicalization, merging, or synthesis — that stays
  command-invoked and verifier-gated.
- No calendar events created without a human confirm.
- No pushes or PRs from the manual/local routines — nightly commits locally only.
- The cloud routines never write anything at all (both are read-only).
- Reports and drafts are the output; the human decides what to act on.
