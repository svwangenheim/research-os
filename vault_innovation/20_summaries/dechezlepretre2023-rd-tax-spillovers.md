---
title: "Do Tax Incentives for Research Increase Firm Innovation? An RD Design for R&D, Patents, and Spillovers"
note_type: source_summary
summary: "Dechezleprêtre et al. (2023) provide quasi-experimental evidence that UK R&D tax credits substantially increase firm R&D and patenting, with large positive spillovers to technologically related firms. Using an RD design around the UK SME size threshold, they estimate an R&D price elasticity of ~2.6 and find £1.7 of private R&D per £1 of taxpayer money. Effects are strongest for young, credit-constrained SMEs. The paper does NOT contain TRL-differentiated estimates — earlier vault claims about 30% higher social returns at low TRL were incorrect and have been removed."
authors:
  - "Antoine Dechezleprêtre"
  - "Elias Einiö"
  - "Ralf Martin"
  - "Kieu-Trang Nguyen"
  - "John Van Reenen"
year: 2023
doi: "10.1257/aer.20190805"
journal: "American Economic Review"
volume: "113"
issue: "1"
pages: "53-94"
institution: "LSE / NBER"
proximity: 2
source_files:
  - "10_sources/dechezlepretre2023-rd-tax-incentives.md"
source_urls:
  - "https://doi.org/10.1257/aer.20190805"
  - "https://www.nber.org/papers/w22405"
projects:
  - bundesinnovationshaushalt-trl
related_concepts:
  - "[[30_concepts/rd-subsidy-additionality.md]]"
  - "[[30_concepts/knowledge-spillovers-and-entrepreneurship.md]]"
  - "[[30_concepts/sme-innovation-participation.md]]"
related_synthesis:
  - "[[90_synthesis/innovation-policy-governance-and-evaluation.md]]"
tags:
  - source-summary
  - rd-subsidies
  - additionality
  - spillovers
  - rdd
  - tax-incentives
  - uk
updated: "2026-05-18"
---

# Dechezleprêtre, Einiö, Martin, Nguyen & Van Reenen (2023) — R&D Tax Incentives and Spillovers

## Source paper link/path

- Source file: `10_sources/dechezlepretre2023-rd-tax-incentives.md` (NBER WP 22405, converted from PDF)
- Published version DOI: [10.1257/aer.20190805](https://doi.org/10.1257/aer.20190805)
- Source status: VERIFIED against NBER WP 22405 on 2026-05-18. Published as AER 113(1), 2023.

⚠️ **Correction notice (2026-05-18):** The prior version of this summary falsely attributed TRL-differentiated spillover results to this paper, claiming "30% higher social returns for low-TRL innovations." This finding does NOT appear in the paper. The paper contains no TRL analysis. The incorrect claim originated in `explorations/trl_research_briefing.md` and has been removed.

## Bibliographic metadata

- Authors: Antoine Dechezleprêtre, Elias Einiö, Ralf Martin, Kieu-Trang Nguyen, John Van Reenen
- Year: 2023 (NBER WP 2016; AER published 2023)
- Journal: American Economic Review, 113(1), pp. 53–94
- DOI: 10.1257/aer.20190805

## Detailed summary

The paper provides quasi-experimental evidence on whether R&D tax incentives actually increase firm innovation. It exploits a UK policy reform that raised the asset threshold for accessing the more generous SME R&D tax credit regime, implementing a Regression Discontinuity (RD) Design around this threshold using HMRC administrative data on the population of UK firms.

The identification strategy is unusually clean: the threshold is unique to R&D tax policy, does not overlap with other programs, and uses pre-reform accounting data (total assets) as the running variable — removing the concern that firms manipulate their tax-credit status.

**Key results:**
- R&D approximately doubled in treated firms relative to control firms just above the threshold.
- Patenting rose by ~60%, robust to quality adjustment (forward citations, patent families, EPO vs. UK patents).
- R&D tax price elasticity ~2.6 — higher than the typical literature range of 1–2, attributable to the SME subsample being more credit-constrained and therefore more responsive.
- £1.7 of private R&D induced for every £1 of taxpayer expenditure — positive fiscal multiplier.
- UK business R&D would be ~10% lower absent the policy.
- Positive technology spillovers: R&D induced by the tax credit generates additional innovation in technologically related firms, identified via patent citation networks.
- Effects are strongest for young and financially constrained firms.

## Research question

Do R&D tax incentives increase firm R&D investment and innovation output, and do they generate positive spillovers to related firms?

## Core argument or contribution

Two contributions: (1) A credible causal estimate of R&D tax credit effects on both R&D inputs and innovation outputs using a clean RD design with administrative data on the full UK firm population. (2) Evidence that induced R&D generates positive technology spillovers — the externality that justifies public subsidy in the first place.

## Methodology

- Regression Discontinuity Design (RDD) exploiting the UK R&D tax credit SME asset threshold
- Running variable: total assets (pre-reform HMRC data)
- Outcomes: R&D expenditure, patent counts (EPO, UK, all jurisdictions), quality-adjusted patents
- Spillover estimation: patent citation network following Jaffe (1986); IV regression

## Key findings

1. **Input additionality:** R&D doubled in treated SMEs; elasticity ~2.6 w.r.t. tax-adjusted user cost.
2. **Output additionality:** Patenting +60%; robust to quality adjustment.
3. **Fiscal multiplier:** £1.7 private R&D per £1 public cost.
4. **Spillovers confirmed:** Tax-induced R&D generates additional patenting in technologically related firms.
5. **Heterogeneity:** Effects concentrated in young, credit-constrained firms.

## Limitations

- UK-specific; may not generalize to German direct grant programs.
- RDD is local to the SME/large-firm threshold.
- Patent-based outcome measure misses non-patented innovation.
- No TRL disaggregation — paper is agnostic on where in the R&D pipeline effects occur.

## Important concepts discussed

- [[30_concepts/rd-subsidy-additionality.md]] — direct and spillover additionality both confirmed; elasticity ~2.6; fiscal multiplier positive
- [[30_concepts/knowledge-spillovers-and-entrepreneurship.md]] — R&D tax credit induces R&D that spills over to patent-citation-connected firms
- [[30_concepts/sme-innovation-participation.md]] — effects strongest for young and credit-constrained SMEs

## Relation to other papers in the vault

- Complements [[20_summaries/czarnitzki2004-rd-subsidies-zew.md]] and [[20_summaries/czarnitzki2014-funding-source.md]] — all confirm additionality from different instruments.
- Relates to [[20_summaries/howell2017-financing-innovation.md]]: both use RD designs around thresholds to estimate causal innovation effects.

## Implications for the Bundesinnovationshaushalt project

1. **DOI confirmed:** 10.1257/aer.20190805 — cite as AER 2023, 113(1): 53–94.
2. **No TRL claim:** Do not use this paper to support TRL-differentiated return arguments.
3. **Usable for:** general R&D subsidy additionality, SME credit constraint mechanism, spillover justification for public R&D support.
4. **German applicability:** UK-specific; frame as international evidence, not German estimates.

## Links to canonical concept, method, dataset, synthesis, and project notes

- Concepts: [[30_concepts/rd-subsidy-additionality.md]], [[30_concepts/knowledge-spillovers-and-entrepreneurship.md]], [[30_concepts/sme-innovation-participation.md]]
- Methods: RDD — see [[40_methods/causal-evaluation-innovation-policy.md]]
- Synthesis: [[90_synthesis/innovation-policy-governance-and-evaluation.md]]
- Project: [[70_projects/bundesinnovationshaushalt-trl.md]]
