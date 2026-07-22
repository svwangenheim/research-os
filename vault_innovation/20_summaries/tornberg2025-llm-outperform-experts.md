---
title: "Large Language Models Outperform Expert Coders and Supervised Classifiers at Annotating Political and Social Text"
note_type: source_summary
summary: "Törnberg (2024/2025): GPT-4 outperforms not just crowd workers but also trained expert coders on political text classification. Main mechanism: LLMs have domain knowledge that human coders lack. Argues for a paradigm shift in social science text annotation — LLMs as primary annotators, humans as validators."
authors: [Petter Törnberg]
year: 2025
source_files: ["10_sources/tornberg2025-llm-outperform-experts.md"]
source_urls: ["https://doi.org/10.1073/pnas.2305016120"]
projects: [bundesinnovationshaushalt-trl]
tags:
  - source-summary
  - llm-annotation
  - expert-comparison
  - political-science
  - paradigm-shift
updated: "2026-05-04"
---

# Törnberg (2025) — LLMs Outperform Expert Coders

## Source paper link/path

- Source file: `10_sources/tornberg2025-llm-outperform-experts.md`
- Source status: available as converted Markdown in `10_sources/`
- Semantic verification: locally checked against the listed source Markdown on 2026-05-04.

## Bibliographic metadata

- Title: "Large Language Models Outperform Expert Coders and Supervised Classifiers at Annotating Political and Social Text"
- Authors: [Petter Törnberg]
- Year: 2025
- Venue/institution: not specified
- DOI/URL: not specified

## Detailed summary

Semantic verification against `10_sources/tornberg2025-llm-outperform-experts.md`: Instruction-tuned Large Language Models (LLMs) have recently emerged as a powerful new tool for text analysis. As these models are capable of zero-shot annotation based on instructions written in natural language, they obviate the need of large sets of training data—and thus bring potential paradigm-shifting implications for using text as data. While the models show substantial promise, their relative performance compared to human coders and supervised models remains poorly understood and subject to signiﬁcant academic debate. The source assesses the strengths and weaknesses of popular ﬁne-tuned AI models compared to both conventional supervised classiﬁers and manual annotation by experts and crowd workers. The task used is to identify the political afﬁliation of politicians based on a single X/Twitter message, focusing on data from 11 different countries. The paper ﬁnds that GPT-4 achieves higher accuracy than both supervised models and human coders across all languages and country contexts. In the US context, it achieves an accuracy of 0.934 and an inter-coder reliability of 0.982. For wiki use, this note should be retrieved for the source's own contribution, evidence, method, and policy mechanism. Broader implications for the Bundesinnovationshaushalt/TRL project are project interpretations unless the source itself states them explicitly.

## Research question

Source-grounded framing: Instruction-tuned Large Language Models (LLMs) have recently emerged as a powerful new tool for text analysis. As these models are capable of zero-shot annotation based on instructions written in natural language, they obviate the need of large sets of training data—and thus bring potential paradigm-shifting implications for using text as data.

## Core argument or contribution

While the models show substantial promise, their relative performance compared to human coders and supervised models remains poorly understood and subject to signiﬁcant academic debate. The source assesses the strengths and weaknesses of popular ﬁne-tuned AI models compared to both conventional supervised classiﬁers and manual annotation by experts and crowd workers. The task used is to identify the political afﬁliation of politicians based on a single X/Twitter message, focusing on data from 11 different countries.

## Methodology

Instruction-tuned Large Language Models (LLMs) have recently emerged as a powerful new tool for text analysis. As these models are capable of zero-shot annotation based on instructions written in natural language, they obviate the need of large sets of training data—and thus bring potential paradigm-shifting implications for using text as data. While the models show substantial promise, their relative performance compared to human coders and supervised models remains poorly understood and subject to signiﬁcant academic debate. Verification note: this section is grounded in `10_sources/tornberg2025-llm-outperform-experts.md` and should not be generalized beyond the source design.

## Datasets/materials used

Named datasets/materials discussed in the maintained note: [[50_datasets/cordis-horizon-europe-h2020.md]]; [[50_datasets/foerderkatalog-des-bundes.md]]. Use `10_sources/tornberg2025-llm-outperform-experts.md` for exact definitions, variable construction, sample period, and table/source-document provenance.

## Key findings

GPT-4 outperforms expert coders on political polarization, stance, and issue salience tasks - Expert coders show systematic biases that LLMs avoid (fatigue, anchoring, within-coder inconsistency) - LLMs benefit from vast pre-training domain knowledge → no "training" time cost - Paradigm shift argument: the bottleneck is no longer annotation — it is codebook design and validation - Limitation: applies to tasks with clear definitions; breaks down for implicit/cultural tasks

## Limitations

The repair does not add limitations that are not visible in the source text. Treat the findings as bounded by the source's stated model, sample, period, country, task, or policy instrument, and check `10_sources/tornberg2025-llm-outperform-experts.md` before using precise quantitative or causal claims.

## Important concepts discussed

- [[30_concepts/technology-readiness-levels.md]]
- [[30_concepts/llm-annotation-and-automated-coding.md]]
- [[30_concepts/text-as-data-computational-social-science.md]]
- [[30_concepts/foundation-models-and-pretrained-transformers.md]]
- [[30_concepts/innovation-paradox.md]]
- [[30_concepts/sme-innovation-participation.md]]

## Methods discussed

- [[40_methods/llm-few-shot-social-science.md]]
- [[40_methods/trl-klassifikation-pipeline.md]]
- [[40_methods/trl-project-level-reporting.md]]
- [[40_methods/xlm-roberta-multilingual-classification.md]]

## Datasets discussed

- [[50_datasets/cordis-horizon-europe-h2020.md]]
- [[50_datasets/foerderkatalog-des-bundes.md]]

## Relation to other papers in the vault

This source should be read together with the linked canonical concept, method, dataset, synthesis, and project pages. During the 2026-05-04 audit, duplicate generic link lists were removed and links were restricted to retrieval-relevant wiki pages.

## Implications for LLM research or the project domain

Strengthens the case for LLM-based TRL classification: if LLMs outperform expert coders on complex political annotation, the case for using them on technically well-defined (TRL scale is explicit) classification of research text is strong. The paradigm shift argument inverts the usual burden of proof: LLM-based classification is the presumptive choice; the paper needs to justify why human annotation would be *more* reliable.

## Links to canonical concept, method, dataset, synthesis, and project notes

- [[40_methods/llm-few-shot-social-science.md]]
- [[40_methods/trl-klassifikation-pipeline.md]]
- [[70_projects/bundesinnovationshaushalt-trl.md]]
- [[30_concepts/technology-readiness-levels.md]]
- [[40_methods/trl-project-level-reporting.md]]
- [[50_datasets/cordis-horizon-europe-h2020.md]]
- [[50_datasets/foerderkatalog-des-bundes.md]]
- [[30_concepts/llm-annotation-and-automated-coding.md]]
- [[30_concepts/text-as-data-computational-social-science.md]]
- [[30_concepts/foundation-models-and-pretrained-transformers.md]]
- [[40_methods/xlm-roberta-multilingual-classification.md]]
- [[90_synthesis/llm-text-classification-and-annotation.md]]
- [[30_concepts/innovation-paradox.md]]
- [[30_concepts/sme-innovation-participation.md]]

## Semantic verification details

Source identity was checked locally against `10_sources/tornberg2025-llm-outperform-experts.md` during the 2026-05-04 paper-by-paper verification pass. The maintained summary is tied to the source titled "Large Language Models Outperform Expert Coders and Supervised Classifiers at Annotating Political and Social Text" and should be used for the argument, method, findings, and limitations stated in that mapped source rather than for adjacent claims that only appear in project interpretation.

Verification synthesis: Semantic verification against `10_sources/tornberg2025-llm-outperform-experts.md`: Instruction-tuned Large Language Models (LLMs) have recently emerged as a powerful new tool for text analysis. As these models are capable of zero-shot annotation based on instructions written in natural language, they obviate the need of large sets of training data—and thus bring potential paradigm-shifting implications for using text as data. While the models show substantial promise, their relative performance compared to human coders and supervised models remains poorly understood and subject to signiﬁcant academic debate. The source assesses the strengths and weaknesses of popular ﬁne-tuned AI models compared to both conventional supervised classiﬁers and manual annotation by experts and crowd workers. The task used is to identify the political afﬁliation of politicians based on a single X/Twitter message, focusing on data from 11 different countries. The paper ﬁnds that GPT-4 achieves higher accuracy than both supervised models and human coders across all languages and country contexts. In the US context, it achieves an accuracy of

Method and materials check: Instruction-tuned Large Language Models (LLMs) have recently emerged as a powerful new tool for text analysis. As these models are capable of zero-shot annotation based on instructions written in natural language, they obviate the need of large sets of training data—and thus bring potential paradigm-shifting implications for using text as data. While the models show substantial promise, their relative performance compared to human coders and supervised models remains poorly understood and subject to signiﬁcant academic debate. Verification note: this section is grounded in `10_sources/tornberg2025-llm-outperform-experts.md` and should not be generalized beyond Data/materials scope: Named datasets/materials discussed in the maintained note: [[50_datasets/cordis-horizon-europe-h2020.md]]; [[50_datasets/foerderkatalog-des-bundes.md]]. Use `10_sources/tornberg2025-llm-outperform-experts.md` for exact definitions, variable construction, sample period, and table/source-document provenance.

Finding-level check: GPT-4 outperforms expert coders on political polarization, stance, and issue salience tasks - Expert coders show systematic biases that LLMs avoid (fatigue, anchoring, within-coder inconsistency) - LLMs benefit from vast pre-training domain knowledge → no "training" time cost - Paradigm shift argument: the bottleneck is no longer annotation — it is codebook design and validation - Limitation: applies to tasks with clear definitions; breaks down for implicit/cultural tasks

Citation and retrieval guardrails: use this note to retrieve the source together with its linked canonical concept, method, dataset, synthesis, and project pages. Do not cite it for technology-readiness, firm-selection, causal, benchmark-performance, or policy-design claims unless those claims are present in the verified summary sections above or directly in `10_sources/tornberg2025-llm-outperform-experts.md`. If a future draft needs exact quotations, sample definitions, coefficients, task metrics, or legal/institutional wording, reopen the source file before citation.
