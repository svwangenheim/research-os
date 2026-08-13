---
paths:
  - "03_analysis/**"
  - "04_paper/**"
---

<!-- Written by /create-project. Thin pointer, not the rule itself: the full
     text lives in the plugin and is the single source of truth. This stub
     exists only so the rule ACTIVATES automatically - plugin rules/ is not a
     recognized Claude Code component and never auto-loads, but project-scope
     .claude/rules/ does, and honours `paths:` frontmatter. -->

# Code and Paper Invariants

Work in these directories is governed by the numbered invariants INV-1 .. INV-22.

The ones that bite most often: no absolute paths (INV-16, enforced at write time by
`hooks/git-guardrails.py`); `set.seed()` exactly once at the top (INV-14); packages
loaded at the top (INV-15); no `setwd()` / `rm(list=ls())` / `install.packages()` in
scripts (INV-19); numbers in the text match the tables exactly (INV-11); every
non-trivial claim registered in `passport.yaml` `claim_manifest` (INV-22).

**Read `${CLAUDE_PLUGIN_ROOT}/rules/content-invariants.md` in full before non-trivial
work here.** Critics cite these by number, so knowing which one you tripped is the
difference between a fix and a guess.
