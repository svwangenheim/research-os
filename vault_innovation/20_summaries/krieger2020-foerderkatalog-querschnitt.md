---
title: "Identifizierung von Querschnittsthemen in Projekten der Direkten Projektfoerderung des BMBF"
note_type: source_summary
summary: "ZEW feasibility study showing how rule-based semantic text analysis can identify cross-cutting themes in BMBF direct-project-funding descriptions, while also showing the limits of LPS categories and of a tested neural-network classifier on short standardized project abstracts."
authors:
  - Bastian Krieger
  - Christian Rammer
  - Patrick Breithaupt
year: 2020
source_files:
  - "10_sources/krieger2020-foerderkatalog-querschnitt.md"
source_urls:
  - "https://hdl.handle.net/10419/222373"
projects:
  - "bundesinnovationshaushalt-trl"
tags:
  - source-summary
  - foerderkatalog
  - bmbf
  - text-classification
  - semantic-analysis
  - digitalization
  - artificial-intelligence
  - social-innovation
  - lps
  - profi
status: verified
updated: "2026-05-04"
---

# Identifizierung von Querschnittsthemen in Projekten der Direkten Projektfoerderung des BMBF

## Source paper link/path

- Source file: `10_sources/krieger2020-foerderkatalog-querschnitt.md`
- Source status: available as converted Markdown in `10_sources/`
- Verification status: semantically checked against the converted source on 2026-05-04.

## Bibliographic metadata

- Title: "Identifizierung von Querschnittsthemen in Projekten der Direkten Projektfoerderung des BMBF: Bericht zur Machbarkeitsstudie"
- Authors: Bastian Krieger, Christian Rammer, Patrick Breithaupt
- Year: 2020
- Publication type: ZEW-Gutachten / research report
- Institution: ZEW - Leibniz Centre for European Economic Research, Mannheim
- URL: `https://hdl.handle.net/10419/222373`

## Detailed summary

Krieger, Rammer, and Breithaupt examine whether cross-cutting themes in BMBF direct project funding can be identified from project descriptions with sufficient accuracy. The problem is that official funding classifications, especially the German Leistungsplansystematik (LPS), assign each project to a primary research or technology field. That structure is useful for administrative reporting, but it is weak for themes that cut across fields, such as digitalization, artificial intelligence, or social innovation.

The study tests a rule-based semantic text-analysis workflow on 70,460 BMBF-funded R&D projects approved from 2005 to 2018. The source texts are project short descriptions of up to 3,000 words, supplemented with PROFI/BMBF administrative fields such as LPS category, approved funding, project duration, and funding period. The authors use ZEW's TexAn software to classify projects by keywords, word stems, word combinations, and proximity rules. Initial rule sets are iteratively refined through manual review of false positives and false negatives.

For digitalization, the study finds that a single unambiguous classification is not practical because the theme is broad and many projects sit near the boundary. The authors therefore report both a restrictive and a broader definition. Under the restrictive definition, nearly 18,000 projects and about EUR 8.7 billion in approved funding are assigned to digitalization, equal to roughly 1,300 projects and EUR 620 million per year. Under the broader definition, about 23,400 projects and EUR 11.3 billion are assigned, equal to roughly 1,700 projects and EUR 810 million per year. The digitalization share rises from 18 percent of BMBF projects in 2005 to 28 percent in 2018 under the restrictive definition, and from 25 percent to 38 percent under the broader definition.

The comparison with the LPS category for information and communication technologies is central. Using only that category would capture fewer than 600 projects and about EUR 250 million per year. The semantic analysis therefore implies more than twice as much digitalization-related activity even under the narrow definition. The study shows that digitalization projects appear across many LPS fields, including work and services, civil security research, production technologies, and innovation-related frameworks and cross-cutting activities.

The artificial-intelligence subanalysis identifies more than 3,000 AI-related projects from 2005 to 2018 with about EUR 1.4 billion in approved funding. Annual AI funding rises from about EUR 20-30 million in 2005-2007 to around EUR 300 million in 2018, and the AI share of BMBF projects rises from about 1 percent in 2007 to almost 10 percent in 2018. AI projects are spread across nearly all funding areas, with especially large counts in innovation-related frameworks and cross-cutting activities, ICT, production technologies, health research and the health economy, and work/services.

For social innovation, the semantic analysis identifies a much smaller corpus: 127 projects and EUR 101 million in approved funding during 2005-2018. The trend is upward, but the absolute number is low. Projects are concentrated in innovation-related frameworks and cross-cutting activities, climate/environment/sustainability, work and services, and humanities/economics/social-science areas.

The report also tests a machine-learning approach for AI classification. A neural network is trained on labels generated by the TexAn semantic classification and evaluated on a held-out subset. The result is not strong enough for the task: recall for TexAn-identified AI projects is 68 percent, precision is 78 percent, and the high overall accuracy of 98 percent is partly explained by the fact that only about 4 percent of the projects are AI projects. The authors conclude that the tested machine-learning setup is not suitable for reliable cross-cutting-theme assignment from short BMBF project descriptions. They attribute the weakness to the small positive class, the short and standardized nature of abstracts, and limited test observations.

## Research question

Can cross-cutting themes in BMBF direct project funding be identified from project descriptions with sufficient accuracy, and does text-based semantic analysis improve on administrative LPS categories for themes such as digitalization, artificial intelligence, and social innovation?

## Core argument or contribution

The contribution is a feasibility assessment for text-based classification of public R&D project portfolios. It shows that rule-based semantic analysis can reveal cross-cutting funding activity that is hidden by one-dimensional administrative taxonomies, but it also shows that such classification requires careful manual validation and that a simple neural-network approach trained on generated labels was not reliable enough in this setting.

## Methodology

- Corpus construction: 70,460 BMBF-funded R&D projects approved from 2005 to 2018.
- Text input: project short descriptions/extended abstracts with up to 3,000 words.
- Administrative variables: LPS category, approval amounts, funding periods, and project durations from PROFI/BMBF-related data.
- Rule-based semantic analysis: ZEW's TexAn software searches for words, word stems, word combinations, proximity relations, and exclusion terms.
- Validation and refinement: manual checks of classification results, especially false positives and false negatives, are used to adjust the semantic rules.
- Theme definitions: digitalization is reported with restrictive and broader definitions because a single clean boundary is not feasible; AI is treated as a subfield; social innovation is separately classified.
- Machine-learning test: a neural network is trained on TexAn-generated AI labels and evaluated with precision, recall, and accuracy.

## Datasets/materials used

- BMBF direct project funding records for 70,460 projects approved during 2005-2018.
- Project descriptions/abstracts submitted by funding recipients.
- PROFI/BMBF administrative fields, including LPS categories, approval amounts, funding periods, and project durations.
- TexAn semantic rule sets for digitalization, artificial intelligence, and social innovation.
- For this vault, the relevant canonical dataset note is [[50_datasets/foerderkatalog-des-bundes.md]], with the caveat that the study uses BMBF/PROFI project data rather than only a public Foerderkatalog export.

## Key findings

- LPS categories undercount cross-cutting themes because each project is assigned to a primary field and cross-field themes are not directly represented.
- Digitalization cannot be assigned with one unambiguous boundary; the authors therefore use restrictive and broad definitions.
- Restrictive digitalization classification: nearly 18,000 projects, about EUR 8.7 billion in approved funding, roughly 1,300 projects and EUR 620 million per year.
- Broad digitalization classification: about 23,400 projects, EUR 11.3 billion, roughly 1,700 projects and EUR 810 million per year.
- Digitalization shares rise between 2005 and 2018: from 18 percent to 28 percent under the restrictive definition and from 25 percent to 38 percent under the broader definition.
- The ICT LPS category captures fewer than 600 projects and about EUR 250 million per year, less than half the narrow semantic estimate for digitalization.
- Digitalization projects appear across many LPS areas, including work/services, civil security, production technologies, and innovation-related frameworks/cross-cutting activities.
- AI classification identifies more than 3,000 projects and EUR 1.4 billion in approved funding for 2005-2018, with annual approved AI funding rising to roughly EUR 300 million by 2018.
- Social innovation classification identifies 127 projects and EUR 101 million in approved funding, with an upward trend but much lower counts than digitalization or AI.
- The tested neural-network approach for AI classification performs too weakly for reliable operational use: 78 percent precision, 68 percent recall, and 98 percent accuracy in a heavily imbalanced corpus.
- The authors conclude that short, standardized project abstracts and limited positive training observations make the tested machine-learning approach unsuitable for identifying BMBF cross-cutting themes at the required quality.

## Limitations

- The study is a feasibility study, not a causal evaluation of BMBF funding impacts.
- The semantic classifications depend on manually designed and iteratively refined rules; results are sensitive to theme boundaries and keyword/proximity choices.
- Digitalization is especially difficult to classify because the concept is broad and has many borderline cases.
- The manual validation burden is substantial; the source reports about 150 hours of work for the complex digitalization classification.
- The machine-learning test uses TexAn-generated labels, so it evaluates against a rule-based benchmark rather than independent expert truth.
- High accuracy for the neural network is misleading because the AI class is rare; precision and recall are more informative.
- The evidence covers BMBF direct project funding from 2005-2018, not all German innovation policy instruments and not later Foerderkatalog extracts.
- The study does not assign TRLs and should not be cited as a TRL measurement source.

## Important concepts discussed

- [[30_concepts/text-as-data-computational-social-science.md]] - the study is an applied text-as-data classification exercise for public R&D project descriptions.
- [[30_concepts/llm-annotation-and-automated-coding.md]] - relevant as a later canonical concept for automated coding, although this source uses rule-based semantic analysis and a neural network, not LLM annotation.
- Cross-cutting themes in public R&D funding.
- Leistungsplansystematik/LPS as an administrative taxonomy.
- Digitalization, artificial intelligence, and social innovation as funding themes.

## Methods discussed

- Rule-based semantic text analysis with TexAn.
- Keyword, word-stem, word-combination, proximity, and exclusion-rule classification.
- Manual false-positive and false-negative review.
- Binary theme assignment for project descriptions.
- Neural-network text classification for AI project assignment.
- Precision, recall, and accuracy as classification metrics.
- [[40_methods/trl-klassifikation-pipeline.md]] is relevant only as a downstream project method that can learn from this study's validation design; the source itself does not classify TRLs.

## Datasets discussed

- [[50_datasets/foerderkatalog-des-bundes.md]] - relevant canonical dataset context for German public project-funding records.
- PROFI/BMBF direct project funding data for 2005-2018.
- Project short descriptions/extended abstracts.
- LPS categories and approved funding amounts.

## Relation to other papers in the vault

- Methodologically related to [[20_summaries/grimmer2013-text-as-data.md]], which provides broader guidance on text-as-data methods and validation.
- Provides a German public-funding classification predecessor for [[20_summaries/egami2024-llm-annotation-framework.md]], [[20_summaries/gilardi2023-chatgpt-annotation.md]], [[20_summaries/pangakis2023-llm-annotation-validation.md]], and [[20_summaries/halterman2025-codebook-llms.md]], which discuss later LLM or supervised annotation workflows.
- Relevant to [[20_summaries/ec-trl-horizon2020.md]] and [[20_summaries/bmle-merkblatt-technologiereifegrade.md]] only at the project-design level: those sources define TRL concepts, while Krieger et al. show how a German project corpus can be classified from descriptions.
- Complements [[20_summaries/cherif2022-rd-subsidies-imf.md]], [[20_summaries/czarnitzki2004-rd-subsidies-zew.md]], and [[20_summaries/czarnitzki2014-funding-source.md]] by focusing on portfolio classification rather than treatment effects or firm-level additionality.

## Implications for LLM research or the project domain

For the Bundesinnovationshaushalt/TRL project, this report is a direct methodological predecessor because it works with BMBF project descriptions and asks whether cross-cutting analytical categories can be inferred from project text. It supports the premise that administrative labels alone are insufficient for portfolio analysis and that text fields contain additional policy-relevant information.

The source also gives concrete design warnings. First, classification categories need explicit scope boundaries because broad concepts such as digitalization produce many borderline cases. Second, evaluation should emphasize false positives and false negatives, not just aggregate accuracy. Third, short and standardized abstracts are a real constraint. Fourth, LPS categories should be treated as context features or stratification variables rather than as substitutes for text-based classification.

The report does not establish that transformer or LLM methods will solve the problem. That is a project-level hypothesis to test against the Foerderkatalog corpus. The source-grounded lesson is narrower: any TRL or theme-classification pipeline for German project funding needs clear definitions, source-text checks, class-specific precision/recall reporting, and manual review of ambiguous cases.

## Links to canonical concept, method, dataset, synthesis, and project notes

- [[30_concepts/text-as-data-computational-social-science.md]]
- [[30_concepts/llm-annotation-and-automated-coding.md]]
- [[40_methods/trl-klassifikation-pipeline.md]]
- [[50_datasets/foerderkatalog-des-bundes.md]]
- [[70_projects/bundesinnovationshaushalt-trl.md]]
- [[90_synthesis/llm-text-classification-and-annotation.md]]
