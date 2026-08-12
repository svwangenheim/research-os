---
name: research-os-help
description: research-os front door. Inside a project, reports the pipeline stage and exact next step; outside one, routes you to the right skill. Use for "what's next" or "what can this do". Has an ELI5 mode.
argument-hint: "[nothing | explain | list | eli5]"
allowed-tools: Read,Glob,Grep,Bash,AskUserQuestion,Skill,Task
---

# research-os Help

The front door. Orient the user and route them to the right next step — for the
paper pipeline, the knowledge base, the routines, or the learning layer. Modeled
on BMAD's `bmad-help`.

**Input:** `$ARGUMENTS` — an optional free-form question. Route on it:

| If `$ARGUMENTS`… | Go to |
|---|---|
| empty, or "what's next", "next step", "where am I" | **Mode A — Next step** (Steps 1–3) |
| "explain", "workflow", "how does this work" | **Mode B — Explain the workflow** |
| "list", "skills", "agents", "what can you do", "capabilities" | **Mode C — Full capability catalog** |
| "eli5", "simple", "explain like I'm 5", "I'm new" | **Mode D — ELI5** |
| anything else | answer using the catalog + pipeline map; fall back to Mode A |

Keep knowledge current: the catalog below is curated, but the plugin's skills and
agents are the source of truth. When listing capabilities, you may `Glob`
`${CLAUDE_PLUGIN_ROOT}/skills/*/SKILL.md` and `${CLAUDE_PLUGIN_ROOT}/agents/*.md`
and read each one's frontmatter `name` + `description` to confirm nothing has
been added or renamed since this file was written.

---

## Mode A — Next step (default)

### Step 1 — Locate state
1. Look for `passport.yaml` in the current project (cwd, or a path in `$ARGUMENTS`).
2. **If found:** read `meta`, `research`, `pipeline` (current_stage + per-stage status/score/gate), `integrity`, and `literature_corpus`. This is the source of truth for "where am I."
3. **If not found:** the user isn't inside a project folder — that's a normal, common state, not a dead end. research-os isn't limited to tracked, staged research-paper projects: it's useful for whatever the user is actually doing, project or not. Most skills work directly on a target — a file, a topic, a question — rather than requiring `passport.yaml`:
   - **Knowledge layer:** `/wiki-pull`, `/wiki-ingest`, `/wiki-push`, `/wiki-maintain`, `/connect`, `/wiki-setup`, `/add-thematic-wiki`.
   - **Learning layer:** `/learn`, `/recall`, `/coach`.
   - **Admin routines:** `/daily-summary`, `/weekly-planning`.
   - **General-purpose:** `/article-writing`, `/content-engine`, `/frontend-slides`, `/exa-search`, `/prompt-optimizer`, `/python-patterns`, `/python-testing`, `/documentation-lookup`, `/git-workflow`, `/data-scraper-agent`.
   - **Pipeline skills too, when invoked on a specific target:** most route by explicit input (a file path, a topic, a flag) rather than by pipeline stage, so a project isn't a precondition for using them one-off — e.g. `/peer-review --code path/to/script.py` or `/discover lit "some topic"`, but this pattern isn't limited to those two; check the skill's own argument-hint for what it accepts directly.

   Ask what they're actually trying to do and route straight to the matching skill — don't default to pointing at `/create-project` just because no project was found. Offer `/create-project` as the option to formalize the work into a fully tracked paper (discover → strategize → analyze → write → review → revise → submit) once that's what the user actually wants, not a gate they have to pass through first. If their intent isn't clear from the question, ask a short clarifying question before routing rather than dumping the whole catalog unprompted.

### Step 2 — Determine the next step
From `pipeline`: find `current_stage` and the first stage whose `status` isn't `passed`.
- `blocked` (gate below threshold) → **fix and re-run** that stage's critic/gate; say what failed (from `integrity.unresolved` or the stage score) and which skill fixes it.
- `in_progress` → recommend continuing it.
- `pending` with dependencies `passed` → recommend starting it.
- Mark each recommendation **required** or **optional**.

#### Canonical pipeline (stage → skill + mode)

| Stage | Skill (mode) | Gate | Notes |
|-------|-------------|------|-------|
| discovery | `/discover` (interview → spec; `lit` → literature; `data` → data; PRISMA for systematic reviews) | 80 | reads the wiki corpus before the web; claims post-flight verified |
| strategy | `/strategize` (+ `theory` for econometric-methods/theory/structural) | 80 | reads `<main_wiki>/40_methods/` for the chosen design |
| analysis | `/analyze` | 80 | reads `<main_wiki>/50_datasets/` before writing loading code |
| writing | `/write` (detects paper type: imrad · review · theory · case_study · conference) | 80 | reads `20_summaries/` + `30_concepts/` for content, never for voice |
| review | `/peer-review` (`--all` comprehensive; `--peer` referees) — **integrity gate blocks here** | 90 | claims traced, citations triangulated, temporal + figure audit; the editor's verdict passes a hallucination gate |
| revision | `/revise` (+ `rebuttal-audit` to QA your response letter) | 90 | |
| submission | `/submit` (`target` · `package` · `environment` · `ai-disclosure` · `final`) | 95 | `environment` pins lockfiles, seeds and RNG kind |

#### Blocking conditions to check before recommending anything

Three things can stop a stage regardless of its score. Name whichever applies instead of recommending the next stage:

1. **`integrity.unresolved` is non-empty** — the ARS gate failed. `/peer-review` will not dispatch the editor and `/submit` will not run. Say which check failed.
2. **A claim is STALE.** The `claim-reconcile` hook flags this in-session when an analysis script changes under a recorded claim. `/peer-review --replicate` re-verifies; `/diagnose` localizes which step drifted.
3. **A post-flight FAIL was surfaced but not resolved** — a citation or number the forked verifier contradicted.

#### Cross-cutting (recommend when relevant, not stage-bound)
- **Start of any work session:** the SessionStart hook already injects a short wiki digest — stage-relevant concepts, methods or datasets, plus any unpushed items. Run `/wiki-pull` for the full read when the digest is not enough.
- **New source found:** `/wiki-ingest <pdf>` — into the thematic wiki.
- **A wrong or failing number:** `/diagnose` — reproduce, minimise, hypothesise, instrument, fix. Never edits before it can reproduce, never fixes before it can explain.
- **Handing work to someone else:** `/coauthor-brief` (what a collaborator needs to take over) — distinct from `/checkpoint` (what *you* need to resume).
- **After a work block:** `/wiki-push` (objective knowledge down to a wiki, personal/cross-theme up into `_brain/synthesis/`) and `/checkpoint` (Orientation + journal → `_brain/projects/<slug>.md`). Claude also writes council-approved durable knowledge into the wiki on its own — `/wiki-maintain --review-auto` shows what it wrote, and `RESEARCH_OS_WIKI_AUTOWRITE=0` turns it off.
- **Spot latent cross-theme links:** `/connect [themeA] [themeB]` — read-only bridge-finder.
- **Overview anytime:** `/dashboard` (living `project_dashboard.html`).
- **Confused by a method/code Claude introduced:** `/learn`; clear due reviews with `/recall`; check retention/strategy with `/coach`.
- **End of day / week:** `/daily-summary` · `/weekly-planning`. (Also available as scheduled agents — see the catalog.)
- **First time / new machine:** `/wiki-setup` (bootstrap or repair the whole knowledge layer); `/add-thematic-wiki` to register a new thematic wiki.
- **~Bimonthly:** `/check-update-upstream-repos` (diffs clo-author / ARS / engram / obsidian-second-brain against upstream).

### Step 3 — Present + optionally advance

**If a project was found (Step 1.2),** report concisely:
1. **You are here:** current stage + one-line status of each stage (✓ passed / ▶ in progress / ○ pending / ✗ blocked).
2. **Next step (required):** the exact command + mode, and why.
3. **Optional next steps:** e.g. `/wiki-pull`, `/learn`, `/dashboard`, `/connect`.
4. **Integrity flags:** anything in `integrity.unresolved`.

**If no project was found (Step 1.3),** skip the stage report entirely — there's no pipeline state to summarize. Instead name the one skill (or short sequence) that matches what the user asked for, and why it's the right fit standalone.

Either way, then offer **guided auto-advance**:
> Want me to run **`<next command>`** now? (yes / no — I'll wait)

- On **yes**: invoke the recommended skill (via the Skill tool); let it run its normal flow.
- On **no**: stop; the user drives. Never auto-run without a yes.

---

## Mode B — Explain the workflow

Give the full pipeline map (the Step 2 table + cross-cutting list) and, if a
passport exists, where they currently sit — without auto-advancing. Explain the
two-layer knowledge model (below) and how the pipeline, wikis, `_brain/`, and
learning layer fit together.

---

## Mode C — Full capability catalog

Present the grouped catalog below. If asked for "everything" or an exact count,
also enumerate live from `${CLAUDE_PLUGIN_ROOT}/skills/*/SKILL.md` +
`agents/*.md` frontmatter so nothing is missed.

### Skills — by group

**Pipeline (paper lifecycle):**
- `/discover` — research question, literature (narrative or PRISMA), data discovery, ideation → writes the spec into `passport.yaml`.
- `/strategize` — identification strategy / pre-analysis plan / formal theory section.
- `/analyze` — end-to-end data analysis (R/Python/Julia); scripts + outputs.
- `/write` — draft/revise sections by paragraph-level argument moves; strips AI patterns.
- `/peer-review` — all quality reviews; owns the **blocking ARS integrity gate**. The editor's verdict passes a hallucination gate before it is saved.
- `/diagnose` — root-cause a wrong or failing number: reproduce → minimise → hypothesise → instrument → fix. Single-symptom; `--no-fix` to localize without editing.
- `/revise` — R&R cycle: classify referee comments, draft + audit the response letter.
- `/talk` — build + audit presentations (Beamer or Quarto RevealJS).
- `/submit` — journal targeting, replication package, environment capture, AI-disclosure, final gate.
- `/tools` — utility subcommands (commit, compile, validate-bib, lint, journal, context, dashboard, deploy, learn, upgrade, permission-check).
- `/checkpoint` — session handoff for *you* resuming: passport + journal + `_brain/projects/<slug>.md`, plus a "discarded as noise" section so dead ends are not quoted back later.
- `/coauthor-brief` — handoff for *someone else* starting: what changed, where each artifact stands, how to reproduce, how to get data access.
- `/dashboard` — generate/refresh the living project dashboard HTML.
- `/freeze` · `/careful` — session guards (freeze edits outside dirs; block destructive bash).

**Project:**
- `/create-project` — scaffold a new numbered project (assigns a main wiki).
- `/research-os-help` — this guide.

**Knowledge (two-layer vault):**
- `/wiki-setup` — bootstrap or repair the whole knowledge layer (structure, templates, root docs, registry).
- `/add-thematic-wiki` — register a new thematic wiki (numbered layout + READMEs).
- `/wiki-pull` — retrieve prior knowledge before work (reads each wiki's `_map.md` first).
- `/wiki-push` — write durable knowledge back (down to a wiki, up into `_brain/synthesis/`).
- `/wiki-ingest` — ingest a source (PDF/markdown/Office/citation) into a thematic wiki.
- `/wiki-maintain` — audit + remediate wikis to A-tier; regenerates the `_map.md` MOCs; reports `_brain/` health (read-only).
- `/connect` — read-only cross-theme bridge-finder (structural analogy / transfer / collision).

**Routines:**
- `/daily-summary` — end-of-day: commit per project, log to `_brain/daily/`.
- `/weekly-planning` — end-of-week: check off last week, set this week's goals + calendar + "questions for next week".

**Learning (vendored engram):**
- `/learn` — first-principles curriculum + Socratic tutoring + verified recall (FSRS-scheduled); context-sourced intake.
- `/recall` — clear due spaced-repetition reviews (engram's review loop).
- `/coach` — learning telemetry, strategy, calibration, dashboard.

**Maintenance:**
- `/check-update-upstream-repos` — diff tracked upstreams (clo-author, ARS, engram, obsidian-second-brain) against live HEAD.

**General-purpose:**
- `/article-writing` · `/content-engine` · `/frontend-slides` — long-form, social, and slide content.
- `/git-workflow` · `/python-patterns` · `/python-testing` · `/documentation-lookup` — engineering helpers.
- `/exa-search` · `/prompt-optimizer` · `/data-scraper-agent` — search, prompt-tuning, scraping.

### Scheduled agents (opt-in, set up via `/schedule`)
Specs live in `${CLAUDE_PLUGIN_ROOT}/references/scheduled-agents.md`:
- **09:00 morning brief** (read-only) · **22:00 nightly consolidation** (commit + daily note, flags push candidates) · **Fri 16:30 weekly review + planning** (draft) · **Fri 15:00 weekly vault-health audit** (read-only).

### Agents — dispatched by the skills (not called directly)
Most run automatically inside a skill; each worker is paired with a critic (separation of powers).
- **Discovery/lit/data:** `explorer` + `explorer-critic`, `librarian` + `librarian-critic`.
- **Strategy/theory:** `strategist` + `strategist-critic`, `theorist` + `theorist-critic`.
- **Analysis:** `coder` + `coder-critic`, `data-engineer` (paired with `coder-critic`).
- **Writing/talks:** `writer` + `writer-critic`, `storyteller` + `storyteller-critic`.
- **Review:** `methods-referee`, `domain-referee`, `editor`, `verifier` (owns the ARS integrity gate).
- **Infrastructure:** `orchestrator` (phase transitions, dispatch, gates).
- **Knowledge:** `wiki-librarian` (two-layer retrieval + wiki maintenance).
- **Code/docs:** `code-reviewer`, `python-reviewer`, `guide-writer`.
- **Learning (engram):** `engram-curriculum-architect`, `engram-assessor` (blind grader), `engram-artifact-smith`.

---

## Mode D — ELI5

Explain in plain, jargon-free language. Adapt to what they ask, but the shape is:

**What this is.** research-os is a set of tools that turn Claude into a research
assistant with a memory. It does two big things: (1) helps you take a paper from
an idea all the way to submission, and (2) remembers what you learn so you never
start from scratch.

**The two "brains".** Your knowledge lives in an Obsidian folder with two parts:
- **The wikis** — tidy reference shelves Claude keeps for you (one shelf per topic).
  Claude writes these; you read them. Facts about the world go here.
- **`_brain/`** — your own notebook: daily notes, weekly plans, project journals,
  stray thoughts, lessons learned. This is yours; Claude only helps you keep it.

**The shelves now come to you.** You used to have to ask ("`/wiki-pull`") before
Claude would look at what you already knew. Now every session starts by showing a
short summary of the relevant shelf — the methods when you're planning, the
datasets when you're coding, the synthesis when you're writing. You can still ask
for the full read; you just don't have to remember to.

**Claude files things away by itself now.** When something worth keeping comes out
of a session, Claude adds it to the right shelf without asking. Before anything is
filed, five separate checkers look at it independently — does this belong on a
shelf or in your notebook? does a page for it already exist? does it contradict
what's there? is it actually sourced? is it formatted right? Four of five have to
say yes.

There are hard limits on this. Claude never edits your notebook, never touches the
original PDFs, and never deletes or rewrites something that's already there — if a
new finding disagrees with an old one, both stay and the disagreement is written
down. Everything filed automatically is logged and saved as a separate checkpoint,
so `/wiki-maintain --review-auto` shows you exactly what it did, and one command
undoes a whole week of it. If you'd rather it went back to asking first, set
`RESEARCH_OS_WIKI_AUTOWRITE=0`.

**Claude checks its own facts before showing you.** When it writes something with
citations or numbers in it, a second Claude — one that has never seen the draft —
checks each claim against the actual sources. It can't just agree with itself,
because it doesn't know what the first one wrote. Fabricated citations are the
most common way this kind of work goes wrong, and they're much cheaper to catch
the moment they appear than three days later.

**The pipeline, in one line.** Have an idea → `/create-project`, then walk the
steps: **discover** (what's known + what data exists) → **strategize** (the plan)
→ **analyze** (crunch the data) → **write** → **peer-review** (a strict quality
check) → **revise** → **submit**. At each step Claude does the work and a second
"critic" double-checks it. Stuck on which step? Just run `/research-os-help`.

**A simple "what do I run?" guide:**
- "I found a paper I want to keep" → `/wiki-ingest <the pdf>`
- "I'm starting work — what do I already know about this?" → `/wiki-pull`
- "I did some work, save it" → `/checkpoint` (and `/wiki-push` for reusable facts)
- "I don't understand this thing Claude just did" → `/learn`
- "What should I do next?" → `/research-os-help` (this)
- "Show me the big picture of my project" → `/dashboard`
- "Wrap up my day / plan my week" → `/daily-summary` / `/weekly-planning`

**The golden rule.** Nothing important is written automatically without asking
you first, and Claude never edits your `_brain/` notebook behind your back.

End by asking if they want to try one of these now.

---

## System overview (shared by Modes B/C/D)

research-os layers:
- **Projects** — `/create-project` scaffolds a numbered project; the pipeline turns it into a paper.
- **Knowledge** — two layers in one Obsidian root: Claude-only **thematic wikis** (`/wiki-ingest`, `/wiki-maintain`, `/connect`) and your personal **`_brain/`** second brain (`/wiki-setup`, `/add-thematic-wiki`, `/wiki-pull`, `/wiki-push`). Objective facts go down to a wiki; personal/cross-theme thinking goes up into `_brain/`. Humans read the wikis but don't hand-edit them.
- **Routines** — `/daily-summary`, `/weekly-planning`, plus opt-in scheduled agents.
- **Learning** — `/learn`, `/recall`, `/coach`: **engram**'s spaced-repetition engine (FSRS-4.5, blind assessor), **vendored** directly into this plugin (not a separate install); its state lives in `_brain/learning/`.
- **Maintenance** — `/check-update-upstream-repos` tracks clo-author, ARS, the vendored engram commit, and obsidian-second-brain (watched for ideas).
- **Complementary (separate plugin, called into, not vendored):** `dz-core` — branded charts (`dz-core:create-chart`), branded PDF (`dz-core:create-paper`), Instagram tiles, onboarding.

---

## Principles

- **Passport is truth, when one exists.** Never guess the stage — read `passport.yaml`. No passport is not an error state — it just means route by intent instead of by pipeline stage.
- **One step at a time.** Recommend the single next step; advance only on explicit confirmation.
- **Required vs optional, always.** Don't bury the one thing they must do next.
- **Name the exact command + mode.** No vague "continue the analysis."
- **Match the register.** ELI5 mode uses plain words; default mode can use the domain terms.
- **The catalog can drift** — when in doubt, read the live skill/agent frontmatter to confirm.
