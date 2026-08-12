# Changelog

All notable changes to research-os are recorded here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and
the project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
Version numbers track `plugins/research-os/.claude-plugin/plugin.json`.

## [Unreleased]

Nothing yet.

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
