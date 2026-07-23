---
name: dashboard
description: Generate or refresh the living project dashboard HTML. Scans the passport, literature corpus + wiki-links, data, analysis scripts/outputs, results, reviews, plans, and git history to build a single-page project overview. Invoke with /dashboard to create from scratch or update an existing dashboard.
argument-hint: "[refresh | create | add-changelog TITLE]"
allowed-tools: Read,Grep,Glob,Write,Edit,Bash
---

# Dashboard

Generate or refresh **`project_dashboard.html`** — the single canonical, living overview of the project, at the project root. This is the canonical filename (never `research_overview.html`, never split).

**Input:** `$ARGUMENTS` — optional subcommand.

State comes from `passport.yaml` (schema: `${CLAUDE_PLUGIN_ROOT}/templates/passport.yaml`); paths follow `${CLAUDE_PLUGIN_ROOT}/rules/folder-map.md`; structure and design system are specified in `${CLAUDE_PLUGIN_ROOT}/rules/html-dashboard.md`. The renderer is `${CLAUDE_PLUGIN_ROOT}/scripts/generate_dashboard.py`.

---

## Subcommands

### `/dashboard` or `/dashboard refresh` — Rebuild from current state

Run the generator, then verify/patch authored sections:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/generate_dashboard.py" --project-root .
```

The generator scans:

1. **passport.yaml** — `meta` (title, slug, main_wiki, output_types), `research:` block, `pipeline` (current_stage + per-stage status/score), `literature_corpus`, `claim_manifest`, `integrity`, latest `sessions:` entry.
2. **Literature** — `passport.yaml` `literature_corpus` + `wiki-links.md` for citation status (see the citation-status section below).
3. **Data** — `find 02_data/raw 02_data/cleaned -type f` — count, sizes, categories.
4. **Analysis code** — `find 03_analysis/scripts/{R,py,jl} -type f` — list with status.
5. **Results** — `03_analysis/output/` figures/tables/`results_summary.md`.
6. **Paper** — `04_paper/<output>/sections/`, `figures/`, `tables/` (per selected output type).
7. **Reviews** — `04_paper/reviews/` (referee, editorial, verification, integrity).
8. **Plans** — `00_admin/process/plans/` — active plans with status from frontmatter.
9. **Journal / sessions** — `00_admin/process/journal.md`, `00_admin/process/sessions/`.
10. **git log** — recent commits for the history section.

Preserve authored content: the Overview (question, causal chain, contributions, risks), identification strategy, and literature positioning are authored — refresh operational sections only unless `create` mode. **Never overwrite existing changelog entries — only append.**

Output: write/update `project_dashboard.html` at the project root, then open it for the user.

### `/dashboard create` — Generate from scratch

Full generation including authored research-design sections. Use after `/discover` and `/strategize`. Prompts the user for: research question, causal chain (nodes), contributions (2–4 bullets), risk-matrix entries. Then generates all sections with the operational ones populated from the passport + disk scan.

### `/dashboard add-changelog TITLE` — Append a changelog entry

Append a dated entry to the changelog. Prompts for a tag type (data/design/code/paper/lit/review/infra) and bullet points.

---

## Section Structure

A single long scrollable page (two levels of sticky nav — see `rules/html-dashboard.md`), sections in this order:

| # | Section | Nav ID | Content |
|---|---------|--------|---------|
| 1 | Overview | `#overview` | Research question, causal chain, contributions, risk matrix, current stage |
| 2 | Data | `#data` | Role inventory + file-level tables with sizes/status |
| 3 | Identification | `#identification` | Design, specifications, threats, fallback |
| 4 | Literature | `#literature` | Positioning, proximity, gaps, **citation-status** (below) |
| 5 | Analysis | `#analysis` | Scripts run, analysis-done checklist, robustness progress |
| 6 | Results | `#results` | Current results — figures/tables/estimates produced so far |
| 7 | Paper | `#paper` | Figure/table budget, word allocation, section completion |
| 8 | Quality | `#quality` | Component scores + gate status from `passport.yaml` `pipeline.stages` |
| 9 | History | `#history` | Journal / sessions / reviews timeline |
| 10 | Plans | `#plans` | Active plans (DRAFT/APPROVED/COMPLETED) |
| 11 | Changelog | `#changelog` | Reverse-chronological milestone log (append-only) |

---

## Literature Citation-Status Section (Living)

The Literature section carries a **citation-status** panel — the heart of the living overview. It is built from `passport.yaml` `literature_corpus` (each entry has `bibkey`, `title`, `proximity`, `citation_status`, `wiki_path`) cross-referenced with `wiki-links.md`. Papers are grouped into three buckets:

| Bucket | Source of truth | Pill |
|--------|-----------------|------|
| **Cited** | `citation_status: cited` — actually `\cite{}`d in a `04_paper/<output>/` section | `CITED` (pass) |
| **Intended to cite** | `citation_status: intended` — planned for citation, not yet in the draft | `INTENDED` (warn) |
| **Relevant, not cited** | `citation_status: relevant` — in the corpus/wiki, relevant, but not (yet) planned for citation | `RELEVANT` (neutral) |

For each paper show: author/year (bibkey), short title, proximity (1–5), citation status, and — if `wiki_path` is set — a link/marker that the paper is summarized in the wiki. Show counts per bucket (e.g. "12 cited · 5 intended · 9 relevant-not-cited") so the gap between intended and cited is visible at a glance. A paper that is `intended` but still absent from any section is a to-do; a `relevant` paper with proximity 1–2 that is uncited is a coverage flag.

This panel is *living*: it updates every time `/discover lit`, `/write`, or `/checkpoint` runs, because those update `literature_corpus.citation_status` and `wiki-links.md`.

---

## Analysis-Done + Current-Results Sections (Living)

- **Analysis (`#analysis`)** — what analysis has actually run. Scripts present in `03_analysis/scripts/{R,py,jl}/`, the robustness checklist (done/total), and any `analysis-done` markers derived from `03_analysis/output/results_summary.md` and `passport.yaml` `claim_manifest` (claims whose `evidence_origin` is an `analysis:<script>`).
- **Results (`#results`)** — the current empirical results: figures and tables in `03_analysis/output/` (and `04_paper/<output>/figures|tables/`), with the headline estimates if `results_summary.md` records them. Empty-state card until estimation runs.

Both are refreshed on every dashboard rebuild so the dashboard always reflects the true current state of the analysis, not a stale snapshot.

---

## Data Status Labels

| Label | Pill class | Meaning |
|-------|-----------|---------|
| `downloaded` | `pill-pass` | File is on disk in `02_data/raw/` |
| `manual download` | `pill-warn` | Requires registration or browser interaction — flag for collaborators |

---

## Design System

Use the research-os HTML design system (shared CSS/JS in `${CLAUDE_PLUGIN_ROOT}/styles/`, embedded inline by the generator):
- Palette: ivory/clay/serif (light) with automatic dark mode + manual toggle
- Sticky main nav + section sub-navs, smooth scroll, IntersectionObserver highlighting
- Pills for status; cards (bordered-left with accent); `report-table` for structured data
- Monospace for paths/dates; serif for section titles
- Self-contained: all CSS/JS inline, no external dependencies; print-friendly (navs hidden)
- Footer: "Generated YYYY-MM-DD by research-os"

---

## Bundled Resources

| Resource | Path | What It Contains |
|----------|------|-----------------|
| Dashboard structure + CSS | `${CLAUDE_PLUGIN_ROOT}/rules/html-dashboard.md` | Nav architecture, design system, regenerate triggers |
| Generator | `${CLAUDE_PLUGIN_ROOT}/scripts/generate_dashboard.py` | Scans passport + numbered layout, renders the HTML |

---

## Rules

1. **One file** — always `project_dashboard.html` at the project root, never split, never renamed.
2. **Refresh is safe** — operational sections (data, analysis, results, quality, history) rebuilt from the passport + disk. Authored sections (overview, identification, literature positioning) preserved unless `create` mode.
3. **Changelog is append-only** — never delete or rewrite existing entries.
4. **Living overview** — literature citation-status, analysis-done, and results always reflect current state. Regenerate after any pipeline milestone (data added, analysis run, section drafted, review scored) or anytime with `/dashboard refresh`.
5. **Collaborator-friendly** — clear language; link download instructions for `manual download` items.
6. **State from the passport** — scores/stage/corpus come from `passport.yaml`, not re-derived guesses.
