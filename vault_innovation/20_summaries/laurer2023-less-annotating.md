---
title: "Less Annotating, More Classifying: Addressing the Data Scarcity Issue of Supervised Machine Learning with Deep Transfer Learning and BERT-NLI"
note_type: source_summary
summary: "Political Analysis article showing that BERT-NLI transfer learning sharply reduces labeled-data needs for political text classification, especially under small and imbalanced training-data regimes."
authors:
  - Moritz Laurer
  - Wouter van Atteveldt
  - Andreu Casas
  - Kasper Welbers
year: 2023
source_files:
  - "10_sources/laurer2023-less-annotating.md"
source_urls:
  - "https://doi.org/10.1017/pan.2023.20"
projects:
  - "bundesinnovationshaushalt-trl"
tags:
  - source-summary
  - bert-nli
  - transfer-learning
  - text-classification
  - political-analysis
  - data-scarcity
  - imbalanced-data
  - text-as-data
status: verified
updated: "2026-05-04"
---

# Less Annotating, More Classifying

## Source paper link/path

- Source file: `10_sources/laurer2023-less-annotating.md`
- Source status: available as converted Markdown in `10_sources/`
- Verification status: semantically checked against the converted source on 2026-05-04.

## Bibliographic metadata

- Title: "Less Annotating, More Classifying: Addressing the Data Scarcity Issue of Supervised Machine Learning with Deep Transfer Learning and BERT-NLI"
- Authors: Moritz Laurer, Wouter van Atteveldt, Andreu Casas, Kasper Welbers
- Journal: Political Analysis
- Publication date: 9 June 2023 online; Political Analysis 32(1): 84-100
- DOI: `10.1017/pan.2023.20`
- Code/data: `https://github.com/MoritzLaurer/less-annotating-with-bert-nli`; replication data also via Code Ocean and Harvard Dataverse.

## Detailed summary

Laurer, van Atteveldt, Casas, and Welbers study a core bottleneck in supervised text-as-data research: political scientists often need to classify large corpora for a new substantive research question, but each new task normally requires a new manually labeled training set. This is especially costly when concepts are rare, classes are imbalanced, or the available annotation budget is small.

The paper argues that deep transfer learning can reduce this data-scarcity problem. Classical supervised models such as support vector machines and logistic regression begin with no internal representation of language or task structure beyond the labeled training data. BERT-style models already contain statistical "language knowledge" from pretraining, but ordinary BERT fine-tuning still has to learn the target classification task from task-specific labels. BERT-NLI adds a second kind of transfer: "task knowledge" learned from natural language inference (NLI), a general task in which a model predicts whether a context entails, contradicts, or is neutral toward a hypothesis.

The key methodological move is to convert ordinary classification labels into natural-language hypotheses. For a topic-classification task, each class is verbalized as a hypothesis such as "This text is about the economy." The input text is treated as the context. The model evaluates each context-hypothesis pair and the class with the strongest entailment signal is selected. This allows BERT-NLI to use both language representations and the general NLI task format rather than learning every target task entirely from scratch.

The empirical analysis compares two classical supervised algorithms, SVM and logistic regression, with two transfer-learning approaches, BERT-base and BERT-NLI. The comparison spans eight political-science classification tasks drawn from five widely used datasets, including the Manifesto Corpus, Sentiment Economy News, US State of the Union speeches, US Supreme Court cases, CoronaNet, and Manifesto stance subsets for military, protectionism, and traditional morality. Tasks vary in domain, unit of analysis, text length, number of classes, and imbalance.

The headline finding is that BERT-NLI reduces annotation needs substantially. Across the eight tasks, BERT-NLI trained on 100 to 2,500 labeled texts performs on average 10.7 to 18.3 F1-macro percentage points better than classical TF-IDF-based models. BERT-NLI with about 500 labeled texts reaches similar average F1-macro performance to classical models trained on about 5,000 texts. BERT-NLI is particularly useful with very small labeled datasets, roughly up to 1,000 observations, while simpler BERT-base can become preferable as more labeled data become available, especially around 2,000 or more observations.

The paper also emphasizes imbalanced data. F1 macro improves more than accuracy or micro-F1 when transfer learning is used, indicating better handling of minority classes. This is important for social-science classification because substantively important concepts often appear in only a small share of the corpus. The authors warn that accuracy or micro-F1 alone can hide poor performance on minority classes.

The authors do not claim that BERT-NLI removes the need for validation. They present it as a way to reduce the amount of training data required and to make supervised classification feasible in more projects. They also discuss limits: BERT-NLI works better when labels can be clearly verbalized as hypotheses, may struggle with complex or ambiguous concepts, can behave differently for majority versus minority classes, remains less interpretable than classical linear models, and requires continued attention to validity and political bias.

## Research question

How much can deep transfer learning, and especially BERT-NLI, reduce task-specific annotation requirements for supervised political text classification compared with classical supervised models and standard BERT fine-tuning?

## Core argument or contribution

The paper's contribution is to show that transfer learning has two separable components for text classification: language knowledge from pretraining and task knowledge from NLI. By verbalizing labels as hypotheses and reusing NLI task knowledge, BERT-NLI can learn new political-science classification tasks from far fewer examples than classical models, especially when data are scarce or imbalanced.

## Methodology

- Model comparison: SVM and logistic regression versus BERT-base and BERT-NLI.
- Transfer-learning setup: BERT-base supplies pretrained language representations; BERT-NLI adds intermediate training on about 1.28 million hypothesis-context pairs from eight general-purpose NLI datasets.
- Task conversion: each target class is manually verbalized as a natural-language hypothesis derived from the codebook.
- Evaluation design: eight tasks from five political-science datasets are repeatedly trained with varying labeled-data sizes.
- Main metric: F1 macro, with additional attention to accuracy/micro-F1 and imbalanced-data behavior.
- Data-size analysis: focuses especially on small training regimes from 100 to 2,500 observations, with comparisons to larger classical-model baselines.

## Datasets/materials used

- Manifesto Corpus topic classification.
- Sentiment Economy News.
- US State of the Union Speeches from the Policy Agendas Project.
- US Supreme Court Cases from the Policy Agendas Project.
- CoronaNet COVID-19 policy-measure data.
- Manifesto stance subsets for military, protectionism, and traditional morality.
- Eight general-purpose NLI datasets used to train the BERT-NLI model.
- Replication code and cleaned data released by the authors.

## Key findings

- BERT-NLI outperforms classical TF-IDF-based supervised models by 10.7 to 18.3 F1-macro percentage points on average when 100 to 2,500 labeled texts are available.
- BERT-NLI with about 500 labeled texts reaches roughly the same average F1-macro performance as classical models with about 5,000 texts.
- BERT-NLI tends to be strongest when labeled data are very limited, especially at or below about 1,000 observations.
- BERT-base can become preferable when more data are available, especially around 2,000 or more observations, because it can learn the target task directly from sufficient examples.
- Transfer learning is particularly useful for imbalanced data because it improves F1 macro more than accuracy/micro-F1 and reduces reliance on majority classes.
- BERT-NLI can make predictions for classes absent from a random training sample because the class is represented as a hypothesis, but those zero-shot capabilities still need validation.
- Word embeddings also improve classical models relative to TF-IDF alone, but the remaining performance gap to BERT-NLI is still large in small-data settings.

## Limitations

- BERT-NLI depends on good hypothesis wording; unclear or complex concepts are harder to verbalize and classify.
- It performs better on relatively simple, clearly expressible concepts, such as military stance, than on complex concepts such as traditional morality.
- BERT-NLI can improve minority-class performance while sometimes performing less well on majority classes, so model choice depends on the substantive use case.
- The study uses random training samples; active learning and other sampling strategies could change annotation-efficiency results.
- Transfer-learning models are less transparent than classical linear models, even if interpretability tools can partly help.
- Political bias, validity, and external validity require further study.
- The paper evaluates political-science English-language tasks; transfer to German R&D project descriptions or TRL classification is not demonstrated directly.

## Important concepts discussed

- [[30_concepts/text-as-data-computational-social-science.md]] - the paper addresses supervised classification as a central text-as-data workflow.
- [[30_concepts/foundation-models-and-pretrained-transformers.md]] - BERT and DeBERTa-style models are used as pretrained transfer-learning models.
- [[30_concepts/llm-annotation-and-automated-coding.md]] - relevant for automated coding under scarce labels, though the paper focuses on BERT-NLI rather than LLM teacher annotation.
- Transfer learning.
- Natural language inference.
- Label verbalization.
- Data scarcity and class imbalance.

## Methods discussed

- Natural-language-inference-based text classification.
- BERT-NLI / NLI-transfer classification.
- Standard BERT fine-tuning.
- SVM and logistic-regression supervised baselines.
- TF-IDF and word-embedding feature representations.
- F1 macro for imbalanced classification evaluation.
- [[40_methods/llm-few-shot-social-science.md]] is a related later/adjacent method family; this paper is about BERT-NLI, not prompting a generative LLM.
- [[40_methods/xlm-roberta-multilingual-classification.md]] is related through multilingual pretrained encoder classification, but XLM-RoBERTa is not the central model in this paper.

## Datasets discussed

- Manifesto Corpus.
- Sentiment Economy News.
- US State of the Union Speeches.
- US Supreme Court Cases.
- CoronaNet.
- General-purpose NLI datasets.

## Relation to other papers in the vault

- Extends the text-as-data concerns in [[20_summaries/grimmer2013-text-as-data.md]] by focusing on supervised learning under annotation scarcity.
- Relates to [[20_summaries/devlin2019-bert.md]] because BERT-style pretrained models provide the language-representation layer.
- Relates to [[20_summaries/zhang2021-few-shot-bert.md]], [[20_summaries/wang2024-bert-vs-gpt.md]], and [[20_summaries/timoneda2025a-bert-roberta-deberta.md]] as evidence about BERT-family classification under limited labels.
- Contrasts with [[20_summaries/gilardi2023-chatgpt-annotation.md]], [[20_summaries/egami2024-llm-annotation-framework.md]], [[20_summaries/halterman2025-codebook-llms.md]], and [[20_summaries/kuzman2025-parlacap.md]], which focus more directly on LLMs as annotators or teachers.

## Implications for LLM research or the project domain

For the Bundesinnovationshaushalt/TRL project, the paper is relevant as a lower-cost alternative or complement to LLM-based annotation. If TRL labels can be expressed clearly as hypotheses or short codebook statements, BERT-NLI-style classification could be tested as a small-label baseline before relying on API-based generative LLM classification.

The project should not treat the paper as evidence that BERT-NLI already works for Foerderkatalog or CORDIS TRL labels. The transferable lessons are methodological: use F1 macro, inspect rare TRL levels separately, compare against simpler supervised baselines, test how many labeled examples are really needed, and validate hypothesis wording carefully.

## Links to canonical concept, method, dataset, synthesis, and project notes

- [[30_concepts/text-as-data-computational-social-science.md]]
- [[30_concepts/foundation-models-and-pretrained-transformers.md]]
- [[30_concepts/llm-annotation-and-automated-coding.md]]
- [[40_methods/llm-few-shot-social-science.md]]
- [[40_methods/xlm-roberta-multilingual-classification.md]]
- [[50_datasets/cordis-horizon-europe-h2020.md]]
- [[70_projects/bundesinnovationshaushalt-trl.md]]
- [[90_synthesis/llm-text-classification-and-annotation.md]]
