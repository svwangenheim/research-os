---
title: "Merkblatt Technologiereifegrade"
note_type: source_summary
authors: ["BMLE"]
year: null
source_files: ["10_sources/bmle_merkblatt_technologiereifegrade.md"]
tags: [source-summary, TRL, German, technology-readiness]
updated: "2026-05-04"
---

# BMLE - Merkblatt Technologiereifegrade

## Source paper link/path

- Source file: `10_sources/bmle_merkblatt_technologiereifegrade.md`
- Source status: available as converted Markdown in `10_sources/`; table extraction is noisy, but the TRL definitions are readable.
- Audit status: checked one-by-one against the mapped source on 2026-05-04.

## Bibliographic metadata

- Title: Merkblatt Technologiereifegrade / Technology Readiness Levels (TRLs)
- Author/institution: BMLE as named in the local vault record
- Year: not visible in the converted source
- Source type: German ministry reference sheet / guidance note

## Detailed summary

This source is a short German reference sheet defining technology readiness levels from TRL 1 to TRL 9. Its value for the vault is definitional: it provides stage language for classifying the maturity of technologies, prototypes, demonstrations, pilots, qualified systems, and operational use. It is not an evaluation of a funding program and does not provide empirical evidence on project success.

The source maps TRLs onto broad research and market phases. The visible table places the lower levels near basic research, middle levels near industrial research and experimental development, and higher levels near market introduction, market entry, and serial production. The OCR/table extraction is messy, so exact table layout should be checked against the PDF before citation, but the level-by-level descriptions are legible.

The TRL scale begins with basic principles and application concepts. TRL 1 is observation of the functional principle and corresponds to scientific basic research. TRL 2 moves from theory and scientific foundations toward application scenarios and the formulation of a technology concept.

TRL 3 marks proof of concept. Research and development begin with initial laboratory investigations, and general feasibility is demonstrated through lab tests. TRL 4 describes independent prototype construction, implementation, integration of technical elements, and laboratory testing, including complex tasks or datasets. The target result is a technology checked in the lab, described as a lab model.

TRL 5 shifts from laboratory testing to a relevant operating environment. The setup is intensively tested in a relevant environment, core technical elements are connected with supporting elements, and prototype implementation corresponds to the target environment and interfaces. TRL 6 is demonstration in a relevant operating environment, using realistic complex problems and partial integration into existing systems; the source treats this as full proof of technical feasibility in the current application area.

TRL 7 is demonstration in real use or an operational setting. The system is nearly at operational scale, most functions for demonstration and testing are present, and documentation is extended. TRL 8 is proof of the functionality of a qualified system: system development in the application area is completed, user/training/maintenance documentation is mostly available, and products largely correspond to future serial production, although they are usually not yet marketed in that form. TRL 9 is successful use of the qualified system in the operational environment with completed documentation and successful operating experience.

For wiki and LLM-assisted coding, this note should be used to anchor distinctions between early principles, application concepts, proof of concept, lab validation, relevant-environment validation, real-environment demonstration, qualified system completion, and operational deployment.

## Research question

The source does not pose a research question. It answers a classification need: how should technology maturity be described across TRL 1-9?

## Core argument or contribution

The contribution is a practical German TRL vocabulary that describes typical activities and target outputs for each readiness level.

## Methodology

The source is a guidance document. It defines categories and examples rather than applying a research method.

## Datasets/materials used

No dataset is used. The source provides a classification scale.

## Key findings

- TRL 1: functional principle observed; scientific basic research.
- TRL 2: application scenarios and implementation criteria formulated; technology concept.
- TRL 3: proof of concept through initial lab investigations and feasibility demonstration.
- TRL 4: prototype construction, implementation, integration, and lab testing; lab model.
- TRL 5: setup tested in a relevant environment; functional model.
- TRL 6: prototype demonstrated in a relevant environment with realistic complex problems; technical feasibility shown.
- TRL 7: demonstrator tested in real use or operational environment.
- TRL 8: qualified system completed; documentation largely available; zero-series or near-serial-production status.
- TRL 9: qualified system functions in the operational environment with completed documentation and successful operating experience.

## Limitations

- The converted Markdown has noisy table/OCR extraction, so exact layout and wording should be checked against the PDF.
- The document is definitional and does not validate any automated TRL classifier.
- The source does not explain how to infer TRL from sparse project abstracts, grant descriptions, or Foerderkatalog fields.
- It does not evaluate outcomes, additionality, firm behavior, or innovation-policy effectiveness.

## Important concepts discussed

- [[30_concepts/technology-readiness-levels.md]]

## Methods discussed

- [[40_methods/trl-project-level-reporting.md]]
- [[40_methods/trl-klassifikation-pipeline.md]]

These method links are project-facing uses of the TRL definitions; they are not methods applied by the source itself.

## Datasets discussed

No dataset is discussed.

## Relation to other papers in the vault

- Complements [[20_summaries/ec-trl-horizon2020.md]] as a German-language TRL classification reference.
- Provides definitional support for project-level methods in [[40_methods/trl-project-level-reporting.md]] and [[40_methods/trl-klassifikation-pipeline.md]].
- Should be kept separate from empirical innovation-policy papers that estimate funding effects or measure innovation outcomes.

## Implications for LLM research or the project domain

For the Bundesinnovationshaushalt/TRL project, this source is a coding standard. It can support prompt design, annotation rubrics, reviewer instructions, and validation checks for classifying project maturity. It cannot by itself prove whether funding is well targeted or whether a project description truly belongs to a specific TRL; that requires project text, coding rules, examples, and human review.

## Links to canonical concept, method, dataset, synthesis, and project notes

- [[30_concepts/technology-readiness-levels.md]]
- [[40_methods/trl-project-level-reporting.md]]
- [[40_methods/trl-klassifikation-pipeline.md]]
- [[90_synthesis/germany-innovation-policy-evidence-map.md]]
- [[70_projects/bundesinnovationshaushalt-trl.md]]

## Semantic verification details

Checked one-by-one against `10_sources/bmle_merkblatt_technologiereifegrade.md` on 2026-05-04. Use this note as a TRL definition and coding reference. Do not cite it for LLM annotation methods, CORDIS, Foerderkatalog data, innovation-policy effects, or subsidy additionality.
