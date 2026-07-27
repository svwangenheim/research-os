---
name: submit
description: Submission phase (terminal) - journal targeting, replication package, audit, citation conversion, AI-use disclosure, final gate. Requires the ARS integrity gate to have passed.
argument-hint: "[mode: target | package | audit | format-convert | ai-disclosure | final] [journal name / citation style / venue (optional)]"
allowed-tools: Read,Grep,Glob,Write,Edit,Bash,Task
---

# Submit

Submission pipeline with six modes covering journal selection through final verification.

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

### `/submit audit` -- Audit Replication Package
Verify replication package completeness.

**Agent:** Verifier (submission mode -- 10 checks, `${CLAUDE_PLUGIN_ROOT}/skills/submit/templates/audit-10-checks.md`)

Checks: master script exists and runs; all tables/figures reproduce; README complete; data documentation present; numbered script order; dependencies listed; runtime documented; output paths match `04_paper/academic_paper/tables/` and `.../figures/`; no hardcoded paths.

Save to `04_paper/submission/replication_audit.md`, updating in place. Pass/fail per check; binary for aggregation (0 any failure, 100 all pass) -- contributes 5% to the weighted overall score.

### `/submit format-convert [style] [--apply]` -- Multi-Style Citation Conversion

Convert the manuscript's citations and reference list from the project default (AEA/economics author-date) to another style -- for retargeting a submission outside economics, or to preview fit before committing. Supports **apa | chicago | mla | ieee | vancouver** (`passport.yaml` `meta.citation_style` accepts the same set, plus `aea`).

**Agent:** Writer (format-conversion mode)

Workflow:
1. Read `01_literature/bibliography.bib` and the manuscript's `\citet{}`/`\citep{}` calls.
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
3. Run `/submit audit` (replication audit) if not done recently.
4. Check the score gate: overall aggregate >= 95, all components >= 80 (`${CLAUDE_PLUGIN_ROOT}/rules/quality.md` Section 1).
5. Save the gate summary to `04_paper/submission/quality_gate.md`, updating in place, and refresh the dashboard: run `/dashboard`.
6. **If PASS:** generate the cover letter draft (`${CLAUDE_PLUGIN_ROOT}/skills/submit/templates/cover-letter.tex`) and the submission checklist (`${CLAUDE_PLUGIN_ROOT}/skills/submit/templates/submission-checklist.md`) to `04_paper/submission/`. Remind the user to run `/submit ai-disclosure [venue]` if the target venue requires one, and `/submit format-convert [style]` if the target journal's citation convention differs from the project default.
7. **If FAIL:** list blocking issues (component scores below 80, overall below 95, or unresolved integrity items) and stop.

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
