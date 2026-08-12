---
name: tools
description: Utility commands — graph, commit, compile, validate-bib, lint, journal, context, dashboard, deploy, learn, upgrade, permission-check. Lightweight project-maintenance subcommands with no multi-agent orchestration.
argument-hint: "[subcommand: graph | commit | compile | validate-bib | lint | journal | context | dashboard | deploy | learn | upgrade | permission-check] [args] [--open]"
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

### `/tools graph [status | next | why <node> | stale | dot]` — Pipeline Graph

Ask the pipeline graph what is runnable right now. `rules/permissions.md` declares every agent's
REQUIRES / PRODUCES / PARALLEL_GROUP; `${CLAUDE_PLUGIN_ROOT}/graph/pipeline.json` is the
machine-readable twin of that, and this router evaluates it against the project's actual state.

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/graph.py" next          # the ready frontier
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/graph.py" status        # every node's state
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/graph.py" why coder     # which requirement is missing
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/graph.py" stale         # inputs changed since a recorded run
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/graph.py" dot --mermaid # render the graph
```

| Subcommand | Answers |
|---|---|
| `next` | "What can I work on?" — required vs optional, and which nodes run **in parallel** |
| `status` | every node as `done` / `stale` / `ungated` / `ready` / `blocked` / `n/a` |
| `why <node>` | the exact failing predicate, plus that node's upstream and downstream |
| `stale` | nodes whose declared inputs changed since their recorded run — **advisory, always exits 0** |
| `record <node> --score N` | append a run to `00_admin/process/runs.jsonl` — the orchestrator calls this after every critic score |
| `adopt [--dry-run]` | backfill the ledger for a project that predates the graph — one-time, explicit, idempotent |
| `dot` | Graphviz (or `--mermaid`) render for the dashboard or a quick look |

**It recommends; it never dispatches.** The frontier is a suggestion — you still choose and run
the skill. Pass `--json` to `status` / `next` / `stale` for structured output.

Node state is *computed* on every call from the graph + the filesystem + `passport.yaml` +
`00_admin/process/runs.jsonl`, never stored, so it cannot desync from the project.
`record` is the only thing that writes — an **append-only** ledger, never rewritten.

`selftest` asserts the graph and `rules/permissions.md` still agree — run it after editing either:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/graph.py" selftest
```

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
cd 04_paper/academic_paper && latexmk [file]
```

For talks:
```bash
cd 05_outreach/talks && latexmk [file]
```

Note: the `latexmkrc` in each `04_paper/academic_paper/` folder configures XeLaTeX, TEXINPUTS, and BIBINPUTS. Falls back to a manual 3-pass build if latexmk is unavailable.

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

### `/tools permission-check [tool-call or path]` — Diagnose a Permission Prompt

Explain why a permission prompt fired (or why one did *not*). Read-only diagnosis: this subcommand reports what the settings layers say and never edits them.

**Input:** the tool call or path that triggered the prompt, as best you have it — `Bash(git push origin main)`, `Write` on `03_analysis/scripts/R/02_estimate.R`, or just the tool name. With no argument, report the effective configuration without diagnosing a specific call.

**Step 1 — Walk the layers in precedence order.** Later layers override earlier ones for the same setting; read all five before concluding anything.

| # | Layer | Path | Notes |
|---|-------|------|-------|
| 1 | Managed policy | `/Library/Application Support/ClaudeCode/managed-settings.json` (macOS), `/etc/claude-code/managed-settings.json` (Linux), `C:\ProgramData\ClaudeCode\managed-settings.json` (Windows) | Administrator-set. Cannot be overridden by anything below. Usually absent on a personal machine — say "absent" rather than assuming. |
| 2 | User settings | `~/.claude/settings.json` | The main allow/deny surface on this machine. |
| 3 | Project settings | `<project>/.claude/settings.json` | Shared, committed. |
| 4 | Local project settings | `<project>/.claude/settings.local.json` | Personal, gitignored. Overrides the shared project file. |
| 5 | CLI flags / session state | `--permission-mode`, `--allowedTools`, `/careful`, `/freeze` | Highest precedence. A scheduled run's `--allowedTools` allowlist lives here (`${CLAUDE_PLUGIN_ROOT}/references/scheduled-agents.md`). |

```bash
ls -la ~/.claude/settings.json .claude/settings.json .claude/settings.local.json 2>/dev/null
```

Read each file that exists and report, per layer: whether it is present, its `defaultMode`, and any `permissions.allow` / `permissions.deny` / `permissions.ask` entry that could match the call. Name the file each matching rule came from — "allowed by `~/.claude/settings.json`" is the useful answer; "allowed" is not.

**Step 2 — Report `defaultMode`.** State the effective mode and which layer set it: `default` (prompt on first use of each tool), `auto`, `acceptEdits` (file edits auto-accepted, other tools still prompt), `plan` (no mutation at all), or `bypassPermissions`. Report the raw value you read rather than normalizing it. The mode explains *why a prompt appeared at all*; the `allow`/`deny` rules explain *what happened to this specific call*. Both go in the report — a prompt under `plan` mode and a prompt from a missing allow entry need different fixes.

**Step 3 — Check `deny` before `allow`.** `deny` wins over `allow` regardless of ordering or specificity, so evaluate it first. Reporting "it is in your allow list" when a `deny` entry also matches is the wrong answer and the most common way this diagnosis goes wrong. The user's `deny` list covers destructive git operations and `rm -rf`; a prompt or refusal on one of those is a deny hit, not a missing allow entry.

Then check `ask`, then `allow`. Report the first matching rule per class and the pattern that matched, so the user can see whether the pattern is narrower or wider than they intended (an escaped-regex artifact in a `Bash(...)` pattern is a common cause of a rule that never matches).

**Step 4 — Check the hard-protected set.** Some paths are protected by Claude Code itself, above the settings layers. Writes and edits to the permission surface under `.claude/` — `settings.json`, `settings.local.json`, and the hooks configuration — always require explicit approval, whatever `defaultMode` is and whatever the `allow` list says. A permission system that the thing it constrains could silently edit is not a permission system. If the call targets one of these, that is the whole explanation: the prompt came from above the five layers, and adding an `allow` entry will not remove it.

Also check the plugin's own `PreToolUse` hooks (`${CLAUDE_PLUGIN_ROOT}/hooks/hooks.json`). `git-guardrails.py` denies destructive git operations and `protect-files.py` denies writes to a basename deny-list, both independently of settings and both **before** the permission layers are consulted. A denial from a hook names the hook in its message, so if the user saw a hook name, stop there: the settings layers never ran. The user `deny` list deliberately duplicates part of `git-guardrails.py` as defence in depth, so a given command may match both — say which one actually fired.

**Step 5 — Report.**

```
Call:      Bash(git reset --hard HEAD~1)
Verdict:   DENIED
Fired at:  hooks/git-guardrails.py (PreToolUse, before the settings layers)
Also matches: permissions.deny `Bash(git reset --hard*)` in ~/.claude/settings.json
              — defence in depth; removing one would not have allowed this.
defaultMode: auto  (set in ~/.claude/settings.json)
Hard-protected path: no
Fix:       This is a deliberate guardrail, not a misconfiguration. If you need
           the operation, run it in a terminal outside Claude Code. If the
           guardrail itself is wrong, change it with /update-config.
```

**Never edit settings from this subcommand.** It diagnoses and stops. Changing permissions, adding allow entries, or altering `defaultMode` is `/update-config`'s job — point the user there with the specific change, and let them make it.

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
- **`.claude/` stays editable.** Config, permissions, and session `state/` are never frozen or protected out from under you by research-os. Claude Code itself still asks before writing there — see `/tools permission-check` step 4 — which is a confirmation prompt, not a lock.
- **permission-check reports, it never fixes.** Diagnosis and mutation are separate; settings changes go through `/update-config`.
