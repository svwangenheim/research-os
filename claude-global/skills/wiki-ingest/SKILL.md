---
name: wiki-ingest
description: >
  Ingest a source into the global research wiki. Accepts a PDF (auto-converts
  with markitdown), a markdown file, or a citation string. Runs the full vault
  ingest workflow: source placement, summary creation, concept/method/dataset
  page updates, index and log updates. Use whenever new literature is identified
  as worth preserving. The librarian offers this automatically after each
  literature search.
argument-hint: "[path/to/file.pdf | path/to/file.md | 'Author Year Title']"
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

# Wiki Ingest

Ingest a source into the global research wiki. This is the single entry point
for adding any source — PDF, markdown, or citation text — to the persistent
knowledge base.

## Preconditions

**Step 0: Find the vault**

The vault is made available via `additionalDirectories` in `~/.claude/settings.json`
or via `claude --add-dir /path/to/vault`.

To locate the vault's absolute path for Bash commands (markitdown needs it):
1. Check for `~/.claude/VAULT_PATH` — if it exists, read the path from it
2. If not found: stop and tell the user:
   - Confirm the vault is added to this session
   - Create `~/.claude/VAULT_PATH` with the absolute path (see `claude-global/settings-snippets/global-settings.md`)

If the vault cannot be confirmed: **stop. Do not hallucinate wiki contents.**

## Identify Input Type

`$ARGUMENTS` is one of:
- Path ending in `.pdf` → needs markitdown conversion (Step 1)
- Path ending in `.md` → copy directly to vault (Step 2)
- Plain text (citation string) → create inbox stub (Step 3, then stop)

## Step 1: PDF Conversion

Check if markitdown is installed:
```bash
python -m markitdown --version 2>/dev/null || markitdown --version 2>/dev/null
```

If **not installed**: print the following and stop:
```
markitdown is not installed.
Run: pip install 'markitdown[pdf]'
Then re-run: /wiki-ingest [path/to/file.pdf]
If you already have a markdown version, pass that path instead.
```

If installed, convert:
```bash
VAULT=$(cat ~/.claude/VAULT_PATH)
CLEAN=$(basename "$PDF_PATH" .pdf | tr '[:upper:]' '[:lower:]' | tr ' ' '_')
python -m markitdown "$PDF_PATH" -o "$VAULT/10_sources/$CLEAN.md"
```

If conversion fails, report the error and stop. Do not proceed with a partial file.

## Step 2: Place Markdown in Vault

If the input was `.md` and is not already in `vault/10_sources/`:
- Copy it to `$VAULT/10_sources/`

If the input was a `.pdf`, the file is already in `$VAULT/10_sources/` from Step 1.

## Step 3: Citation Stub (plain text only)

If the input is plain text (no file extension), create a stub note:
- File: `$VAULT/00_inbox/[slugified-title].md`
- Content: The citation text as a note header, with a blank summary section
- Append a log entry: `## [YYYY-MM-DD] ingest | inbox | [citation]`
- Tell the user: "Stub created in vault/00_inbox/. Add the source file later and re-run /wiki-ingest to complete ingestion."
- **Stop here** — do not proceed to the ingest workflow for stubs

## Step 4: Run the Vault Ingest Workflow

Read `$VAULT/CLAUDE.md` for the ingest rules. Execute in order:

Mandatory quality standard for this workflow:
- Create or upgrade a detailed source summary, not a short abstract. The
  summary must include source path, bibliographic metadata, detailed summary,
  research question, core contribution, methodology, datasets/materials, key
  findings, limitations, concepts, methods, datasets, relation to other vault
  papers, project implications, and links to canonical pages.
- Mark unclear or unavailable source claims as `needs source verification`.
  Do not infer findings from title or citation alone.
- Before creating any concept, method, or dataset note, search aliases and
  near-duplicates. Keep one substantive canonical note per concept, method, or
  dataset; mark duplicates as aliases or merge candidates.
- Update synthesis pages when the source changes a claim, mechanism,
  comparison, debate, or project-level interpretation.
- Before reporting success, run `python wiki_quality_check.py --vault "$VAULT"`
  from the Research-OS root when available, or manually report summary depth,
  required-section gaps, missing `source_files`, duplicate canonical candidates,
  weak/orphan links, broken wikilinks, and whether `index.md`, `log.md`, and
  project `wiki-links.md` were updated.

1. **Read the raw source** from `$VAULT/10_sources/[filename].md`

2. **Create a source summary** in `$VAULT/20_summaries/`
   - Use the template at `$VAULT/_templates/source_summary_template.md`
   - Filename: `[author-year]-[short-title].md`
   - Populate: title, authors, year, summary, research question, method/identification,
     main findings, limitations, relevance for ongoing work

3. **Update relevant wiki pages** — check each folder and update rather than create when possible:
   - `$VAULT/30_concepts/` — new or existing concept pages mentioned in the source
   - `$VAULT/40_methods/` — method or identification strategy used
   - `$VAULT/50_datasets/` — datasets used in the source
   - `$VAULT/60_people_instructions/` — notable authors or institutions
   - `$VAULT/70_projects/` — if the source directly relates to an active project

4. **Update `$VAULT/index.md`** — add the new summary under the Summaries section

5. **Append to `$VAULT/log.md`**:
   ```
   ## [YYYY-MM-DD] ingest | [source title]
   [One-line description of what was added and which pages were updated]
   ```

6. **Check `$VAULT/90_synthesis/`** — if the source materially changes the picture
   in its topic area, flag or update the relevant synthesis page

## Step 5: Update Project Bridge

If `wiki-links.md` exists in the current project:
- Add the new summary to the "Papers / summaries" section
- Note any new concept or method pages created
- Update the "Last wiki sync" date

## Step 6: Report

Summarize what was done:
- Source file placed at: `[path]`
- Summary created at: `[path]`
- Pages updated: `[list]`
- Index and log: updated

## Guardrails

Do not:
- Invent wiki content when the vault is not accessible
- Create duplicate pages without checking first
- Dump raw source text without synthesis into summaries
- Create many thin stub pages — prefer fewer, richer notes
- Silently overwrite important interpretations — flag contradictions explicitly
