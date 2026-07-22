---
title: "Automated Annotation with Generative AI Requires Validation"
note_type: source_summary
summary: "Pangakis, Wolken, and Fasching argue that LLM annotation can be useful for social-science text analysis only when validated task by task against high-quality human labels. Using GPT-4, they replicate 27 annotation tasks across 11 non-public social-science datasets, finding promising median performance but substantial heterogeneity, including several tasks with poor precision or recall. The paper contributes a five-step validation workflow, a consistency-score idea, and four use cases for LLM-assisted annotation."
authors: [Nicholas Pangakis, Samuel Wolken, Neil Fasching]
year: 2023
source_files: ["10_sources/pangakis2023-llm-annotation-validation.md"]
source_urls:
  - "https://arxiv.org/abs/2306.00176"
projects: [bundesinnovationshaushalt-trl]
tags:
  - source-summary
  - llm-annotation
  - validation
  - political-science
  - text-classification
updated: "2026-05-04"
---

# Pangakis, Wolken & Fasching (2023) - Automated Annotation with Generative AI Requires Validation

## Source paper link/path

- Source file: `10_sources/pangakis2023-llm-annotation-validation.md`
- Source status: available as converted Markdown in `10_sources/`
- Verification status: source-grounded rewrite completed against the local Markdown on 2026-05-04.

## Bibliographic metadata

- Title: "Automated Annotation with Generative AI Requires Validation"
- Authors: Nicholas Pangakis, Samuel Wolken, and Neil Fasching
- Date: June 2, 2023
- Version context: arXiv working paper `2306.00176`
- Software: `gpt_annotate` Python code released by the authors

## Detailed summary

The paper addresses a central problem in LLM-assisted social-science research: generative LLMs can quickly and cheaply annotate text, but performance varies enough that they cannot be trusted without task-specific validation. The authors push back against both overly optimistic and overly pessimistic conclusions from early LLM annotation studies. Their main claim is procedural: any automated annotation workflow using an LLM must validate the model's labels against a subset of high-quality human labels before using those labels at scale.

The motivation is that human annotation is costly and imperfect, but LLM annotation has its own risks. Human annotators can suffer from fatigue, limited attention, inconsistent category interpretation, and correlated errors. LLMs are faster and reproducible in a narrow operational sense, but they can fail because prompts are ambiguous, text data are noisy or idiosyncratic, concepts are difficult, or performance seen on public benchmark datasets reflects training-data contamination rather than true generalization.

The authors propose a five-step workflow. First, the researcher creates task-specific instructions or a codebook. Second, subject-matter experts annotate a random subset of text samples. Third, the LLM annotates a subset of the same human-labeled data using the same codebook, and performance is evaluated against the human labels with metrics such as accuracy, precision, recall, and F1. Fourth, if performance is low, the researcher refines the codebook to address misclassifications and may repeat human/LLM labeling as needed. Fifth, the final codebook is tested on the remaining held-out human-labeled samples, and only that held-out performance should determine how the LLM is used.

The validation study uses GPT-4 to replicate 27 annotation tasks from 11 non-public datasets used in recent high-impact social-science articles. The authors classify more than 200,000 text samples. They deliberately use non-public or restricted datasets to reduce benchmark-contamination concerns. Annotation tasks are harmonized into binary classification dimensions so that performance can be compared across settings.

The results are mixed in the way the authors expect. Overall performance is promising: across the 27 tasks, the paper reports median accuracy of 0.850 and median F1 of 0.707. But performance varies sharply across tasks. Nine of the 27 tasks have either precision or recall below 0.5. The authors therefore reject any blanket rule that LLMs are good enough or not good enough for annotation. Their conclusion is that LLM annotation can be valuable, but only if each task is validated on its own data and concept.

The paper also introduces a consistency score. The authors repeatedly classify each text sample at a nonzero temperature and treat the modal answer as the LLM label. The degree of consistency across repeated outputs is used as a signal of classification reliability. They report that higher consistency is correlated with a higher probability of a correct classification, so consistency can help identify edge cases or samples that should be prioritized for human review.

Finally, the paper identifies four use cases for LLM-assisted annotation, depending on validation performance: checking the quality of human-labeled data; identifying cases that humans should review; producing labeled data for fine-tuning and validating a supervised classifier; or classifying an entire corpus when validation performance is satisfactory.

## Research question

How can researchers use generative LLMs for automated text annotation in a way that is efficient but still valid, and how well does a validation-first workflow perform across diverse social-science annotation tasks?

## Core argument or contribution

The paper's core contribution is a validation-first workflow for LLM-assisted annotation. Its empirical contribution is showing that GPT-4 can perform well on many social-science annotation tasks, but that performance is heterogeneous enough to make task-specific validation mandatory. The practical contribution is a set of use cases and software for deciding whether an LLM should audit, triage, train, or fully label a corpus.

## Methodology

- Design of a five-step LLM annotation workflow grounded in human expert labels and codebook refinement.
- GPT-4 replication of 27 annotation tasks from 11 non-public datasets from high-impact social-science articles.
- More than 200,000 text samples classified.
- Binary-task harmonization for evaluation.
- Evaluation using accuracy, precision, recall, F1, and comparison with human-labeled ground truth.
- Repeated classification at temperature 0.6 to create a consistency score.

## Datasets/materials used

- Eleven non-public or restricted social-science datasets obtained from recent high-impact articles.
- Twenty-seven annotation tasks derived from those datasets.
- Human-labeled ground-truth labels from the original studies or subject-matter annotation.
- GPT-4 annotations generated under the authors' workflow.
- `gpt_annotate` software released by the authors.

The source does not use Foerderkatalog, CORDIS, or TRL data.

## Key findings

- LLM annotation performance is promising but highly task-dependent.
- Across 27 tasks, the paper reports median accuracy of 0.850 and median F1 of 0.707.
- Nine of the 27 tasks have either precision or recall below 0.5, demonstrating that some tasks fail badly enough to require human review, codebook revision, or abandonment of LLM labeling.
- Performance varies within and across datasets, so results from one annotation task cannot be assumed to transfer to another.
- Consistency across repeated LLM classifications is informative: higher consistency is associated with a higher probability that the predicted label is correct.
- The paper's recommended workflow foregrounds human judgment rather than replacing it: subject-matter experts create labels, LLMs are evaluated against those labels, and performance determines the use case.

## Limitations

- The study uses GPT-4 as the tested LLM; performance may differ for other proprietary or open-source models.
- The tasks come from social-science article datasets, not from German funding-project descriptions or TRL labels.
- Human labels are treated as validation ground truth, but human annotations can also contain error or conceptual ambiguity.
- The workflow reduces risk but does not remove prompt sensitivity, model-version dependence, black-box concerns, or training-data uncertainty.
- The consistency score is a useful triage signal, not a substitute for held-out human-label validation.

## Important concepts discussed

- [[30_concepts/llm-annotation-and-automated-coding.md]]
- [[30_concepts/text-as-data-computational-social-science.md]]
- [[30_concepts/foundation-models-and-pretrained-transformers.md]]
- Human-in-the-loop validation
- Codebook-based annotation
- Consistency score

## Methods discussed

- [[40_methods/llm-few-shot-social-science.md]]
- LLM annotation validation workflow
- Codebook refinement
- Held-out validation against human labels
- Consistency-score triage

## Datasets discussed

No canonical dataset note is linked. The paper uses 11 non-public/restricted social-science datasets and does not use this vault's Foerderkatalog or CORDIS datasets.

## Relation to other papers in the vault

This paper complements [[20_summaries/grimmer2013-text-as-data.md]] by operationalizing validation-first measurement for LLM annotation. It is a direct methodological complement to [[20_summaries/gilardi2023-chatgpt-annotation.md]], [[20_summaries/ornstein2025-stochastic-parrot.md]], [[20_summaries/halterman2025-codebook-llms.md]], [[20_summaries/moller2024-parrot-dilemma.md]], and [[20_summaries/ziems2024-llm-css-benchmark.md]]. Where Gilardi reports strong performance in selected annotation tasks, Pangakis et al. explain why every new task still needs validation.

## Implications for LLM research or the project domain

For [[70_projects/bundesinnovationshaushalt-trl.md]], this is one of the strongest methodological guardrails in the vault. Any LLM-based Foerderkatalog or TRL coding workflow should first create high-quality human labels, evaluate LLM predictions on held-out labels, inspect precision and recall by class, use consistency or confidence only as triage signals, and avoid deploying labels at scale if key classes perform poorly.

The paper does not provide evidence about Foerderkatalog, CORDIS, or technology-readiness distributions. Its implication is procedural: if the project wants LLM-coded TRL or policy categories, it needs a validation sample and task-specific performance reporting before treating labels as evidence.

## Links to canonical concept, method, dataset, synthesis, and project notes

- Concepts: [[30_concepts/llm-annotation-and-automated-coding.md]], [[30_concepts/text-as-data-computational-social-science.md]], [[30_concepts/foundation-models-and-pretrained-transformers.md]]
- Methods: [[40_methods/llm-few-shot-social-science.md]]
- Datasets: no canonical dataset note linked
- Synthesis: [[90_synthesis/llm-text-classification-and-annotation.md]]
- Project: [[70_projects/bundesinnovationshaushalt-trl.md]]
