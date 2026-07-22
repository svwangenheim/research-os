---
title: "TRL Project-Level Reporting (Horizon Europe)"
note_type: method
summary: "How TRL is captured, self-reported, and validated at project level in EU Horizon Europe Periodic Reporting."
assumptions: []
projects: []
tags:
  - method
  - TRL
  - Horizon-Europe
  - measurement
updated: "2026-04-14"
---

# TRL Project-Level Reporting (Horizon Europe)

## What it does

Captures a project's technological maturity at three points during its lifecycle using the standard 9-point TRL scale, as reported by project beneficiaries in the Horizon Europe Periodic Reporting system.

The three data points are:
1. **TRL at project start** — declared at proposal or early-stage report
2. **TRL at time of Periodic Report** — midpoint snapshot
3. **TRL at project end** — achieved (closed projects) or expected (ongoing projects)

**Progression** is then calculated as the step difference between start and end TRL.

## When to use it

Use TRL project-level reporting when a funding program needs a standardized maturity measure for portfolio monitoring, project progress tracking, or cross-program comparison. It is most useful for applied technology projects where maturity can plausibly be mapped to demonstration, validation, deployment, or operational use.

Do not use it as a direct measure of novelty, social value, additionality, or commercialization success. A project can report high TRL while being incremental, and a low-TRL project can be strategically important even when it is far from market deployment.

## Identification logic

- TRL data comes from **CORDA** (European Commission internal raw project data warehouse) and the **Horizon Project Dashboard**
- Work Programme topic-level TRL targets are stored in the **Call Passport System (CPS)** and can be matched to project-level reports to assess compliance
- Company data for sector analysis is sourced externally from **Orbis** (NACE Rev. 2 classification)
- Project Officer (PO) survey and interviews used to validate interpretations and flag systematic biases

## Assumptions

- Beneficiaries interpret TRL definitions consistently — **this is violated in practice** (no domain-specific guidance beyond the 9-line table in the Work Programme General Annexes)
- "TRL at end of project" means the TRL at formal grant closure date, not at exploitation stage (86% of POs interpret it this way)
- A single TRL adequately represents the full project — **violated for multi-work-package projects** where different components sit at different TRL levels
- TRL progresses linearly — **violated in practice** (iterative, non-linear innovation)

## Common pitfalls

| Problem                               | Evidence                                                                                                                                                                         |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Self-reporting bias**               | 89% of Project Officers say there is a risk of deliberate over- or underestimation                                                                                               |
| **No mandatory verification**         | TRL validation is not on the PO assessment checklist in all clusters; ERC TRL is not reviewed by Scientific Officers at all                                                      |
| **Single-TRL aggregation**            | Multi-workstream projects must compress multiple TRL levels into one reported figure                                                                                             |
| **Domain inapplicability**            | TRL scale was designed for hardware/aerospace; performs poorly for social sciences, AI, creative industries                                                                      |
| **Coverage gap**                      | Only 16.3% of Horizon Europe projects (2,462 of 15,148) report any TRL data                                                                                                      |
| **Optimism bias in expected end TRL** | Ongoing projects report expectations, not achievements — likely systematically optimistic                                                                                        |
| **Cluster variation**                 | Some Pillar II clusters (Health, Civil Security) rarely define TRL targets; others (Digital, Climate/Energy) do so routinely — creating uneven data quality across the portfolio |

## Use cases in my work

- Understanding how TRL is **actually operationalised** in EU funding practice, as distinct from how it is **normatively defined** (see [[20_summaries/ec-trl-horizon2020.md]])
- Evaluating data quality when using TRL fields from CORDA or similar administrative sources in research
- Designing TRL-based classification schemes for national program analysis: the self-report + no-verification structure is likely replicated in German programs
- Estimating TRL progression distributions across a project portfolio

## Sources

- [[20_summaries/trucco2025-scaling-up-ideas.md]] — Trucco et al. (2025), full methodology and limitations
- [[20_summaries/ec-trl-horizon2020.md]] — Official EU TRL definitions referenced in reporting
- [[30_concepts/technology-readiness-levels.md]] — Background on the TRL scale itself

## Papers using or discussing this method

- [[20_summaries/trucco2025-scaling-up-ideas.md]]: main Horizon Europe project-level TRL reporting source.
- [[20_summaries/ec-trl-horizon2020.md]]: provides official EU TRL definitions and KET qualifiers.
- [[20_summaries/bmle-merkblatt-technologiereifegrade.md]]: German ministry reference for TRL stages.
- [[20_summaries/heder2017-trl-history.md]]: historical background on TRL adoption and known interpretation problems.

## Binning validation for NLP classifiers (added 2026-04-15)

### Automated TRL classification from text

Three papers have directly attempted automated TRL classification from project text:

- **Britt et al. (2008)** (JASIST) — earliest study; LSI nearest-neighbor on NASA project abstracts; 86% accuracy at 2-class, degrades with finer bins. **Key result: coarser bins reliably improve accuracy.**
- **Bengel et al. (2020)** (Design Society) — identifies gaps: sparse labels at low TRL, ambiguous TRL 4–5 boundary. Recommends 3-class grouping.
- **Prasetyo et al. (2022)** — Indonesian university abstracts; LLDA-Helmholtz; 9-class TRL; lower accuracy. Confirms the TRL 4–5 boundary is the hardest to classify.

### Class imbalance handling

When CORDIS training data peaks at TRL 5–6 (49% of labeled projects), standard cross-entropy loss biases the classifier toward the majority class. **Focal Loss** (Lin et al. 2017, ICCV) directly addresses this by down-weighting well-classified majority examples — a recommended implementation choice for the TRL classifier.

### Train-validate boundary mismatch

If a classifier is trained on TRL 1–4 / 5–6 / 7–9 bins but validated against the international standard 1–3 / 4–6 / 7–9 bins, TRL-4 projects (14% of CORDIS training data) fall differently in each scheme. This must be reported transparently in classifier evaluation.

## Related concepts and datasets

- [[30_concepts/technology-readiness-levels.md]]
- [[30_concepts/radical-vs-incremental-innovation.md]]
- [[30_concepts/rd-subsidy-additionality.md]]
- [[40_methods/trl-klassifikation-pipeline.md]]
- [[50_datasets/cordis-horizon-europe-h2020.md]]
- [[50_datasets/foerderkatalog-des-bundes.md]]
- [[70_projects/bundesinnovationshaushalt-trl.md]]
