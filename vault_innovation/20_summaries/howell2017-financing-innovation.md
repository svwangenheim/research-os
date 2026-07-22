---
title: "Financing Innovation: Evidence from R&D Grants"
note_type: source_summary
authors: ["Sabrina T. Howell"]
year: 2017
doi: "10.1257/aer.20150808"
journal: "American Economic Review"
volume: 107
issue: 4
pages: "1136–1164"
proximity: 1
source_files: []
source_urls:
  - "https://doi.org/10.1257/aer.20150808"
  - "https://www.aeaweb.org/articles?id=10.1257/aer.20150808"
projects:
  - bundesinnovationshaushalt-trl
related_concepts:
  - "[[30_concepts/rd-subsidy-additionality.md]]"
  - "[[30_concepts/technology-transfer-and-translation.md]]"
  - "[[30_concepts/sme-innovation-participation.md]]"
  - "[[30_concepts/equity-gap-sme-financing.md]]"
related_methods:
  - "[[40_methods/causal-evaluation-innovation-policy.md]]"
related_datasets: []
related_synthesis:
  - "[[90_synthesis/innovation-policy-governance-and-evaluation.md]]"
  - "[[90_synthesis/international-innovation-policy-benchmarks.md]]"
tags:
  - source-summary
  - rd-grants
  - sbir
  - financing-constraints
  - regression-discontinuity
  - causal-inference
  - venture-capital
  - innovation-policy
  - entrant-firms
updated: "2026-05-08"
semantic_status: "verified"
---

# Howell (2017) — Financing Innovation: Evidence from R&D Grants

## Source paper link/path

- Source URL: https://doi.org/10.1257/aer.20150808
- Source status: **fully verified** — summary based on published AER paper and circulating working paper (Harvard/Yale JMP). Previous local PDF was a mislabeled Meyer & Mittag paper; do not use that file for Howell claims.
- Replication package available via AEA.

## Bibliographic metadata

- Author: Sabrina T. Howell
- Year: 2017
- Journal: American Economic Review, 107(4), pp. 1136–1164
- DOI: `10.1257/aer.20150808`
- JEL codes: D22, G24, G32, L53, O31, O34, O38

## Detailed summary

Howell (2017) provides the first large-sample, quasi-experimental evaluation of R&D subsidies, using a sharp regression discontinuity (RD) design applied to ranked applicants to the U.S. Department of Energy (DOE) Small Business Innovation Research (SBIR) program.

The data cover **7,436 small high-tech firms** and over **$884 million in Phase I awards** (2012 dollars) across two major DOE program offices (EERE and FE), spanning **1983–2013**. DOE officials rank firms within competitions (average 9.8 applicants per competition, SD = 8); Howell exploits these ranks in a sharp RD comparing firms immediately around the award cutoff, where the lowest-ranked winner has centered rank +1 and the highest-ranked loser has rank −1. Of the 7,436 applicant firms, 71% applied only once and 14% applied twice.

**Main results (Phase I, ~$150k grant):**
- A Phase I award **approximately doubles** the long-run probability of receiving subsequent venture capital: baseline rate 10% → 19% (**+9 percentage points**)
- Within two years of the grant: VC effect of **+7 percentage points**
- Large positive effects on **patenting** (citation-weighted patents)
- Large positive effects on **revenue** (probability of achieving revenue)
- All effects stronger for **more financially constrained firms**

**Phase II result (critical for policy transfer):** RD estimates using Phase II applicants yield **tiny or negative effects** on subsequent VC. This asymmetry is the paper's most important policy insight: the grant effect is specific to early-stage awards in immature technology domains, not to late-stage development support.

**Mechanism:** Howell rules out certification (the award signalling firm quality) as the primary channel — Phase II grants also signal quality but produce no VC effect. Instead, grants work because they **fund technology prototyping**, which reduces investor uncertainty about technology feasibility. This is crucial: grants work through reducing information asymmetries about *technology potential*, not about *firm quality* per se.

**Heterogeneity:** Effects are largest for young, financially constrained firms in early-stage (unreife) technology domains. Open, competitive calls produce large causal effects; narrow topic-specific solicitations produce near-zero effects (consistent with lower adverse selection in competitive allocation).

## Research question

Do early-stage public R&D grants causally improve innovative small firms' access to follow-on venture capital and their subsequent innovation and commercialization outcomes — and through what mechanism?

## Core argument or contribution

First large-sample quasi-experimental evaluation of R&D grants. Phase I SBIR awards approximately double VC probability for financially constrained early-stage firms, operating through technology prototyping (not certification). Phase II grants have no consistent positive VC effect — early-stage targeting is essential.

## Methodology

- **Design:** Sharp regression discontinuity (RD) using DOE applicant rankings within competitions
- **Running variable:** Centered rank (lowest-ranked winner = +1; highest-ranked loser = −1)
- **Bandwidth:** Main estimates bandwidth 2–3 ranks around cutoff; robustness checks with full-data bandwidth and absolute rank dummies
- **Estimator:** OLS with robust standard errors clustered at year level; ZINB model for revenue outcomes (zero-inflated negative binomial)
- **Validation:** Covariate continuity tests (Table 1), goodness-of-fit tests for rank functional form, exclusion of prior DOE winners within EERE/FE
- **Sample:** 7,436 firms, 1983–2013, EERE + FE program offices only

## Datasets/materials used

- Proprietary DOE SBIR applicant rankings (EERE + FE), 1983–2013
- 7,436 firms; $884M in Phase I awards (2012 dollars)
- Matched to: VC investment data, USPTO patent records, revenue data; grant-use survey for mechanism identification

## Key findings

1. Phase I award doubles long-run VC probability: 10% → 19% (+9 pp)
2. +7 pp VC effect within 2 years of the award
3. Large positive patenting effects (citation-weighted)
4. Large positive revenue/commercialization effects
5. Effects concentrated among financially constrained firms
6. **Phase II grants: zero or negative VC effect** — early-stage targeting matters
7. Mechanism: technology prototyping, not certification
8. Open competitive calls → large effects; narrow topic solicitations → near-zero effects

## Limitations

- **External validity:** U.S. DOE energy startups only; transfer to German instruments requires institutional mapping (different Eigenanteil requirements, no ranking-based allocation in ZIM, shallower DE VC market)
- **Phase III gap:** SBIR explicitly exits after Phase II; no evidence on firms that fail to attract private Phase III capital — a known systemic weakness of SBIR that DE policy would need to address separately
- **Local average treatment effect:** Estimates apply to firms around the rank cutoff, not the full population of SBIR applicants
- **Energy sector specificity:** Technology-prototyping mechanism may be stronger in capital-intensive hardware than in software or services
- **Rank discreteness:** Rating variable is discrete, which creates bandwidth constraints in the RD design

## Important concepts discussed

- [[30_concepts/rd-subsidy-additionality.md]] — central causal reference for output additionality (VC, patents, revenue)
- [[30_concepts/technology-transfer-and-translation.md]] — prototyping as bridge between public support and private investment
- [[30_concepts/sme-innovation-participation.md]] — financial constraints and young firm access to grants
- [[30_concepts/equity-gap-sme-financing.md]] — VC market depth as precondition for SBIR-like instruments to work

## Methods discussed

- [[40_methods/causal-evaluation-innovation-policy.md]] — sharp RD using applicant rankings; bandwidth sensitivity; ZINB for revenue

## Datasets discussed

- DOE SBIR applicant rankings (proprietary)
- USPTO patent records (matched)
- VC financing records (matched)

## Relation to other papers in the vault

- Complements [[20_summaries/czarnitzki2004-rd-subsidies-zew.md]] and [[20_summaries/cherif2022-rd-subsidies-imf.md]] (input additionality) by focusing on output additionality for young firms
- Contrasts with [[20_summaries/beck2016-radical-or-incremental.md]]: Howell finds general positive effects; Beck et al. find effects only for radical innovation — setting differences explain divergence
- Upgrades [[20_summaries/audretsch2002-sbir-evaluation.md]] (older descriptive SBIR evidence) with causal identification
- Primary causal citation for SBIR-Äquivalent argument in [[70_projects/bundesinnovationshaushalt-trl.md]]

## Implications for the project

For **Bundesinnovationshaushalt-TRL** (paper Section 5, item 1): Howell is the primary causal citation for the claim that early-stage, open-competition grants for small, financially constrained firms produce large positive VC and commercialization effects.

Key conditions for policy transfer from US to DE:
1. Awards must target **early-stage** (TRL 1–4 equivalent), not TRL 7–9
2. Competition must be **open**, not pre-specified by narrow topic
3. Eligibility must be **restricted to small/young firms** (size cap, not broad-based)
4. **Phase III gap** (no state support post-TRL 6) must be addressed by VC market deepening separately

The Phase II null result is a direct empirical warning against using SBIR logic to justify incumbent-supporting grants at late TRL stages — a pattern found in the FK recipient structure analysis.

## Links to canonical concept, method, dataset, synthesis, and project notes

- Concepts: [[30_concepts/rd-subsidy-additionality.md]], [[30_concepts/technology-transfer-and-translation.md]], [[30_concepts/sme-innovation-participation.md]], [[30_concepts/equity-gap-sme-financing.md]]
- Methods: [[40_methods/causal-evaluation-innovation-policy.md]]
- Synthesis: [[90_synthesis/innovation-policy-governance-and-evaluation.md]], [[90_synthesis/international-innovation-policy-benchmarks.md]]
- Projects: [[70_projects/bundesinnovationshaushalt-trl.md]]
