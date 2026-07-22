---
title: "Text-as-Data and Computational Social Science"
note_type: concept
summary: "Text-as-data and computational social science treats political, administrative, social, and economic text as empirical data that require measurement design, validation, and interpretation rather than mere extraction. In this vault it anchors the LLM/text-classification evidence layer."
canonical: true
aliases:
  - text as data
  - computational social science
  - political text analysis
  - social-science text classification
  - automated text analysis
related_notes:
  - "[[30_concepts/llm-annotation-and-automated-coding.md]]"
  - "[[30_concepts/foundation-models-and-pretrained-transformers.md]]"
  - "[[30_concepts/data-access-for-innovation-policy.md]]"
related_summaries:
  - "[[20_summaries/grimmer2013-text-as-data.md]]"
  - "[[20_summaries/timoneda2025a-bert-roberta-deberta.md]]"
  - "[[20_summaries/timoneda2025b-behind-the-mask.md]]"
  - "[[20_summaries/wang2024-bert-vs-gpt.md]]"
  - "[[20_summaries/laurer2023-less-annotating.md]]"
  - "[[20_summaries/chae2025-llm-instruction-tuning.md]]"
  - "[[20_summaries/egami2024-llm-annotation-framework.md]]"
related_methods:
  - "[[40_methods/llm-few-shot-social-science.md]]"
  - "[[40_methods/xlm-roberta-multilingual-classification.md]]"
  - "[[40_methods/trl-klassifikation-pipeline.md]]"
related_datasets:
  - "[[50_datasets/foerderkatalog-des-bundes.md]]"
projects:
  - "[[70_projects/bundesinnovationshaushalt-trl.md]]"
tags:
  - concept
  - text-as-data
  - computational-social-science
  - methodology
updated: "2026-04-29"
---

# Text-as-Data and Computational Social Science

## Definition

Text-as-data and computational social science is the research approach that converts text into analyzable measures while preserving social-science standards of concept definition, validation, uncertainty, and interpretation. Texts can be speeches, project descriptions, patent abstracts, policy documents, survey answers, manifestos, media texts, or administrative records. The central idea is that text is not automatically data: a researcher must define what is being measured, choose or build a method, validate the resulting labels or scores, and interpret them against a substantive theory.

## Scope boundaries

Included:

- Automated text classification, scaling, topic modeling, embedding workflows, and LLM-assisted coding when used for social-science measurement.
- Validation against expert labels, human-coded benchmarks, or theory-grounded expectations.
- Discussions of domain shift, label design, annotation quality, and measurement error.
- Use of text-derived variables in downstream descriptive, comparative, or causal analysis.

Excluded:

- General NLP engineering without a social-science measurement problem.
- Pure document retrieval or search unless it produces research variables.
- Generic writing assistance by LLMs.

## Papers that discuss this concept

- [[20_summaries/grimmer2013-text-as-data.md]]: foundational survey arguing that automated text analysis must be validated and that no single method is universally superior.
- [[20_summaries/timoneda2025a-bert-roberta-deberta.md]]: compares BERT-family models for political text classification and shows model choice matters for social-science labels.
- [[20_summaries/timoneda2025b-behind-the-mask.md]]: examines domain-adaptive pretraining choices for social-science classification.
- [[20_summaries/wang2024-bert-vs-gpt.md]]: compares BERT fine-tuning and GPT models across political classification tasks with different label counts and sample sizes.
- [[20_summaries/laurer2023-less-annotating.md]]: shows that zero-shot and NLI-style classification can reduce annotation requirements in some political text settings.
- [[20_summaries/chae2025-llm-instruction-tuning.md]]: connects instruction tuning and in-context learning to classification performance.
- [[20_summaries/egami2024-llm-annotation-framework.md]], [[20_summaries/pangakis2023-llm-annotation-validation.md]], and [[20_summaries/ziems2024-llm-css-benchmark.md]]: update the text-as-data tradition for LLM-era annotation and validation.
- [[20_summaries/krieger2020-foerderkatalog-querschnitt.md]]: applies text classification to German funding-project descriptions and directly motivates the Foerderkatalog TRL project.

## How the papers use, support, challenge, or modify it

Grimmer and Stewart provide the older methodological discipline: validate the measure and connect it to the research question. The BERT/RoBERTa/DeBERTa and XLM-R papers add that modern pretrained language models can materially improve classification, but only when the data, language, class structure, and validation design fit the task. The LLM-annotation papers extend the same logic to prompting and model-based coding: LLMs can reduce labeling costs, but they do not remove the need for construct validity.

For the Foerderkatalog project, this concept says that TRL classification is a measurement problem before it is a modeling problem. The project must define TRL categories, represent edge cases, validate model outputs, and decide what descriptive or inferential claims the text-derived variable can support.

## Related concepts

- [[30_concepts/llm-annotation-and-automated-coding.md]]
- [[30_concepts/foundation-models-and-pretrained-transformers.md]]
- [[30_concepts/data-access-for-innovation-policy.md]]
- [[30_concepts/technology-readiness-levels.md]]

## Related methods and datasets

- [[40_methods/llm-few-shot-social-science.md]]
- [[40_methods/xlm-roberta-multilingual-classification.md]]
- [[40_methods/trl-klassifikation-pipeline.md]]
- [[50_datasets/foerderkatalog-des-bundes.md]]
- [[50_datasets/cordis-horizon-europe-h2020.md]]

## Open questions and tensions

- How much validation is enough when the text-derived variable will be used for policy diagnosis?
- When should a researcher prefer few-shot LLM classification over supervised fine-tuning?
- Can LLM annotation replace human coding, or should it mostly be treated as a scalable first pass?
- How should measurement uncertainty be propagated into downstream claims?
- How should multilingual administrative text be handled when source labels and training evidence come from English-language benchmarks?

## Retrieval links

Use this note for queries about text-as-data, computational social science, political text classification, administrative text classification, validation of text-derived variables, and social-science use of LLMs. For operational details, retrieve [[40_methods/llm-few-shot-social-science.md]], [[40_methods/xlm-roberta-multilingual-classification.md]], and [[40_methods/trl-klassifikation-pipeline.md]].
