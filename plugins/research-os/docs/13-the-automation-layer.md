# 13 · The Automation Layer: Executable Procedures, Not Promoted Notes

> **Status: built and dogfooded, 2026-08-12 — supersedes `docs/13-the-workflow-layer.md`
> (deleted), which shipped a design this document explains was wrong.** Ported from
> Miles Deutscher's *"How to Automate Your Life With Claude (Full System)"*, adapted
> from business-owner to researcher. The article body is behind an X native-article
> login wall; its five-step structure is reconstructed from Miles's own summary
> thread (a primary-source quote, not a secondhand paraphrase), and his exact prompt
> templates were never in hand.

## 1 · What went wrong the first time, stated plainly

The first pass at this layer built `_brain/procedures/` as **documentation** —
notes describing a recurring task, gated behind a five-test promotion mechanism
requiring ≥3 recorded runs before a procedure could become a skill. Two things
were wrong with that, one structural and one simply broken:

**Structural: it diverged from the guide at the one step that matters.** Miles's
own words, verified against his summary thread: *"Turn workflows into skills —
either by talking Claude through the process out loud, or using 'Record a
Skill'… which Claude turns into a reusable skill."* Describe → runnable, in one
step. The promotion-gated version instead went describe → inert note → (maybe,
eventually) → runnable, with an entire waiting stage the source design does not
have.

**Broken: the gate could never be reached.** `/procedure`'s own documentation
said `/daily-summary` would match observed work against procedure triggers and
append run-log entries — the mechanism that was supposed to accumulate the 3
runs the gate required. It was never implemented. `grep` on `daily-summary/SKILL.md`
for "procedure" returned zero matches. So the gate was not merely strict; it
was **unreachable by any path that existed**, which means the honest state of
the first version was: extensive scoring, mapping, and quality-checking
machinery, wrapped around a layer that had automated nothing.

## 2 · The insight that resolves it: three layers, not two

Miles has two layers (a personal-brain folder for context, a specs folder of
skills he built) because he is not shipping a product to anyone else. research-os
is. Collapsing that distinction is what produced the divergence:

| Layer | What | Where | Ships? |
|---|---|---|---|
| **1 · research-os skills** | Generalizable research machinery — `/strategize`, `/write`, `/peer-review`, `/automate` itself | `plugins/research-os/skills/` | Yes, to any researcher |
| **2 · Personal procedures** | *This researcher's own* recurring tasks — a scenario run, a specific supervisor's meeting prep | `vault/_brain/procedures/` | Never |
| **3 · The automation engine** | Authors, runs, maps, and schedules layer 2 | `plugins/research-os/scripts/automate_*.py`, `skills/automate/` | Yes — every researcher needs it for *their own* tasks, just not the same tasks |

Miles's "specs folder holding every skill you've built" is **layer 2** — his
skills *are* personal, because he has no layer 1 to keep separate from them.
research-os already had layer 1. It needed 2 and 3, not a promotion path
between them.

**The composition rule that keeps the layers from re-merging:** *procedures may
call skills (and project-local workflows, like a BMAD `mmm-*` step); skills
never call procedures.* A personal procedure's `calls:` field records exactly
this — one direction, enforced by convention because nothing else would stop a
skill author from reaching into someone's personal automation.

## 3 · The runner contract

`scripts/automate_run.py` parses a procedure's Steps into an ordered plan and
returns it — it never executes shell commands itself. `/automate run` is what
acts, one step at a time, using its own tools, which is a deliberate choice:
tool-permission enforcement (and the R2 gate, §5) lives in Claude's own tool
layer, and a script that shelled out independently would be a second,
unaudited execution path — exactly the kind of side door AD-5 exists to close.

Four actor tags, one semantics, identical whether invoked interactively or by
a schedule:

| Tag | Runner behaviour |
|---|---|
| `[ai]` | Executes the step itself |
| `[human]` | **Stops.** Asks, then waits. A scheduled run stops here too and leaves a note in the run log — it does not guess what a human would say. |
| `[external]` | Orchestrates it (invokes the named tool/skill/workflow) but the actual system does the work |
| `[veto]` | **Refuses**, unconditionally. No plan is emitted past this step. |
| *(untagged)* | Also stops — the runner cannot classify what it cannot see, and an unclassified step is not "ai" by default. |

This is what makes R1 (*"strategic/design/identification questions are never
solo"*) structural rather than aspirational: tag the step `[human]`, and the
runner **cannot** execute it alone, regardless of how it was invoked. A
scheduled procedure that reaches a `[human]` step does not fail — it stops
correctly and reports what it stopped on, which is the intended behaviour, not
a bug to route around.

## 4 · Mining real evidence instead of inventing procedures

The 14 procedures in this batch were drafted from `scripts/mine_sessions.py`,
which extracts **user turns only** from `~/.claude/projects/<project>/*.jsonl`
— 117 sessions, 283 MB, 23 projects, verified during planning. The signal is
almost entirely in what was actually typed: prompt sequences, recurring terms,
and correction turns ("no, actually…"), the last being where a workflow's real
rules usually live.

Two filtering bugs, both found by testing before shipping, are worth recording
because the failure mode generalizes: raw session records carry a lot of
**injected** content that is not something a human typed — skill-preamble
dumps, slash-command XML wrappers, task-notification payloads — and an
exact-marker list catches known wrappers but misses the next one. The fix that
actually held was catching the **shape** (any text opening with a raw `<tag>`)
rather than enumerating tag names one at a time.

**Safety.** Every extracted prompt is checked against the project's own
`.claude/settings.json` deny-list via `capture_policy.py` — the same
classifier that gates the observation layer and passes the AD-5 canary —
before being written to a report. A prompt mentioning a denied path is
redacted **wholesale**, never partially: this is free text a human typed, not
a structured file read, so there is no safe way to redact just a span of it.
Verified against the real Microsimulation project output: zero SOEP data
references reach `_brain/.session-mining/`.

## 5 · R2: a real gate, not a nudge

R1 and R2 are the two standing rules the first `/workflow-audit` produced. R1
is structural via the actor tags (§3). R2 — *"whenever new data is included,
Claude should proactively ask whether it's allowed to read it, before touching
any new data, and remember the ruling"* — needed an actual PreToolUse gate,
because the ambient dialogue triggers (`hooks/dialogue-triggers.py`) can only
nudge, never block.

`hooks/data-consent.py` splits three ways on `capture_policy.py`'s own
classification, and the split is the safety property:

- **`CONTENT`** (code/docs) — never gated.
- **`METADATA`** (a data extension, not on any deny-list) — R2's actual case.
  Returns `permissionDecision: "ask"`, a genuine permission prompt shown to
  the human. Approving it is remembered per directory in
  `_brain/read-consent.yaml` (a PostToolUse companion records the grant only
  if the gated call actually succeeded — not a hope about how permission
  caching behaves, a ledger this script owns end to end).
- **`REDACTED`** (already covered by the project's own AD-5-style deny-list,
  e.g. Microsimulation's `SOEP/data/**`) — **`"deny"`, unconditionally, never
  `"ask"`.** Asking would let a human habitually click approve past a hard
  deny, which is exactly the breach Epic 7.2 closed. R2 augments AD-5; it must
  never be able to soften it.

Two bugs found by testing, worth naming because both are the kind that would
have shipped invisibly: `SENSITIVE_DIR_HINTS` included `"raw"`, which
`folder-map.md` names as **standard structure in every research-os project**
(`02_data/raw/`) — removed, since it hard-denied an ordinary folder every
project has. And the ledger's reader and writer disagreed on indentation, so
"remembered" grants were never actually found and every directory asked every
time — a further, subtler bug in the same code broke on Windows path *values*
containing a colon (`C:\Users\...`), which a naive split on the first `:`
mishandles.

## 6 · The BMAD seam

The Microsimulation and Macro-Fiscal repos already run BMAD's `mmm` module —
14 named agents, 6 workflows (`mmm-scenario-design`, `mmm-forecast-run`,
`mmm-baseline-test`, `mmm-fix-dispatch`, `mmm-qa-verify`,
`mmm-report-generation`), a QA gate, a Model Context Block. The user's
explicit judgment on those workflows: *"i like the bmad style of operation,
but these skills are not good/not what i actually want."*

So the DZ-modelling procedures are not thin wrappers around BMAD as it stands.
They encode the *analytically correct* shape of each task — mined from real
session evidence, not invented — and invoke BMAD only where it genuinely
earns it (`mmm-qa-verify`'s `[OK]` gate, `mmm-baseline-test`'s pre-change
capture), while adding what BMAD lacks entirely: commit, checkpoint,
project-note update, wiki push. That connective tissue is exactly what was
missing when 17 files sat uncommitted for two weeks — BMAD ran the model
correctly and had nothing to say about git.

## 7 · The plugin-volatility finding

Edits to `plugins/research-os/` made earlier the same day — before this
rebuild started — were **silently reverted** by a sync from
`origin/feat/harness-overhaul`, discovered only by grepping for a sentinel
string that should have been there and wasn't. Edits to `vault/` (a separate,
local-only git repository with no remote) survived untouched.

This is why every work order in this rebuild was committed to the plugin
repo immediately on completion, rather than batched. It is also why anything
that looked already-fixed from an earlier pass in this same session was
re-verified rather than trusted — `state/dialogue-triggers.json`'s
`session-anchor` trigger, disabled earlier the same day because
`wiki-context.py` already does its job, was found back at `enabled: true`
mid-rebuild and had to be re-disabled (`rules/dialogue-triggers.md` now
records this as a concrete instance, not just an abstract warning).

**The operating rule this leaves behind:** plugin-side state that is not
committed can be reverted out from under you without notice. Treat "I fixed
this earlier" as a claim to re-verify, not a fact to build on, for anything
in `plugins/research-os/` that has not yet reached a commit.

## 8 · What shipped

- **The engine** — `/automate` (`new`/`run`/`list`/`status`/`map`/`schedule`),
  `automate_run.py`, `automate_schedule.py`, `generate_automation_map.py`
  (three views: by role, by procedure, coverage). `/procedure` and
  `procedure_promotion_check.py` deleted — there is no gate to check.
- **The evidence** — `mine_sessions.py`, run against all 23 known projects,
  seeding every procedure drafted in this batch.
- **14 personal procedures**, `draft: true`, every uncertain step tagged
  `[human]`, corrected on first real `/automate run` rather than dialogued in
  advance — the guide's step 2 minus the "Record a Skill" mechanism the user
  explicitly rejected, replaced with evidence-seeded drafting instead.
- **R2**, `hooks/data-consent.py`, canary-verified end to end (code allowed,
  unfamiliar data asks, a denied path refuses outright and is never askable,
  a granted directory is genuinely remembered, a different directory still
  asks).
- **`/checkpoint` auto-fire** — a new `session-close-needed` Stop trigger
  (pure git, fires identically for BMAD and research-os projects) plus
  explicit non-passport handling in `/checkpoint` itself (skip steps 4a/4g,
  run everything else, report the skip as normal rather than an error).
- **Deployment** — 3 previously-orphaned scheduled scripts registered
  (`pending-sweep`, `nightly-repro-check`, `weekly-literature-delta`), plus 4
  procedures self-registered via their own `schedule:` frontmatter. 11 tasks
  confirmed live via `schtasks /query`.
- **Three smaller skill upgrades** — `/wiki-maintain` Step 3b (gap-detection:
  cited-but-never-ingested sources), `/discover feasibility <idea>`
  (single-idea triage, distinct from `ideate`'s many-ideas generation), and
  `reconcile_week.py`'s deadline sweep (DZ + PhD + life, one system, reusing
  Outlook's own `Self-imposed Deadline`/`External Deadline` categories rather
  than a free-text scanner).

## 9 · What this deliberately does not build

- **A second promotion mechanism.** There is no path from procedure to skill
  other than a human writing a skill by hand, having decided the task is
  genuinely generalizable. That decision is not automatable, and pretending
  otherwise is the mistake this document exists to correct.
- **Autonomous execution of `[human]` steps, ever**, regardless of context,
  schedule, or how many times the same step has run cleanly before.
- **A ledger-based "remember denial."** `read-consent.yaml` only ever
  records grants, written by this script; a permanent denial is a manual
  edit, documented in the ledger's own header, because inferring permanent
  denial from a single "no" risks locking out a path the user only meant to
  defer.
- **A second execution path around Claude's own tool-permission layer.**
  `automate_run.py` returns plans; it never shells out.

## 10 · What remains honestly open

1. **The DZ procedures are drafted, not dialogued.** Each is `draft: true`
   and the first real `/automate run` is where it gets corrected — that is
   the designed correction point given the no-stop-for-dialogue constraint
   this rebuild ran under, not a shortcut that quietly became permanent.
2. **`dz-model-equation-estimation` was folded into
   `dz-model-feature-implementation`** rather than given its own procedure —
   it has never actually been run, and writing steps for it would have been
   invention rather than evidence.
3. **The runner's "return a plan, execute in the skill" split has not been
   stress-tested on a long procedure** where a later step genuinely depends
   on an earlier step's output in a way the pre-computed plan can't capture.
   Watch for this on `phd-overnight-estimation-monitor`'s first real run.
4. **`admin-supervisor-brief` was wrong, exactly as predicted here** —
   corrected 2026-08-14: it is the **DZ** supervisor (weekly Thursday 15:00),
   not a PhD supervisor waiting on October 2026. Also added
   `admin-jour-fixe-brief`, a deliberately lighter sibling for the
   Thursday-morning DZ jour fixe. Both now carry `StartBoundary` on their
   underlying Scheduled Tasks pinned to 2026-09-03 — the first Thursday DZ
   work resumes after the August pause — so neither can fire early the way
   the original mis-scoped version did (see the CHANGELOG's Unreleased
   entry). `phd-coursework-cycle` is unaffected and remains open: PhD
   coursework genuinely doesn't exist until October 2026, drafted from what
   the user stated directly rather than observed, and still the most likely
   of the remaining procedures to need a real correction once it does.
5. **The role-hour budgets in `profile.md` are still the original seeded
   guess.** This rebuild added the deadline sweep against them but did not
   revisit the numbers themselves.
