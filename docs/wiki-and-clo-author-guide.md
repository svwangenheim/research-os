# Research OS: Complete Guide to the LLM Wiki and Clo-Author

This guide walks you through the entire system — from a completely empty vault to
a finished paper. It is written for everyone from first-time Claude users to
experienced researchers who just want a precise reference.

---

## What is this system?

Two tools work together here:

**The LLM Wiki** is a permanent, cross-project knowledge base stored as
plain markdown files on your computer. Every paper you read, every concept you
learn, every dataset you assess accumulates here. The wiki grows smarter with
every project you run.

**Clo-Author** is a per-project research scaffold that turns a research idea
into a finished paper — with agents that search literature, design identification
strategies, write code, draft prose, and simulate peer review.

The relationship is simple:

```
Wiki  →  feeds into  →  Clo-Author project
Wiki  ←  enriched by  ←  Clo-Author project
```

The wiki is the long-term memory. Clo-Author is the short-term executor.
They share a bridge file (`wiki-links.md`) that lives inside each project.

> **Beginner note:** Throughout this guide, a *skill* is a named command you type
> into Claude Code starting with `/`, like `/wiki-ingest` or `/discover`. A
> *session* is one Claude Code conversation — it starts when you open the terminal
> and ends when you close it or run `/clear`.

---

## Part 1: First-time setup (do this once)

### What you need installed

| Tool | Purpose | Install |
|------|---------|---------|
| [Claude Code](https://docs.anthropic.com/en/docs/claude-code) | Runs everything | `npm install -g @anthropic-ai/claude-code` |
| Python 3 + markitdown | Converts PDFs to markdown | `pip install 'markitdown[pdf]'` |
| XeLaTeX (optional) | Compiles the final paper | [TeX Live](https://tug.org/texlive/) |
| R (optional) | Runs analysis scripts | [r-project.org](https://www.r-project.org/) |

Verify markitdown works:
```bash
python -m markitdown --version
```

### Step 1: Clone the Research-OS repository

```bash
git clone https://github.com/YOUR-FORK/research-os
cd research-os
```

The repository contains three things:
- `vault/` — your wiki (starts almost empty)
- `claude-global/` — wiki skills and agents to install globally
- `clo-author-template/` — the per-project research scaffold

### Step 2: Install wiki skills globally

These commands make `/wiki-pull`, `/wiki-push`, `/wiki-ingest`, and
`/wiki-maintain` available in *every* Claude Code session on your machine —
not just when you are inside the research-os folder.

```bash
mkdir -p ~/.claude/agents ~/.claude/skills

cp claude-global/agents/wiki-librarian.md ~/.claude/agents/
cp -r claude-global/skills/wiki-pull     ~/.claude/skills/
cp -r claude-global/skills/wiki-push     ~/.claude/skills/
cp -r claude-global/skills/wiki-ingest   ~/.claude/skills/
cp -r claude-global/skills/wiki-maintain ~/.claude/skills/
```

> **Why global?** The wiki is a permanent resource that spans all your projects.
> You want it available everywhere, not just inside one folder.

### Step 3: Write your vault path to a config file

Claude Code needs to know where the vault lives so it can find it from any
working directory.

**Windows (Git Bash or PowerShell):**
```bash
echo 'C:/Users/YOUR_USERNAME/research-os/vault' > ~/.claude/VAULT_PATH
```

**Mac / Linux:**
```bash
echo '/Users/YOUR_USERNAME/research-os/vault' > ~/.claude/VAULT_PATH
```

Verify:
```bash
cat ~/.claude/VAULT_PATH
# Should print the full path to your vault/
```

### Step 4: Add the vault to your global Claude settings

Open (or create) `~/.claude/settings.json` and add the vault to
`additionalDirectories`. This makes the vault readable and writable by Claude
in every session automatically — no extra flags needed.

```json
{
  "$schema": "https://json.schemastore.org/claude-code-settings.json",
  "permissions": {
    "allow": [
      "Bash(markitdown *)",
      "Bash(python -m markitdown *)"
    ],
    "additionalDirectories": [
      "C:/Users/YOUR_USERNAME/research-os/vault"
    ]
  }
}
```

Replace the path with your actual vault location.

> **If you prefer per-session control** (instead of always-on), skip
> `additionalDirectories` and launch Claude with:
> ```bash
> claude --add-dir /path/to/research-os/vault
> ```

### Step 5: Verify everything works

Open any folder in Claude Code and run:
```
/wiki-pull test
```

You should see a response that reads `vault/index.md`. If you see
"wiki not available", check that `additionalDirectories` in
`~/.claude/settings.json` points to the correct path.

**Setup is complete. You will not need to do any of this again.**

---

## Part 2: The wiki on its own

### What the vault looks like

```
vault/
├── CLAUDE.md               ← wiki rules (Claude reads this automatically)
├── index.md                ← content catalog — what is in the wiki
├── log.md                  ← chronological record of all changes
├── 00_inbox/               ← temporary: unsorted papers and stubs
├── 10_sources/             ← raw source files (never modified after ingest)
├── 20_summaries/           ← one summary page per source
├── 30_concepts/            ← concept and mechanism pages
├── 40_methods/             ← identification strategy and method pages
├── 50_datasets/            ← dataset pages
├── 60_people_institutions/ ← notable authors, journals, organizations
├── 70_projects/            ← one page per research project
├── 90_synthesis/           ← cross-paper synthesis and comparisons
└── attachments/            ← local images and files
```

**The core idea:** `10_sources/` holds the immutable raw files. Everything else
is maintained by Claude — updated, cross-linked, and synthesized over time.
You add sources; Claude maintains the knowledge structure.

### Adding your first paper: `/wiki-ingest`

This is the single entry point for adding any source to the wiki. You can
pass a PDF, a markdown file, or a citation string.

**From a PDF:**
```
/wiki-ingest path/to/paper.pdf
```

Claude converts it to markdown, places it in `10_sources/`, creates a detailed
summary in `20_summaries/`, updates relevant concept and method pages, and
updates `index.md` and `log.md`.

**From an existing markdown file:**
```
/wiki-ingest path/to/paper.md
```

**From a citation string (creates a stub for later):**
```
/wiki-ingest "Acemoglu et al. 2023, The Turing Trap"
```

This creates a placeholder in `00_inbox/`. When you later obtain the actual
file, re-run `/wiki-ingest path/to/file` to complete the ingestion.

After ingest, the wiki automatically:
- Creates `vault/20_summaries/[author-year]-[short-title].md` with a full
  structured summary including research question, method, findings, limitations,
  and links to related concept/method/dataset pages
- Updates or creates pages in `30_concepts/`, `40_methods/`, `50_datasets/`
  for every topic the paper touches
- Updates `index.md` and appends to `log.md`

> **Beginner note:** You do not need to understand what Claude writes into these
> files. The point is that the knowledge is there, structured, and searchable —
> so the next time you work on a related topic, Claude already knows about this paper
> without you having to re-read or re-explain it.

### Querying the wiki before work: `/wiki-pull`

Before starting any research task, run:
```
/wiki-pull [topic or question]
```

Claude reads the wiki and returns:
- **What we already know** — synthesized from existing notes
- **Most relevant notes** — specific files you can drill into
- **Reuse opportunities** — what should directly inform the current work
- **Gaps** — what is still missing or unclear

Example:
```
/wiki-pull absorptive capacity and SME innovation subsidies
```

### Keeping the wiki healthy: `/wiki-maintain`

Run this periodically to lint the wiki:
```
/wiki-maintain
```

This detects stale claims, duplicate pages, orphan pages with weak linking,
concepts mentioned often but lacking pages, and contradictions. Claude
summarizes findings and fixes them if instructed.

Run this once a month or after a large batch of ingestions.

### The core wiki habit

**Every time you read a paper worth keeping, run `/wiki-ingest` on it.**

That is the entire maintenance burden on your side. The wiki does the rest.

---

## Part 3: Setting up a clo-author project

Clo-Author is a template you copy for each new research project. The template
lives at `clo-author-template/` in research-os and contains everything Claude
needs to run the full paper-writing pipeline.

### Step 1: Copy the template

```bash
# From the research-os root
cp -r clo-author-template/ /path/to/my-project-name
cd /path/to/my-project-name
```

Then open it in Claude Code:
```bash
claude
```

Tell Claude what you are doing on the first message:
```
I am starting a research project on [YOUR TOPIC]. Read CLAUDE.md and help me set up.
```

### Step 2: Fill in CLAUDE.md

`CLAUDE.md` is the project config file. Claude reads it at the start of every
session. Open it and replace all `[BRACKETED PLACEHOLDERS]`:

```markdown
**Project:** Effect of ZIM Subsidies on SME Innovation
**Institution:** Dezernat Zukunft
**Field:** Innovation Economics / Public Finance
```

This takes two minutes and sets how every agent in the pipeline behaves —
which journals to target, which field conventions to follow, which identification
strategies to consider first.

### Step 3: Fill in the domain profile (or let the interview do it)

Open `.claude/references/domain-profile.md`. You can fill this in manually
(target journals, common datasets, seminal references, field-specific referee
concerns) or run the interview to fill it automatically:

```
/discover interview
```

Claude asks six to eight structured questions about your research idea and
populates the domain profile from your answers. This is the recommended
starting point for any new project.

### Step 4: Extract your writing voice (once, not per project)

This step requires your **own published or drafted papers** — papers you wrote,
not papers you've read. The goal is to extract *your* voice, so the input must
be your work exclusively.

Place your prior papers (`.tex` or `.pdf`) in `master_supporting_docs/` and run:
```
/write style-guide master_supporting_docs/
```

Or point directly at any directory containing your own papers:
```
/write style-guide /path/to/my-own-papers/
```

**Important:** Do NOT point style-guide at the wiki vault (`vault/10_sources/`).
That folder contains other authors' papers. Extracting voice from them would
corrupt your personal style profile. Style-guide reads only the directory you
explicitly provide — the vault is intentionally excluded.

This produces `.claude/references/personal-style-guide.md` — a profile of your
sentence patterns, paragraph openings, lexicon, hedging style, and citation
conventions. The writer agent loads it on every subsequent `/write` call and
drafts in your voice, not generic academic prose.

**Re-run this after publishing a new paper that shifts your style. Otherwise,
once per career is sufficient.**

### Step 5: Run the wiki pull for your topic

```
/wiki-pull [your research topic]
```

Even if the wiki is sparse, this surfaces what already exists and connects the
project to the right wiki pages. The pull result informs the domain profile and
speeds up the literature search in the next step.

---

## Part 4: The research workflow, session by session

Every working session follows the same four-step rhythm:

```
1. Wiki pull          → what do we already know?
2. Research work      → discover, strategize, analyze, write
3. Wiki update        → ingest new papers found this session
4. Checkpoint         → save everything before closing
```

### Discovery phase

**Literature search:**
```
/discover lit [topic]
```

The librarian:
1. Checks `master_supporting_docs/` and `vault/10_sources/` first (your existing
   corpus — no need to copy files between locations)
2. Checks `vault/20_summaries/` for already-ingested papers and uses them as a
   head start, skipping redundant searches
3. Searches top journals, field journals, NBER/SSRN/IZA, and follows citation chains
4. Assigns proximity scores (1 = directly competes, 5 = background)
5. Generates a scored annotated bibliography and an interactive HTML report

At the end of the literature search, you will see a **WIKI-PENDING block**:

```
## WIKI-PENDING — Not yet in global wiki

| Paper | File | Action |
|-------|------|--------|
| Audretsch (2003) | vault/10_sources/audretsch2003-sbir.md | /wiki-ingest |
| Kleer (2010)     | — (not yet in vault)                  | /wiki-ingest |
```

**Ingest every paper in this list before closing the session.**
This is the single most important habit in the system. Papers found but not
ingested are silently lost to future projects. The WIKI-PENDING block exists to
make the action visible, not to let you ignore it.

**Data discovery:**
```
/discover data [requirements]
```

The explorer searches public microdata, administrative data, survey data, and
novel sources. Each dataset receives a feasibility grade (A = ready to use,
D = very difficult) and a five-point critique (measurement validity, sample
selection, external validity, identification compatibility, known issues).

### Strategy phase

```
/strategize
```

The strategist designs an identification strategy, produces a strategy memo,
and routes it through the strategist-critic. The pair iterates until the score
reaches 80/100 or escalates to you.

For papers with formal theory:
```
/strategize theory
```

The theorist drafts assumptions, lemmas, theorems, and proofs. The
theorist-critic reviews through four phases: claim triage, proof validity,
assumption minimality, and citations.

### Execution phase

```
/analyze [dataset]    # Data wrangling and estimation (R, Python, Julia)
/write intro          # Draft the introduction
/write strategy       # Draft the empirical strategy section
/write results        # Draft results — requires output files from /analyze
/write conclusion
/write abstract       # Draft last
```

The writer loads your personal style guide and domain profile automatically.
It drafts using structured paragraph-level argument moves, then strips AI
writing patterns in a cleanup pass.

> **Important:** The writer hard-blocks the Results and Conclusion sections if
> no output files exist in `paper/tables/` or `paper/figures/`. This prevents
> fabricated results. Run `/analyze` before `/write results`.

### Peer review

```
/review --peer [journal]    # Full simulated submission
/review --stress            # Adversarial referees for pre-submission testing
```

Two blind referees with distinct intellectual dispositions (Structuralist,
Credibility, Measurement, Policy, Theory, Skeptic) weighted by journal culture.
Each produces a scored report with FATAL / ADDRESSABLE / TASTE classifications.

For a real R&R from a journal:
```
/revise [referee-report.md]
```

Classifies each comment (NEW ANALYSIS / CLARIFICATION / DISAGREE / MINOR) and
routes it to the right agent. Produces a response letter.

Final gate:
```
/submit
```

Requires aggregate score ≥ 95/100 with all individual components above 80.

### Ending the session: `/checkpoint`

Run this before closing Claude Code:
```
/checkpoint
```

Claude gathers what happened and saves to four places:

| Destination | What gets saved |
|-------------|-----------------|
| Claude Code memory | Corrections and preferences for future sessions |
| `SESSION_REPORT.md` | Append-only session log in the project folder |
| `quality_reports/research_journal.md` | Agent invocation trail |
| `vault/70_projects/[project-name].md` | Session journal entry, written directly to the wiki |

The vault project note is created automatically if it does not exist. It records
what was done and what comes next. The next session reads it as the first step in
session recovery — faster and more reliable than reconstructing from memory.

> **Beginner note:** Think of `/checkpoint` as pressing Save. Without it, Claude
> starts each new session with no memory of the previous one. With it, sessions
> compound: each one builds on the last.

---

## Part 5: Closing the loop after a project

When a paper is done (accepted, submitted, or at a stable draft):

**Ingest the final paper into the wiki:**
```
/wiki-ingest paper/main.tex
```

This means your own paper becomes part of the global corpus. The next project
that touches related territory starts with your own findings already in the wiki,
proximity-scored and linked.

**Push findings to synthesis pages:**
```
/wiki-maintain
```

Ask Claude to update `vault/90_synthesis/` pages that your paper affects. If
your findings challenge or confirm prior synthesis, make that tension explicit.

**Update the project page:**

Open `vault/70_projects/[project-name].md` and add a final entry summarizing
the key finding, what changed the picture, and what still needs further research.

---

## Part 6: Quick reference

### Wiki commands (available everywhere)

| Command | What it does |
|---------|-------------|
| `/wiki-pull [topic]` | Read prior knowledge before starting work |
| `/wiki-ingest [file or citation]` | Add a source to the wiki |
| `/wiki-maintain` | Health check: duplicates, orphans, stale claims |
| `/wiki-push` | Sync manual edits back through the vault |

### Clo-author commands (inside a project)

| Command | What it does |
|---------|-------------|
| `/discover interview` | Research interview → spec + domain profile |
| `/discover lit [topic]` | Literature search + WIKI-PENDING list |
| `/discover data [requirements]` | Data source discovery + feasibility grades |
| `/strategize` | Identification strategy with critic review |
| `/strategize theory` | Formal theory section with theorist-critic |
| `/analyze [dataset]` | Data wrangling + estimation |
| `/write [section]` | Draft paper sections in your voice |
| `/write style-guide` | Extract your writing voice from prior papers |
| `/review --peer [journal]` | Simulated peer review (30 journal profiles) |
| `/revise [report]` | R&R response: classify and route each comment |
| `/talk` | Beamer or Quarto RevealJS presentation |
| `/submit` | Final gate: score ≥ 95/100 |
| `/checkpoint` | Save session to memory + wiki + logs |
| `/dashboard` | Generate HTML project overview |
| `/freeze [dirs]` | Lock directories from accidental edits |
| `/careful` | Block destructive bash commands |

### Quality gates

| Score | Meaning |
|-------|---------|
| ≥ 80/100 | Commit allowed |
| ≥ 90/100 | PR allowed |
| ≥ 95/100 + all components ≥ 80 | Submission allowed |

---

## Part 7: Common mistakes and how to avoid them

**Skipping `/wiki-ingest` after a literature search.**
The WIKI-PENDING block at the end of `/discover lit` is not optional. Papers
found but not ingested are silently lost to future projects. Five minutes of
ingestion at session end compounds into a rich knowledge base over a research career.

**Copying reference papers to `master_supporting_docs/` manually.**
For literature you've *read* (other authors' work), you do not need to copy
anything. Clo-author's librarian and discovery agents automatically search both
`master_supporting_docs/` and `vault/10_sources/`. Leave reference papers in
the vault — they are accessible from every project without copying.

**Exception:** your own prior papers for `/write style-guide` should live in
`master_supporting_docs/` (or a dedicated directory you maintain). Do not put
them in `vault/10_sources/` for this purpose — the vault holds other authors'
work, and style-guide must read only your papers.

**Skipping `/checkpoint` at session end.**
Without a checkpoint, the next session starts blind. The wiki project page
and session report stay empty. Five minutes of checkpoint saves thirty minutes
of re-orientation next time.

**Running `/write` before `/analyze` has produced output.**
The writer refuses to draft Results and Conclusion if no output files exist in
`paper/tables/` or `paper/figures/`. This is a feature, not a bug. Run
`/analyze` first.

**Starting the interview with too vague a topic.**
If you do not have a specific research question yet, start with:
```
/discover ideate [broad topic]
```
This generates three to five candidate questions. Pick one, then run the
interview.

**Letting the wiki grow without periodic maintenance.**
After twenty or thirty ingestions, duplicate concept pages and orphan summaries
accumulate. A monthly `/wiki-maintain` keeps retrieval reliable.

---

## Part 8: The system in one picture

```
┌──────────────────────────────────────────────────────────┐
│                   GLOBAL WIKI (vault/)                   │
│                                                          │
│  10_sources/  →  20_summaries/  →  30_concepts/         │
│                                     40_methods/          │
│  70_projects/  ←  /checkpoint       50_datasets/        │
│  90_synthesis/ ←  /wiki-maintain    60_people/           │
└────────────────────────┬─────────────────────────────────┘
                         │
               wiki-links.md  (bridge)
                         │
┌────────────────────────▼─────────────────────────────────┐
│               CLO-AUTHOR PROJECT (per paper)             │
│                                                          │
│  /discover lit  →  annotated bibliography                │
│  /strategize    →  strategy memo                         │
│  /analyze       →  tables + figures                      │
│  /write         →  paper/main.tex                        │
│  /review        →  quality score                         │
│  /submit        →  final package                         │
└──────────────────────────────────────────────────────────┘
```

The wiki accumulates permanently. Each project draws from it and gives back
to it. Over time, starting a new project means arriving at a rich knowledge
base rather than a blank page.
