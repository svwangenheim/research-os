# AI-Use Disclosure Statement -- Venue-Family Templates

Used by `/submit ai-disclosure`. Pick the family matching the target venue; fall back to Generic if unlisted, and flag that the user should verify against the venue's actual current policy (these policies change often).

**Ground every statement in fact.** Fill `[stage: yes/no]` from `passport.yaml` `pipeline.stages` and `00_admin/process/journal.md` -- never claim a stage that didn't run, never omit one that did.

---

## Economics Journals (AEA-style)

> During the preparation of this manuscript, the author(s) used AI-assisted tools for the following stages: [literature search and screening: yes/no] [identification-strategy drafting: yes/no] [code generation/analysis: yes/no] [manuscript drafting/editing: yes/no]. All statistical results were independently verified against script output by the author(s). All citations were checked against the original sources. The author(s) take full responsibility for the content of this manuscript.

Placement: footnote on the title page, or a brief paragraph in the Acknowledgments.

## ICMJE-Style / Biomedical Journals

> **Declaration of AI Use.** The author(s) declare that [generative AI / AI-assisted technologies] were used during the preparation of this work for [list stages, e.g. "literature search, language editing, and code generation"]. No AI tool is listed as an author. The author(s) reviewed and edited all AI-assisted output and take full responsibility for the accuracy and integrity of the work, per [journal name]'s authorship policy.

Placement: a dedicated "Declaration of AI Use" section, typically before References or in the Methods.

## Funding-Body / Grant Deliverables (e.g. NSF, NIH, EU Horizon)

> This [report/deliverable] was prepared with the assistance of AI tools for [stage list]. All substantive analysis, interpretation, and conclusions are the author(s)' own. AI assistance is disclosed per [funder]'s responsible-AI-use guidance; no confidential or pre-decisional funder information was processed by any AI tool.

Placement: a short paragraph in the report's front matter or methodology section.

## Preprint Servers (arXiv, SSRN, NBER, IZA)

> AI-assisted tools were used in preparing this preprint for [stage list]. This disclosure is provided voluntarily in the interest of transparency; [server name] does not currently mandate a specific disclosure format.

Placement: footnote or brief note in the abstract page.

## Generic Fallback (venue policy not found)

> This work was prepared with AI assistance for [stage list, reconstructed from `passport.yaml`]. The author(s) reviewed all AI-assisted content, verified all quantitative claims against underlying data and analysis, and take full responsibility for the final manuscript. **[Verify the target venue's current AI-disclosure policy before submission -- this statement uses generic language, not a venue-specific requirement.]**

---

## What Counts as a "Stage" (source: `passport.yaml` `pipeline.stages`)

| Stage | Disclose as |
|-------|-------------|
| discovery (`/discover`) | Literature search and screening; research-idea development |
| strategy (`/strategize`) | Identification-strategy / theory drafting |
| analysis (`/analyze`) | Code generation and statistical analysis |
| writing (`/write`) | Manuscript drafting and language editing |
| review (`/peer-review`) | Internal review/critique (not the journal's own peer review -- do not conflate) |
| revision (`/revise`) | Response-letter drafting |

Never disclose "peer review" in a way that could be read as claiming the *journal's* peer review process itself used AI -- `/peer-review` here is research-os's internal quality-control step, not a substitute for or component of the venue's editorial process. Make that distinction explicit if there's any risk of confusion.
