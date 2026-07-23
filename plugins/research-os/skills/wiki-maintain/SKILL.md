---
name: wiki-maintain
description: >
  Audit and remediate one or all registered thematic research wikis until
  they meet the established A-tier standards for source summaries, canonical
  concepts, methods, datasets, synthesis pages, links, and verification. Also
  detects and re-converts poorly-extracted PDF-to-markdown source twins. Use
  when the user asks to improve the wiki(s), check wiki quality, canonicalize
  concepts/methods/datasets, update synthesis, fix a garbled source
  conversion, or make wiki-pull retrieval reliable.
argument-hint: "[--wiki <theme>] [optional scope: all | summaries | concepts | methods | datasets | synthesis | reconvert | path]"
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

# Wiki Maintain

Audit and remediate the research wiki(s) as a whole. This skill is the
whole-wiki counterpart to `wiki-ingest`: `wiki-ingest` processes one source;
`wiki-maintain` checks and improves an entire maintained wiki (or every
registered wiki) until the established standards are met. It never touches
`_brain/` — that layer is human-owned.

## Step 0: Resolve scope

1. **Read the registry** `~/.claude/vaults.json`. If it exists, use it.
2. **If it does not exist**, check whether `vault/index.md` (or
   `vault/CLAUDE.md`) exists in the current workspace as a single legacy
   vault, or fall back to `~/.claude/VAULT_PATH`.
3. **If still not found**: stop and tell the user to run `/wiki-setup`, or
   confirm a vault is added to this session. Do not hallucinate wiki
   contents.
4. **Determine which wiki(s) to audit**:
   - `--wiki <theme>` argument → that one wiki only.
   - Else, no `--wiki` given → **audit every wiki in the registry** (this is
     the default — wider than a single-project default, because maintenance
     is a whole-knowledge-base concern, not a per-project one).
   - Legacy `VAULT_PATH` fallback → there is only one vault; use it.

## Identify Scope (within the chosen wiki/wikis)

The rest of `$ARGUMENTS` (after any `--wiki <theme>`) is optional:

- `all` or empty → audit and remediate the whole wiki.
- `summaries` → focus on `20_summaries/`.
- `concepts` → focus on `30_concepts/`.
- `methods` → focus on `40_methods/`.
- `datasets` → focus on `50_datasets/`.
- `synthesis` → focus on `90_synthesis/`.
- `reconvert` → run only the re-conversion pass (below), skip the
  canonicalization steps.
- path → focus on that file or folder, then check affected backlinks.

Even for a narrow scope, check whether changes create missing backlinks,
duplicates, broken links, or synthesis update needs.

## Step 1: Run the Quality Baseline

```bash
# single wiki:
python "${CLAUDE_PLUGIN_ROOT}/scripts/wiki_quality_check.py" --vault "$WIKI"
# every registered wiki (default, no --wiki given):
python "${CLAUDE_PLUGIN_ROOT}/scripts/wiki_quality_check.py" --root "$VAULT_ROOT"
```

Capture, per wiki:
- source Markdown/PDF/summary counts;
- required-frontmatter-section gaps and thin summaries;
- duplicate canonical candidates;
- orphan and weakly-linked notes;
- broken wikilinks;
- index/log staleness.

If the checker is unavailable, perform the same checks manually with `Grep`,
`Glob`, and file reads.

## Step 2: Re-conversion Pass — detect and fix garbled source conversions

For every file in `$WIKI/10_sources/*.md`, screen for signs of a poor PDF
extraction:

- **No markdown headings at all** in a document long enough to obviously
  have sections (a >2-page academic paper with zero `#`/`##` lines).
- **Excessive very-short lines** — a high fraction of lines under ~4 words,
  which usually means column interleaving or line-by-line OCR dumping
  rather than reflowed paragraphs.
- **Broken or missing table syntax where a table is likely** — runs of
  numbers/percentages separated by inconsistent whitespace instead of `|`
  pipes, immediately after a caption-like line such as "Table 3".
  Also flag pipe tables where every row has a different column count.
- **OCR garbage patterns** — repeated single-character "words", strings of
  mixed symbols/digits with no surrounding real words, or long runs of `�`/
  replacement characters.

For each file that trips these heuristics:
1. Look for the original PDF next to it in `$WIKI/10_sources/` (same
   basename, `.pdf` extension) or referenced in the corresponding summary's
   `source_files:` frontmatter.
2. If found, re-run the mechanical extraction step from `wiki-ingest`
   (`pymupdf4llm`, Step 1a — retry with `force_ocr=True` if the first pass is
   still thin), overwrite the `.md` twin, then run the **mandatory Claude
   normalization pass** (`wiki-ingest` Step 1b) on the fresh extraction.
3. If no original PDF can be found, report the file as `needs original PDF
   to re-convert` — do not attempt to hand-clean a garbled OCR dump without
   the source to check against.
4. After re-conversion, re-check whether the summary that cites this source
   (`related` via `source_files:`) still accurately reflects the corrected
   text; flag it for review if the correction changes anything material.

## Step 3: Audit Source Coverage and Summary Quality

For every source in `$WIKI/10_sources/`:

1. Check whether a matching summary exists in `$WIKI/20_summaries/`.
2. Check whether the summary points to the correct source path.
3. Check whether the summary is detailed and source-grounded.
4. Check whether it links to relevant canonical concept, method, dataset,
   and synthesis notes.

Every upgraded summary must include: source paper link/path; bibliographic
metadata; detailed summary; research question; core argument or
contribution; methodology; datasets/materials used; key findings;
limitations; important concepts/methods/datasets discussed; relation to
other papers in this wiki; and links to canonical concept, method, dataset,
and synthesis notes.

Do not fabricate claims. If a source is unavailable, unclear, or badly
converted, mark the uncertain part as `needs source verification` (or route
it through Step 2 first if it's a conversion problem, not a content one).

## Step 4: Canonical Concept Scan

Read all summaries and existing concept notes in `$WIKI/30_concepts/`.
Identify important recurring concepts.

Before creating a concept note:
1. Search `$WIKI/30_concepts/` for exact, alias, and near-duplicate names.
2. Search summaries and synthesis pages for existing terminology.
3. Choose one canonical note.
4. Convert duplicates into aliases or merge candidates; do not delete
   without explicit approval.

Each canonical concept note must include: canonical name; aliases/synonyms;
definition; scope boundaries; papers that discuss it and how; related
concepts; related methods/datasets; open questions/tensions; links back to
relevant summaries and synthesis pages.

Create a new concept only when it is important and recurring. Otherwise
record it as a watch item in the relevant synthesis note.

## Step 5: Canonical Method Scan

Read all summaries and existing method notes in `$WIKI/40_methods/`.
Identify recurring methods, identification strategies, classification
pipelines, validation approaches, and measurement workflows.

Each canonical method note must include: method name; aliases; what it
does; when it is used; assumptions; papers using or discussing it;
strengths, limitations, and common pitfalls; related concepts/datasets/
synthesis notes.

Keep exactly one substantive note per method. Merge or alias duplicates.

## Step 6: Canonical Dataset Scan

Read all summaries and existing dataset notes in `$WIKI/50_datasets/`.
Identify recurring datasets, administrative records, survey panels,
benchmarks, corpora, and registries.

Each canonical dataset note must include: dataset name; aliases;
description and domain; unit of observation; key variables; papers using or
discussing it; what it is used to evaluate or demonstrate; strengths;
limitations and known biases; related methods/concepts/synthesis notes.

Keep exactly one substantive note per dataset. Merge or alias duplicates.

## Step 7: Synthesis Layer (theme-internal only)

Create or update `$WIKI/90_synthesis/` pages when papers are connected by
shared claims/mechanisms, disagreements/tensions, common concepts/methods/
datasets, or evidence gaps/open questions — **within this one theme**. If
maintenance surfaces a cross-theme or personal insight instead, do not put
it here — flag it in the report so the user can route it through
`/wiki-push` into `_brain/synthesis/`.

Each synthesis page should: compare findings across papers; group papers by
shared concepts/methods/datasets/claims/debates; identify agreements,
disagreements, tensions, and open questions; explain how findings build on,
contradict, or refine each other; link to all relevant summaries and
canonical pages; include a retrieval map where useful.

Also refresh the calling project's `wiki-links.md`, if one exists and this
maintenance pass changed what it should retrieve.

## Step 8: Log and Backlinks

Update `$VAULT_ROOT/log.md` with a dated, theme-prefixed maintenance entry:
```
## [YYYY-MM-DD] maintain | <theme> | [short summary of what changed]
```
No manual `index.md` edit is needed — it is Dataview-driven.

Ensure: every summary links to relevant canonical pages; every canonical
page links back to relevant summaries; synthesis pages link both
directions where useful; aliases point to canonical notes; no new broken
links are introduced.

## Step 9: Verify and Iterate

```bash
python "${CLAUDE_PLUGIN_ROOT}/scripts/wiki_quality_check.py" --vault "$WIKI"
```

Do not stop after the first pass if the checker reports: thin or
required-section-gapped summaries; duplicate canonical candidates not
explained as aliases; orphan or weakly-linked notes; broken wikilinks; or
index/log staleness. Iterate until the wiki is verifier-clean or until a
real blocker remains (e.g. a garbled source with no recoverable PDF).

## Step 10: Report

Report, per wiki audited:
- scope maintained;
- counts before and after;
- re-conversions attempted, succeeded, or blocked (missing original PDF);
- summaries upgraded or created;
- concepts/methods/datasets created, updated, aliased, or merged;
- synthesis/log updates;
- final verifier output;
- unresolved issues and source-verification needs;
- anything flagged for `_brain/` routing that this skill correctly left
  untouched.

## Guardrails

Do not:
- write into `_brain/` — that layer is human-owned
- rewrite raw sources in `$WIKI/10_sources/` except via the explicit
  re-conversion pipeline in Step 2 (never hand-edit a garbled conversion
  without re-running the pipeline against the original PDF)
- invent paper findings
- create duplicate concept/method/dataset notes
- create thin stubs just to satisfy a checklist
- delete notes without explicit approval
- call a wiki complete while checker failures remain
- optimize for short summaries over accurate, detailed, connected knowledge
