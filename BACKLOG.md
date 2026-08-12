# Backlog

Work that is deliberately not being done yet, kept in the repository so the
reasoning survives the session that produced it. An item leaves this file when
it ships (into `CHANGELOG.md`) or when it is dropped (deleted, with the reason
folded into whatever replaced it).

Each item states what it is, why it is deferred, and roughly what it costs.
Cost estimates are session-sized: **S** is under an hour, **M** is a working
session, **L** is several sessions or needs a measurement period first.

## Open

### 1. Tune the session-start retrieval budget

**What.** The wiki digest injected at session start is capped at roughly 40
lines / 600 tokens. That number is a guess.

**Why deferred.** It needs a week of real sessions and `/context` readings to
tune against. Guessing again now is not better than the first guess.

**Cost.** S to change the cap, plus a week of use to know what to change it to.

### 2. German-language output style

**What.** A third output style for Dezernat Zukunft policy briefs, alongside
`academic-writing` and `referee`.

**Why deferred.** Worth building only if German briefs are a regular output. If
the papers are English-only it is dead weight, and an unused output style is
one more surface the sync gate has to keep honest.

**Cost.** S once the question is answered.

### 3. Calibrate the wiki auto-write council thresholds

**What.** The promotion council's vote-to-action mapping — 5/5 and 4/5
auto-write, 3/5 propose, 2 or fewer discard — is a starting point, not a
measured value.

**Why deferred.** Calibration needs data. After two weeks of use, review
`/wiki-maintain --review-auto`: if the 4/5 writes are regularly the ones you
would have rejected, raise the bar to 5/5 only. If almost nothing clears, the
candidates are under-evidenced and the fix is upstream in `/wiki-ingest`, not a
lower threshold.

**Evidence so far.** A six-case dry run against a disposable scratch vault
(2026-08-12) found the council genuinely adversarial rather than a rubber
stamp — it independently caught an unacknowledged contradiction and a
template mismatch in the first hand-built test candidate, and correctly
split 4/5 on a second candidate whose Evidence dissent (a study's summary
statistics don't establish that a structured dataset exists) was a real
methodological point, not noise. Both are early, favorable signals for the
current thresholds, not a substitute for the two-week read.

**Cost.** S to change the thresholds, two weeks of use to know which way.

### 4. `log.md` merge conflicts on an older `wiki(auto):` revert

**What.** `git revert` on a `wiki(auto):` commit restores the affected wiki
*page* cleanly — verified byte-for-byte in the same dry run — but `log.md` is
a single append-only file that most auto-write commits touch near the same
lines. Reverting one several commits back can produce an ordinary merge
conflict there, needing a manual `git add` / `revert --continue`.

**Why deferred.** It is not a data-integrity problem — the reverted page is
never at risk, only the log entry needs manual resolution — and it only
shows up on a revert that isn't the most recent auto-write. Worth fixing, not
urgent. Two directions worth weighing before picking one: give each auto-write
its own dated log file instead of one running `log.md` (trades a single
chronological view for conflict-free reverts), or teach `/wiki-maintain
--review-auto`'s revert helper to regenerate the affected `log.md` lines from
git history after a conflicted revert instead of hand-resolving text.

**Cost.** S once a direction is picked.

## Resolved this session (2026-08-12)

Kept briefly for context on what was decided and why, since the reasoning
does not fully survive in a one-line `CHANGELOG.md` entry. Delete once the
`feat/harness-overhaul` branch merges and the decisions are no longer live
questions anyone would re-litigate.

- **Plugin `rules/` auto-loading.** Confirmed empirically (via
  `claude-code-guide`, citing the plugins reference and the memory docs):
  `rules/` is not a recognized plugin component and never auto-loads — only
  user (`~/.claude/rules/`) and project (`.claude/rules/`) rules do, and only
  the latter two honor `paths:` frontmatter. `/create-project` now writes
  five thin path-scoped stubs from `templates/project-rules/` into the new
  project's `.claude/rules/`, each pointing at the authoritative plugin rule.
- **`~/.claude/rules/common/`.** The premise that these loaded nothing was
  itself wrong — files without `paths:` frontmatter auto-load unconditionally
  at user scope (confirmed directly: their content appeared in this
  session's own system prompt). Six superseded by plugin rules were deleted
  (`agents.md`, `code-review.md`, `development-workflow.md`, `hooks.md`,
  `patterns.md`, `performance.md` — the last of which would have directly
  contradicted `rules/model-routing.md`); `coding-style.md`, `git-workflow.md`,
  `security.md`, `skill-router.md` were kept as-is. No `@`-import wiring was
  needed, since always-on loading turned out to already be the mechanism.
- **Surface-sync table markers.** All four component READMEs now carry
  `<!-- surface-sync-table: ... -->` markers with one row per item on disk;
  `check_surface_sync.py` enforces row parity in the pre-commit hook and CI.
- **`effort:` on every agent.** Landed with the model-routing roster
  (`rules/model-routing.md`) rather than ahead of it, as this file originally
  recommended — all 29 agents carry both `model:` and `effort:`.
- **`allowed-tools` on the general-purpose skills.** Twelve of the thirteen
  skills without frontmatter got a minimal correct tool list, each read
  individually rather than assigned generically. The thirteenth,
  `skill-stocktake`, was retired rather than fixed — it scanned the wrong
  directories for this plugin's own skills and duplicated work the new
  checkers and `/deep-audit` now do more precisely.
