# Changelog

All notable changes to research-os are recorded here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and
the project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
Version numbers track `plugins/research-os/.claude-plugin/plugin.json`.

## [Unreleased]

### Added

- **The pipeline graph.** `graph/pipeline.json` (16 nodes, 33 derived edges) plus
  `graph/schema.md` make the phase dependency structure a declared,
  machine-evaluated graph instead of prose. `scripts/graph.py` computes each
  node's state (ready / blocked / done / stale) fresh on every call from the
  graph, the filesystem, and `passport.yaml` — nothing is cached, so nothing
  can desync from reality. `graph.py next` returns the true ready frontier
  (often more than one node), `graph.py why <node>` names the exact unmet
  predicate, `graph.py stale` flags a node whose recorded input has since
  changed, and `graph.py selftest` asserts the graph never drifts from
  `rules/permissions.md`. `research-os-help`'s Step 2 now runs the router
  instead of reading `pipeline.current_stage` by hand.
- **The personal automation layer.** `/automate` (`new` / `run` / `list` /
  `status` / `map` / `schedule`) authors and executes procedures in
  `_brain/procedures/` with no promotion gate — a procedure is runnable the
  moment it validates. Four actor tags (`[ai]`, `[human]`, `[external]`,
  `[veto]`) give the runner contract real teeth: a `[human]`-tagged step stops
  a scheduled run rather than being guessed at. `scripts/automate_run.py` and
  `scripts/automate_schedule.py` are the engine; `scripts/mine_sessions.py`
  drafts real procedures from a researcher's own past session history rather
  than inventing them; `scripts/generate_automation_map.py` renders
  `_brain/automation-map.html`. See
  `docs/13-the-automation-layer.md` for why the first version (a five-test
  promotion gate requiring three recorded runs) shipped a gate that could
  never actually be reached.
- **R2 — a real data-consent gate.** `hooks/data-consent.py` asks before
  reading a data-file extension not yet recorded in
  `_brain/read-consent.yaml`, remembers the ruling per directory, and treats
  anything already on a project's own deny-list as an unconditional `deny` —
  never softened into an `ask`. Code and docs are never gated.
- **`/pending`.** Clears the backlog across every project — uncommitted work,
  unpushed commits, unpushed wiki knowledge — grouped by project, asking once
  per project per action class and remembering the answer.
  `scripts/pending_actions.py` does the (non-mutating) sweep; the skill is the
  only thing that acts, and only on consent recorded in
  `_brain/automation-consent.yaml`. A seventh scheduled routine
  (`pending-sweep`, daily) runs the sweep unattended and reports only when
  there is something to clear.
- **`/week`.** Refreshes the live week view: pulls the calendar read-only,
  reconciles the weekly plan's machine-owned block, and regenerates
  `_brain/week.html` with each project's state inside its block.
- **Checkpoint auto-fire.** A new `session-close-needed` Stop trigger
  (`hooks/dialogue-triggers.py`) detects an unsaved session by git state alone
  — identical logic for research-os and BMAD projects — and offers
  `/checkpoint`; the skill itself now handles non-passport projects
  explicitly (skips the passport-only steps, runs everything else, reports
  the skip as normal).
- **Deployment of previously orphaned routines.** `pending-sweep`,
  `nightly-repro-check`, and `weekly-literature-delta` — all written earlier
  but never registered — are now live Windows Scheduled Tasks, bringing the
  scheduled-routine count to seven. Personal procedures can self-register via
  their own `schedule:` frontmatter through `/automate schedule <name>`.
- **Three smaller skill upgrades.** `/wiki-maintain` gap-detection (Step 3b:
  cited-but-never-ingested sources), `/discover feasibility <idea>`
  (single-idea triage, distinct from `ideate`'s many-ideas generation), and a
  deadline sweep in `scripts/reconcile_week.py` unifying DZ, PhD, and personal
  deadlines against Outlook's own deadline categories.
- **The house style, written down and enforced.**
  `references/authoring-conventions.md` specifies how every Claude-facing file
  in the plugin is written — typography, skill and agent frontmatter, body
  shape, progressive disclosure, where rules end and references begin — and
  resolves the places the two upstream workflows diverge. Its deterministic
  half is a sixth check in `scripts/check_plugin_integrity.py`, advisory (P2)
  except for the one style finding that costs real capability.
  `templates/skill-template.md` is the starter new skills copy from, and a root
  `CLAUDE.md` now carries the standing brief for working on the plugin itself
  — the repo had none, so every session started without one.

### Changed

- **Every skill and agent conformed to the house style.** 811 prose `--`
  normalised to em dashes across 78 files (code fences, inline spans, and CLI
  flags untouched); slash-prefixed headings retitled; `**Input:**` lines added
  to the 19 skills that take arguments but never documented them; 13
  descriptions rewritten to end in a `Use when …` clause with the phrases a
  user would actually type, without which the router cannot match them. The ten
  vendored skills carrying `origin:` are deliberately exempt, so
  `/check-update-upstream-repos` can still diff them against upstream.

- `hooks/dialogue-triggers.py`'s stage-transition nudge now asks
  `graph/pipeline.json` what is actually ready instead of carrying its own
  hardcoded next-step map, falling back to one only if the graph itself is
  unreachable.
- `templates/brain-notes/procedure_template.md` and
  `templates/brain/folder-readmes/procedures.md` rewritten for executable,
  ungated procedures.

### Fixed

- `hooks/observe.py` — shipped by the harness-layer commit but never actually
  committed, so the hook it registered in `hooks.json` pointed at a file that
  did not exist. Off by default (`observer-config.json`'s `enabled: true`
  turns it on) and gated through `scripts/capture_policy.py` so data-file
  content is never captured.
- `hooks/README.md` and `rules/README.md` listed rows for hooks that were
  never actually committed; removed rather than left to drift further.
- **Three agents silently received every tool.** `agents/code-reviewer.md`
  declared `allowed-tools:` — a skills-only key, ignored on an agent — with
  permission-style scoping (`Bash(git diff*)`) that is not valid there either;
  `agents/engram-assessor.md` declared no tools at all, despite being the blind
  grader that must never write; `agents/python-reviewer.md` used the JSON-array
  dialect. All three now declare `tools:` as a comma list, and the integrity
  checker blocks on the mistake.

### Removed

- **`/procedure` and `scripts/procedure_promotion_check.py`.** Replaced by
  `/automate`; there is no promotion gate left to check. See
  `docs/13-the-automation-layer.md` for the full rationale.

## [0.1.0] - 2026-08-11

First recorded version. The plugin existed before this entry; 0.1.0 describes
the state of the tree at the point a changelog started being kept, including
the repairs and harness work that landed immediately before it.

### Added

- **Paper pipeline.** Eight worker-critic pairs (librarian, explorer,
  strategist, theorist, coder, writer, storyteller, plus the referees and
  editor) driven by phase skills: `/discover`, `/strategize`, `/analyze`,
  `/write`, `/peer-review`, `/revise`, `/talk`, `/submit`. Ported from
  clo-author and rewired to a numbered project folder scheme.
- **ARS integrity gate.** Blocking pre-submission check covering claim tracing,
  four-database citation triangulation, temporal and anachronism audit, and
  figure-caption fidelity. Co-owned by the verifier, methods-referee and
  writer-critic, so no agent clears its own work.
- **Two-layer knowledge vault.** A personal `_brain/` layer plus
  Claude-maintained thematic wikis with immutable sources, canonical concept,
  method and dataset pages, and preserved contradictions. Managed by
  `/wiki-setup`, `/add-thematic-wiki`, `/wiki-pull`, `/wiki-push`,
  `/wiki-ingest`, `/wiki-maintain` and `/connect`.
- **Project state.** One `passport.yaml` per project holding the research spec,
  claim manifest, literature corpus, pipeline stage, integrity state and
  session history.
- **Learning layer.** engram vendored directly into the plugin as `/learn`,
  `/recall` and `/coach`, with the engine at `scripts/engram.py`.
- **Routines.** `/daily-summary`, `/weekly-planning`, `/checkpoint`, and four
  scheduled Windows tasks under `scripts/scheduled/`.
- **Harness hooks.** `git-guardrails.py` (denies destructive git, warns on
  absolute machine paths written into analysis code), `claim-reconcile.py`
  (flags claims whose evidence just changed), `context-monitor.py`
  (progressive context nudges, and the `context-pct.txt` the status line
  reads), `session-journal.py` (writes the session change-set record rather
  than only nudging about it).
- **Status line.** `scripts/statusline.py` renders permission mode, model,
  branch and dirty count, pipeline stage, integrity gate state and context
  estimate. Every field degrades independently.
- **Rules.** `summary-parity.md` (re-verify enumerative claims when editing any
  summary paragraph), `prompt-shaping.md`, `confidential-data.md` (restricted
  and administrative microdata protocol).
- **Self-governance.** `scripts/check_plugin_integrity.py` and
  `scripts/check_surface_sync.py`, wired into `.githooks/pre-commit` (installed
  by `scripts/install-hooks.sh`, bypassable with `SKIP_INTEGRITY_GATE=1`) and
  `.github/workflows/gates.yml`.
- **Documentation surfaces.** This changelog, `docs/PROVENANCE.md`,
  `BACKLOG.md`, and `plugins/research-os/references/audit-pet-peeves.md`.

### Changed

- `hooks/post-edit-lint.sh` rewritten as `post-edit-lint.py`: it parses the
  hook JSON on stdin instead of reading `$CLAUDE_TOOL_ARG_FILE_PATH`, and emits
  the PostToolUse JSON contract.
- `hooks/protect-files.sh` ported to `protect-files.py`, dropping the `jq`
  dependency and returning the modern PreToolUse decision object rather than
  exiting 2.
- `hooks/stop-push-nudge.py` replaced by `session-journal.py`.
- `agents/verifier.md` now reads the wiki corpus (`<main_wiki>/10_sources/` and
  `20_summaries/`) before external citation triangulation, implementing what
  `rules/wiki-integration.md` already promised.
- `/add-vault` renamed to `/add-thematic-wiki` across `vault/CLAUDE.md`,
  `vault/_brain/wikis-index.md` and `templates/vault-root/CLAUDE.md`.
- `styles/styles.css`, `styles/components.js` and
  `scripts/generate_html_report.py` carry research-os headers. The clo-author
  attribution they used to hold now lives in `docs/PROVENANCE.md`.

### Fixed

- `post-edit-lint` never ran, so the code invariants INV-14 to INV-19 had no
  write-time enforcement at all.
- `protect-files` failed silently on any machine without `jq`, which is the
  default on Windows.
- `skills/continuous-learning-v2/SKILL.md` claimed an `observe.sh` hook was
  registered in `hooks/hooks.json`. Neither the file nor the entry existed.

### Removed

- `skills/continuous-learning-v2/` - the skill was disabled and its central
  claim was false.

[Unreleased]: https://github.com/svw-dz/research-os/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/svw-dz/research-os/releases/tag/v0.1.0
