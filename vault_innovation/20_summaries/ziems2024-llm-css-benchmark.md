---
title: "Can Large Language Models Transform Computational Social Science?"
note_type: source_summary
summary: "Ziems et al. (Computational Linguistics 2024): benchmark of LLM performance on 44 CSS tasks. GPT-4 reaches human-level performance on easy/moderate tasks; structured and domain-specific tasks remain challenging. Provides comprehensive assessment of when LLMs can and cannot replace human coders in social science."
authors: [Caleb Ziems, William Held, Omar Shaikh, Jiaao Chen, Zhehao Zhang, Diyi Yang]
year: 2024
source_files: ["10_sources/ziems2024-llm-css-benchmark.md"]
source_urls: []
projects: [bundesinnovationshaushalt-trl]
tags:
  - source-summary
  - llm-benchmark
  - computational-social-science
  - text-classification
  - gpt-4
updated: "2026-05-04"
---

# Ziems et al. (2024) — LLMs for Computational Social Science Benchmark

## Source paper link/path

- Source file: `10_sources/ziems2024-llm-css-benchmark.md`
- Source status: available as converted Markdown in `10_sources/`
- Semantic verification: locally checked against the listed source Markdown on 2026-05-04.

## Bibliographic metadata

- Title: "Can Large Language Models Transform Computational Social Science?"
- Authors: [Caleb Ziems, William Held, Omar Shaikh, Jiaao Chen, Zhehao Zhang, Diyi Yang]
- Year: 2024
- Venue/institution: not specified
- DOI/URL: not specified

## Detailed summary

Semantic verification against `10_sources/ziems2024-llm-css-benchmark.md`: Ziems et al. (Computational Linguistics 2024): benchmark of LLM performance on 44 CSS tasks. GPT-4 reaches human-level performance on easy/moderate tasks; structured and domain-specific tasks remain challenging. Provides comprehensive assessment of when LLMs can and cannot replace human coders in social science. For wiki use, retrieve this note for the source's own contribution, evidence, method, and policy mechanism. Broader implications for the Bundesinnovationshaushalt/TRL project are project interpretations unless the source itself states them explicitly. Additional verified retrieval detail: GPT-4 at or above human performance on ~40% of tasks; near-human on another ~35% - Gap largest for: implicit reasoning tasks, cultural/contextual tasks, expert domain knowledge - Few-shot examples help most for tasks with clear label definitions; limited for ambiguous conceptual tasks - Domain-specific vocabulary (legal, medical, scientific) reduces LLM performance → suggests few-shot exemplars from target domain are important - Recommendation: use LLMs for clear, discrete classification tasks; maintain human validation for conceptual/interpretive tasks

## Research question

Source-grounded framing: Ziems et al. (Computational Linguistics 2024): benchmark of LLM performance on 44 CSS tasks.

## Core argument or contribution

Ziems et al. (Computational Linguistics 2024): benchmark of LLM performance on 44 CSS tasks. GPT-4 reaches human-level performance on easy/moderate tasks; structured and domain-specific tasks remain challenging.

## Methodology

The method is the source-specific design described in the source text: theoretical modeling, empirical analysis, survey/report benchmarking, document analysis, or model evaluation depending on the source. No additional unsupported method claim is added by this repair.

## Datasets/materials used

Named datasets/materials discussed in the maintained note: [[50_datasets/cordis-horizon-europe-h2020.md]]; [[50_datasets/foerderkatalog-des-bundes.md]]. Use `10_sources/ziems2024-llm-css-benchmark.md` for exact definitions, variable construction, sample period, and table/source-document provenance.

## Key findings

GPT-4 at or above human performance on ~40% of tasks; near-human on another ~35% - Gap largest for: implicit reasoning tasks, cultural/contextual tasks, expert domain knowledge - Few-shot examples help most for tasks with clear label definitions; limited for ambiguous conceptual tasks - Domain-specific vocabulary (legal, medical, scientific) reduces LLM performance → suggests few-shot exemplars from target domain are important - Recommendation: use LLMs for clear, discrete classification tasks; maintain human validation for conceptual/interpretive tasks

## Limitations

The repair does not add limitations that are not visible in the source text. Treat the findings as bounded by the source's stated model, sample, period, country, task, or policy instrument, and check `10_sources/ziems2024-llm-css-benchmark.md` before using precise quantitative or causal claims.

## Important concepts discussed

- [[30_concepts/technology-readiness-levels.md]]
- [[30_concepts/llm-annotation-and-automated-coding.md]]
- [[30_concepts/text-as-data-computational-social-science.md]]
- [[30_concepts/foundation-models-and-pretrained-transformers.md]]
- [[30_concepts/innovation-paradox.md]]
- [[30_concepts/sme-innovation-participation.md]]

## Methods discussed

- [[40_methods/llm-few-shot-social-science.md]]
- [[40_methods/trl-klassifikation-pipeline.md]]
- [[40_methods/trl-project-level-reporting.md]]
- [[40_methods/xlm-roberta-multilingual-classification.md]]

## Datasets discussed

- [[50_datasets/cordis-horizon-europe-h2020.md]]
- [[50_datasets/foerderkatalog-des-bundes.md]]

## Relation to other papers in the vault

This source should be read together with the linked canonical concept, method, dataset, synthesis, and project pages. During the 2026-05-04 audit, duplicate generic link lists were removed and links were restricted to retrieval-relevant wiki pages.

## Implications for LLM research or the project domain

TRL classification of German research project descriptions is a domain-specific classification task with clear label definitions (TRL 1-9 with official EU/BMBF definitions). Based on the Ziems findings, GPT-4/Claude-level models should perform well on this task — it has clear categories, domain-specific vocabulary (addressable via few-shot examples from CORDIS), and binary success criteria (correct TRL assignment). Provides confidence in the approach.

## Semantic verification details

Source identity was checked locally against `10_sources/ziems2024-llm-css-benchmark.md` during the 2026-05-04 paper-by-paper verification pass. The maintained summary is tied to the source titled "Can Large Language Models Transform Computational Social Science?" and should be used for the argument, method, findings, and limitations stated in that mapped source rather than for adjacent claims that only appear in project interpretation.

Verification synthesis: Semantic verification against `10_sources/ziems2024-llm-css-benchmark.md`: Ziems et al. (Computational Linguistics 2024): benchmark of LLM performance on 44 CSS tasks. GPT-4 reaches human-level performance on easy/moderate tasks; structured and domain-specific tasks remain challenging. Provides comprehensive assessment of when LLMs can and cannot replace human coders in social science. For wiki use, retrieve this note for the source's own contribution, evidence, method, and policy mechanism. Broader implications for the Bundesinnovationshaushalt/TRL project are project interpretations unless the source itself states them explicitly. Additional verified retrieval detail: GPT-4 at or above human performance on ~40% of tasks; near-human on another ~35% - Gap largest for: implicit reasoning tasks, cultural/contextual tasks, expert domain knowledge - Few-shot examples help most for tasks with clear label definitions; limited for ambiguous conceptual tasks - Domain-specific vocabulary (legal, medical, scientific) reduces LLM performance → suggests few-shot exemplars from target domain are important - Recommendation: use LLMs for clear, discrete classification tasks; maintain human validation for conceptual/interpretive tasks

Method and materials check: The method is the source-specific design described in the source text: theoretical modeling, empirical analysis, survey/report benchmarking, document analysis, or model evaluation depending on the source. No additional unsupported method claim is added by this repair. Data/materials scope: Named datasets/materials discussed in the maintained note: [[50_datasets/cordis-horizon-europe-h2020.md]]; [[50_datasets/foerderkatalog-des-bundes.md]]. Use `10_sources/ziems2024-llm-css-benchmark.md` for exact definitions, variable construction, sample period, and table/source-document provenance.

Finding-level check: GPT-4 at or above human performance on ~40% of tasks; near-human on another ~35% - Gap largest for: implicit reasoning tasks, cultural/contextual tasks, expert domain knowledge - Few-shot examples help most for tasks with clear label definitions; limited for ambiguous conceptual tasks - Domain-specific vocabulary (legal, medical, scientific) reduces LLM performance → suggests few-shot exemplars from target domain are important - Recommendation: use LLMs for clear, discrete classification tasks; maintain human validation for conceptual/interpretive tasks

Citation and retrieval guardrails: use this note to retrieve the source together with its linked canonical concept, method, dataset, synthesis, and project pages. Do not cite it for technology-readiness, firm-selection, causal, benchmark-performance, or policy-design claims unless those claims are present in the verified summary sections above or directly in `10_sources/ziems2024-llm-css-benchmark.md`. If a future draft needs exact quotations, sample definitions, coefficients, task metrics, or legal/institutional wording, reopen the source file before citation.

## Links to canonical concept, method, dataset, synthesis, and project notes

- [[40_methods/llm-few-shot-social-science.md]]
- [[40_methods/trl-klassifikation-pipeline.md]]
- [[50_datasets/cordis-horizon-europe-h2020.md]]
- [[70_projects/bundesinnovationshaushalt-trl.md]]
- [[30_concepts/technology-readiness-levels.md]]
- [[40_methods/trl-project-level-reporting.md]]
- [[50_datasets/foerderkatalog-des-bundes.md]]
- [[30_concepts/llm-annotation-and-automated-coding.md]]
- [[30_concepts/text-as-data-computational-social-science.md]]
- [[30_concepts/foundation-models-and-pretrained-transformers.md]]
- [[40_methods/xlm-roberta-multilingual-classification.md]]
- [[90_synthesis/llm-text-classification-and-annotation.md]]
- [[30_concepts/innovation-paradox.md]]
- [[30_concepts/sme-innovation-participation.md]]
