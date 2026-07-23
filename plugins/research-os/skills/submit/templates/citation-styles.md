# Citation Styles -- Conversion Reference

Used by `/submit format-convert`. The project default is AEA/economics author-date (the convention baked into `${CLAUDE_PLUGIN_ROOT}/rules/working-paper-format.md` and `${CLAUDE_PLUGIN_ROOT}/rules/content-invariants.md` INV-4/INV-9). This file gives the in-text and reference-list conventions for the five alternate styles `passport.yaml` `meta.citation_style` supports, so a conversion is mechanical rather than improvised.

---

## AEA / Economics (project default, for contrast)

- **In-text:** `\citet{smith2024}` -> "Smith (2024)"; `\citep{smith2024}` -> "(Smith, 2024)"
- **Multiple authors:** 2 authors "Smith and Jones (2024)"; 3+ "Smith et al. (2024)"
- **Reference list:** alphabetical by author surname, hanging indent, journal name spelled out, volume(issue): pages.
- **Stars:** AEA journals use no significance stars (INV-4) -- report SEs/CIs instead. Non-AEA economics journals typically do use stars.
- **Package:** `biblatex` + `biber`, `authoryear` style (INV-9).

## APA (7th edition)

- **In-text:** author-date, same shape as AEA -- "(Smith, 2024)" / "Smith (2024)". Page numbers required for direct quotes: "(Smith, 2024, p. 12)".
- **3+ authors:** "Smith et al." from the first citation (APA 7 dropped the "6+ authors" threshold from APA 6).
- **Reference list:** "References," alphabetical, hanging indent. Journal article: `Author, A. A. (Year). Title of article. Journal Name, Volume(Issue), pages. https://doi.org/xxxx`. Title sentence-case; journal name and volume italicized.
- **`biblatex` style:** `apa` (via the `biblatex-apa` package) or convert to `natbib` + `apalike` if the target venue requires it.

## Chicago (17th edition -- two variants, ask the user which)

- **Author-Date variant:** in-text "(Smith 2024, 12)" -- no comma before year, page appended directly. Reference list "References," alphabetical.
- **Notes-Bibliography variant:** in-text is a superscript footnote number; full citation in the footnote on first use, shortened on repeat; a "Bibliography" section duplicates full citations alphabetically. This variant has no in-text author-date markers at all -- every `\citet`/`\citep` becomes a `\footnote{}`.
- **`biblatex` style:** `chicago-authordate` or `chicago-notes` (via `biblatex-chicago`).

## MLA (9th edition)

- **In-text:** parenthetical author-page, no year: "(Smith 12)". No comma between author and page.
- **Reference list:** "Works Cited," alphabetical. Journal article: `Author. "Title of Article." Journal Name, vol. X, no. Y, Year, pp. pages.`
- **Note:** MLA is uncommon for economics/quant social science journals -- confirm the venue actually wants it before converting (more common for humanities-adjacent or interdisciplinary outlets).
- **`biblatex` style:** `mla` (via `biblatex-mla`).

## IEEE

- **In-text:** numbered, bracketed, in citation order (not alphabetical): "[3]" or "[3], [7]". Renumber if a citation is added or removed mid-revision -- this is the main source of conversion errors.
- **Reference list:** "References," numbered in citation order (not alphabetical). Journal article: `[3] A. Smith, "Title of article," Journal Name, vol. X, no. Y, pp. pages, Year.`
- **`biblatex` style:** `ieee` (via `biblatex-ieee`), or `\usepackage[style=ieee]{biblatex}`.

## Vancouver (ICMJE -- common in medicine/health economics)

- **In-text:** numbered, superscript or bracketed, in citation order: "Smith showed X.¹" or "Smith showed X [1]."
- **Reference list:** numbered in citation order. Journal article: `1. Smith A. Title of article. Journal Abbrev. Year;Volume(Issue):pages.` Author names as surname + initials, no periods between initials.
- **`biblatex` style:** `vancouver` (via `biblatex-vancouver`), or `numeric` with `sorting=none`.

---

## Conversion Checklist

- [ ] In-text citation commands converted (author-date <-> numbered <-> footnote, per style above)
- [ ] Reference-list sort order matches the style (alphabetical vs. citation order)
- [ ] Reference-list entry format matches the style (field order, punctuation, italics)
- [ ] `biblatex` style option updated in the preamble; recompile and check for `??` citations
- [ ] Significance-star convention (INV-4) re-checked against the *new* target journal, not just the style guide
- [ ] No fabricated fields -- missing DOIs/pages marked `[MISSING: field]`, never invented
- [ ] If numbered (IEEE/Vancouver): renumbering re-verified after any citation added/removed
