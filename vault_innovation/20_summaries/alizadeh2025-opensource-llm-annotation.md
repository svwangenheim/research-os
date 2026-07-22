---
title: "Open-Source LLMs for Text Annotation: A Practical Guide for Model Setting and Fine-Tuning"
note_type: source_summary
summary: "Alizadeh et al. (2024) evaluate open-source and proprietary LLMs for political-science text annotation across content-moderation tweets, content-moderation news, and U.S. congressional tweets. The paper shows that fine-tuned open-source LLMs can exceed MTurk performance and rival zero-shot ChatGPT on several tasks, while fine-tuned GPT-3.5 remains the strongest benchmark. The main practical lesson is validation-first: annotate a modest expert-labeled test/training set, prefer fine-tuning over costly few-shot prompting when labels are available, use low temperature for repeatability, and report accuracy/agreement rather than assuming transfer across tasks."
authors: ["Meysam Alizadeh", "Mael Kubli", "Zeynab Samei", "Shirin Dehghani", "Mohammadmasiha Zahedivafa", "Juan D. Bermeo", "Maria Korobeynikova", "Fabrizio Gilardi"]
year: 2024
source_files: ["10_sources/alizadeh2025-opensource-llm-annotation.md", "10_sources/alizadeh2025-opensource-llm-annotation.pdf"]
source_urls:
  - "https://arxiv.org/abs/2307.02179"
projects: [bundesinnovationshaushalt-trl]
tags:
  - source-summary
  - llm-annotation
  - open-source-llms
  - text-classification
  - social-science-methods
updated: "2026-05-04"
---

# Alizadeh et al. (2024) - Open-Source LLMs for Text Annotation

## Source paper link/path

- Source file: `10_sources/alizadeh2025-opensource-llm-annotation.md`
- Source PDF: `10_sources/alizadeh2025-opensource-llm-annotation.pdf`
- Source status: corrected on 2026-05-04. The previous local PDF/Markdown were an unrelated stochastic-optimization paper.
- One-by-one audit status: locally checked against the listed source Markdown on 2026-05-04.

## Bibliographic metadata

- Title: "Open-Source LLMs for Text Annotation: A Practical Guide for Model Setting and Fine-Tuning"
- Authors: Meysam Alizadeh, Mael Kubli, Zeynab Samei, Shirin Dehghani, Mohammadmasiha Zahedivafa, Juan D. Bermeo, Maria Korobeynikova, and Fabrizio Gilardi
- Year/version in local source: May 30, 2024 arXiv v2
- arXiv: `2307.02179`
- Field: computational social science / political-science text annotation

## Detailed summary

The paper studies whether open-source LLMs can be used for political-science text annotation in a way that is accurate, reproducible, and practically useful. Its central contribution is not just another claim that LLMs can annotate text, but a workflow comparison: researchers must decide whether to use zero-shot prompting, few-shot prompting, or supervised fine-tuning; whether to use proprietary or open-source models; how much human-labeled data to create; what temperature to use; and how to validate the resulting labels.

The authors extend earlier work on ChatGPT and text annotation by comparing GPT-3.5, GPT-4, LLaMA-1 through HuggingChat, LLaMA-2, and FLAN-T5 across eleven annotation tasks distributed over four datasets. The tasks include relevance classification, stance detection, topic detection, content-moderation problem/solution framing, and policy-frame detection. The gold standard is trained human annotation, and performance is assessed using accuracy, intercoder agreement, and, for fine-tuning, precision/recall/F1 by class.

The results are deliberately practical. Few-shot prompting with chain-of-thought examples produces mixed results: some tasks improve, some deteriorate, and no stable rule emerges by task complexity, model, or data type. Lower temperature settings are more reliable for annotation because they increase repeatability and intercoder agreement; for HuggingChat, reducing temperature substantially improves agreement and can improve accuracy in some tasks. Fine-tuning is the strongest lever. With modest expert-labeled training data, fine-tuned open-source models such as LLaMA and FLAN become competitive alternatives for text annotation. They generally exceed MTurk performance and can rival zero-shot GPT-3.5/ChatGPT in several settings, although fine-tuned GPT-3.5 remains ahead overall.

The paper's main recommendation is validation-first use of LLMs. Researchers should not assume that a model, prompt, or temperature setting transfers to a new corpus. They should manually annotate a small but meaningful sample, use part of it for fine-tuning and part for evaluation, validate outputs against expert labels, run models more than once when stochasticity matters, report both accuracy and agreement, and prefer low temperature for repeatability.

## Research question

How should researchers configure and validate open-source and proprietary LLMs for social-science text annotation, and when do zero-shot prompting, few-shot prompting, and fine-tuning provide reliable performance relative to trained annotators and MTurk?

## Core argument or contribution

The paper contributes a practical benchmark and workflow guide for LLM-based text annotation. It shows that open-source LLMs are viable for many political-science annotation tasks when they are fine-tuned and validated, but it rejects the idea that one model or prompt setting can be assumed to work across tasks.

## Methodology

- Comparative benchmark of proprietary and open-source LLMs against trained human labels and MTurk.
- Zero-shot prompting, few-shot chain-of-thought prompting, and supervised fine-tuning.
- Model comparison across GPT-3.5, GPT-4, LLaMA-1/HuggingChat, LLaMA-2, and FLAN-T5 variants.
- Low-temperature versus default-temperature comparison for accuracy and intercoder agreement.
- Fine-tuning with modest labeled training sets, LoRA/adapters, quantization, and held-out evaluation.
- Evaluation by average accuracy, intercoder agreement, precision, recall, and F1.

## Datasets/materials used

- Content-moderation tweets from 2020-2021: randomly sampled from a larger corpus of about 2.6 million tweets.
- Content-moderation news articles from 2020-2021: sampled from LexisNexis articles.
- Content-moderation tweets from January 2023: a new sample used partly to address training-data contamination concerns.
- Tweets by members of the U.S. Congress from 2017-2022.
- Trained political-science student annotations used as the main reference labels.
- MTurk annotations collected under quality restrictions and used as a comparison group.

## Key findings

- Fine-tuning substantially improves text-annotation performance and is the paper's most important practical lever.
- Fine-tuned open-source LLMs can generally outperform MTurk and rival zero-shot ChatGPT/GPT-3.5 in several tasks, while fine-tuned GPT-3.5 remains stronger overall.
- Few-shot chain-of-thought prompting is not consistently better than zero-shot prompting; effects vary by task, model, and dataset.
- Lower temperature settings improve repeatability and intercoder agreement, and the paper recommends low or zero temperature for annotation.
- The authors recommend manually annotating roughly 250-500 examples when feasible, splitting them between fine-tuning and accuracy testing.
- Researchers should always validate LLM annotations with expert human evaluation on the specific corpus and task.
- Open-source LLMs offer practical advantages in cost, reproducibility, transparency, and data protection, but they still require task-specific testing.

## Limitations

- The findings are bounded by political-science text annotation tasks, especially content-moderation and U.S. political text.
- Performance does not transfer automatically to new domains, languages, codebooks, or high-stakes classification tasks.
- Fine-tuning open-source models requires technical infrastructure and can require substantial GPU resources.
- The gold standard is trained human annotation, so model performance is measured relative to the quality and scope of those labels.
- The paper evaluates annotation quality, not whether downstream causal or policy analyses remain valid after using LLM-generated labels.

## Important concepts discussed

- [[30_concepts/llm-annotation-and-automated-coding.md]]
- [[30_concepts/text-as-data-computational-social-science.md]]
- [[30_concepts/foundation-models-and-pretrained-transformers.md]]
- Open-source LLMs
- Fine-tuning
- Few-shot prompting
- Zero-shot prompting
- Annotation validation
- Intercoder agreement

## Methods discussed

- [[40_methods/llm-few-shot-social-science.md]]
- Supervised fine-tuning for text classification
- Chain-of-thought few-shot prompting
- Low-temperature annotation runs
- Human-label validation
- Accuracy and intercoder-agreement benchmarking

## Datasets discussed

- Content-moderation tweet datasets
- Content-moderation news article dataset
- U.S. congressional tweet dataset
- MTurk annotation outputs
- Trained human reference labels

## Relation to other papers in the vault

This paper complements [[20_summaries/gilardi2023-chatgpt-annotation.md]], which established that ChatGPT can outperform crowd workers on several annotation tasks. It also connects to [[20_summaries/pangakis2023-llm-annotation-validation.md]] because both stress validation against human-coded labels, and to [[20_summaries/tornberg2025-llm-outperform-experts.md]] because both compare LLMs with human annotators. Compared with those papers, Alizadeh et al. are especially useful for decisions about open-source models, fine-tuning, temperature, and how many labeled examples to create before scaling annotation.

## Implications for LLM research or the project domain

For [[70_projects/bundesinnovationshaushalt-trl.md]], this paper supports an LLM-assisted Foerderkatalog coding workflow only if it includes project-specific human validation. It is relevant for deciding whether open-source models can classify German public-funding records when privacy, reproducibility, or cost constraints matter. The paper does not itself validate TRL coding, German-language funding descriptions, or innovation-policy categories, so its correct use is methodological: create a labeled German test set, compare model settings, validate agreement and accuracy, and only then scale automated coding.

## Semantic verification details

Checked one-by-one against `10_sources/alizadeh2025-opensource-llm-annotation.md` on 2026-05-04. The maintained note reflects the corrected local source, whose title is "Open-Source LLMs for Text Annotation: A Practical Guide for Model Setting and Fine-Tuning." It should not be cited as evidence that open-source LLMs universally outperform proprietary LLMs; the source-specific claim is that fine-tuned open-source LLMs can be competitive and often outperform MTurk, while fine-tuned GPT-3.5 remains the strongest benchmark in the paper.

## Links to canonical concept, method, dataset, synthesis, and project notes

- [[30_concepts/llm-annotation-and-automated-coding.md]]
- [[30_concepts/text-as-data-computational-social-science.md]]
- [[30_concepts/foundation-models-and-pretrained-transformers.md]]
- [[40_methods/llm-few-shot-social-science.md]]
- [[90_synthesis/llm-text-classification-and-annotation.md]]
- [[70_projects/bundesinnovationshaushalt-trl.md]]
