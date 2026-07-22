---
name: wiki-maintain
description: >
  Audit and remediate the global research wiki until it meets the established
  A-tier standards for source summaries, canonical concepts, methods, datasets,
  project pages, synthesis pages, links, indexes, and verification. Use when
  the user asks to improve the whole wiki, check wiki quality, canonicalize
  concepts/methods/datasets, update synthesis, or make wiki-pull retrieval
  reliable across the vault.
argument-hint: "[optional scope: all | summaries | concepts | methods | datasets | synthesis | project | path]"
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

# Wiki Maintain

Audit and remediate the research wiki as a whole. This skill is the
whole-vault counterpart to `wiki-ingest`: `wiki-ingest` processes one source;
`wiki-maintain` checks and improves the entire maintained wiki until the
established standards are met.

## Preconditions

**Step 0: Find the vault**

The vault is made available via `additionalDirectories` in `~/.claude/settings.json`
or via `claude --add-dir /path/to/vault`.

To locate the vault's absolute path:

1. Check for `~/.claude/VAULT_PATH`; if it exists, read the path from it.
2. If not found, check whether `vault/index.md` exists in the current workspace.
3. If still not found, stop and tell the user:
   - Confirm the vault is added to this session.
   - Create `~/.claude/VAULT_PATH` with the absolute path.

If the vault cannot be confirmed: **stop. Do not hallucinate wiki contents.**

## Identify Scope

`$ARGUMENTS` is optional:

- `all` or empty -> audit and remediate the whole maintained wiki.
- `summaries` -> focus on `20_summaries/`.
- `concepts` -> focus on `30_concepts/`.
- `methods` -> focus on `40_methods/`.
- `datasets` -> focus on `50_datasets/`.
- `synthesis` -> focus on `90_synthesis/`.
- `project` -> focus on `70_projects/` and current-project `wiki-links.md`.
- path -> focus on that file or folder, then check affected backlinks.

Even for a narrow scope, check whether changes create missing backlinks,
duplicates, broken links, or synthesis/project update needs.

## Step 1: Run the Quality Baseline

From the Research-OS root, run when available:

```bash
python wiki_quality_check.py --vault "$VAULT"
```

Capture:

- source Markdown/PDF/summary counts;
- summary quality tiers;
- missing source paths;
- zero-link summaries;
- required-section gaps;
- concept, method, dataset, and synthesis quality tiers;
- duplicate canonical candidates;
- orphan core notes;
- weak core notes;
- broken wikilinks.

If the checker is unavailable, perform the same checks manually with `Grep`,
`Glob`, and file reads.

## Step 2: Audit Source Coverage and Summary Quality

For every source in `10_sources/`:

1. Check whether a matching summary exists in `20_summaries/`.
2. Check whether the summary points to the correct source path.
3. Check whether the summary is detailed and source-grounded.
4. Check whether it links to relevant canonical concept, method, dataset,
   synthesis, and project notes.

Every upgraded summary must include:

- Source paper link/path
- Bibliographic metadata
- Detailed summary
- Research question
- Core argument or contribution
- Methodology
- Datasets/materials used
- Key findings
- Limitations
- Important concepts discussed
- Methods discussed
- Datasets discussed
- Relation to other papers in the vault
- Implications for LLM research or the project domain
- Links to canonical concept, method, dataset, synthesis, and project notes

Do not fabricate claims. If a source is unavailable, unclear, or badly
converted, mark the uncertain part as `needs source verification`.

## Step 3: Canonical Concept Scan

Read all summaries and existing concept notes. Identify important recurring
concepts.

Before creating a concept note:

1. Search `30_concepts/` for exact, alias, and near-duplicate names.
2. Search summaries and synthesis pages for existing terminology.
3. Choose one canonical note.
4. Convert duplicates into aliases or merge candidates; do not delete without
   explicit approval.

Each canonical concept note must include:

- Canonical name
- Aliases/synonyms
- Definition
- Scope boundaries: what the concept is and is not
- Papers that discuss it
- How each paper uses, supports, challenges, or modifies it
- Related concepts
- Methods and datasets commonly associated with it
- Open questions or tensions
- Links back to relevant summaries and synthesis pages

Create a new concept only when it is important and recurring. Otherwise record
it as a watch item in the relevant synthesis or maintenance note.

## Step 4: Canonical Method Scan

Read all summaries and existing method notes. Identify recurring methods,
identification strategies, classification pipelines, validation approaches, and
measurement workflows.

Each canonical method note must include:

- Method name
- Aliases
- What the method does
- When it is used
- Assumptions
- Papers using or discussing it
- Strengths, limitations, and common pitfalls
- Related concepts, datasets, synthesis notes, and projects

Keep exactly one substantive note per method. Merge or alias duplicates.

## Step 5: Canonical Dataset Scan

Read all summaries and existing dataset notes. Identify recurring datasets,
administrative records, survey panels, benchmarks, corpora, and registries.

Each canonical dataset note must include:

- Dataset name
- Aliases
- Description and domain
- Unit of observation
- Key variables
- Papers using or discussing it
- What it is used to evaluate or demonstrate
- Strengths
- Limitations and known biases
- Related methods, concepts, synthesis notes, and projects

Keep exactly one substantive note per dataset. Merge or alias duplicates.

## Step 6: Project and Synthesis Layer

Update project pages in `70_projects/` and current-project `wiki-links.md` when
maintenance changes what a project should retrieve.

Create or update synthesis pages when papers are connected by:

- shared claims or mechanisms;
- disagreements or tensions;
- common concepts, methods, or datasets;
- project-level implications;
- evidence gaps or open questions.

Each synthesis page should:

- compare findings across papers;
- group papers by shared concepts, methods, datasets, claims, or debates;
- identify agreements, disagreements, tensions, and open questions;
- explain how findings build on, contradict, or refine each other;
- link to all relevant summaries, concept notes, method notes, dataset notes,
  project pages, and other synthesis pages;
- include a retrieval map where useful.

## Step 7: Index, Log, and Backlinks

Update:

- `$VAULT/index.md` for new or materially changed maintained notes.
- `$VAULT/log.md` with a dated maintenance entry.
- Project `wiki-links.md`, if present, with changed retrieval targets and sync
  date.

Ensure:

- every summary links to relevant canonical pages;
- every canonical page links back to relevant summaries;
- synthesis pages link both directions where useful;
- aliases point to canonical notes;
- no new broken links are introduced.

## Step 8: Verify and Iterate

Run:

```bash
python wiki_quality_check.py --vault "$VAULT"
```

Do not stop after the first pass if the checker reports:

- B/C/D summaries that should be A-tier;
- missing source paths;
- zero-link summaries;
- required-section gaps;
- C/D concept, method, dataset, or synthesis notes;
- duplicate canonical candidates not explained as aliases;
- orphan core notes;
- weak core notes;
- broken wikilinks.

Iterate until the wiki is verifier-clean or until a real blocker remains.

## Step 9: Report

Report:

- scope maintained;
- counts before and after;
- summaries upgraded or created;
- concepts/methods/datasets created, updated, aliased, or merged;
- synthesis/project/index/log updates;
- final verifier output;
- unresolved issues and source-verification needs.

## Guardrails

Do not:

- rewrite raw sources in `10_sources/` except for explicit source conversion
  performed by `wiki-ingest`;
- invent paper findings;
- create duplicate concept/method/dataset notes;
- create thin stubs just to satisfy a checklist;
- delete notes without explicit approval;
- call the wiki complete while checker failures remain;
- optimize for short summaries over accurate, detailed, connected knowledge.
