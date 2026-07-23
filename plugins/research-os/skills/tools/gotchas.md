# Tools Skill -- Gotchas

- `latexmk` handles multi-pass compilation automatically -- don't run xelatex/biber manually unless debugging.
- `validate-bib` checks `01_literature/bibliography.bib` for common issues but doesn't verify that every citation key resolves to a recorded `passport.yaml` `literature_corpus` entry -- do both.
- Journal review (`/tools journal`) reads `00_admin/process/journal.md`; scores and phase state come from `passport.yaml` `pipeline.stages`, not the journal.
- Commit staging must never include `.env`, credentials, or `.claude/state/` files.
- The lint subcommand is advisory (exit 0 always). It catches grep-able violations in `03_analysis/scripts/`; the coder-critic handles judgment calls.
- `lint` and the dashboard/lint hook scripts live in `${CLAUDE_PLUGIN_ROOT}/hooks/` and `${CLAUDE_PLUGIN_ROOT}/scripts/`, not in the project -- invoke them via the plugin root, not a project-relative path.
- `upgrade` is a plugin/marketplace update, not a `.claude/` directory swap -- it preserves all project content because the plugin ships no project state.
- `.claude/` (config, permissions, `state/`) is always editable -- freeze/careful guards and protect-files never block it.
