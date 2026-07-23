# research-os (plugin)

Personal research operating system for Claude Code — the sole global plugin install. Built on the [clo-author](https://github.com/hugosantanna/clo-author) fork, enhanced with the integrity layer of [ARS](https://github.com/Imbad0202/academic-research-skills), and a two-layer Obsidian knowledge base with daily/weekly routines. Also absorbs the general-purpose global skills/agents that survived a consolidation audit — nothing custom lives loose in `~/.claude/skills` or `~/.claude/agents` anymore.

Sits **above** two separately-installed plugins it calls into rather than vendors:
- `dz-core` — branded charts, branded-PDF build, Instagram tiles, onboarding.
- [`engram`](https://github.com/nagisanzenin/engram) — the spaced-repetition learning engine behind `/learn`/`/recall`; research-os only owns the context-sourced intake, not the teaching/grading/scheduling logic (see `skills/learn/`, `skills/recall/`).

Ships **no personal data** — vaults, the `_brain/` second brain, and projects live in the user's data directories, never in this plugin.

## Installed as

Registered as a local marketplace and installed as a real Claude Code plugin (not just source in this repo):
```
claude plugin marketplace add <path-to-this-repo>
claude plugin install research-os@research-os
```
After editing anything under `plugins/research-os/`, run `claude plugin marketplace update research-os` to pick up the change. `claude plugin details research-os@research-os` shows the live component inventory + token-cost estimate.

**`engram` (learning engine) install** — separate plugin, same mechanism:
```
claude plugin marketplace add nagisanzenin/engram
claude plugin install engram@engram
```
Requires `ENGRAM_HOME` set (in `~/.claude/settings.json`'s `env` block) to `<vault root>/_brain/learning` so learning state lives in the second brain rather than the default `~/.claude/learning/`. On Windows/Anaconda setups without a `python3` on PATH (only `python`), engram's skills hardcode `python3` in their shell blocks — add a one-line shim (`exec python "$@"`) somewhere ahead on `PATH` rather than editing engram's own files.

## Layout

| Dir | Contents |
|-----|----------|
| `skills/` | Slash-command skills (pipeline, wiki, routines, upstream-sync, help, + consolidated general-purpose skills) |
| `agents/` | Worker↔critic agents (clo-author roster + ARS capabilities merged in) + `wiki-librarian`, `python-reviewer`, `code-reviewer` |
| `hooks/` | `hooks.json` (note: plugin hook manifests need a top-level `"hooks"` wrapper key — unlike a project's `.claude/settings.json`) + hook scripts (SessionStart nudges, guards) |
| `rules/` | Governance rules (permissions, quality gates, folder-map, output-discipline, wiki-integration) |
| `templates/` | Project + vault + passport scaffolds |
| `state/` | Upstream-repo tracking (`upstream-repos.json`) |

## Status

- [x] Phase 1: plugin skeleton, trim globals, fix broken bits
- [x] Phase 2: project layer (globalize + rewire clo-author, merge ARS)
- [x] Phase 3: knowledge layer (two-layer vault, registry, PDF pipeline)
- [x] Phase 4: routines + upstream sync (daily-summary, weekly-planning, check-update-upstream-repos)
- [x] DZ-specific output types (Geldbrief/Fachtext/Hintergrundpapier/Policy Brief) removed — academic paper only, per house-style calibration never materializing
- [x] Global skill/agent consolidation — audited every remaining global skill/agent against research-os's own coverage; survivors vendored here, `claude-global/` retired, `~/.claude/skills`+`agents` now empty of custom content
- [x] Phase 5: learning layer — `engram` installed as its own plugin (not vendored); `/learn` is research-os's context-sourced intake, handing off to `engram:learn`; `/recall` aliases `engram:review`; `/coach` used directly

## Publishing note

When sharing with DZ, keep personal data out of the published tree — either move this plugin to its own repository, or `.gitignore` the unified Obsidian vault root and any `_brain/` content from the marketplace repo.
