# <Project Title>

research-os project. This file is the per-project config Claude reads on entry.

## Config

- **Main wiki:** `<theme>` (primary thematic wiki this project draws on; all registered wikis are readable, this is the default)
- **Paper type:** `<imrad | literature_review | theory | case_study | conference>`
- **Language:** `<en | de>`
- **Citation style:** `<apa | chicago | mla | ieee | vancouver | aea>`

## How to work here

- State lives in **`passport.yaml`** — the single ledger. Don't create scattered state files.
- Run **`/research-os-help`** at any time to see the current stage and the exact next step.
- Folder layout follows the numbered scheme (see the plugin's `rules/folder-map.md`): `00_admin · 01_literature · 02_data · 03_analysis · 04_paper · 05_outreach`.
- Durable knowledge belongs in the **wiki** (`/wiki-ingest`) and the **second brain** (`/wiki-push`, `/checkpoint`) — not in this project folder.
- **Update over create** (see `rules/output-discipline.md`): improve existing reviews/reports; a new file only for a genuinely new question/literature.

## Non-negotiables

Six standing rules. Everything else is loaded on demand — `.claude/rules/` holds path-scoped stubs that pull in the full plugin rule when you touch a matching file, so this list stays short deliberately. Claude follows a bounded number of standing instructions reliably; a long CLAUDE.md means the rules at the bottom get quietly ignored.

1. **Plan first, verify after.** Non-trivial work enters plan mode and the plan is saved to `00_admin/process/plans/`. Nothing is reported done until it compiles, renders, or runs.
2. **The wiki is read before the web.** Check the corpus (`<main_wiki>/10_sources`, `20_summaries`, `30_concepts`, `40_methods`, `50_datasets`) before searching outward. It is already summarized, already scored for proximity, and already linked.
3. **Every non-trivial claim is registered.** `passport.yaml` `claim_manifest`, with an `evidence_origin` that resolves — a bibkey, a data path, an analysis script, or explicit reasoning. The integrity gate reads exactly this.
4. **Critics score, creators fix.** No agent clears its own work. A creator that reports its own score is discarded and its critic is dispatched.
5. **The integrity gate is blocking.** `/peer-review` and `/submit` do not proceed while `passport.yaml` `integrity.unresolved` is non-empty. A confident assurance is not evidence.
6. **Gates:** 80 to commit, 90 for review, 95 to submit with every component at 80 or better.

## Pipeline (one step at a time)

`/discover` → `/strategize` → `/analyze` → `/write` → `/peer-review` → `/revise` → `/submit`
Ask `/research-os-help` what's next rather than memorizing this.

## Wiki bridge

`wiki-links.md` (this folder) tracks which wiki notes are relevant and their citation status (relevant / intended / cited). It is refreshed by `/wiki-pull`, `/wiki-push`, and `/checkpoint`, and reflected in `project_dashboard.html`.
