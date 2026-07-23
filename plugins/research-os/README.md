# research-os (plugin)

Personal research operating system for Claude Code. Built on the [clo-author](https://github.com/hugosantanna/clo-author) fork, enhanced with the integrity layer of [ARS](https://github.com/Imbad0202/academic-research-skills), a two-layer Obsidian knowledge base, daily/weekly routines, and a spaced-repetition learning layer ([engram](https://github.com/nagisanzenin/engram)).

Sits **above** `dz-core` (calls into it for branded charts, branded-PDF build, Instagram tiles, onboarding). Ships **no personal data** — vaults, the `_brain/` second brain, and projects live in the user's data directories, never in this plugin.

## Layout

| Dir | Contents |
|-----|----------|
| `skills/` | Slash-command skills (pipeline, wiki, routines, learning, help, upstream-sync) |
| `agents/` | Worker↔critic agents (clo-author roster + ARS capabilities merged in) |
| `hooks/` | `hooks.json` + hook scripts (SessionStart nudges, guards) |
| `rules/` | Governance rules (permissions, quality gates, folder-map, output-discipline, wiki-integration) |
| `templates/` | Project + vault + passport scaffolds |

## Status

Under construction — see the build plan at `~/.claude/plans/help-me-create-my-dazzling-turtle.md`.

- [x] Phase 1: plugin skeleton
- [ ] Phase 1: trim globals, fix broken bits
- [ ] Phase 2: project layer (globalize + rewire clo-author, merge ARS)
- [ ] Phase 3: knowledge layer (two-layer vault, registry, PDF pipeline)
- [ ] Phase 4: routines + upstream sync
- [ ] Phase 5: learning layer (engram-adapted)

## Publishing note

When sharing with DZ, keep personal data out of the published tree — either move this plugin to its own repository, or `.gitignore` the unified Obsidian vault root and any `_brain/` content from the marketplace repo.
