# Backlog

Work that is deliberately not being done yet, kept in the repository so the
reasoning survives the session that produced it. An item leaves this file when
it ships (into `CHANGELOG.md`) or when it is dropped (deleted, with the reason
folded into whatever replaced it).

Each item states what it is, why it is deferred, and roughly what it costs.
Cost estimates are session-sized: **S** is under an hour, **M** is a working
session, **L** is several sessions or needs a measurement period first.

## Open

### 1. Confirm whether plugin rules auto-load from `paths:` frontmatter

**What.** Establish empirically whether Claude Code auto-loads a rule from a
*plugin's* `rules/` directory when its `paths:` glob matches an edited file, or
whether that only works for project and user `.claude/rules/`. Test with a
throwaway rule containing a distinctive token and a file that matches its glob.

**Why deferred.** The answer picks between two different implementations. If
plugin rules auto-load, add `paths:` frontmatter to the file-type-specific
rules. If they do not, `/create-project` writes thin project-scope stubs into
`<project>/.claude/rules/` that each carry `paths:` and an `@`-reference to the
plugin rule. Building either before knowing the answer wastes one of them.

**Cost.** S to test, M to implement whichever branch it selects.

### 2. Tune the session-start retrieval budget

**What.** The wiki digest injected at session start is capped at roughly 40
lines / 600 tokens. That number is a guess.

**Why deferred.** It needs a week of real sessions and `/context` readings to
tune against. Guessing again now is not better than the first guess.

**Cost.** S to change the cap, plus a week of use to know what to change it to.

### 3. Decide the fate of `~/.claude/rules/common/`

**What.** Eleven files, roughly 48 KB, loaded by nothing. `additionalDirectories`
grants read access, not loading, so `skill-router.md` describes itself as
always-on and never runs.

**Why deferred.** It is a judgement call, not a mechanical fix, and it touches
user-level configuration rather than the repository. The standing recommendation
is to delete the six that plugin rules already supersede (`agents.md`,
`code-review.md`, `development-workflow.md`, `hooks.md`, `patterns.md`,
`performance.md`) and wire the remaining two (`skill-router.md`, `security.md`)
through a `~/.claude/CLAUDE.md` with `@rules/common/*.md` imports.

**Cost.** S.

### 4. German-language output style

**What.** A third output style for Dezernat Zukunft policy briefs, alongside
`academic-writing` and `referee`.

**Why deferred.** Worth building only if German briefs are a regular output. If
the papers are English-only it is dead weight, and an unused output style is
one more surface the sync gate has to keep honest.

**Cost.** S once the question is answered.

### 5. Calibrate the wiki auto-write council thresholds

**What.** The promotion council's vote-to-action mapping — 5/5 and 4/5
auto-write, 3/5 propose, 2 or fewer discard — is a starting point, not a
measured value.

**Why deferred.** Calibration needs data. After two weeks of use, review
`/wiki-maintain --review-auto`: if the 4/5 writes are regularly the ones you
would have rejected, raise the bar to 5/5 only. If almost nothing clears, the
candidates are under-evidenced and the fix is upstream in `/wiki-ingest`, not a
lower threshold.

**Cost.** S to change the thresholds, two weeks of use to know which way.

### 6. Surface-sync table markers in the READMEs

**What.** `check_surface_sync.py` enforces one table row per item on disk, but
only for tables introduced by `<!-- surface-sync-table: skills -->`. No README
carries a marker yet, so row parity is currently unenforced.

**Why deferred.** The markers belong with the documentation rewrite that
re-derives those tables from disk. Adding markers to tables that are already
wrong just moves the failure earlier.

**Cost.** S per README, once the tables are rewritten.

### 7. Backfill `effort:` on every agent

**What.** `check_plugin_integrity.py` reports a P2 for each agent without an
`effort:` field. All of them are missing it today.

**Why deferred.** Effort belongs with the model-routing roster, not ahead of
it. Setting effort per agent without the roster means guessing twice.

**Cost.** S once the roster is settled.

### 8. Give the general-purpose skills an `allowed-tools` list

**What.** Thirteen skills adopted from an earlier global-skills collection ship
with no `allowed-tools` frontmatter, so `check_plugin_integrity.py` cannot
check tool parity on them at all.

**Why deferred.** It is mechanical but not free: each one needs its body read
to work out what it actually invokes, and a wrong list is worse than no list
because it silently blocks a tool the skill needs.

**Cost.** M.
