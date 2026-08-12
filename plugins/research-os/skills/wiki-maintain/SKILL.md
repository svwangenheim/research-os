---
name: wiki-maintain
description: Audit and remediate registered thematic wikis to A-tier standards - summaries, canonical concepts, methods, datasets, synthesis, links. Also re-converts garbled PDF twins.
argument-hint: "[--wiki <theme>] [--review-auto [--since <date>]] [--synthesize] [optional scope: all | summaries | concepts | methods | datasets | synthesis | reconvert | path]"
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task
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
# every registered wiki + the _brain/ personal layer (default, no --wiki given):
python "${CLAUDE_PLUGIN_ROOT}/scripts/wiki_quality_check.py" --root "$VAULT_ROOT"

# regenerate the Claude-readable map(s) so /wiki-pull reads a current index:
python "${CLAUDE_PLUGIN_ROOT}/scripts/generate_wiki_moc.py" --vault "$WIKI"      # single wiki
python "${CLAUDE_PLUGIN_ROOT}/scripts/generate_wiki_moc.py" --root "$VAULT_ROOT" # all wikis
```

Capture, per wiki:
- source Markdown/PDF/summary counts;
- required-frontmatter-section gaps and thin summaries;
- duplicate canonical candidates;
- orphan and weakly-linked notes;
- broken wikilinks;
- index/log staleness.

In `--root` mode the checker also reports the `_brain/` personal layer
(frontmatter gaps, catalog-invisible project notes, stale active projects).
Those findings are **detection only** — surface them for the human or the
owning skill (`/checkpoint` maintains project notes); this skill never
remediates or writes into `_brain/`.

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

## Step 3b: Gap-detection — sources cited but never ingested

Step 3 audits **forward**: for a source already in `10_sources/`, is it
summarized well? This step audits **backward**: is there a source that
should be in `10_sources/` at all, but isn't?

Added 2026-08-12, from the first `/workflow-audit`'s own refinement of the
wiki-push backlog problem: *"I should be reminded to search for missing
papers and include them in the sources folder and to run wiki-ingest more
often"* — a reliability gap, not a missing capability (`/wiki-ingest`
already exists; nothing was prompting its use for citations that never
made it in).

For every project whose `main_wiki` resolves to this wiki:

1. Read `passport.yaml`'s `literature_corpus` — every entry with a
   `citation_status` of `relevant`, `intended`, or `cited`.
2. For each, check whether `wiki_path` is set **and** resolves to a real
   file under `10_sources/` or `20_summaries/`.
3. Flag every entry that is cited/discussed (per step 1) but has no
   resolving `wiki_path` — this is a paper the project is relying on that
   the wiki does not actually have.
4. Cross-check `00_admin/process/journal.md` and `03_analysis/strategy/`
   for author-year mentions (`Author et al. YYYY` / `(Author, YYYY)`
   patterns) that don't appear anywhere in `literature_corpus` at all —
   these are citations that were never even logged, the earlier stage of
   the same gap.

For each flag, do not silently ingest — ingestion is a judgment call about
scope and placement (see `/wiki-ingest`'s own guardrails). **Surface the gap
in this pass's report** (Step 10) and hand off to `/wiki-ingest` per source,
by name, so the human sees exactly what's missing before it's added.

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

### `--synthesize`: propose pages for the thinnest layer

`90_synthesis/` sits fifth in the `/wiki-pull` reading order — above the
summaries and just under the canonical pages — and it is reliably the emptiest
folder in the vault. That inverts the retrieval design: the tier meant to be
read first has the least in it.

With `--synthesize`, find clusters worth a page: **five or more summaries
sharing two or more concepts, methods, or datasets**, or a set of papers whose
findings disagree. For each cluster, propose (do not write) a synthesis page
with a working title, the member summaries, and the specific tension or
convergence that justifies it.

**Propose only.** Synthesis is interpretation, and interpretation stays outside
the auto-write blast radius no matter how strong the clustering signal
(`rules/wiki-integration.md`). The user picks which proposals become pages.

While here, `60_people_institutions/` is usually empty too and is cheaper to
fill: the authors and affiliations already sit in `20_summaries/` frontmatter,
so offer to generate entity pages from what is on disk.

## Step 7b: `--review-auto` — audit what was written without asking

Auto-write is only safe because it is reviewable. This mode is the review.

1. Find every auto-written change: `git -C "<VAULT_ROOT>" log --oneline --grep="^wiki(auto):"` (add `--since` when given), and every `## Changelog` line tagged `auto`.
2. Present them grouped by note, each with its council tally, the triggering session, and a one-line diff summary.
3. Flag for closer attention: anything that passed **4 of 5** (a critic objected and was outvoted), anything appended to a page that has taken three or more auto-writes in the window (a page accreting without a human ever reading it), and any contradiction appended without a matching source.
4. Offer to revert a batch: `git -C "<VAULT_ROOT>" revert <sha>`.

**Read the tallies as calibration data, not just as a log.** If the 4-of-5
writes are consistently the ones you would have rejected, the threshold is too
loose — raise it to 5-of-5 only. If almost nothing clears the council, the
candidates are under-evidenced and the fix is upstream in `/wiki-ingest`, not a
lower bar here.

## Step 8: Log and Backlinks

Update `$VAULT_ROOT/log.md` with a dated, theme-prefixed maintenance entry:
```
## [YYYY-MM-DD] maintain | <theme> | [short summary of what changed]
```
No manual `index.md` edit is needed — it is Dataview-driven. Regenerate the Claude-readable `_map.md` (`generate_wiki_moc.py`) so the fast index reflects the changes.

Ensure: every summary links to relevant canonical pages; every canonical
page links back to relevant summaries; synthesis pages link both
directions where useful; aliases point to canonical notes; no new broken
links are introduced.

## Step 9: Verify and Iterate

```bash
python "${CLAUDE_PLUGIN_ROOT}/scripts/wiki_quality_check.py" --vault "$WIKI"
python "${CLAUDE_PLUGIN_ROOT}/scripts/generate_wiki_moc.py" --vault "$WIKI"
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
- **gaps found (Step 3b): cited/discussed sources with no resolving
  `wiki_path`, named per project and per source — the hand-off list for
  `/wiki-ingest`, not something this pass ingests itself;**
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
