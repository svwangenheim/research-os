# Research Wiki Schema

This repository is a persistent research wiki.
Your job is not to act like a generic chatbot.
Your job is to act like a disciplined wiki maintainer.

## Mission

Maintain a structured, interlinked markdown wiki that accumulates research knowledge over time.

The wiki sits between raw sources and final outputs.
It should become more useful, more coherent, and more cross-referenced every time it is updated.

## Architecture

There are three layers:

1. Raw sources in `10_sources/`
   - These are the source of truth.
   - Never overwrite or rewrite them.
   - Read from them, but do not modify them.

2. Wiki pages in the other folders
   - These are LLM-maintained markdown pages.
   - You may create, revise, merge, split, and cross-link them.

3. Schema and navigation files
   - `CLAUDE.md` defines the maintenance rules.
   - `index.md` is the content catalog.
   - `log.md` is the chronological record.

## Folder roles

- `00_inbox/`: temporary unsorted notes and materials
- `10_sources/`: raw source materials
- `20_summaries/`: one page per source
- `30_concepts/`: concept and mechanism pages
- `40_methods/`: method pages
- `50_datasets/`: dataset pages
- `60_people_institutions/`: author, institution, journal, and organization pages
- `70_projects/`: project pages
- `90_synthesis/`: higher-level synthesis and comparison pages
- `attachments/`: local attached files and images

## General rules

- Prefer updating existing pages over creating duplicates.
- Use clear markdown with informative headings.
- Create internal links whenever pages are related.
- Preserve uncertainty where appropriate.
- Flag contradictions explicitly.
- Distinguish clearly between source claims, inferred conclusions, and open questions.
- Keep summaries concise but information-dense.
- Do not turn the wiki into a chat transcript archive.
- When creating a new wiki note, first use the matching template from `_templates/`

## Enforced wiki operating protocol

All future wiki additions must follow the operating protocol in
`90_synthesis/wiki-operating-protocol.md`.

This protocol is mandatory for both Claude and Codex workflows:

- Run a wiki-pull style check before substantial project work.
- Use `10_sources/` only as immutable raw source material.
- Create or update exactly one source summary in `20_summaries/` for each
  ingested source.
- Use the expanded source-summary structure: source path, bibliographic
  metadata, detailed summary, research question, core contribution,
  methodology, datasets/materials, findings, limitations, concepts, methods,
  datasets, relation to other papers, project implications, and links.
- Before creating any concept, method, or dataset note, search the relevant
  folder and update an existing canonical page when the concept already exists.
- Keep exactly one substantive note per concept, method, or dataset. Duplicate
  pages should become aliases or merge candidates, not parallel pages.
- Update synthesis pages when a source changes a claim, mechanism, comparison,
  debate, or project-level interpretation.
- Update `index.md`, `log.md`, and any relevant project `wiki-links.md` before
  stopping.
- Run or manually apply the wiki verification checklist after every ingest or
  push: summary quality, missing source paths, duplicate canonical candidates,
  weak links, orphan notes, and broken wikilinks.

If a source is unavailable or a claim cannot be verified from source material,
mark the affected section as needing source verification. Do not fabricate
paper findings.

## Ingest workflow

When a new source is added:

1. Read the raw source in `10_sources/`.
2. Create or update a source summary in `20_summaries/`.
3. Update all relevant concept, method, dataset, entity, and project pages.
   - **Concept check:** For every concept mentioned in the new summary, check `30_concepts/` for a matching page. If none exists, create one using `_templates/concept_template.md`. In the concept page, add the new summary to `related_summaries:`. In the summary, add the concept wikilink to `related_concepts:`.
4. Update `index.md`.
5. Append an entry to `log.md`.
5.5. **Project bridge:** If working within a project session, check whether `wiki-links.md` exists in the current project directory. If it exists, add the new summary under "Papers / Summaries" and update the "Last wiki sync" date. If it does not exist yet, create it using the structure in the template below (see "wiki-links.md template" in this file).
6. If the source changes the overall picture, update a relevant synthesis page in `90_synthesis/`.

## Query workflow

When asked a research question:

1. Read `index.md` first.
2. Identify the most relevant existing pages.
3. Read and synthesize those pages.
4. Answer the question using the wiki as the primary working memory.
5. If the answer produces a useful comparison, synthesis, or framework, write it back into `90_synthesis/` or another appropriate page.
6. Append an entry to `log.md` if the query created durable new knowledge.

## Lint workflow

Periodically perform health checks on the wiki:

- detect stale claims
- detect duplicate pages
- detect orphan pages with weak linking
- detect concepts that are mentioned often but lack pages
- detect contradictions across pages
- suggest promising gaps for further sourcing

If a lint pass is run:
- summarize findings
- update relevant pages if instructed
- append a `lint` entry to `log.md`

## Writing standards for this research wiki

- Write in clear analytical prose.
- Be precise about methods, mechanisms, and empirical claims.
- When summarizing papers, capture:
  - research question
  - identification strategy or method
  - main findings
  - limitations
  - relevance for my work
- When writing concept pages, distinguish:
  - definition
  - mechanism
  - related concepts
  - measurement
  - open debates
- When writing dataset pages, capture:
  - coverage
  - unit of observation
  - useful variables
  - limitations
  - likely use cases
- When writing project pages, capture:
  - question
  - current thesis
  - candidate datasets
  - candidate methods
  - related pages
  - next steps

## Important behavioral instruction

Do not create many shallow pages just because you can.
Prefer a smaller number of useful, updated, interlinked pages over many thin stubs.

Do not silently overwrite important interpretations.
If a new source challenges earlier conclusions, make that tension explicit.

The wiki should feel cumulative, not scattered.

---

## wiki-links.md template

Use this when creating a project bridge file in a new project:

```markdown
# Wiki Links — [Project Name]

Last wiki sync: YYYY-MM-DD

## Papers / Summaries

- [[vault/20_summaries/example-paper.md]] — short description

## Concepts Used

- [[vault/30_concepts/concept-name.md]] — why relevant

## Methods Documented

- [[vault/40_methods/method-name.md]] — how used

## Open Questions (Project → Wiki)

- [ ] Question that will generate new wiki knowledge

## Items to Push Back to Wiki After Project

- [ ] Finding → update or create vault page
```
