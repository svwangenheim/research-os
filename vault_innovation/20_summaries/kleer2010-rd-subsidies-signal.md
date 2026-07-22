---
title: "Government R&D Subsidies as a Signal for Private Investors"
note_type: source_summary
summary: "Kleer (Research Policy, 2010) develops a theoretical signaling model of government R&D subsidies under asymmetric information between firms, banks, and a public agency. The paper does not present a German firm-panel estimate. Its central claim is conditional: a subsidy decision that only reveals whether a project is basic or applied research may be of limited use to private investors, but if the subsidy is accompanied by credible quality information, it can lead to increased or better-selected private investment."
authors: ["Robin Kleer"]
year: 2010
source_files: ["10_sources/kleer2010-rd-subsidies-signal.md"]
source_urls:
  - "https://doi.org/10.1016/j.respol.2010.08.001"
projects:
  - bundesinnovationshaushalt-trl
related_concepts:
  - "[[30_concepts/rd-subsidy-additionality.md]]"
  - "[[30_concepts/equity-gap-sme-financing.md]]"
related_methods: []
related_datasets: []
related_synthesis:
  - "[[90_synthesis/innovation-policy-governance-and-evaluation.md]]"
tags:
  - source-summary
  - rd-subsidies
  - signaling
  - private-finance
  - asymmetric-information
updated: "2026-05-04"
---

# Kleer (2010) - Government R&D Subsidies as a Signal

## Source paper link/path

- Source file: `10_sources/kleer2010-rd-subsidies-signal.md`
- Source status: available as converted Markdown in `10_sources/`
- Verification status: semantically checked against the mapped source on 2026-05-04.

## Bibliographic metadata

- Title: "Government R&D Subsidies as a Signal for Private Investors"
- Author: Robin Kleer
- Year: 2010
- Journal: Research Policy, 39(10), 1361-1374
- DOI: `10.1016/j.respol.2010.08.001`
- Institution listed in source: RWTH Aachen University, Technology and Innovation Management Group

## Detailed summary

Kleer studies whether government R&D subsidies can function as a signal for private investors. The paper starts from the standard rationale for public R&D support: socially valuable projects may have private returns that are too low because of spillovers, low appropriability, high risk, or long time horizons. Public agencies therefore try to support projects with high social returns that private investors would otherwise underfund. But the subsidy decision may also transmit information to banks or investors, especially where private actors cannot easily assess project quality.

The source is a theoretical model, not an empirical evaluation. It builds a signaling game with three actors: firms that apply for R&D subsidies, a government agency that screens projects and decides whether to grant a subsidy, and banks that observe the subsidy decision and decide whether to provide loans. The agency has better information about project type than banks. Projects are stylized as basic research or applied research. Basic research is socially valuable but less privately attractive because it is risky, hard to appropriate, and produces spillovers. Applied research is more privately attractive but less central to the agency's social-return objective.

The paper first considers a setup in which the subsidy can only distinguish between basic and applied research. In that case, the subsidy signal is often not very helpful for banks. If the agency mainly uses subsidies to support socially valuable basic research, banks may infer that subsidized projects are less privately profitable. Pooling equilibria, in which the agency does not reveal useful project-type information, are likely. This means a public subsidy is not automatically a useful private-finance signal.

Kleer then adds quality information. In this second setup, subsidies can carry both project-type and quality information. This changes the result: if the subsidy is accompanied by credible quality information, it can lead to increased or better-selected private investment. The model therefore clarifies that "certification" is not automatic. A subsidy becomes useful as a signal only when the selection process credibly communicates information that private investors care about, not merely that a project is eligible for public support.

The paper also discusses partial crowding out and additional private funds for subsidized R&D projects. The main results remain: crowding out does not overturn the core logic, and the likelihood of subsidy equilibria increases if subsidies induce substantial additional private funding. But the central conclusion stays conditional on the information content of the subsidy decision.

## Research question

Can government R&D subsidies serve as credible signals to private investors, and under what informational conditions do they increase or improve private investment in R&D projects?

## Core argument or contribution

The paper contributes a theoretical qualification to the certification argument. Subsidies do not automatically certify attractive private investments. They can help private investors when public screening reveals credible quality information, but a subsidy that only signals project type may be weak or even unhelpful for banks.

## Methodology

Kleer uses a formal signaling model with perfect Bayesian equilibria. The model compares cases without and with quality information, and then discusses how partial crowding out or additional private funds for subsidized projects affect the equilibria.

## Datasets/materials used

No empirical dataset is used. The paper is theoretical and draws on prior empirical and theoretical literature, including work on SBIR, R&D subsidies, entrepreneurial finance, asymmetric information, and crowding out.

## Key findings

- Public R&D subsidies can have an informational role beyond direct funding.
- If a subsidy only distinguishes basic from applied research, it may not help banks identify privately attractive projects.
- A subsidy accompanied by quality information can increase or improve selection of private investment.
- The certification mechanism depends on credible project-quality screening.
- The model clarifies why public-agency and private-investor objectives may diverge: agencies may prefer high-social-return basic research, while banks prefer high-private-return applied research.
- Partial crowding out and additional private funding change some equilibrium conditions but do not remove the main signaling logic.

## Limitations

- The paper is a stylized theoretical model and does not estimate effects on firms, patents, revenue, or private finance.
- The model abstracts from many institutional details of real subsidy programs.
- It assumes simplified project categories and information structures.
- It should not be cited as empirical proof that subsidized firms attract more external finance.

## Important concepts discussed

- [[30_concepts/rd-subsidy-additionality.md]] - relevant because the paper distinguishes direct funding effects, crowding out, and informational signaling effects.
- [[30_concepts/equity-gap-sme-financing.md]] - relevant because the mechanism operates through asymmetric information and private-finance constraints.
- Asymmetric information.
- Certification and signaling.
- Basic versus applied research.

## Methods discussed

- Formal signaling model.
- Perfect Bayesian equilibrium analysis.

## Datasets discussed

- No empirical dataset.

## Relation to other papers in the vault

Kleer should be read as the theoretical counterpart to empirical grant-finance studies such as [[20_summaries/howell2017-financing-innovation.md]] and [[20_summaries/audretsch2002-sbir-evaluation.md]]. It also relates to [[20_summaries/beck2016-radical-or-incremental.md]] and [[20_summaries/cherif2022-rd-subsidies-imf.md]] because it clarifies a mechanism that is distinct from input additionality: public funding can affect investor beliefs if the public selection process carries credible quality information.

## Implications for LLM research or the project domain

For [[70_projects/bundesinnovationshaushalt-trl.md]], Kleer supports a careful coding distinction between grant amount, project type, and certification quality. A project database should not assume every subsidy sends a useful signal. The relevant retrieval question is whether the funding program has credible selection, review, or quality-screening features that outside investors could observe.

## Links to canonical concept, method, dataset, synthesis, and project notes

- [[30_concepts/rd-subsidy-additionality.md]]
- [[30_concepts/equity-gap-sme-financing.md]]
- [[90_synthesis/innovation-policy-governance-and-evaluation.md]]
- [[70_projects/bundesinnovationshaushalt-trl.md]]
