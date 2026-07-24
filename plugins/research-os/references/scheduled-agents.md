# Scheduled agents

Four routines keep the second brain and wikis current without manual
prompting. They follow the plan's automation principle: **detection is
autonomous; mutation is bounded and supervised.** A scheduled run never
canonicalizes a wiki, never creates calendar events, and never writes into
`_brain/` beyond what the named skill already does deterministically —
anything needing judgment is drafted or flagged for a human confirm.

## How this is actually wired up

All four run **locally**, as Windows Scheduled Tasks that invoke the
`claude` CLI in non-interactive (`-p`/print) mode — not cloud routines.
Cloud routines (`/schedule`) were tried first, but a cloud run only sees a
single cloned GitHub repo, not this machine, so it can't see local project
folders, can't commit to local project repos, and would have required
pushing every project (and the vault) to GitHub just to make that work. A
local Scheduled Task has the same access this machine's interactive Claude
Code sessions have — full filesystem, full git — so all four routines run
at full fidelity, and nothing has to leave this machine.

**The pieces:**
- `plugins/research-os/scripts/scheduled/*.ps1` — one PowerShell wrapper
  script per routine. Each sets the working directory to the vault root,
  builds the routine's prompt, and calls `claude -p` with a scoped
  `--allowedTools` list and `--permission-mode acceptEdits` (never
  `--dangerously-skip-permissions` — the allowlist is the actual safety
  boundary: for instance, the nightly-consolidation script's allowlist has
  no `git push`, so it's structurally incapable of pushing even if it tried).
  Output is logged to `vault/_brain/.scheduled-logs/<routine>/<timestamp>.log`
  (gitignored in the vault's own repo) so every unattended run leaves a
  reviewable trail.
- `--model sonnet` is pinned explicitly in every script — the default model
  hit a usage-credits requirement in headless/print mode when tested
  un-pinned; `sonnet` did not.
- Windows Scheduled Tasks named `ResearchOS-MorningBrief`,
  `ResearchOS-NightlyConsolidation`, `ResearchOS-WeeklyVaultHealthAudit`, and
  `ResearchOS-WeeklyPlanning`, each pointing at its script. Registered with
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
  confirmation (calendar events, project selection). Morning brief and the
  vault-health audit have no single matching skill to call (the former
  spans multiple unrelated read paths; the latter runs a plugin script
  directly), so those two stay as directly-specified read-only prompts.

## The four routines

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

## Guardrails (all routines)

- No autonomous wiki canonicalization, merging, or synthesis — that stays
  command-invoked and verifier-gated.
- No calendar events created without a human confirm.
- No pushes or PRs — nightly consolidation commits locally only, structurally
  enforced by its script's `--allowedTools` allowlist (no `git push`).
- The two read-only routines make no writes at all — also structurally
  enforced (no `Write`/`Edit`/mutating `Bash` in their allowlists).
- Reports and drafts are the output; the human decides what to act on.
- Every run is logged to `vault/_brain/.scheduled-logs/<routine>/` for
  after-the-fact review.
