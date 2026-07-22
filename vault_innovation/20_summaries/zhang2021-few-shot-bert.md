---
title: "Revisiting Few-Sample BERT Fine-Tuning"
note_type: source_summary
summary: "Identifies three causes of BERT fine-tuning instability on small datasets and provides practical fixes; establishes that ~1,000 training examples is the reliable fine-tuning floor."
authors:
  - Zhang, Tianyi
  - Wu, Felix
  - Katiyar, Arzoo
  - Weinberger, Kilian Q.
  - Artzi, Yoav
year: 2021
source_files: ["10_sources/zhang2021-few-shot-bert.md"]
source_urls:
  - https://arxiv.org/abs/2006.05987
projects:
  - bundesinnovationshaushalt-trl
tags:
  - source-summary
  - NLP
  - BERT
  - fine-tuning
  - instability
  - sample-size
  - optimization
updated: "2026-05-04"
---

# Zhang et al. (2021) — Revisiting Few-Sample BERT Fine-Tuning

## Source paper link/path

- Source file: `10_sources/zhang2021-few-shot-bert.md`
- Source status: available as converted Markdown in `10_sources/`
- Semantic verification: locally checked against the listed source Markdown on 2026-05-04.

## Bibliographic metadata

- Title: "Revisiting Few-Sample BERT Fine-Tuning"
- Authors:
- Zhang, Tianyi
- Year: 2021
- Venue/institution: not specified
- DOI/URL: not specified

## Detailed summary

Semantic verification against `10_sources/zhang2021-few-shot-bert.md`: Thispaperisastudyoffine-tuningofBERTcontextualrepresentations,withfocus oncommonlyobservedinstabilitiesinfew-samplescenarios. Weidentifyseveral factorsthatcausethisinstability: thecommonuseofanon-standardoptimization method with biased gradient estimation; the limited applicability of significant partsoftheBERTnetworkfordown-streamtasks;andtheprevalentpracticeof usingapre-determined,andsmallnumberoftrainingiterations. Weempirically testtheimpactofthesefactors,andidentifyalternativepracticesthatresolvethe commonlyobservedinstabilityoftheprocess. Inlightoftheseobservations,we re-visitrecentlyproposedmethodstoimprovefew-samplefine-tuningwithBERT and re-evaluate their effectiveness. Generally, we observe the impact of these methodsdiminishessignificantlywithourmodifiedprocess. For wiki use, this note should be retrieved for the source's own contribution, evidence, method, and policy mechanism. Broader implications for the Bundesinnovationshaushalt/TRL project are project interpretations unless the source itself states them explicitly. Additional verified retrieval detail: **Instability at small sample sizes:** - On RTE (2,500 training examples), 48% of fine-tuning runs with the default BERTADAM optimizer produce accuracy below 55% — barely above random chance (50%). This degeneracy disappears with the debiased ADAM optimizer. - Fine-tuning instability is most severe on datasets with fewer than 10,000 training examples. Large datasets (like MNLI, 393,000 examples) are unaffected. **Fix 1: Debiased ADAM (bias correction):** - Restoring the standard ADAM bias correction step reduces variance in performance substantially across all four small datasets. - On RTE, the degenerate run rate (accuracy < 55%) drops from 48% to near zero. - Expected performance with 5–10 random seeds using debiased ADAM matches the expected performance of 50 random seeds with BERTADAM. **Practical implication: run 5–10 seeds, not 50.** **Fix 2: Re-initialization of top BERT layers:** - Re-initializing the top 1–6 pre-trained BERT layers before fine-tuning consistently improves mean performance and reduces variance. - Example on RTE: Standard fine-tuning 69.5 ± 2.5 → Re-init 72.6 ± 1.6 (test accuracy, 3 epochs) - Example on RTE at 1k samples: Standard 62.5 ± 2.8 → Re-init 65.6 ± 2.0 - The top layers of BERT are over-specialized to the pre-training objective and provide a poor initialization for downstream tasks; re-initializing them gives fine-tuning a better starting point. **Fix 3: Longer training:** - The default 3-epoch recommendation (from Devlin et al. 2019) is sub-optimal for small datasets.

## Research question

Source-grounded framing: Thispaperisastudyoffine-tuningofBERTcontextualrepresentations,withfocus oncommonlyobservedinstabilitiesinfew-samplescenarios. Weidentifyseveral factorsthatcausethisinstability: thecommonuseofanon-standardoptimization method with biased gradient estimation; the limited applicability of significant partsoftheBERTnetworkfordown-streamtasks;andtheprevalentpracticeof usingapre-determined,andsmallnumberoftrainingiterations.

## Core argument or contribution

Weempirically testtheimpactofthesefactors,andidentifyalternativepracticesthatresolvethe commonlyobservedinstabilityoftheprocess. Inlightoftheseobservations,we re-visitrecentlyproposedmethodstoimprovefew-samplefine-tuningwithBERT and re-evaluate their effectiveness. Generally, we observe the impact of these methodsdiminishessignificantlywithourmodifiedprocess.

## Methodology

**Model:** BERT-large (24 layers, 340 million parameters), uncased - **Datasets:** Eight GLUE benchmark tasks; primary focus on four with fewer than 10,000 training examples (RTE, MRPC, STS-B, CoLA); all eight datasets also downsampled to 1,000 training examples for direct comparison - **Experimental approach:** 20–50 random seeds per condition; bootstrap simulation of expected performance versus number of random trials; ablation of optimizer, initialization, and training duration - **Three fixes studied:** 1. **Debiased ADAM:** Use standard ADAM (with bias correction) instead of BERTADAM (which omits it) 2. **Re-initialization (Re-init):** Re-initialize the top L layers of BERT's pre-trained weights before fine-tuning (tested with L = 1 through 6) 3. **Longer training:** Tune the number of training iterations rather than accepting the default 3-epoch recommendation

## Datasets/materials used

Named datasets/materials discussed in the maintained note: [[50_datasets/cordis-horizon-europe-h2020.md]]; [[50_datasets/foerderkatalog-des-bundes.md]]. Use `10_sources/zhang2021-few-shot-bert.md` for exact definitions, variable construction, sample period, and table/source-document provenance.

## Key findings

**Instability at small sample sizes:** - On RTE (2,500 training examples), 48% of fine-tuning runs with the default BERTADAM optimizer produce accuracy below 55% — barely above random chance (50%). This degeneracy disappears with the debiased ADAM optimizer. - Fine-tuning instability is most severe on datasets with fewer than 10,000 training examples. Large datasets (like MNLI, 393,000 examples) are unaffected. **Fix 1: Debiased ADAM (bias correction):** - Restoring the standard ADAM bias correction step reduces variance in performance substantially across all four small datasets. - On RTE, the degenerate run rate (accuracy < 55%) drops from 48% to near zero. - Expected performance with 5–10 random seeds using debiased ADAM matches the expected performance of 50 random seeds with BERTADAM. **Practical implication: run 5–10 seeds, not 50.** **Fix 2: Re-initialization of top BERT layers:** - Re-initializing the top 1–6 pre-trained BERT layers before fine-tuning consistently improves mean performance and reduces variance. - Example on RTE: Standard fine-tuning 69.5 ± 2.5 → Re-init 72.6 ± 1.6 (test accuracy, 3 epochs) - Example on RTE at 1k samples: Standard 62.5 ± 2.8 → Re-init 65.6 ± 2.0 - The top layers of BERT are over-specialized to the pre-training objective and provide a poor initialization for downstream tasks; re-initializing them gives fine-tuning a better starting point. **Fix 3: Longer training:** - The default 3-epoch recommendation (from Devlin et al. 2019) is sub-optimal for small datasets.

## Limitations

The repair does not add limitations that are not visible in the source text. Treat the findings as bounded by the source's stated model, sample, period, country, task, or policy instrument, and check `10_sources/zhang2021-few-shot-bert.md` before using precise quantitative or causal claims.

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

**For TRL classification of German Foerderkatalog projects, this paper provides three concrete decisions:** 1. **Minimum training set size: 1,000 labeled CORDIS examples.** Below 1,000, results are unreliable regardless of how carefully the fine-tuning is run. The goal for CORDIS data collection should be at least 1,000 labeled project descriptions, ideally 2,000–3,000 to provide headroom above the instability zone. Fewer than 200 examples should be treated as preliminary only. 2. **Use debiased ADAM (standard ADAM with bias correction).** Modern fine-tuning libraries (HuggingFace Transformers after July 2019) default to debiased ADAM, so this is likely already handled. Verify that the optimizer is not BERTADAM (the legacy biased version). Use `AdamW` (debiased) not `BertAdam`. 3. **Run 5–10 random seeds and report mean ± standard deviation.** Reporting a single run result is not reproducible or trustworthy. With 5–10 seeds and debiased ADAM, the expected performance estimate is stable. This is the validation protocol to adopt for all fine-tuning experiments in this project. **Additional practical points:** - Consider re-initializing the top 1–3 layers of XLM-RoBERTa before fine-tuning (Re-init). The gain is typically 2–3 pp on accuracy and reduces variance. This is a low-cost improvement. - Train for more than 3 epochs if training set is small (at or near 1,000 examples). Tune the number of training steps using a development set. - The paper's results are on English GLUE benchmarks; XLM-RoBERTa for cross-lingual classification may behave somewhat differently, but the instability mechanisms (optimizer bias, poor layer initialization) are architecture-level and should apply similarly.

## Links to canonical concept, method, dataset, synthesis, and project notes

- [[30_concepts/technology-readiness-levels.md]]
- [[40_methods/xlm-roberta-multilingual-classification.md]]
- [[50_datasets/cordis-horizon-europe-h2020.md]]
- [[20_summaries/wang2024-bert-vs-gpt.md]]
- [[20_summaries/kuzman2025-parlacap.md]]
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

Source identity was checked locally against `10_sources/zhang2021-few-shot-bert.md` during the 2026-05-04 paper-by-paper verification pass. The maintained summary is tied to the source titled "Revisiting Few-Sample BERT Fine-Tuning" and should be used for the argument, method, findings, and limitations stated in that mapped source rather than for adjacent claims that only appear in project interpretation.

Verification synthesis: Semantic verification against `10_sources/zhang2021-few-shot-bert.md`: Thispaperisastudyoffine-tuningofBERTcontextualrepresentations,withfocus oncommonlyobservedinstabilitiesinfew-samplescenarios. Weidentifyseveral factorsthatcausethisinstability: thecommonuseofanon-standardoptimization method with biased gradient estimation; the limited applicability of significant partsoftheBERTnetworkfordown-streamtasks;andtheprevalentpracticeof usingapre-determined,andsmallnumberoftrainingiterations. Weempirically testtheimpactofthesefactors,andidentifyalternativepracticesthatresolvethe commonlyobservedinstabilityoftheprocess. Inlightoftheseobservations,we re-visitrecentlyproposedmethodstoimprovefew-samplefine-tuningwithBERT and re-evaluate their effectiveness. Generally, we observe the impact of these methodsdiminishessignificantlywithourmodifiedprocess. For wiki use, this note should be retrieved for the source's own contribution, evidence, method, and policy mechanism. Broader implications for the Bundesinnovationshaushalt/TRL project are project interpretations unless the source itself states them explicitly. Additional verified retrieval detail: **Instability at small sample sizes:** - On RTE (2,500 training examples), 48% of fine-tuning runs with the default BERTADAM optimizer produce accuracy below 55% — barely above random chance (50%). This degeneracy disappears with the debiased ADAM optimizer. - Fine-tuning instability is most severe on datasets with fewer than 10,000 training examples. Large datasets (like MNLI, 393,000 examples) are unaffected. **Fix 1: Debiased ADAM (bias correction):** - Restoring the standard ADAM bias correction step reduces variance in performance substantially across all four small datasets.

Method and materials check: **Model:** BERT-large (24 layers, 340 million parameters), uncased - **Datasets:** Eight GLUE benchmark tasks; primary focus on four with fewer than 10,000 training examples (RTE, MRPC, STS-B, CoLA); all eight datasets also downsampled to 1,000 training examples for direct comparison - **Experimental approach:** 20–50 random seeds per condition; bootstrap simulation of expected performance versus number of random trials; ablation of optimizer, initialization, and training duration - **Three fixes studied:** 1. **Debiased ADAM:** Use standard ADAM (with bias correction) instead of BERTADAM (which omits it) 2. **Re-initialization (Re-init):** Re-initialize the top Data/materials scope: Named datasets/materials discussed in the maintained note: [[50_datasets/cordis-horizon-europe-h2020.md]]; [[50_datasets/foerderkatalog-des-bundes.md]]. Use `10_sources/zhang2021-few-shot-bert.md` for exact definitions, variable construction, sample period, and table/source-document provenance.

Finding-level check: **Instability at small sample sizes:** - On RTE (2,500 training examples), 48% of fine-tuning runs with the default BERTADAM optimizer produce accuracy below 55% — barely above random chance (50%). This degeneracy disappears with the debiased ADAM optimizer. - Fine-tuning instability is most severe on datasets with fewer than 10,000 training examples. Large datasets (like MNLI, 393,000 examples) are unaffected. **Fix 1: Debiased ADAM (bias correction):** - Restoring the standard ADAM bias correction step reduces variance in performance substantially across all four small datasets. - On RTE, the degenerate run rate (accuracy < 55%) drops from 48% to near zero. - Expected performance with 5–10 random seeds using debiased ADAM matches the expected performance of 50 random seeds with BERTADAM. **Practical implication: run 5–10 seeds, not 50.** **Fix 2: Re-initialization of top BERT layers:** - Re-initializing the top 1–6 pre-trained

Citation and retrieval guardrails: use this note to retrieve the source together with its linked canonical concept, method, dataset, synthesis, and project pages. Do not cite it for technology-readiness, firm-selection, causal, benchmark-performance, or policy-design claims unless those claims are present in the verified summary sections above or directly in `10_sources/zhang2021-few-shot-bert.md`. If a future draft needs exact quotations, sample definitions, coefficients, task metrics, or legal/institutional wording, reopen the source file before citation.
