---
name: wiki-pull
description: >
  Retrieve and synthesize relevant prior knowledge from the personal brain
  (`_brain/`) and the relevant thematic research wiki before starting
  substantial project work. Use whenever beginning literature reviews,
  empirical design, data work, model building, writing, slides, synthesis, or
  project planning — even if the user does not explicitly mention the wiki.
  Also use when entering an existing project and needing to understand what
  is already known.
argument-hint: "[--wiki <theme>] [research topic or question]"
allowed-tools: Read, Glob, Grep
---

# Wiki Pull

Retrieve relevant prior knowledge — from the user's personal second brain and
from the relevant Claude-maintained thematic wiki — before starting
substantial work on a topic. This is a **global** skill: it works standalone
and inside any research-os project.

## Goal

Do not start from zero if the user already has relevant knowledge saved.

This skill should:
- find relevant prior notes, in both knowledge layers
- summarize what is already known
- identify what can be reused
- identify what is still missing
- connect the project to the right wiki pages

## Resolve the knowledge layers

research-os keeps durable knowledge in two layers (full policy:
`${CLAUDE_PLUGIN_ROOT}/rules/wiki-integration.md` when running inside a
research-os project; the same model applies standalone). A personal
**`_brain/`** layer (human-owned: profile, projects, personal/cross-theme
synthesis) and one or more Claude-maintained **thematic wikis** (one per
research theme, numbered `00_inbox` .. `90_synthesis`).

1. **Read the registry** `~/.claude/vaults.json` (a `theme -> path` map, plus
   `brain.path`). If it exists, use it.
2. **If it does not exist**, fall back to the legacy single pointer
   `~/.claude/VAULT_PATH` — treat its target as one flat legacy vault (no
   `_brain` split, no multiple themes).
3. **If neither exists**: skip all wiki/brain steps silently. Say nothing
   about it and proceed with whatever the user asked, using only what's in
   the current project. Do not hallucinate wiki contents.
4. **Pick the target wiki** (registry case), in order:
   - `--wiki <theme>` argument, if given.
   - Else, if a `passport.yaml` exists in the current project, read
     `meta.main_wiki`.
   - Else, if the registry has exactly one wiki, use it.
   - Else (ambiguous): ask the user in plain text which registered wiki to
     use — list the themes with their one-line descriptions from the
     registry. Wait for the answer. This is the one place this otherwise
     silently-degrading skill asks a question, because guessing the wrong
     theme would return misleading results.
5. Resolve `<WIKI>` (the chosen wiki's path) and `<BRAIN>` (`brain.path` from
   the registry, if present).

## Retrieval order — check `_brain/` first, then the wiki

1. **`<BRAIN>/profile.md`** — standing context: who the user is, how they
   want Claude to work with them, recurring constraints. Skip if it is still
   the uninitialized placeholder.
2. **`<BRAIN>/projects/<slug>.md`** — if working inside a named project
   (slug = `passport.yaml` `meta.slug`, or `basename $(pwd)` lowercased with
   spaces to hyphens), read the project's own journal for what was already
   decided or tried.
3. **`<BRAIN>/synthesis/`** — personal or cross-theme insight that might bear
   on the current task, even if it spans multiple wikis.
4. **`<WIKI>/90_synthesis/`** — theme-internal synthesis pages that connect
   multiple sources; the fastest way to reuse cumulative understanding.
5. **`<WIKI>/30_concepts/`, `/40_methods/`, `/50_datasets/`,
   `/60_people_institutions/`** — canonical notes.
6. **`<WIKI>/20_summaries/`** — detailed source summaries.
7. **`<WIKI>/10_sources/`** — raw sources, only when maintained notes are
   missing or need verification.
8. **`wiki-links.md`** in the current project, if present — the project's own
   curated bridge into the wiki.

Flag when the best available notes are weak, shallow, missing source paths,
or need source verification so the user understands retrieval confidence.

## Workflow

### Step 1: Understand the current task
Identify what kind of task is being started: literature review, conceptual
framing, identification strategy, method choice, dataset selection, model
design, writing, slides, project planning, replication/debugging.

### Step 2: Search `_brain/`, then the wiki
Follow the retrieval order above. Prefer:
- personal project context over starting fresh
- synthesis and canonical notes over fragmented mentions
- existing summaries over raw sources

### Step 3: Select the most useful notes
Choose only the most relevant material from each layer. Do not overwhelm the
user with everything found.

### Step 4: Synthesize
Produce a concise synthesis that answers:
- What does the user already know or think about this (from `_brain/`)?
- What does the wiki already establish (from `<WIKI>`)?
- What can be reused directly?
- What is still unclear or missing?
- Which notes — in either layer — matter most for this task?

### Step 5: Update the project bridge if useful
If `wiki-links.md` exists in the current project, update it when helpful by
adding the most relevant wiki notes and noting missing knowledge gaps. Do not
write into `_brain/` or the wiki during a pure pull step unless the user
explicitly asks for that — that is `/wiki-push`'s job.

## Output Format

### Personal context (from `_brain/`)
- what the user's own profile/project notes/synthesis already say

### Wiki knowledge (from `<WIKI>`)
- concise bullets or a short structured summary

### Most relevant notes
- note/file paths or clear references, tagged by layer

### Reuse opportunities
- what should directly inform the current work

### Gaps
- what still needs to be figured out

### Wiki maintenance needed
- weak summaries, duplicate canonical candidates, missing synthesis, or
  broken retrieval paths noticed during the pull (flag for `/wiki-maintain`,
  do not fix them here)

### Optional project bridge update
- what was added or clarified in `wiki-links.md`

## Guardrails

Do not:
- dump large excerpts
- list every weakly related note
- fabricate wiki or `_brain/` contents
- modify `_brain/` or the wiki unless clearly asked
- create duplicate project notes unnecessarily
- write personal/project-specific content into the thematic wiki, or
  objective source knowledge into `_brain/` — each layer has one job

## Standard

This skill is successful if the user can begin the task with a clear view of:
- what they already know or decided (from `_brain/`)
- what the wiki already establishes
- what should be reused
- what is missing
