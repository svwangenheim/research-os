---
title: "Large-Scale Text Analysis Using Generative Language Models: A Case Study in Discovering Public Value Expressions in AI Patents"
note_type: source_summary
summary: "Pelaez, Verma, Ribeiro, and Shapira use GPT-4 to label and generate rationales for public value expressions in US AI patent sentences, then train BERT-based classifiers to scale prediction across a 154,934-document patent corpus containing 5.4 million sentences. The paper is a strong example of LLM-assisted labeling plus rationale review plus discriminative-model scaling for complex abstract concepts."
authors: [Sergio Pelaez, Gaurav Verma, Barbara Ribeiro, Philip Shapira]
year: 2024
source_files: ["10_sources/pelaez2024-patent-public-value-llm.md", "10_sources/pelaez2024-patent-public-value-llm.pdf"]
source_urls:
  - "https://arxiv.org/abs/2305.10383"
  - "https://doi.org/10.1162/qss_a_00285"
projects: [bundesinnovationshaushalt-trl]
tags:
  - source-summary
  - llm-annotation
  - patents
  - public-value
  - bert
  - ai-patents
updated: "2026-05-04"
---

# Pelaez et al. (2024) - Public Value Expressions in AI Patents

## Source paper link/path

- Source file: `10_sources/pelaez2024-patent-public-value-llm.md`
- Source PDF: `10_sources/pelaez2024-patent-public-value-llm.pdf`
- Source status: corrected on 2026-05-04. The previous local PDF/Markdown were an unrelated superconducting-islands physics paper.

## Bibliographic metadata

- Title: "Large-Scale Text Analysis Using Generative Language Models: A Case Study in Discovering Public Value Expressions in AI Patents"
- Authors: Sergio Pelaez, Gaurav Verma, Barbara Ribeiro, and Philip Shapira
- Year: 2024 journal reference; arXiv version dated 2023
- Journal: Quantitative Science Studies, 5(1), 153-169
- DOI: `10.1162/qss_a_00285`
- arXiv: `2305.10383`

## Detailed summary

The paper develops a semi-automated text-analysis workflow for identifying complex abstract concepts in large corpora. Its case is public value expressions in US artificial-intelligence patent text. Public value expressions are sentences that indicate societal benefits promised to or for people, organizations, or ecosystems. The authors stress that such expressions are signals of intended or narrated public value, not proof that a patented technology actually produces those benefits.

The data pipeline begins with an AI-patent search strategy based on AI keywords and CPC/IPC classifications. The authors submit a Boolean query to InnovationQ+, yielding 198,456 patent documents at the invention-family level. They then merge those records with USPTO/PatentsView full patent text and obtain a final corpus of 154,934 US AI patent documents filed between 2005 and 2022. Splitting patent text into sentences yields about 5.4 million sentences.

Because public value expressions are sparse in patent text, the authors use keyword filtering to create a denser candidate set. They build a list of 320 single words, bigrams, and trigrams from literature and guidelines on AI benefits, AI risks, governance, responsible innovation, and related topics. Filtering produces 73,813 candidate sentences. They then construct a 10,000-sentence training and evaluation set using a keyword-importance ranking that oversamples sentences more likely to contain public value expressions.

The conceptual and labeling framework is developed iteratively with human input and GPT-4. The classification distinguishes direct public value expressions, contextual public value expressions, and no public value expression. The prompt gives GPT-4 a role, definitions, coding guidelines, examples, and rationales. The workflow asks GPT-4 to provide both a label and a rationale, making the annotation more inspectable for human review.

The authors evaluate GPT-4 rationales using BLEU scores and topic modeling. These checks are intended to assess whether GPT-4 simply parrots the examples or produces diverse and faithful rationales that generalize to unseen public value themes. The paper reports that GPT-4 produces labels and rationales that are accurate, diverse, and faithful enough to support the workflow, and that in a separate evaluation set GPT-4 agreement with human labels reached 95%.

Because labeling the entire 5.4-million-sentence corpus directly with GPT-4 would be expensive, the authors use GPT-4-generated labels to train open-source BERT-based classifiers. They use 9,000 GPT-labeled examples for training and 1,000 GPT-identified, human-verified examples for evaluation. The modeling compares several pretrained language models under both three-class and two-class settings. The paper reports F1 around 0.85 for the three-class task and above 0.90 for the binary public-value/no-public-value task.

For the vault, the paper is important as a method pattern: use a generative LLM to handle abstract, codebook-heavy labeling and produce human-checkable rationales, then train a cheaper discriminative classifier for full-corpus scaling. It is especially relevant where the target concept is too abstract for simple keyword rules but too large for manual coding.

## Research question

Can a generative LLM produce useful labels and rationales for complex public-value concepts in patent text, and can those labels train scalable classifiers for large patent corpora?

## Core argument or contribution

The paper contributes a hybrid LLM-plus-classifier workflow for large-scale text analysis. Its substantive contribution is a framework for detecting public value expressions in AI patents. Its methodological contribution is showing that GPT-4 can support abstract-concept labeling with rationales and that GPT-4 labels can be used to train BERT-based models for large-scale prediction.

## Methodology

- AI patent corpus construction using InnovationQ+ search and USPTO/PatentsView full text.
- Sentence segmentation of patent documents.
- Keyword filtering to obtain a denser candidate set of possible public value expressions.
- Human-guided framework development for direct, contextual, and non-public-value sentences.
- GPT-4 prompt-based labeling with definitions, guidelines, examples, and rationales.
- BLEU and topic-modeling checks of generated rationales.
- BERT-based classifier training on GPT-4 labels and human-verified evaluation samples.
- Corpus-scale prediction over patent sentences.

## Datasets/materials used

- InnovationQ+ AI patent search results.
- USPTO/PatentsView full patent text.
- 154,934 US AI patent documents filed between 2005 and 2022.
- Approximately 5.4 million patent sentences.
- 73,813 keyword-filtered candidate sentences.
- 10,000-sentence training/evaluation set.
- GPT-4 labels and rationales.
- Human verification for evaluation.

## Key findings

- GPT-4 can label patent sentences for public value expressions when given a carefully designed framework, examples, and rationales.
- Public value expressions can be divided into direct PVE, contextual PVE, and no-PVE categories.
- GPT-4-generated rationales are used as a transparency and verification mechanism rather than as unquestioned ground truth.
- BLEU and topic-modeling checks suggest the rationales are diverse and can surface public value themes beyond the prompt examples.
- BERT-based classifiers trained on GPT-4 labels achieve strong reported performance: about 0.85 F1 for the three-class setting and above 0.90 F1 for the binary setting.
- The workflow reduces manual labeling costs while preserving a human-review path for complex concepts.

## Limitations

- A public value expression is only a signal in patent text; it is not evidence that a technology actually produces public value.
- The application is restricted to US AI patent documents and public value expressions.
- GPT-4 labels and rationales require human oversight and framework design; they should not be treated as automatically valid.
- BLEU and topic modeling are indirect checks of rationale quality and do not replace substantive expert validation.
- The approach depends on access to full patent text, a strong LLM, and enough labeled examples to train and evaluate downstream classifiers.

## Important concepts discussed

- [[30_concepts/llm-annotation-and-automated-coding.md]]
- [[30_concepts/text-as-data-computational-social-science.md]]
- [[30_concepts/foundation-models-and-pretrained-transformers.md]]
- Public value expressions
- AI patents
- LLM rationales
- Hybrid generative/discriminative annotation workflow

## Methods discussed

- [[40_methods/llm-few-shot-social-science.md]]
- GPT-4 assisted labeling
- Rationale-based annotation
- BERT-based text classification
- Topic-modeling validation
- Patent text mining

## Datasets discussed

- US AI patent corpus from InnovationQ+ and USPTO/PatentsView
- Patent sentence corpus
- GPT-4-labeled training/evaluation set

No canonical dataset note is linked because the vault does not currently contain a dedicated AI-patent/public-value dataset note.

## Relation to other papers in the vault

This paper complements [[20_summaries/egami2024-llm-annotation-framework.md]], [[20_summaries/pangakis2023-llm-annotation-validation.md]], [[20_summaries/halterman2025-codebook-llms.md]], and [[20_summaries/ziems2024-llm-css-benchmark.md]]. It is especially relevant for workflows that use LLMs to produce initial labels and explanations before training scalable classifiers.

## Implications for LLM research or the project domain

For [[70_projects/bundesinnovationshaushalt-trl.md]], the paper supports a possible hybrid workflow: use an LLM to generate interpretable labels and rationales for a validated subset of project descriptions, then train a cheaper classifier for larger-scale application. This is relevant for abstract coding tasks such as public-value relevance, mission relevance, societal-benefit framing, or possibly TRL-adjacent categories.

The paper does not directly validate TRL classification or Foerderkatalog coding. Its transferable lesson is method design: define the concept carefully, include examples and negative examples, require rationales, verify outputs with humans, and use a discriminative model only after the generated labels have passed validation.

## Links to canonical concept, method, dataset, synthesis, and project notes

- Concepts: [[30_concepts/llm-annotation-and-automated-coding.md]], [[30_concepts/text-as-data-computational-social-science.md]], [[30_concepts/foundation-models-and-pretrained-transformers.md]]
- Methods: [[40_methods/llm-few-shot-social-science.md]]
- Datasets: no canonical dataset note linked
- Synthesis: [[90_synthesis/llm-text-classification-and-annotation.md]]
- Project: [[70_projects/bundesinnovationshaushalt-trl.md]]
