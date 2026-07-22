---
title: "LLM Text Classification and Annotation"
note_type: synthesis
summary: "Cross-paper synthesis for the vault's LLM/text-as-data evidence: when LLMs can annotate research texts, how they compare with BERT-family classifiers and human coders, and what validation is required for the Foerderkatalog TRL workflow."
projects:
  - "[[70_projects/bundesinnovationshaushalt-trl.md]]"
included_notes:
  - "[[20_summaries/grimmer2013-text-as-data.md]]"
  - "[[20_summaries/brown2020-gpt3-fewshot.md]]"
  - "[[20_summaries/devlin2019-bert.md]]"
  - "[[20_summaries/conneau2020-xlm-roberta.md]]"
  - "[[20_summaries/gilardi2023-chatgpt-annotation.md]]"
  - "[[20_summaries/egami2024-llm-annotation-framework.md]]"
  - "[[20_summaries/halterman2025-codebook-llms.md]]"
  - "[[20_summaries/pangakis2023-llm-annotation-validation.md]]"
  - "[[20_summaries/ziems2024-llm-css-benchmark.md]]"
  - "[[20_summaries/wang2024-bert-vs-gpt.md]]"
related_concepts:
  - "[[30_concepts/llm-annotation-and-automated-coding.md]]"
  - "[[30_concepts/text-as-data-computational-social-science.md]]"
  - "[[30_concepts/foundation-models-and-pretrained-transformers.md]]"
  - "[[30_concepts/technology-readiness-levels.md]]"
related_methods:
  - "[[40_methods/llm-few-shot-social-science.md]]"
  - "[[40_methods/llm-few-shot-applicability-trl-förderkatalog.md]]"
  - "[[40_methods/xlm-roberta-multilingual-classification.md]]"
  - "[[40_methods/trl-klassifikation-pipeline.md]]"
related_datasets:
  - "[[50_datasets/foerderkatalog-des-bundes.md]]"
  - "[[50_datasets/cordis-horizon-europe-h2020.md]]"
tags:
  - synthesis
  - llm
  - text-classification
  - annotation
updated: "2026-04-29"
---

# LLM Text Classification and Annotation

## Scope

This synthesis connects the vault's LLM annotation, text-as-data, foundation-model, and TRL-classification evidence. It is the retrieval hub for questions about whether LLMs can classify research texts, how LLM prompting compares with BERT-family fine-tuning, what validation is required, and how this applies to German Foerderkatalog TRL classification.

## Main synthesis

The literature supports a cautious but usable position: LLMs and pretrained transformers can classify social-science and policy text at useful quality, but they only become research-grade when the task is carefully defined, validated against independent human judgment, and interpreted as measurement rather than ground truth.

[[20_summaries/grimmer2013-text-as-data.md]] provides the older methodological rule: automated text analysis must be validated because no method is universally best. [[20_summaries/devlin2019-bert.md]] and [[20_summaries/conneau2020-xlm-roberta.md]] provide the pretrained-transformer base for supervised and multilingual classification. [[20_summaries/brown2020-gpt3-fewshot.md]] opens the few-shot prompting route: large language models can perform tasks from instructions and examples without gradient updates.

The newer LLM annotation papers test what that means for social science. [[20_summaries/gilardi2023-chatgpt-annotation.md]] and [[20_summaries/tornberg2025-llm-outperform-experts.md]] show that LLMs can match or outperform crowd workers and sometimes expert coders. [[20_summaries/egami2024-llm-annotation-framework.md]], [[20_summaries/pangakis2023-llm-annotation-validation.md]], and [[20_summaries/ziems2024-llm-css-benchmark.md]] keep the stronger methodological constraint: LLM labels must be validated, rare classes need calibration, and downstream analysis must account for measurement error. [[20_summaries/halterman2025-codebook-llms.md]] adds that the codebook and label definitions are not documentation afterthoughts; they are part of model performance.

For the Bundesinnovationshaushalt project, the practical implication is a two-path design. LLM few-shot classification is attractive because the Foerderkatalog corpus is large, German-language, and weakly labeled. XLM-RoBERTa is attractive as a robustness path because CORDIS provides project-level labels and multilingual transfer is a plausible bridge. Neither path eliminates the need for a manually validated German sample.

## Agreements across papers

- Text classification is a measurement problem, not only a prediction problem.
- Human validation remains necessary even when model performance is high.
- Codebooks, label boundaries, examples, and prompt structure materially affect classification quality.
- LLMs reduce annotation cost and can make large-scale coding feasible.
- Model outputs should be reported with uncertainty, error analysis, and class-specific performance.

## Tensions and disagreements

- Some papers emphasize LLMs outperforming humans; others emphasize hidden instability, bias, and calibration problems.
- BERT-family fine-tuning can outperform GPT-style models for many-class classification when enough labeled data exist, while LLM prompting is better when labeled data are scarce or concepts need rich natural-language definitions.
- Crowd annotation, expert annotation, and LLM annotation each fail differently; no one source of labels is automatically the gold standard.
- LLM-generated labels can scale analysis, but if they are reused to train other models they may propagate LLM-specific biases.

## Implications for the Bundesinnovationshaushalt project

The TRL workflow should treat [[30_concepts/technology-readiness-levels.md]] as the construct, [[50_datasets/foerderkatalog-des-bundes.md]] as the target corpus, and [[50_datasets/cordis-horizon-europe-h2020.md]] as the main external training/reference source. The core method notes are [[40_methods/llm-few-shot-social-science.md]], [[40_methods/llm-few-shot-applicability-trl-förderkatalog.md]], [[40_methods/xlm-roberta-multilingual-classification.md]], and [[40_methods/trl-klassifikation-pipeline.md]].

Policy claims should be staged:

1. Descriptive retrieval and exploratory coding can rely on LLM labels with transparent caveats.
2. Working-paper claims about TRL distribution need human validation and class-specific error reporting.
3. Strong claims about policy allocation should combine TRL labels with recipient type, ministry, technology field, and possibly evaluation evidence.

## Open questions

- What minimum German human-validation sample is enough for credible TRL claims?
- Should the validation sample oversample early TRL classes because they are rarer and more ambiguous?
- Are short Foerderkatalog project descriptions sufficiently informative for detailed TRL 1-9 labels, or should reporting focus on broader TRL groups?
- Does XLM-R transfer from English CORDIS labels to German Foerderkatalog descriptions without systematic maturity bias?
- How should disagreement between LLM labels, XLM-R labels, and human labels be resolved?

## Retrieval map

| Query | Expected retrieval |
| --- | --- |
| "LLM annotation social science validation" | [[30_concepts/llm-annotation-and-automated-coding.md]], [[40_methods/llm-few-shot-social-science.md]], this synthesis |
| "text-as-data validate validate validate" | [[30_concepts/text-as-data-computational-social-science.md]], [[20_summaries/grimmer2013-text-as-data.md]], this synthesis |
| "BERT versus GPT text classification" | [[30_concepts/foundation-models-and-pretrained-transformers.md]], [[20_summaries/wang2024-bert-vs-gpt.md]], [[40_methods/xlm-roberta-multilingual-classification.md]] |
| "Foerderkatalog TRL LLM classification" | [[70_projects/bundesinnovationshaushalt-trl.md]], [[40_methods/trl-klassifikation-pipeline.md]], [[40_methods/llm-few-shot-applicability-trl-förderkatalog.md]], this synthesis |
| "LLM codebook prompting" | [[20_summaries/halterman2025-codebook-llms.md]], [[30_concepts/llm-annotation-and-automated-coding.md]], [[40_methods/llm-few-shot-social-science.md]] |

## Maintenance needs

Update this synthesis when new LLM annotation, text-as-data, classifier validation, benchmark, or Foerderkatalog TRL workflow notes are added. Any new method note in this cluster should link back here and to the three canonical concepts: [[30_concepts/llm-annotation-and-automated-coding.md]], [[30_concepts/text-as-data-computational-social-science.md]], and [[30_concepts/foundation-models-and-pretrained-transformers.md]].
