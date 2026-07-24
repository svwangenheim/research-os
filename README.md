# research-os

**A personal AI research assistant that remembers things.** It helps run an
actual research project end to end — from "I have an idea" to a submitted
paper — while also keeping a growing, organized set of notes about your
research field and about you, so every new conversation picks up where the
last one left off instead of starting from zero. It can also teach you
things properly and hold you to a daily/weekly routine.

This repo is a [Claude Code](https://claude.com/claude-code) plugin
(`plugins/research-os/`) plus the personal Obsidian vault it maintains
(`vault/`, kept out of this public repo — see [Privacy](#privacy) below).

## The problem, in one breath

Every AI chat starts from nothing: you re-explain your project every time,
good ideas said mid-conversation just evaporate, and your Obsidian notes
never talk to your AI at all. Meanwhile, real research has a lot of
repetitive scaffolding — folder structures, literature reviews, citation
formatting, replication packages — that a careful process can mostly do for
you, if something actually holds you to the process. research-os is an
attempt to fix both: a system that remembers, and a system that doesn't skip
steps.

## The three layers

**1. A research pipeline.** Discover a question → design the strategy →
analyze the data → write the paper → get it peer-reviewed → revise → submit.
Each phase has a specialist "worker" agent and, in most phases, a paired
"critic" agent whose entire job is to find problems in the worker's output —
critics can't edit files, and workers can't grade their own work. This part
is built on [clo-author](https://github.com/hugosantanna/clo-author) with
[ARS](https://github.com/Imbad0202/academic-research-skills)'s integrity
checks folded in (see [Built on the shoulders of](#built-on-the-shoulders-of)).

**2. A two-layer knowledge base.** `_brain/` is *your* space — profile,
daily/weekly notes, project journals, your own synthesis. Alongside it sit
one or more **thematic wikis** — Claude-maintained knowledge bases, one per
research theme, that absorb every paper/dataset/method you feed them and
keep rewriting themselves to stay current rather than just piling up notes.
You read the wikis; you don't hand-edit them.

**3. A learning layer.** Built on
[engram](https://github.com/nagisanzenin/engram), vendored directly into
this plugin: point it at anything that confused you, and it teaches it to
you properly — a first-principles breakdown, Socratic back-and-forth, tested
recall — then schedules spaced-repetition reviews so it actually sticks.

## Two hats: research assistant, personal assistant

Split the skills above into what they're actually doing for you, and it's
two separate jobs wearing one system:

- **Research assistant** — the pipeline and the wikis. This is the part
  that helps you *do the research*: find the literature, design the
  strategy, run the analysis, write the paper, survive peer review, and keep
  a knowledge base that gets smarter every time you feed it a source.
- **Personal assistant** — the daily/weekly admin routines and the learning
  layer. This is the part that runs *you*: what happened today, what's
  planned for the week, what's due for review, what you asked to actually
  learn instead of just having Claude do it for you.

Neither needs you to remember which hat is on. You just run `/checkpoint`
at the end of a session, `/daily-summary` at the end of a day,
`/weekly-planning` at the end of a week, and `/learn` whenever something
confuses you — the system routes the rest.

## What happens when you...

**...start a new project** — `/create-project "does X affect Y"` → Claude
runs a short interview, picks (or asks about) which thematic wiki this
belongs to, and scaffolds the whole folder tree, a project config, and a
starter dashboard. Nothing is guessed silently; every step is confirmed.

**...find an interesting paper** — `/wiki-ingest paper.pdf` → Claude extracts
it, writes a proper summary page, updates or creates the relevant concept /
method / dataset pages in the wiki, and links everything together. The next
time this topic comes up in any project, `/wiki-pull` finds it automatically.

**...finish a work session** — `/checkpoint` → Claude writes down what
happened and what's next into that project's journal note, so the next
session (yours or a future Claude's) doesn't start blind. At the end of the
day, `/daily-summary` rolls that up across every project you touched, plus a
scan of Slack/mail for anything relevant — and `/weekly-planning` does the
same at the end of the week, checking what actually happened against what
was planned.

**...get confused by something** — `/learn` (no need to name the topic —
point it at whatever just confused you) → Claude breaks it into a
first-principles concept map, teaches it Socratically (asking you to
generate answers, not just reading them to you), and schedules a review so
it's still there in a month.

## Skills vs. agents, in one paragraph

A **skill** is something *you* invoke — a slash command like `/checkpoint`,
a recipe Claude follows step by step. An **agent** is a specialized *worker*
that a skill dispatches to do one bounded piece of work and report back
(e.g. `/analyze` dispatches the `coder` agent to write analysis code, and
the `coder-critic` agent to check it). You'll use skills constantly; you'll
almost never invoke an agent by name yourself — they work behind the scenes.

## Every skill and agent

Grouped by what they're for. One line each, plain language — see each
skill's own file for the full technical description.

### Research workflow (the academic pipeline)

| Skill | What it's for |
|---|---|
| `/create-project` | Scaffold a brand-new research project — folders, config, dashboard. |
| `/discover` | Kick off a project: literature search, data search, brainstorming, or a guided interview to land on a research question. |
| `/strategize` | Design the empirical strategy — identification approach, pre-analysis plan, or formal theory. |
| `/analyze` | Turn the strategy into real code and results (R, Python, or Julia). |
| `/write` | Draft the paper itself, section by section, in a real academic voice. |
| `/peer-review` | Simulate a real journal's peer review — an editor and referees who can disagree with you. |
| `/revise` | Respond to referee comments: classify, draft the response, then audit the response letter itself. |
| `/submit` | Get ready to actually submit — journal targeting, replication package, AI-use disclosure, final checks. |
| `/talk` | Turn the paper into a presentation — Beamer or a modern web deck. |
| `/dashboard` | Generate a single-page HTML overview of the whole project. |
| `/tools` | Grab-bag of utilities: commit, compile, check the bibliography, deploy. |
| `/freeze` | Lock a set of folders from accidental edits while you focus elsewhere. |
| `/careful` | Block dangerous shell commands (`rm -rf`, force-push, ...) for the rest of the session. |

Agents dispatched by the above (you don't call these directly):

| Agent(s) | Dispatched by | What they do |
|---|---|---|
| `librarian` / `librarian-critic` | `/discover` | Find related papers and build a lit review; the critic checks for coverage gaps. |
| `explorer` / `explorer-critic` | `/discover` | Find and evaluate datasets; the critic checks measurement validity and identification fit. |
| `strategist` / `strategist-critic` | `/strategize` | Design the empirical strategy; the critic is the gatekeeper who has to sign off. |
| `theorist` / `theorist-critic` | `/strategize` | Write formal theory and proofs; the critic checks logical validity. |
| `coder` / `data-engineer` / `coder-critic` | `/analyze` | Write the analysis code and cleaning scripts; the critic reviews both. |
| `writer` / `writer-critic` | `/write` | Draft paper sections; the critic checks the draft against the evidence. |
| `storyteller` / `storyteller-critic` | `/talk` | Build the presentation; the critic checks narrative flow and whether it compiles. |
| `domain-referee` / `methods-referee` / `editor` | `/peer-review` | Referee the field-substance and the methods separately; the editor makes the final call. |
| `orchestrator` | (infrastructure) | The traffic controller behind the whole pipeline — decides what runs next, enforces quality gates. |
| `verifier` | (infrastructure) | Checks everything actually compiles/runs/replicates before a commit, PR, or submission. |

### Wiki & knowledge

| Skill | What it's for |
|---|---|
| `/wiki-setup` | Set up or repair the whole two-layer knowledge system — the first thing you run on a new machine. |
| `/add-vault` | Register a new thematic wiki — adopt one you already have, or start a brand-new empty one. |
| `/wiki-ingest` | Feed in a source (PDF, doc, citation) and have it properly filed — summary, linked concept/method/dataset pages. |
| `/wiki-pull` | At the start of work, pull in what's already known about this topic. |
| `/wiki-push` | At the end of work, push new knowledge back into the wikis and your personal brain. |
| `/wiki-maintain` | Health-check and clean up a wiki — dedupe, fix broken links, tidy summaries. |
| `/connect` | Ask "what connects these two themes?" and get non-obvious links surfaced (read-only, never writes). |

| Agent | Dispatched by | What it does |
|---|---|---|
| `wiki-librarian` | all of the above | Knows the two-layer knowledge model's standards inside out and enforces them behind the scenes. |

### Second brain & admin

| Skill | What it's for |
|---|---|
| `/checkpoint` | End-of-session save: what happened, what's next, into the project's journal. |
| `/daily-summary` | End-of-day routine: commits today's work, writes a summary, checks Slack/mail for anything relevant. |
| `/weekly-planning` | End-of-week routine: reviews the plan vs. reality, sets next week's goals, proposes calendar blocks. |
| `/check-update-upstream-repos` | Checks whether the open-source projects this system is built on have moved since we last looked. |
| `/research-os-help` | The front door — "what's next", "what can this do", or a full ELI5 walkthrough of the whole system. |

No dedicated agents in this group — these work directly, without dispatching a named worker.

### Learning (engram)

| Skill | What it's for |
|---|---|
| `/learn` | Actually learn something properly — first-principles teaching, Socratic dialogue, tested recall. |
| `/recall` | Your two-minute daily habit: clear whatever's due for spaced-repetition review. |
| `/coach` | How's your learning going — retention stats, a dashboard, tuning how the tutor teaches you. |

| Agent | Dispatched by | What it does |
|---|---|---|
| `engram-curriculum-architect` | `/learn` | Breaks a topic into a first-principles concept map before teaching starts. |
| `engram-assessor` | `/learn`, `/coach` | Grades what you produced — deliberately blind to the conversation so it can't be swayed. |
| `engram-artifact-smith` | `/learn` | Builds an interactive HTML explainer for a concept that keeps tripping you up. |

### Coding

| Skill | What it's for |
|---|---|
| `/python-patterns` | Pythonic idioms and best practices, on tap while you code. |
| `/python-testing` | pytest/TDD guidance while you write tests. |
| `/documentation-lookup` | Pull real, current library docs instead of guessing from training data. |
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
| `/exa-search` | Neural web/code/company search. |
| `/prompt-optimizer` | Feed it a rough prompt, get back a sharper one — never runs the task itself. |
| `/frontend-slides` | Build an animated HTML presentation, or convert a PowerPoint into one. |
| `/data-scraper-agent` | Stand up a free, scheduled scraper for any public data source. |
| `/continuous-learning-v2` | Claude observes its own sessions and slowly builds up small learned preferences over time. |
| `/skill-stocktake` | Audit all the skills/commands in this plugin for quality. |

| Agent | Dispatched by | What it does |
|---|---|---|
| `guide-writer` | writing-focused skills above | Writes documentation/guide pages in a pedagogical, tutorial voice. |

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
| `docs/`, `gold/`, `references/` | Vendored engram pedagogy docs, its grading gold-set, and reference material like the [testing guide](plugins/research-os/references/testing-guide.md) and [scheduled-agent specs](plugins/research-os/references/scheduled-agents.md). |

**The vault** (`vault/` — see [Privacy](#privacy)):

| Dir | Contents |
|---|---|
| `_brain/` | Your space — profile, daily/weekly notes, thoughts, project journals, personal + cross-theme synthesis. |
| `<theme>/` (e.g. `cognitive-load/`) | One thematic wiki per research area, each with the same numbered layout: `00_inbox` → `90_synthesis`. |
| `_templates/` | Shared note templates used by every wiki and `_brain/`. |
| `index.md` | Cross-wiki catalog. |

## Getting started

Four steps, in order — the first two aren't optional, the rest is up to you.

**1. Install** the plugin (not just source in this repo — a real install):
```
claude plugin marketplace add <path-to-this-repo>
claude plugin install research-os@research-os
```

**2. Set up the knowledge base — `/wiki-setup`.** Run this before anything
else; every other capability assumes it exists. It's conversational: it
asks whether you already have a wiki/vault somewhere (point it there) or
you're starting fresh (it builds everything — folder structure, Obsidian
config, the registry — in one pass), then runs a short profile interview.
You'll come out the other side with a real `_brain/profile.md` and, if you
gave it one, at least one registered thematic wiki.

**3. Get oriented — `/research-os-help`.** Never used this before? Run
`/research-os-help eli5` for a plain-language walkthrough of the whole
system. Already in a project and just not sure what's next? Plain
`/research-os-help` reads that project's state and tells you exactly where
you are and what to do next. Come back to this command any time you're
unsure — it's the front door, not a one-time onboarding step.

**4. Do something.** Pick whichever matches what's actually in front of you:
- Have a research question? → `/create-project "does X affect Y"`
- Have a paper or dataset you want preserved? → `/wiki-ingest paper.pdf`
- Something just confused you (a method, a piece of code, anything)? → `/learn`
- Just want to see everything that exists? → the tables further down, or
  `/research-os-help list`

From here, the [testing guide](plugins/research-os/references/testing-guide.md)
walks through every capability area with a concrete "what should now exist"
check, and is the fastest way to actually learn the system by doing rather
than reading. For the plugin's technical internals (directory-by-directory
component inventory, token-cost notes, vendoring details), see
[plugins/research-os/README.md](plugins/research-os/README.md).

## Built on the shoulders of

- [clo-author](https://github.com/hugosantanna/clo-author) — the base
  research pipeline (skills, agents, hooks, rules), ported in and adapted.
- [academic-research-skills (ARS)](https://github.com/Imbad0202/academic-research-skills) —
  the integrity layer merged into the ported pipeline: citation
  triangulation, anachronism checks, PRISMA systematic-review support,
  multi-style citations, AI-use disclosure.
- [engram](https://github.com/nagisanzenin/engram) — the spaced-repetition
  learning engine, vendored directly (not installed as a separate plugin) —
  the FSRS-4.5 engine, its curriculum/assessment/artifact agents, and its
  pedagogy docs are copied in and adapted for this system.
- [obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain) —
  not integrated, just watched for ideas worth porting: the freshness/
  confidence note conventions, the MOC/index approach, and the four
  scheduled-agent design (see below) all drew on patterns from here.

## Scheduled admin routines

Four routines are specced (cron schedule + exact prompt) in
[scheduled-agents.md](plugins/research-os/references/scheduled-agents.md).
Only two can actually run unattended in the cloud — `/schedule` spawns an
isolated cloud sandbox that only sees a cloned GitHub repo, not your local
machine:

- **Morning brief** and **weekly vault-health audit** — both read-only, both
  registered as cloud routines via `/schedule` against a private GitHub
  repo the vault is pushed to for this purpose.
- **Nightly consolidation** and **weekly review + planning** — stay
  manual/local: the former commits directly in local project repos (and is
  guardrailed to never push, which only a local execution model can honor
  faithfully), the latter reads per-project state a cloud clone of the
  vault alone can't see. Run these by hand, or wire them up via `/loop` on a
  machine that stays on.

See `scheduled-agents.md` for the exact crons/prompts and why the split
exists, and the
[testing guide](plugins/research-os/references/testing-guide.md) for how to
dry-run each one manually before trusting any schedule.

## Privacy

`vault/` — your notes, profile, and everything the thematic wikis have
learned — is **gitignored** in this repo and lives in its own independent
git repo instead (`vault/.git`). It is never part of *this* repo's history,
including past commits, so this repo can be shared or made public without
exposing any personal research content. The vault repo itself has no remote
by default; a **private** (never public) GitHub remote is only added if you
want the two cloud routines above, which need somewhere to clone from.
