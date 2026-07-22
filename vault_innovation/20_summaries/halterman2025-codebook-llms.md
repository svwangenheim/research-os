---
title: "Codebook LLMs: Evaluating LLMs as Measurement Tools for Political Science Concepts"
note_type: source_summary
summary: "Halterman and Keith (2025) evaluate whether open-weight LLMs can faithfully apply real political-science codebooks to text classification. They curate three codebook datasets covering US protest events, political violence in Pakistan, and party manifestos; propose a five-stage codebook-LLM measurement workflow; and show that current 7B-12B open-weight models often struggle in zero-shot codebook use, while supervised instruction tuning can substantially improve performance."
authors: ["Andrew Halterman", "Katherine A. Keith"]
year: 2025
source_files: ["10_sources/halterman2025-codebook-llms.md", "10_sources/halterman2025-codebook-llms.pdf"]
source_urls: []
projects:
  - bundesinnovationshaushalt-trl
related_concepts:
  - "[[30_concepts/llm-annotation-and-automated-coding.md]]"
  - "[[30_concepts/text-as-data-computational-social-science.md]]"
  - "[[30_concepts/foundation-models-and-pretrained-transformers.md]]"
related_methods:
  - "[[40_methods/llm-few-shot-social-science.md]]"
related_datasets: []
related_synthesis:
  - "[[90_synthesis/llm-text-classification-and-annotation.md]]"
tags:
  - source-summary
  - llm-annotation
  - codebooks
  - measurement-validity
  - instruction-tuning
  - political-science
updated: "2026-05-04"
---

# Halterman & Keith (2025) - Codebook LLMs

## Source paper link/path

- Source files: `10_sources/halterman2025-codebook-llms.md`, `10_sources/halterman2025-codebook-llms.pdf`
- Source status: available as converted Markdown in `10_sources/`; source identity verified against the title page and abstract during the 2026-05-04 one-by-one audit.

## Bibliographic metadata

- Title: "Codebook LLMs: Evaluating LLMs as Measurement Tools for Political Science Concepts"
- Authors: Andrew Halterman and Katherine A. Keith
- Year/version visible in source metadata: 2025 arXiv version
- Venue/institution: working paper / arXiv source in the vault

## Detailed summary

Halterman and Keith examine a measurement problem that sits between traditional political-science codebook coding and modern LLM classification. Social scientists often operationalize concepts through codebooks: documents that define categories, specify inclusion and exclusion rules, provide examples, and guide human annotators. LLM-based coding can scale this work, but the authors argue that simply giving an LLM labels or short descriptions risks measuring a broad background concept rather than the specific systematized construct in the codebook. For example, different datasets can define "protest" differently; an LLM may know the general concept but fail to follow the project-specific definition.

The paper's main contribution is a five-stage framework for codebook-LLM measurement. Stage 0 prepares the codebook in a semi-structured format that can be used by humans and machines, with standardized components such as definitions, clarifications, positive examples, negative examples, and output instructions. Stage 1 runs label-free behavioral tests before investing in new hand labels. These tests check whether an LLM returns legal labels, recovers verbatim definitions, classifies codebook examples, and remains invariant to the order of categories in the prompt. Stage 2 evaluates zero-shot measurement accuracy on a hand-coded evaluation set. Stage 3 performs zero-shot error analysis using behavioral tests that require labels, ablation of codebook components, and manual analysis of model outputs. Stage 4 uses supervised instruction tuning if zero-shot performance is inadequate.

The empirical demonstration uses three real-world political-science codebook datasets: the Crowd Counting Consortium (CCC) protest-events dataset for the United States, the BFRS political-violence dataset for Pakistan, and the Manifesto Project corpus. These are realistic and difficult codebook settings because they include domain-specific political concepts, long codebooks, and, in the Manifesto case, up to 142 classes. The authors format the tasks as single-label, multi-class classification and split data into train, development, and test sets.

The model comparison focuses on reproducible open-weight LLMs that can run on a consumer GPU: Mistral-7B-Instruct-v0.2, Mistral-NeMo-Instruct-2407, Llama-3.1-8B-Instruct, and OLMo-7B-0724-Instruct-hf. The authors emphasize that the point is not to crown a best model, since model capabilities change quickly, but to show how to evaluate whether a chosen LLM can follow a codebook.

The findings are cautionary for zero-shot use. In label-free behavioral tests on the BFRS codebook, several models can return legal labels and recover verbatim definitions/examples, but all models are sensitive to codebook order, suggesting attention or prompt-ordering problems. In labeled zero-shot evaluation, weighted F1 scores are modest or poor: around 0.57 for BFRS with Llama-8B in the authors' format, around 0.61-0.65 for CCC, and only around 0.15-0.21 for Manifestos depending on model and codebook format. Error analyses suggest that models can rely too much on label names rather than definitions and may fail when definitions conflict with a model's pretrained background concept.

The paper then shows that supervised instruction tuning can substantially improve performance, by up to 55 percent in the authors' demonstration. This supports a practical conclusion: for complex political-science codebooks, off-the-shelf zero-shot LLMs are not automatically reliable measurement tools. Researchers should test basic codebook-following behavior, evaluate against labels, inspect errors, and be prepared to fine-tune or otherwise adapt the model when zero-shot performance is insufficient.

## Research question

Can off-the-shelf open-weight LLMs faithfully follow real political-science codebooks when measuring complex concepts in text, and what workflow should researchers use to evaluate and improve codebook-based LLM measurement?

## Core argument or contribution

The core argument is that codebook-based LLM measurement must be evaluated as a measurement problem, not just a text-classification convenience. LLMs may recognize broad concepts from pretraining while failing to follow the specific operational definitions in a research codebook. The paper contributes curated codebook datasets, a five-stage evaluation framework, behavioral tests, and evidence that supervised instruction tuning can substantially improve weak zero-shot performance.

## Methodology

- Methodological framework plus empirical demonstration.
- Three curated codebook datasets: CCC protest events, BFRS political violence in Pakistan, and Manifesto Project quasi-sentence labels.
- Single-label, multi-class classification setup with train/development/test splits.
- Open-weight model evaluation using Mistral-7B, Mistral-NeMo-12B, Llama-8B, and OLMo-7B.
- Label-free behavioral tests for legal labels, definition recovery, in-context example recovery, and codebook-order invariance.
- Labeled zero-shot evaluation with weighted F1 scores and bootstrap confidence intervals.
- Labels-required behavioral tests for exclusion criteria, generic labels, and swapped labels.
- Codebook-component ablation and manual output/error analysis.
- Parameter-efficient supervised instruction tuning on human-coded examples.

## Datasets/materials used

The source uses three political-science codebook datasets: Crowd Counting Consortium (CCC) data on protest events in the United States, BFRS data on political violence in Pakistan, and the Manifesto Project corpus. It uses original codebooks, source texts, human labels, and curated train/development/test splits. It does not use Foerderkatalog, CORDIS, the European Innovation Scoreboard, TRL data, German innovation-policy datasets, or patent datasets.

## Key findings

- Real codebook-LLM tasks are harder than short-label classification because the model must follow a project-specific operationalization, not just the label's ordinary meaning.
- The proposed workflow has five stages: codebook preparation, label-free behavioral testing, labeled zero-shot evaluation, zero-shot error analysis, and supervised instruction tuning.
- Open-weight LLMs can pass simple legal-label and verbatim-recovery tests yet still be sensitive to codebook order.
- Zero-shot weighted F1 is weak to moderate in the empirical demonstration: better for CCC, lower for BFRS, and poor for the 142-class Manifesto task.
- Behavioral tests show that models can rely too heavily on label semantics and insufficiently on definitions.
- Codebook ablations indicate that codebook components matter, but the best component mix may be task-specific.
- Supervised instruction tuning can substantially improve performance, reportedly by up to 55 percent.
- The paper does not recommend one universal best LLM; it recommends an evaluation workflow for each codebook-measurement project.

## Limitations

The empirical demonstration is limited to three English-language political-science codebook datasets and a set of 7B-12B open-weight models available at the time of the study. Results may differ with larger closed models, different languages, different codebook complexity, or different prompting/engineering choices. The paper focuses on measurement accuracy and codebook compliance; downstream statistical inference with noisy labels still requires additional methods such as those discussed by Egami et al. The source is not an evaluation of German TRL classification or innovation-policy data.

## Important concepts discussed

- [[30_concepts/llm-annotation-and-automated-coding.md]]
- [[30_concepts/text-as-data-computational-social-science.md]]
- [[30_concepts/foundation-models-and-pretrained-transformers.md]]
- Measurement validity
- Codebook operationalization
- Background concept versus systematized construct
- Codebook-following behavior
- Instruction tuning

## Methods discussed

- Codebook-based LLM measurement
- Zero-shot multi-class classification
- Label-free behavioral tests
- Labels-required behavioral tests
- Codebook-order invariance tests
- Generic-label and swapped-label tests
- Codebook ablation
- Manual error analysis
- Parameter-efficient supervised instruction tuning
- [[40_methods/llm-few-shot-social-science.md]] as the closest canonical LLM annotation method note, although this source emphasizes codebook evaluation and instruction tuning more than few-shot prompting

## Datasets discussed

- Crowd Counting Consortium (CCC) protest-event dataset
- BFRS political-violence dataset for Pakistan
- Manifesto Project corpus
- Curated codebook/source-text/human-label datasets released by the authors

## Relation to other papers in the vault

This paper extends the validation logic of [[20_summaries/grimmer2013-text-as-data.md]] to codebook-following LLMs. It complements [[20_summaries/gilardi2023-chatgpt-annotation.md]] by showing that stronger performance on simpler or shorter-label tasks does not guarantee faithful measurement with long, complex codebooks. It connects closely to [[20_summaries/egami2024-llm-annotation-framework.md]]: Halterman and Keith focus on improving and validating the measurement step, while Egami et al. focus on downstream inference when predicted labels remain noisy.

## Implications for LLM research or the project domain

For the Bundesinnovationshaushalt/TRL project, the paper is directly relevant to TRL and topic-codebook design. A TRL scale is a codebook-like measurement instrument, so the project should not assume that an LLM will follow official definitions just because the prompt lists TRL labels. The project should prepare a machine-readable codebook with definitions, clarifications, boundary cases, positive and negative examples, and output constraints; run label-free checks; validate against human-coded examples; inspect systematic errors; and consider supervised adaptation if zero-shot performance is weak. This supports a stricter standard than simply writing a prompt and spot-checking outputs.

## Links to canonical concept, method, dataset, synthesis, and project notes

- Concepts: [[30_concepts/llm-annotation-and-automated-coding.md]], [[30_concepts/text-as-data-computational-social-science.md]], [[30_concepts/foundation-models-and-pretrained-transformers.md]]
- Methods: [[40_methods/llm-few-shot-social-science.md]]
- Datasets: no canonical vault dataset note applies directly
- Projects: [[70_projects/bundesinnovationshaushalt-trl.md]]
- Synthesis: [[90_synthesis/llm-text-classification-and-annotation.md]]
