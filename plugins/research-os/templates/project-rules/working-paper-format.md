---
paths:
  - "04_paper/**/*.tex"
  - "**/*.tex"
---

<!-- Written by /create-project. Thin pointer, not the rule itself: the full
     text lives in the plugin and is the single source of truth. This stub
     exists only so the rule ACTIVATES automatically - plugin rules/ is not a
     recognized Claude Code component and never auto-loads, but project-scope
     .claude/rules/ does, and honours `paths:` frontmatter. -->

# Paper Format

LaTeX conventions for the manuscript: biblatex + biber (not natbib), booktabs rules
(no `\hline`, no vertical rules), `threeparttable`/`talltblr` table notes, `hyperref`
second-to-last with `cleveref` immediately after, significance-star policy per the
journal profile.

**Read `${CLAUDE_PLUGIN_ROOT}/rules/working-paper-format.md` before editing the
manuscript preamble or adding a table or figure.**
