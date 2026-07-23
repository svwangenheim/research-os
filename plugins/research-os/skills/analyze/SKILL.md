---
name: analyze
description: End-to-end data analysis dispatching Coder and Data-engineer for implementation, coder-critic for review. Supports R, Python, Julia. Analysis phase of the research-os pipeline; writes scripts to 03_analysis/ and output to 04_paper/<output>/, and updates passport.yaml.
argument-hint: "[dataset path or goal] Options: --dual [lang1,lang2]"
allowed-tools: Read,Grep,Glob,Write,Edit,Bash,Task
---

# Analyze

Run end-to-end data analysis by dispatching the **Coder** (analysis), **Data-engineer** (cleaning + figures), and **coder-critic** (code review).

**Input:** `$ARGUMENTS` — dataset path or description of analysis goal.

State lives in **`passport.yaml`** (schema: `${CLAUDE_PLUGIN_ROOT}/templates/passport.yaml`). Paths follow `${CLAUDE_PLUGIN_ROOT}/rules/folder-map.md`: scripts → `03_analysis/scripts/{R,py,jl}/`, tables/figures → `04_paper/<output>/tables/` and `.../figures/`, results summary + code review → `03_analysis/output/`. Outputs obey `${CLAUDE_PLUGIN_ROOT}/rules/output-discipline.md`: **re-running a script overwrites its figures/tables deterministically (no date-versioned copies); the code review is one file per target, updated in place with a `## Changelog`.** The coder-critic score is written to `passport.yaml` `pipeline.stages.analysis`; severity is Strict/high (Analysis phase, `${CLAUDE_PLUGIN_ROOT}/rules/quality.md`). Externally declared datasets are recorded in `passport.yaml` `data_provenance`.

---

## Workflow

### Step 1: Pre-Code Report (mandatory)
Before writing any code, the Coder must output a structured report proving it read the strategy inputs:

```markdown
## Pre-Code Report
**Strategy memo:** [`03_analysis/strategy/strategy_memo.md` or "not found"]
**Domain profile:** [`00_admin/domain-profile.md` loaded / not found]
**Language:** [R / Python / Julia — from CLAUDE.md]
**Paper type:** [reduced-form / structural / theory+empirics / descriptive]

**Identification strategy:** [one sentence from memo]
**Key variables:**
- Outcome: [paper name] → [code name]
- Treatment: [paper name] → [code name]
- Controls: [list]
- Fixed effects: [list]
- Clustering: [level]
**Data source:** [path or description]
**Estimator:** [from strategy memo]
**Robustness checks required:** [list from memo]
**Naming map confirms:** [yes / no — do planned code names match paper notation?]

Proceeding to implementation.
```

If the strategy memo is missing, the Coder proceeds with the user's description — but flags that no memo was found and strategic alignment checks (coder-critic categories 1-3) cannot be verified.

### Step 2: Data Preparation (if needed)
If raw data provided, dispatch **Data-engineer** first:
- Clean and wrangle raw data (raw stays immutable in `02_data/raw/`)
- Handle missing values, construct variables per strategy memo
- Generate summary statistics table
- Create publication-quality descriptive figures → `03_analysis/output/`
- Save cleaned data to `02_data/cleaned/`, codebook to `02_data/codebooks/`, and figures

### Step 3: Main Analysis
Dispatch **Coder** agent:
- Stage 0: Data loading (from `02_data/cleaned/` or `02_data/raw/`)
- Stage 1: Main specification (from strategy memo or user description)
- Stage 2: Robustness checks
- Stage 3: Publication-ready output (tables to `04_paper/<output>/tables/`, figures to `04_paper/<output>/figures/`)
- Produce `03_analysis/output/results_summary.md` with all estimates, SEs, and key statistics (MANDATORY)
- Save scripts to `03_analysis/scripts/R/` (or the appropriate language directory: `py/`, `jl/`)

The Coder follows these principles:
- **Script structure:** Use the Script Structure Template below (full scaffolds: `${CLAUDE_PLUGIN_ROOT}/skills/analyze/templates/r-script-structure.R` and `python-script-structure.py`)
- **Packages:** `fixest` for panel data, `modelsummary` for tables, `ggplot2` for figures
- **Standard errors:** Cluster at appropriate level (match treatment assignment)
- **Output:** `.tex` tables for LaTeX, `.pdf`/`.png` figures, `.rds` for intermediate objects
- **No hardcoded paths.** All paths relative to repository root (use `here()` in R, `Path(__file__)` in Python).
- **saveRDS everything.** Every computed object (estimates, model fits, data frames, summary statistics) gets serialized to `.rds` (in `03_analysis/scripts/R/output/`) for downstream use by the writer and other agents.

### Step 4: Code Review
Dispatch **coder-critic** agent — run the full 12-category checklist:

**Strategic (categories 1-3):**
1. **Code-strategy alignment** — Does the code implement the strategy memo faithfully? Correct dependent variable, treatment, controls, fixed effects, sample restrictions?
2. **Sanity checks** — Are summary statistics printed before regressions? Do coefficient signs match economic intuition? Are sample sizes reasonable?
3. **Robustness sufficiency** — Are required robustness checks present? Alternative specifications, placebo tests, sensitivity analysis per strategy memo?

**Code Quality (categories 4-12):**
4. **Structure** — Does the script follow the standard template? Clear section headers, logical flow from setup to export?
5. **Console hygiene** — No spurious `print()` statements polluting output. Intentional output only.
6. **Reproducibility** — `set.seed()` at top if any stochastic elements. No absolute paths. All packages loaded at top. Directory creation with `showWarnings = FALSE`.
7. **Functions** — Repeated logic extracted into functions. No copy-paste code blocks with minor variations.
8. **Figure quality** — Publication-ready: proper axis labels, titles, legends, font sizes. Consistent theme across all figures.
9. **RDS pattern** — Every computed object (models, data frames, summary stats) saved via `saveRDS()` for downstream use. Not just final outputs — intermediate objects too.
10. **Comments** — Section headers present. Non-obvious code commented. No commented-out dead code left behind.
11. **Error handling** — Graceful handling of missing files, empty data subsets, convergence failures. Informative error messages.
12. **Polish** — Consistent naming conventions. No magic numbers. Clean whitespace. Professional quality ready for replication package.

If strategy memo exists, cross-reference code against stated design.
**Save the report to `03_analysis/output/code_review.md`, updating in place** (one consolidated review, sectioned per script, with a `## Changelog`). Write the coder-critic score into `passport.yaml` `pipeline.stages.analysis`.

Refresh the dashboard: run `/dashboard`.

### Step 5: Fix Issues
If coder-critic finds Critical or Major issues:
1. Re-dispatch Coder with specific fixes (max 3 rounds)
2. Re-run coder-critic to verify fixes

### Step 6: Present Results
1. **Results summary** — key estimates with SEs and interpretation (from `03_analysis/output/results_summary.md`)
2. **Scripts created** — paths and descriptions
3. **Output files** — tables in `04_paper/<output>/tables/`, figures in `04_paper/<output>/figures/`
4. **Code review score** — from coder-critic (recorded in `passport.yaml`)
5. **TODO items** — missing data, additional specifications needed

---

## Script Structure Template

```r
# ============================================================
# [Descriptive Title]
# Author: [from project context]
# Purpose: [What this script does]
# Inputs: [Data files]
# Outputs: [Figures, tables, RDS files]
# ============================================================

# 0. Setup ----
library(here)
library(tidyverse)
library(fixest)
library(modelsummary)

set.seed(42)

# Replace "academic_paper" with the target output folder under 04_paper/.
dir.create(here("04_paper", "academic_paper", "tables"), recursive = TRUE, showWarnings = FALSE)
dir.create(here("04_paper", "academic_paper", "figures"), recursive = TRUE, showWarnings = FALSE)

# 1. Data Loading ----

# 2. Exploratory Analysis ----

# 3. Main Analysis ----

# 4. Tables and Figures ----

# 5. Export ----
# saveRDS(model_fit, here("03_analysis", "scripts", "R", "output", "model_fit.rds"))
# saveRDS(main_results, here("03_analysis", "scripts", "R", "output", "main_results.rds"))
```

---

## Results Summary (Mandatory Artifact)

Every analysis run MUST produce `03_analysis/output/results_summary.md` containing:
- All point estimates with standard errors and significance levels
- Sample sizes for each specification
- Key summary statistics (means, medians, standard deviations of main variables)
- Robustness check results (brief table or comparison)
- Any flags or anomalies discovered during analysis

This file is the primary handoff artifact to the writer agent — the writer traces every numerical claim in the draft back to it when building the `claim_manifest` in `passport.yaml`. Without it, the writer cannot draft the results section.

---

## Dual-Language Mode (`--dual r,python`)

When `--dual [lang1,lang2]` is provided (e.g., `--dual r,python`, `--dual r,julia`):

1. **Data-engineer** runs once — language-agnostic cleaning, saves to `02_data/cleaned/`
2. **Two Coder agents** dispatched in parallel — same strategy memo, different languages (`03_analysis/scripts/R/` and `03_analysis/scripts/py/` or `jl/`)
3. **coder-critic** reviews each implementation independently (max 3 rounds each)
4. **Comparison step** — verify numerical alignment per the tolerances in `${CLAUDE_PLUGIN_ROOT}/skills/analyze/config/replication-tolerances.json` (or `00_admin/domain-profile.md` if the field declares its own):
   - Point estimates must match within declared tolerance
   - Standard errors must match within declared tolerance
   - Flag any divergences with exact values from both languages
5. Save comparison report to `03_analysis/output/cross_language_comparison.md`

### Replication Tolerance Approach

Inspired by Scott Cunningham's replication methodology: **if two independent implementations agree, neither has a bug.** This is the core rationale for dual-language mode.

**Tolerance thresholds:**
- **Floating-point differences are normal.** Minor numerical differences (e.g., 1e-10) between R and Python arise from different linear algebra backends, optimizer defaults, and floating-point arithmetic. These are expected, not bugs.
- **Point estimates:** Must agree within 1e-6 (relative) or as declared in `replication-tolerances.json` / `domain-profile.md`
- **Standard errors:** Must agree within 1e-4 (relative) — SE computation varies more across implementations due to degrees-of-freedom corrections and clustering algorithms
- **P-values:** Must agree on significance at conventional levels (0.01, 0.05, 0.10). If one language says p=0.049 and the other says p=0.051, flag for manual review but do not treat as a bug.
- **Sample sizes:** Must match exactly. Any discrepancy indicates a data handling difference that must be resolved.

**When results diverge beyond tolerance:**
1. Both Coder agents are re-dispatched to investigate
2. Check: different default options (e.g., na.rm handling, convergence criteria)
3. Check: different variable coding or factor ordering
4. The comparison report includes a side-by-side table of all estimates
5. If divergence persists after investigation, escalate to user with exact values from both languages

---

## Bundled Resources

### Templates
| File | Purpose |
|------|---------|
| `${CLAUDE_PLUGIN_ROOT}/skills/analyze/templates/pre-code-report.md` | Mandatory pre-check report format before writing code |
| `${CLAUDE_PLUGIN_ROOT}/skills/analyze/templates/paper-to-code-map.md` | Naming map protocol: paper notation to code variables |
| `${CLAUDE_PLUGIN_ROOT}/skills/analyze/templates/r-script-structure.R` | Boilerplate R script scaffold following INV-14..19 |
| `${CLAUDE_PLUGIN_ROOT}/skills/analyze/templates/python-script-structure.py` | Boilerplate Python script scaffold |
| `${CLAUDE_PLUGIN_ROOT}/skills/analyze/templates/results-summary.md` | Mandatory results summary output for writer handoff |

### References
| File | Purpose |
|------|---------|
| `${CLAUDE_PLUGIN_ROOT}/skills/analyze/references/table-standards.md` | Full table formatting standards: booktabs, coefficient display, panel structure, R packages, file naming |
| `${CLAUDE_PLUGIN_ROOT}/skills/analyze/references/figure-standards.md` | Full figure formatting standards: themes, colors, axis labels, export settings, common plot types |

### Config
| File | Purpose |
|------|---------|
| `${CLAUDE_PLUGIN_ROOT}/skills/analyze/config/replication-tolerances.json` | Tolerances for dual-language replication comparison (point estimates, SEs, p-values) |

### Gotchas
| File | Purpose |
|------|---------|
| `${CLAUDE_PLUGIN_ROOT}/skills/analyze/gotchas.md` | Known failure points: R package quirks, numerical issues, output traps, cross-language divergence sources |

---

## Principles
- **Reproduce, don't guess.** If the user specifies a regression, run exactly that.
- **Show your work.** Print summary statistics before jumping to regressions.
- **Strategy alignment.** If strategy memo exists, code MUST implement it faithfully.
- **Worker-critic pairing.** Coder creates, coder-critic critiques. Never skip review.
- **saveRDS everything.** Every computed object gets saved via `saveRDS()` for downstream use — model fits, cleaned data frames, summary statistics, not just final tables.
- **Publication-ready output.** Tables and figures directly includable in the paper.
- **Overwrite, don't proliferate.** Re-running a script replaces its output in place; provenance lives in git + `passport.yaml`, not date-stamped filenames.
- **Cross-language convergence.** When `--dual` is used, divergence is a bug until proven otherwise.
