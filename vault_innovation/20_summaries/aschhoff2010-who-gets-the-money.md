---
title: "Who Gets the Money? The Dynamics of R&D Project Subsidies in Germany"
note_type: source_summary
summary: "Aschhoff (2010) analyzes persistence in German direct R&D project funding. Using Mannheim Innovation Panel/CIS firm data merged with the PROFI database for the German federal non-defense Direct Project Funding scheme, the paper shows that participation is highly persistent: few innovating firms enter the scheme, and prior DPF experience increases the probability of receiving new grants. Firm size, R&D capabilities, human capital, other subsidy experience, and the supply of relevant subsidies also matter. The paper is crucial for distinguishing subsidy allocation and selection from subsidy effects."
authors: ["Birgit Aschhoff"]
year: 2010
source_files: ["10_sources/aschhoff2010-who-gets-money.md"]
doi: "10.2139/ssrn.1101174"
journal: "Jahrbuecher fuer Nationaloekonomie und Statistik"
volume: 230
issue: 5
pages: "522-546"
zew_dp: "ZEW Discussion Paper 08-018"
projects: [bundesinnovationshaushalt-trl]
tags:
  - source-summary
  - germany
  - rd-subsidies
  - subsidy-selection
  - state-dependence
  - direct-project-funding
updated: "2026-05-04"
---

# Aschhoff (2010) - Who Gets the Money?

## Source paper link/path

- Source file: `10_sources/aschhoff2010-who-gets-money.md`
- Source status: available as converted Markdown in `10_sources/`
- One-by-one audit status: locally checked against the listed source Markdown on 2026-05-04.

## Bibliographic metadata

- Title: "Who Gets the Money? The Dynamics of R&D Project Subsidies in Germany"
- Author: Birgit Aschhoff
- First ZEW version: March 2008; revised version: May 2009
- Journal year: 2010
- Journal: Jahrbuecher fuer Nationaloekonomie und Statistik, 230(5), 522-546
- DOI: `10.2139/ssrn.1101174`
- ZEW Discussion Paper: `08-018`

## Detailed summary

Aschhoff studies who receives German federal direct R&D project grants and whether the set of funded firms changes dynamically over time or remains stable. The paper focuses on the German Federal Government's non-defense Direct R&D Project Funding (DPF) scheme, which funds business R&D projects through non-repayable grants in selected technology fields. The core empirical question is not whether subsidies increase R&D, but how firms are selected into public funding and how prior participation shapes future participation.

The paper is motivated by an identification problem in subsidy evaluation. If the same firms repeatedly receive grants, or if firms with stronger R&D capabilities are more likely to be selected, then estimates of subsidy effects must account for selection into treatment. Aschhoff therefore distinguishes persistent funding due to long-running projects from persistence due to newly approved projects. This distinction matters because DPF projects last about three years on average; without separating continuing projects from newly approved grants, persistence would be overstated mechanically.

Empirically, the paper combines two data sources. The Mannheim Innovation Panel, Germany's part of the Community Innovation Survey, provides firm-level information for manufacturing and knowledge-intensive services. The PROFI database provides information on DPF grants, including project start and end dates, funding amounts, project costs, and participating firms. The final sample covers roughly 6,800 firms, with manufacturing observed from 1994 to 2005 and knowledge-intensive services from 1996 onward.

The descriptive evidence shows that entry into DPF is rare among innovating firms. More than 98 percent of firms that are not funded in a given year remain unfunded in the following year. Among firms already participating, however, the probability of receiving newly approved projects is higher than the probability of leaving the scheme, so participation is stable. The multivariate analysis confirms that experience in the same funding scheme matters beyond the preceding year's subsidy status. Experience with other subsidy programs also helps firms enter DPF, and the overall supply of relevant subsidies must be controlled because program budgets and technology priorities shift over time.

The paper also finds that larger firms are more successful in receiving new DPF grants. This means the evidence does not confirm that the scheme particularly reaches SMEs, despite SMEs being a policy target. Knowledge capabilities matter as well: R&D activities and human capital increase the probability of obtaining new grants, especially for firms not previously subsidized. For already subsidized firms, human capital matters particularly, while recent firm growth has only a limited effect. Aschhoff interprets this pattern as consistent with program agencies selecting capable or promising firms, sometimes described as a picking-the-winner strategy.

## Research question

Which firms receive new German federal direct R&D project grants, how persistent is participation in the DPF scheme over time, and how much does previous subsidy experience affect the probability of receiving new grants?

## Core argument or contribution

The paper's contribution is to show that German direct R&D project funding has a stable and selective participation structure. Prior DPF participation, other subsidy experience, firm size, R&D capabilities, human capital, and subsidy supply all shape the probability of receiving new grants. This makes subsidy allocation a necessary object of study before evaluating subsidy effects.

## Methodology

- Descriptive analysis of DPF participation histories using the PROFI project-funding database.
- Transition-rate analysis for movement between non-participation, participation, and newly approved grants.
- Firm-level sample from the Mannheim Innovation Panel / German CIS merged with DPF subsidy status.
- Markov-chain framing for subsidy transitions.
- Rare-events logit for transition from not subsidized to subsidized.
- Logit model for transition from already subsidized to newly subsidized.
- Controls for DPF history, ongoing projects, other subsidy experience, subsidy supply by industry/year, firm size, age, employment growth, R&D activity, human capital, patent stock, group status, and East/West location.

## Datasets/materials used

- PROFI database of German federal DPF projects, excluding contract research.
- Mannheim Innovation Panel (MIP), the German part of the Community Innovation Survey.
- Firm-level sample covering manufacturing from 1994-2005 and knowledge-intensive services from 1996 onward.
- Patent stock constructed from European Patent Office applications and scaled relative to industry averages.
- Subsidy-supply measure based on starting DPF project funding by industry and year.

## Key findings

- DPF participation is stable over time, but part of apparent persistence must be separated from multi-year project duration.
- Entry into DPF among innovating firms is rare; more than 98 percent of firms not funded in one year remain unfunded in the following year.
- Prior DPF experience increases the probability of receiving newly approved DPF grants beyond simple subsidy status in the previous year.
- Experience with European or regional subsidy programs can increase the probability of entering the DPF scheme.
- Overall subsidy supply by industry and year is important and should be controlled in allocation models.
- Larger firms are more successful in receiving new DPF grants, so the evidence does not confirm that DPF particularly reaches SMEs.
- R&D activity and human capital increase the likelihood of receiving new grants, especially for firms not previously subsidized.
- The results are consistent with selection of capable or promising firms rather than random allocation of project funding.

## Limitations

- The paper analyzes allocation into DPF, not the causal impact of DPF on firm R&D inputs, innovation outputs, or productivity.
- The data do not reveal all stages of the application process, including awareness of programs, withdrawn applications, informal agency contacts, or rejection rates.
- Project-level information is unavailable for non-subsidized project proposals, so the analysis cannot directly compare funded and rejected project quality.
- The study covers German manufacturing and knowledge-intensive service firms in the 1994-2005 period; later funding structures and programs require separate evidence.
- The paper does not analyze TRL distributions, text descriptions of funded projects, or the current Foerderkatalog classification problem.

## Important concepts discussed

- [[30_concepts/rd-subsidy-additionality.md]]
- [[30_concepts/sme-innovation-participation.md]]
- Subsidy selection
- State dependence in funding participation
- Direct R&D project funding
- Picking-the-winner strategy
- Knowledge capabilities

## Methods discussed

- [[40_methods/causal-evaluation-innovation-policy.md]]
- Transition-rate analysis
- Rare-events logit
- Logit model for subsidy transitions
- Markov-chain framing of program participation

## Datasets discussed

- PROFI database for German direct project funding
- Mannheim Innovation Panel / German Community Innovation Survey
- European Patent Office patent applications

## Relation to other papers in the vault

Aschhoff is a central allocation-side counterpart to subsidy-effect papers such as [[20_summaries/czarnitzki2004-rd-subsidies-zew.md]], [[20_summaries/kleer2010-rd-subsidies-signal.md]], and [[20_summaries/czarnitzki2014-funding-source.md]]. Those papers ask whether public support changes firm behavior or financing conditions; Aschhoff asks which firms receive the support in the first place. It also connects to [[20_summaries/akcigit2024-innovation-paradox.md]] because both warn that the allocation of innovation resources matters, but Aschhoff provides German DPF-specific evidence rather than the U.S. incumbent-allocation mechanism discussed by Akcigit.

## Implications for LLM research or the project domain

For [[70_projects/bundesinnovationshaushalt-trl.md]], the paper is direct evidence that German federal R&D project funding should be analyzed as a selective allocation process. It supports project questions about whether public funding repeatedly reaches established actors and whether recipient characteristics shape funding access. It does not itself answer whether funded projects are low-TRL or high-TRL, so the correct bridge to the project is: combine Aschhoff's allocation logic with text-based project classification to ask what types of projects repeatedly funded firms receive.

## Three-pillar innovation paradox framing (added 2026-05-11)

The TRL research briefing (`explorations/trl_research_briefing.md`, Section 2.2) explicitly positions Aschhoff (2010) as the empirical anchor for the "large firm advantage" that constitutes pillar (a) of Germany's three-pillar innovation paradox:

- **Pillar (a):** Large, established firms receive a disproportionate share of federal R&D grants (Aschhoff 2010 — DPF state dependence and large-firm selection)
- **Pillar (b):** Non-high-tech sectors dominate the recipient structure (documented by OECD 2022, BMBF 2024, Mitteltechnologie-Falle literature)
- **Pillar (c):** Funding is likely concentrated at mid-to-high TRL stages, where the case for public support is weakest (Foerderprojekte TRL classification — pending confirmation)

The briefing's diagnostic matrix (Section 2.3) identifies the combination of Large firm × Non-high-tech sector × High TRL as the cell most clearly representing the innovation paradox — all three structural biases reinforcing each other. Aschhoff provides the first-pillar evidence: successful firms win grants repeatedly, and larger firms are disproportionately successful. This self-selection problem is also documented by [[20_summaries/czarnitzki2018-additionality-firm-size.md]] to correlate with lower additionality for large firms, amplifying the social cost of large-firm concentration.

## Semantic verification details

Checked one-by-one against `10_sources/aschhoff2010-who-gets-money.md` on 2026-05-04. The maintained note is restricted to DPF allocation, subsidy-selection dynamics, and the implications for evaluating subsidy effects. It should not be used as evidence about LLM annotation, TRL classification, CORDIS/Horizon data, or Foerderkatalog text classification.

## Links to canonical concept, method, dataset, synthesis, and project notes

- [[30_concepts/rd-subsidy-additionality.md]]
- [[30_concepts/sme-innovation-participation.md]]
- [[40_methods/causal-evaluation-innovation-policy.md]]
- [[70_projects/bundesinnovationshaushalt-trl.md]]
- [[90_synthesis/innovation-policy-governance-and-evaluation.md]]
- See also: [[20_summaries/czarnitzki2018-additionality-firm-size.md]] — large firms have lower additionality, amplifying the social-return cost of large-firm dominance in grant receipt
