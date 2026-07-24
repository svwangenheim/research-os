---
name: research-os-help
description: Your research-os front door and complete guide. Reads the current project's passport.yaml and tells you exactly where you are in the pipeline and the next step (required vs optional); explains the whole system; knows every skill and agent in the plugin and what each is for; and — if you confirm — runs the next step for you. Has an ELI5 mode (`/research-os-help eli5`) that explains everything in plain language for a newcomer. Use anytime you're unsure what to do next, want the full capability list, or ask e.g. "what's next", "what can this do", "explain the whole workflow".
argument-hint: "[nothing | 'what's next' | 'explain' | 'list' / 'what can you do' | 'eli5' | a free-form question]"
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
3. **If not found:** the user isn't inside a project. Give the system overview (Mode B / the catalog) and point them to `/create-project` — or, if they're doing knowledge/learning work, route to the relevant cross-cutting skill below.

### Step 2 — Determine the next step
From `pipeline`: find `current_stage` and the first stage whose `status` isn't `passed`.
- `blocked` (gate below threshold) → **fix and re-run** that stage's critic/gate; say what failed (from `integrity.unresolved` or the stage score) and which skill fixes it.
- `in_progress` → recommend continuing it.
- `pending` with dependencies `passed` → recommend starting it.
- Mark each recommendation **required** or **optional**.

#### Canonical pipeline (stage → skill + mode)

| Stage | Skill (mode) | Gate | Notes |
|-------|-------------|------|-------|
| discovery | `/discover` (interview → spec; `lit` → literature; `data` → data; PRISMA for systematic reviews) | 80 | run `/wiki-pull` first to reuse prior knowledge |
| strategy | `/strategize` (+ `theory` for econometric-methods/theory/structural) | 80 | |
| analysis | `/analyze` | 80 | |
| writing | `/write` (detects paper type: imrad · review · theory · case_study · conference) | 80 | |
| review | `/peer-review` (`--all` comprehensive; `--peer` referees) — **integrity gate blocks here** | 90 | claims traced, citations triangulated, temporal + figure audit |
| revision | `/revise` (+ `rebuttal-audit` to QA your response letter) | 90 | |
| submission | `/submit` (`target` · `package` · `ai-disclosure` · `final`; multi-style citations) | 95 | |

#### Cross-cutting (recommend when relevant, not stage-bound)
- **Start of any work session:** `/wiki-pull` — reuse prior knowledge from the main wiki (its `_map.md` first) + `_brain/`.
- **New source found:** `/wiki-ingest <pdf>` — into the thematic wiki.
- **After a work block:** `/wiki-push` (objective knowledge down to a wiki, personal/cross-theme up into `_brain/synthesis/`) and `/checkpoint` (Orientation + journal → `_brain/projects/<slug>.md`). A Stop-hook nudges `/wiki-push` if the project bridge still lists unpushed items.
- **Spot latent cross-theme links:** `/connect [themeA] [themeB]` — read-only bridge-finder.
- **Overview anytime:** `/dashboard` (living `project_dashboard.html`).
- **Confused by a method/code Claude introduced:** `/learn`; clear due reviews with `/recall`; check retention/strategy with `/coach`.
- **End of day / week:** `/daily-summary` · `/weekly-planning`. (Also available as scheduled agents — see the catalog.)
- **First time / new machine:** `/wiki-setup` (bootstrap or repair the whole knowledge layer); `/add-vault` to register a new thematic wiki.
- **~Bimonthly:** `/check-update-upstream-repos` (diffs clo-author / ARS / engram / obsidian-second-brain against upstream).

### Step 3 — Present + optionally advance
Report concisely:
1. **You are here:** current stage + one-line status of each stage (✓ passed / ▶ in progress / ○ pending / ✗ blocked).
2. **Next step (required):** the exact command + mode, and why.
3. **Optional next steps:** e.g. `/wiki-pull`, `/learn`, `/dashboard`, `/connect`.
4. **Integrity flags:** anything in `integrity.unresolved`.

Then offer **guided auto-advance**:
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
- `/peer-review` — all quality reviews; owns the **blocking ARS integrity gate**.
- `/revise` — R&R cycle: classify referee comments, draft + audit the response letter.
- `/talk` — build + audit presentations (Beamer or Quarto RevealJS).
- `/submit` — journal targeting, replication package, AI-disclosure, final gate.
- `/tools` — utility subcommands (commit, compile, validate-bib, lint, journal, context, dashboard, deploy, learn, upgrade).
- `/checkpoint` — session handoff: passport + journal + `_brain/projects/<slug>.md` (Orientation + Journal).
- `/dashboard` — generate/refresh the living project dashboard HTML.
- `/freeze` · `/careful` — session guards (freeze edits outside dirs; block destructive bash).

**Project:**
- `/create-project` — scaffold a new numbered project (assigns a main wiki).
- `/research-os-help` — this guide.

**Knowledge (two-layer vault):**
- `/wiki-setup` — bootstrap or repair the whole knowledge layer (structure, templates, root docs, registry).
- `/add-vault` — register a new thematic wiki (numbered layout + READMEs).
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
- `/skill-stocktake` — audit skills/commands for quality.

**General-purpose:**
- `/article-writing` · `/content-engine` · `/frontend-slides` — long-form, social, and slide content.
- `/git-workflow` · `/python-patterns` · `/python-testing` · `/documentation-lookup` — engineering helpers.
- `/exa-search` · `/prompt-optimizer` · `/data-scraper-agent` · `/continuous-learning-v2` — search, prompt-tuning, scraping, instinct learning.

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
- **Knowledge** — two layers in one Obsidian root: Claude-only **thematic wikis** (`/wiki-ingest`, `/wiki-maintain`, `/connect`) and your personal **`_brain/`** second brain (`/wiki-setup`, `/add-vault`, `/wiki-pull`, `/wiki-push`). Objective facts go down to a wiki; personal/cross-theme thinking goes up into `_brain/`. Humans read the wikis but don't hand-edit them.
- **Routines** — `/daily-summary`, `/weekly-planning`, plus opt-in scheduled agents.
- **Learning** — `/learn`, `/recall`, `/coach`: **engram**'s spaced-repetition engine (FSRS-4.5, blind assessor), **vendored** directly into this plugin (not a separate install); its state lives in `_brain/learning/`.
- **Maintenance** — `/check-update-upstream-repos` tracks clo-author, ARS, the vendored engram commit, and obsidian-second-brain (watched for ideas).
- **Complementary (separate plugin, called into, not vendored):** `dz-core` — branded charts (`dz-core:create-chart`), branded PDF (`dz-core:create-paper`), Instagram tiles, onboarding.

---

## Principles

- **Passport is truth.** Never guess the stage — read `passport.yaml`.
- **One step at a time.** Recommend the single next step; advance only on explicit confirmation.
- **Required vs optional, always.** Don't bury the one thing they must do next.
- **Name the exact command + mode.** No vague "continue the analysis."
- **Match the register.** ELI5 mode uses plain words; default mode can use the domain terms.
- **The catalog can drift** — when in doubt, read the live skill/agent frontmatter to confirm.
