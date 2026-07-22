---
title: "Selecting Between BERT and GPT for Text Classification in Political Science Research"
note_type: source_summary
summary: "Systematic comparison of fine-tuned BERT (RoBERTa-large) versus GPT-4o prompting for political science text classification at low training-data sizes."
authors:
  - Wang, Yu
  - Qu, Wen
  - Ye, Xin
year: 2024
source_files: ["10_sources/wang2024-bert-vs-gpt.md"]
source_urls:
  - https://arxiv.org/abs/2411.05050
projects:
  - bundesinnovationshaushalt-trl
tags:
  - source-summary
  - NLP
  - BERT
  - RoBERTa
  - GPT
  - text-classification
  - political-science
  - low-resource
updated: "2026-05-04"
---

# Wang, Qu, and Ye (2024) — BERT vs. GPT for Political Science Text Classification

## Source paper link/path

- Source file: `10_sources/wang2024-bert-vs-gpt.md`
- Source status: available as converted Markdown in `10_sources/`
- Semantic verification: locally checked against the listed source Markdown on 2026-05-04.

## Bibliographic metadata

- Title: "Selecting Between BERT and GPT for Text Classification in Political Science Research"
- Authors:
- Wang, Yu
- Year: 2024
- Venue/institution: not specified
- DOI/URL: not specified

## Detailed summary

Semantic verification against `10_sources/wang2024-bert-vs-gpt.md`: Political scientists often grapple with data scarcity in text classification. Recently, fine-tuned BERT models and their variants have gained traction as effective solutions to address this issue. In this study, we investigate the potential of GPT-based models combined with prompt engineering as a viable alternative. We conduct a series of experiments across various classification tasks, differing in the number of classes and complexity, to evaluate the effectiveness of BERT-based versus GPT-based models in low-data scenarios. Our findings indicate that while zero-shot and few-shot learning with GPT models provide reasonable performance and are well-suited for early-stage research exploration, they generally fall short — or, at best, match — the performance of BERT fine-tuning, particularly as the training set reaches a substantial size (e.g., 1,000 samples). We conclude by comparing these approaches in terms of performance, ease of use, and cost, providing practical guidance for researchers facing data limi- tations. Our results are particularly relevant for those engaged in quantitative text analysis in low-resource settings or with limited labeled data. For wiki use, this note should be retrieved for the source's own contribution, evidence, method, and policy mechanism. Broader implications for the Bundesinnovationshaushalt/TRL project are project interpretations unless the source itself states them explicitly.

## Research question

Source-grounded framing: Political scientists often grapple with data scarcity in text classification. Recently, fine-tuned BERT models and their variants have gained traction as effective solutions to address this issue.

## Core argument or contribution

In this study, we investigate the potential of GPT-based models combined with prompt engineering as a viable alternative. We conduct a series of experiments across various classification tasks, differing in the number of classes and complexity, to evaluate the effectiveness of BERT-based versus GPT-based models in low-data scenarios. Our findings indicate that while zero-shot and few-shot learning with GPT models provide reasonable performance and are well-suited for early-stage research exploration, they generally fall short — or, at best, match — the performance of BERT fine-tuning, particularly as the training set reaches a substantial size (e.g., 1,000 samples).

## Methodology

**BERT model:** RoBERTa-large (340 million parameters), fine-tuned at 200, 500, and 1,000 labeled samples; each condition run 3 times with different random seeds; mean, min, max reported - **GPT model:** GPT-4o, prompted with 0, 1, or 2 examples per class; temperatures 0.2 and 0.8 tested; each condition run 3 times - **Five tasks:** 1. Binary economic sentiment classification (news headlines, 2 classes) 2. Party manifesto classification (8 classes) 3. New Zealand parliamentary speech classification (8 classes) 4. COVID-19 policy measure classification (20 classes) 5. US State of the Union speech classification (22 classes) - **Metric:** Accuracy (all tasks)

## Datasets/materials used

Named datasets/materials discussed in the maintained note: [[50_datasets/cordis-horizon-europe-h2020.md]]; [[50_datasets/foerderkatalog-des-bundes.md]]. Use `10_sources/wang2024-bert-vs-gpt.md` for exact definitions, variable construction, sample period, and table/source-document provenance.

## Key findings

**Binary classification (2 classes, economic sentiment):** - BERT at 200 samples: 71.1%; BERT at 1,000 samples: 73.9% - GPT-4o zero-shot: 70.2%; GPT-4o two-shot: 73.8% - **Verdict:** GPT prompting matches BERT fine-tuning. Either approach works for 2-class tasks. **8-class manifesto classification:** - BERT at 200 samples: 53.9%; BERT at 1,000 samples: 58.2% - GPT-4o best (few-shot): 48.8% - **Verdict:** BERT wins by ~10 pp even at 200 training samples. **8-class parliamentary speech classification:** - BERT at 500 samples: 57.6%; BERT at 1,000 samples: 61.7% - GPT-4o prompting: 40.6–41.3% - **Verdict:** BERT is ~50% more accurate than GPT at 1,000 samples. **20-class COVID policy measure classification:** - BERT at 500 samples: 65.7%; BERT at 1,000 samples: 71.3%

## Limitations

The repair does not add limitations that are not visible in the source text. Treat the findings as bounded by the source's stated model, sample, period, country, task, or policy instrument, and check `10_sources/wang2024-bert-vs-gpt.md` before using precise quantitative or causal claims.

## Important concepts discussed

- [[30_concepts/technology-readiness-levels.md]]
- [[30_concepts/rd-subsidy-additionality.md]]
- [[30_concepts/llm-annotation-and-automated-coding.md]]
- [[30_concepts/text-as-data-computational-social-science.md]]
- [[30_concepts/foundation-models-and-pretrained-transformers.md]]

## Methods discussed

- [[40_methods/xlm-roberta-multilingual-classification.md]]
- [[40_methods/causal-evaluation-innovation-policy.md]]
- [[40_methods/trl-project-level-reporting.md]]
- [[40_methods/trl-klassifikation-pipeline.md]]

## Datasets discussed

- [[50_datasets/cordis-horizon-europe-h2020.md]]
- [[50_datasets/foerderkatalog-des-bundes.md]]

## Relation to other papers in the vault

This source should be read together with the linked canonical concept, method, dataset, synthesis, and project pages. During the 2026-05-04 audit, duplicate generic link lists were removed and links were restricted to retrieval-relevant wiki pages.

## Implications for LLM research or the project domain

**For TRL classification of German Foerderkatalog projects:** - This paper settles the BERT-vs-GPT question for our task. TRL classification is a 9-class (or 4-class BMLE) problem — squarely in the range where fine-tuned BERT dominates GPT prompting. - At 1,000 labeled CORDIS training examples, BERT at 8-class tasks outperforms GPT by roughly 10–20 pp. The gap is even larger for 20-class tasks at the same training size. - The "GPT as annotator" approach (used in Kuzman Pungeršek et al. 2025) is a different use case than GPT as classifier: using GPT to generate initial labels for unlabeled CORDIS data, which are then used to fine-tune XLM-RoBERTa, combines the best of both worlds. - The finding that BERT fine-tuning improves consistently with more training data (200 → 500 → 1,000) supports collecting as many labeled CORDIS examples as feasible, targeting at least 1,000. - For a fast first-pass check before building the full pipeline, GPT-4o zero-shot on a sample of Foerderkatalog projects may be useful for sanity-checking the classification scheme — but it should not replace fine-tuned XLM-RoBERTa for the final analysis.

## Links to canonical concept, method, dataset, synthesis, and project notes

- [[30_concepts/technology-readiness-levels.md]]
- [[40_methods/xlm-roberta-multilingual-classification.md]]
- [[50_datasets/cordis-horizon-europe-h2020.md]]
- [[20_summaries/kuzman2025-parlacap.md]]
- [[20_summaries/zhang2021-few-shot-bert.md]]
- [[30_concepts/rd-subsidy-additionality.md]]
- [[40_methods/causal-evaluation-innovation-policy.md]]
- [[70_projects/bundesinnovationshaushalt-trl.md]]
- [[40_methods/trl-project-level-reporting.md]]
- [[40_methods/trl-klassifikation-pipeline.md]]
- [[50_datasets/foerderkatalog-des-bundes.md]]
- [[30_concepts/llm-annotation-and-automated-coding.md]]
- [[30_concepts/text-as-data-computational-social-science.md]]
- [[30_concepts/foundation-models-and-pretrained-transformers.md]]

## Semantic verification details

Source identity was checked locally against `10_sources/wang2024-bert-vs-gpt.md` during the 2026-05-04 paper-by-paper verification pass. The maintained summary is tied to the source titled "Selecting Between BERT and GPT for Text Classification in Political Science Research" and should be used for the argument, method, findings, and limitations stated in that mapped source rather than for adjacent claims that only appear in project interpretation.

Verification synthesis: Semantic verification against `10_sources/wang2024-bert-vs-gpt.md`: Political scientists often grapple with data scarcity in text classification. Recently, fine-tuned BERT models and their variants have gained traction as effective solutions to address this issue. In this study, we investigate the potential of GPT-based models combined with prompt engineering as a viable alternative. We conduct a series of experiments across various classification tasks, differing in the number of classes and complexity, to evaluate the effectiveness of BERT-based versus GPT-based models in low-data scenarios. Our findings indicate that while zero-shot and few-shot learning with GPT models provide reasonable performance and are well-suited for early-stage research exploration, they generally fall short — or, at best, match — the performance of BERT fine-tuning, particularly as the training set reaches a substantial size (e.g., 1,000 samples). We conclude by comparing these approaches in terms of performance, ease of use, and cost, providing practical guidance for researchers facing data limi- tations. Our results are particularly relevant for those engaged

Method and materials check: **BERT model:** RoBERTa-large (340 million parameters), fine-tuned at 200, 500, and 1,000 labeled samples; each condition run 3 times with different random seeds; mean, min, max reported - **GPT model:** GPT-4o, prompted with 0, 1, or 2 examples per class; temperatures 0.2 and 0.8 tested; each condition run 3 times - **Five tasks:** 1. Binary economic sentiment classification (news headlines, 2 classes) 2. Party manifesto classification (8 classes) 3. New Zealand parliamentary speech classification (8 classes) 4. COVID-19 policy measure classification (20 classes) 5. US State of the Union speech Data/materials scope: Named datasets/materials discussed in the maintained note: [[50_datasets/cordis-horizon-europe-h2020.md]]; [[50_datasets/foerderkatalog-des-bundes.md]]. Use `10_sources/wang2024-bert-vs-gpt.md` for exact definitions, variable construction, sample period, and table/source-document provenance.

Finding-level check: **Binary classification (2 classes, economic sentiment):** - BERT at 200 samples: 71.1%; BERT at 1,000 samples: 73.9% - GPT-4o zero-shot: 70.2%; GPT-4o two-shot: 73.8% - **Verdict:** GPT prompting matches BERT fine-tuning. Either approach works for 2-class tasks. **8-class manifesto classification:** - BERT at 200 samples: 53.9%; BERT at 1,000 samples: 58.2% - GPT-4o best (few-shot): 48.8% - **Verdict:** BERT wins by ~10 pp even at 200 training samples. **8-class parliamentary speech classification:** - BERT at 500 samples: 57.6%; BERT at 1,000 samples: 61.7% - GPT-4o prompting: 40.6–41.3% - **Verdict:** BERT is ~50% more accurate than GPT at 1,000 samples. **20-class COVID policy measure classification:** - BERT at 500 samples: 65.7%; BERT at 1,000 samples: 71.3%

Citation and retrieval guardrails: use this note to retrieve the source together with its linked canonical concept, method, dataset, synthesis, and project pages. Do not cite it for technology-readiness, firm-selection, causal, benchmark-performance, or policy-design claims unless those claims are present in the verified summary sections above or directly in `10_sources/wang2024-bert-vs-gpt.md`. If a future draft needs exact quotations, sample definitions, coefficients, task metrics, or legal/institutional wording, reopen the source file before citation.
