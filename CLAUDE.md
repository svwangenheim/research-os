# CLAUDE.md — Working on research-os

<!-- Loaded every session. Keep it under ~150 lines: it is the standing brief, not the
     documentation. Full documentation is in README.md; the per-directory READMEs are
     the source of truth for their own contents. -->

**Repo:** research-os — a Claude Code plugin (`plugins/research-os/`) plus the personal Obsidian vault it maintains (`vault/`, gitignored, its own local repo).
**Owner:** Sven von Wangenheim, Dezernat Zukunft
**Main branch:** `main`

This file governs work **on the plugin itself**. A research project scaffolded by `/create-project` gets its own `CLAUDE.md` from `plugins/research-os/templates/project-CLAUDE.md`; that one governs the project, not this.

---

## Core Principles

- **Plan first** — enter plan mode for anything non-trivial; plans persist under `00_admin/process/`.
- **Enforcement lives in hooks, not instructions** — anything that must happen every time goes in `hooks/`, because rules can be compressed out of context and hooks cannot.
- **One source of truth per fact** — `rules/permissions.md` for agent capabilities, `rules/folder-map.md` for paths, `rules/model-routing.md` for models, `graph/pipeline.json` for phase dependencies. Nothing restates them.
- **Worker-critic pairs** — every creator has a paired critic; critics never edit files.
- **Verify after** — run the two checkers before every commit (below). Deterministic drift is caught by scripts, not by review.
- **Update over create** — a new file only for a genuinely new question. See `rules/output-discipline.md`.

Authoring style for every Claude-facing file is specified in [`plugins/research-os/references/authoring-conventions.md`](plugins/research-os/references/authoring-conventions.md). New skills start from [`plugins/research-os/templates/skill-template.md`](plugins/research-os/templates/skill-template.md).

---

## Layout

```
research-os/
├── CLAUDE.md                     # This file
├── README.md                     # Full documentation and the skill/agent index
├── CHANGELOG.md / BACKLOG.md     # What shipped / what was deferred and why
├── 00_admin/process/             # Session journals
├── docs/PROVENANCE.md            # What came from where, at which upstream commit
├── scripts/install-hooks.sh      # Installs .githooks as core.hooksPath
├── plugins/research-os/
│   ├── skills/                   # Slash commands (one dir per skill, SKILL.md + Level-3 files)
│   ├── agents/                   # Worker and critic agents, each pinned to model + effort
│   ├── rules/                    # Governance rules
│   ├── hooks/                    # Session and tool-event enforcement
│   ├── graph/pipeline.json       # The pipeline as a declared dependency graph
│   ├── references/               # Standing knowledge (internal/ is gitignored)
│   ├── templates/                # Project, vault, passport, and skill scaffolds
│   └── scripts/                  # Status line, dashboards, engine, checkers, scheduled routines
└── vault/                        # Gitignored — personal brain + thematic wikis
```

---

## Commands

```bash
# The two deterministic gates — run both before committing
python plugins/research-os/scripts/check_plugin_integrity.py
python plugins/research-os/scripts/check_surface_sync.py

# Install the pre-commit hook that runs them
bash scripts/install-hooks.sh

# Pipeline graph
python plugins/research-os/scripts/graph.py next          # ready frontier
python plugins/research-os/scripts/graph.py why <node>    # the unmet predicate
python plugins/research-os/scripts/graph.py selftest      # graph vs rules/permissions.md

# Vault and dashboards
python plugins/research-os/scripts/generate_wiki_moc.py
python plugins/research-os/scripts/generate_dashboard.py
```

Bypass the gate only with `SKIP_INTEGRITY_GATE=1` and record the reason in the commit body. CI (`.github/workflows/gates.yml`) runs both checkers on every pull request, so a bypassed commit surfaces there.

---

## Where Things Go

| If it must… | It is a… | Lives in |
|---|---|---|
| happen every time, regardless of context | hook | `plugins/research-os/hooks/` |
| always be true in a domain | rule | `plugins/research-os/rules/` |
| run as a named workflow the user invokes | skill | `plugins/research-os/skills/<name>/` |
| do specialist work under dispatch | agent | `plugins/research-os/agents/` |
| be known but not obeyed | reference | `plugins/research-os/references/` |
| be one person's recurring busywork | procedure | `vault/_brain/procedures/` via `/automate` |

Procedures may call skills. Skills never call procedures — one direction only, so the two layers cannot re-merge.

---

## Conventions in One Screen

- **Em dash, never `--`.** `--` is literal only in code fences and CLI flags.
- **H1 is Title Case, no leading slash.** `# Wiki Push`, not `# /wiki-push — pushing the wiki`.
- **Skill frontmatter:** `name`, `description` (ending in a `Use when…` clause with real trigger phrases), `argument-hint`, `allowed-tools` (comma-separated, no spaces).
- **Agent frontmatter:** `name`, `description`, `tools` (comma-separated with spaces — **not** `allowed-tools`), `model`, `effort`.
- **`SKILL.md` under 300 lines.** Past that, move content into `templates/`, `references/`, or `config/` beside the skill and list it in the Bundled Resources table.
- **Bundled paths** use `${CLAUDE_PLUGIN_ROOT}/skills/<name>/…` in backticks. Relative markdown links are for documentation-to-documentation links only.
- **Every agent** appears in `rules/permissions.md`. **Every rule** appears in `rules/README.md`. **Every hook** appears in `hooks/README.md`.

---

## Git

- Branch off `main`; the current working branch is a feature branch.
- Conventional commits: `feat|fix|refactor|docs|test|chore|perf|ci: <description>`.
- Never commit anything from `vault/` — it is gitignored deliberately and has its own remote-less repo.
- Never commit raw microdata, credentials, or restricted-data extracts. See `rules/confidential-data.md`.

---

## Upstreams

This plugin is built on four tracked repos; drift is reviewed roughly bimonthly with `/check-update-upstream-repos`, and the record of what came from where lives in [`docs/PROVENANCE.md`](docs/PROVENANCE.md).

| Upstream | What we took |
|---|---|
| [clo-author](https://github.com/hugosantanna/clo-author) | The research pipeline: skills, agents, hooks, rules, progressive disclosure. |
| [ARS](https://github.com/Imbad0202/academic-research-skills) | The integrity layer: citation triangulation, anachronism audit, PRISMA. |
| [claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow) | Harness patterns: hooks over instructions, model/effort routing, forked verification, deterministic self-governance. |
| [engram](https://github.com/nagisanzenin/engram) | The learning layer, vendored: FSRS engine, curriculum/assessor/artifact agents. |
