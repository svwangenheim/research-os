---
name: wiki-ingest
description: Ingest a source into a thematic research wiki - PDF, markdown, Office doc, or citation string. Runs source placement, summary, concept/method/dataset updates, and log update.
argument-hint: "[--wiki <theme>] [path/to/file.pdf | path/to/file.md | 'Author Year Title']"
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task
---

# Wiki Ingest

Ingest a source into a thematic research wiki. This is the single entry
point for adding any source — PDF, Office doc, markdown, or citation text —
to the persistent, Claude-maintained knowledge base. **This skill writes only
into a thematic wiki, never into `_brain/`** — personal or project-specific
content is out of scope here; that belongs to `/wiki-push` or `/checkpoint`.

## Step 0: Resolve the wiki

1. **Read the registry** `~/.claude/vaults.json` (`theme -> path` map, plus
   `root`). If it exists, use it.
2. **If it does not exist**, fall back to the legacy pointer
   `~/.claude/VAULT_PATH` — treat its target as one flat legacy vault (its
   numbered folders sit directly under that path, no `<theme>/` layer).
3. **If neither exists**: stop and tell the user:
   - Run `/wiki-setup` to create the registry, or
   - Confirm a vault directory is added to this session and create
     `~/.claude/VAULT_PATH` manually.
   Do not hallucinate wiki contents.
4. **Pick the target wiki** (full algorithm:
   `${CLAUDE_PLUGIN_ROOT}/rules/wiki-integration.md` §"Picking the target
   wiki — no project required"): `--wiki <theme>` argument (parsed out of
   `$ARGUMENTS` before the file path/citation) > current project's
   `passport.yaml` `meta.main_wiki` > a `.research-os-wiki` pin file in the
   cwd (`wiki:` value) > the registry's only wiki > ask the user which
   registered wiki to ingest into (list themes + descriptions, wait for the
   answer, then offer to write the pin file so this folder doesn't ask
   again).
5. Resolve `$WIKI` = the chosen wiki's absolute path, and `$VAULT_ROOT` =
   its parent directory (where the shared `_templates/`, `index.md`, and
   `log.md` live). Under the legacy-pointer fallback, `$WIKI` and
   `$VAULT_ROOT` are the same path.

If the vault cannot be confirmed: **stop. Do not hallucinate wiki contents.**

## Identify Input Type

The remainder of `$ARGUMENTS` (after any `--wiki <theme>`) is one of:
- Path ending in `.pdf` → mechanical extraction + mandatory cleanup (Step 1)
- Path ending in `.docx`/`.pptx`/`.xlsx`/other markitdown-supported format →
  markitdown conversion (Step 1c)
- Path ending in `.md` → copy directly to the wiki (Step 2)
- Plain text (citation string) → create an inbox stub (Step 3, then stop)

## Step 1: PDF Conversion — mechanical extraction + mandatory cleanup

High-fidelity local extraction, then a **mandatory** Claude normalization
pass. A raw mechanical dump is never treated as the final `10_sources/*.md`
file for a PDF.

### 1a. Mechanical extraction (`pymupdf4llm`)

Chosen over `docling` because it needs no PyTorch/ML runtime — it's a thin
layer over PyMuPDF's own layout engine, fast, and good enough at structure
detection (headings, paragraphs, tables-as-pipe-markdown, images) that the
mandatory cleanup pass in 1b can fix its remaining rough edges (mainly:
merged table cells get duplicated, not properly spanned).

Check it's installed:
```bash
python -c "import pymupdf4llm" 2>/dev/null && echo OK || echo MISSING
```
If **missing**, print and stop:
```
pymupdf4llm is not installed.
Run: pip install pymupdf4llm
Then re-run: /wiki-ingest [path/to/file.pdf]
If you already have a markdown version, pass that path instead.
```

If installed, convert:
```bash
CLEAN=$(basename "$PDF_PATH" .pdf | tr '[:upper:]' '[:lower:]' | tr ' ' '_')
python3 -c "
import sys
import pymupdf4llm
from pathlib import Path

pdf_path, out_path = sys.argv[1], sys.argv[2]
md = pymupdf4llm.to_markdown(pdf_path, table_strategy='lines_strict')
Path(out_path).write_text(md, encoding='utf-8')
print(f'{len(md.split())} words extracted from {pdf_path}')
" "$PDF_PATH" "$WIKI/10_sources/$CLEAN.md"
```

If the reported word count looks implausibly low for the page count (a rough
rule of thumb: under ~50 words/page suggests a scanned, image-only PDF with
no embedded text layer), retry with OCR:
```bash
python3 -c "
import sys
import pymupdf4llm
from pathlib import Path

pdf_path, out_path = sys.argv[1], sys.argv[2]
md = pymupdf4llm.to_markdown(pdf_path, table_strategy='lines_strict', force_ocr=True, ocr_language='eng')
Path(out_path).write_text(md, encoding='utf-8')
" "$PDF_PATH" "$WIKI/10_sources/$CLEAN.md"
```
This requires Tesseract OCR on the system. If it fails because Tesseract is
missing, report the exact error and ask the user to install Tesseract (or
supply a text-layer PDF) rather than silently accepting a near-empty file.

Never delete the original PDF — copy it alongside its markdown twin into
`$WIKI/10_sources/` (or leave it wherever it already is and just record the
path). The PDF is the source of truth if re-conversion is ever needed
(`/wiki-maintain`'s re-conversion mode, below).

### 1b. Mandatory Claude normalization pass

Read the freshly written `$WIKI/10_sources/$CLEAN.md` in full, then edit it
**in place** (Edit tool — do not create a second file) to:

1. **Strip boilerplate** — repeated journal name/volume/issue headers,
   "Downloaded from ..." lines, DOI/copyright footers, received/accepted
   date stamps recurring on every page, running headers/footers, bare page
   numbers, bare line numbers.
2. **Reflow columns** — `pymupdf4llm` handles most two-column academic
   layouts correctly, but check for leftover interleaving (short fragments
   that don't form a sentence read top-to-bottom); re-order into a single
   reading-order flow if you find it.
3. **Fix heading hierarchy** — convert misdetected `**Bold Text**`
   paragraph-starts into real `#`/`##`/`###` headings for actual sections
   (Abstract, Introduction, Data, Methodology, Results, Discussion,
   References, Appendix); demote anything wrongly promoted to a heading.
4. **Rebuild tables** — `table_strategy='lines_strict'` renders plain
   pipe-delimited Markdown with no merged-cell syntax (a merged header gets
   duplicated across the columns it spans). Compare each extracted table
   against the likely source layout and rewrite as a clean GFM table; note a
   spanning header in the cell text instead of silently duplicating it.
5. **De-hyphenate** — rejoin PDF line-wrap hyphenation (e.g. `endog-\nenous`
   → `endogenous`).
6. **Preserve figure/table captions** — keep `Figure N: ...` / `Table N: ...`
   caption text attached to where it appeared, even though the graphic
   itself is not preserved as an image.
7. **Handle OCR garbage conservatively** — remove isolated noise characters
   and repeated symbol runs that are clearly extraction artifacts, but never
   delete or guess at real content. Mark genuinely illegible passages as
   `[illegible in source]` instead of inventing text.

For unusually long PDFs (60+ pages), it is fine to normalize section-by-
section across multiple edits rather than one pass. This step is not
optional — do not proceed to Step 4 on an unreviewed mechanical dump.

### 1c. Non-PDF documents (docx, pptx, xlsx, html, ...) — `markitdown`

`markitdown` remains the converter for everything that is **not** a PDF (its
PDF backend has no equivalent of the mandatory cleanup pass above, so PDFs
always go through 1a/1b instead).
```bash
python -m markitdown --version 2>/dev/null || markitdown --version 2>/dev/null
```
If **not installed**, print and stop:
```
markitdown is not installed.
Run: pip install 'markitdown[all]'
Then re-run: /wiki-ingest [path/to/file]
```
If installed:
```bash
python -m markitdown "$SOURCE_PATH" -o "$WIKI/10_sources/$CLEAN.md"
```
Give the result a lighter read-through before treating it as final — at
minimum, strip boilerplate/headers-footers (1b.1) and de-hyphenate (1b.5).

If conversion fails at any point, report the error and stop. Do not proceed
with a partial file.

## Step 2: Place Markdown in Wiki

If the input was `.md` and is not already in `$WIKI/10_sources/`, copy it
there. If the input was a PDF/docx/etc., the file is already in
`$WIKI/10_sources/` from Step 1.

## Step 3: Citation Stub (plain text only)

If the input is plain text (no file extension), create a stub note:
- File: `$WIKI/00_inbox/[slugified-title].md`
- Content: the citation text as a note header, with a blank summary section
- Append a log entry: `## [YYYY-MM-DD] ingest | <theme> | inbox | [citation]`
- Tell the user: "Stub created in `<theme>/00_inbox/`. Add the source file
  later and re-run `/wiki-ingest` to complete ingestion."
- **Stop here** — do not proceed to Step 4 for stubs.

## Step 4: Run the Wiki Ingest Workflow

Read `$VAULT_ROOT/CLAUDE.md` and `${CLAUDE_PLUGIN_ROOT}/rules/wiki-integration.md`
for the ingest rules. Execute in order.

Mandatory quality standard for this workflow:
- Create or upgrade a detailed source summary, not a short abstract. The
  summary must include source path, bibliographic metadata, detailed
  summary, research question, core contribution, methodology,
  datasets/materials, key findings, limitations, concepts, methods,
  datasets, relation to other papers in this wiki, project implications, and
  links to canonical pages.
- Mark unclear or unavailable source claims as `needs source verification`.
  Do not infer findings from title or citation alone.
- Before creating any concept, method, or dataset note, search aliases and
  near-duplicates. Keep one substantive canonical note per concept, method,
  or dataset; mark duplicates as aliases or merge candidates.
- Update `$WIKI/90_synthesis/` when the source changes a claim, mechanism,
  comparison, debate, or theme-internal interpretation — **only within this
  theme**; cross-theme or personal implications are out of scope for
  wiki-ingest (that's `/wiki-push` routing up into `_brain/synthesis/`).
- Before reporting success, run
  `python "${CLAUDE_PLUGIN_ROOT}/scripts/wiki_quality_check.py" --vault "$WIKI"`
  when available, or manually report summary depth, required-section gaps,
  missing `source_files`, duplicate canonical candidates, weak/orphan links,
  and broken wikilinks.

1. **Read the raw source** from `$WIKI/10_sources/[filename].md`.

2. **Create a source summary** in `$WIKI/20_summaries/`:
   - Use the template at `$VAULT_ROOT/_templates/source_summary_template.md`
   - Filename: `[author-year]-[short-title].md`
   - Populate: title, authors, year, doi, journal, abstract (1-3 plain-text
     sentences -- the source's own abstract if published, else a faithful
     synopsis; this is what project dashboards show in the Literature panel,
     read live from this frontmatter), proximity, related_concepts
     (wikilinks to `30_concepts/`), related_methods, related_datasets,
     summary, research question, method/identification, main findings,
     limitations, relevance for ongoing work.

3. **Update relevant wiki pages** — check each folder and update rather than
   create when possible:
   - `$WIKI/30_concepts/` — new or existing concept pages mentioned in the
     source
   - `$WIKI/40_methods/` — method or identification strategy used
   - `$WIKI/50_datasets/` — datasets used in the source
   - `$WIKI/60_people_institutions/` — notable authors or institutions
   - **Concept-creation rule:** for each concept mentioned in the summary
     that does not have a page in `$WIKI/30_concepts/`, create a new concept
     page using `$VAULT_ROOT/_templates/concept_template.md`. Add the new
     summary to `related_summaries:` in the concept page. Add the concept
     wikilink to `related_concepts:` in the summary frontmatter.
   - There is no `70_projects/` folder in the wiki — project-specific
     relevance goes in the summary's own "Implications" section, or (if it's
     worth carrying forward) into `_brain/projects/<slug>.md` via
     `/wiki-push`, never into the wiki itself.

4. **`$VAULT_ROOT/index.md`** — no manual edit needed. It is Dataview-driven
   and picks up the new summary/concept/method/dataset page automatically as
   long as it was created in the right numbered folder under a wiki already
   listed in the index's `FROM` clauses (if this is a brand-new wiki, that's
   `/add-thematic-wiki`'s job, not this skill's).

5. **Append to `$VAULT_ROOT/log.md`**, theme-prefixed:
   ```
   ## [YYYY-MM-DD] ingest | <theme> | [source title]
   [One-line description of what was added and which pages were updated.]
   ```

6. **Check `$WIKI/90_synthesis/`** — if the source materially changes the
   picture in its topic area **within this theme**, flag or update the
   relevant synthesis page. Synthesis stays proposal-only: flag it, do not
   auto-write it (`rules/wiki-integration.md`).

7. **Council-gate the canonical pages.** The `20_summaries/` note is the
   direct product of the ingest and lands as it always has. But any
   *canonical* page this ingest would create or extend — in `30_concepts/`,
   `40_methods/`, `50_datasets/`, `60_people_institutions/` — goes through
   the five-critic council first, exactly as in `/wiki-push` Step 3b: five
   parallel `Task` calls with `subagent_type=wiki-promotion-council` and
   `context: fork`, one per role, then 5/5 or 4/5 writes, 3/5 proposes, and
   2-or-fewer discards with the reason logged.

   The canonicity critic earns its place here: a new source is the most
   common moment for a second page on a concept that already has one.

8. **Refresh the catalogue and commit.** `_map.md` is what `/wiki-pull` and
   the SessionStart hook read first, so an ingest that skips it leaves the
   fast path stale:
   ```bash
   python "${CLAUDE_PLUGIN_ROOT}/scripts/generate_wiki_moc.py" --vault "$WIKI"
   git -C "$VAULT_ROOT" add <touched pages> log.md _map.md
   git -C "$VAULT_ROOT" commit -m "wiki: ingest <source title> (<theme>)"
   ```
   Use the `wiki(auto):` prefix instead for any page the council auto-wrote,
   so `--review-auto` can find it. Stage specific files — blanket staging is
   blocked by the git guardrails hook.

## Step 5: Update Project Bridge

If `wiki-links.md` exists in the current project:
- Add the new summary to the "Papers / summaries" section
- Note any new concept or method pages created
- Update the "Last wiki sync" date

## Step 6: Report

Summarize what was done:
- Wiki: `<theme>`
- Source file placed at: `[path]`
- Summary created at: `[path]`
- Pages updated: `[list]`
- Log: updated (index.md needs no manual edit)

## Guardrails

Do not:
- Write into `_brain/` — this skill's output is theme-scoped, objective
  knowledge only; personal/project-specific content routes through
  `/wiki-push` or `/checkpoint` instead
- Invent wiki content when the wiki is not accessible
- Create duplicate pages without checking first
- Dump raw source text without synthesis into summaries
- Treat a raw `pymupdf4llm`/`markitdown` conversion as final without the
  Step 1b cleanup pass (PDFs) or the lighter equivalent (non-PDF)
- Create many thin stub pages — prefer fewer, richer notes
- Silently overwrite important interpretations — flag contradictions
  explicitly
