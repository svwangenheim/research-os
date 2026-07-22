---
title: "Supercharging Agenda Setting Research: The ParlaCAP Dataset of 28 European Parliaments"
note_type: source_summary
summary: "ParlaCAP builds a multilingual European parliamentary agenda-setting dataset by using GPT-4o as a teacher annotator for CAP policy topics and fine-tuning XLM-RoBERTa/XLM-R-Parla student classifiers for scalable annotation of millions of speeches."
authors:
  - Taja Kuzman Pungersek
  - Peter Rupnik
  - Daniela Sirinic
  - Nikola Ljubesic
year: 2026
source_files:
  - "10_sources/kuzman2025-parlacap.md"
source_urls:
  - "https://arxiv.org/abs/2602.16516"
projects:
  - "bundesinnovationshaushalt-trl"
tags:
  - source-summary
  - parlacap
  - parlamint
  - comparative-agendas-project
  - llm-annotation
  - teacher-student
  - xlm-roberta
  - multilingual-classification
  - text-as-data
status: verified
updated: "2026-05-04"
---

# Supercharging Agenda Setting Research: The ParlaCAP Dataset of 28 European Parliaments

## Source paper link/path

- Source file: `10_sources/kuzman2025-parlacap.md`
- Source status: available as converted Markdown in `10_sources/`
- Verification status: semantically checked against the converted source on 2026-05-04.
- Filename note: the vault filename uses `2025`, while the local source points to arXiv `2602.16516`.

## Bibliographic metadata

- Title: "Supercharging Agenda Setting Research: The ParlaCAP Dataset of 28 European Parliaments and a Scalable Multilingual LLM-Based Classification"
- Authors: Taja Kuzman Pungersek, Peter Rupnik, Daniela Sirinic, Nikola Ljubesic
- Year: 2026 arXiv version
- Institutions: Jozef Stefan Institute; University of Ljubljana; Institute of Contemporary History; University of Zagreb
- URL: `https://arxiv.org/abs/2602.16516`

## Detailed summary

Kuzman Pungersek, Rupnik, Sirinic, and Ljubesic introduce ParlaCAP, a large multilingual dataset for comparative agenda-setting research in European parliaments. The dataset applies Comparative Agendas Project (CAP) major-topic labels to the ParlaMint parliamentary-speech corpus and combines these topic labels with speaker, party, and sentiment metadata. The goal is to make large-scale comparison of parliamentary attention possible across countries, languages, parties, and speaker groups without requiring manual coding of millions of speeches.

The paper has two linked contributions. First, it develops a scalable LLM-teacher/student-model pipeline for policy-topic classification. GPT-4o is used to annotate in-domain training data with 22 labels: the 21 CAP major topics plus an "Other" label for speeches that do not address a policy topic. Smaller multilingual encoder models, especially XLM-RoBERTa-large and the parliamentary-domain XLM-R-Parla model, are then fine-tuned on the LLM-labeled training data. This design uses the LLM where its quality is valuable but avoids applying it directly to the entire corpus of more than 8 million speeches.

Second, the paper releases a structured ParlaCAP dataset built from ParlaMint 5.0. It contains about 8 million speeches from 28 European national and regional parliaments. For each speech, the dataset provides the assigned CAP topic, an aggregate sentiment label from ParlaSent, and metadata from ParlaMint and other political-data sources. It is designed in a tabular text-as-data format for social-science analysis rather than only linguistic corpus analysis.

The training data are constructed by sampling 1,200 speeches from each of 29 ParlaMint 4.1 corpora, yielding 34,800 speeches, and automatically labeling them with GPT-4o using detailed CAP label descriptions. Because the Public Lands category is extremely rare in the initial data, the authors add targeted augmentation: keyword retrieval over machine-translated English text identifies candidate speeches, GPT-4o re-annotates them, and 779 additional Public Lands examples are added. This raises the Public Lands training count from 145 to 924. The final training dataset contains 35,579 speeches, with 29,779 training instances and 5,800 development instances.

For evaluation, the authors create expert-annotated test sets in English, Croatian, Serbian, and Bosnian, with roughly 824 to 876 instances per language and 22 labels. A Croatian sample is triple-annotated to compare human-human and GPT-4o-human agreement. Nominal Krippendorff's alpha among human annotators ranges from 0.59 to 0.68, while agreement between GPT-4o and human annotators ranges from 0.60 to 0.64. The authors interpret this as evidence that GPT-4o is sufficiently comparable to human annotators for generating training labels in this task.

The fine-tuned model results support the teacher-student design. XLM-R-Parla generally performs slightly better than baseline XLM-RoBERTa and substantially better when rare-category augmentation is included. Public Lands F1 rises from 0.30 to 0.80 after augmentation. The best XLM-R-Parla model trained on ParlaMint plus Public Lands examples achieves macro-F1 of about 0.72 on English, 0.68 on Croatian, 0.71 on Serbian, and 0.64 on Bosnian without confidence filtering. With a 0.60 confidence threshold that labels uncertain predictions as "Mix", the remaining predictions reach micro-F1/macro-F1/accuracy of 0.76 in English, 0.72/0.73/0.72 in Croatian, 0.75/0.74/0.75 in Serbian, and 0.69/0.68/0.69 in Bosnian, while about 9-11 percent of instances are withheld as low confidence.

The paper also compares ParlaCAP to existing out-of-domain CAP classifiers. ParlaCAP outperforms other XLM-RoBERTa CAP models trained on manually annotated but less domain-matched sources. This supports the paper's domain-specific training argument: LLM-labeled in-domain data can be more useful than manually labeled but domain-mismatched data for large-scale parliamentary topic classification.

Finally, the paper illustrates the dataset with three descriptive use cases: the distribution of parliamentary attention across policy topics, sentiment patterns across topics and countries, and gender differences in policy attention. These examples are demonstrations of dataset utility, not causal claims.

## Research question

Can a multilingual LLM-teacher/student-model workflow produce reliable, scalable CAP topic labels for millions of European parliamentary speeches, and can the resulting ParlaCAP dataset support comparative agenda-setting research across parliaments?

## Core argument or contribution

The paper argues that large language models can be used cost-effectively as high-quality training-data annotators, while smaller multilingual encoder models can do the scalable production annotation. This combination produces an in-domain parliamentary topic classifier that is competitive with human annotation agreement, comparable to GPT-4o performance on test data, and stronger than existing CAP classifiers trained on out-of-domain data.

## Methodology

- Label schema: 21 CAP major topics plus an "Other" label for non-policy-topic speeches.
- Teacher annotation: GPT-4o labels 34,800 sampled ParlaMint speeches using detailed CAP label descriptions.
- Rare-class augmentation: Public Lands is augmented through keyword retrieval over machine-translated English text and GPT-4o re-annotation, increasing the class from 145 to 924 examples.
- Student models: XLM-RoBERTa-large and XLM-R-Parla are fine-tuned on the LLM-labeled training data.
- Training data: 35,579 speeches total; 29,779 training instances and 5,800 development instances.
- Test data: manually annotated English, Croatian, Serbian, and Bosnian test sets with roughly 824-876 instances each.
- Agreement check: nominal Krippendorff's alpha compares human-human and GPT-4o-human annotation.
- Evaluation metrics: macro-F1, micro-F1, accuracy, and performance after confidence-threshold filtering.
- Dataset release: the classifier is applied to ParlaMint 5.0 to build ParlaCAP with topic labels, sentiment labels, and metadata.

## Datasets/materials used

- ParlaMint 4.1 for training-data sampling.
- ParlaMint 5.0 for the released ParlaCAP dataset.
- Comparative Agendas Project (CAP) master-codebook labels and descriptions.
- GPT-4o-labeled training data.
- Expert-annotated test sets in English, Croatian, Serbian, and Bosnian.
- XLM-RoBERTa-large and XLM-R-Parla models.
- ParlaSent sentiment predictions.
- PartyFacts and V-Dem metadata, alongside ParlaMint metadata.

## Key findings

- The ParlaCAP dataset covers about 8 million speeches from 28 European national and regional parliaments.
- GPT-4o agreement with human annotators is similar to human-human agreement for the CAP labeling task: human-human alpha ranges from 0.59 to 0.68, while GPT-4o-human alpha ranges from 0.60 to 0.64.
- LLM annotation through the OpenAI batch API costs about USD 100 for the training-data labeling step described in the source.
- XLM-R-Parla with Public Lands augmentation is the strongest fine-tuned student model in the reported experiments.
- Without confidence filtering, the best XLM-R-Parla model reports macro-F1 of about 0.72 on English, 0.68 on Croatian, 0.71 on Serbian, and 0.64 on Bosnian.
- Confidence filtering at 0.60 with a "Mix" label excludes about 9 percent of English instances and 11 percent of the other test sets, raising performance on retained predictions to roughly 0.69-0.76 across micro-F1, macro-F1, and accuracy.
- Rare-class augmentation matters strongly: Public Lands F1 improves from 0.30 to 0.80 after adding LLM-labeled examples.
- Domain-matched LLM-labeled training data outperform several existing CAP classifiers trained on manually annotated but out-of-domain data.
- The dataset enables descriptive comparative analyses of topic attention, sentiment, and gendered attention patterns, but the paper does not present causal estimates.

## Limitations

- The teacher labels depend on GPT-4o and the authors' CAP prompt/label-description design.
- Student-model performance is bounded by the quality and biases of LLM-labeled training data.
- The expert test sets cover four languages, not all languages in ParlaCAP.
- The confidence-thresholded results trade coverage for reliability by moving low-confidence cases into "Mix".
- Rare categories can perform poorly without targeted augmentation.
- Some corpus components rely on machine-translated English text for retrieval or cross-language processing.
- Use-case analyses are illustrative/descriptive and require additional research designs for causal claims.
- The paper is about parliamentary policy-topic classification, not R&D funding classification or TRL assignment.

## Important concepts discussed

- [[30_concepts/llm-annotation-and-automated-coding.md]] - GPT-4o is used as a scalable teacher annotator for social-science labels.
- [[30_concepts/text-as-data-computational-social-science.md]] - ParlaCAP converts parliamentary speech corpora into structured comparative political data.
- [[30_concepts/foundation-models-and-pretrained-transformers.md]] - the workflow combines a decoder LLM teacher with multilingual encoder student models.
- Comparative agenda-setting research.
- Domain adaptation and in-domain training data.
- Confidence filtering and abstention in automated coding.

## Methods discussed

- [[40_methods/xlm-roberta-multilingual-classification.md]] - XLM-RoBERTa and XLM-R-Parla are the main student classifier architectures.
- LLM teacher-student annotation/classification pipeline.
- GPT-4o prompt-based data annotation.
- Fine-tuning multilingual encoder models.
- Rare-class augmentation through keyword retrieval and LLM re-annotation.
- Expert test-set annotation and Krippendorff's alpha agreement checks.
- Confidence-threshold filtering with a "Mix" label.

## Datasets discussed

- ParlaCAP.
- ParlaMint 4.1 and 5.0.
- Comparative Agendas Project labels/codebook.
- ParlaSent.
- PartyFacts.
- V-Dem.

## Relation to other papers in the vault

- Closely related to [[20_summaries/alizadeh2025-opensource-llm-annotation.md]], [[20_summaries/gilardi2023-chatgpt-annotation.md]], [[20_summaries/pangakis2023-llm-annotation-validation.md]], and [[20_summaries/halterman2025-codebook-llms.md]] as evidence on LLM-assisted annotation and automated coding workflows.
- Related to [[20_summaries/grimmer2013-text-as-data.md]] because ParlaCAP operationalizes text-as-data principles at a large multilingual scale.
- Related to [[20_summaries/conneau2020-xlm-roberta.md]] and [[20_summaries/wang2024-bert-vs-gpt.md]] for multilingual encoder models and BERT-versus-GPT tradeoffs.
- Methodologically relevant to [[20_summaries/krieger2020-foerderkatalog-querschnitt.md]] because both classify large policy-text corpora into policy-relevant categories, though Krieger et al. use rule-based semantic analysis of German R&D project descriptions.

## Implications for LLM research or the project domain

For the Bundesinnovationshaushalt/TRL project, this paper is useful as a methodological analogue rather than a direct evidence source about R&D funding. It supports a workflow where an expensive or stronger LLM is used to create training labels and a cheaper multilingual encoder is fine-tuned for large-scale classification. That design is relevant for Foerderkatalog classification if manual labels are scarce and production inference must be cheap.

The paper also gives concrete evaluation lessons: report macro-F1, not only accuracy; inspect rare classes separately; use targeted augmentation for underrepresented labels; hold out expert-labeled test data; and consider confidence-based abstention instead of forcing every project into a class. These lessons map naturally to TRL classification, where some TRL levels may be rare or ambiguous.

The source does not show that ParlaCAP performance directly transfers to TRL classification. Any claim that a TRL classifier can reach a specific macro-F1 should be treated as a project hypothesis requiring validation on Foerderkatalog or CORDIS-like labeled data, not as a finding from this paper.

## Links to canonical concept, method, dataset, synthesis, and project notes

- [[30_concepts/llm-annotation-and-automated-coding.md]]
- [[30_concepts/text-as-data-computational-social-science.md]]
- [[30_concepts/foundation-models-and-pretrained-transformers.md]]
- [[40_methods/xlm-roberta-multilingual-classification.md]]
- [[50_datasets/foerderkatalog-des-bundes.md]]
- [[50_datasets/cordis-horizon-europe-h2020.md]]
- [[70_projects/bundesinnovationshaushalt-trl.md]]
- [[90_synthesis/llm-text-classification-and-annotation.md]]
