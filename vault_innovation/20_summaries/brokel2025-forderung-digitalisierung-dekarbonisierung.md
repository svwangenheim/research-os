---
title: "Die Förderung der Digitalisierung und Dekarbonisierung in Deutschland: Eine Analyse des Förderkatalogs"
note_type: summary
authors:
  - Brökel, Tom
year: 2025
doi:
journal: "EFI Studie zum deutschen Innovationssystem Nr. 6-2025"
volume:
issue:
pages:
institution: "University of Stavanger / Expertenkommission Forschung und Innovation (EFI)"
proximity: 1
source_files:
  - "[[10_sources/brokel_2025_forderung_digitalisierung_dekarbonisierung.md]]"
source_urls:
  - "https://www.e-fi.de/studien-und-gutachten/"
projects:
  - "[[70_projects/bundesinnovationshaushalt-trl.md]]"
related_concepts:
  - "[[30_concepts/mission-oriented-innovation-policy.md]]"
  - "[[30_concepts/green-innovation-and-transition-policy.md]]"
  - "[[30_concepts/data-access-for-innovation-policy.md]]"
  - "[[30_concepts/technology-readiness-levels.md]]"
related_methods:
  - "[[40_methods/trl-klassifikation-pipeline.md]]"
related_datasets:
  - "[[50_datasets/foerderkatalog-des-bundes.md]]"
related_synthesis:
  - "[[90_synthesis/germany-innovation-policy-evidence-map.md]]"
tags:
  - summary
  - foerderkatalog
  - digitalisierung
  - dekarbonisierung
  - innovation-policy
  - germany
updated: "2026-05-05"
---

# Die Förderung der Digitalisierung und Dekarbonisierung in Deutschland

## Source paper link/path

- Source files: `vault/10_sources/brokel_2025_forderung_digitalisierung_dekarbonisierung.md`
- Source URLs: https://www.e-fi.de (EFI Studien)
- Source status: Converted from PDF via markitdown; complete

## Bibliographic metadata

- Authors: Tom Brökel (University of Stavanger, School of Business and Law)
- Year: 2025 (February)
- Venue/institution: EFI (Expertenkommission Forschung und Innovation), Studie zum deutschen Innovationssystem Nr. 6-2025; ISSN 1613-4338
- DOI/URL: https://www.e-fi.de/studien-und-gutachten/

## Detailed summary

This EFI-commissioned study by Tom Brökel analyzes German federal funding for digitalization and decarbonization projects using the Förderkatalog (through September 2024; 141,496 projects starting after 1999 out of 206,710 total). The study's main methodological contribution is a combined filter approach that overcomes the limitations of the Leistungsplansystematik (LPS) classification system alone.

Two filter methods are developed: (1) a regex-based text filter applied to project titles and descriptions, and (2) an LPS-based filter using the 1,749 fine-grained LPS categories. The two approaches are shown to be **complementary, not substitutable**: only 37% of LPS-identified digitalization projects are also captured by the regex filter, and vice versa. Wide-definition and narrow-definition variants are constructed for each theme.

**Temporal analysis** shows that digitalization funding (project count) grew continuously from 2012. Decarbonization funding grew similarly but shows a pronounced acceleration from 2020 in funding amounts. The private sector's share of digitalization funding declined from 2012 onwards, while its role in decarbonization grew markedly.

**Sectoral distribution**: Digitalization concentrates in IT services (WZ 620), computing hardware (WZ 260), and publishing/software (WZ 580). Decarbonization concentrates in mechanical engineering (WZ 280), chemicals (WZ 200), and electrical equipment (WZ 270).

**Regional distribution**: Digitalization projects are predominantly in urban, industrially dense regions (overproportional funding per project). Decarbonization projects appear more in rural areas. Urbanization level predicts digitalization funding but not decarbonization funding.

**Cooperation**: Digitalization projects have high cooperation rates (cooperative projects are the norm). Decarbonization cooperation rates are below the catalog-wide average and have declined in recent years.

**Network analysis**: A stable core of economically strong regions (primarily urban agglomerations) occupies central positions in both digitalization and decarbonization inter-regional knowledge-transfer networks. These hub regions show temporal stability over time.

## Research question

How is German federal project funding distributed across digitalization and decarbonization projects — temporally, sectorally, spatially, and in terms of cooperation? Which filtering approach best captures cross-cutting themes in the Förderkatalog?

## Core argument or contribution

The LPS classification system alone systematically undercounts cross-cutting themes. A combined regex + LPS approach is necessary for reliable identification. Results show digitalization and decarbonization display structurally different patterns in sectoral focus, spatial distribution, and cooperation behavior.

## Methodology

- Descriptive analysis of the Förderkatalog (2000–2024)
- Combined filter approach: regex text matching on project titles/descriptions + LPS category classification
- Wide (recall-maximizing) and narrow (precision-maximizing) filter variants
- Temporal analysis, sectoral analysis (WZ classification), spatial analysis (NUTS regions), urbanization regression, cooperation rate analysis, network centrality analysis (degree and betweenness centrality)

## Datasets/materials used

- Förderkatalog des Bundes (BMBF/BMWK, public; 141,496 projects, 2000–September 2024 extract)

## Key findings

1. LPS and regex filters are complementary — overlap only 12–37% across variants; both are needed.
2. Digitalization funding grew continuously since 2012; private sector's role declined post-2012.
3. Decarbonization funding surged from 2020; private sector role increasing.
4. Sectoral concentration differs structurally: IT/software for digitalization; manufacturing sectors for decarbonization.
5. Urban bias in digitalization funding; decarbonization spatially more dispersed.
6. Cooperation is more central to digitalization than decarbonization; decarbonization cooperation declining.
7. A stable set of large, economically strong regions dominates inter-regional knowledge networks in both themes.

## Limitations

- No distinction between research-oriented and non-research-oriented projects (explicitly flagged as limitation).
- BMWK projects have lower coverage in Förderkatalog than BMBF projects — systematic representation bias.
- Filter development is iterative and partially manual; some classification errors remain.
- No causal analysis — purely descriptive.
- Wide vs. narrow filter definitions create a precision-recall tradeoff with no ground-truth resolution.

## Important concepts discussed

- Leistungsplansystematik (LPS) as a cross-cutting-theme classification system — and its limitations
- Digitalization and decarbonization as policy mission areas
- Regional knowledge networks in German innovation funding

## Methods discussed

- Regex-based text classification for cross-cutting topic identification
- LPS-based thematic classification
- Combined (multi-filter) project classification
- Network centrality analysis (degree + betweenness) for inter-regional cooperation
- Scaling regression for urbanization analysis

## Datasets discussed

- Förderkatalog des Bundes — same primary dataset as the TRL project

## Relation to other papers in the vault

- **[[20_summaries/krieger2020-foerderkatalog-querschnitt.md]]**: Direct methodological predecessor. Krieger et al. develop text-based (TexAn rule-based) classification of digitalization in the Förderkatalog and document the LPS undercounting problem. Brökel 2025 extends this approach to decarbonization and develops a combined filter.
- **[[20_summaries/bmbf2024-bundesbericht-datenband.md]]**: Provides the macro context for the funding amounts Brökel analyzes.
- **[[20_summaries/efi2023-gutachten.md]]** and **[[20_summaries/efi2024-gutachten.md]]**: Published by the same institution (EFI); the Gutachten use EFI-commissioned studies as evidence input.

## Implications for the project domain

**High direct relevance** for the Bundesinnovationshaushalt TRL project:

1. **Validated methodology**: Brökel 2025 validates the combined regex + LPS approach for thematic classification of the Förderkatalog — directly applicable to TRL classification design. The finding that LPS alone systematically undercounts cross-cutting themes supports text-based NLP over LPS-only classification.

2. **Sector-mission connection**: Digitalization and decarbonization have structurally different sectoral concentrations — consistent with the hypothesis that different policy missions support different TRL stages and different recipient types.

3. **Institutional patterns**: Private sector declining in digitalization but rising in decarbonization — mirrors incumbent vs. entrant dynamics the TRL project investigates.

4. **Data quality confirmation**: Confirms the LPS Schwerpunktprinzip limitation. Directly corroborates [[50_datasets/foerderkatalog-des-bundes.md]] documentation on classification bias.

## Links to canonical concept, method, dataset, synthesis, and project notes

- Concepts: [[30_concepts/mission-oriented-innovation-policy.md]], [[30_concepts/green-innovation-and-transition-policy.md]], [[30_concepts/data-access-for-innovation-policy.md]], [[30_concepts/technology-readiness-levels.md]]
- Methods: [[40_methods/trl-klassifikation-pipeline.md]]
- Datasets: [[50_datasets/foerderkatalog-des-bundes.md]]
- Projects: [[70_projects/bundesinnovationshaushalt-trl.md]]
- Synthesis: [[90_synthesis/germany-innovation-policy-evidence-map.md]]
