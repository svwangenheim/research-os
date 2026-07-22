---
name: wiki-push
description: >
  Write durable knowledge from the current project back into the global research
  wiki after meaningful work blocks. Use whenever new reusable knowledge has been
  produced — paper summaries, method insights, dataset lessons, conceptual
  clarifications, project synthesis, or reusable research reasoning — even if the
  user does not explicitly mention updating the wiki.
argument-hint: "[optional: specific notes or topic to push]"
allowed-tools: Read, Write, Edit, Glob, Grep
---

# Wiki Push

Write durable knowledge from the current project back into the global research wiki.

## Goal

Turn project work into reusable long-term knowledge.

This skill should:
- identify what is worth preserving
- distinguish durable knowledge from temporary project clutter
- update existing wiki notes where possible
- create clean new notes only when needed
- keep the wiki coherent and non-duplicative

## Preconditions

Before proceeding, confirm that the global wiki is accessible in the current
session (check for `vault/index.md` or `vault/CLAUDE.md`).

If it is not accessible:
- stop
- say that the global wiki is not currently available
- ask the user to add the wiki directory to the session
- do not invent file updates

## What Counts as Durable Knowledge

**Good candidates:**
- clean paper summaries
- method lessons
- dataset notes
- conceptual clarifications
- synthesis across sources
- reusable project insights
- definitions that will matter again
- decisions that future projects may benefit from

**Poor candidates:**
- scratch notes
- temporary logistics
- half-formed thoughts
- duplicate notes
- raw copied text without synthesis
- project-specific clutter with no broader reuse value

## Inputs to Inspect

Check, when available:
- the current user request
- `notes/` folder in the current project
- `wiki-links.md`
- recent outputs, summaries, or decisions
- the existing wiki structure, especially:
  - `vault/20_summaries/`
  - `vault/30_concepts/`
  - `vault/40_methods/`
  - `vault/50_datasets/`
  - `vault/70_projects/`
  - `vault/90_synthesis/`

## Workflow

### Step 1: Identify durable knowledge
Decide what has been learned that deserves to survive beyond this project session.

### Step 2: Check for an existing destination
Look for an existing wiki note that should be updated.
Prefer updating existing notes over creating new ones.
For concepts, methods, and datasets, search aliases and near-duplicates before
writing. There must be only one substantive canonical page per concept, method,
or dataset.

### Step 3: Write or update cleanly
When updating the wiki:
- write concise, reusable prose
- structure clearly
- remove redundancy
- keep notes easy to reuse later
- preserve or add useful links where appropriate
- link project findings back to relevant summaries, canonical pages, datasets,
  methods, and synthesis pages
- distinguish project evidence, source claims, inferred conclusions, and open
  questions

If a project result changes the interpretation of several papers, update or
create a synthesis page rather than scattering the insight across isolated
notes.

### Step 4: Update the project bridge
Update `wiki-links.md` to record:
- what was written back
- which wiki notes now matter for the project
- what still remains to be pushed later

### Step 5: Append to log
Append an entry to `vault/log.md`:
```
## [YYYY-MM-DD] synthesis | [short title]
[One-line description of what was pushed and which pages were updated]
```

### Step 6: Report clearly
Before reporting, run `python wiki_quality_check.py --vault [vault path]` from
Research-OS when available, or manually report required-section gaps, missing
source paths, duplicate canonical candidates, orphan/weak links, broken
wikilinks, and whether `index.md`, `log.md`, and project `wiki-links.md` were
updated.

Summarize:
- what was updated
- what was created
- what was intentionally left out because it was too temporary
- verification result and unresolved wiki-quality issues

## Output Format

Structure the result like this:

### Durable knowledge identified
- what is worth preserving

### Wiki updates made
- existing notes updated
- new notes created

### Project bridge update
- what changed in `wiki-links.md`

### Not pushed
- what was intentionally kept out of the wiki

## Guardrails

Do not:
- dump raw project notes into the wiki
- create duplicate pages without checking first
- overfit the wiki to one project's temporary needs
- fabricate updates when the vault is not accessible
- overwrite substantial notes carelessly
- push durable findings without updating backlinks, synthesis, index/log, and
  project bridge where relevant

## Standard
This skill is successful if the wiki becomes more useful for future work without
becoming cluttered.
