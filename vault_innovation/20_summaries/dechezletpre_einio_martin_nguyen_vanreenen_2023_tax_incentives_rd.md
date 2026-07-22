---
title: "Do Tax Incentives for Research Increase Firm Innovation? An RD Design for R&D"
note_type: summary
authors: ["Antoine Dechezleprêtre", "Elias Einiö", "Ralf Martin", "Kieu-Trang Nguyen", "John Van Reenen"]
year: 2023
doi: "NBER Working Paper 22405"
venue: "National Bureau of Economic Research"
publication_date: "2016-07 (Updated 2023)"
proximity: 2
source_files:
  - "dechezletpre_2023_tax_incentives_research.md"
projects:
  - "Bundesinnovationshaushalt"
  - "Fördermaßnahmen-Evaluierung"
related_concepts:
  - "[[R&D Tax Incentives]]"
  - "[[Firm Innovation]]"
  - "[[Policy Evaluation]]"
  - "[[SME Innovation]]"
related_methods:
  - "[[Regression Discontinuity Design (RDD)]]"
  - "[[Causal Inference]]"
  - "[[Patent Quality Analysis]]"
  - "[[Firm-level Policy Analysis]]"
related_datasets:
  - "HMRC administrative tax data (UK)"
  - "Patent databases"
  - "Firm performance metrics (TFP, size)"
tags:
  - summary
  - innovation-economics
  - policy-evaluation
  - causal-methods
updated: "2026-05-17"
---

> **⚠ DUPLICATE — see canonical:** [[20_summaries/dechezlepretre2023-rd-tax-spillovers.md]]
> Created during batch ingest 2026-05-17. Contains an earlier version with incorrectly attributed claims (no TRL-differentiated estimates in paper). The corrected canonical was verified against source on 2026-05-18.

# Do Tax Incentives for Research Increase Firm Innovation? An RD Design for R&D

## Source paper link/path

- Source files: `vault/10_sources/dechezletpre_2023_tax_incentives_research.md`
- Venue: National Bureau of Economic Research (NBER)
- Working Paper: No. 22405
- Publication date: July 2016 (updated 2023)
- DOI: NBER WP 22405

## Bibliographic metadata

- **Authors:** Antoine Dechezleprêtre (LSE), Elias Einiö (LSE), Ralf Martin (Imperial College/LSE), Kieu-Trang Nguyen (LSE), John Van Reenen (LSE/NBER)
- **Institution:** Centre for Economic Performance, London School of Economics
- **Year:** 2016 (updated 2023)
- **JEL Code:** O31 (Technological Change and Progress)

## Detailed summary

This paper presents causal evidence that R&D tax incentives increase both firm innovation and firm R&D spending. The authors address major limitations in prior literature by: (1) measuring both R&D spending and innovation (patents), (2) analyzing patent quality, (3) studying SMEs (where constraints bind), and (4) using a credible causal design.

They exploit a UK policy reform that raised the asset-based size threshold for SME access to more generous R&D tax relief. Using a Regression Discontinuity Design (RDD) with administrative tax data for the universe of UK firms (1980-2011), they find:

- **Large positive effects** on both R&D spending and quality-adjusted patenting
- **High R&D price elasticity** (~2.6), suggesting SMEs are financially constrained
- **Positive spillovers** on innovation in technologically related firms
- **Economically significant aggregate effect**: business R&D would be ~10% lower without the tax relief scheme

## Research question

Do R&D tax incentives actually increase firm innovation (not just reported R&D spending)? What is the magnitude of the effect, especially for financially constrained firms? Are there spillover effects on other firms?

## Core argument or contribution

Prior work on R&D tax policy faces two critical problems: (1) it measures only R&D spending, not actual innovation, so tax credits could simply relabel existing activities; (2) it focuses on large firms with internal research capacity. This paper solves both problems by analyzing both R&D and patents (innovation) for SMEs using a clean causal design (RDD). The large elasticity (~2.6) suggests that SMEs are severely credit-constrained and thus highly responsive to tax incentives.

## Methodology

**Study Design: Regression Discontinuity Design (RDD)**
- **Policy exploit:** UK 2008 reform raised SME threshold for R&D tax relief from EC definition to a higher asset-based threshold
- **Running variable:** Firm assets (pre-determined, not subject to post-policy manipulation)
- **Discontinuity:** Access to higher tax relief rate at threshold
- **Window:** Firms near the threshold, analyzed pre- and post-reform

**Data sources:**
- **HMRC Datalab:** Administrative tax records for population of UK firms (1980-2011)
- **Patent data:** USPTO and UK patent applications
- **Patent quality metrics:** Citations, forward citations, international patent status
- **Firm performance:** Total factor productivity (TFP), employment, size
- **Balance checks:** Covariate balance across threshold, no bunching of assets pre-reform

**Sample:** All UK firms filing corporate tax returns near the SME size threshold (both treated and control firms observed over time)

## Datasets/materials used

- **HMRC (Her Majesty's Revenue and Customs):** Complete administrative tax records for UK firms, including R&D credits claimed
- **Patent data:** USPTO and UK Intellectual Property Office filings
- **Compustat and Amadeus:** Firm financial data for analysis of TFP and other performance metrics
- **Patent citation databases:** Forward and backward citations as quality indicators

## Key findings

### 1. **Effect on R&D Spending:**
- Firms just above the threshold (eligible for higher relief) spend ~19-22% more on R&D post-reform
- Effect is robust to alternative model specifications
- Effect is larger for firms with lower prior R&D intensity (suggesting credit constraint)

### 2. **Effect on Innovation (Patents):**
- Patenting increases by ~15% post-reform
- **Quality-adjusted patents also increase**, suggesting innovation is real (not just relabeling)
- Effect is strongest for patents in core technological areas for the firm
- No evidence of gaming (low-quality patent filing)

### 3. **R&D Price Elasticity:**
- **Elasticity ~2.6** — extremely high compared to large firm estimates (typically 0.5-1.5)
- Suggests SMEs are **severely financially constrained** in R&D investment
- Tax relief is especially cost-effective for SMEs

### 4. **Spillover Effects:**
- Firms in technologically related industries also increase patenting
- Suggests **positive knowledge spillovers** from the tax-induced R&D
- Spillovers are economically significant

### 5. **Aggregate Effects:**
- Aggregate business R&D would be ~10% lower without the tax relief scheme (2006-2011 period)
- Aggregate patent counts would be substantially lower

### 6. **No Evidence of Pre-policy Manipulation:**
- Covariate balance across threshold pre-reform
- No bunching of assets around the threshold pre-reform
- Pre-reform trends in R&D and patents are smooth across threshold (confirming validity of RDD)

## Limitations

- **Geographic scope:** UK only (1980-2011), so findings may not generalize to other countries/time periods
- **Time window:** Data end in 2011; effects may have changed with economic conditions
- **SME focus:** Sample is SMEs near the threshold; results may not apply to large firms or very small firms
- **Spillover measurement:** Spillovers measured only on patenting (not product market outcomes or long-term firm growth)
- **Patent quality:** Patent counts and citations may not fully capture innovation value (software, service innovations underrepresented)

## Important concepts discussed

- **R&D Tax Incentives** — fiscal policy tools to subsidize private R&D
- **Financial Constraints** — barriers to R&D investment due to credit rationing or high cost of capital
- **Additionality** — whether policy-induced R&D is additional or displaces other spending
- **Patent Quality** — forward citations, international patent status as quality indicators
- **Knowledge Spillovers** — external benefits of private R&D to other firms/society
- **SME Innovation** — particular importance of credit constraints for smaller firms
- **Policy Elasticity** — responsiveness of firm behavior to policy changes

## Methods discussed

- **Regression Discontinuity Design (RDD)** — exploiting sharp threshold in policy eligibility
- **Covariate balance tests** — checking validity of RDD assumptions
- **Bunching analysis** — detecting strategic behavior around policy threshold
- **Patent citation analysis** — measuring innovation quality
- **Event study methodology** — comparing pre/post-reform outcomes

## Datasets discussed

- HMRC administrative tax records (complete firm population)
- Patent application databases (USPTO, UKIPO)
- Patent citation databases (forward and backward)
- Firm financial data (Compustat, Amadeus)

## Relation to other papers in the vault

**Related causal inference work:**
- **Arora et al. (2018)** — Complements this work by showing corporate labs are declining; tax incentives may help sustain private R&D
- **Cohen & Levinthal (1990)** — Absorptive capacity relevant for understanding spillover mechanisms

**Related policy evaluation work:**
- **David et al. (2000)** — Foundational survey of public R&D grant effectiveness; this paper extends to tax incentives
- **Hall & Van Reenen (2000)** — Earlier work on R&D tax policy effects

## Implications for innovation policy and research

**For R&D tax policy:**
- **High effectiveness for SMEs:** Tax incentives are particularly cost-effective for financially constrained firms
- **Spillovers justify support:** Positive externalities suggest policy is socially beneficial beyond private returns
- **Magnitude matters:** 10% aggregate R&D effect is substantial and justifies continued support

**For empirical research on policy:**
- RDD design with administrative data is powerful for causal inference
- Must analyze both inputs (R&D spending) and outputs (patents) to avoid relabeling issues
- Patent quality analysis is essential

**For German innovation policy (Bundesinnovationshaushalt context):**
- Tax incentives for SMEs are evidence-based, high-effectiveness tools
- Spillover analysis suggests coordination between firms creates value
- SME credit constraints suggest targeted support for smaller firms is important
- Could inform design of German R&D tax credit reform

## Links to canonical concept, method, dataset, synthesis, and project notes

### Concepts:
- [[R&D Tax Incentives]]
- [[SME Innovation]]
- [[Financial Constraints on Innovation]]
- [[Knowledge Spillovers]]
- [[Policy Evaluation]]

### Methods:
- [[Regression Discontinuity Design (RDD)]]
- [[Causal Inference Methods]]
- [[Patent Quality Metrics]]

### Datasets:
- [[HMRC Administrative Tax Data]]
- [[Patent Citation Data]]

### Synthesis pages to update:
- [[Effectiveness of R&D Policy Instruments]]
- [[Firm-level Innovation Response to Policy]]
- [[Spillover Effects in Innovation Systems]]

### Project notes (Bundesinnovationshaushalt):
- Provides methodological template for evaluating federal R&D support effectiveness
- Evidence on SME responsiveness to policy can inform TRL targeting
- Spillover analysis relevant for designing complementary programs
