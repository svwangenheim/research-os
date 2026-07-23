# Content Invariants

These are non-negotiable. Every agent checks against them. Violations are deductions, not suggestions. Critics cite invariant numbers (e.g., "violates INV-3") in their reports.

---

## Output types

research-os produces five first-class output types, declared per project in `passport.yaml` `meta.output_types` and scaffolded into `04_paper/<output>/`:

| Output type | Scope of the invariants below |
|-------------|-------------------------------|
| `academic_paper` | All Paper invariants (INV-1 … INV-13) apply — LaTeX, booktabs, biblatex, JEL codes, etc. |
| `policy_brief` | DZ house style (see the DZ output skills/templates). Universal invariants apply; LaTeX-specific ones apply only when the brief is built in LaTeX. |
| `fachtext` | DZ house style. Universal invariants apply. |
| `hintergrundpapier` | DZ house style. Universal invariants apply. |
| `geldbrief` | DZ house style. Universal invariants apply. |

**Universal invariants** — apply to every output type regardless of format: Code (INV-14 … INV-19), Traceability (INV-22), consistent notation (INV-7), the causal-language rule (INV-8), and the citation-honesty rule (never fabricate a citation; mark unverifiable entries `% UNVERIFIED`; cite the published version of a working paper). The ARS integrity gate in `quality.md` enforces these across all output types.

**Academic-paper / LaTeX invariants** — INV-1 … INV-13 and the talk invariants INV-20/INV-21 govern LaTeX manuscripts and Beamer talks. DZ brief formatting (typography, length, section conventions) is governed by the DZ output skills and their templates, not restated here — do not invent LaTeX rules for the DZ types.

---

## Paper

**INV-1.** Every table has notes explaining key variables, sample, and data source — via `threeparttable` + `tablenotes` (traditional) or `talltblr` with `note{}` keys (tabularray).

**INV-2.** Every figure has a `\caption{}` with a note explaining what is shown, how to read it, and the data source.

**INV-3.** No `\hline` — use `\toprule`, `\midrule`, `\bottomrule` (booktabs). No vertical rules.

**INV-4.** Significance stars follow the journal profile. AEA journals: no stars, report standard errors and use confidence intervals. Default: stars with note defining thresholds.

**INV-5.** Abstract is 150 words or fewer.

**INV-6.** JEL codes and keywords present after the abstract.

**INV-7.** Notation is consistent across all sections — the same symbol means the same thing everywhere. Different concepts get different symbols.

**INV-8.** Every causal claim has a corresponding identification section. No causal language in descriptive papers.

**INV-9.** `biblatex` + `biber`, not `natbib` + `bibtex`.

**INV-10.** `hyperref` loaded second-to-last in preamble; `cleveref` loaded immediately after it.

**INV-11.** Numbers in text match the tables and figures exactly. No rounding discrepancies, no stale values.

**INV-12.** No titles inside ggplot/matplotlib figures. Titles go in LaTeX `\caption{}`. Panel labels ("Panel A: ...") inside multi-panel figures are fine.

**INV-13.** R/Python/Julia scripts export bare `tabular` environments — no `\begin{table}`, `\caption{}`, or notes. The paper's `main.tex` wraps them.

## Code

**INV-14.** `set.seed()` (or language equivalent) called exactly once, at the top of the main script, if any stochastic element exists.

**INV-15.** All packages/libraries loaded at the top of the script, before any data loading or computation.

**INV-16.** No absolute paths. All paths relative to project root via `here()` (R), `pathlib.Path` (Python), or `joinpath(@__DIR__, ...)` (Julia).

**INV-17.** No growing vectors/lists in loops. Pre-allocate result containers or use vectorized operations.

**INV-18.** Output files go to the path specified by the Output Organization setting in `CLAUDE.md` (analysis output defaults to `03_analysis/output/`; paper tables/figures to `04_paper/<output>/`).

**INV-19.** No prohibited functions: `setwd()` / `os.chdir()` / `cd()`, `rm(list = ls())`, `install.packages()` in scripts, `attach()` / `detach()`.

## Talk

**INV-20.** Notation in talk matches paper exactly — same symbols, same subscripts, same definitions.

**INV-21.** Every claim on a slide is traceable to the paper. No orphan results or numbers that don't appear in the manuscript.

## Traceability

**INV-22.** Every non-trivial claim in the manuscript (or DZ output) must have an entry in `passport.yaml` `claim_manifest`, with an `evidence_origin` traceable to a real source: a `bibkey` in `literature_corpus`, a `data:<path>`, a specific `analysis:<script>` line and output file, or explicit `reasoning`. This is what the ARS integrity gate (`quality.md`) reads.

---

## How Agents Use This File

| Agent | Checks | Action on Violation |
|-------|--------|-------------------|
| **writer-critic** | INV-1 through INV-13, INV-22 | Deduct per scoring rubric |
| **coder-critic** | INV-13 through INV-19 | Deduct per scoring rubric |
| **storyteller-critic** | INV-20, INV-21 | Deduct per scoring rubric |
| **verifier** | INV-9, INV-10, INV-14, INV-15, INV-16, INV-19, INV-22 | FAIL if present (integrity gate) |
| **lint hook** | INV-14, INV-15, INV-16, INV-19 | Advisory warning |
