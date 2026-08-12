---
paths:
  - "wiki-links.md"
  - "01_literature/**"
---

<!-- Written by /create-project. Thin pointer, not the rule itself: the full
     text lives in the plugin and is the single source of truth. This stub
     exists only so the rule ACTIVATES automatically - plugin rules/ is not a
     recognized Claude Code component and never auto-loads, but project-scope
     .claude/rules/ does, and honours `paths:` frontmatter. -->

# Knowledge Layer

This project is bridged to a thematic wiki and the personal brain. Resolve the target
wiki in this order: `--wiki <theme>` > `passport.yaml` `meta.main_wiki` >
`.research-os-wiki` pin file > the registry's only wiki > ask. Paths come from
`~/.claude/vaults.json`.

Read the corpus before searching the web. Sources are immutable; a newer source never
silently rewrites an older source's page.

**Read `${CLAUDE_PLUGIN_ROOT}/rules/wiki-integration.md` for the routing table, the
auto-write blast radius, and the regeneration-safety markers.**
