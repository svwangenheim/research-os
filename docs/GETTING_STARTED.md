# Getting Started with Research-OS

A personal research operating system that combines a persistent knowledge wiki
with a full AI-assisted research pipeline for academic papers.

---

## What This Is

Research-OS has three independent components:

**`vault/`** — your global research wiki. Lives here permanently. Shared across
all your research projects. Structured by content type: source summaries,
concepts, methods, datasets, entities, project notes, and syntheses. Claude
maintains this wiki; you curate sources and direct the work.

**`claude-global/`** — global Claude Code configuration. Install once into
`~/.claude/` and the wiki skills become available in every Claude session,
regardless of which project you're working on.

**`project-starter/clo-author-template/`** — the project template. Copy it
anywhere on your filesystem to start a new research project. Each project is
independent and self-contained. Projects connect to the wiki via `wiki-links.md`.

```
Research-OS/
├── vault/                  ← global wiki (never move this)
├── claude-global/          ← install once into ~/.claude/
├── project-starter/
│   └── clo-author-template/  ← copy to start a new project
└── docs/
    └── GETTING_STARTED.md    ← this file
```

Your research projects live **outside** Research-OS, anywhere on your filesystem:
```
~/projects/
├── paper-2025-innovation/   ← your project (copied from template)
├── paper-2026-inequality/   ← another project
└── ...
```

---

## One-Time Setup

Do this once before using the system for the first time.

### Step 1: Install wiki skills globally

From the Research-OS root directory:

```bash
mkdir -p ~/.claude/agents ~/.claude/skills

cp claude-global/agents/wiki-librarian.md ~/.claude/agents/
cp -r claude-global/skills/wiki-pull   ~/.claude/skills/
cp -r claude-global/skills/wiki-push   ~/.claude/skills/
cp -r claude-global/skills/wiki-ingest ~/.claude/skills/
```

After this, `/wiki-pull`, `/wiki-push`, `/wiki-ingest`, and the `wiki-librarian`
agent are available in every Claude Code session.

### Step 2: Configure the vault path

**Create `~/.claude/VAULT_PATH`** — the file that wiki-ingest uses to find the vault for Bash commands:

```bash
# Windows (Git Bash):
echo 'C:/Users/YOUR_USERNAME/Research-OS/vault' > ~/.claude/VAULT_PATH

# Mac/Linux:
echo '/Users/YOUR_USERNAME/Research-OS/vault' > ~/.claude/VAULT_PATH
```

**Add to `~/.claude/settings.json`** — makes the vault available automatically in every session:

```json
{
  "permissions": {
    "allow": [
      "Bash(markitdown *)",
      "Bash(python -m markitdown *)"
    ],
    "additionalDirectories": [
      "C:/Users/YOUR_USERNAME/Research-OS/vault"
    ]
  }
}
```

Replace the path with your actual vault location. If `~/.claude/settings.json`
already exists, merge these entries into the existing `permissions` section.

See `claude-global/settings-snippets/global-settings.md` for more detail.

### Step 3: Install markitdown

```bash
pip install 'markitdown[pdf]'
```

Required for converting PDF papers to markdown when ingesting into the wiki.

### Step 4: Verify setup

Run these checks in order. Each one tests a different layer. Fix any failure
before moving to the next check.

**Check 1 — VAULT_PATH file exists and is correct**

```bash
cat ~/.claude/VAULT_PATH
```

Expected: prints the absolute path to your vault (e.g. `C:/Users/you/Research-OS/vault`)

If missing or wrong: re-run the `echo '...' > ~/.claude/VAULT_PATH` command from Step 2

**Check 2 — Vault directory exists at that path**

```bash
ls "$(cat ~/.claude/VAULT_PATH)/CLAUDE.md"
```

Expected: prints the path to `vault/CLAUDE.md`

If missing: confirm the vault path in `~/.claude/VAULT_PATH` is correct and the Research-OS repo is at that location

**Check 3 — Wiki skills are installed globally**

```bash
ls ~/.claude/skills/wiki-pull ~/.claude/skills/wiki-push ~/.claude/skills/wiki-ingest
ls ~/.claude/agents/wiki-librarian.md
```

Expected: all four paths exist

If missing: re-run the `cp` commands from Step 1

**Check 4 — markitdown is installed**

```bash
python -m markitdown --version
```

Expected: prints a version number (e.g. `markitdown, 0.x.x`)

If missing: run `pip install 'markitdown[pdf]'`

**Check 5 — Vault is accessible inside Claude Code**

Open any directory in Claude Code and run:

```
/wiki-pull test
```

Expected: Claude reads `vault/index.md` and reports "wiki is empty" or lists existing content

If "wiki not available": confirm `additionalDirectories` in `~/.claude/settings.json`
contains the vault path, then restart Claude Code

**Check 6 — Full ingest test (end-to-end)**

Find any PDF on your machine and run:

```
/wiki-ingest /path/to/any-file.pdf
```

Expected: Claude converts the PDF, places markdown in `vault/10_sources/`, creates
a summary in `vault/20_summaries/`, and appends an entry to `vault/log.md`

Verify from the terminal:

```bash
ls "$(cat ~/.claude/VAULT_PATH)/10_sources/"
tail -5 "$(cat ~/.claude/VAULT_PATH)/log.md"
```

Expected: the converted file appears in `10_sources/` and a new `ingest` entry
appears in `log.md`

If markitdown fails: check Check 4; pass a `.md` file instead to test the rest
of the workflow independently

---

**All six checks passing = setup is complete.**

---

## Starting a New Research Project

### Step 1: Copy the template

```bash
cp -r /path/to/Research-OS/project-starter/clo-author-template ~/projects/my-paper-name
cd ~/projects/my-paper-name
```

### Step 2: Fill in CLAUDE.md

Open `CLAUDE.md` and replace the bracketed placeholders:
- `[YOUR PROJECT NAME]`
- `[YOUR INSTITUTION]`
- `[YOUR FIELD]`

The wiki integration section is already configured — no changes needed there.

### Step 3: Launch Claude Code

```bash
claude
```

The vault is automatically available because you added it to `additionalDirectories`
in Step 2 of the one-time setup. If you skipped that step, add it per session:

```bash
claude --add-dir /path/to/Research-OS/vault
```

### Step 4: Start researching

```
/new-project [your research topic]     ← full orchestrated pipeline
/discover interview [topic]            ← guided start with interview
/discover lit [topic]                  ← literature search only
```

---

## How the Wiki Works

The wiki accumulates research knowledge across all your projects so you never
start from zero.

### Structure

```
vault/
├── 00_inbox/        ← temporary unsorted notes and stubs
├── 10_sources/      ← raw source files (PDFs converted to markdown, immutable)
├── 20_summaries/    ← one page per important source
├── 30_concepts/     ← concept and mechanism pages
├── 40_methods/      ← methodology pages (DiD, IV, RDD, etc.)
├── 50_datasets/     ← dataset pages
├── 60_people_institutions/  ← author, journal, and institution pages
├── 70_projects/     ← one page per research project (wiki notes, not repos)
├── 90_synthesis/    ← higher-level synthesis and comparison pages
├── _templates/      ← templates for each content type
├── CLAUDE.md        ← wiki maintenance rules (read by Claude)
├── index.md         ← content catalog
└── log.md           ← chronological record of changes
```

### Three workflows

**Ingest** — adding a new source: raw source → summary → concept/method/dataset
pages → index + log. Triggered automatically by `/wiki-ingest` or offered by
the librarian after a literature search.

**Query** — asking a research question: read index → identify relevant pages →
synthesize → optionally write useful answers back to `90_synthesis/`.

**Lint** — health check: detect stale claims, duplicate pages, orphan pages,
concepts that need pages, contradictions. Run periodically via `/wiki-pull lint`.

### What lives in 70_projects/

This folder contains **wiki notes about your projects**, not the project repos
themselves. Each entry captures: core question, thesis, related concepts/methods/
datasets, open questions, next steps. It's the bridge between the wiki and your
active work.

---

## Adding Sources to the Wiki

The wiki-ingest skill handles all source ingestion. Three input types:

```
/wiki-ingest path/to/paper.pdf          ← PDF (auto-converts with markitdown)
/wiki-ingest path/to/note.md            ← already-converted markdown
/wiki-ingest "Smith et al. 2023 Title"  ← citation string (creates inbox stub)
```

**What happens automatically:**
1. PDF → converted to markdown via markitdown → placed in `vault/10_sources/`
2. Summary created in `vault/20_summaries/` from the source template
3. Relevant concept, method, dataset, and project pages updated
4. `vault/index.md` and `vault/log.md` updated
5. `wiki-links.md` in the current project updated

**The librarian also offers this automatically** after each literature search —
you'll see a numbered list of new sources with a prompt to select which ones
to add.

---

## Key Skills Reference

### Clo-Author Research Skills

| Command | What It Does |
|---------|-------------|
| `/new-project [topic]` | Full pipeline: idea → paper (orchestrated) |
| `/discover interview [topic]` | Guided interview to define research question |
| `/discover lit [topic]` | Literature search + annotated bibliography |
| `/discover data [topic]` | Dataset discovery and feasibility assessment |
| `/strategize [question]` | Identification strategy + pre-analysis plan |
| `/analyze [dataset]` | End-to-end data analysis (code + review) |
| `/write [section]` | Draft paper sections + AI-pattern cleanup |
| `/review [file/--flag]` | Quality reviews (paper, code, or peer review) |
| `/revise [report]` | R&R cycle: classify and route referee comments |
| `/talk [mode] [format]` | Create and audit Beamer/Quarto presentations |
| `/submit [mode]` | Journal targeting, replication package, final gate |
| `/tools [subcommand]` | Utilities: commit, compile, lint, validate-bib, etc. |

### Wiki Skills (globally available)

| Command | When to Use |
|---------|-------------|
| `/wiki-pull [topic]` | Before starting substantial literature or data work |
| `/wiki-push` | After peer review passes (>= 80) — pipeline milestone |
| `/wiki-ingest [source]` | When adding any source to the wiki |

---

## FAQ

**Q: Where do my project repos live?**
Anywhere on your filesystem. They are not inside Research-OS. The template is
just a starting point you copy.

**Q: Where does the vault live?**
Always at `Research-OS/vault/`. Do not move it — the path is stored in
`~/.claude/VAULT_PATH` and `~/.claude/settings.json`.

**Q: My project shows "wiki not available". What's wrong?**
The vault is not in this session's accessible directories. Check that:
1. `additionalDirectories` in `~/.claude/settings.json` has the correct vault path
2. Or use `claude --add-dir /path/to/vault` when launching

**Q: Can I use wiki skills without running a full project pipeline?**
Yes. `/wiki-pull`, `/wiki-push`, and `/wiki-ingest` all work as standalone
commands from any Claude session where the vault is available.

**Q: Does each project get its own wiki?**
No. All projects share `vault/`. Project notes live in `vault/70_projects/` as
wiki pages, not separate vaults.

**Q: What if markitdown doesn't handle a PDF well?**
Try the Azure Document Intelligence option for complex layouts:
`markitdown file.pdf -d -e "your-endpoint"`. Or pre-process the PDF with another
tool and pass the resulting `.md` file to `/wiki-ingest`.

**Q: How do I keep the wiki clean as it grows?**
Run a lint pass periodically: `/wiki-pull lint`. The wiki-librarian will identify
stale notes, orphan pages, and gaps worth addressing.
