---
name: wiki-pull
description: >
  Retrieve and synthesize relevant prior knowledge from the global research wiki
  before starting substantial project work. Use whenever beginning literature
  reviews, empirical design, data work, model building, writing, slides,
  synthesis, or project planning — even if the user does not explicitly mention
  the wiki. Also use when entering an existing project and needing to understand
  what is already known.
argument-hint: "[research topic or question]"
allowed-tools: Read, Glob, Grep
---

# Wiki Pull

Retrieve relevant prior knowledge from the global research wiki before starting
substantial work on a topic.

## Goal

Do not start from zero if the user already has relevant knowledge in the wiki.

This skill should:
- find relevant prior notes
- summarize what is already known
- identify what can be reused
- identify what is still missing
- connect the project to the right wiki pages

## Preconditions

Before proceeding, confirm that the global wiki is accessible in the current
session (check for `vault/index.md` or `vault/CLAUDE.md`).

If it is not accessible:
- stop
- say that the global wiki is not currently available
- ask the user to add the wiki directory to the session (via `--add-dir` or
  `additionalDirectories` in `~/.claude/settings.json`)
- do not hallucinate wiki contents

## Inputs to Inspect

Check, when available:
- the current user request
- the current project files
- `wiki-links.md` in the current project
- the global wiki folders, especially:
  - `vault/20_summaries/`
  - `vault/30_concepts/`
  - `vault/40_methods/`
  - `vault/50_datasets/`
  - `vault/70_projects/`
  - `vault/90_synthesis/`

## Workflow

### Step 1: Understand the current task
Identify what kind of task is being started:
- literature review
- conceptual framing
- identification strategy
- method choice
- dataset selection
- model design
- writing
- slides
- project planning
- replication or debugging

### Step 2: Search the wiki
Search for notes that are relevant to the current task.

Prefer:
- existing summaries over raw notes
- concept and method notes over fragmented mentions
- related project notes when the task resembles earlier work

Stronger retrieval order:
1. synthesis pages that connect multiple sources
2. canonical concept, method, and dataset notes
3. detailed source summaries
4. project pages and `wiki-links.md`
5. raw sources only when maintained notes are missing or need verification

Flag when the best available notes are weak, shallow, missing source paths, or
need source verification so the user understands retrieval confidence.

### Step 3: Select the most useful notes
Choose only the most relevant material.
Do not overwhelm the user with everything you find.

### Step 4: Synthesize
Produce a concise synthesis that answers:
- What do we already know?
- What can be reused directly?
- What is still unclear or missing?
- Which wiki notes matter most for this task?

### Step 5: Update the project bridge if useful
If `wiki-links.md` exists, update it when helpful by adding the most relevant
wiki notes and noting missing knowledge gaps.

Do not write into the global wiki during a pure pull step unless the user
explicitly asks for that.

## Output Format

Structure the result like this:

### Relevant wiki knowledge
- concise bullets or a short structured summary

### Most relevant notes
- note/file names or clear references

### Reuse opportunities
- what should directly inform the current work

### Gaps
- what still needs to be figured out

### Wiki maintenance needed
- weak summaries, duplicate canonical candidates, missing synthesis, or broken
  retrieval paths found during the pull

### Optional project bridge update
- what was added or clarified in `wiki-links.md`

## Guardrails

Do not:
- dump large excerpts
- list every weakly related note
- fabricate wiki contents
- modify the global wiki unless clearly asked
- create duplicate project notes unnecessarily

## Standard
This skill is successful if the user can begin the task with a clear view of:
- what already exists
- what should be reused
- what is missing
