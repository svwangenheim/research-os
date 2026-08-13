# Scheduled agents

Seven hand-authored routines, plus any number of procedure-driven schedules
(§ below), keep the second brain, the wikis, and the projects' numeric claims
current without manual prompting. They follow the plan's automation principle:
**detection is autonomous; mutation is bounded and supervised.** A scheduled run
never canonicalizes a wiki, never creates calendar events, and never writes into
`_brain/` beyond what the named skill already does deterministically —
anything needing judgment is drafted or flagged for a human confirm.

## Two findings from 2026-08-11, still load-bearing

**Reach.** Every routine grants every tracked project via `--add-dir`, derived
from `working_directory:` in `vault/_brain/projects/*.md` by
`scripts/resolve_project_paths.py`. Before this the tasks only ever saw the
vault, so unattended runs reported "no indication of work" while project
repos sat busy and uncommitted. Never hardcode a project path in a routine —
add `working_directory:` to the project note instead.

**Scan, don't explore.** Project state is gathered by
`scripts/project_state_scan.py` *before* `claude` is invoked. The project
repos are on OneDrive with Files-On-Demand, where directory traversal runs
~20x slower than local (measured: `git status` 0.7s vs. a depth-2 `find` 3.8s
for 68 files) — letting a routine's prompt explore project directories
itself is slow enough to look hung. A routine prompt must say not to explore
and must supply the scan instead. (Both findings, and the incident that
surfaced them, are in `docs/13-the-automation-layer.md`.)

## How this is actually wired up

All hand-authored routines run **locally**, as Windows Scheduled Tasks that
invoke the `claude` CLI in non-interactive (`-p`/print) mode — not cloud
routines. Cloud routines (`/schedule`) were tried first, but a cloud run only
sees a single cloned GitHub repo, not this machine, so it can't see local
project folders, can't commit to local project repos, and would have required
pushing every project (and the vault) to GitHub just to make that work. A
local Scheduled Task has the same access this machine's interactive Claude
Code sessions have — full filesystem, full git — so every routine runs
at full fidelity, and nothing has to leave this machine.

**The pieces:**
- `plugins/research-os/scripts/scheduled/*.ps1` — one PowerShell wrapper
  script per routine. Each sets the working directory to the vault root,
  builds the routine's prompt, and calls `claude -p` with a scoped
  `--allowedTools` list and `--permission-mode acceptEdits` (never
  `--dangerously-skip-permissions` — the allowlist is the actual safety
  boundary: for instance, the nightly-consolidation script's allowlist has
  no `git push`, so it's structurally incapable of pushing even if it tried).
  Output is logged to `vault/_brain/scheduled-logs/<date>/<routine>_<time>.log`
  (gitignored in the vault's own repo) so every unattended run leaves a
  reviewable trail. Dated-folder-first rather than routine-first, and without
  the leading dot `.scheduled-logs` used to carry — that dot made the whole
  directory invisible in Obsidian's file explorer, and grouping by day means
  one day's morning brief, nightly consolidation, and pending sweep sit next
  to each other instead of scattered across separate routine folders.
- `plugins/research-os/scripts/scheduled/_common.ps1` — dot-sourced by each
  wrapper. It supplies `$VaultRoot`, `$PluginRoot`, a probed Python
  interpreter, `Get-LogFile`, and `Get-ProjectAddDirArgs`, which derives the
  `--add-dir` grants from `vault/_brain/projects/*.md` frontmatter so no script
  hardcodes a project path. New routines dot-source it rather than repeating
  the setup.
- `--model sonnet` is pinned explicitly in every script — the default model
  hit a usage-credits requirement in headless/print mode when tested
  un-pinned; `sonnet` did not.
- Windows Scheduled Tasks named `ResearchOS-MorningBrief`,
  `ResearchOS-NightlyConsolidation`, `ResearchOS-NightlyReproCheck`,
  `ResearchOS-WeeklyVaultHealthAudit`, `ResearchOS-WeeklyPlanning`, and
  `ResearchOS-WeeklyLiteratureDelta`, each pointing at its script. Registered with
  `schtasks /create`; inspect or remove them with `schtasks /query /tn
  <name> /fo LIST /v` / `schtasks /delete /tn <name> /f`. They run in
  "interactive logon" mode — only when this Windows account is logged in,
  no stored password.
- Each script's prompt **calls the relevant skill** where one exists
  (`/research-os:daily-summary`, `/research-os:weekly-planning`), with an
  explicit non-interactive override: both of those skills are written to
  *ask conversationally* at several steps, which only works with a human
  present — the wrapper prompt tells Claude to infer autonomously instead of
  asking, and to draft rather than create anything requiring live
  confirmation (calendar events, project selection). The other four have no
  single matching skill to call — morning brief spans multiple unrelated read
  paths, the vault-health audit runs a plugin script directly, and the two
  detection routines below deliberately do *not* call `/peer-review` or
  `/discover lit`, since those skills mutate project state and a detection run
  must not — so those four stay as directly-specified prompts.

## The seven hand-authored routines

### 1. Morning brief — daily 09:00 — READ-ONLY

`ResearchOS-MorningBrief` / `scripts/scheduled/morning-brief.ps1`

> Read-only morning brief. Do not modify any file. Report, in a few lines:
> what's pending across my active projects (scan each project's
> `passport.yaml` `pipeline.current_stage` and open plan items — discover
> project paths from `_brain/projects/*.md`'s Orientation section; if none
> are recorded yet, say so and skip this part rather than guessing), the
> single next step per project, any due engram spaced-repetition reviews
> (read `_brain/learning/`'s FSRS state; report a count, don't run
> `/recall`), and today's calendar if the Microsoft 365 connector is
> authorized (skip gracefully, note once, if not). No writes.

### 2. Nightly consolidation — daily 22:00 — BOUNDED MUTATION

`ResearchOS-NightlyConsolidation` / `scripts/scheduled/nightly-consolidation.ps1`

> Run `/research-os:daily-summary` — but non-interactively, since this is an
> unattended scheduled run: autonomously detect touched projects today
> (git activity + `_brain/projects/*.md`'s Orientation section) instead of
> asking, then proceed through its steps without stopping to confirm. Still
> respect its guardrails exactly: never push or open a PR, never fail the
> whole run over an unauthorized connector, never touch the thematic wikis.
> Afterward, flag — don't act on — any durable knowledge that looks unpushed
> and any contradictions noticed; leave `/wiki-push` and wiki
> canonicalization for me.

### 3. Weekly vault-health audit — Fridays 15:00 (before planning) — READ-ONLY

`ResearchOS-WeeklyVaultHealthAudit` / `scripts/scheduled/weekly-vault-health-audit.ps1`

> Read-only audit. Run:
> `python "${CLAUDE_PLUGIN_ROOT}/scripts/wiki_quality_check.py" --root "<vault root>"`
> (covers every wiki + the `_brain/` personal layer) and report the findings
> grouped by wiki and for `_brain/`. Also surface any `WIKI-PENDING`
> sources. Do not remediate and do not invoke `/wiki-maintain`
> automatically — this is a report I act on by hand.

### 4. Weekly review + planning — Fridays 16:30 — DRAFT

`ResearchOS-WeeklyPlanning` / `scripts/scheduled/weekly-planning.ps1`

> Run `/research-os:weekly-planning` — but non-interactively and in draft
> mode: infer last week's check-off status per goal from git commit
> activity instead of asking (label anything genuinely unclear rather than
> guessing), infer this week's likely goals/timeslots from unresolved
> threads in the daily notes, and propose calendar blocks checked against
> the existing calendar but do **not** create them under any circumstances —
> leave every proposed block in the weekly file for me to confirm by hand.

### 5. Nightly reproducibility check — daily 03:00 — READ-ONLY, SILENT ON PASS

`ResearchOS-NightlyReproCheck` / `scripts/scheduled/nightly-repro-check.ps1`

> Read-only. For each active project, re-verify every numeric claim in
> `passport.yaml` `claim_manifest` against the artifact its `evidence_origin`
> points at, applying the tolerances in
> `skills/analyze/config/replication-tolerances.json`. Assign each claim PASS,
> EXPLAINED, FAIL, STALE, or UNMATCHED. **If everything is PASS or EXPLAINED,
> output the single line `REPRO OK` and nothing else.** Otherwise output a
> `REPRO DRIFT` report with the affected claim ids, recorded versus current
> values, and the specific next step. Write nothing back into `passport.yaml` —
> a supervised run decides dispositions.

Two rules carried over from the replication protocol matter here. A gap
explained by a **concrete, named** alternative specification is EXPLAINED and is
not reported; a blank or vague note never downgrades a FAIL. And a mismatch
means one of {paper, code} must change — the routine says which artifacts
disagree and never concludes that the code should be reverted to match the
paper, since a refactor may have fixed a real bug the paper still reflects.

This routine detects the drift that `claim-reconcile.py` flags at write time but
that nobody acts on, and it does it while you are not looking. It does **not**
call `/peer-review --replicate` — that skill mutates project state.

### 6. Weekly literature delta — Mondays 08:00 — SEARCH + DIFF, SILENT ON NOTHING-NEW

`ResearchOS-WeeklyLiteratureDelta` / `scripts/scheduled/weekly-literature-delta.ps1`

> Resolve watch topics (`_brain/lit-watch.md` if present, else each active
> project's `passport.yaml` `research.question` / `research.methodology` and the
> registered wiki themes), sweep NBER, CEPR, SSRN, RePEc, arXiv econ, and the
> field journals in each `00_admin/domain-profile.md` for work from the past
> week, then diff against the seen-list, the projects' `literature_corpus`, and
> the wikis' `10_sources/` and `20_summaries/`. Filter the remainder for
> **direct** relevance: a paper qualifies only if it would change the
> identification strategy, the estimator, the data source, the positioning, or a
> claim in a draft, and only if that sentence can actually be written. **If
> nothing survives, output the single line `LIT DELTA: none`.** Otherwise list
> each survivor with its relevance sentence and the project it affects. Nothing
> is ingested automatically.

Its one write is the seen-list at
`_brain/scheduled-logs/weekly-literature-delta/seen.md`, and the allowlist is
scoped to that single path rather than granting `Write` outright. Every hit it
evaluated goes on the list, kept and dropped alike, so the same paper is not
re-surfaced next week. Nothing enters `bibliography.bib` or a wiki without
`/wiki-ingest`, which stays command-invoked.

### 7. Pending sweep — daily 18:00 — READ-ONLY, no `claude` invocation at all

`ResearchOS-PendingSweep` / `scripts/scheduled/pending-sweep.ps1`

Sweeps every project for uncommitted work, unpushed commits, and unchecked
`wiki-links.md` items into `vault/_brain/.pending-actions.yaml`, then
refreshes the weekly plan's generated block, the week dashboard, and the
procedure promotion status. **Contains no `claude` invocation** — detection is
pure computation, so it costs nothing and cannot go wrong in an interesting
way. Acting on the queue happens only through `/pending`, which asks once per
project and records the answer in `automation-consent.yaml`. This is the
shape to copy for a future routine: if the job is deterministic, run the
script, not a model.

## Procedure-driven scheduling (2026-08-12) — a different mechanism, same safety shape

The seven routines above are hand-authored: one `.ps1` file each, registered
by hand. As of the executable-procedure layer (`docs/13-the-automation-layer.md`),
a personal procedure in `_brain/procedures/` can declare its own `schedule:`
frontmatter and register **itself** — the whole deploy step (guide step 5) is
that one declaration:

```bash
python scripts/automate_schedule.py --root <vault> --name <procedure>          # register
python scripts/automate_schedule.py --root <vault> --name <procedure> --off    # unregister
python scripts/automate_schedule.py --root <vault> --list                      # declared-vs-registered drift
```

One shared wrapper, `scripts/scheduled/automate-procedure.ps1 -Name <procedure>`,
handles every scheduled procedure — no new `.ps1` file per procedure. Same
runner semantics as an interactive `/automate run`: `[ai]` executes, `[human]`
stops and leaves a note (a scheduled run never guesses past a human step),
`[veto]` refuses. Currently registered:

| Task | Procedure | Schedule |
|---|---|---|
| `ResearchOS-Automate-admin-deadline-sweep` | `admin-deadline-sweep` | weekly Monday 08:00 |
| `ResearchOS-Automate-wiki-hygiene` | `wiki-hygiene` | weekly Friday 14:00 |
| `ResearchOS-Automate-dz-dashboard-health` | `dz-dashboard-health` | weekly Friday 15:00 |
| `ResearchOS-Automate-admin-supervisor-brief` | `admin-supervisor-brief` | weekly Friday 16:00 |

`automate_schedule.py --list` is the source of truth for this table, not this
file — re-run it rather than trusting these rows if they might have drifted.

## Notification discipline: push on failure, silence on success

**A routine reports only when there is something to do. Silence is the
success signal.**

This is a design rule, not a preference. A job that reports "all good" every
night trains you to stop reading it, and the one night it says something
different you will skim past that too. The value of an unattended check is
entirely in the reader's attention, and a daily digest spends that attention
down to zero within a fortnight.

| Routine | Fires when | Silent when |
|---|---|---|
| Nightly repro check | any claim is FAIL, STALE, or UNMATCHED | every claim is PASS or EXPLAINED — prints `REPRO OK` only |
| Weekly literature delta | a genuinely new, directly-relevant paper survives the filter | nothing survives — prints `LIT DELTA: none` only |

The two informational routines (morning brief, weekly planning) are the
deliberate exception: you asked for those, they are scheduled to a moment you
are actually reading, and their content is a plan rather than an alarm. The
detection routines are not in that category and must not drift into it. If a
detection routine starts producing output most runs, the filter is too loose —
tighten the filter, do not learn to ignore the output.

Both write a full log to `vault/_brain/scheduled-logs/<date>/` regardless.
Silence in the notification is not silence in the record: the detail is there
when you go looking for it, which is the only time it is worth reading.

## Guardrails (all routines)

- No autonomous wiki canonicalization, merging, or synthesis — that stays
  command-invoked and verifier-gated.
- No calendar events created without a human confirm.
- No pushes or PRs — nightly consolidation commits locally only, structurally
  enforced by its script's `--allowedTools` allowlist (no `git push`).
- The three read-only routines (morning brief, vault-health audit, nightly repro
  check) make no writes at all — also structurally enforced (no `Write`/`Edit`/
  mutating `Bash` in their allowlists). The literature delta's `Write` is scoped
  to the single seen-list path.
- No routine ingests a source, edits `bibliography.bib`, or writes a
  disposition into `passport.yaml`. Detection is autonomous; the corpus and the
  ledger stay command-invoked.
- Reports and drafts are the output; the human decides what to act on.
- Detection routines are silent on success — see the notification-discipline
  section above.
- Every run is logged to `vault/_brain/scheduled-logs/<date>/` for
  after-the-fact review.

## Why these stay local: the cloud-Routine guardrail

Cloud Routines (`/schedule`) look like the natural upgrade path for anything
here. They are not, and the reason is worth stating so this design is not
casually "modernized" later.

**A cloud Routine attaches its connectors by default, with write access, and
runs without approval prompts.** The run inherits whatever the account has
connected — mail, calendar, drive, repository access — and no one is present to
decline anything. The default posture is therefore the opposite of the one
every routine above is built on: broad authority, granted implicitly, exercised
unattended.

The local design inverts each of those three properties deliberately:

| | Cloud Routine default | These routines |
|---|---|---|
| Authority | every attached connector, write-enabled | the explicit `--allowedTools` list and nothing else |
| Granting | implicit, at attach time | explicit, per script, visible in one line of PowerShell |
| Blast radius | whatever the account can reach | this machine, this working directory, this allowlist |

The allowlist is the actual safety boundary, not the prompt. The nightly
consolidation script is structurally incapable of pushing because its allowlist
has no `git push`, not because its prompt asks it not to. The repro check cannot
write to `passport.yaml` because it has no `Write` at all. Prompt instructions
are advice; an omitted tool is a wall.

**Before moving any routine to a cloud Routine**, least-privilege its connector
list first, and check that the capability it needs is actually reachable from a
cloud run — the local design exists in the first place because a cloud run sees
one cloned repo rather than this machine's project folders and vault. If a
routine does move, it loses the allowlist boundary and needs an equivalent one
put back by hand. Treat that as a redesign, not a migration.
