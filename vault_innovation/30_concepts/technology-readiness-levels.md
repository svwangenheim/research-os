---
title: "Technology Readiness Levels (TRL)"
note_type: concept
summary: "A 9-level scale used to assess the maturity of a technology, from basic research to proven operational deployment."
related_notes:
  - "20_summaries/bmle-merkblatt-technologiereifegrade.md"
  - "20_summaries/ec-trl-horizon2020.md"
  - "20_summaries/trucco2025-scaling-up-ideas.md"
projects: []
tags:
  - concept
  - TRL
  - innovation-policy
  - technology-assessment
updated: "2026-04-14"
---

# Technology Readiness Levels (TRL)

## Definition

A standardized 9-level scale for assessing the maturity of a technology or innovation. Originally developed by NASA; now the dominant framework in European and German public research funding. TRL 1 marks the observation of basic principles; TRL 9 marks a fully proven system in operational deployment.

## Mechanism

TRL levels serve as a common vocabulary for:
- **Funders** to specify what stage of development they will support
- **Applicants** to self-classify their project
- **Evaluators** to assess whether a project has reached the claimed maturity
- **Policy analysts** to track the distribution of public funding across the research-to-market pipeline

The scale is not a linear development path but a classification scheme. A project does not need to begin at TRL 1 — it enters the scale wherever its current maturity sits.

## Level definitions: EU (Horizon 2020) vs. German (BMLE)

| TRL | Horizon 2020 (EU, English)                      | BMLE (German)                         | German deliverable            |
| --- | ----------------------------------------------- | ------------------------------------- | ----------------------------- |
| 1   | Basic principles observed                       | Beobachtung des Funktionsprinzips     | Grundprinzip beobachtet       |
| 2   | Technology concept formulated                   | Beschreibung von Anwendungsszenarien  | Technologiekonzept formuliert |
| 3   | Experimental proof of concept                   | Nachweis der Funktionsfähigkeit       | Proof of Concept              |
| 4   | Technology validated in lab                     | Versuchsaufbau im Labor               | Labormuster                   |
| 5   | Technology validated in relevant environment    | Versuchsaufbau in relevanter Umgebung | Funktionsmuster               |
| 6   | Technology demonstrated in relevant environment | Demonstration in relevanter Umgebung  | Prototyp                      |
| 7   | System prototype in operational environment     | Demonstration im realen Einsatz       | Demonstrator                  |
| 8   | System complete and qualified                   | Nachweis der Funktionstüchtigkeit     | Nullserie                     |
| 9   | Actual system proven in operational environment | Nachweis des erfolgreichen Einsatzes  | System operational            |

## Key distinctions between frameworks

- **TRL 2 wording differs**: The EU says "technology concept formulated"; the BMLE focuses on "description of application scenarios" — slightly earlier/narrower emphasis.
- **Key Enabling Technologies (KETs)**: The Horizon 2020 definitions add explicit qualifiers at TRL 5, 6, and 9 for KETs (industrially relevant environment; competitive manufacturing). The BMLE document does not include this qualifier.
- **Deliverables**: The BMLE document uniquely specifies a concrete *artifact* expected at each level (Labormuster, Funktionsmuster, Prototyp, Demonstrator, Nullserie). The EU definitions do not specify deliverables.
- **Phase mapping**: The BMLE maps TRL levels to German funding phase categories (Grundlagenforschung, Industrielle Forschung, Experimentelle Entwicklung, Markt). The Horizon 2020 document has no such mapping.

## How it is measured

Self-reported by applicants, verified by evaluators. No standardized measurement instrument. Common sources of variation: disagreement on what counts as a "relevant environment" at TRL 5–6, and whether internal testing counts as "validated."

In Horizon Europe specifically (see [[40_methods/trl-project-level-reporting.md]]):
- Beneficiaries report TRL at three points: project start, midpoint (Periodic Report), and end (expected or achieved)
- No mandatory verification by Project Officers; no domain-specific guidance exists beyond the standard 9-line table
- 89% of Project Officers acknowledge risk of over- or underreporting
- Only 16.3% of all Horizon Europe projects report any TRL data
- Multi-work-package projects must collapse multiple TRL levels into a single figure — a known source of distortion

## TRL distribution in practice (Horizon Europe, 2021–2025)

From Trucco et al. (2025), based on 2,462 projects:
- 68% of all EU funding concentrates at **TRL5–TRL7** at project end
- TRL8–TRL9 accounts for only 16% of funding — evidence of the "valley of death" at the market-entry stage
- Most projects advance **2–3 TRL steps** per grant (36–48 months)
- Typical trajectories: TRL3→TRL5, TRL2→TRL4, TRL6→TRL9
- Universities (HES) dominate funding at TRL1–TRL2 (~60%); companies (PRC) dominate at TRL8+ (~67%)
- SMEs represent ~80% of companies across the entire TRL range

## Related concepts

- Innovation funding policy
- Research-to-market pipeline
- Key Enabling Technologies (KETs)
- Grundlagenforschung / Industrielle Forschung / Experimentelle Entwicklung (German funding categories)

## Open debates

- Whether TRL is appropriate for software, AI, or social innovation (scale was designed for hardware/aerospace)
- Whether self-reported TRL assessments are reliable — Trucco et al. (2025) provide systematic evidence they are not fully reliable; POs flag risk of misreporting and lack verification tools
- Whether funders should concentrate on specific TRL ranges or fund across the full spectrum — Draghi (2024) and EC Competitiveness Compass both argue EU underinvests at high TRLs (scaling gap); Horizon Europe data confirms low-to-mid-TRL concentration
- Whether a single TRL can represent a multi-workstream collaborative project — likely not; single-TRL reporting collapses internal variation

## Relevance for my research

Central classification framework in German and EU innovation policy. Understanding TRL definitions and their differences between funders (BMLE vs. EU) is essential for analyzing project portfolios, funding distributions, or policy evaluations in the German research system.

## Sources

- [[20_summaries/bmle-merkblatt-technologiereifegrade.md]] — German federal definitions with deliverables and phase mapping
- [[20_summaries/ec-trl-horizon2020.md]] — EU Horizon 2020 canonical definitions, including KET qualifiers
- [[20_summaries/trucco2025-scaling-up-ideas.md]] — Empirical analysis of TRL distribution and progression across 2,462 Horizon Europe projects; methodology and limitations of project-level TRL reporting

## Comparative Framework Overview (added 2026-04-15)

### Convergent grouping across frameworks

Despite originating independently, the major TRL frameworks converge on the same three-phase structure:

| Phase                      | TRL range | Frameworks                           |
| -------------------------- | --------- | ------------------------------------ |
| Basic research / concept   | TRL 1–3   | NASA, DoD (2025), ESA, EARTO, UKRI   |
| Development / validation   | TRL 4–6   | NASA, DoD (2025), EU State Aid, UKRI |
| Demonstration / deployment | TRL 7–9   | NASA, DoD (2025), ESA, UKRI          |

The TRL 3|4 boundary (concept proof → applied development) and TRL 6|7 boundary (lab validation → operational demo) are the most institutionally validated cut-points.

### EU EIC exception

The European Innovation Council (EIC) uses TRL 4|5 and TRL 8|9 as programme boundaries (Pathfinder / Transition / Accelerator), not 3|4 and 6|7. This creates ambiguity when using CORDIS Horizon Europe data — projects selected under EIC Accelerator (TRL 5–8) do not align with the NASA/DoD 3-phase cut-points.

### OECD Frascati alignment

The OECD Frascati Manual three categories (basic research / applied research / experimental development) map approximately to TRL 1–3 / TRL 4–6 / TRL 7–8, with TRL 9 treated as commercialisation outside the R&D boundary. The EARTO (2014) policy paper makes this mapping explicit in the EU State Aid context.

### Empirical distribution anchor

Trucco et al. (2025) report 68% of Horizon Europe projects at TRL 5–7, 16% at TRL 8–9, 16% at TRL 1–4 (internal EC CORDA data). The TRL 5–6 peak is a structural feature of EU programme design, not a data artifact.

### Recommended grouping for classifiers

For a 3-class text classifier on short project abstracts, the most literature-grounded scheme is:
- Class A: TRL 1–3 (basic research; NASA/DoD "basic research" phase)
- Class B: TRL 4–6 (development; corresponds to EU State Aid "industrial research")
- Class C: TRL 7–9 (demonstration/deployment; corresponds to "experimental development" + market)

Alternative (EIC-aligned): TRL 1–4 / TRL 5–6 / TRL 7–9 — better class balance when training data peaks at TRL 5–6.

## Scope boundaries

TRL is a maturity scale, not a value, novelty, or impact scale. It says whether
a technology has moved from principles and proof of concept toward validation,
demonstration, qualification, and operational use. It does not by itself show
whether an innovation is radical, socially valuable, commercially viable, or
additional.

## German federal ministerial mandate split (added 2026-05-11)

The TRL research briefing (`explorations/trl_research_briefing.md`, Section 1.3) documents the German federal mandate that maps ministries to TRL ranges:

| Ministry                    | Mandate scope                                         | TRL range |
| --------------------------- | ----------------------------------------------------- | --------- |
| BMBF                        | Anwendungsorientierte Grundlagenforschung             | TRL 1–4   |
| BMWK                        | Industrielle Forschung und experimentelle Entwicklung | TRL 3–7   |
| BMWK Reallabore / Invest AI | Demonstration / deployment support                    | TRL 7–9   |
| SPRIND                      | Breakthrough / disruptive innovation mandate          | TRL 1–4   |
|                             |                                                       |           |

This structure means the Ressort (ministry code) field in Förderprojekte is a primary TRL classifier signal:
- BMBF Ressort → strong prior for Low TRL (1–3)
- BMWK Ressort + energy-sector label → strong prior for High TRL (7–9)
- BMWK Ressort + general industrial label → Mid TRL (4–6) most likely

The policy question: does the actual TRL distribution of funded projects match the stated mandate? If BMBF-tagged projects concentrate at High TRL, this signals mandate drift. If the overall allocation skews toward High TRL regardless of ministry, this represents a structural mismatch between stated innovation policy and actual funding allocation.

## Valley of death: TRL 5–6 specificity

The EIB Energy Transition Finance Report (2022) — [[20_summaries/eib2022-energy-transition-finance.md]] — provides sector-specific evidence that the valley of death is most acute at **TRL 5–6** specifically (technology validated in relevant environment but not demonstrated at operational scale), not at TRL 4–6 as a whole. The EIB also uses a four-group scheme (Research 1–3 / Development 3–6 / Innovation 6–8 / Production Support 9) that allows distinguishing legitimate first-of-kind demonstrations (TRL 7–8) from serial production subsidies (TRL 9).

## TRL and social returns

⚠️ A previously cited claim — "low-TRL innovations generate 30% higher social returns than high-TRL innovations (Dechezleprêtre et al. 2023)" — was incorrect. Source verification on 2026-05-18 confirmed this finding does not appear in the paper. [[20_summaries/dechezlepretre2023-rd-tax-spillovers.md]] has been corrected accordingly. The general theoretical argument (larger spillovers at earlier TRL stages) remains supported by the market-failure literature, but no verified empirical estimate with this specific quantification is currently in the vault.

## TRL 1-3 and firm absorptive capacity (added 2026-05-14)

The policy case for company-facing TRL 1-3 instruments rests not only on the direct output of that research but on a second-order mechanism: **absorptive capacity**.

**Cohen & Levinthal (1990)** — [[20_summaries/cohen-levinthal1990-absorptive-capacity.md]] — establish that a firm's ability to recognize, assimilate, and exploit external knowledge is primarily built through its own prior R&D, especially basic research (TRL 1-3 equivalent). This is path-dependent: firms that exit basic research progressively lose the cognitive infrastructure needed to exploit public science from universities and public labs, even if university TRL 1-3 output is strong. Re-entry after exit is costly. The implication for the Förderkatalog finding (0% company share at TRL 1-3) is that structural absence does not only mean companies forgo basic research outputs — it means German companies are progressively losing the interface function between public basic research and commercial application.

**Arora, Belenzon & Patacconi (2018)** — [[20_summaries/arora2018-corporate-basic-research.md]] — provide longitudinal empirical evidence consistent with this mechanism: corporate basic research share in the US declined from ~30% to <20% of BERD (1985–2015), publications per firm fell ~20% per decade, and the decline is linked to productivity slowdowns. The mechanism — firms rationally substituting external basic research (from universities and startups) for internal basic research via markets for ideas — is individually rational but collectively damaging because the science-industry interface degrades even when university output grows.

**Policy implication for TRL distribution analysis:** A portfolio architecture that excludes companies from TRL 1-3 is not merely declining to fund one category of research. It is systematically weakening the industry absorptive capacity that makes TRL 4-6 grants effective. This extends the valley of death framing: the valley begins at TRL 2-3, not only at TRL 4, because early-stage company absence damages the translation capacity that all subsequent stages rely on.

## Papers that discuss this concept

Key linked sources are [[20_summaries/bmle-merkblatt-technologiereifegrade.md]],
[[20_summaries/ec-trl-horizon2020.md]], [[20_summaries/trucco2025-scaling-up-ideas.md]],
[[20_summaries/heder2017-trl-history.md]], [[20_summaries/earto2014-trl-policy-tool.md]],
[[20_summaries/eib2022-energy-transition-finance.md]],
[[20_summaries/dechezlepretre2023-rd-tax-spillovers.md]],
[[20_summaries/cohen-levinthal1990-absorptive-capacity.md]],
[[20_summaries/arora2018-corporate-basic-research.md]], and the method notes
[[40_methods/trl-klassifikation-pipeline.md]] and
[[40_methods/trl-project-level-reporting.md]].

## How the papers use the concept

Administrative sources define the TRL scale. Trucco et al. use reported TRL to
study Horizon Europe project maturity. The Bundesinnovationshaushalt project
uses TRL as a classification target inferred from German project text because
the Foerderkatalog does not contain a native TRL field.

## Open questions

- How reliable are self-reported or inferred TRL values?
- How should TRL be adapted for AI, software, social innovation, and data-heavy
  projects?
- Does a single TRL score hide variation across work packages in large projects?

### Key sources

- Mankins (1995, 2009) — original NASA scale and retrospective
- DoD TRA Guidebook (2025) — current US procurement standard
- ESA ECSS-E-HB-11A (2017) — European space standard
- EARTO (2014) — EU State Aid mapping
- Trucco et al. (2025) — empirical Horizon Europe distribution
