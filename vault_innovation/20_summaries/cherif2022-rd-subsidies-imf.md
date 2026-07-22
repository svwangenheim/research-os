---
title: "Promoting Innovation: The Differential Impact of R&D Subsidies"
note_type: source_summary
summary: "Cherif, Hasanov, Grimpe, and Sofka (2022) use German firm-level innovation and patent data to estimate how R&D subsidies affect R&D spending and future patenting across ownership types, industries, and firm-size classes. The paper finds positive subsidy effects on R&D and patents, but the size and form of the response vary more by ownership and industry than by firm size."
authors: [Reda Cherif, Fuad Hasanov, Christoph Grimpe, Wolfgang Sofka]
year: 2022
source_files: ["10_sources/cherif2022-rd-subsidies-imf.md"]
source_urls: ["https://ssrn.com/abstract=4234381"]
projects: [bundesinnovationshaushalt-trl]
tags:
  - source-summary
  - rd-subsidies
  - heterogeneous-effects
  - germany
  - imf
updated: "2026-05-04"
---

# Cherif et al. (2022) - Promoting Innovation: The Differential Impact of R&D Subsidies

## Source paper link/path

- Source file: `10_sources/cherif2022-rd-subsidies-imf.md`
- Source status: available as converted Markdown in `10_sources/`
- Verification status: semantically checked against the mapped source on 2026-05-04.

## Bibliographic metadata

- Title: "Promoting Innovation: The Differential Impact of R&D Subsidies"
- Authors: Reda Cherif, Fuad Hasanov, Christoph Grimpe, Wolfgang Sofka
- Year: 2022
- Publication type: IMF Working Paper, WP/22/192
- Institution: International Monetary Fund, European Department
- URL: https://ssrn.com/abstract=4234381
- Geographic scope: Germany
- Period covered by source data: German innovation survey waves from the 2000s, linked to EPO patent applications through 2011

## Detailed summary

This working paper studies whether public R&D subsidies increase firm innovation and whether the effect differs by ownership, industry, and firm size. Its starting point is that average subsidy effects are not sufficient for policy design: two firms can both receive R&D support while differing strongly in ownership structure, technological environment, market position, and capacity to convert subsidized R&D into patentable output.

The paper uses Germany as the empirical setting because German innovation policy relies heavily on application-based grants rather than R&D tax credits during the studied period, and because Germany combines high R&D intensity, large domestic firms, foreign multinational subsidiaries, and a mature innovation system. The source frames R&D subsidies as a response to market failures such as knowledge spillovers, imperfect information, financing frictions, network failures, and possible lock-in around existing technologies.

The empirical design links firm-level innovation survey data from the Mannheim Innovation Panel with EPO patent applications. The authors estimate subsidy effects on two outcomes: R&D spending as an innovation input and patent applications over the following five years as an innovation output. They compare subsidized firms with comparable non-subsidized firms using propensity score matching and regressions on the matched sample. The treatment is receipt of an R&D subsidy; the source does not observe the subsidy amount, so it can estimate positive effects on R&D spending but cannot calculate a full subsidy multiplier relative to euros of public support.

The core result is that subsidies are associated with higher R&D spending and higher subsequent patenting, but the effect is heterogeneous. Domestic firms show stronger R&D-spending responses in low-tech manufacturing, knowledge-intensive services, and technological services. Domestic and foreign multinational firms show broadly similar R&D-spending responses, with larger responses in medium-tech and high-tech manufacturing. On patenting, foreign multinational subsidiaries have a stronger response than domestic multinationals in most industries. By contrast, the source reports that subsidy effects do not differ substantially by firm size. This is important because it cautions against inferring from this paper alone that small firms always respond more strongly to R&D subsidies than large firms.

For the Bundesinnovationshaushalt and TRL wiki, the paper is most useful as evidence on heterogeneous additionality: public R&D support can raise firm-level innovation input and patent output, but the expected effect depends on the type of firm and sector receiving support. It is not a paper about TRL measurement, Foerderkatalog program coding, or the public value of patent content. It should therefore be used as an empirical subsidy-effect study, not as a source for readiness-level classification or direct budget taxonomy rules.

## Research question

Do R&D subsidies increase firms' innovation input and output in Germany, and do these effects vary by firm ownership, industry, and size?

## Core argument or contribution

The paper contributes firm-level evidence that R&D subsidy effects are positive but not uniform. It shifts the policy question from whether subsidies have an average effect to where and for whom subsidies generate different R&D-spending and patenting responses. Its most relevant contribution for the wiki is the interaction between subsidy receipt, ownership type, industry, and innovation outcomes.

## Methodology

- Empirical setting: German firms in the 2000s.
- Treatment: receipt of an R&D subsidy.
- Outcomes: firm R&D expenditures and EPO patent applications in the following five years.
- Estimation strategy: propensity score matching followed by regressions on the matched sample.
- Unit of observation: firm observations from repeated survey waves, not a clean firm fixed-effects panel.
- Ownership groups: foreign multinational subsidiaries, domestic multinational firms, and domestic firms.
- Industry groups: low-tech manufacturing, medium-tech manufacturing, high-tech manufacturing, distributive services, knowledge-intensive services, and technological services.
- Size groups: small firms, medium-sized firms, and large firms.
- Controls discussed in the source include firm size, age, current and historical patenting, human-capital share, continuous R&D, export share, process innovation, industry, and time indicators.

## Datasets/materials used

- [[50_datasets/mannheimer-innovationspanel.md]]: German component of the Community Innovation Survey, used for firm-level innovation, subsidy, ownership, size, industry, R&D, and control variables.
- EPO patent application data: linked to firms by assignee names and addresses; used to construct patent outcomes and historical patenting controls.

The source uses MIP survey waves from 2000, 2002, 2003, 2004, and 2006. The source states that 2001 and 2005 are not used because the subsidy-receipt questions are unavailable in those years.

## Key findings

- Subsidized firms spend more on R&D than comparable non-subsidized firms.
- Subsidized firms also show higher future patenting activity.
- The effect on R&D spending differs by ownership and industry.
- Domestic firms have larger R&D-spending responses in low-tech manufacturing, knowledge-intensive services, and technological services.
- Domestic and foreign multinational firms have broadly similar R&D-spending responses, with stronger effects in medium-tech and high-tech manufacturing.
- Foreign multinational subsidiaries show stronger patent responses than domestic multinationals in most industries.
- Subsidy effects do not differ substantially by firm size in the paper's estimates.
- Because subsidy amounts are not observed, the paper supports a positive effect on R&D spending but does not prove a euro-for-euro multiplier above one.

## Limitations

- The dataset identifies subsidy receipt but not subsidy amount, limiting fiscal cost-effectiveness or multiplier interpretation.
- The design uses matching on observables; unobserved selection into subsidy receipt can still matter.
- The source uses repeated cross-sections rather than a panel design with firm fixed effects.
- Patent applications are an incomplete measure of innovation output and favor patentable technological activity.
- The five-year patent outcome window reduces but does not remove attribution problems.
- The sample construction excludes very small firms below the source's cutoff and excludes firms without product or process innovation activity, so results should not be generalized to every German firm.
- The study is Germany-specific and tied to the application-based grant regime of the 2000s.
- The paper does not evaluate TRL levels, Foerderkatalog budget categories, or mission-oriented portfolio design directly.

## Important concepts discussed

- [[30_concepts/rd-subsidy-additionality.md]]: central concept; the paper estimates whether subsidized firms increase R&D spending and future patenting compared with comparable non-subsidized firms.
- [[30_concepts/sme-innovation-participation.md]]: relevant only as a boundary condition; the paper tests firm-size heterogeneity but does not find substantially different subsidy effects by size.

## Methods discussed

- [[40_methods/causal-evaluation-innovation-policy.md]]: the paper uses propensity score matching and matched-sample regressions to approximate counterfactual outcomes for subsidized firms.

## Datasets discussed

- [[50_datasets/mannheimer-innovationspanel.md]]

## Relation to other papers in the vault

- [[czarnitzki2004-rd-subsidies-zew.md]]: closely related German evidence on R&D subsidy additionality and firm-level innovation behavior.
- [[kleer2010-rd-subsidies-signal.md]]: complements Cherif et al. by treating subsidies as a possible signal in financing markets.
- [[howell2017-financing-innovation.md]]: provides US SBIR evidence on early-stage public R&D funding and innovation outcomes, useful for comparing direct grants across institutional contexts.
- [[aschhoff2010-who-gets-the-money.md]]: helps interpret selection into German R&D programs, while Cherif et al. focuses on effects conditional on subsidy receipt.
- [[akcigit2024-innovation-paradox.md]]: should be used as a broader competition-and-incumbency contrast, not as support for Cherif et al.'s firm-size result.

## Implications for LLM research or the project domain

For project retrieval, this source should support questions about additionality, heterogeneous subsidy effects, and the design of evidence-aware innovation budgets. It suggests that policy evaluation should not stop at aggregate spending totals or average effects: ownership and industry composition matter for expected R&D and patent outcomes. For a Bundesinnovationshaushalt/TRL workflow, the paper is useful when interpreting whether funding concentrated in particular sectors or firm types is likely to generate different innovation responses. It does not by itself answer whether a project is early-stage, frontier-creating, mission-oriented, or socially valuable.

## Links to canonical concept, method, dataset, synthesis, and project notes

- [[30_concepts/rd-subsidy-additionality.md]]
- [[30_concepts/sme-innovation-participation.md]]
- [[40_methods/causal-evaluation-innovation-policy.md]]
- [[50_datasets/mannheimer-innovationspanel.md]]
- [[90_synthesis/germany-innovation-policy-evidence-map.md]]
- [[70_projects/bundesinnovationshaushalt-trl.md]]
