---
title: "LLM Few-Shot Classification in Social Science"
note_type: method
summary: "Best practices for using large language models (LLMs) for text annotation and classification in social science research. Covers prompt design, few-shot exemplar selection, validation protocols (Cohen's Kappa), calibration, and integration with downstream analysis. Synthesizes guidance from Grimmer & Stewart (2013), Gilardi et al. (2023), Egami et al. (2024), Ornstein et al. (2025)."
related_notes:
  - "20_summaries/grimmer2013-text-as-data.md"
  - "20_summaries/gilardi2023-chatgpt-annotation.md"
  - "20_summaries/egami2024-llm-annotation-framework.md"
  - "20_summaries/ornstein2025-stochastic-parrot.md"
  - "20_summaries/pangakis2023-llm-annotation-validation.md"
  - "20_summaries/halterman2025-codebook-llms.md"
  - "20_summaries/ziems2024-llm-css-benchmark.md"
  - "20_summaries/pelaez2024-patent-public-value-llm.md"
  - "20_summaries/tornberg2025-llm-outperform-experts.md"
  - "20_summaries/brown2020-gpt3-fewshot.md"
  - "20_summaries/chae2025-llm-instruction-tuning.md"
  - "20_summaries/alizadeh2025-opensource-llm-annotation.md"
  - "20_summaries/moller2024-parrot-dilemma.md"
  - "20_summaries/snow2008-cheap-fast-annotation.md"
projects: [bundesinnovationshaushalt-trl]
tags:
  - method
  - llm
  - text-classification
  - few-shot
  - annotation
  - validation
updated: "2026-04-22"
---

# LLM Few-Shot Classification in Social Science

## Overview

Large language models (LLMs) are increasingly used for text classification tasks in social science research. The approach replaces traditional supervised classification (requiring large labeled datasets) or manual crowd-sourcing with in-context learning: providing the LLM with a task description, label definitions, and a small number of examples (few-shot), then asking it to classify new texts.

## When to Use

**LLM annotation is appropriate when:**
- Labeled data is insufficient for training a specialized classifier (< 500 examples)
- Task has clear, discrete label definitions (not highly interpretive)
- Cross-lingual classification is needed without parallel training data
- Speed or cost prevents manual annotation at scale
- Domain vocabulary can be conveyed via few-shot examples

**Prefer supervised fine-tuning when:**
- Labeled data is large (> 5,000 examples) and task-specific performance is critical
- Annotation consistency across many runs is paramount (fine-tuned models are deterministic)
- Cost per query is prohibitive (very large corpus + expensive API)

## Prompt Architecture (Best Practice)

Based on Halterman et al. (2025), Ornstein et al. (2025), Egami et al. (2024):

```
[SYSTEM ROLE]
You are an expert at classifying [domain] text. 
Your task is to assign [label set] to each input.

[TASK DESCRIPTION]
Classify the following [text type] according to the [label set]:
[Label 1]: [Definition] — [key characteristics]
[Label 2]: [Definition] — [key characteristics]
...

[FEW-SHOT EXAMPLES]
---
Text: [Example 1 from domain]
Label: [Label A]
Reasoning: [brief chain-of-thought]
---
Text: [Example 2 from domain]
Label: [Label B]
...

[CLASSIFICATION INSTRUCTION]
Now classify the following text. Think step-by-step, 
then provide your answer in JSON format: 
{"label": "...", "confidence": 0.0-1.0, "reasoning": "..."}

Text: {input_text}
```

**Key design choices:**
- Use instruction-tuned models (not base models) — Chae & Davidson (2025)
- Include ≥1 example per label category — Chae & Davidson (2025)
- Use chain-of-thought ("think step-by-step") for complex tasks — Ornstein et al. (2025)
- Request confidence score for borderline case identification
- Set temperature=0 for reproducibility

## Few-Shot Exemplar Selection

- Select from domain-specific labeled data (if available); do not use generic examples
- Balance: include at least 1 example per label (especially rare categories)
- Select clear, unambiguous exemplars — avoid borderline cases for exemplars
- **For TRL classification:** Use CORDIS-labeled EU projects as exemplars (same domain, English; cross-lingual transfer via XLM-R or multilingual LLMs)

## Validation Protocol

Mandatory validation before deploying LLM annotations in downstream analysis (Grimmer & Stewart 2013, Egami et al. 2024):

1. **Sample size:** Stratified random sample of ≥ 300-600 texts (stratify by expected label distribution)
2. **Human annotation:** 2+ independent human annotators (domain experts, not crowd workers for complex tasks)
3. **Agreement metric:** Cohen's Kappa (κ) for categorical labels; report both human-human κ and human-LLM κ
4. **Thresholds:** κ ≥ 0.60 = substantial agreement (minimum acceptable); κ ≥ 0.80 = near-perfect (preferred)
5. **Error analysis:** Examine which labels LLM confuses; identify systematic patterns
6. **Calibration check:** Compare LLM aggregate label distribution to human aggregate — correct for systematic over/underclassification
7. **Multi-prompt testing:** Run 2-3 prompt variants; report variation (Pangakis et al. 2023)

## Common Failure Modes and Mitigations

| Failure Mode | Detection | Mitigation |
|-------------|-----------|------------|
| Class imbalance bias | Compare LLM distribution vs. human distribution | Few-shot examples for rare classes; calibration |
| Prompt sensitivity | Run multiple prompt variants; measure variance | Test 2-3 phrasings; average or select most stable |
| Run inconsistency | Test with temperature=0; compare multiple runs | Always use temperature=0; or majority vote |
| Domain vocabulary gap | Error analysis on rare technical terms | Few-shot from target domain; domain-specific model |
| Parrot dilemma (Møller 2024) | Compare LLM labels to human labels on test set | Human gold standard must be independent of LLM |

## Application: TRL Classification of Förderkatalog

**Setup (Script 07):**
- Model: Claude Haiku (instruction-tuned, API)
- Labels: TRL 1-3 (Basic Research), TRL 4-6 (Industrial Research), TRL 7-9 (Experimental Development); + detailed TRL 1-9
- Few-shot exemplars: 3 examples per TRL group from CORDIS training data (9 total)
- Input: FK "Thema" + "Leistungsplansystematik" field
- Output: JSON {trl_group, trl_score, key_tech, confidence}
- Temperature: 0.0
- Validation: 600-project stratified sample, 2 human annotators (Script 08)

**Robustness check:** XLM-RoBERTa fine-tuned on CORDIS (1,846 labeled EU projects), applied to FK via cross-lingual transfer.

## Cost Estimates

| Approach | Cost (39,555 FK projects) | Quality |
|----------|--------------------------|---------|
| Claude Haiku (API) | ~€15-20 | High |
| GPT-4o-mini | ~€10-15 | High |
| Open-source (Llama local) | €0 + compute | Moderate |
| Manual annotation | €80k-150k | Reference |

## What it does

This method note defines how to use LLMs for social-science text annotation and
classification with few-shot examples, structured prompts, validation, and
calibration checks.

## Assumptions

- The codebook has clear labels and scope boundaries.
- The validation set is independent of the LLM output.
- Downstream analysis accounts for classification error and uncertainty.

## Papers using or discussing this method

Key sources include [[20_summaries/gilardi2023-chatgpt-annotation.md]],
[[20_summaries/egami2024-llm-annotation-framework.md]],
[[20_summaries/halterman2025-codebook-llms.md]],
[[20_summaries/ornstein2025-stochastic-parrot.md]], and
[[20_summaries/snow2008-cheap-fast-annotation.md]].

## Strengths and limitations

LLM annotation is fast and inexpensive, but it is sensitive to prompt design,
model choice, label imbalance, and calibration. It should support, not replace,
validation and transparent measurement design.

## Related concepts and datasets

- [[30_concepts/llm-annotation-and-automated-coding.md]]
- [[30_concepts/text-as-data-computational-social-science.md]]
- [[30_concepts/foundation-models-and-pretrained-transformers.md]]
- [[90_synthesis/llm-text-classification-and-annotation.md]]
- [[40_methods/trl-klassifikation-pipeline.md]]
- [[40_methods/llm-few-shot-applicability-trl-förderkatalog.md]]
- [[50_datasets/foerderkatalog-des-bundes.md]]
- [[50_datasets/cordis-horizon-europe-h2020.md]]

## Links
- [[40_methods/llm-few-shot-applicability-trl-förderkatalog.md]]
- [[40_methods/trl-klassifikation-pipeline.md]]
- [[40_methods/xlm-roberta-multilingual-classification.md]]
- [[30_concepts/technology-readiness-levels.md]]
- [[70_projects/bundesinnovationshaushalt-trl.md]]
