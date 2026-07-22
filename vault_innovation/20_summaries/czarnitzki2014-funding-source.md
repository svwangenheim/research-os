---
title: "Innovation Subsidies: Does the Funding Source Matter for Innovation Intensity and Performance?"
note_type: source_summary
summary: "Czarnitzki and Lopes Bento compare national, EU, and combined innovation subsidies for German firms using a multiple-treatment matching design. They find that both national and EU grants increase innovation input, EU grants have stronger input effects when received alone, and national funding or national-plus-EU funding performs better on several output measures such as future patenting."
authors: [Dirk Czarnitzki, Cindy Lopes Bento]
year: 2011
source_files: ["10_sources/czarnitzki2014-funding-source.md"]
source_urls: ["http://ftp.zew.de/pub/zew-docs/dp/dp11053.pdf"]
projects: [bundesinnovationshaushalt-trl]
tags:
  - source-summary
  - rd-subsidies
  - eu-vs-national
  - additionality
  - germany
  - patent-quality
updated: "2026-05-04"
---

# Czarnitzki and Lopes Bento - Does the Funding Source Matter?

## Source paper link/path

- Source file: `10_sources/czarnitzki2014-funding-source.md`
- Source status: available as converted Markdown in `10_sources/`
- Verification status: semantically checked against the mapped source on 2026-05-04.

## Bibliographic metadata

- Title: "Innovation Subsidies: Does the Funding Source Matter for Innovation Intensity and Performance? Empirical Evidence from Germany"
- Authors: Dirk Czarnitzki and Cindy Lopes Bento
- Source version: ZEW Discussion Paper No. 11-053
- Source date: July 2011
- Institution: ZEW - Leibniz Centre for European Economic Research
- URL: http://ftp.zew.de/pub/zew-docs/dp/dp11053.pdf
- Geographic scope: Germany
- Sectoral scope: innovative firms in manufacturing and business services

## Detailed summary

This paper asks whether the source of innovation subsidies matters. Earlier evaluation work often estimated an average treatment effect for public R&D support or focused on one program. Czarnitzki and Lopes Bento instead distinguish national grants, European grants, the combination of both, and no grant, then compare their effects on innovation input and innovation performance for German firms.

The policy problem is that firms can receive support from multiple levels of government. If national and EU grants have different project-selection rules, grant sizes, administrative requirements, or target activities, their effects may differ. The paper therefore treats the policy mix itself as an empirical question rather than assuming that all subsidies are equivalent.

The study uses the Mannheim Innovation Panel, the German part of the Community Innovation Survey, with waves covering innovation activity from 1992-1994 through 2004-2006. The survey contains information on receipt of national and EU innovation subsidies, innovation expenditure, R&D intensity, innovation sales, and market novelties. The data are complemented with patent information to study future patent applications and forward citations. The sample is restricted to innovative German firms in manufacturing and business services.

Methodologically, the authors apply a multiple-treatment matching framework. The treatment categories distinguish firms receiving no subsidies, national subsidies only, EU subsidies only, and both national and EU subsidies. The first part estimates effects on innovation input, including R&D intensity and broader innovation intensity. The second part studies innovation performance while holding innovation input constant, using patenting, total innovation sales, sales from market novelties, and average forward citations per patent.

The input results show that national grants, EU grants, and the combination of both increase innovation input relative to no funding. Receiving both sources yields the largest input effect. Among firms that receive only one source, EU grants have stronger input effects, which the authors suggest may be connected to higher average EU grant amounts.

The output results are more nuanced. Funding from both sources is associated with higher sales from market novelties. If only one grant source is obtained, the paper finds superiority for national funding on several output measures. Nationally funded firms, either national-only or national-plus-EU, are more likely to file future patents. The citation analysis is used to check whether subsidized patents are merely administrative compliance with funding-agency advice or instead represent valuable technology. The paper finds evidence that subsidized patents receive more forward citations in relevant comparisons, supporting the interpretation that the patents reflect meaningful technological development.

For the wiki, this source should be used for funding-source heterogeneity, policy-mix evaluation, multiple-treatment matching, and German evidence on national versus EU innovation subsidies. It should not be used as a direct TRL, CORDIS, or Foerderkatalog classification source.

## Research question

Do national innovation subsidies, EU innovation subsidies, and the combination of both have different effects on German firms' innovation input and innovation performance?

## Core argument or contribution

The paper's contribution is to evaluate innovation subsidies as heterogeneous treatments. It shows that the source and combination of funding matter: EU and national grants are both additional for innovation input, but output patterns differ, with national funding and combined funding performing better on several measures of innovation performance.

## Methodology

- Design: multiple-treatment policy evaluation.
- Treatment categories: no subsidy, national subsidy only, EU subsidy only, and both national and EU subsidies.
- Estimator: non-parametric matching variant for multiple treatments.
- Input outcomes: R&D intensity and innovation intensity.
- Output outcomes: future patent applications, total innovation sales, sales from market novelties, and average forward citations per patent.
- Output design feature: innovation input is held constant when comparing performance outcomes, so the estimates focus on whether funded projects perform differently for a given innovation budget.
- Citation window: forward citations over a future window are used as a proxy for patent quality or technological importance.

## Datasets/materials used

- [[50_datasets/mannheimer-innovationspanel.md]]: German Community Innovation Survey data, including subsidy source, innovation input, and innovation sales measures.
- Patent databases: used to measure future patent applications and average forward citations per patent.

The source uses survey-based indicators of national and EU subsidy receipt. It does not use CORDIS or the German Foerderkatalog as project-level text datasets.

## Key findings

- National grants, EU grants, and combined national-plus-EU grants all increase innovation input compared with no funding.
- Receiving both national and EU funding produces the largest input effect.
- Among single-source treatments, EU grants have stronger effects on innovation input than national grants, possibly because EU grants are larger on average.
- Full crowding out is rejected for both national and EU grants.
- Funding from both sources is associated with higher sales from market novelties.
- If only one grant source is received, national funding performs better on several innovation-output measures.
- Nationally funded firms, including national-only and national-plus-EU recipients, are more likely to file future patents.
- Forward-citation evidence supports the interpretation that subsidized patents are not only compliance artifacts but reflect valuable technological developments in the studied comparisons.
- Product-sales results are less clear than the patent results, partly because product-market success may take longer to materialize than the cross-sectional survey design can capture.

## Limitations

- The paper relies on matching and therefore depends on observed covariates; unobserved selection into national versus EU support can still matter.
- The source uses survey waves and repeated cross-sectional information rather than a full causal panel design with firm fixed effects.
- Product-sales outcomes may not allow enough time from subsidized input to market output.
- Patent applications and forward citations are imperfect proxies for innovation quality and may not capture non-patented or non-market outcomes.
- The analysis is Germany-specific and tied to the subsidy instruments and EU-program environment covered by the MIP waves.
- The source does not evaluate project-level TRL, mission content, or budget-category allocation.

## Important concepts discussed

- [[30_concepts/rd-subsidy-additionality.md]]: the paper tests whether different funding sources increase innovation input and performance.
- [[30_concepts/radical-vs-incremental-innovation.md]]: relevant only indirectly through market novelties and patent citations; the paper does not provide a TRL or radicalness classification of individual projects.

## Methods discussed

- [[40_methods/causal-evaluation-innovation-policy.md]]: the paper uses multiple-treatment matching for innovation-policy evaluation.

## Datasets discussed

- [[50_datasets/mannheimer-innovationspanel.md]]
- Patent databases for future patenting and forward citations

## Relation to other papers in the vault

- [[czarnitzki2004-rd-subsidies-zew.md]]: earlier German additionality study focused on R&D spending and patent production for federal R&D project funding.
- [[cherif2022-rd-subsidies-imf.md]]: later German study on heterogeneity by ownership, industry, and size.
- [[aschhoff2010-who-gets-the-money.md]]: complements this paper by examining selection into direct project funding.
- [[beck2016-radical-or-incremental.md]]: related evaluation of whether policy affects radical versus incremental innovation outcomes.
- [[edler2017-innovation-policy.md]]: useful conceptual review for interpreting the paper within broader innovation-policy design and evaluation debates.

## Implications for LLM research or the project domain

For the Bundesinnovationshaushalt/TRL project, this source supports the idea that funding-source composition matters. National and EU support cannot be treated as interchangeable if the goal is to understand innovation input, patenting, market novelty, or project quality. For project-level retrieval, the paper is especially useful when comparing national German funding with EU funding or when asking whether different funding channels may select different project types. It does not itself provide a machine-readable project taxonomy or a validated TRL label source.

## Links to canonical concept, method, dataset, synthesis, and project notes

- [[30_concepts/rd-subsidy-additionality.md]]
- [[30_concepts/radical-vs-incremental-innovation.md]]
- [[40_methods/causal-evaluation-innovation-policy.md]]
- [[50_datasets/mannheimer-innovationspanel.md]]
- [[90_synthesis/germany-innovation-policy-evidence-map.md]]
- [[70_projects/bundesinnovationshaushalt-trl.md]]
