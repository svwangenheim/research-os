---
name: create-project
description: Scaffold a new research-os project — a light Socratic intro, choose intended outputs (paper / policy brief / Fachtext / Hintergrundpapier / Geldbrief), assign a main thematic wiki, then create the numbered folder tree, passport.yaml, CLAUDE.md, wiki-links.md, and a dashboard seed. Replaces clo-author's fork-and-clone. Use when starting a new project.
argument-hint: "[topic, or path to create the project in]"
allowed-tools: Read,Glob,Grep,Write,Edit,Bash,AskUserQuestion,Task
---

# Create Project

Scaffold a new research-os project and initialize its state. This **sets up** the project; it does not run the pipeline. When done, point the user to `/research-os-help` for the next step.

**Input:** `$ARGUMENTS` — a research topic and/or a target path.

Templates live in `${CLAUDE_PLUGIN_ROOT}/templates/`. The folder scheme is defined in `${CLAUDE_PLUGIN_ROOT}/rules/folder-map.md` — treat it as the single source of truth.

---

## Step 1 — Light Socratic intro

Conversational, **not** a form. Ask 1–2 questions at a time in plain text; wait for replies. Do NOT use AskUserQuestion here (that comes in Step 2). Keep it short (3–6 exchanges) — just enough to seed the passport. Cover: the phenomenon/question, why it matters, rough method/setting, and the intended contribution. Be curious, not prescriptive; probe weak spots gently ("what would a skeptic say?").

For a deeper research-question interview, note that `/discover interview` exists — `/create-project` only needs enough to scaffold.

## Step 2 — Intended outputs (multi-select)

Ask, using AskUserQuestion (multiSelect), which outputs this project will produce. Options:
- **Academic paper** (`academic_paper/`) — IMRaD / review / theory / case study / conference
- **DZ Policy brief** (`policy_brief/`)
- **DZ Fachtext** (`fachtext/`)
- **DZ Hintergrundpapier** (`hintergrundpapier/`)
- **DZ Geldbrief** (`geldbrief/`)

Each selected output becomes a subfolder under `04_paper/`. At least one is required.

## Step 3 — Assign main wiki

1. Read the vault registry at `~/.claude/vaults.json`.
2. If it exists, list the thematic wikis and ask the user to pick the **main wiki** for this project (all wikis stay readable; this is the default). Offer "create a new one" → run `/add-vault` then continue.
3. If the registry does **not** exist yet (knowledge layer not built), say so, and ask for a theme name to record in the passport now; suggest running `/wiki-setup` later. Do not block project creation.

## Step 4 — Confirm the plan

Summarize: project title + slug, target path, selected outputs (→ `04_paper/` subfolders), main wiki, language, citation style. Get a yes before creating anything.

## Step 5 — Scaffold the folder tree

Derive `<slug>` (kebab-case) and `<path>` (a positional path arg, else `./<slug>`). Create the numbered tree per `folder-map.md`:

```bash
cd "<path>"
mkdir -p 00_admin/process/{plans,decisions,sessions} 00_admin/logistics \
         01_literature/{sources,reviews,notes} \
         02_data/{raw,cleaned,codebooks,external} \
         03_analysis/{strategy,scripts/R,scripts/py,scripts/jl,output,replication} \
         04_paper/{reviews,revisions,submission} \
         05_outreach/{talks,social} \
         explorations ARCHIVE
```

Then create **one `04_paper/<output>/` subfolder per selected output**, each with `sections/ figures/ tables/ preambles/ supplementary/`:

```bash
# for each selected output in {academic_paper, policy_brief, fachtext, hintergrundpapier, geldbrief}:
mkdir -p 04_paper/<output>/{sections,figures,tables,preambles,supplementary}
```

## Step 6 — Write config + state from templates

Fill placeholders from the interview + selections, then write:
- `CLAUDE.md` ← `${CLAUDE_PLUGIN_ROOT}/templates/project-CLAUDE.md`
- `passport.yaml` ← `${CLAUDE_PLUGIN_ROOT}/templates/passport.yaml` (fill `meta`, `research`; leave corpus/claims empty; `pipeline.current_stage: discovery`)
- `wiki-links.md` ← `${CLAUDE_PLUGIN_ROOT}/templates/wiki-links.md`
- `00_admin/research_outline.md` — a short living brief seeded from the interview
- `explorations/README.md` ← `${CLAUDE_PLUGIN_ROOT}/templates/explorations-root-readme.md`
- `project_dashboard.html` — run `/dashboard` (or its generator) to seed the living overview

## Step 7 — Prime the wiki bridge

If a main wiki is registered, run `/wiki-pull` for it to pre-populate relevant concepts/methods/datasets into `wiki-links.md` and flag reuse opportunities. Skip silently if the knowledge layer isn't built yet.

## Step 8 — Hand off

Print a short summary of what was created and end with:

> Project ready. Run **`/research-os-help`** to see your next step (it reads `passport.yaml`). Typical first step: `/discover` to build the research spec + literature.

---

## Principles

- **Scaffold, don't execute.** One step at a time — `/create-project` only sets up; the user drives the pipeline.
- **Outputs drive `04_paper/`.** Only create subfolders for what was selected.
- **State in the passport.** Seed `passport.yaml`; never scatter state.
- **Degrade gracefully.** Works before the knowledge layer exists (Step 3 fallback).
- **Follow `folder-map.md`.** Never invent paths.
