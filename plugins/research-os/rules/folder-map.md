# Folder Map — single source of truth for project paths

Every research-os agent, hook, and skill references **this file** for where things live. The scheme is the numbered project layout; the mapping table drives the mechanical rewire from clo-author's old named folders.

## Project layout (numbered)

```
<project>/
  CLAUDE.md                     # project config: main_wiki, selected outputs, language
  passport.yaml                 # material-passport state ledger (see passport-schema)
  wiki-links.md                 # bridge to the main thematic wiki (relevance + citation status)
  project_dashboard.html        # living overview (root)

  00_admin/
    research_outline.md         # living project brief / overview
    domain-profile.md           # field calibration (journals, methods, referee concerns) — from /discover interview
    process/
      plans/                    # phase plans
      decisions/                # decision records
      sessions/                 # session handoffs
      traces/                   # trace analysis / debugging artifacts (logging.md)
      journal.md                # research journal (newest-first)
    logistics/
      timeline.md  deadlines.md  funding.md  ethics.md  contacts.md

  01_literature/
    sources/                    # project-local PDFs not (yet) in the wiki
    reviews/                    # literature-review outputs — UPDATE IN PLACE
    notes/                      # reading notes
    bibliography.bib            # cited/intended bib (generated from the wiki digest)

  02_data/
    raw/                        # immutable
    cleaned/
    codebooks/
    external/                   # declared external experiment/data provenance

  03_analysis/
    strategy/                   # identification strategy / PAP / formal theory memos
    scripts/{R,py,jl}/          # analysis code
    output/                     # figures, tables, charts, results
    replication/                # replication package staging

  04_paper/                     # ONE subfolder per selected output (from /create-project):
    academic_paper/  |  policy_brief/  |  fachtext/  |  hintergrundpapier/  |  geldbrief/ ...
      sections/  figures/  tables/  preambles/  supplementary/  <final PDF>
    reviews/                    # peer-review + integrity reports (shared)
    revisions/                  # R&R trackers + response letters (shared)
    submission/                 # submission package (cover letter, metadata, replication)

  05_outreach/
    talks/                      # Beamer / Quarto slides
    social/                     # tiles, threads (dz-core:create-chart / dz-instagram-kacheln)

  explorations/  ARCHIVE/       # research sandbox (kept from clo-author)
```

## Old (clo-author) → new (research-os) path map

Apply during the rewire; grep ported files for the left column, replace with the right.

| clo-author path | research-os path |
|---|---|
| `paper/sections/` | `04_paper/<output>/sections/` |
| `paper/figures/`, `paper/tables/` | `04_paper/<output>/figures/`, `.../tables/` |
| `paper/preambles/`, `paper/supplementary/` | `04_paper/<output>/preambles/`, `.../supplementary/` |
| `paper/replication/` | `03_analysis/replication/` |
| `paper/talks/`, `paper/quarto/` | `05_outreach/talks/` |
| `paper/dz/fachtexte/` | `04_paper/fachtext/` |
| `paper/dz/geldbrief/` | `04_paper/geldbrief/` |
| `data/raw/` | `02_data/raw/` |
| `data/cleaned/` | `02_data/cleaned/` |
| `scripts/R/` | `03_analysis/scripts/R/` |
| `scripts/*.py`, `scripts/` (python) | `03_analysis/scripts/py/` |
| `quality_reports/plans/` | `00_admin/process/plans/` |
| `quality_reports/session_logs/` | `00_admin/process/sessions/` |
| `quality_reports/decisions/` | `00_admin/process/decisions/` |
| `quality_reports/research_journal.md` | `00_admin/process/journal.md` |
| `quality_reports/reviews/` (manuscript) | `04_paper/reviews/` |
| `master_supporting_docs/`, `supporting_papers/` | `01_literature/sources/` (+ main wiki `10_sources/`) |
| `supporting_slides/` | `05_outreach/talks/` |
| `notes/` | `00_admin/research_outline.md` + `00_admin/process/` |
| `Bibliography_base.bib` | `01_literature/bibliography.bib` |
| `project_dashboard.html` | `project_dashboard.html` (root — unchanged) |
| `wiki-links.md` | `wiki-links.md` (root — unchanged) |
| `SESSION_REPORT.md`, `MEMORY.md`, `pipeline-state.json` | **retired** → `passport.yaml` + `00_admin/process/` |
| `.claude/references/domain-profile.md` | `00_admin/domain-profile.md` |
| `.claude/rules/journal-profiles.md` | `${CLAUDE_PLUGIN_ROOT}/references/journal-profiles.md` (plugin-level reference, not per-project) |

## Rules

- `/create-project` creates only the `04_paper/<output>/` subfolders for the output types the user selects (academic paper · policy brief · Fachtext · Hintergrundpapier · Geldbrief · …).
- Charts have no dedicated top-level folder: analysis charts → `03_analysis/output/`; paper figures → `04_paper/<output>/figures/`; social/standalone → `05_outreach/social/`.
- No `build/` folder — the final compiled PDF sits in its `04_paper/<output>/` folder.
- Durable knowledge does **not** live here — it lives in the thematic wiki and `_brain/` (see `wiki-integration.md`).
- Plugin-level reference material (journal profiles, DZ style guides) lives under `${CLAUDE_PLUGIN_ROOT}/references/` and `${CLAUDE_PLUGIN_ROOT}/styles/` — shared across all projects, not per-project.
