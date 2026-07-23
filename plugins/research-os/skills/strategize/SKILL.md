---
name: strategize
description: Design identification strategy, pre-analysis plan, or formal theory section. Dispatches Strategist / Theorist (proposer) and the paired critic (validator). Strategy phase of the research-os pipeline; writes the strategy into 03_analysis/strategy/ and updates passport.yaml.
argument-hint: "[mode: strategy | pap | pap interactive | theory] [research question or spec path]"
allowed-tools: Read,Grep,Glob,Write,Edit,Task
---

# Strategize

Design an identification strategy, pre-analysis plan, or formal theory section by dispatching the appropriate creator (**Strategist** or **Theorist**) and its paired critic.

**Input:** `$ARGUMENTS` — mode keyword followed by research question or path to research spec.

State lives in **`passport.yaml`** (schema: `${CLAUDE_PLUGIN_ROOT}/templates/passport.yaml`). Paths follow `${CLAUDE_PLUGIN_ROOT}/rules/folder-map.md` — the single source of truth. Strategy memos, PAPs, theory memos, and their critic reports live in `03_analysis/strategy/`; decision records in `00_admin/process/decisions/`. All outputs obey `${CLAUDE_PLUGIN_ROOT}/rules/output-discipline.md`: **update the existing memo/review in place with a `## Changelog` entry; a new file only for a genuinely distinct strategy.** Critic scores are written to `passport.yaml` `pipeline.stages.strategy` (status + score); the severity gradient in `${CLAUDE_PLUGIN_ROOT}/rules/quality.md` applies (Strategy phase = constructive/medium severity).

---

## Modes

### `/strategize [question]` or `/strategize strategy [question]` — Identification Strategy
Design the causal identification strategy.

**Agents:** Strategist → strategist-critic
**Output:** Strategy memo + robustness plan + falsification tests → `03_analysis/strategy/strategy_memo.md`

Workflow:
1. **Pre-Strategy Report (mandatory).** Before proposing any strategy, the Strategist must output a structured report proving it read the discovery inputs:

```markdown
## Pre-Strategy Report
**Research spec:** [passport.yaml `research:` block / `00_admin/research_outline.md` / "not found"]
**Literature review:** [`01_literature/reviews/<question-slug>.md` or "not found"]
**Data assessment:** [`02_data/data-sources.md` or "not found"]
**Domain profile:** [`00_admin/domain-profile.md` loaded / not found]

**Research question:** [one sentence from spec]
**Key findings from literature:**
- [What methods have been used for this question]
- [What gaps remain]
**Available data:**
- [Dataset name] — [key variables, coverage, access]
- [Variation available for identification]: [describe]
**Candidate designs from domain profile:** [list relevant designs]

Proceeding to strategy design.
```

If research spec, literature review, or data assessment are missing, the Strategist proceeds with ASSUMED placeholders — but flags each clearly.

2. Read `00_admin/domain-profile.md` for common identification strategies in the field.
3. Dispatch Strategist to produce:
   - Strategy memo: design choice, estimand, assumptions, comparison group
   - Pseudo-code: implementation sketch
   - Robustness plan: ordered list of checks with rationale
   - Falsification tests: what SHOULD NOT show effects
   - Referee objection anticipation: top 5 objections with responses
4. Dispatch strategist-critic to review through 4 phases:
   - Phase 1: Claim identification (design, estimand, treatment, control)
   - Phase 2: Core design validity (assumption checks, sanity checks)
   - Phase 3: Inference soundness (clustering, multiple testing)
   - Phase 4: Polish and completeness (robustness, citations)
5. If CRITICAL issues found, iterate (max 3 rounds per three-strikes).
6. **Save memo to `03_analysis/strategy/strategy_memo.md`, updating in place if it exists** (per output-discipline). Prepend a dated entry to the memo's `## Changelog`.
7. **Save the critic report to `03_analysis/strategy/strategy_review.md`** (one review per artifact, updated in place — latest verdict + changelog). Write the strategist-critic score into `passport.yaml` `pipeline.stages.strategy` (`status: passed` once the gate of 80 is met).
8. Refresh the dashboard: run `/dashboard`.
9. **Save decision record** → `00_admin/process/decisions/strategy_[topic].md`
   Using `${CLAUDE_PLUGIN_ROOT}/skills/strategize/templates/decision-record.md`, record:
   - **Decision:** The chosen identification strategy (design + estimator)
   - **Alternatives:** Other designs the Strategist considered (e.g., IV, RDD, SC, selection-on-observables)
   - **Why rejected:** For each, the specific reason (no valid instrument, insufficient density at cutoff, no clean donor pool, etc.)
   - **Key assumptions:** What must hold (parallel trends, exclusion restriction, continuity, etc.)
   - **What would invalidate:** What findings would force a strategy change (pre-trends failure, weak first stage, manipulation at cutoff)

### `/strategize pap [spec]` — Pre-Analysis Plan
Draft a pre-analysis plan following AEA/OSF/EGAP standards.

**Input:** `$ARGUMENTS` — path to research spec file, a topic, or `interactive` for guided interview.

- If `$ARGUMENTS` includes a file path: read it (research spec from `/discover interview`, i.e. the `research:` block + `00_admin/research_outline.md`)
- If `$ARGUMENTS` includes `interactive`: conduct the guided PAP interview (see below)
- Otherwise: treat as topic and draft with ASSUMED placeholders marked clearly

**Agents:** Strategist (in PAP mode), optionally strategist-critic
**Output:** Pre-analysis plan document → `03_analysis/strategy/pre_analysis_plan.md`

#### Interactive PAP Interview (6-Question Guided Flow)

When invoked as `/strategize pap interactive`, conduct a **free-form conversation**. Ask these questions directly in your text responses, **one or two at a time, and wait for the user to reply before continuing**. Do NOT use AskUserQuestion. (Flow reference: `${CLAUDE_PLUGIN_ROOT}/skills/strategize/references/pap-interview-flow.md`.)

1. **What is the research question?**
2. **What is the study design?** (RCT / natural experiment / quasi-experimental / observational)
3. **What are the primary outcome variables?** (names, measurement, data source)
4. **What is the identification strategy?** (randomization mechanism / treatment assignment / source of variation)
5. **What subgroup analyses are pre-specified?** (with justification for each)
6. **What multiple testing concerns exist?** (number of primary outcomes, family-wise error rate plan)

After all 6 answers are collected, proceed to PAP drafting.

#### PAP Sections

Dispatch Strategist in PAP mode to produce all standard sections:

1. **Study overview** — research question, design, treatment, control
2. **Outcomes** — primary, secondary, mechanism variables with measurement details
3. **Estimating equations** — with full notation protocol
4. **Subgroup analyses** — pre-specified, with justification for each
5. **Multiple testing correction** — Bonferroni / Benjamini-Hochberg / Romano-Wolf (specify which and why)
6. **Power calculations** — MDE, baseline statistics, sample size, assumptions stated explicitly with sensitivity
7. **Sample and exclusion rules** — inclusion criteria, attrition handling, outlier treatment
8. **Data and analysis** — sources, software, randomization/assignment mechanism
9. **Timeline** — data collection, analysis, registration dates
10. **Deviations log** — empty template for tracking post-registration changes

#### Platform-Specific PAP Templates

Ask the user (free-form, in plain text) which registry platform they plan to use, if unclear from context:

**AEA RCT Registry** (`${CLAUDE_PLUGIN_ROOT}/skills/strategize/templates/pap-templates/aea-rct.md`):
- Most structured format. All fields required.
- Must be registered before intervention begins.
- Strict section ordering: hypotheses → outcomes → analysis → power.
- Requires IRB information and funding sources.

**OSF (Open Science Framework)** (`${CLAUDE_PLUGIN_ROOT}/skills/strategize/templates/pap-templates/osf.md`):
- More flexible format. Good for observational studies and natural experiments.
- Allows iterative updates with version history.
- Less rigid section structure — can adapt to study design.
- Supports pre-registration of observational/archival studies.

**EGAP (Evidence in Governance and Politics)** (`${CLAUDE_PLUGIN_ROOT}/skills/strategize/templates/pap-templates/egap.md`):
- Development economics and political science focused.
- Additional governance and ethics questions required.
- Emphasizes pre-specification of heterogeneous treatment effects.
- Requires description of implementing partners and field conditions.

#### Observational Study PAP Adaptation

For observational, quasi-experimental, or natural experiment designs, adapt the PAP template:

- **Identification strategy replaces randomization** — describe the source of exogenous variation
- **Comparison group replaces control group** — define who is compared to whom and why
- **Identification assumption discussion** — explicitly state and defend each assumption
- **Placebo and falsification tests** — pre-specify what SHOULD NOT show effects
- **Robustness to specification choices** — pre-commit to bandwidth, functional form, sample restrictions
- **Treatment of endogeneity concerns** — document known threats and planned diagnostics

#### ASSUMED Placeholder Safety

**CRITICAL: Flag every ASSUMED item clearly. The researcher must review and approve before registration.**

When drafting a PAP from a topic (without a full research spec or interactive interview), many details will be assumed. For each assumed item:

- Mark it with `[ASSUMED]` in bold
- Explain what was assumed and why
- Provide the most reasonable default but flag it for review

A registered PAP with unchecked assumptions is worse than no PAP. The final section of every PAP must include:

```markdown
## Pre-Registration Checklist

**Review every [ASSUMED] item before registering this plan.**

- [ ] [ASSUMED] Item 1 — [what was assumed]
- [ ] [ASSUMED] Item 2 — [what was assumed]

**Do not register until all items are reviewed and confirmed or corrected.**
```

#### Optional strategist-critic Review

After PAP creation, optionally dispatch the strategist-critic to review:
- Are identification assumptions clearly stated and defensible?
- Is the estimator choice appropriate for the design?
- Are power calculation assumptions reasonable? Show sensitivity.
- Are pre-specified subgroups justified (not fishing)?
- Are multiple testing corrections appropriate?
- Are any [ASSUMED] items potentially problematic if left uncorrected?

Save PAP to `03_analysis/strategy/pre_analysis_plan.md` and the review to `03_analysis/strategy/pap_review.md` (both updated in place).

---

### `/strategize theory [target]` — Formal Theory Section

Produce a formal theory section: assumptions, definitions, lemmas, theorems, and proofs.

**When to use:**
- Paper type is **econometric methods** (the method is the contribution)
- Paper type is **theory + empirics** (theoretical predictions are tested)
- Paper type is **structural** (identification of structural parameters needs formal argument)
- Paper type is **methodological reduced-form** (the design contributes a new estimator)

**Skip this mode** for applied papers that use off-the-shelf estimators — the strategist's memo is sufficient. (Consistent with the theorist's CONDITIONAL flag in `${CLAUDE_PLUGIN_ROOT}/rules/permissions.md`, the theory weight is renormalized away when this mode is skipped.)

**Input:** `$ARGUMENTS` — research question, path to strategy memo, or path to existing paper/draft.

**Agents:** Theorist → theorist-critic
**Output:** Theory memo + assumptions.tex + results.tex + proofs.tex + notation glossary

Workflow:
1. **Pre-Theory Report (mandatory).** Before writing any math, the Theorist must output a structured report showing what was read:

```markdown
## Pre-Theory Report
**Research spec:** [passport.yaml `research:` block / `00_admin/research_outline.md` / "not found"]
**Strategy memo:** [`03_analysis/strategy/strategy_memo.md` or "not found"]
**Existing paper/draft:** [path or "not found"]
**Domain profile:** [`00_admin/domain-profile.md` loaded / not found]
**Notation conventions:** [`04_paper/<output>/preambles/` / domain-profile notation table / "not found"]
**Bibliography base:** [`01_literature/bibliography.bib` / "not found"]

**Paper type:** [econometric methods / theory+empirics / structural / methodological reduced-form]
**Theoretical object(s) to produce:** [identification / consistency / asymp. normality / influence function / DML / bootstrap / test / proposition]
**Data structure:** [iid / panel / staggered / clustered / triangular array]
**Target parameter:** [definition as functional of P]
**Estimator:** [definition]
**Assumptions anticipated:** [A1 sampling, A2 parallel trends, ...]

Proceeding to theory drafting.
```

If strategy memo or paper type is missing, the Theorist flags it and asks before proceeding.

2. Read `00_admin/domain-profile.md` for the Theoretical Foundational References table and Author Team table.
3. Dispatch **Theorist** to produce:
   - `03_analysis/strategy/theory_memo.md`
   - `04_paper/<output>/sections/assumptions.tex`
   - `04_paper/<output>/sections/results.tex`
   - `04_paper/<output>/sections/proofs.tex`
   - `03_analysis/strategy/notation_glossary.md`
   (`<output>` is the selected academic-paper output folder — usually `academic_paper`.)
4. Dispatch **theorist-critic** to review through 4 sequential phases:
   - Phase 1: Claim identification (object type, target parameter, estimator, assumptions)
   - Phase 2: Proof validity (logical, measurability, expansions, identification, asymptotic distribution) — **early-stop on critical gaps**
   - Phase 3: Assumption minimality + statement calibration + notation consistency (INV-7)
   - Phase 4: Citation fidelity + linkage to empirical claims + exposition
5. If CRITICAL issues found, iterate (max 3 rounds per three-strikes). Escalation target: User.
6. **Save the critic report to `03_analysis/strategy/theory_review.md`** (updated in place); write the theorist-critic score into `passport.yaml` `pipeline.stages.strategy`.
7. **Save decision record** → `00_admin/process/decisions/theory_[topic].md`
   Record:
   - **Decision:** The theoretical objects proved (identification, asymptotic distribution, etc.)
   - **Assumptions:** Full list with interpretation
   - **What's open:** What the theory does NOT cover (caveats for the writer)
   - **Linkage:** Which empirical claims each theorem supports

---

## Bundled Resources

### Templates
| File | Purpose |
|------|---------|
| `${CLAUDE_PLUGIN_ROOT}/skills/strategize/templates/pre-strategy-report.md` | Mandatory pre-check report before designing strategy |
| `${CLAUDE_PLUGIN_ROOT}/skills/strategize/templates/strategy-memo.md` | Strategy memo output format (5 required sections) |
| `${CLAUDE_PLUGIN_ROOT}/skills/strategize/templates/robustness-plan.md` | Ordered robustness checklist template |
| `${CLAUDE_PLUGIN_ROOT}/skills/strategize/templates/theory-memo.md` | Theory section output format (assumptions, results, proofs) |
| `${CLAUDE_PLUGIN_ROOT}/skills/strategize/templates/decision-record.md` | Shared decision-record format (also referenced by `/discover`) |

### Design Checklists
| File | Design |
|------|--------|
| `${CLAUDE_PLUGIN_ROOT}/skills/strategize/templates/design-checklists/did.md` | Difference-in-Differences (parallel trends, staggered, estimator selection) |
| `${CLAUDE_PLUGIN_ROOT}/skills/strategize/templates/design-checklists/iv.md` | Instrumental Variables (relevance, exclusion, monotonicity, LATE) |
| `${CLAUDE_PLUGIN_ROOT}/skills/strategize/templates/design-checklists/rdd.md` | Regression Discontinuity (bandwidth, manipulation, balance) |
| `${CLAUDE_PLUGIN_ROOT}/skills/strategize/templates/design-checklists/event-study.md` | Event Study (pre-trends, binning, heterogeneity-robust estimators) |
| `${CLAUDE_PLUGIN_ROOT}/skills/strategize/templates/design-checklists/structural.md` | Structural Estimation (model environment, identification, counterfactuals) |
| `${CLAUDE_PLUGIN_ROOT}/skills/strategize/templates/design-checklists/descriptive.md` | Descriptive/Measurement (construction, validation, decomposition) |

### PAP Templates
| File | Registry |
|------|----------|
| `${CLAUDE_PLUGIN_ROOT}/skills/strategize/templates/pap-templates/aea-rct.md` | AEA RCT Registry (most structured, all fields required) |
| `${CLAUDE_PLUGIN_ROOT}/skills/strategize/templates/pap-templates/osf.md` | OSF (flexible, good for observational studies) |
| `${CLAUDE_PLUGIN_ROOT}/skills/strategize/templates/pap-templates/egap.md` | EGAP (development/political science, governance emphasis) |

### References
| File | Purpose |
|------|---------|
| `${CLAUDE_PLUGIN_ROOT}/skills/strategize/references/pap-interview-flow.md` | 6-question guided interview for building a PAP interactively |

### Gotchas
| File | Purpose |
|------|---------|
| `${CLAUDE_PLUGIN_ROOT}/skills/strategize/gotchas.md` | Known failure points: design selection traps, memo pitfalls, PAP anti-patterns, theory-mode caveats |

---

## Principles

- **Strategist proposes, strategist-critic critiques.** Adversarial pairing catches design flaws early.
- **Theorist proves, theorist-critic checks the proof.** Proof validity gates everything downstream — notation, citations, polish.
- **Strategy memo is the contract.** Once approved, the Coder implements it faithfully.
- **Catch problems before coding.** A flawed strategy caught now saves weeks of wasted analysis.
- **Multiple strategies are OK.** Present trade-offs and let the user choose — free-form, never AskUserQuestion.
- **The user decides.** If Strategist and strategist-critic disagree after 3 rounds, the user resolves it.
- **State in the passport.** Scores land in `pipeline.stages.strategy`; never scatter state into per-step files.
- **Update over create.** Improve the existing memo/review in `03_analysis/strategy/` with a Changelog entry; a new file only for a materially distinct strategy.
- **Pre-specification is the point.** Everything in a PAP is decided before seeing outcomes.
- **Be honest about what's exploratory.** Label subgroups and secondary outcomes clearly.
- **Power calculations require assumptions.** State every assumption. Show sensitivity.
- **A PAP is a commitment device.** Make sure the researcher understands what they're committing to.
