# Talk Skill -- Gotchas

Known failure points and edge cases for presentation creation.

- Notation in talks must match the paper exactly (INV-20). Different subscripts or variable names will confuse the audience.
- Every claim on a slide must appear in the manuscript (INV-21). No orphan results.
- Beamer `\pause` within `itemize` can cause spacing issues -- use `\onslide` for complex reveals.
- The job market talk is the most important format. Allocate time for iteration.
- Talk scoring is advisory (non-blocking) -- a low score won't stop the pipeline, but it should prompt revision.
- Custom Beamer environments from the project preamble aren't defined in the scaffold template -- check `04_paper/academic_paper/preambles/` for project-specific environments.
- `aspectratio=169` is standard for modern projectors. Only use 4:3 if specifically requested.
- Talks live in `05_outreach/talks/`; figures are referenced from `04_paper/academic_paper/figures/` or `03_analysis/output/` via relative paths (`../../...`). If a figure path 404s, confirm the relative path is correct.
