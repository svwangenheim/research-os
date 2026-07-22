---
title: "Behind the Mask: Random and Selective Masking in Transformer Models Applied to Specialized Social Science Texts"
note_type: source_summary
summary: "Systematic test of how changing the masking rate during BERT/RoBERTa pre-training affects classification performance on social science text."
authors:
  - Timoneda, Joan C.
  - Vallejo Vera, Sebastián
year: 2025
source_files: ["10_sources/timoneda2025b-behind-the-mask.md"]
source_urls:
  - https://doi.org/10.1371/journal.pone.0318421
projects:
  - bundesinnovationshaushalt-trl
tags:
  - source-summary
  - NLP
  - BERT
  - RoBERTa
  - masking
  - MLM
  - classification
  - social-science
updated: "2026-05-04"
---

# Timoneda and Vallejo Vera (2025b) — Behind the Mask

## Source paper link/path

- Source file: `10_sources/timoneda2025b-behind-the-mask.md`
- Source status: available as converted Markdown in `10_sources/`
- Semantic verification: locally checked against the listed source Markdown on 2026-05-04.

## Bibliographic metadata

- Title: "Behind the Mask: Random and Selective Masking in Transformer Models Applied to Specialized Social Science Texts"
- Authors:
- Timoneda, Joan C.
- Year: 2025
- Venue/institution: not specified
- DOI/URL: not specified

## Detailed summary

Semantic verification against `10_sources/timoneda2025b-behind-the-mask.md`: Transformer models such as BERT and RoBERTa are increasingly popular in the social sciences to generate data through supervised text classification. These models can be further trained through Masked Language Modeling (MLM) to increase performance in specialized applications. MLM uses a default masking rate of 15 percent, and few works have investigated how different masking rates may affect performance. Importantly, there are no systematic tests on whether selectively masking certain words improves classi- fier accuracy. In this article, we further train a set of models to classify fake news around the coronavirus pandemic using 15, 25, 40, 60 and 80 percent random and selective masking. The authors find that a masking rate of 40 percent, both random and selective, improves within-category performance but has little impact on overall performance. This finding has important implications for scholars looking to build BERT and RoBERTa classifiers, especially those where one specific category is more relevant to their research. For wiki use, this note should be retrieved for the source's own contribution, evidence, method, and policy mechanism. Broader implications for the Bundesinnovationshaushalt/TRL project are project interpretations unless the source itself states them explicitly.

## Research question

Source-grounded framing: Transformer models such as BERT and RoBERTa are increasingly popular in the social sciences to generate data through supervised text classification. These models can be further trained through Masked Language Modeling (MLM) to increase performance in specialized applications.

## Core argument or contribution

MLM uses a default masking rate of 15 percent, and few works have investigated how different masking rates may affect performance. Importantly, there are no systematic tests on whether selectively masking certain words improves classi- fier accuracy. In this article, we further train a set of models to classify fake news around the coronavirus pandemic using 15, 25, 40, 60 and 80 percent random and selective masking.

## Methodology

**Model:** RoBERTa-large, further pre-trained on COVID-19-domain text (6,079 academic abstracts + 4.8 million tweets), then fine-tuned for 3-class classification (fake / true / undetermined news) - **Dataset for fine-tuning:** 7,179 labeled news headlines and tweets (3,681 fake, 1,878 true, 1,620 undetermined); 500 per category used for fine-tuning - **Masking rates tested:** 15%, 25%, 40%, 60%, 80% — both fully random and selective - **Selective masking:** masks the same percentage of random tokens plus the same percentage of occurrences of specific domain tokens ("covid," "coronavirus") - **Evaluation:** 10-times repeated 10-fold cross-validation; F1 scores reported per category and overall - **Baselines:** Original BERT-large and RoBERTa-large at 15% masking

## Datasets/materials used

Named datasets/materials discussed in the maintained note: [[50_datasets/cordis-horizon-europe-h2020.md]]; [[50_datasets/foerderkatalog-des-bundes.md]]. Use `10_sources/timoneda2025b-behind-the-mask.md` for exact definitions, variable construction, sample period, and table/source-document provenance.

## Key findings

**Random masking results (F1 scores):** | Masking rate | Fake F1 | True F1 | Undetermined F1 | Overall F1 | |---|---|---|---|---| | 15% (default) | 0.848 | 0.811 | 0.767 | 0.809 | | 25% | 0.847 | 0.797 | 0.767 | 0.804 | | **40%** | **0.857** | 0.800 | 0.767 | 0.808 | | 60% | 0.852 | 0.802 | 0.770 | 0.808 | | 80% | 0.848 | 0.796 | 0.767 | 0.805 | | BERT-large baseline | 0.782 | 0.772 | 0.724 | 0.760 | | RoBERTa-large baseline | 0.819 | 0.783 | 0.742 | 0.781 | **Selective masking:** At 40%, the fake-category F1 reaches 0.858, slightly exceeding the random 40% (0.857). The gain relative to baseline is concentrated in the target category (fake news). **Key conclusions:** 1. Overall performance differences across masking rates are small and not statistically significant — the original 15% choice is defensible for overall accuracy. 2. Category-specific performance (the metric that matters when you care about one label) improves with 40% masking: +0.9 pp for the fake category versus default 15%.

## Limitations

The repair does not add limitations that are not visible in the source text. Treat the findings as bounded by the source's stated model, sample, period, country, task, or policy instrument, and check `10_sources/timoneda2025b-behind-the-mask.md` before using precise quantitative or causal claims.

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
- [[40_methods/llm-few-shot-social-science.md]]

## Datasets discussed

- [[50_datasets/cordis-horizon-europe-h2020.md]]
- [[50_datasets/foerderkatalog-des-bundes.md]]

## Relation to other papers in the vault

This source should be read together with the linked canonical concept, method, dataset, synthesis, and project pages. During the 2026-05-04 audit, duplicate generic link lists were removed and links were restricted to retrieval-relevant wiki pages.

## Implications for LLM research or the project domain

**For TRL classification of German Foerderkatalog projects:** - The paper shows that the domain-adaptive pre-training step (Step 2 in the standard BERT pipeline) can be tuned via masking rate. If we further pre-train XLM-RoBERTa on CORDIS text before fine-tuning on TRL labels, the masking rate matters at the category level. - TRL classification is exactly the type of problem where category-specific performance is what matters: we likely care more about correctly identifying TRL 1–2 (basic research) than about aggregate accuracy, since these categories may be the rarest and most important for policy conclusions. - The paper recommends testing multiple masking rates (15%, 25%, 40%) during domain pre-training and selecting based on category-level F1, not just overall F1. This is a low-cost tuning step. - The selective masking idea (masking domain keywords more often) could apply to CORDIS-specific vocabulary ("proof of concept," "technology readiness," "laboratory prototype") — but this is optional and the gains are modest. - The further pre-training data for this project would be CORDIS project objective texts (English) — potentially millions of words of EU R&D vocabulary. **Practical recommendation:** When running domain-adaptive pre-training of XLM-RoBERTa on CORDIS text, test masking rates of 15%, 25%, and 40%. Use category-level F1 (not overall accuracy) to select the best masking rate. Expect the biggest gains in whichever TRL category has the lowest baseline performance.

## Links to canonical concept, method, dataset, synthesis, and project notes

- [[30_concepts/technology-readiness-levels.md]]
- [[40_methods/xlm-roberta-multilingual-classification.md]]
- [[50_datasets/cordis-horizon-europe-h2020.md]]
- [[20_summaries/trucco2025-scaling-up-ideas.md]]
- [[30_concepts/rd-subsidy-additionality.md]]
- [[40_methods/causal-evaluation-innovation-policy.md]]
- [[70_projects/bundesinnovationshaushalt-trl.md]]
- [[40_methods/trl-project-level-reporting.md]]
- [[40_methods/trl-klassifikation-pipeline.md]]
- [[50_datasets/foerderkatalog-des-bundes.md]]
- [[30_concepts/llm-annotation-and-automated-coding.md]]
- [[30_concepts/text-as-data-computational-social-science.md]]
- [[30_concepts/foundation-models-and-pretrained-transformers.md]]
- [[40_methods/llm-few-shot-social-science.md]]

## Semantic verification details

Source identity was checked locally against `10_sources/timoneda2025b-behind-the-mask.md` during the 2026-05-04 paper-by-paper verification pass. The maintained summary is tied to the source titled "Behind the Mask: Random and Selective Masking in Transformer Models Applied to Specialized Social Science Texts" and should be used for the argument, method, findings, and limitations stated in that mapped source rather than for adjacent claims that only appear in project interpretation.

Verification synthesis: Semantic verification against `10_sources/timoneda2025b-behind-the-mask.md`: Transformer models such as BERT and RoBERTa are increasingly popular in the social sciences to generate data through supervised text classification. These models can be further trained through Masked Language Modeling (MLM) to increase performance in specialized applications. MLM uses a default masking rate of 15 percent, and few works have investigated how different masking rates may affect performance. Importantly, there are no systematic tests on whether selectively masking certain words improves classi- fier accuracy. In this article, we further train a set of models to classify fake news around the coronavirus pandemic using 15, 25, 40, 60 and 80 percent random and selective masking. The authors find that a masking rate of 40 percent, both random and selective, improves within-category performance but has little impact on overall performance. This finding has important implications for scholars looking to build BERT and RoBERTa classifiers, especially those where one specific category is more relevant to their research. For

Method and materials check: **Model:** RoBERTa-large, further pre-trained on COVID-19-domain text (6,079 academic abstracts + 4.8 million tweets), then fine-tuned for 3-class classification (fake / true / undetermined news) - **Dataset for fine-tuning:** 7,179 labeled news headlines and tweets (3,681 fake, 1,878 true, 1,620 undetermined); 500 per category used for fine-tuning - **Masking rates tested:** 15%, 25%, 40%, 60%, 80% — both fully random and selective - **Selective masking:** masks the same percentage of random tokens plus the same percentage of occurrences of specific domain tokens ("covid," "coronavirus") - **Evaluation:** 10-times repeated 10-fold cross-validation; Data/materials scope: Named datasets/materials discussed in the maintained note: [[50_datasets/cordis-horizon-europe-h2020.md]]; [[50_datasets/foerderkatalog-des-bundes.md]]. Use `10_sources/timoneda2025b-behind-the-mask.md` for exact definitions, variable construction, sample period, and table/source-document provenance.

Finding-level check: **Random masking results (F1 scores):** | Masking rate | Fake F1 | True F1 | Undetermined F1 | Overall F1 | |---|---|---|---|---| | 15% (default) | 0.848 | 0.811 | 0.767 | 0.809 | | 25% | 0.847 | 0.797 | 0.767 | 0.804 | | **40%** | **0.857** | 0.800 | 0.767 | 0.808 | | 60% | 0.852 | 0.802 | 0.770 | 0.808 | | 80% | 0.848 | 0.796 | 0.767 | 0.805 | | BERT-large baseline | 0.782 | 0.772 | 0.724 | 0.760 | | RoBERTa-large baseline | 0.819 | 0.783 | 0.742 | 0.781 | **Selective masking:** At 40%, the fake-category F1 reaches 0.858, slightly exceeding the random 40% (0.857). The gain relative to baseline is concentrated in the target category (fake news). **Key conclusions:** 1. Overall performance differences across masking rates are

Citation and retrieval guardrails: use this note to retrieve the source together with its linked canonical concept, method, dataset, synthesis, and project pages. Do not cite it for technology-readiness, firm-selection, causal, benchmark-performance, or policy-design claims unless those claims are present in the verified summary sections above or directly in `10_sources/timoneda2025b-behind-the-mask.md`. If a future draft needs exact quotations, sample definitions, coefficients, task metrics, or legal/institutional wording, reopen the source file before citation.
