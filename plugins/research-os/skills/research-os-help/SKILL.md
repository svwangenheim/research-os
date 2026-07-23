---
name: research-os-help
description: Your research-os workflow guide. Reads the current project's passport.yaml, tells you exactly where you are in the pipeline and the next step to take (required vs optional), explains the full workflow from any point, and — if you confirm — runs the next step for you (guided auto-advance). Use anytime you're unsure what to do next, or ask e.g. "I finished the analysis, what now?".
argument-hint: "[optional question, e.g. 'what's next' or 'explain the whole workflow']"
allowed-tools: Read,Glob,Grep,Bash,AskUserQuestion,Skill,Task
---

# research-os Help

The front door. Orient the user in the research-os workflow and route them to the right next step. Modeled on BMAD's `bmad-help`.

**Input:** `$ARGUMENTS` — an optional free-form question. If absent, default to "what's my next step?".

---

## Step 1 — Locate state

1. Look for `passport.yaml` in the current project (cwd, or the path in `$ARGUMENTS`).
2. **If found:** read `meta`, `research`, `pipeline` (current_stage + per-stage status/score/gate), `integrity`, and `literature_corpus`. This is the source of truth for "where am I."
3. **If not found:** the user isn't inside a project. Give the system overview (Step 4) and point them to `/create-project`.

## Step 2 — Determine the next step

From `pipeline`:
- Find `current_stage` and the first stage whose `status` is not `passed`.
- If a stage is `blocked` (gate score below threshold), the next step is to **fix and re-run** that stage's critic/gate — say what failed (from `integrity.unresolved` or the stage score) and which skill fixes it.
- If a stage is `in_progress`, recommend continuing it.
- If a stage is `pending` and its dependencies are `passed`, recommend starting it.
- Mark each recommendation **required** or **optional**.

### Canonical pipeline (stage → skill + mode)

| Stage | Skill (mode) | Gate | Notes |
|-------|-------------|------|-------|
| discovery | `/discover` (interview → spec; `lit` → literature; `data` → data; `lit` PRISMA for systematic reviews) | 80 | run `/wiki-pull` first to reuse prior knowledge |
| strategy | `/strategize` (+ `theory` if econometric-methods/theory/structural) | 80 | |
| analysis | `/analyze` | 80 | |
| writing | `/write` (detects paper type: imrad · review · theory · case_study · conference) | 80 | |
| review | `/peer-review` (`--all` comprehensive; `--peer` referees) — **integrity gate blocks here** | 90 | claims traced, citations triangulated, temporal + figure audit |
| revision | `/revise` (+ `rebuttal-audit` to QA your response letter) | 90 | |
| submission | `/submit` (`target` · `package` · `ai-disclosure` · `final`; multi-style citations) | 95 | |

### Cross-cutting (recommend when relevant, not stage-bound)
- **Before any work session:** `/wiki-pull` (reuse prior knowledge from the main wiki + `_brain`).
- **New source found:** `/wiki-ingest <pdf>` (into the thematic wiki).
- **After a work block:** `/wiki-push` (synthesize up into `_brain`) and `/checkpoint` (journal → `_brain/projects/<slug>.md`).
- **Overview anytime:** `/dashboard` (living `project_dashboard.html`).
- **Didn't understand a method/code Claude introduced:** `/learn` (engram's teaching loop, vendored, with research-os's context-sourced intake + wiki/project linkage woven in); review due items with `/recall` (engram's review loop, vendored, renamed to avoid confusion with `/peer-review`); check retention/strategy with `/coach` (engram's telemetry/dashboard loop, vendored).
- **Utilities/guards:** `/tools`, `/freeze`, `/careful`.
- **End of day:** `/daily-summary` (commits work per project, logs to `_brain/daily/`).
- **End of week:** `/weekly-planning` (checks off last week, sets this week's goals + calendar).
- **~Bimonthly:** `/check-update-upstream-repos` (diffs clo-author/ARS/engram against upstream).
- **First time / new machine:** `/wiki-setup` (bootstraps or repairs the whole knowledge layer);
  `/add-vault` to register a new thematic wiki.

## Step 3 — Present + optionally advance

Report concisely:
1. **You are here:** current stage + one-line status of each stage (✓ passed / ▶ in progress / ○ pending / ✗ blocked).
2. **Next step (required):** the exact command + mode, and why.
3. **Optional next steps:** e.g. `/wiki-pull`, `/learn`, `/dashboard`.
4. **Integrity flags:** anything in `integrity.unresolved`.

Then offer **guided auto-advance**:
> Want me to run **`<next command>`** now? (yes / no — I'll wait)

- On **yes**: invoke the recommended skill (via the Skill tool) and let it run its normal interactive flow.
- On **no**: stop; the user drives. (Default is user-driven — never auto-run without a yes.)

If `$ARGUMENTS` asks to "explain the workflow" or similar, give the full pipeline map (Step 2 table + cross-cutting) and where they currently sit, without auto-advancing.

## Step 4 — System overview (when no passport / on request)

research-os layers:
- **Projects** — `/create-project` scaffolds a numbered project; the pipeline above turns it into a paper.
- **Knowledge** — two layers in one Obsidian root: Claude-only **thematic wikis** (`/wiki-ingest`, `/wiki-maintain`) and your personal **`_brain/`** second brain (`/wiki-setup`, `/add-vault`, `/wiki-pull`, `/wiki-push`).
- **Routines** — `/daily-summary`, `/weekly-planning`.
- **Learning** — `/learn`, `/recall`, `/coach`: **engram**'s spaced-repetition engine (FSRS-4.5, blind assessor), vendored directly into this plugin (not a separate install) — `/learn` weaves research-os's context-sourced intake and wiki/project-journal linkage into engram's real teaching loop; `/recall` is engram's review loop (renamed to avoid colliding with `/peer-review`); `/coach` is engram's telemetry/strategy/dashboard loop.
- **Maintenance** — `/check-update-upstream-repos` (tracks clo-author, ARS, **and** the vendored engram commit for upstream drift).
- **Complementary (separate plugin, called into, not vendored):** `dz-core` for branded charts (`dz-core:create-chart`), branded PDF (`dz-core:create-paper`), Instagram tiles, onboarding.

---

## Principles

- **Passport is truth.** Never guess the stage — read `passport.yaml`.
- **One step at a time.** Recommend the single next step; advance only on explicit confirmation.
- **Required vs optional, always.** Don't bury the one thing they must do next.
- **Name the exact command + mode.** No vague "continue the analysis."
