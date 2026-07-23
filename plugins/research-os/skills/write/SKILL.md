---
name: write
description: Draft sections for any research-os output — academic paper (IMRaD, literature review, theory, case study, conference) or DZ output (policy brief, Fachtext, Hintergrundpapier, Geldbrief) — using paragraph-level argument moves. Cleanup pass strips AI patterns; style-guide mode extracts the author's voice. Writing phase of the pipeline.
argument-hint: "[section or mode: intro | strategy | results | conclusion | abstract | full | humanize | style-guide] [file path (optional)]"
allowed-tools: Read,Grep,Glob,Write,Edit,Task
---

# Write

Draft output sections, apply a cleanup pass, or extract a personal style guide from prior papers by dispatching the **Writer** agent.

**Input:** `$ARGUMENTS` — section name or mode, optionally followed by file path.

State lives in **`passport.yaml`** (schema: `${CLAUDE_PLUGIN_ROOT}/templates/passport.yaml`). Paths follow `${CLAUDE_PLUGIN_ROOT}/rules/folder-map.md`: section files → `04_paper/<output>/sections/`, assembled doc → `04_paper/<output>/main.tex`, figures/tables → `04_paper/<output>/{figures,tables}/`. Outputs obey `${CLAUDE_PLUGIN_ROOT}/rules/output-discipline.md`: **the writer updates section files in place — it never spawns `intro-v2.tex`.** As it drafts, the writer records every non-trivial claim in `passport.yaml` `claim_manifest` (INV-22, `${CLAUDE_PLUGIN_ROOT}/rules/content-invariants.md`) so the integrity gate can trace each to a real source. Writing-phase severity is Strict/high (`${CLAUDE_PLUGIN_ROOT}/rules/quality.md`); the writer-critic scores in `/peer-review` and its score lands in `passport.yaml` `pipeline.stages.writing`.

---

## Modes

### `/write [section]` — Draft Output Section
Draft a specific section: `intro`, `strategy`, `results`, `conclusion`, `abstract`, or `full`.

**Agent:** Writer
**Output:** section file in `04_paper/<output>/sections/` (LaTeX for `academic_paper` and LaTeX-built DZ outputs; the DZ skill's format otherwise)

Workflow:

#### 1. Context Gathering

Before drafting, read all available context:
1. Read the existing draft in `04_paper/<output>/` (if it exists)
2. Read `01_literature/sources/` and `00_admin/research_outline.md` for notes, outlines, research spec
3. Read the `research:` block in `passport.yaml` and the relevant `01_literature/reviews/<question-slug>.md`
4. Read `00_admin/domain-profile.md` for field conventions
5. Check `01_literature/bibliography.bib` for available citations
6. Scan `04_paper/<output>/tables/` and `04_paper/<output>/figures/` for generated output
7. Read `03_analysis/output/results_summary.md` if it exists (from the Coder)

#### 2. Paper Type Detection (the planner step)

Before routing, the planner detects the output type from `passport.yaml` `meta.output_types` + `research.paper_type` (and the strategy memo / existing draft), then selects the matching scaffold from `${CLAUDE_PLUGIN_ROOT}/skills/write/templates/section-templates.md`. Recognized types:

**Academic-paper family:**
- **`imrad`** — the empirical/IMRaD family, with four design sub-types the writer must further distinguish:
  - **Reduced-form** — DiD, IV, RDD, event study
  - **Structural** — model estimation, counterfactual simulations
  - **Theory + empirics** — propositions tested with data
  - **Descriptive / measurement** — new data, new measure, stylized facts
- **`literature_review`** — review/synthesis (PRISMA structure when systematic)
- **`theory`** — pure theory paper (formal argument is the contribution)
- **`case_study`** — case study
- **`conference`** — compressed IMRaD to a page/word limit

**DZ output family (first-class):**
- **`policy_brief`**, **`fachtext`**, **`hintergrundpapier`**, **`geldbrief`** — DZ house-style outputs. The writer scaffolds their section backbones from section-templates.md; detailed house style is owned by the DZ output skills/templates. Universal invariants (traceability, notation, causal-language, citation-honesty) apply; LaTeX invariants apply only when the output is built in LaTeX (`${CLAUDE_PLUGIN_ROOT}/rules/content-invariants.md`).

This determines which section templates the Writer uses.

#### 3. Section Routing

Based on `$ARGUMENTS`:
- **`full`**: Draft all sections in sequence, pausing between major sections for user feedback
- **`intro`**: Draft introduction (most common request)
- **`strategy`**: Draft empirical strategy (reduced-form), model + estimation (structural), model + tests (theory+empirics), or the equivalent analytical section for DZ outputs
- **`results`**: Draft results — narration style depends on paper type and output type (regression tables, event study figures, counterfactual simulations, evidence sections in a brief, etc.)
- **`conclusion`**: Draft conclusion with type-appropriate ending (policy implications, counterfactual implications, research agenda, or the DZ "bottom line")
- **`abstract`**: Draft abstract / executive summary (must have other sections first)
- **`data`**: Draft data section — expanded for descriptive/measurement papers
- **`model`**: Draft model section (structural, theory+empirics, or theory papers only)
- **No argument**: Ask user (free-form, plain text) which section to draft

#### 4. Dispatch Writer

Dispatch Writer with the detected paper type and argument-move templates for the target section. The writer drafts using paragraph types (motivation, result statement, mechanism, etc.), applies type-specific moves, then runs the cleanup pass. Save to `04_paper/<output>/sections/[section].tex` (updating in place if it exists).

#### 5. Quality Self-Check

Before presenting the draft:
- [ ] Paper type identified and correct scaffold used
- [ ] Every paragraph has an identifiable purpose (argument move type)
- [ ] Findings lead sentences — not buried after setup
- [ ] Design-specific / type-specific elements present (see section-templates.md and the writer agent checklists)
- [ ] Every displayed equation is numbered (`\label{eq:...}`) — LaTeX outputs
- [ ] All `\cite{}` keys exist in `01_literature/bibliography.bib`
- [ ] Introduction/contribution names specific papers
- [ ] Effect sizes stated with units
- [ ] No banned hedging phrases
- [ ] Notation consistent throughout (INV-7)
- [ ] All tables/figures referenced actually exist in `04_paper/<output>/tables/` or `04_paper/<output>/figures/`
- [ ] Results narrated correctly for output type (tables, event study figures, counterfactuals, evidence sections)
- [ ] Personal style guide loaded (not template) — or user prompted to run `/write style-guide`
- [ ] `claim_manifest` in `passport.yaml` updated for all numerical/non-trivial claims (INV-22; format reference `${CLAUDE_PLUGIN_ROOT}/skills/write/templates/claim-source-map.md`)
- [ ] Results/Conclusion only drafted after verifying actual output files exist

#### 6. Present to User

Present sections through drafting gates, pausing for approval at each (`${CLAUDE_PLUGIN_ROOT}/skills/write/templates/drafting-gates.md`):

**GATE 1:** Introduction + Literature positioning → present, wait for approval
**GATE 2:** Data + Empirical Strategy (or Model) → present, wait for approval
**GATE 3:** Results + Robustness + Conclusion → present, wait for approval

For single-section drafts, present the section directly. For `full`, use all three gates. (DZ outputs use the analogous gates: framing → analysis → recommendation/close.)

Flag items that need attention:
- **BLOCKED items:** Results/Conclusion cannot be drafted without output files
- **VERIFY items:** Citations that need user confirmation
- **VOICE items:** Style guide not yet extracted (drafting blocked until resolved)

### `/write style-guide [paper-dir]` — Extract Personal Voice

One-shot extraction of the user's writing voice from their published or drafted papers. Produces `00_admin/personal-style-guide.md`, which the writer auto-loads on every subsequent invocation.

**When to run:**
- Once at the start of a project, after pointing at a directory of the user's prior papers
- After publishing a new paper that shifts voice (re-run to refresh the profile)

**Input:** `$ARGUMENTS` — path to a directory containing prior papers (.tex or .pdf). If omitted, defaults to `01_literature/sources/` and scans for .tex/.pdf files.

**Agent:** Writer (style-extraction mode)
**Output:** `00_admin/personal-style-guide.md`

Workflow:
1. **Discover corpus.** List .tex and .pdf files in the target directory only. **Do NOT scan the thematic wiki (`<main_wiki>/10_sources/`)** — style extraction must use the user's own papers exclusively, not other authors' work from the corpus (the explicit style-guide exception in `${CLAUDE_PLUGIN_ROOT}/rules/wiki-integration.md`). If fewer than 2 papers found, flag and ask before proceeding (style extraction on a single paper overfits).
2. **Sample strategically.** For each paper, extract:
   - The full introduction
   - The first two paragraphs of each major section
   - The abstract and conclusion
   - A random sample of 5–10 results-section paragraphs
   This keeps context usage bounded while capturing voice variation across sections.
3. **Extract patterns.** The Writer (in style-extraction mode, per `${CLAUDE_PLUGIN_ROOT}/skills/write/templates/style-extraction-protocol.md`) produces quantitative and qualitative patterns:
   - Sentence-length distribution (median, 10th–90th pct)
   - Passive-voice frequency, first-person-plural frequency, em dash rate
   - Paragraph opening and closing moves
   - Section-architecture patterns (how introductions open, how results lead)
   - Lexicon: words used repeatedly, words demonstrably avoided
   - Hedging and comparison patterns
   - Citation conventions (textual vs. parenthetical split; papers-per-claim)
   - Tone markers and anti-patterns already stripped
4. **Write to `00_admin/personal-style-guide.md`.** Fill every template section with quoted examples from the corpus. Never invent patterns — if a section has no evidence, write "[insufficient corpus evidence]".
5. **Present summary.** One-paragraph recap of the voice profile: sentence length, passive rate, signature lexicon, distinguishing tone markers. User confirms before the guide takes effect on subsequent `/write` calls.

Principles for the extraction:
- **Ground every claim in the corpus.** Each pattern must have at least one quoted example.
- **Extract, don't prescribe.** The guide records the author's observed behavior, not what the Writer thinks is good style.
- **Don't duplicate `00_admin/domain-profile.md`.** The style guide is about voice; the domain profile is about field conventions.
- **Don't override the working-paper-format invariants.** Voice doesn't trump INV-1..22.

### `/write humanize [file]` — Cleanup Pass Only
Strip AI writing patterns from existing text without rewriting content.

**Agent:** Writer (cleanup mode, `${CLAUDE_PLUGIN_ROOT}/skills/write/templates/cleanup-patterns.md`)
**Output:** Edited file with AI patterns removed

Strips 24 patterns across 4 categories:
- Structural: forced narrative arcs, artificial progression
- Lexical: "delve, leverage, nuanced, robust"
- Rhetorical: rule-of-three, negative parallelisms, em dash overuse
- Formatting: excessive bullet points, promotional language

---

## Section Standards

**All academic paper types share the IMRaD backbone; moves diverge by type — see `${CLAUDE_PLUGIN_ROOT}/skills/write/templates/section-templates.md` for full scaffolds (IMRaD sub-types, literature_review, theory, case_study, conference, and the DZ types).**

| Section | Length | Reduced-Form | Structural | Theory+Empirics | Descriptive |
|---------|--------|-------------|-----------|----------------|-------------|
| Introduction | 1000-1500 | ...preview → result → contribution | ...model preview → counterfactual → contribution | ...theory preview → test result → contribution | ...data innovation → key fact → contribution |
| Data | 800-1200 | Treatment, outcome, controls | Moments that identify parameters | Standard | 1200-1800 (core contribution) |
| Strategy/Model | 800-1500 | Design-specific (DiD/IV/RDD/ES) | Environment → decisions → equilibrium → estimation | Model → propositions → tests | N/A (merged into Data) |
| Results | 800-1500 | Main spec → robustness → heterogeneity | Estimates → model fit → counterfactuals → welfare | Prediction-by-prediction evidence | Key facts → decompositions → implications |
| Conclusion | 500-700 | Policy implications | Counterfactual implications + model limitations | What model gets right/wrong | Research agenda enabled by new data |
| Abstract | 100-150 | Question, design, finding with magnitude | Question, model, counterfactual finding | Question, prediction, test result | Question, measurement, key fact |

DZ outputs follow their own length/structure conventions (headline → context → evidence → recommendation → bottom line, adapted per type) — see section-templates.md and the DZ output skills.

---

## LaTeX Conventions (academic_paper and LaTeX-built DZ outputs)

- `\citet{}` for textual citations ("Smith (2024) shows...")
- `\citep{}` for parenthetical citations ("...is well documented (Smith, 2024)")
- `booktabs` rules (`\toprule`, `\midrule`, `\bottomrule`) — never `\hline` (INV-3)
- Notation protocol: `Y_{it}`, `D_{it}`, `\gamma_i`, `\delta_t`, `\varepsilon_{it}` (`${CLAUDE_PLUGIN_ROOT}/skills/write/references/notation-protocol.md`)
- Full preamble/format standard: `${CLAUDE_PLUGIN_ROOT}/rules/working-paper-format.md`

---

## Bundled Resources

Loaded on demand by the writer agent:

| Resource | Path | When |
|----------|------|------|
| Section templates | `${CLAUDE_PLUGIN_ROOT}/skills/write/templates/section-templates.md` | Always — defines section structure for all paper types |
| Paragraph moves | `${CLAUDE_PLUGIN_ROOT}/skills/write/templates/paragraph-moves.md` | Always — defines argument types |
| Cleanup patterns | `${CLAUDE_PLUGIN_ROOT}/skills/write/templates/cleanup-patterns.md` | After drafting — cleanup pass |
| Style extraction | `${CLAUDE_PLUGIN_ROOT}/skills/write/templates/style-extraction-protocol.md` | `/write style-guide` mode |
| Drafting gates | `${CLAUDE_PLUGIN_ROOT}/skills/write/templates/drafting-gates.md` | Full draft mode |
| Claim-source map | `${CLAUDE_PLUGIN_ROOT}/skills/write/templates/claim-source-map.md` | After results section — format for the `claim_manifest` |
| Notation protocol | `${CLAUDE_PLUGIN_ROOT}/skills/write/references/notation-protocol.md` | Strategy + results sections |
| Gotchas | `${CLAUDE_PLUGIN_ROOT}/skills/write/gotchas.md` | Always — known failure points |

---

## Principles
- **This is the user's paper, not Claude's.** Match their voice and style.
- **Every paper type is first-class.** DZ outputs get the same care as an AER submission — the scaffold changes, the rigor does not.
- **Never fabricate results.** Use TBD placeholders.
- **Citations must be verifiable.** Only cite confirmed papers; mark unverifiable as `% UNVERIFIED`.
- **Trace every claim.** Each non-trivial claim enters `passport.yaml` `claim_manifest` with a real `evidence_origin` (INV-22).
- **Update over create.** Edit section files in place; never proliferate versioned drafts.
- **Argument moves first, cleanup second.** Draft with structure, then strip AI patterns.
