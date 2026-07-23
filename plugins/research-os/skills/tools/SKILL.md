---
name: tools
description: Utility commands — commit, compile, validate-bib, lint, journal, context, dashboard, deploy, learn, upgrade. Lightweight project-maintenance subcommands with no multi-agent orchestration.
argument-hint: "[subcommand: commit | compile | validate-bib | lint | journal | context | dashboard | deploy | learn | upgrade] [args]"
allowed-tools: Read,Grep,Glob,Write,Edit,Bash,Task
---

# Tools

Utility subcommands for project maintenance and infrastructure.

**Input:** `$ARGUMENTS` — subcommand followed by any arguments.

All paths follow the numbered project scheme (`${CLAUDE_PLUGIN_ROOT}/rules/folder-map.md` — the single source of truth). State lives in `passport.yaml` (schema: `${CLAUDE_PLUGIN_ROOT}/templates/passport.yaml`); narrative context in `00_admin/process/`.

---

## Subcommands

### `/tools dashboard [--open]` — Project Dashboard
Regenerate the living project dashboard.

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/generate_dashboard.py" --project-root .
```

If `--open` is specified (default), open the dashboard in the browser:
```bash
open project_dashboard.html
```

The generator scans the numbered project layout — `passport.yaml`, `01_literature/`, `02_data/`, `03_analysis/`, `04_paper/`, `00_admin/process/` — plus `wiki-links.md`, and renders `project_dashboard.html` at the project root. This is a thin wrapper around the `/dashboard` skill; prefer `/dashboard refresh` when you also want to preserve authored research sections. See `${CLAUDE_PLUGIN_ROOT}/rules/html-dashboard.md`.

### `/tools commit [message]` — Git Commit
Stage changes, create commit, optionally create PR and merge.
- Run `git status` to identify changes
- Stage relevant files (never stage `.env`, credentials, or `.claude/state/` files)
- Create commit with a descriptive message
- If a quality score is available in `passport.yaml` (`pipeline.stages`) and the relevant stage gate is met, note it in the commit

### `/tools compile [file]` — LaTeX Compilation
Automated multi-pass compilation via latexmk.

For papers (per selected output type):
```bash
cd 04_paper/<output> && latexmk [file]
```

For talks:
```bash
cd 05_outreach/talks && latexmk [file]
```

Note: the `latexmkrc` in each `04_paper/<output>/` folder configures XeLaTeX, TEXINPUTS, and BIBINPUTS. Falls back to a manual 3-pass build if latexmk is unavailable.

### `/tools validate-bib` — Bibliography Validation
Cross-reference all `\cite{}` keys in the paper and talk files against `01_literature/bibliography.bib`.
Report: missing entries, unused entries, duplicate keys. Also cross-check against `passport.yaml` `literature_corpus` so cited keys map to a recorded source.

### `/tools lint [file|dir]` — Mechanical Code Linting
Run grep-based checks on R/Python/Julia scripts against the coding standards' prohibited patterns. Catches mechanical violations before the coder-critic's judgment review.

```bash
"${CLAUDE_PLUGIN_ROOT}/hooks/lint-scripts.sh" [target]
```

- **Single file:** `/tools lint 03_analysis/scripts/R/02_estimate.R`
- **Directory:** `/tools lint 03_analysis/scripts/` (recursive)
- **Default:** `/tools lint` (lints `03_analysis/scripts/`)

**What it checks:**

| Check | R | Python | Julia | Severity |
|-------|---|--------|-------|----------|
| Absolute paths | x | x | x | HIGH |
| `setwd()` / `os.chdir()` / `cd()` | x | x | x | HIGH |
| Missing seed (stochastic code) | x | x | x | HIGH |
| `install.packages()` / `pip install` | x | x | | HIGH |
| `rm(list = ls())` | x | | | MEDIUM |
| `T`/`F` literals | x | | | MEDIUM |
| `sapply()` | x | | | MEDIUM |
| `attach()`/`detach()` | x | | | MEDIUM |
| `<<-` global assignment | x | | | MEDIUM |
| `stargazer` / `plyr` | x | | | MEDIUM |
| `set.seed()` position (after line 30) | x | | | MEDIUM |
| Wildcard imports | | x | | MEDIUM |
| `np.random.seed()` global state | | x | | MEDIUM |
| Bare `except:` | | x | | MEDIUM |
| `eval`/`@eval` runtime | | | x | MEDIUM |
| Late `library()`/`import`/`using` | x | x | x | LOW |
| `print()` for status | x | | | LOW |
| `require()` | x | | | LOW |
| `1:n` patterns | x | | | LOW |

**Output:** Findings by file with severity, line number, and fix suggestion. Always advisory (exit 0).

**When to use:**
- Before `/peer-review --code` — catches mechanical violations instantly
- Before commits — quick sanity check
- The coder-critic focuses on judgment (strategy alignment, numerical plausibility, design); this catches the grep-able stuff

### `/tools journal` — Research Journal
Regenerate / review the research journal timeline. The journal is `00_admin/process/journal.md` (newest-first, per `${CLAUDE_PLUGIN_ROOT}/rules/logging.md`) — a narrative record of agent actions, phase transitions, scores, and decisions. Scores and phase state are read from `passport.yaml` `pipeline.stages`; the journal explains the reasoning behind them.

### `/tools context` — Context Status
Show current context status and session health. Check context usage, whether auto-compact is approaching, and what state will be preserved (`passport.yaml`, `00_admin/process/`, git status). Run `/checkpoint` before compaction if unsaved work exists.

### `/tools deploy` — Deploy Guide Site
Render the Quarto guide site and publish to GitHub Pages.
```bash
cd guide && quarto publish gh-pages --no-browser
```

### `/tools learn` — Extract Learnings
Extract reusable knowledge from the current session. Auto-memory handles corrections automatically; objective, reusable knowledge (a new concept/method/dataset) is pushed *down* into the relevant wiki via `/wiki-ingest`, and cross-theme or personal insight is pushed *up* into `_brain/synthesis/`. Use this for a multi-step workflow worth turning into a full skill.

### `/tools upgrade` — Upgrade research-os
Update the research-os plugin to its latest version while preserving all project content.

**What it does:**
1. Update the plugin from its marketplace / source repository
2. Preserve everything project-local — the plugin ships no project state, so `passport.yaml`, `00_admin/`, `01_literature/`–`05_outreach/`, `CLAUDE.md`, `wiki-links.md`, and the project `.claude/` (permissions, `state/`, filled-in `00_admin/domain-profile.md`) are untouched
3. Report what changed (new/updated agents, skills, rules, templates)

**Rules:**
- The plugin is infrastructure; the project's numbered folders and `.claude/` remain editable and are never overwritten.
- Never touch user content in `00_admin/`–`05_outreach/`, `passport.yaml`, `CLAUDE.md`, `wiki-links.md`, `.gitignore`, or `01_literature/bibliography.bib`.

> Note: unlike clo-author's clone-and-replace `.claude/` upgrade, research-os is a Claude Code plugin — upgrade is a plugin/marketplace update, not a directory swap. No git merge, no upstream remote in the project.

---

## Bundled Resources

| Resource | Path | When |
|----------|------|------|
| Gotchas | `${CLAUDE_PLUGIN_ROOT}/skills/tools/gotchas.md` | Always — known failure points |

---

## Principles
- **Each subcommand is lightweight.** No multi-agent orchestration needed.
- **Compile uses latexmk.** Handles multi-pass and biber automatically.
- **validate-bib catches drift.** Run before commits to catch broken citations; cross-check against `passport.yaml` `literature_corpus`.
- **Upgrade preserves content.** Infrastructure changes; your project doesn't.
- **`.claude/` stays editable.** Config, permissions, and session `state/` are never frozen or protected out from under you.
