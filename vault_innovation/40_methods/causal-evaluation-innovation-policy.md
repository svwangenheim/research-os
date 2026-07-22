---
title: "Causal Evaluation of Innovation Policy"
note_type: method
summary: "Causal evaluation of innovation policy estimates whether observed firm, project, or system outcomes were caused by a policy instrument rather than merely correlated with it. The method layer covers counterfactual designs, matching, difference-in-differences, regression discontinuity, randomized or quasi-experimental designs, and evaluation-data requirements for R&D grants, tax incentives, and innovation programs."
canonical: true
aliases:
  - causal analysis of policy effects
  - Kausalanalyse von Maßnahmeneffekten
  - counterfactual innovation-policy evaluation
  - impact evaluation of R&D policy
assumptions:
  - comparable treated and control units or a credible source of quasi-random variation
  - outcome data observed after treatment
  - transparent treatment definition and timing
  - access to administrative, survey, or firm-level data
related_summaries:
  - "[[20_summaries/efi2024-gutachten.md]]"
  - "[[20_summaries/prognos2019-zim-evaluation.md]]"
  - "[[20_summaries/stehnken2024-zim-evaluation.md]]"
  - "[[20_summaries/struss2016-zim-wirkungsanalyse.md]]"
  - "[[20_summaries/audretsch2002-sbir-evaluation.md]]"
  - "[[20_summaries/aschhoff2010-who-gets-the-money.md]]"
  - "[[20_summaries/czarnitzki2004-rd-subsidies-zew.md]]"
  - "[[20_summaries/kleer2010-rd-subsidies-signal.md]]"
related_concepts:
  - "[[30_concepts/data-access-for-innovation-policy.md]]"
  - "[[30_concepts/mission-oriented-innovation-policy.md]]"
  - "[[30_concepts/sme-innovation-participation.md]]"
related_datasets:
  - "[[50_datasets/mannheimer-innovationspanel.md]]"
  - "[[50_datasets/foerderkatalog-des-bundes.md]]"
related_synthesis:
  - "[[90_synthesis/innovation-policy-governance-and-evaluation.md]]"
projects:
  - "[[70_projects/bundesinnovationshaushalt-trl.md]]"
tags:
  - method
  - evaluation
  - causal-inference
  - innovation-policy
updated: "2026-04-29"
---

# Causal Evaluation of Innovation Policy

## What it does

Causal evaluation estimates whether a policy instrument caused an observed change in outcomes. In innovation policy, the treatment may be an R&D grant, a tax credit, a procurement program, a mission instrument, a transfer program, or participation in a support scheme. Outcomes can include R&D spending, patents, sales from new products, employment, productivity, commercialization, survival, private finance, or adoption of a technology.

The method matters because descriptive evaluation can show that funded firms performed well, but not whether they performed well because of the funding. EFI 2024 explicitly argues that many federally commissioned F&I-policy evaluations do not allow causal conclusions, making causal evaluation a core method gap for evidence-based policy learning.

## When to use it

Use this method when the question is:

- Did a subsidy, grant, tax credit, or program change firm behavior?
- Did public funding add to private R&D, or crowd it out?
- Did a program increase commercialization, patents, sales, survival, or employment?
- Did a mission instrument shift the innovation portfolio?
- Did a policy activate firms that had not previously conducted R&D?

Do not use it when the question is purely descriptive, such as "what share of projects are TRL 4-6?" A TRL classifier describes the portfolio; causal evaluation estimates the effect of a policy instrument.

## Identification logic

Credible causal evaluation requires a counterfactual: what would have happened without the policy. Common designs include:

- randomized assignment where feasible;
- regression discontinuity around application scores or eligibility thresholds;
- difference-in-differences using before/after changes in treated and comparison groups;
- matching or entropy balancing to construct comparable control groups;
- instrumental variables when a credible instrument exists;
- event-study designs around policy or program changes.

The design must align treatment timing, comparison group, outcome window, and data availability.

## Assumptions

The key assumptions depend on design, but common requirements are:

- treatment and control units are comparable after adjustment;
- no unobserved shocks differentially affect treated units in ways that mimic treatment effects;
- outcome measures are observed consistently;
- selection into treatment is handled by design or modeling;
- spillovers are considered rather than ignored;
- administrative data and survey data are linkable and reliable.

## Papers using or discussing this method

- [[20_summaries/efi2024-gutachten.md]]: demands systematic integration of causal analysis into F&I-policy evaluation and better data access for evaluators.
- [[20_summaries/prognos2019-zim-evaluation.md]]: combines monitoring, surveys, interviews, descriptive indicators, and econometric counterfactual analysis of ZIM effects, while flagging small-sample robustness limits.
- [[20_summaries/stehnken2024-zim-evaluation.md]]: uses counterfactual impact analysis and entropy balancing in the ZIM evaluation.
- [[20_summaries/struss2016-zim-wirkungsanalyse.md]]: evaluates ZIM impacts and provides earlier evidence on additionality and outcomes.
- [[20_summaries/audretsch2002-sbir-evaluation.md]]: evaluates SBIR-supported research and commercialization outcomes.
- [[20_summaries/aschhoff2010-who-gets-the-money.md]], [[20_summaries/czarnitzki2004-rd-subsidies-zew.md]], and [[20_summaries/kleer2010-rd-subsidies-signal.md]]: connect R&D subsidies to selection, technological performance, and private finance.

## Common pitfalls

- treating funded firms' post-treatment outcomes as program effects without a counterfactual;
- comparing treated and untreated firms that differ systematically before funding;
- measuring outputs too soon for innovation effects to appear;
- ignoring firms that would have innovated without public support;
- failing to observe spillovers, unsuccessful applicants, or non-applicants;
- evaluating only published success cases;
- lacking access to administrative and outcome data.

## Strengths and limitations

The strength of causal evaluation is policy learning: it can distinguish additionality from selection and help improve instrument design. Its limitation is data and design feasibility. Some instruments are difficult to evaluate cleanly because treatment is targeted, outcomes are delayed, spillovers are large, or administrative data are not accessible. EFI 2024's data-access recommendations are therefore part of the method, not an external detail.

## Related concepts and datasets

- [[30_concepts/data-access-for-innovation-policy.md]]
- [[30_concepts/mission-oriented-innovation-policy.md]]
- [[30_concepts/sme-innovation-participation.md]]
- [[50_datasets/mannheimer-innovationspanel.md]]
- [[50_datasets/foerderkatalog-des-bundes.md]]

## Use cases in my work

For the Bundesinnovationshaushalt/TRL project, this note marks the boundary between portfolio mapping and impact evaluation. LLM classification can identify the technological maturity and thematic distribution of projects, but any claim that a program caused more innovation, higher productivity, or better commercialization requires a causal evaluation design and outcome data.
