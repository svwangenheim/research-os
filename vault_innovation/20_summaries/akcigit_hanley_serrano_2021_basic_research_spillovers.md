---
title: "Back to Basics: Basic Research Spillovers, Innovation Policy and Growth"
note_type: summary
authors: ["Ufuk Akcigit", "Douglas Hanley", "Nicolas Serrano-Velarde"]
year: 2021
doi: "10.1093/restud/rdaa061"
journal: "Review of Economic Studies"
volume: 88
issue: 4
pages: "1674–1718"
institution: "University of Chicago / University of Pittsburgh / Bocconi University"
proximity: 2
source_files:
  - "10_sources/akcigit_et_al_2021_back_to_basics.md"
source_urls:
  - "https://academic.oup.com/restud/article/88/4/1674/5922649"
projects:
  - "[[70_projects/bundesinnovationshaushalt-trl.md]]"
related_concepts:
  - "[[30_concepts/basic-research-in-firms.md]]"
  - "[[30_concepts/knowledge-spillovers-and-entrepreneurship.md]]"
  - "[[30_concepts/rd-subsidy-additionality.md]]"
related_methods: []
related_datasets: []
related_synthesis:
  - "[[90_synthesis/germany-innovation-policy-evidence-map.md]]"
tags:
  - summary
  - corporate-basic-research
  - innovation-policy
  - knowledge-spillovers
  - endogenous-growth
  - structural-estimation
updated: "2026-05-19"
---

# Back to Basics: Basic Research Spillovers, Innovation Policy and Growth

## Source paper link/path

- Source files: `10_sources/akcigit_et_al_2021_back_to_basics.md`
- Source URLs: https://academic.oup.com/restud/article/88/4/1674/5922649
- Source status: Published in Review of Economic Studies 88(4), 2021

## Bibliographic metadata

- Authors: Ufuk Akcigit (U Chicago), Douglas Hanley (U Pittsburgh), Nicolas Serrano-Velarde (Bocconi/IGIER)
- Year: 2021 (circulated 2020)
- Venue/institution: Review of Economic Studies
- DOI/URL: 10.1093/restud/rdaa061
- JEL: J82, L25, L50, O31, O38, O40

## Detailed summary

This paper builds a general equilibrium model of endogenous technical change with an explicit distinction between basic and applied research. Basic research is special in two ways: (1) it generates spillovers *across industries* (not just within a targeted industry as applied research does), and (2) private-sector basic research commercializes faster than public-sector basic research (the "Ivory Tower" effect of academic science). The model is estimated using French firm-level data on actual basic and applied research expenditures (2000–2006), exploiting the rare availability of within-firm basic/applied decomposition from the French Ministry of Research survey.

The central quantitative finding is that 68% of cross-industry spillovers from basic research are not internalized in the decentralized equilibrium. This creates dynamic misallocation of research *within types* — not primarily between production and research as in standard Romer/Klette-Kortum models, but between basic and applied innovation. The welfare loss is 4.6 percentage points in consumption-equivalent terms.

A striking secondary result: there is *overinvestment* in applied research in the decentralized equilibrium, driven by strategic complementarity between basic research spillovers and applied research returns. Uniform R&D subsidies make this worse by pushing even more resources into the over-supplied applied category.

The optimal policy is type-dependent: subsidize basic research at 49%, applied research at 11%. This result is robust to misclassification of research types up to 50%. Public basic research and its productive interaction with the private sector are welfare-improving even independent of the subsidy question.

## Research question

What are the differential roles of basic versus applied research in the growth process? What is the optimal public policy to address research misallocation given that basic research generates cross-industry externalities that applied research does not?

## Core argument or contribution

1. First structural quantification of the welfare loss from basic-vs-applied research misallocation in a GE framework.
2. The dominant market failure is wrong *composition* of R&D (too much applied, too little basic), not insufficient total R&D.
3. Uniform R&D subsidies are welfare-inferior; type-specific subsidies are needed.
4. Optimal policy: 49% subsidy for basic research, 11% for applied.

## Methodology

- **Model**: General equilibrium multi-industry framework (Klette-Kortum 2004 extended); basic vs. applied distinction; public vs. private research sectors
- **Estimation**: Structural estimation via simulated method of moments (SMM)
- **Identification of spillovers**: Cross-industry spillovers from basic research identified through multi-industry firm investment patterns (diversified firms invest proportionally more in basic research)
- **Validation**: Patent citation data (NBER) used to measure innovation step-size and importance for follow-up innovations

## Datasets/materials used

- **French R&D Survey** (annual, French Ministry of Research, 2000–2006): unique basic/applied decomposition at firm level
- **LIFI + EAE**: French databases for multi-industry presence and ownership links
- **NBER patent citation data**: innovation quality measurement
- Final sample: 13,708 firm-year observations

## Key findings

1. 68% of cross-industry basic research spillovers are not internalized.
2. Welfare loss of 4.6 pp (consumption-equivalent) from dynamic research misallocation.
3. Overinvestment in applied research in the decentralized equilibrium.
4. Optimal subsidy: 49% basic, 11% applied — robust to ≤50% misclassification.
5. Eliminating public basic research substantially reduces welfare; public-private interaction matters.

## Limitations

- French data: generalizability to Germany or other innovation systems uncertain
- Basic/applied split in administrative data may not perfectly match the theoretical concept
- Does not explicitly model the absorptive capacity mechanism through which basic research benefits firms (see Martinez-Senra et al. 2011 for the micro-level channel)

## Important concepts discussed

- [[30_concepts/basic-research-in-firms.md]]: private vs. public basic research; "Ivory Tower" theory; Pasteur's Quadrant (Stokes 1997)
- [[30_concepts/knowledge-spillovers-and-entrepreneurship.md]]: basic research generates larger and broader spillovers than applied research
- Dynamic misallocation: research composition failure
- Type-dependent vs. uniform subsidies

## Methods discussed

- Structural GE estimation, simulated method of moments
- Patent citation quality measures (Hall-Jaffe-Trajtenberg 2001)

## Datasets discussed

- French R&D Survey (basic/applied decomposition)
- NBER patent citation database

## Relation to other papers in the vault

- **[[20_summaries/arora_belenzon_sheer_2017_why_firms_invest_in_research.md]]**: micro-level companion documenting the internal appropriation mechanism
- **[[20_summaries/arora2018-corporate-basic-research.md]]**: documents corporate basic research decline; this paper explains why it's welfare-costly
- **[[20_summaries/akcigit2024-innovation-paradox.md]]**: Akcigit's broader innovation paradox diagnosis; this paper provides structural foundations
- **[[20_summaries/dechezlepretre2023-rd-tax-spillovers.md]]**: empirical R&D tax incentives evidence; this paper provides theoretical rationale for type-specific subsidies
- **[[20_summaries/martinez_senra_et_al_2011_basic_research_firms_spain.md]]**: micro-level evidence for the basic research → absorptive capacity → innovation mechanism encoded in the macro model

## Implications for the project domain

- **Bundesinnovationshaushalt**: if Germany's public R&D funding does not target basic research (TRL 1–3) explicitly, it may subsidize the already-over-provided applied research category
- The 49% optimal basic research subsidy rate implies current support levels for early-stage projects are substantially insufficient
- Uniform subsidies (e.g., ZIM program, which does not discriminate by TRL) may reduce welfare by exacerbating applied research overinvestment
- Germany's Fraunhofer/Helmholtz → industry transfer model should be evaluated against the prediction that public basic research quality and public-private connectivity are welfare-critical

## Links to canonical concept, method, dataset, synthesis, and project notes

- Concepts: [[30_concepts/basic-research-in-firms.md]], [[30_concepts/knowledge-spillovers-and-entrepreneurship.md]], [[30_concepts/rd-subsidy-additionality.md]]
- Projects: [[70_projects/bundesinnovationshaushalt-trl.md]]
- Synthesis: [[90_synthesis/germany-innovation-policy-evidence-map.md]]
