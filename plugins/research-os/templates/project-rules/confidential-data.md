---
paths:
  - "02_data/**"
  - "**/*.dta"
  - "**/*.sav"
  - "**/raw/**"
  - "**/restricted/**"
---

<!-- Written by /create-project. Thin pointer, not the rule itself: the full
     text lives in the plugin and is the single source of truth. This stub
     exists only so the rule ACTIVATES automatically - plugin rules/ is not a
     recognized Claude Code component and never auto-loads, but project-scope
     .claude/rules/ does, and honours `paths:` frontmatter. -->

# Restricted Data

Three hard rules: never commit raw confidential data; nothing leaves without disclosure
clearance; access is per-person, per-agreement.

Set `RESEARCH_OS_STRICT_PATHS=1` while working here - it turns the hardcoded-path
warning into a hard denial, which matters more when the path names a location on a
secured machine.

**Read `${CLAUDE_PLUGIN_ROOT}/rules/confidential-data.md` before touching these paths.**
