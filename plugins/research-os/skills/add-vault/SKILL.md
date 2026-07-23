---
name: add-vault
description: Register a new thematic research wiki. Scaffolds the numbered layout (00_inbox, 10_sources, 20_summaries, 30_concepts, 40_methods, 50_datasets, 60_people_institutions, 90_synthesis) with per-folder README.md placeholders under the vault root, adds an entry to ~/.claude/vaults.json, updates _brain/wikis-index.md's table, and writes a short theme README.md after a brief Socratic scope interview. Use when the user wants to start tracking a new research theme, add a new wiki, or split off part of an existing wiki into its own theme.
argument-hint: "[theme-name]"
allowed-tools: Read, Write, Edit, Glob, Bash
---

# Add Vault

Register and scaffold a new thematic wiki under the existing vault root. This
is the only supported way to create a new wiki folder — never hand-create
`<theme>/00_inbox` etc.; that skips the registry entry, the shared-template
wiring, and the index/README conventions this skill keeps consistent.

## Step 0: Require the registry

Read `~/.claude/vaults.json`. If it does not exist, stop and tell the user to
run `/wiki-setup` first (it creates the root + registry); re-run `/add-vault`
afterward. Do not bootstrap a root here — that's `/wiki-setup`'s job.

Resolve `<ROOT>` = registry `root`, `<BRAIN>` = registry `brain.path`. Also
check `<ROOT>/_templates/` exists (Step 4 below wires new pages to it) — if
it's missing, stop and tell the user to run `/wiki-setup` first to repair the
structure, then re-run `/add-vault`.

## Step 1: Determine the theme slug

- Use `$ARGUMENTS` if given; otherwise ask: "What should this new wiki be
  called?" (a short theme name — it becomes the folder name).
- Normalize to kebab-case: lowercase, spaces/underscores → hyphens, strip
  anything that isn't `[a-z0-9-]`.
- Check the slug isn't already a key in the registry's `wikis` map, and isn't
  `_brain` or `_templates`. If a folder with that name already exists under
  `<ROOT>` but isn't registered, tell the user and ask how to proceed (reuse
  it as this new wiki vs. pick a different name) rather than silently
  overwriting anything inside it.

## Step 2: Short Socratic scope interview

**Conversational, not a form.** Ask 1-2 questions at a time in plain text;
wait for replies. Do NOT use `AskUserQuestion`. Keep it to 2-4 exchanges —
just enough to write an honest one-paragraph scope description, modeled on
`vault/cognitive-load/README.md`'s style: what this theme covers, and how it
differs from (or feeds) related work.

Cover:
1. **Scope** — "What does this wiki cover? What research question or family
   of questions does it serve?"
2. **Boundary** — "What's explicitly out of scope — the thing someone might
   expect here but that actually belongs in a different wiki?" (probe gently
   if the answer suggests this should be a section of an existing wiki
   instead of a new one — a new theme should earn its own top-level folder)
3. *(optional, if unclear)* "Which project(s), if any, will this feed?"

## Step 3: Confirm before creating anything

Summarize: theme slug, one-paragraph scope description, target path
(`<ROOT>/<slug>/`). Get a yes before scaffolding.

## Step 4: Scaffold the folder tree

```bash
cd "<ROOT>/<slug>"
mkdir -p 00_inbox 10_sources 20_summaries 30_concepts 40_methods 50_datasets 60_people_institutions 90_synthesis
```

Every wiki in this vault documents each numbered folder's purpose with a
short `README.md` — write the same eight placeholders (these are generic
and theme-independent; do not customize their content per theme):

`00_inbox/README.md`
```markdown
# Inbox

This folder is for unsorted incoming material.

Examples:
- rough notes
- links
- pasted abstracts
- screenshots
- temporary markdown notes
- early thoughts not yet filed into the wiki

Nothing should live here permanently.
Inbox items should later be:
- moved into `10_sources/` if they are raw source materials
- turned into proper wiki pages
- deleted if no longer useful
```

`10_sources/README.md`
```markdown
# Raw Sources

This folder contains the raw source materials that feed the wiki.

Examples:
- paper PDFs
- reports
- markdown article clips
- transcripts
- tables
- images

Rules:
- treat this folder as the immutable source layer
- do not rewrite source files
- do not use this folder for summaries or interpretation
- every important source should eventually have a corresponding page in `20_summaries/`
```

`20_summaries/README.md`
```markdown
# Source Summaries

This folder contains one page per important source.

Each summary page should usually include:
- source title
- author(s)
- year
- source type
- one-paragraph summary
- key claims
- method or identification strategy
- main findings
- limitations
- relevance for my research
- links to related concept, method, dataset, and project pages

The goal is to make each source reusable without rereading the full raw document.
```

`30_concepts/README.md`
```markdown
# Concepts

This folder contains concept and mechanism pages.

A concept page should usually include:
- definition
- why it matters
- mechanism
- common measurements or proxies
- related concepts
- debates or ambiguities
- links to summaries, methods, datasets, and projects
```

`40_methods/README.md`
```markdown
# Methods

This folder contains methodology pages.

A method page should usually include:
- what the method does
- identification logic
- assumptions
- typical diagnostics
- common pitfalls
- best use cases
- links to papers and projects using it
```

`50_datasets/README.md`
```markdown
# Datasets

This folder contains dataset pages.

A dataset page should usually include:
- what the dataset covers
- geography and period
- unit of observation
- key variables
- strengths
- limitations
- likely use cases
- related projects and methods
```

`60_people_institutions/README.md`
```markdown
# People and Institutions

This folder contains entity pages for recurring people, institutions, journals, and organizations.

Examples:
- authors
- research groups
- journals
- think tanks
- ministries
- firms
- data providers

Each page should explain:
- who or what the entity is
- why it matters for my research
- related topics, methods, datasets, or projects
```

`90_synthesis/README.md`
```markdown
# Synthesis

This folder contains higher-level synthesis pages, **within this theme only**
— cross-theme or personal synthesis belongs in `_brain/synthesis/` instead.

Examples:
- literature overviews
- comparison pages
- competing hypotheses
- research design comparisons
- "what we know so far" notes
- thematic briefings

This folder should capture durable thinking, not temporary chat output. If a
query or discussion produces a useful synthesis, it should be written here
instead of disappearing into conversation history.
```

New note pages inside this wiki use the shared templates at
`<ROOT>/_templates/` (`concept_template.md`, `method_template.md`,
`dataset_template.md`, `entity_template.md`, `synthesis_template.md`,
`source_summary_template.md`) — they are not duplicated per wiki.

## Step 5: Write the theme `README.md`

At `<ROOT>/<slug>/README.md`, using the interview answers, modeled on
`vault/cognitive-load/README.md`'s length and tone (2-4 sentences):
```markdown
# <slug>

<one-paragraph scope description from the interview.>

Fully Claude-maintained — see the root `CLAUDE.md` and the plugin's
`wiki-integration.md` for the schema and rules. Don't hand-edit; use
`/wiki-ingest` and `/wiki-maintain`.
```

## Step 6: Register in `~/.claude/vaults.json`

Add an entry under `wikis` (never touch `root`, `brain`, or other wikis'
entries):
```json
"<slug>": {
  "path": "<ROOT>/<slug>",
  "description": "<one-line scope, distilled from the interview>",
  "registered": "<YYYY-MM-DD>"
}
```

## Step 7: Update `<BRAIN>/wikis-index.md`

Add a row to its table:
```markdown
| [[<slug>/README\|<slug>]] | `<slug>/` | <one-line scope> | <YYYY-MM-DD> |
```

## Step 8: Update the root `index.md` Dataview queries (if present)

`<ROOT>/index.md` is Dataview-driven with per-section `FROM` clauses listing
every wiki (e.g. `FROM "cognitive-load/20_summaries" OR
"innovation-policy/20_summaries"`). Extend every `FROM` clause in that file
to include `"<slug>/<folder>"` alongside the existing wikis, for all six
content folders (summaries, concepts, methods, datasets, people/
institutions, synthesis).

## Step 9: Report

Summarize:
- Theme registered: `<slug>` at `<ROOT>/<slug>/`
- Folders scaffolded (8) + README placeholders written
- `~/.claude/vaults.json`: entry added
- `_brain/wikis-index.md`: row added
- `index.md`: `FROM` clauses extended (or "no `index.md` found — skipped")
- Next step: `/wiki-ingest [source]` to start populating it, or set this as
  a project's `main_wiki` in its `passport.yaml`

## Guardrails

Do not:
- create a wiki folder without registering it (always do both together)
- customize the eight per-folder README placeholders per theme — they are
  intentionally generic and consistent across every wiki
- silently reuse an unregistered folder that already has content — ask first
- touch other wikis' entries in `vaults.json` or their rows in
  `wikis-index.md`
- skip the scope interview and guess a description from the slug alone
