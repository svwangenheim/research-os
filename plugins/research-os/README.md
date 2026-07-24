# research-os (plugin)

Personal research operating system for Claude Code — the sole global plugin install. Built on the [clo-author](https://github.com/hugosantanna/clo-author) fork, enhanced with the integrity layer of [ARS](https://github.com/Imbad0202/academic-research-skills), a two-layer Obsidian knowledge base with daily/weekly routines, and [engram](https://github.com/nagisanzenin/engram)'s spaced-repetition learning engine — vendored, not called into. Also absorbs the general-purpose global skills/agents that survived a consolidation audit — nothing custom lives loose in `~/.claude/skills` or `~/.claude/agents` anymore.

Sits **above** one separately-installed plugin it calls into rather than vendors:
- `dz-core` — branded charts, branded-PDF build, Instagram tiles, onboarding.

**engram is vendored, not installed as its own plugin.** `scripts/engram.py` (the FSRS-4.5 engine), `agents/engram-*.md` (curriculum architect, blind assessor, artifact smith), and `skills/_shared/`'s dialogue/problem grammar + explorable contract are copied in directly from upstream, byte-for-byte where it's pure engine/pedagogy. What's adapted on top is `skills/learn/`, `skills/recall/` (renamed from engram's `/review` to avoid colliding with `/peer-review`), and `skills/coach/` — the same teaching loop, with the multi-platform engine-resolution boilerplate stripped to a direct `${CLAUDE_PLUGIN_ROOT}/scripts/engram.py` reference, agent spawning simplified to bare Task-tool dispatch by name, and (in `/learn` only) research-os's own context-sourced intake and thematic-wiki/project-journal linkage woven directly into the flow rather than bolted on as a wrapper. This keeps the learning layer in sync with everything else here — one plugin update picks up wiki, second-brain, and learning changes together, and a topic learned via `/learn` links straight into the wiki page and project journal that motivated it. `state/upstream-repos.json`'s `engram` entry tracks the vendored commit so `/check-update-upstream-repos` can flag drift; a diff there means re-copying the changed upstream files and re-applying the same adaptation, not a plugin update.

Ships **no personal data** — vaults, the `_brain/` second brain (including `_brain/learning/`, engram's state directory), and projects live in the user's data directories, never in this plugin.

## Installed as

Registered as a local marketplace and installed as a real Claude Code plugin (not just source in this repo):
```
claude plugin marketplace add <path-to-this-repo>
claude plugin install research-os@research-os
```
After editing anything under `plugins/research-os/`, run `claude plugin marketplace update research-os` to pick up the change. `claude plugin details research-os@research-os` shows the live component inventory + token-cost estimate.

**Learning-layer state** needs `ENGRAM_HOME` set (in `~/.claude/settings.json`'s `env` block) to `<vault root>/_brain/learning` so learning state lives in the second brain rather than the engine's default `~/.claude/learning/`. On Windows/Anaconda setups without a `python3` on PATH (only `python`), the vendored skills hardcode `python3` in their shell blocks — add a one-line shim (`exec python "$@"`) somewhere ahead on `PATH` rather than editing the vendored files.

## Layout

| Dir | Contents |
|-----|----------|
| `skills/` | Slash-command skills (pipeline, wiki, routines, upstream-sync, help, learning, + consolidated general-purpose skills) |
| `agents/` | Worker↔critic agents (clo-author roster + ARS capabilities merged in) + `wiki-librarian`, `python-reviewer`, `code-reviewer` + `engram-curriculum-architect`, `engram-assessor`, `engram-artifact-smith` |
| `hooks/` | `hooks.json` (note: plugin hook manifests need a top-level `"hooks"` wrapper key — unlike a project's `.claude/settings.json`) + hook scripts (SessionStart nudges incl. engram's due-reviews nudge, a Stop two-output `/wiki-push` nudge, guards) |
| `rules/` | Governance rules (permissions, quality gates, folder-map, output-discipline, wiki-integration) |
| `templates/` | Project + vault + passport scaffolds |
| `state/` | Upstream-repo tracking (`upstream-repos.json` — clo-author, ARS, engram vendored; obsidian-second-brain watched for adoptable ideas) |
| `scripts/engram.py` | Vendored FSRS-4.5 learning engine — stdlib-only, self-testing, never hand-edited (see Update note below) |
| `docs/`, `gold/`, `references/` | Vendored engram pedagogy docs, grader gold-set, and upstream README/LICENSE — cited by the learning skills for provenance |

**Updating the vendored engram files:** never patch `scripts/engram.py` or `agents/engram-*.md`/`skills/_shared/*` directly with local fixes — re-copy from upstream at the new commit, then re-apply the same two adaptations (engine-path + agent-spawn simplification) by hand. `/check-update-upstream-repos` flags when upstream has moved past the recorded `last_seen_sha`.

## Status

- [x] Phase 1: plugin skeleton, trim globals, fix broken bits
- [x] Phase 2: project layer (globalize + rewire clo-author, merge ARS)
- [x] Phase 3: knowledge layer (two-layer vault, registry, PDF pipeline)
- [x] Phase 4: routines + upstream sync (daily-summary, weekly-planning, check-update-upstream-repos)
- [x] DZ-specific output types (Geldbrief/Fachtext/Hintergrundpapier/Policy Brief) removed — academic paper only, per house-style calibration never materializing
- [x] Global skill/agent consolidation — audited every remaining global skill/agent against research-os's own coverage; survivors vendored here, `claude-global/` retired, `~/.claude/skills`+`agents` now empty of custom content
- [x] Phase 5: learning layer — engram **vendored directly** into this plugin (engine, agents, and shared pedagogy files copied in; not installed as a separate plugin); `/learn` is the context-sourced intake woven into engram's real teaching loop; `/recall` is engram's review loop (renamed to avoid colliding with `/peer-review`); `/coach` is engram's telemetry/strategy/dashboard loop, also vendored
- [x] Phase 6: second-brain layer — per-folder READMEs + `note_type` templates for every `_brain/` folder, hybrid project note (Orientation + Journal, repairs the `index.md` catalog), surgical wiki conventions (In-brief lede, inline `confidence` tags, `(as of …)` stamps), Claude-readable `_map.md` MOC (`generate_wiki_moc.py`), `/connect` cross-theme bridge-finder, a standing two-output/propagation rule + Stop-hook `/wiki-push` nudge, narrow regeneration sentinels, `_brain` checks in `wiki_quality_check.py`, scheduled agents (morning brief / nightly consolidation / weekly review+planning / weekly health audit), and obsidian-second-brain added as a watched upstream

## Publishing note

When sharing with DZ, keep personal data out of the published tree — either move this plugin to its own repository, or `.gitignore` the unified Obsidian vault root and any `_brain/` content from the marketplace repo.
