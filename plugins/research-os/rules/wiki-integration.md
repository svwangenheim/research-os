# Wiki Integration — the two-layer knowledge model

research-os keeps durable knowledge **outside** the project, in two layers. Every agent reads this file to understand how the project, the thematic wikis, and the personal brain relate. Durable knowledge does not live in the numbered project folders (`folder-map.md`) — it lives here.

---

## The two layers

### Layer 1 — Thematic wikis (Claude-maintained)

The durable knowledge layer is a set of **thematic wikis**, one per research theme (e.g. `cognitive-load`, `labor-economics`). Claude maintains them automatically — ingesting sources, writing scored summaries, and canonicalizing concepts/methods/datasets. **Humans read the wikis but do not hand-edit them**; curation flows through Claude (`/wiki-ingest`, `/wiki-maintain`). Each wiki uses the numbered layout:

```
<theme>/
  00_inbox/               # unprocessed captures awaiting triage/ingest
  10_sources/             # PDFs and raw source files
  20_summaries/           # scored, concept-linked source summaries
  30_concepts/            # canonical concept notes
  40_methods/             # canonical method notes
  50_datasets/            # canonical dataset notes
  60_people_institutions/ # people and institutions
  90_synthesis/           # theme-internal synthesis (within this theme only)
```

### Layer 2 — Personal brain (`_brain/`, human-owned)

`_brain/` is the human's space. **Human edits go here, not into the wikis.** It holds personal notes, planning, and cross-theme thinking:

```
_brain/
  profile.md              # the researcher's profile / standing context
  daily/                  # daily notes
  weekly/                 # weekly reviews
  thoughts/               # freeform notes and ideas
  projects/               # per-project notes (moved from the old wiki 70_projects/)
  synthesis/              # personal synthesis + cross-theme insight (spans multiple wikis)
  learning/               # durable learnings (what used to accumulate in MEMORY.md)
  wikis-index.md          # index of the registered thematic wikis
```

Key distinction from the theme wikis: `90_synthesis/` inside a wiki is **theme-internal** (synthesis within one theme); `_brain/synthesis/` is **personal and cross-theme** (insight that spans wikis, tied to the researcher's own thinking).

### Layer 0 — The project's working slice

The project holds only what it is actively using:
- `01_literature/sources/` — project-local PDFs not (yet) in a wiki
- `01_literature/reviews/` — literature-review outputs (UPDATE IN PLACE, `output-discipline.md`)
- `wiki-links.md` (project root) — the bridge (below)

---

## Locating the wikis — the registry

Wiki paths are resolved through the registry **`~/.claude/vaults.json`** (a theme → path map), which replaces the old single pointer `~/.claude/VAULT_PATH`. All registered wikis are readable; a project's **default** is its **main wiki**, recorded in `passport.yaml` (`meta.main_wiki`) and `CLAUDE.md`. `_brain/`'s location is recorded in the same registry.

```bash
# resolve a wiki path (theme -> path) from the registry
# and the project's default from passport.yaml meta.main_wiki
```

**Fallback:** if `~/.claude/vaults.json` does not exist yet (knowledge layer not built), fall back to the legacy single-vault pointer `~/.claude/VAULT_PATH` if present; otherwise skip all wiki steps silently — agents work from `01_literature/sources/` only.

---

## Two literature sources — always search both

| Location | Role |
|----------|------|
| `01_literature/sources/` | Project-specific: papers, notes, drafts placed here for this project |
| `<main_wiki>/10_sources/` | Theme corpus: every paper ingested into the wiki for this theme |

**Rule:** Any agent that reads `01_literature/sources/` as a *reference literature corpus* MUST also read `<main_wiki>/10_sources/` (and other registered wikis when relevant) when the registry is present. Papers in a wiki do NOT need to be copied into `01_literature/sources/`. Treat both as a single unified corpus.

This applies to:
- **Librarian** — scanning for existing papers before searching the web
- **Verifier** — checking citation coverage (integrity gate)

**Exception — style-guide mode:** `/write style-guide` scans the target directory only and MUST NOT read `<main_wiki>/10_sources/`. Style extraction must use only the user's own prior papers; the wiki contains other authors' work, and mixing it in would corrupt the voice profile. The user's own papers belong in `01_literature/sources/` (or a directory explicitly passed as the argument).

---

## Wiki summaries as a head start

Before searching the web for literature, agents check `<main_wiki>/20_summaries/`. A summary already in the wiki means the paper is ingested, a proximity-scored annotated entry exists, and related concepts/methods/datasets are already linked. Scanning summaries first saves search effort and gives richer context than reading raw source files.

---

## WIKI-PENDING — papers not yet ingested

After any literature search (`/discover lit`) or when new papers appear in `01_literature/sources/`, check which papers are NOT yet present in `<main_wiki>/20_summaries/`. Append a `WIKI-PENDING` block to the review:

```
## WIKI-PENDING — Not yet in the wiki

These papers were found but have no summary in <main_wiki>/20_summaries/.
Run `/wiki-ingest [path]` for each to preserve them across projects.

| Paper | Source | Action |
|-------|--------|--------|
| Author (Year), Title | 01_literature/reviews/<question-slug>.md | /wiki-ingest |
```

If all papers are already in the wiki, print "All papers already in the wiki — no action needed." If the registry is not present, skip this block silently.

---

## Checkpoint: the project note in `_brain/`

`/checkpoint` writes session progress directly to the personal brain as a plain markdown file — a direct filesystem write, no Obsidian MCP or plugin required.

**Target:** `_brain/projects/<slug>.md`
**Project slug:** basename of the working directory, lowercased, spaces replaced with hyphens (matches `passport.yaml` `meta.slug`).

**Entry format** (prepend under `## Journal`, newest first):

```markdown
### YYYY-MM-DD

**Done:**
- [concrete accomplishments from this session]

**Next:**
- [concrete next steps]
```

**File creation:** if the project note does not exist, create it:

```markdown
# [Project Name]

**Working directory:** [basename]
**Started:** [YYYY-MM-DD]

---

## Journal

```

Write directly with the Write/Edit tool. This is a human-facing note in `_brain/` — it does not go into the theme wikis. Objective, reusable knowledge (a new concept/method/dataset learned here) is instead pushed *down* into the relevant wiki via `/wiki-ingest`; cross-theme or personal insight is pushed *up* into `_brain/synthesis/`.

---

## Obsidian MCP (secondary, optional)

If a local Obsidian config exists AND the Obsidian MCP is connected, `/checkpoint` may additionally push to the Obsidian app UI (dashboard, daily journal, kanban). This is a visual enhancement on top of the filesystem write — not a replacement. If the MCP is unavailable, the `_brain/projects/<slug>.md` write already captured the session.

---

## wiki-links.md — the bridge

Each project keeps `wiki-links.md` at its root — a curated index of the wiki notes relevant to this project, plus each source's citation status (relevant / intended / cited). It is refreshed by `/wiki-pull`, `/wiki-push`, and `/checkpoint`, and reflected in `project_dashboard.html`. Agents read it as a fast path to the most relevant wiki pages without scanning the full corpus. The template is `${CLAUDE_PLUGIN_ROOT}/templates/wiki-links.md`.

- `/wiki-pull` — at the start of a session, load the relevant wiki notes into the bridge
- `/wiki-push` — at the end, push objective knowledge down into the wikis and personal/cross-theme insight up into `_brain/synthesis/`
- `/checkpoint` — refresh the bridge and write the `_brain/projects/<slug>.md` note
