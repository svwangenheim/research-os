---
name: submit
description: Submission phase (terminal) - journal targeting, replication package, environment capture, audit, citation conversion, AI-use disclosure, final gate. Requires the ARS integrity gate to have passed.
argument-hint: "[mode: target | package | environment | audit | format-convert | ai-disclosure | final] [journal name / citation style / venue (optional)] [--apply] [--docker]"
allowed-tools: Read,Grep,Glob,Write,Edit,Bash,Task
---

# Submit

Submission pipeline with seven modes covering journal selection through final verification.

**Input:** `$ARGUMENTS` -- mode keyword, optionally followed by a journal name, citation style, or venue.

State lives in **`passport.yaml`** (schema: `${CLAUDE_PLUGIN_ROOT}/templates/passport.yaml`). Paths follow `${CLAUDE_PLUGIN_ROOT}/rules/folder-map.md`: the replication package lives in `03_analysis/replication/`; journal recommendations, the AI-disclosure statement, the citation-style conversion, the cover letter, and the quality-gate summary live in `04_paper/submission/`. Outputs obey `${CLAUDE_PLUGIN_ROOT}/rules/output-discipline.md`: **update the existing recommendation/audit/gate file in place with a `## Changelog`.** Submission is the terminal phase (`passport.yaml` `pipeline.stages.submission`, gate 95) and **requires the ARS integrity gate to have already passed** (`${CLAUDE_PLUGIN_ROOT}/rules/quality.md` Section 3, `${CLAUDE_PLUGIN_ROOT}/rules/permissions.md` verifier entry) -- `/submit` does not run that gate itself; it checks that `/peer-review` already cleared it and refuses to proceed if `passport.yaml` `integrity.unresolved` is non-empty.

---

## Modes

### `/submit target [journal]` -- Journal Targeting
Get ranked journal recommendations.

**Agent:** Orchestrator (journal selection function)

Considers: contribution fit, methodology fit, audience fit, recent publications, desk rejection risk. Consults `${CLAUDE_PLUGIN_ROOT}/references/journal-profiles.md` for journal tiers and `00_admin/domain-profile.md` for field/target journals.

Output: ranked list of 3 target journals with rationale. Save to `04_paper/submission/journal_recommendations.md`, updating in place.

### `/submit package [language]` -- Build Replication Package
Assemble an AEA-compliant replication package (adapt file naming to non-AEA journals when `journal-profiles.md` specifies a different convention).

**Agents:** Coder + Verifier

Produces:
- Master script that runs all analyses end-to-end
- README with data sources, computational requirements, instructions (`${CLAUDE_PLUGIN_ROOT}/skills/submit/templates/replication-readme.md`)
- Data documentation and codebook
- Organized file structure per AEA standards

Save to `03_analysis/replication/`.

Run `/submit environment` alongside this: `package` assembles the deposit, `environment` captures the lockfiles, seeds, and runtime the deposit's README has to declare.

### `/submit environment [--docker]` -- Capture the Computational Environment

Record what it takes to run this project's analysis on another machine. `/submit package` builds the deposit (scripts, data documentation, README); `environment` supplies the half of that deposit a replicator cannot reconstruct from the files: exact package versions, the RNG state, and the runtime. Target audience is the **AEA Data Editor** and the openICPSR deposit form, whose reviewers reject packages that list dependencies without versions.

**Agent:** Verifier (environment mode)

Run this before `/submit audit` -- the audit's "dependencies listed" and "runtime documented" checks read what this mode produces.

#### 1. Detect the stack

```bash
ls -1 03_analysis/scripts/R 03_analysis/scripts/py 03_analysis/scripts/jl 2>/dev/null
```

A language counts as in use if its script directory holds at least one script that the master script actually calls. A directory with one abandoned prototype is not a dependency -- say so rather than emitting a lockfile for it.

#### 2. Emit the matching lockfiles

**Match the tooling the project already uses. Do not introduce a new dependency manager as part of a submission.** If the project pins with `requirements.txt`, produce `requirements.txt`; do not switch it to `uv` or conda because that would be tidier. Introducing tooling at submission time invalidates every instruction already written in the README.

| Stack | Emit | How |
|---|---|---|
| **R** | `renv.lock` **and** `sessionInfo.txt` | `renv::snapshot()` if `renv/` exists; otherwise `renv::init()` first and say that you did. `sessionInfo.txt` from `writeLines(capture.output(sessionInfo()), "sessionInfo.txt")` -- it records the R version, platform, BLAS/LAPACK, and locale, none of which are in `renv.lock`, and BLAS differences are a real source of last-digit non-reproducibility. |
| **Python** | whichever of `requirements.txt`, `environment.yml`, `uv.lock` the project already uses | `uv.lock` if `uv.lock` or `pyproject.toml` with a `[tool.uv]` section is present; `environment.yml` if the project is conda-based (`environment.yml` present or a conda prefix in the README); otherwise `requirements.txt` with `==` pins, never bare names or `>=`. Record the Python version explicitly -- `requirements.txt` does not carry it. |
| **Julia** | `Project.toml` + `Manifest.toml` | `Pkg.instantiate()` then commit both. `Manifest.toml` is the lockfile; `Project.toml` alone is not enough. |
| **Stata** | `version` statement + ado inventory | Confirm every `.do` opens with a `version` statement matching the version actually used. Inventory user-written commands (`ssc`/SSC or `net install` packages: `reghdfe`, `ivreghdfe`, `estout`, `coefplot`, ...) with the version each was installed at, and ship them under the package's `ado/` directory -- the Data Editor requires user-written ados to travel with the deposit, since SSC has no version archive. |

Record the operating system and CPU architecture the analysis was actually run on. "Windows 11, x86-64" is a fact a replicator needs when a result does not reproduce.

#### 3. Seeds and RNG

Grep the scripts for the master seed and the generator kind:

```bash
grep -rn "set.seed\|RNGkind\|np.random\|default_rng\|Random.seed!\|MersenneTwister\|set seed" 03_analysis/scripts/
```

Record, per script that uses randomness: the seed value, where it is set (it must be set before the first stochastic call, not mid-script), and the generator kind. In R this means `RNGkind()` as well as `set.seed()` -- R's default generator changed in 3.6.0, and a script that sets a seed but not the kind does not reproduce across that boundary. In Python, prefer a seeded `np.random.default_rng(seed)` passed explicitly over the global `np.random.seed()`.

**WARN loudly if the pipeline is randomized and no master seed is set.** Bootstrap, simulation, Monte Carlo, permutation or randomization inference, cross-validation splits, random subsampling, and stochastic optimizers all count. The warning names each affected script and states plainly that the reported numbers cannot be reproduced exactly as they stand. This is a blocking finding for `/submit final`, not an advisory: an unseeded randomized pipeline fails the AEA reproducibility standard, and it is also how a result that is really noise survives to publication.

#### 4. Optional pinned Dockerfile (`--docker`)

Only with the explicit flag. Emit a `Dockerfile` in `03_analysis/replication/` that pins the base image **by digest, not by tag** (`FROM rocker/r-ver:4.4.1@sha256:...`), installs the system libraries the stack needs, and restores from the lockfiles produced in step 2 rather than re-resolving dependencies. A Dockerfile whose base is a moving tag and whose installs are unpinned reproduces nothing and is worse than no Dockerfile, because it looks like a guarantee.

#### 5. Paste-ready "Computational requirements" block

Produce a block the author pastes into the replication README and the openICPSR deposit form:

```markdown
## Computational requirements

### Software
- R 4.4.1 (2024-06-14), platform x86_64-w64-mingw32
  - Package versions pinned in `renv.lock`; restore with `renv::restore()`
  - Full session details in `sessionInfo.txt`
- Stata 18.0 MP (4 cores)
  - User-written commands shipped in `ado/`: reghdfe 6.12.3, estout 3.31

### Randomness
- Master seed: 20260811, set in `03_analysis/scripts/R/00_master.R` line 12
- RNG kind: Mersenne-Twister, Inversion (R >= 3.6.0 default)
- Affects: `04_bootstrap.R` (1,000 replications)

### Memory, runtime, and storage
- Run on Windows 11, x86-64, 32 GB RAM, 8 cores
- Approximate runtime: 3 hours 40 minutes end to end; `04_bootstrap.R` is 3 hours of that
- Peak memory: ~12 GB
- Output storage: ~2 GB

### Data availability
- See `03_analysis/replication/README.md` for source, access class, and terms
```

Fill every field from what was measured or read. Do not estimate a runtime you did not observe -- write `[NOT MEASURED: run the master script and record wall time]` instead. A wrong runtime wastes a replicator's afternoon and is one of the Data Editor's standing complaints.

Save the block to `03_analysis/replication/computational_requirements.md`, updating in place with a `## Changelog`, and place the lockfiles at the project root or in `03_analysis/replication/` following whatever convention the project already uses.

### `/submit audit` -- Audit Replication Package
Verify replication package completeness.

**Agent:** Verifier (submission mode -- 10 checks, `${CLAUDE_PLUGIN_ROOT}/skills/submit/templates/audit-10-checks.md`)

Checks: master script exists and runs; all tables/figures reproduce; README complete; data documentation present; numbered script order; dependencies listed; runtime documented; output paths match `04_paper/academic_paper/tables/` and `.../figures/`; no hardcoded paths.

Save to `04_paper/submission/replication_audit.md`, updating in place. Pass/fail per check; binary for aggregation (0 any failure, 100 all pass) -- contributes 5% to the weighted overall score.

### `/submit format-convert [style] [--apply]` -- Multi-Style Citation Conversion

Convert the manuscript's citations and reference list from the project default (AEA/economics author-date) to another style -- for retargeting a submission outside economics, or to preview fit before committing. Supports **apa | chicago | mla | ieee | vancouver** (`passport.yaml` `meta.citation_style` accepts the same set, plus `aea`).

**Agent:** Writer (format-conversion mode)

Workflow:
1. Read `01_literature/bibliography.bib` and the manuscript's `\citet{}`/`\citep{}` calls. For each bibkey, resolve its `wiki_path` from `passport.yaml` `literature_corpus` and read that `<main_wiki>/20_summaries/` note's frontmatter (`authors`, `year`, `doi`, `journal`, `volume`, `issue`, `pages`). The wiki summary is the source of truth for this metadata -- it often carries a DOI, volume, or page range the `.bib` entry is missing, and every style below requires fields the AEA default does not. Resolve the thematic wiki via the standard ladder in `${CLAUDE_PLUGIN_ROOT}/rules/wiki-integration.md` (`--wiki` > `passport.yaml` `meta.main_wiki` > `.research-os-wiki` > the registry's only wiki), reading `~/.claude/vaults.json` for the path. **Read only** -- `/submit` never writes to the wiki, and a field the note does not have stays `[MISSING: field]` per step 5. If no wiki is resolvable, skip this step silently.
2. Look up the target style's in-text and reference-list conventions in `${CLAUDE_PLUGIN_ROOT}/skills/submit/templates/citation-styles.md`.
3. **Without `--apply` (default, non-destructive):** produce a preview report at `04_paper/submission/citation_style_preview_[style].md` showing what would change (sample converted citations, reference-list format, any manuscript claims that depend on the AEA no-stars convention (INV-4) and would need to change too) -- the manuscript itself is untouched.
4. **With `--apply`:** convert the manuscript's citation commands and reference list in place (`04_paper/academic_paper/main.tex` and/or `sections/*.tex`), update `passport.yaml` `meta.citation_style` to the new value, and re-flag INV-4 (significance stars) if the target journal's convention differs from the current one. This is a manuscript edit -- re-run `/peer-review --proofread` afterward.
5. Never fabricate a reference-list entry to fit a style's required fields (e.g. a missing DOI) -- mark it `[MISSING: field]` for the user to fill in.

### `/submit ai-disclosure [venue]` -- AI-Use Disclosure Statement

Generate a venue-appropriate statement disclosing AI assistance used in producing the paper -- grounded in what actually happened in this project, not generic boilerplate.

**Agent:** Writer (disclosure mode)

Workflow:
1. **Reconstruct actual AI use** from `passport.yaml` `pipeline.stages` (which phases ran) and `00_admin/process/journal.md` -- e.g. literature search and screening (`/discover lit`), identification-strategy drafting (`/strategize`), code generation (`/analyze`), drafting/editing assistance (`/write`), and review (`/peer-review`). Do not claim uses that didn't happen; do not omit uses that did.
2. Select the disclosure template matching the venue's policy family from `${CLAUDE_PLUGIN_ROOT}/skills/submit/templates/ai-disclosure-statement.md` (economics-journal / ICMJE-style / funding-body / preprint-server families -- fall back to the generic template if the venue isn't listed, and flag that the user should check the venue's actual policy).
3. Draft the statement in the venue's expected location (methods/acknowledgments footnote, or a separate disclosure section) and register any human-in-the-loop verification performed (e.g., "all statistical results were verified against script output; all citations were checked by the author").
4. Save to `04_paper/submission/ai_disclosure_statement.md`, updating in place. Flag it clearly: **the user must confirm accuracy and insert it per the venue's actual submission instructions** -- this is a draft, not a filed disclosure.

### `/submit final [journal]` -- Final Submission Gate
Full verification + score enforcement + submission checklist.

Workflow:
1. Confirm the ARS integrity gate has passed (`passport.yaml` `integrity.unresolved` is empty) -- if not, stop and point to `/peer-review`.
2. Run `/peer-review --all` (comprehensive review) if not done recently.
3. Run `/submit environment` if the lockfiles or `03_analysis/replication/computational_requirements.md` are missing or older than the newest analysis script. An unresolved unseeded-randomness warning from that mode blocks this gate.
4. Run `/submit audit` (replication audit) if not done recently.
5. Check the score gate: overall aggregate >= 95, all components >= 80 (`${CLAUDE_PLUGIN_ROOT}/rules/quality.md` Section 1).
6. Save the gate summary to `04_paper/submission/quality_gate.md`, updating in place, and refresh the dashboard: run `/dashboard`.
7. **If PASS:** generate the cover letter draft (`${CLAUDE_PLUGIN_ROOT}/skills/submit/templates/cover-letter.tex`) and the submission checklist (`${CLAUDE_PLUGIN_ROOT}/skills/submit/templates/submission-checklist.md`) to `04_paper/submission/`. Remind the user to run `/submit ai-disclosure [venue]` if the target venue requires one, and `/submit format-convert [style]` if the target journal's citation convention differs from the project default.
8. **If FAIL:** list blocking issues (component scores below 80, overall below 95, unresolved integrity items, or an unseeded randomized pipeline) and stop.

---

## Bundled Resources

| Resource | Path | When |
|----------|------|------|
| Submission checklist | `${CLAUDE_PLUGIN_ROOT}/skills/submit/templates/submission-checklist.md` | `/submit final` -- pre-submission verification |
| Cover letter | `${CLAUDE_PLUGIN_ROOT}/skills/submit/templates/cover-letter.tex` | `/submit final` -- draft cover letter |
| Replication README | `${CLAUDE_PLUGIN_ROOT}/skills/submit/templates/replication-readme.md` | `/submit package` -- AEA-compliant README |
| Audit checklist | `${CLAUDE_PLUGIN_ROOT}/skills/submit/templates/audit-10-checks.md` | `/submit audit` -- verifier submission mode |
| Citation styles | `${CLAUDE_PLUGIN_ROOT}/skills/submit/templates/citation-styles.md` | `/submit format-convert` -- apa/chicago/mla/ieee/vancouver conventions |
| AI-disclosure statement | `${CLAUDE_PLUGIN_ROOT}/skills/submit/templates/ai-disclosure-statement.md` | `/submit ai-disclosure` -- venue-family boilerplate |
| Gotchas | `${CLAUDE_PLUGIN_ROOT}/skills/submit/gotchas.md` | Always -- known failure points |

---

## Principles
- **Score >= 95 + all components >= 80. No exceptions.**
- **The integrity gate is a precondition, not this skill's job.** `/submit` checks `passport.yaml` `integrity`; it does not re-run the gate itself -- that's `/peer-review`'s.
- **Don't skip verification.** Even if reports exist, check they're recent.
- **If it fails, stop.** Don't generate materials for a failing paper.
- **Cover letter and disclosure statement are drafts.** The user must review both before sending.
- **Disclosure must be true.** Ground the AI-use statement in what `passport.yaml` and the journal actually show happened -- never a generic boilerplate.
- **Style conversion previews by default.** `format-convert` only edits the manuscript with an explicit `--apply`.
- **Pin, don't re-tool.** `environment` records the dependency manager the project already uses. Switching tooling at submission time invalidates the instructions already written.
- **An unseeded randomized pipeline is a blocking finding.** Not an advisory. Numbers that cannot be regenerated fail the reproducibility standard whatever the rest of the package looks like.

## Node contract

This skill executes graph node `verifier` in `${CLAUDE_PLUGIN_ROOT}/graph/pipeline.json` —
**terminal**: `graph.py` marks it `terminal: true`, no re-entry after this node is `done`. On
completion: `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/graph.py" record verifier --score <N>`.
