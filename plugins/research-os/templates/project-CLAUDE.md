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

## Pipeline (one step at a time)

`/discover` → `/strategize` → `/analyze` → `/write` → `/peer-review` → `/revise` → `/submit`
Ask `/research-os-help` what's next rather than memorizing this.

## Wiki bridge

`wiki-links.md` (this folder) tracks which wiki notes are relevant and their citation status (relevant / intended / cited). It is refreshed by `/wiki-pull`, `/wiki-push`, and `/checkpoint`, and reflected in `project_dashboard.html`.
