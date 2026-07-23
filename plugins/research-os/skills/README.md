# skills/

Slash-command skills for research-os. Each is a directory with a `SKILL.md` (YAML frontmatter: `name`, `description`, `argument-hint`, `allowed-tools`). Run `claude plugin details research-os@research-os` for the live, auto-generated roster + token-cost inventory rather than relying on this file for an exact count.

- **Pipeline (from clo-author, rewired + ARS-merged):** `discover`, `strategize`, `analyze`, `write`, `peer-review` (was `review`), `revise`, `talk`, `submit`, `tools`, `checkpoint`, `dashboard`, `freeze`, `careful`
- **Project:** `create-project`, `research-os-help`
- **Knowledge:** `wiki-setup`, `add-vault`, `wiki-pull`, `wiki-push`, `wiki-ingest`, `wiki-maintain` (all vendored here — previously split across a separate `claude-global/` sync mechanism, retired once research-os itself became the global plugin install)
- **Routines:** `daily-summary`, `weekly-planning`
- **Maintenance:** `check-update-upstream-repos`
- **Learning (Phase 5):** `learn` (context-sourced intake, hands off to the separately-installed `engram` plugin's `engram:learn`), `recall` (thin alias for `engram:review`) — `/coach` is engram's own, used directly, not vendored or wrapped here
- **General-purpose (consolidated from global skills — kept after an audit of what research-os doesn't already cover):** `article-writing`, `content-engine`, `frontend-slides`, `git-workflow`, `python-patterns`, `python-testing`, `documentation-lookup`, `exa-search`, `prompt-optimizer`, `skill-stocktake`, `continuous-learning-v2` (+ its `learned/` data dir), `data-scraper-agent`
