# research-os

**A personal AI research assistant with persistent memory.** It runs an actual research project end to end — from an initial idea to a submitted paper — while maintaining a growing, organized set of notes about your research field and about you, so each new conversation continues from where the last one left off rather than starting over. It can also teach concepts properly and hold you to a daily and weekly routine.

This repo is a [Claude Code](https://claude.com/claude-code) plugin (`plugins/research-os/`) plus the personal Obsidian vault it maintains (`vault/`, kept out of this public repo — see [Privacy](#privacy) below).

## Contents

- [Motivation](#motivation)
- [The three layers](#the-three-layers)
- [Two roles: research assistant and personal assistant](#two-roles-research-assistant-and-personal-assistant)
- [Getting started](#getting-started)
- [Common workflows](#common-workflows)
- [Skills vs. agents](#skills-vs-agents)
- [Every skill and agent](#every-skill-and-agent)
  - [Research workflow](#research-workflow-the-academic-pipeline)
  - [Wiki & knowledge](#wiki--knowledge)
  - [Second brain & admin](#second-brain--admin)
  - [Learning (engram)](#learning-engram)
  - [Coding](#coding)
  - [Other / general-purpose](#other--general-purpose)
- [Layout](#layout)
- [Acknowledgments](#acknowledgments)
- [Scheduled admin routines](#scheduled-admin-routines)
- [Privacy](#privacy)

## Motivation

research-os is a single AI research assistant setup that works across every research project you run. It organizes your work and assists you through the entire empirical research process — from an initial idea to a submitted paper — while retaining context across all of your projects, not just within one conversation. It doubles as a second brain and knowledge wiki for researchers: literature, methods, datasets, and your own thinking accumulate in one place instead of evaporating at the end of each session.

Every AI conversation otherwise starts from a blank slate: you re-explain your project each time, ideas raised mid-conversation are lost, and your notes never reach your AI assistant. At the same time, research work involves a lot of repetitive scaffolding — folder structures, literature reviews, citation formatting, replication packages — that a disciplined process can largely handle for you, provided something actually enforces that process. research-os is built to solve both: a system that retains context, and a system that does not skip steps.

## The three layers

**1. A research pipeline.** Discover a question → design the strategy → analyze the data → write the paper → get it peer-reviewed → revise → submit. Each phase has a specialist "worker" agent and, in most phases, a paired "critic" agent whose sole job is to find problems in the worker's output — critics cannot edit files, and workers cannot grade their own work. This part is built on [clo-author](https://github.com/hugosantanna/clo-author), with [ARS](https://github.com/Imbad0202/academic-research-skills)'s integrity checks incorporated (see [Acknowledgments](#acknowledgments)).

**2. A two-layer knowledge base.** `_brain/` is your personal space — profile, daily/weekly notes, project journals, your own synthesis. Alongside it sit one or more **thematic wikis** — Claude-maintained knowledge bases, one per research theme, that absorb every paper, dataset, and method you feed them and continuously rewrite themselves to stay current rather than simply accumulating notes. You read the wikis; you do not edit them directly.

**3. A learning layer.** Built on [engram](https://github.com/nagisanzenin/engram), vendored directly into this plugin: point it at anything that was unclear, and it teaches the concept properly — a first-principles breakdown, Socratic dialogue, tested recall — then schedules spaced-repetition reviews so it is retained.

## Two roles: research assistant and personal assistant

The skills described here serve two distinct functions within one system:

- **Research assistant** — the pipeline and the wikis. This is the part that helps you conduct the research itself: finding the literature, designing the strategy, running the analysis, writing the paper, navigating peer review, and maintaining a knowledge base that improves with every source you add.
- **Personal assistant** — the daily and weekly admin routines and the learning layer. This is the part that tracks your work: what happened today, what is planned for the week, what is due for review, and what you asked to actually learn rather than delegate outright.

You do not need to track which role is active at a given moment. Running `/checkpoint` at the end of a session, `/daily-summary` at the end of a day, `/weekly-planning` at the end of a week, and `/learn` whenever something is unclear is enough — the system routes the rest.

## Getting started

Four steps, in order. The first two are required; the remainder depend on what you need.

**1. Install** the plugin (not just source in this repo — a real install):
```
claude plugin marketplace add <path-to-this-repo>
claude plugin install research-os@research-os
```

**2. Set up the knowledge base — `/wiki-setup`.** Run this before anything else; every other capability assumes it exists. It is conversational: it asks whether you already have a wiki or vault somewhere (point it there), or whether you are starting fresh (it builds everything — folder structure, Obsidian config, the registry — in one pass), then runs a short profile interview. You will come out the other side with a real `_brain/profile.md` and, if you provided one, at least one registered thematic wiki.

**3. Get oriented — `/research-os-help`.** New to this system? Run `/research-os-help eli5` for a plain-language walkthrough. Already in a project and unsure what's next? Plain `/research-os-help` reads that project's state and tells you exactly where you are and what to do next. Return to this command any time you're unsure — it's the front door, not a one-time onboarding step.

**4. Do something.** Pick whichever matches what's in front of you:
- Have a research question? → `/create-project "does X affect Y"`
- Have a paper or dataset worth preserving? → `/wiki-ingest paper.pdf`
- Something was unclear (a method, a piece of code, anything)? → `/learn`
- Want the full inventory? → the tables below, or `/research-os-help list`

For the plugin's technical internals (directory-by-directory component inventory, token-cost notes, vendoring details), see [plugins/research-os/README.md](plugins/research-os/README.md).

## Common workflows

**Starting a new project** — `/create-project "does X affect Y"` runs a short interview, identifies (or asks about) which thematic wiki the project belongs to, and scaffolds the full folder tree, a project config, and a starter dashboard. Nothing is inferred silently; every step is confirmed.

**Ingesting a paper** — `/wiki-ingest paper.pdf` extracts the source, writes a proper summary page, updates or creates the relevant concept, method, and dataset pages in the wiki, and links everything together. The next time this topic comes up in any project, `/wiki-pull` retrieves it automatically.

**Closing a work session** — `/checkpoint` records what happened and what comes next in that project's journal note, so the next session — yours or a future Claude's — does not start from zero. At the end of the day, `/daily-summary` rolls that up across every project touched, along with a scan of Slack and mail for anything relevant; `/weekly-planning` does the same at the end of the week, checking what actually happened against what was planned.

**Encountering something unclear** — `/learn` (no need to name the topic — point it at whatever was unclear) breaks it into a first-principles concept map, teaches it Socratically (prompting you to generate answers rather than reading them to you), and schedules a review so it is still retained a month later.

## Skills vs. agents

A **skill** is something you invoke directly — a slash command like `/checkpoint`, a procedure Claude follows step by step. An **agent** is a specialized worker that a skill dispatches to complete one bounded piece of work and report back (for example, `/analyze` dispatches the `coder` agent to write analysis code, and the `coder-critic` agent to review it). You will use skills constantly; you will rarely invoke an agent by name yourself — they operate behind the scenes.

## Every skill and agent

Grouped by function. One line each, in plain language — see each skill's own file for the full technical description.

### Research workflow (the academic pipeline)

| Skill | What it's for |
|---|---|
| `/create-project` | Scaffold a new research project — folders, config, dashboard. |
| `/discover` | Start a project: literature search, data search, brainstorming, or a guided interview to land on a research question. |
| `/strategize` | Design the empirical strategy — identification approach, pre-analysis plan, or formal theory. |
| `/analyze` | Turn the strategy into code and results (R, Python, or Julia). |
| `/write` | Draft the paper itself, section by section, in an academic voice. |
| `/peer-review` | Simulate a journal's peer review — an editor and referees who can disagree with you. |
| `/revise` | Respond to referee comments: classify, draft the response, then audit the response letter itself. |
| `/submit` | Prepare for submission — journal targeting, replication package, AI-use disclosure, final checks. |
| `/talk` | Turn the paper into a presentation — Beamer or a modern web deck. |
| `/dashboard` | Generate a single-page HTML overview of the project. |
| `/tools` | Project utilities: commit, compile, check the bibliography, deploy. |
| `/freeze` | Lock a set of folders against accidental edits while you focus elsewhere. |
| `/careful` | Block dangerous shell commands (`rm -rf`, force-push, etc.) for the rest of the session. |

Agents dispatched by the above (not called directly):

| Agent(s) | Dispatched by | What they do |
|---|---|---|
| `librarian` / `librarian-critic` | `/discover` | Find related papers and build a literature review; the critic checks for coverage gaps. |
| `explorer` / `explorer-critic` | `/discover` | Find and evaluate datasets; the critic checks measurement validity and identification fit. |
| `strategist` / `strategist-critic` | `/strategize` | Design the empirical strategy; the critic serves as gatekeeper and must sign off. |
| `theorist` / `theorist-critic` | `/strategize` | Write formal theory and proofs; the critic checks logical validity. |
| `coder` / `data-engineer` / `coder-critic` | `/analyze` | Write the analysis code and cleaning scripts; the critic reviews both. |
| `writer` / `writer-critic` | `/write` | Draft paper sections; the critic checks the draft against the evidence. |
| `storyteller` / `storyteller-critic` | `/talk` | Build the presentation; the critic checks narrative flow and whether it compiles. |
| `domain-referee` / `methods-referee` / `editor` | `/peer-review` | Referee field substance and methods separately; the editor makes the final call. |
| `orchestrator` | (infrastructure) | Coordinates execution across the pipeline — determines what runs next and enforces quality gates. |
| `verifier` | (infrastructure) | Confirms everything compiles, runs, and replicates before a commit, PR, or submission. |

### Wiki & knowledge

| Skill | What it's for |
|---|---|
| `/wiki-setup` | Set up or repair the two-layer knowledge system — run this first on a new machine. |
| `/add-thematic-wiki` | Register a new thematic wiki — adopt an existing one or start a new, empty one. |
| `/wiki-ingest` | Feed in a source (PDF, document, citation) and have it properly filed — summary, linked concept/method/dataset pages. |
| `/wiki-pull` | At the start of work, retrieve what is already known about the topic. |
| `/wiki-push` | At the end of work, write new knowledge back into the wikis and your personal brain. |
| `/wiki-maintain` | Audit and clean up a wiki — deduplicate, fix broken links, tidy summaries. |
| `/connect` | Ask what connects two themes and surface non-obvious links (read-only, never writes). |

| Agent | Dispatched by | What it does |
|---|---|---|
| `wiki-librarian` | all of the above | Enforces the two-layer knowledge model's standards behind the scenes. |

### Second brain & admin

| Skill | What it's for |
|---|---|
| `/checkpoint` | End-of-session save: what happened and what's next, into the project's journal. |
| `/daily-summary` | End-of-day routine: commits the day's work, writes a summary, checks Slack/mail for anything relevant. |
| `/weekly-planning` | End-of-week routine: reviews plan against reality, sets next week's goals, proposes calendar blocks. |
| `/check-update-upstream-repos` | Checks whether the open-source projects this system is built on have changed since last reviewed. |
| `/research-os-help` | The front door — "what's next," "what can this do," or a full plain-language walkthrough of the system. |

No dedicated agents in this group — these skills operate directly, without dispatching a named worker.

### Learning (engram)

| Skill | What it's for |
|---|---|
| `/learn` | Learn a concept properly — first-principles teaching, Socratic dialogue, tested recall. |
| `/recall` | A two-minute daily habit: clear whatever is due for spaced-repetition review. |
| `/coach` | Track learning progress — retention stats, a dashboard, tuning how the tutor teaches. |

| Agent | Dispatched by | What it does |
|---|---|---|
| `engram-curriculum-architect` | `/learn` | Breaks a topic into a first-principles concept map before teaching begins. |
| `engram-assessor` | `/learn`, `/coach` | Grades what was produced — deliberately blind to the conversation so it cannot be swayed. |
| `engram-artifact-smith` | `/learn` | Builds an interactive HTML explainer for a concept that keeps causing difficulty. |

### Coding

| Skill | What it's for |
|---|---|
| `/python-patterns` | Pythonic idioms and best practices while coding. |
| `/python-testing` | pytest/TDD guidance while writing tests. |
| `/documentation-lookup` | Pull current library documentation instead of relying on training data. |
| `/git-workflow` | Branching, commit conventions, merge-vs-rebase guidance. |

| Agent | Dispatched by | What it does |
|---|---|---|
| `python-reviewer` | after Python edits | PEP 8, security, and performance review. |
| `code-reviewer` | after any code change | A senior-engineer-style review pass. |

### Other / general-purpose

| Skill | What it's for |
|---|---|
| `/article-writing` | Long-form writing — blog posts, guides, newsletters — in a consistent voice. |
| `/content-engine` | Turn one idea into platform-native content for X, LinkedIn, TikTok, YouTube, newsletters. |
| `/exa-search` | Neural web, code, and company search. |
| `/prompt-optimizer` | Feed it a rough prompt and get back a sharper one — never runs the task itself. |
| `/frontend-slides` | Build an animated HTML presentation, or convert a PowerPoint into one. |
| `/data-scraper-agent` | Stand up a free, scheduled scraper for any public data source. |
| `/continuous-learning-v2` | Claude observes its own sessions and gradually builds small learned preferences over time. |
| `/skill-stocktake` | Audit all skills and commands in this plugin for quality. |

| Agent | Dispatched by | What it does |
|---|---|---|
| `guide-writer` | writing-focused skills above | Writes documentation and guide pages in a pedagogical, tutorial voice. |

## Layout

**The plugin** (`plugins/research-os/`):

| Dir | Contents |
|---|---|
| `skills/` | All the slash commands above. |
| `agents/` | All the worker/critic agents above. |
| `hooks/` | Small scripts that fire on session start/stop/compact — nudges (due learning reviews, unpushed wiki knowledge), guardrails. |
| `rules/` | The governance rules agents follow (permissions, quality gates, wiki conventions). |
| `templates/` | Project, vault, and passport scaffolds. |
| `state/` | Tracks the upstream repos this is built on, so drift can be flagged. |
| `docs/`, `gold/`, `references/` | Vendored engram pedagogy docs, its grading gold-set, and reference material such as the [scheduled-agent specs](plugins/research-os/references/scheduled-agents.md). |

**The vault** (`vault/` — see [Privacy](#privacy)):

| Dir | Contents |
|---|---|
| `_brain/` | Your personal space — profile, daily/weekly notes, thoughts, project journals, personal and cross-theme synthesis. |
| `<theme>/` (e.g. `cognitive-load/`) | One thematic wiki per research area, each with the same numbered layout: `00_inbox` → `90_synthesis`. |
| `_templates/` | Shared note templates used by every wiki and `_brain/`. |
| `index.md` | Cross-wiki catalog. |

## Acknowledgments

- [clo-author](https://github.com/hugosantanna/clo-author) — the base research pipeline (skills, agents, hooks, rules), ported in and adapted.
- [academic-research-skills (ARS)](https://github.com/Imbad0202/academic-research-skills) — the integrity layer merged into the ported pipeline: citation triangulation, anachronism checks, PRISMA systematic-review support, multi-style citations, AI-use disclosure.
- [engram](https://github.com/nagisanzenin/engram) — the spaced-repetition learning engine, vendored directly rather than installed as a separate plugin: the FSRS-4.5 engine, its curriculum/assessment/artifact agents, and its pedagogy docs are copied in and adapted for this system.
- [obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain) — not integrated directly, but monitored for design ideas worth adopting: the freshness/confidence note conventions, the MOC/index approach, and the four-routine scheduled-agent design (see below) all draw on patterns from here.

## Scheduled admin routines

Four routines run unattended, entirely **locally** — no cloud, nothing pushed anywhere: a read-only morning brief (daily), a bounded-mutation nightly consolidation (daily; commits locally, never pushes), a read-only weekly vault-health audit (Fridays), and a draft-only weekly review and planning pass (Fridays). Each is a small PowerShell script (`plugins/research-os/scripts/scheduled/*.ps1`) registered as a Windows Scheduled Task, calling `claude -p` with a permission allowlist scoped to exactly what that routine needs — the nightly consolidation's allowlist simply has no `git push` in it, so it is structurally incapable of pushing, not merely instructed not to. Two of the four call the matching skill directly (`/research-os:daily-summary`, `/research-os:weekly-planning`) with an explicit non-interactive override, since those skills normally ask conversational questions a scheduled run has no one to answer. Every run logs to `vault/_brain/.scheduled-logs/<routine>/`.

See [scheduled-agents.md](plugins/research-os/references/scheduled-agents.md) for the exact schedule, prompts, and design rationale. Dry-run any of them by hand before trusting the schedule, and inspect the registered tasks with `schtasks /query /tn ResearchOS-<name> /fo LIST /v`.

## Privacy

`vault/` — your notes, profile, and everything the thematic wikis have learned — is **gitignored** in this repo and lives in its own independent local git repo instead (`vault/.git`, no remote). It is never part of this repo's history, including past commits, so this repo can be shared or made public without exposing any personal research content. The scheduled routines above do not change this — they are local processes with the same filesystem access as an interactive session, not a reason to push anything anywhere.
