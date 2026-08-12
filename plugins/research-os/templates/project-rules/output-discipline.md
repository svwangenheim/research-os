---
paths:
  - "01_literature/**"
  - "03_analysis/output/**"
  - "04_paper/reviews/**"
---

<!-- Written by /create-project. Thin pointer, not the rule itself: the full
     text lives in the plugin and is the single source of truth. This stub
     exists only so the rule ACTIVATES automatically - plugin rules/ is not a
     recognized Claude Code component and never auto-loads, but project-scope
     .claude/rules/ does, and honours `paths:` frontmatter. -->

# Update Over Create

The default failure mode of an AI research assistant is file proliferation: a fresh
review, critic report, or analysis note on every re-run.

Improve the existing file. Create a new one only for a genuinely new question or
literature. Ask: is this a new question, or the same question re-examined? Same
question means update, and prepend a line to the file's `## Changelog`.

**Read `${CLAUDE_PLUGIN_ROOT}/rules/output-discipline.md` for the full contract.**
