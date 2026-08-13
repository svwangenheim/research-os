# research-os

**A personal AI research assistant with persistent memory.** It runs an actual research project end to end — from an initial idea to a submitted paper — while maintaining a growing, organized set of notes about your research field and about you, so each new conversation continues from where the last one left off rather than starting over. It can also teach concepts properly and hold you to a daily and weekly routine.

This repo is a [Claude Code](https://claude.com/claude-code) plugin (`plugins/research-os/`) plus the personal Obsidian vault it maintains (`vault/`, kept out of this public repo — see [Privacy](#privacy) below).

## Contents

- [Motivation](#motivation)
- [The four layers](#the-four-layers)
- [How the vault, wikis, and projects fit together](#how-the-vault-wikis-and-projects-fit-together)
- [Two roles: research assistant and personal assistant](#two-roles-research-assistant-and-personal-assistant)
- [Getting started](#getting-started)
- [Common workflows](#common-workflows)
- [What runs without being asked](#what-runs-without-being-asked)
- [How claims get checked](#how-claims-get-checked)
- [Which model does what](#which-model-does-what)
- [Skills vs. agents](#skills-vs-agents)
- [Every skill and agent](#every-skill-and-agent)
  - [Research workflow](#research-workflow-the-academic-pipeline)
  - [Wiki & knowledge](#wiki--knowledge)
  - [Second brain & admin](#second-brain--admin)
  - [Learning (engram)](#learning-engram)
  - [Coding](#coding)
  - [Other / general-purpose](#other--general-purpose)
- [Layout](#layout)
- [Keeping the plugin honest](#keeping-the-plugin-honest)
- [Acknowledgments](#acknowledgments)
- [Scheduled admin routines](#scheduled-admin-routines)
- [Privacy](#privacy)

## Motivation

research-os is a single AI research assistant setup that works across every research project you run. It organizes your work and assists you through the entire empirical research process — from an initial idea to a submitted paper — while retaining context across all of your projects, not just within one conversation. It doubles as a second brain and knowledge wiki for researchers: literature, methods, datasets, and your own thinking accumulate in one place instead of evaporating at the end of each session.

Every AI conversation otherwise starts from a blank slate: you re-explain your project each time, ideas raised mid-conversation are lost, and your notes never reach your AI assistant. At the same time, research work involves a lot of repetitive scaffolding — folder structures, literature reviews, citation formatting, replication packages — that a disciplined process can largely handle for you, provided something actually enforces that process. research-os is built to solve both: a system that retains context, and a system that does not skip steps.

## The four layers

**1. A research pipeline — a declared graph, not a waterfall.** Discover a question → design the strategy → analyze the data → write the paper → get it peer-reviewed → revise → submit. Each phase has a specialist "worker" agent and, in most phases, a paired "critic" agent whose sole job is to find problems in the worker's output — critics cannot edit files, and workers cannot grade their own work. This part is built on [clo-author](https://github.com/hugosantanna/clo-author), with [ARS](https://github.com/Imbad0202/academic-research-skills)'s integrity checks incorporated (see [Acknowledgments](#acknowledgments)).

The dependency structure between phases is machine-readable (`plugins/research-os/graph/pipeline.json`) rather than implied by prose, and nothing in it stores state — a node's status (ready, blocked, done, stale) is recomputed on every call from the graph plus the filesystem plus `passport.yaml`, so it cannot silently drift from reality. `python3 plugins/research-os/scripts/graph.py next` returns the true *ready frontier* — often more than one node at once, since real work fans out and a waterfall model would hide that — and a project that already has data can enter straight at `/strategize` instead of always starting at `/discover`. `graph.py dot --mermaid` renders the current graph as a diagram on demand.

**2. A two-layer knowledge base.** `_brain/` is your personal space — profile, daily/weekly notes, project journals, your own synthesis. Alongside it sit one or more **thematic wikis** — Claude-maintained knowledge bases, one per research theme, that absorb every paper, dataset, and method you feed them and continuously rewrite themselves to stay current rather than simply accumulating notes. You read the wikis; you do not edit them directly.

The knowledge base is not a filing cabinet you consult at the start. It is read into every phase of the pipeline — the strategy step reads the wiki's page on the design you picked, the analysis step reads what is known about the dataset before writing loading code, the writing step reads the summaries and concept pages behind the paragraph being drafted — and it writes back on its own, under the constraints described in [What runs without being asked](#what-runs-without-being-asked).

**3. A learning layer.** Built on [engram](https://github.com/nagisanzenin/engram), vendored directly into this plugin: point it at anything that was unclear, and it teaches the concept properly — a first-principles breakdown, Socratic dialogue, tested recall — then schedules spaced-repetition reviews so it is retained.

**4. A personal automation layer.** Distinct from the pipeline above: this is *your own* recurring busywork, not generalizable research machinery, and it never ships as a research-os skill itself. `_brain/procedures/` holds procedures you or Claude write down; `/automate` authors (`new`), runs (`run`), inventories (`list`/`status`/`map`), and schedules (`schedule`) them. There is no promotion gate — a procedure is runnable the moment it validates, drafted either in dialogue or seeded from evidence mined out of your own past sessions (`scripts/mine_sessions.py`). Every step in a procedure is tagged `[ai]` (Claude executes it), `[human]` (stops and asks — a scheduled run hits this and correctly just stops rather than guessing), `[external]` (hands off to another named tool or skill), or `[veto]` (refuses unconditionally, no plan emitted past it). Procedures may call research-os skills; skills never call procedures — one direction only, so the two layers cannot re-merge. See `plugins/research-os/docs/13-the-automation-layer.md` for the full design history, including why an earlier version of this layer shipped a promotion gate that could never actually be reached.

## How the vault, wikis, and projects fit together

There is exactly **one vault** (`vault/` in this repo, though it can live anywhere — see [Privacy](#privacy)). It is the single top-level container for everything durable, and it holds two kinds of things:

- **`_brain/`** — your personal second brain. One per vault: profile, daily/weekly notes, freeform thoughts, project journals, and cross-theme synthesis that spans multiple wikis.
- **One or more thematic wikis** — each wiki stores the sources, summaries, concepts, methods, and datasets for a single research theme (e.g. `climate/`, `pensions/`, `innovation/`). A wiki isn't scoped to one project: it accumulates knowledge that *any* project on that theme can draw on.

Projects themselves live outside the vault, in their own folders (created by `/create-project`). Each project points to a **main wiki** — the theme its research question belongs to, recorded in `passport.yaml`'s `meta.main_wiki` and bridged via the project's `wiki-links.md`. A project reads from its main wiki (and can read others) but never edits one directly; all wiki writes go through Claude via `/wiki-ingest`, `/wiki-push`, and `/wiki-maintain`.

The relationship nests, many-to-one at each level:

```
vault (exactly one)
 ├── _brain/                     one personal space, shared by every wiki and project
 ├── wiki: climate/               ← several projects can share one wiki
 │    ├── project: "carbon-tax-incidence"
 │    └── project: "eu-ets-reform"
 ├── wiki: pensions/
 │    └── project: "pension-reform-2026"
 └── wiki: innovation/
      ├── project: "patent-citations"
      └── project: "vc-funding-cycles"
```

In short: one or more **projects** connect to a **wiki** → one or more **wikis** connect to the **vault** → there is only ever one vault, containing all wikis and, through them, all projects. Use `/add-thematic-wiki` once per research theme (not once per project — projects on the same theme should share a wiki); use `/create-project` to start a research project and assign it to an existing or new wiki.

## Two roles: research assistant and personal assistant

The skills described here serve two distinct functions within one system:

- **Research assistant** — the pipeline and the wikis. This is the part that helps you conduct the research itself: finding the literature, designing the strategy, running the analysis, writing the paper, navigating peer review, and maintaining a knowledge base that improves with every source you add.
- **Personal assistant** — the daily and weekly admin routines and the learning layer. This is the part that tracks your work: what happened today, what is planned for the week, what is due for review, and what you asked to actually learn rather than delegate outright.

You do not need to track which role is active at a given moment. Running `/checkpoint` at the end of a session, `/daily-summary` at the end of a day, `/weekly-planning` at the end of a week, and `/learn` whenever something is unclear is enough — the system routes the rest.

## Getting started

**Prerequisites:**
- **Claude Code** — install the CLI first if you haven't already, from [claude.com/claude-code](https://claude.com/claude-code), and sign in with an Anthropic/Claude account that has Claude Code access (it will prompt you to log in on first run).
- **Git** — installed and available on your `PATH` (check with `git --version`; install from [git-scm.com](https://git-scm.com) if missing). Claude Code clones this repo when you register it as a plugin marketplace source, so it needs a working `git` command.
- **No GitHub login needed** — this repo is public, so nothing beyond git itself is required to add it as a marketplace source.

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

**Adding a new thematic wiki** — `/add-thematic-wiki` registers a new theme with the two-layer knowledge system: point it at a vault or notes folder you already have to adopt it, or let it scaffold a brand-new empty one with the standard numbered layout (`00_inbox` → `90_synthesis`). Either way it adds an entry to `~/.claude/vaults.json` and a row to `_brain/wikis-index.md`, so `/create-project` and `/wiki-pull` can find it. Do this once per research theme, not once per project — projects that share a theme should share a wiki.

**Ingesting a paper** — `/wiki-ingest paper.pdf` extracts the source, writes a proper summary page, updates or creates the relevant concept, method, and dataset pages in the wiki, and links everything together. The next time this topic comes up in any project, `/wiki-pull` retrieves it automatically.

**Closing a work session** — `/checkpoint` records what happened and what comes next in that project's journal note, so the next session — yours or a future Claude's — does not start from zero. At the end of the day, `/daily-summary` rolls that up across every project touched, along with a scan of Slack and mail for anything relevant; `/weekly-planning` does the same at the end of the week, checking what actually happened against what was planned.

**Encountering something unclear** — `/learn` (no need to name the topic — point it at whatever was unclear) breaks it into a first-principles concept map, teaches it Socratically (prompting you to generate answers rather than reading them to you), and schedules a review so it is still retained a month later.

## What runs without being asked

Some of the system is not a command you type. It fires on its own, because the things it does are the things you forget to do precisely when you can least afford to.

**Hooks.** Small scripts wired to session events — start, stop, compaction, and every file write or shell command. The reason they are hooks rather than instructions is that instructions live in the conversation and get compressed away, while hooks fire regardless of what the conversation still remembers. They cover destructive-git guardrails, protection of single-writer files, write-time linting of analysis code, a warning when a file you just changed is the evidence behind a recorded claim, progressive context-budget nudges, an automatic session journal at the end of each work block, and a bounded digest of the relevant wiki injected at session start. Every one of them fails open: a bug in a hook must never block the session. The full table is in [plugins/research-os/hooks/README.md](plugins/research-os/hooks/README.md).

**A status line.** `plugins/research-os/scripts/statusline.py` puts the permission mode, model, git branch and dirty count, the project's pipeline stage, the integrity gate's state, and the context estimate into one line. Wire it via `statusLine` in `~/.claude/settings.json`. Two of those — stage and gate state — previously required running a command to find out.

**Writing into the wiki.** Claude writes durable knowledge into the thematic wiki without being asked, when it judges the material fitting and important enough. This replaces an earlier rule that required you to remember `/wiki-push`, which meant knowledge was lost on exactly the sessions where the most was learned and the least time remained. Three constraints make it safe rather than merely convenient:

- **A gate.** Every candidate goes to the `wiki-promotion-council` — five critics reviewing layer-routing, canonicity, staleness, evidence, and format in isolated forks, so the five dimensions are judged independently rather than collapsed into one impression. Five votes of five writes; four of five writes with the dissent recorded; three of five proposes and writes nothing; fewer is discarded with the reason logged. Nothing bypasses the council.
- **A blast radius.** Auto-write may append to and create pages under `30_concepts/`, `40_methods/`, `50_datasets/`, and `60_people_institutions/`, and may touch the wiki's log, its map, and the project's `wiki-links.md`. It may not write to `10_sources/` at all — sources are immutable. It may not delete or rewrite an existing claim; a contradicting finding is appended as a contradiction, because that audit trail is what the integrity gate depends on. It may not write into `_brain/`, which stays human-written, and it may not write `90_synthesis/`, because synthesis is interpretation.
- **An undo.** Every auto-write leaves a changelog line tagged `auto` with the vote tally, a dated row in the wiki's log, and its own `wiki(auto):` commit in the vault's git repo — so a week of them reads as one diff and reverts with one command. `/wiki-maintain --review-auto` lists every auto-written change for review.

To turn it off: `RESEARCH_OS_WIKI_AUTOWRITE=0`, or `autowrite: false` in `~/.claude/vaults.json`, or `--no-autowrite` for a single invocation. It is on by default. The full contract is in `plugins/research-os/rules/wiki-integration.md`.

## How claims get checked

Checking used to happen at `/peer-review` and `/submit`. That is thorough and late: a fabricated citation introduced during a literature search survives into the strategy memo, the introduction, and three days of argument built on top of it, and by the time the gate catches it the fix is structural. Checking now happens in three places.

**At the point of generation.** Skills whose output contains independently checkable claims verify them before returning. The `claim-verifier` agent runs in a forked context and never sees the draft — it receives the extracted claims, the verification questions, and pointers to sources, and nothing else. That is the whole mechanism: an agent that cannot see the draft cannot confirm it out of politeness. PASS ships as written, PARTIAL ships with the uncertainty flagged, FAIL regenerates the affected section rather than shipping a claim known to be wrong. `--no-verify` opts out.

**At review.** `/peer-review` still owns the blocking integrity gate — claim tracing, citation triangulation, the anachronism audit, figure–caption fidelity — and no agent clears its own work through it. On top of that, anything the editor raises as blocking that neither referee raised is re-checked in a fresh fork against the artifact it cites; if it does not hold up it is dropped to a note and the verdict is recomputed. A judge may always downgrade a finding, but it may only introduce one that survives that check.

**Against the numbers.** Replication verdicts are not binary. A claim comes back **PASS**, **FAIL**, **EXPLAINED** (the gap is accounted for by a concrete, named alternative specification — a defensible alternative is not a failure, but a vague note never earns this), **STALE** (its evidence file changed since the claim was recorded), or **UNMATCHED**. `claim-reconcile.py` is what sets STALE, at the moment you edit the script rather than weeks later. When a number and the manuscript disagree, the report says one of the two must change and which artifacts to isolate — never "revert the code to match the paper," which is how a genuine bug fix gets undone to make a table reproduce.

## Which model does what

Every agent pins an explicit model and effort level. None inherit from the session.

The reason is protection rather than cost. With agents inheriting, running a session on a cheaper model silently downgrades the methods referee, the verifier, and the integrity gate along with it — the parts of the system that decide whether a paper is sound get weaker because of a choice made for an unrelated reason. Pinning makes the judgment tier independent of what the session happens to be running.

The routing rule is to match the model to the cognitive demand of the task and nothing else. Identification validity, proof correctness, referee dispositions, editorial decisions, claim verification, and what enters a permanent knowledge base get the strongest tier whatever it costs, because one false PASS costs more than any routing saving. Generation and bounded review with a stronger critic downstream sit a tier below. A critic is never routed below the worker it reviews. The roster, per-agent, is in [plugins/research-os/agents/README.md](plugins/research-os/agents/README.md); the reasoning and the anti-patterns are in `plugins/research-os/rules/model-routing.md`.

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
| `/diagnose` | A result is wrong or won't run: reproduce it, shrink it, name the cause, then fix — never a guessed fix that makes the symptom disappear. |
| `/peer-review` | Simulate a journal's peer review — an editor and referees who can disagree with you. |
| `/revise` | Respond to referee comments: classify, draft the response, then audit the response letter itself. |
| `/coauthor-brief` | Write a handoff brief so a coauthor can take over part of the project — what changed, what state it's in, how to reproduce it locally. |
| `/submit` | Prepare for submission — journal targeting, replication package, environment capture, AI-use disclosure, final checks. |
| `/talk` | Turn the paper into a presentation — Beamer or a modern web deck. |
| `/dashboard` | Generate a single-page HTML overview of the project. |
| `/tools` | Project utilities: commit, compile, check the bibliography, lint, deploy, and diagnose which permission layer blocked something. |
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
| `claim-verifier` | `/discover`, `/write`, `/peer-review`, others | Checks factual claims in a forked context that never sees the draft, so it cannot confirm its own side. |
| `orchestrator` | (infrastructure) | Coordinates execution across the pipeline — determines what runs next and enforces quality gates. |
| `verifier` | (infrastructure) | Confirms everything compiles, runs, and replicates before a commit, PR, or submission, and owns the integrity gate. |

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
| `wiki-promotion-council` | `/wiki-push`, `/wiki-ingest`, `/wiki-maintain` | Five independent critics vote on whether a note may enter the wiki. The gate that licenses writing without being asked. |

### Second brain & admin

| Skill | What it's for |
|---|---|
| `/checkpoint` | End-of-session save: what happened, what's next, and what turned out to be a dead end, into the project's journal. |
| `/daily-summary` | End-of-day routine: commits the day's work, writes a summary, checks Slack/mail for anything relevant. |
| `/week` | Refresh the live week view — pull the calendar, reconcile the plan, regenerate the week page. |
| `/weekly-planning` | End-of-week routine: reviews plan against reality, sets next week's goals, proposes calendar blocks. |
| `/pending` | Clear the backlog across every project — uncommitted work, unpushed commits, unpushed wiki knowledge — grouped by project, asked once and remembered. |
| `/automate` | Author and run your own recurring procedures (`_brain/procedures/`) — no promotion gate, runnable the moment one validates. |
| `/workflow-audit` | Inventory the recurring work across your roles and score it, so the highest-leverage processes become procedures. |
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

| Agent | Dispatched by | What it does |
|---|---|---|
| `guide-writer` | writing-focused skills above | Writes documentation and guide pages in a pedagogical, tutorial voice. |

## Layout

**The plugin** (`plugins/research-os/`):

| Dir | Contents |
|---|---|
| `skills/` | All the slash commands above — see [skills/README.md](plugins/research-os/skills/README.md) for the full table. |
| `agents/` | All the worker/critic agents above, each pinned to a model and effort — see [agents/README.md](plugins/research-os/agents/README.md). |
| `hooks/` | Scripts that fire on session and tool events: guardrails, write-time linting, staleness and context nudges, the session journal, the wiki digest. See [hooks/README.md](plugins/research-os/hooks/README.md). |
| `rules/` | The governance rules agents follow — permissions, quality gates, model routing, verification, wiki conventions. See [rules/README.md](plugins/research-os/rules/README.md). |
| `graph/` | `pipeline.json` — the pipeline as a declared, executable dependency graph — plus its `schema.md`. Evaluated by `scripts/graph.py`; kept consistent with `rules/permissions.md` by `graph.py selftest`. |
| `scripts/` | The status line, the wiki map generator, the dashboard renderer, the learning engine, the automation-layer scripts (`automate_run.py`, `automate_schedule.py`, `mine_sessions.py`), the graph evaluator, the plugin's own consistency checkers, and the scheduled routines. |
| `output-styles/` | Response styles for academic writing and for refereeing, selectable via `outputStyle`. |
| `templates/` | Project, vault, and passport scaffolds, plus the [skill template](plugins/research-os/templates/skill-template.md) new skills start from. |
| `state/` | Tracks the upstream repos this is built on, so drift can be flagged. |
| `docs/`, `gold/`, `references/` | Vendored engram pedagogy docs, its grading gold-set, and reference material such as the [scheduled-agent specs](plugins/research-os/references/scheduled-agents.md) and the [authoring conventions](plugins/research-os/references/authoring-conventions.md) every Claude-facing file follows. |

**The vault** (`vault/` — see [Privacy](#privacy)):

| Dir | Contents |
|---|---|
| `_brain/` | Your personal space — profile, daily/weekly notes, thoughts, project journals, personal and cross-theme synthesis. |
| `<theme>/` (e.g. `cognitive-load/`) | One thematic wiki per research area, each with the same numbered layout: `00_inbox` → `90_synthesis`. |
| `_templates/` | Shared note templates used by every wiki and `_brain/`. |
| `index.md` | Cross-wiki catalog. |

## Keeping the plugin honest

The plugin describes itself in prose, and prose drifts from disk the moment something is added or retired. Two scripts hold the description to what is actually there:

- `plugins/research-os/scripts/check_plugin_integrity.py` — the deterministic checks. Every tool a skill's body says it invokes must be declared in its frontmatter; every documented flag must appear in the argument hint and vice versa; every internal link anchor must resolve to a real heading; a rule that claims a skill follows its protocol must find that protocol in the skill; every agent must carry an explicit model and effort. It also checks the house style from [`references/authoring-conventions.md`](plugins/research-os/references/authoring-conventions.md) — em dash over `--`, Title-Case headings, an `**Input:**` line wherever a skill takes arguments, a `Use when …` clause in every description, `SKILL.md` under 300 lines — as advisories, except an agent declaring `allowed-tools:` instead of `tools:`, which silently hands it every tool and so blocks.
- `plugins/research-os/scripts/check_surface_sync.py` — the documentation checks. Any count stated in a README must match the files on disk, and any table carrying a `<!-- surface-sync-table: ... -->` marker must have exactly one row per item on disk. Missing and extra rows are reported by name, which is the drift a count check cannot see: the total stays right while the rows say something else.

Both run on staged changes through `.githooks/pre-commit` (install with `git config core.hooksPath .githooks`) and on every pull request through `.github/workflows/gates.yml`. The escape hatch is `SKIP_INTEGRITY_GATE=1`, with the reason recorded in the commit body.

The class of bug these catch is deterministic — a field exists, an anchor resolves, a count matches — and that is exactly the class an agent misses, because it sits as one item among many in a long prompt and attention drifts. The script does not drift.

Alongside them: [`CHANGELOG.md`](CHANGELOG.md) records what shipped, [`docs/PROVENANCE.md`](docs/PROVENANCE.md) records what came from where and at which upstream commit, and [`BACKLOG.md`](BACKLOG.md) records what was deliberately deferred and why.

## Acknowledgments

- [clo-author](https://github.com/hugosantanna/clo-author) (Hugo Sant'Anna, UAB) — the base research pipeline (skills, agents, hooks, rules), ported in and adapted.
- [academic-research-skills (ARS)](https://github.com/Imbad0202/academic-research-skills) — the integrity layer merged into the ported pipeline: citation triangulation, anachronism checks, PRISMA systematic-review support, multi-style citations, AI-use disclosure.
- [claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow) (Pedro H. C. Sant'Anna, Emory) — the harness-layer patterns: enforcement in hooks rather than instructions, explicit model and effort routing, verification at the point of generation in a forked context, the promotion-council design behind wiki auto-write, and deterministic self-governance through checkers, a pre-commit gate, and CI. Nothing was copied verbatim; the patterns were re-implemented for this system. Note that Pedro H. C. Sant'Anna and Hugo Sant'Anna are different people and neither project derives from the other — see [`docs/PROVENANCE.md`](docs/PROVENANCE.md).
- [engram](https://github.com/nagisanzenin/engram) — the spaced-repetition learning engine, vendored directly rather than installed as a separate plugin: the FSRS-4.5 engine, its curriculum/assessment/artifact agents, and its pedagogy docs are copied in and adapted for this system.
- [obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain) — not integrated directly, but monitored for design ideas worth adopting: the freshness/confidence note conventions, the MOC/index approach, and the original scheduled-agent design (see below) all draw on patterns from here.

## Scheduled admin routines

Seven routines run unattended, entirely **locally** — no cloud, nothing pushed anywhere: a read-only morning brief (daily), a bounded-mutation nightly consolidation (daily; commits locally, never pushes), a read-only nightly reproducibility check against the project's recorded claims (daily), a read-only weekly vault-health audit (Fridays), a draft-only weekly review and planning pass (Fridays), a weekly literature sweep on saved topics diffed against the previous week (Mondays), and a daily pending-work sweep that reports uncommitted, unpushed, and unpushed-wiki items across every project without invoking Claude at all. Each is a small PowerShell script (`plugins/research-os/scripts/scheduled/*.ps1`) registered as a Windows Scheduled Task, calling `claude -p` with a permission allowlist scoped to exactly what that routine needs — the nightly consolidation's allowlist simply has no `git push` in it, so it is structurally incapable of pushing, not merely instructed not to. The two that wrap an existing skill (`/research-os:daily-summary`, `/research-os:weekly-planning`) pass an explicit non-interactive override, since those skills normally ask conversational questions a scheduled run has no one to answer. The detection routines report only when there is something to do — a job that says "all good" every morning trains you to stop reading it. Every run logs to `vault/_brain/scheduled-logs/<date>/` regardless — dated-folder-first and without a leading dot, so the logs are both grouped by day and actually visible in Obsidian's file explorer (a dot-prefixed folder isn't). A personal procedure can register its own schedule the same way via `/automate schedule <name>`, reusing the same wrapper machinery rather than a separate mechanism.

See [scheduled-agents.md](plugins/research-os/references/scheduled-agents.md) for the exact schedule, prompts, and design rationale. Dry-run any of them by hand before trusting the schedule, and inspect the registered tasks with `schtasks /query /tn ResearchOS-<name> /fo LIST /v`.

## Privacy

`vault/` — your notes, profile, and everything the thematic wikis have learned — is **gitignored** in this repo and lives in its own independent local git repo instead (`vault/.git`, no remote). It is never part of this repo's history, including past commits, so this repo can be shared or made public without exposing any personal research content. The scheduled routines above do not change this — they are local processes with the same filesystem access as an interactive session, not a reason to push anything anywhere.
