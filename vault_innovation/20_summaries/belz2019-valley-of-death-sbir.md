---
title: "Mapping the 'Valley of Death': Managing Selection and Technology Advancement in NASA's Small Business Innovation Research Program"
note_type: source_summary
authors:
  - "Belz, Andrea"
  - "Zapatero, Fernando"
  - "Terrile, Richard"
  - "Kawas, Michael"
  - "Giga, Aleksandar"
year: 2019
doi: "10.2139/ssrn.3221328"
journal: "SSRN Working Paper / IEEE Engineering Management Review"
institution: "University of Southern California / JPL-Caltech"
proximity: 2
source_files:
  - "10_sources/belz2019-valley-of-death-sbir.md"
source_urls:
  - "https://ssrn.com/abstract=3221328"
projects:
  - bundesinnovationshaushalt-trl
related_concepts:
  - "[[30_concepts/technology-readiness-levels.md]]"
  - "[[30_concepts/commercialization-gap.md]]"
  - "[[30_concepts/rd-subsidy-additionality.md]]"
related_synthesis:
  - "[[90_synthesis/international-innovation-policy-benchmarks.md]]"
tags:
  - source-summary
  - trl
  - valley-of-death
  - sbir
  - nasa
  - innovation-policy
updated: "2026-05-26"
---

# Belz et al. (2019) — Mapping the Valley of Death: NASA SBIR and TRL Advancement

## Source paper link/path

- Source file: `10_sources/belz2019-valley-of-death-sbir.md`
- SSRN: https://ssrn.com/abstract=3221328
- Source status: Full paper text in vault (32-page working paper / IEEE EM submission).

## Bibliographic metadata

- Title: Mapping the "Valley of Death": Managing Selection and Technology Advancement in NASA's Small Business Innovation Research Program
- Authors: Andrea Belz, Fernando Zapatero, Richard Terrile, Michael Kawas, Aleksandar Giga
- Affiliations: USC Viterbi Engineering; USC Marshall Business; JPL/Caltech
- Year: 2019 (SSRN)
- Keywords: TRL, NASA, SBIR, entrepreneurship, innovation, technology maturity

## Detailed summary

Belz et al. study the NASA SBIR program using TRL levels from proposals (PI-assessed) and NASA-measured final TRL levels, covering all NASA Mission Directorates 2010–2016. This provides a rare empirical window into actual TRL advancement as a technical outcome, rather than the economic outcomes dominating prior SBIR evaluation literature.

The central finding: NASA SBIR advances technologies from roughly TRL 2–3 to TRL 4–5 across its two-phase program, but rarely to TRL 6 (the threshold for infusion into a NASA flight project, used as a commercial readiness proxy). The program partially — but not fully — spans the valley of death.

**Phase I selection**: Tends toward larger companies. A tenfold increase in headcount raises selection probability by ~15%. TRL maturity itself does not drive Phase I selection. Overly ambitious projected advances decrease selection likelihood by ~8% — reviewers penalize implausible advancement claims.

**Phase II selection**: Company size disappears as a predictor. Only initial TRL modestly affects Phase II selection. This shift from size-based to maturity-based selection reflects a two-stage risk disaggregation: Phase I accepts business risk (small firms), Phase II manages technical risk.

**Technical advancement**: Technologies start at TRL ~2, advance to ~TRL 3 via Phase I ($100k), and to roughly TRL 4.5–5 by program end ($700k Phase II). Only ~10% reach TRL 6+; ~10% remain at TRL 1–3. Microfirms (1–5 employees) advance further than standard small businesses in Phase I; difference vanishes in Phase II.

**TRL cost calibration**: $100k ≈ one TRL step (TRL 2→3); $700k ≈ 2–3 TRL steps. Computational technologies advance faster per dollar than manufacturing/hardware.

## Research question

How does the NASA SBIR program manage business and technical risk, and what actual TRL advancement does it produce?

## Core contribution

First study to use TRL advancement (not economic outcomes) as the primary SBIR evaluation metric. Provides empirical cost-per-TRL-step calibration. Documents that SBIR covers TRL 2→5 but the TRL 5→6 gap remains unfunded.

## Methodology

- Logit regression on Phase I / Phase II selection probability (binary)
- OLS regression on final TRL as function of initial TRL, headcount, advancement
- Kolmogorov-Smirnoff and Anderson-Darling tests on TRL distributions
- Data: NASA SBIR Electronic Handbook, 2010–2016; 8,499 Phase I proposals (1,926 winners); 1,833 Phase II proposals (674 winners)

## Key findings

1. Phase I selects larger firms; Phase II selects more mature technologies — two-stage risk management.
2. Technologies advance TRL 2 → ~3 in Phase I; TRL 2 → ~4.5–5 across both phases.
3. Only ~10% reach TRL 6 (infusion-ready); ~10% remain at TRL 1–3.
4. Microfirms advance further in Phase I; converge with standard small businesses by Phase II.
5. $100k ≈ TRL 2→3; $700k ≈ TRL 3.5–5.

## Limitations

- Does not control for technology type (software vs. hardware costs differ sharply)
- Assumes TRL self-reports are accurate; gaming not tested
- US aerospace context; cross-national applicability indirect
- No post-program economic follow-through for the same cohort

## Important concepts discussed

- [[30_concepts/technology-readiness-levels.md]]: Empirically validates TRL 2–6 as the valley of death; provides cost-per-TRL-step anchors
- [[30_concepts/commercialization-gap.md]]: Documents the TRL 5→6 gap as structurally uncovered by the two-phase SBIR design
- [[30_concepts/rd-subsidy-additionality.md]]: Demonstrates real technical additionality before economic outcomes materialize

## Relation to other papers in the vault

- **[[20_summaries/audretsch2003-sbir.md]]**: Audretsch describes the SBIR three-phase structure; Belz et al. provide TRL outcomes under that structure
- **[[20_summaries/howell2017-financing-innovation.md]]**: Howell (2017) examines DOE SBIR's financial mechanism; Belz et al. focus on the technical (TRL) mechanism
- **[[20_summaries/earto2014-trl-policy-tool.md]]**: EARTO frames the valley as TRL 5–6; Belz et al. confirm Phase II typically ends at TRL 4.5–5, leaving TRL 5–6 unfunded
- **[[20_summaries/azoulay2019-arpa-model.md]]**: ARPA targets nascent S-curves; SBIR targets the valley between TRL 3 (proof-of-concept) and TRL 6 (prototype validation)

## Implications for the Bundesinnovationshaushalt project

1. **TRL cost calibration**: Belz et al.'s empirical anchors ($100k/step at early stage) are useful for German FK program design. ZIM Phase I (~€180k) should yield ~1 TRL step; a Phase II equivalent (~€1.2m) should yield 2–3 steps.
2. **TRL 5–6 gap confirmed**: 90% of SBIR projects don't reach TRL 6. Germany's FK has very few instruments targeting TRL 5–6. This confirms the commercialization-gap diagnosis.
3. **Two-stage risk disaggregation absent from FK**: Phase I selects for firm quality, Phase II for technology maturity. The German Förderkatalog does not explicitly implement this risk-staged structure.

## Links to canonical concept, method, dataset, synthesis, and project notes

- Concepts: [[30_concepts/technology-readiness-levels.md]], [[30_concepts/commercialization-gap.md]], [[30_concepts/rd-subsidy-additionality.md]]
- Synthesis: [[90_synthesis/international-innovation-policy-benchmarks.md]]
- Projects: [[70_projects/bundesinnovationshaushalt-trl.md]]
