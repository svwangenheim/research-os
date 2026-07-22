---
title: "The Link Between R&D Subsidies, R&D Spending and Technological Performance"
note_type: source_summary
summary: "Czarnitzki and Hussinger (2004) study German manufacturing firms to test whether federal R&D project funding crowds out private R&D or instead increases total R&D spending and patenting. Using treatment-effect matching and a patent production function, they reject full and partial crowding out and find that publicly induced R&D has positive patent productivity."
authors: [Dirk Czarnitzki, Katrin Hussinger]
year: 2004
source_files: ["10_sources/czarnitzki2004-rd-subsidies-zew.md"]
source_urls: ["https://hdl.handle.net/10419/24065"]
projects: [bundesinnovationshaushalt-trl]
tags:
  - source-summary
  - rd-subsidies
  - additionality
  - germany
  - crowding-out
updated: "2026-05-04"
---

# Czarnitzki and Hussinger (2004) - R&D Subsidies, R&D Spending and Technological Performance

## Source paper link/path

- Source file: `10_sources/czarnitzki2004-rd-subsidies-zew.md`
- Source status: available as converted Markdown in `10_sources/`
- Verification status: semantically checked against the mapped source on 2026-05-04.

## Bibliographic metadata

- Title: "The Link Between R&D Subsidies, R&D Spending and Technological Performance"
- Authors: Dirk Czarnitzki and Katrin Hussinger
- Year: 2004
- Series: ZEW Discussion Papers, No. 04-56
- Institution: ZEW - Leibniz Centre for European Economic Research
- URL: https://hdl.handle.net/10419/24065
- Geographic scope: Germany
- Sectoral scope: manufacturing R&D performers
- Period: 1992-2000

## Detailed summary

This paper evaluates a core policy mechanism behind European and German R&D support: public R&D project funding should stimulate business R&D spending, and the induced R&D should lead to technological output. The source explicitly tests both links. First, it asks whether subsidies increase firms' R&D expenditure or merely replace private spending. Second, it asks whether the additional R&D associated with subsidies contributes to patenting.

The authors frame the problem through the Barcelona objectives and the European Action Plan, which aimed to raise R&D intensity and increase business-sector R&D. They note two reasons the mechanism could fail. Firms might substitute public money for R&D they would have financed anyway, creating full or partial crowding out. Even if subsidies induce additional R&D, the marginal projects funded by subsidies may have lower expected private returns or higher uncertainty, so the induced R&D might not generate patentable technological output.

Empirically, the paper links several firm-level data sources. The Mannheim Innovation Panel supplies innovation and firm-level survey information; the BMBF PROFI database identifies federal civilian R&D project funding; the German Patent and Trade Mark Office data provide patent applications; Creditreform contributes firm characteristics such as age, legal form, and ownership; and industry-level controls come from OECD STAN and German antitrust commission reports. The final data section reports a manufacturing sample for 1992-2000 with 588 federally funded firm-year observations and 3,191 non-funded observations after excluding firms with other public R&D grants, very small firms, and very large unique firms.

The empirical design proceeds in two stages. In the first stage, the authors estimate the average treatment effect on the treated for subsidy receipt using propensity-score-based nearest-neighbor matching. They compare subsidized firms with similar non-subsidized firms, imposing common support and industry restrictions. They then test whether total R&D, net private R&D, and R&D intensity are higher for subsidized firms. In the second stage, they use the estimated treatment effect to split R&D into counterfactual privately financed R&D and publicly induced additional R&D, then estimate patent production functions using negative binomial models for patent counts and probit models for whether a firm patents at all.

The main finding is that the study rejects both full and partial crowding out. Subsidies are associated with higher total R&D spending, and the results also support an acceleration effect: funded firms spend more net R&D than comparable non-funded firms. In the patent-production stage, both counterfactual privately financed R&D and the publicly induced R&D component have positive effects on patenting. The authors therefore conclude that federal R&D project funding does not merely re-label private research expenditure in their sample; it also contributes to technological performance as measured by patents.

For the wiki, this is a key additionality paper. It should be retrieved for subsidy additionality, crowding-out tests, German firm-level treatment-effect evaluation, and the link from R&D input to patent output. It should not be used as evidence on TRL levels, Foerderkatalog text classification, CORDIS, radical versus incremental innovation, or current German budget taxonomy.

## Research question

Do German federal R&D project subsidies increase firms' R&D spending, and does the additional R&D induced by subsidies improve technological performance measured by patent applications?

## Core argument or contribution

The paper's contribution is to connect input additionality and output additionality in one empirical framework. It does not only estimate whether subsidies raise R&D expenditure; it carries the estimated additional R&D into a patent production function to test whether publicly induced R&D has positive technological productivity.

## Methodology

- Design: two-stage firm-level evaluation.
- Stage 1: treatment-effect analysis for subsidy receipt, using propensity-score-based nearest-neighbor matching.
- Matching restrictions: common support and same-industry comparison requirements.
- Stage 1 outcomes: total R&D spending, R&D net of subsidies, R&D intensity, and net R&D intensity.
- Stage 2: patent production functions that distinguish counterfactual privately financed R&D from the estimated subsidy-induced R&D component.
- Patent models: negative binomial regressions for patent counts and probit models for whether a firm files at least one patent.
- Key controls: firm size, Eastern Germany indicator, firm age, patent stock, group membership, foreign ownership, legal form, export intensity, import intensity, market concentration, industry dummies, and time dummies.

## Datasets/materials used

- [[50_datasets/mannheimer-innovationspanel.md]]: annual ZEW innovation survey used for firm-level innovation and R&D information.
- BMBF PROFI database: identifies German federal civilian R&D project funding.
- German Patent and Trade Mark Office patent database: used for firm-level patent applications and patent stock construction.
- Creditreform firm database: provides firm age, legal form, and major shareholding information.
- OECD STAN and German antitrust commission data: provide industry-level controls.

The source does not use CORDIS or Foerderkatalog as datasets.

## Key findings

- The treatment-effect analysis rejects full crowding out: subsidized firms spend more total R&D than comparable non-subsidized firms.
- The analysis also rejects partial crowding out in the paper's tests of net R&D.
- The results support an acceleration effect: subsidies are associated with additional R&D beyond the subsidy itself.
- Both privately financed R&D and the estimated publicly induced R&D component have positive effects on patenting.
- The authors interpret the findings as supporting the policy mechanism that federal R&D support can raise business R&D engagement and technological performance.
- Eastern German firms show lower patenting activity in the patent regressions, and this gap remains after additional controls in robustness checks.

## Limitations

- The study is limited to German manufacturing R&D performers in the 1992-2000 period.
- The empirical design relies on selection on observables; unobserved differences between subsidized and non-subsidized firms can still affect results.
- The source uses pooled cross-sections because many firms are observed only once; it cannot use a full panel fixed-effects strategy.
- Patent applications are a narrow measure of innovation output and miss non-patented innovations, sales from new products, cost reductions, and employment effects.
- The sample excludes firms receiving other public R&D grants, firms below the minimum size threshold, and very large firms that lack plausible comparison firms.
- The paper tests project funding effects but does not classify projects by TRL, mission orientation, radicalness, or public value.

## Important concepts discussed

- [[30_concepts/rd-subsidy-additionality.md]]: central concept; the paper tests input additionality, crowding out, and patent-output additionality.

## Methods discussed

- [[40_methods/causal-evaluation-innovation-policy.md]]: the paper uses matching-based treatment-effect analysis and patent production functions for policy evaluation.

## Datasets discussed

- [[50_datasets/mannheimer-innovationspanel.md]]
- BMBF PROFI database
- German Patent and Trade Mark Office patent database
- Creditreform firm database

## Relation to other papers in the vault

- [[cherif2022-rd-subsidies-imf.md]]: later German firm-level subsidy study that examines heterogeneity by ownership, industry, and firm size.
- [[kleer2010-rd-subsidies-signal.md]]: complements this paper by examining subsidies as certification signals for external finance.
- [[aschhoff2010-who-gets-the-money.md]]: helps interpret which firms receive German direct project funding.
- [[howell2017-financing-innovation.md]]: provides US SBIR evidence on grant effects in early-stage innovation finance.
- [[beck2016-radical-or-incremental.md]]: evaluates Swiss innovation-policy effects and distinguishes radical and incremental innovation outcomes, which Czarnitzki and Hussinger do not.

## Implications for LLM research or the project domain

For the Bundesinnovationshaushalt/TRL project, this paper is useful as evidence that direct R&D project funding can generate additional firm R&D and patent output. It also highlights why the project should keep separate questions apart: whether subsidies increase R&D, whether induced R&D generates measurable output, and whether the funded portfolio is allocated to the right technological stages or societal goals. This source answers the first two questions for a historical German manufacturing sample; it does not answer the TRL or portfolio-composition question.

## Links to canonical concept, method, dataset, synthesis, and project notes

- [[30_concepts/rd-subsidy-additionality.md]]
- [[40_methods/causal-evaluation-innovation-policy.md]]
- [[50_datasets/mannheimer-innovationspanel.md]]
- [[90_synthesis/germany-innovation-policy-evidence-map.md]]
- [[70_projects/bundesinnovationshaushalt-trl.md]]
