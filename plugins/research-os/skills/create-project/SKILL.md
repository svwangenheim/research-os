---
name: create-project
description: Scaffold a new research-os paper project - folder tree, passport.yaml, CLAUDE.md, wiki-links.md, dashboard seed, and a main thematic wiki. Use when starting a new project.
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

## Step 2 — Assign main wiki

1. Read the vault registry at `~/.claude/vaults.json`.
2. If it exists, list the thematic wikis and ask the user to pick the **main wiki** for this project (all wikis stay readable; this is the default). Offer "create a new one" → run `/add-thematic-wiki` then continue.
3. If the registry does **not** exist yet (knowledge layer not built), say so, and ask for a theme name to record in the passport now; suggest running `/wiki-setup` later. Do not block project creation.

## Step 3 — Confirm the plan

Summarize: project title + slug, target path, main wiki, language, citation style. Get a yes before creating anything.

## Step 4 — Scaffold the folder tree

Derive `<slug>` (kebab-case) and `<path>` (a positional path arg, else `./<slug>`). Create the numbered tree per `folder-map.md`, including the single `04_paper/academic_paper/` output folder:

```bash
cd "<path>"
mkdir -p .claude/rules \
         00_admin/process/{plans,decisions,sessions,handoffs} 00_admin/logistics \
         01_literature/{sources,reviews,notes} \
         02_data/{raw,cleaned,codebooks,external} \
         03_analysis/{strategy,scripts/R,scripts/py,scripts/jl,output,replication} \
         04_paper/academic_paper/{sections,figures,tables,preambles,supplementary} \
         04_paper/{reviews,revisions,submission} \
         05_outreach/{talks,social} \
         explorations ARCHIVE
```

## Step 5 — Write config + state from templates

Fill placeholders from the interview + selections, then write:
- `CLAUDE.md` ← `${CLAUDE_PLUGIN_ROOT}/templates/project-CLAUDE.md`
- `passport.yaml` ← `${CLAUDE_PLUGIN_ROOT}/templates/passport.yaml` (fill `meta`, `research`; leave corpus/claims empty; `pipeline.current_stage: discovery`)
- `wiki-links.md` ← `${CLAUDE_PLUGIN_ROOT}/templates/wiki-links.md`
- `00_admin/research_outline.md` — a short living brief seeded from the interview
- `explorations/README.md` ← `${CLAUDE_PLUGIN_ROOT}/templates/explorations-root-readme.md`
- `project_dashboard.html` — run `/dashboard` (or its generator) to seed the living overview

Also copy every file from `${CLAUDE_PLUGIN_ROOT}/templates/project-rules/` into `.claude/rules/` (create the directory). These are **path-scoped rule stubs**, and they are the only reason the plugin's rules activate on their own.

The mechanism is worth understanding, because it is not obvious: `rules/` is **not** a recognized Claude Code plugin component, so the plugin's own rules never auto-load — they are inert files a skill has to `Read`. A project's `.claude/rules/` **is** loaded, and honours `paths:` frontmatter, so a rule there enters context only when a matching file is touched. Each stub therefore carries the `paths:` glob plus a short pointer to the authoritative rule in the plugin. Keep them thin: the plugin rule stays the single source of truth, and a stub that starts restating it will drift from it.

## Step 6 — Prime the wiki bridge

If a main wiki is registered, run `/wiki-pull` for it to pre-populate relevant concepts/methods/datasets into `wiki-links.md` and flag reuse opportunities. Skip silently if the knowledge layer isn't built yet.

## Step 7 — Hand off

Print a short summary of what was created and end with:

> Project ready. Run **`/research-os-help`** to see your next step (it reads `passport.yaml`). Typical first step: `/discover` to build the research spec + literature.

---

## Principles

- **Scaffold, don't execute.** One step at a time — `/create-project` only sets up; the user drives the pipeline.
- **State in the passport.** Seed `passport.yaml`; never scatter state.
- **Degrade gracefully.** Works before the knowledge layer exists (Step 2 fallback).
- **Follow `folder-map.md`.** Never invent paths.
