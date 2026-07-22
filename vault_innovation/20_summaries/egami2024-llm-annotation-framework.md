---
title: "Using Large Language Model Annotations for the Social Sciences: A General Framework of Using Predicted Variables in Downstream Analyses"
note_type: source_summary
summary: "Egami, Hinck, Stewart, and Wei (2024) show that treating LLM or other automated text labels as observed variables can bias downstream statistical analyses and invalidate confidence intervals, even when annotation accuracy is above 90 percent. They propose design-based supervised learning (DSL), a doubly robust framework that combines large-scale automated annotations with a randomly sampled set of expert annotations so researchers can use predicted text variables while preserving valid inference."
authors: ["Naoki Egami", "Musashi Hinck", "Brandon M. Stewart", "Hanying Wei"]
year: 2024
source_files: ["10_sources/egami2024-llm-annotation-framework.md", "10_sources/egami2024-llm-annotation-framework.pdf"]
source_urls: ["https://arxiv.org/abs/2307.01984"]
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
  - text-as-data
  - measurement-error
  - causal-inference
  - social-science
updated: "2026-05-04"
---

# Egami et al. (2024) - LLM Annotations and Predicted Variables in Downstream Analyses

## Source paper link/path

- Source files: `10_sources/egami2024-llm-annotation-framework.md`, `10_sources/egami2024-llm-annotation-framework.pdf`
- Source URL: https://arxiv.org/abs/2307.01984
- Source status: available as converted Markdown in `10_sources/`; source identity verified against title page and abstract during the 2026-05-04 one-by-one audit.

## Bibliographic metadata

- Title: "Using Large Language Model Annotations for the Social Sciences: A General Framework of Using Predicted Variables in Downstream Analyses"
- Authors: Naoki Egami, Musashi Hinck, Brandon M. Stewart, Hanying Wei
- Version date visible in source: November 17, 2024
- Venue/institution: working paper / arXiv source in the vault
- Software: `dsl` R package, listed in the source as `http://dsl.software`

## Detailed summary

Egami et al. address a specific statistical problem in social-science text analysis: researchers increasingly use LLMs and other automated annotation systems to create labels, then analyze those labels as if they were directly observed variables. The paper argues that this practice is not statistically valid in general. High annotation accuracy at the label-prediction stage does not guarantee unbiased downstream estimates, valid confidence intervals, or reliable p-values, because prediction errors can be systematic rather than random. Errors may correlate with observed covariates, unobserved variables, outcomes, treatments, or task features, so even small error rates can distort regression coefficients, category estimates, or causal estimands.

The paper's central contribution is design-based supervised learning (DSL). DSL combines automated annotations for the full document corpus with a smaller set of expert annotations collected through a researcher-controlled sampling design, commonly random sampling. The method then uses a doubly robust correction to combine predicted labels and expert labels in downstream analysis. The key design assumption is not that LLMs are unbiased or that expert labels are perfect; it is that the researcher controls the process by which documents are sampled for expert annotation and every document has positive probability of expert coding. Under that design condition and regularity assumptions, the DSL estimator can produce statistically valid estimates even when automated labels contain arbitrary non-random prediction errors.

The paper is not primarily a prompt-engineering guide. It uses LLM annotation examples to motivate the problem, but its main object is inference with predicted variables. The authors show that the same problem applies to LLM-only annotation pipelines and classical supervised machine-learning pipelines when predicted labels are inserted directly into downstream analyses. Their framework covers predicted text variables used as outcomes, independent variables, treatments, instruments, or covariates, and extends to common social-science analyses such as linear regression, logistic regression, multinomial-logistic regression, Poisson regression, linear fixed-effects regression, category-proportion estimation, instrumental-variable models, and causal inference with text.

The paper illustrates the problem with simulation and empirical applications. In simulations, ignoring prediction errors can produce substantial standardized bias and poor confidence-interval coverage even at high prediction accuracy, including 90-95 percent. The authors also examine LLM classification performance in two empirical applications: Fowler et al. (2021) political-ad tone classification using 13,040 expert-coded ads, and Pan and Chen (2018) Chinese citizen-complaint classification using 1,412 expert-coded complaints. They further review 113 annotation tasks from eight papers to show that LLM classification performance varies widely across tasks, models, and prompts. This empirical variation is part of the motivation for DSL: if annotation error behavior is unpredictable, inference should be designed to remain valid without assuming that the automated annotator's errors are random.

The practical message for the vault is that LLM labels should not be treated as measurement-free project variables when they feed later statistical analysis. For the Bundesinnovationshaushalt/TRL project, this source is relevant when LLM-generated TRL classes, technology labels, policy-topic labels, or mission labels become explanatory variables, outcomes, or grouping variables in quantitative analysis. A held-out expert validation set, intercoder comparison, and accuracy metrics are useful, but they are not enough if the labels are used for inference. The project either needs a design that uses human-coded samples to estimate and correct downstream quantities or must explicitly limit LLM labels to descriptive retrieval, screening, and qualitative analysis rather than causal or statistical inference.

## Research question

How can social scientists use LLM-generated or otherwise predicted text labels as variables in downstream statistical analyses without obtaining biased estimates or invalid uncertainty statements from prediction errors in the annotation step?

## Core argument or contribution

The paper argues that the common workflow "predict labels, check accuracy, then analyze predicted labels as observed data" is insufficient for valid statistical inference. Prediction errors can bias downstream estimates even when annotation accuracy is high. DSL solves this by combining full-corpus automated annotations with a probability sample of expert annotations and a doubly robust correction, allowing researchers to use advances in LLM annotation while preserving valid inference for text-based variables.

## Methodology

The paper develops a statistical framework and demonstrates it through theory, simulations, software, and empirical applications. Methodologically, it:

- Formalizes downstream analyses where some outcome, treatment, covariate, independent variable, instrument, or category variable is text-based and must be annotated.
- Shows why directly using predicted labels generally fails unless prediction errors are conditionally random in a way that is usually implausible.
- Proposes DSL, a doubly robust estimator that combines automated predictions, expert annotations, known sampling probabilities for expert coding, and cross-fitting.
- Proves consistency and asymptotic normality under a design-based expert-sampling assumption and regularity conditions.
- Uses simulations to compare direct use of predicted labels with DSL under varying prediction accuracy.
- Demonstrates the workflow on political-ad tone classification and Chinese citizen-complaint classification.
- Provides practical guidance on expert-annotation sample size, uncertainty in expert labels, and implementation through the `dsl` R package.

## Datasets/materials used

The source uses empirical materials from Fowler et al. (2021) on political-ad tone, including 13,040 expert-coded ads, and Pan and Chen (2018) on Chinese citizen complaints, including 1,412 expert-coded complaints. It also reviews 113 social-science LLM annotation tasks from eight papers and uses simulation designs to study bias, coverage, and RMSE. No Foerderkatalog, CORDIS, TRL, MIP, patent, or innovation-policy dataset is used in this paper.

## Key findings

- Automated text labels are often used as downstream variables, but treating predicted labels as observed variables can lead to substantial bias, invalid confidence intervals, and wrong p-values.
- High document-level annotation accuracy is not enough for valid inference; the source explicitly warns that bias can persist even above 90 percent and 95 percent accuracy.
- LLM annotation performance varies sharply by task, prompt, model, and application; the paper reports wide F1-score variation across two empirical applications and a review of 113 tasks.
- DSL provides a design-based way to combine automated annotations with a smaller probability sample of expert annotations.
- The key assumption is control over expert-annotation sampling, not unbiased LLM errors.
- Better automated annotations still help because they can reduce standard errors within DSL, but DSL does not require the automated annotation errors to be random.
- Expert annotations are treated as a target annotation procedure, not necessarily perfect truth; the paper discusses how to handle disagreement or uncertainty in expert annotations.
- The proposed method applies beyond simple classification accuracy checks and can support common downstream analyses involving text-based outcomes, predictors, treatments, instruments, and causal quantities.

## Limitations

The method requires a researcher-controlled expert-annotation sample with known or designable sampling probabilities; it is not a substitute for expert coding when no validation or target-annotation procedure exists. DSL protects downstream inference under its design assumptions, but it does not make the substantive construct validity of the annotation scheme automatic. Researchers still need a clear codebook or target annotation procedure, task-specific validation, attention to expert disagreement, and enough expert annotations for the intended precision. The paper is methodological and does not evaluate German innovation-policy datasets directly.

## Important concepts discussed

- [[30_concepts/llm-annotation-and-automated-coding.md]]
- [[30_concepts/text-as-data-computational-social-science.md]]
- [[30_concepts/foundation-models-and-pretrained-transformers.md]]
- Predicted variables
- Measurement error in automated annotation
- Expert annotations as target procedure
- Statistical validity of downstream text-as-data analysis
- Design-based sampling

## Methods discussed

- Design-based supervised learning (DSL)
- Doubly robust estimation
- Probability sampling for expert annotations
- Cross-fitting
- Data-driven power analysis for expert annotation size
- Quasi-Bayesian treatment of expert-label uncertainty
- LLM text classification, including zero-shot and few-shot prompting as annotation procedures
- Direct predicted-label analysis as the baseline to avoid
- [[40_methods/llm-few-shot-social-science.md]]

## Datasets discussed

- Fowler et al. (2021) expert-coded political advertisements from the Wesleyan Media Project context
- Pan and Chen (2018) expert-coded Chinese citizen complaints
- Literature-review corpus of 113 LLM annotation tasks from eight papers
- Simulation data generated in the paper

## Relation to other papers in the vault

This paper should be read after [[20_summaries/grimmer2013-text-as-data.md]] because it addresses a later-stage inference problem in text-as-data workflows: not just how to classify text, but how to use text-derived variables in statistical analysis. It complements [[20_summaries/gilardi2023-chatgpt-annotation.md]], [[20_summaries/pangakis2023-llm-annotation-validation.md]], [[20_summaries/halterman2025-codebook-llms.md]], and [[20_summaries/ziems2024-llm-css-benchmark.md]] by showing that annotation accuracy and validation benchmarks do not by themselves solve downstream measurement-error bias. It is also relevant to [[20_summaries/tornberg2025-llm-outperform-experts.md]] because strong LLM annotation performance still needs inferential correction when predicted labels enter statistical models.

## Implications for LLM research or the project domain

For the Bundesinnovationshaushalt/TRL project, Egami et al. imply a strong boundary between classification for retrieval and classification for inference. If LLM-generated TRL or topic labels are used only to organize documents, support qualitative coding, or prioritize human review, ordinary validation may be sufficient. If those labels are used to estimate policy patterns, compare agencies, explain funding allocation, or infer relationships between funding and outcomes, the project should not simply regress on LLM-predicted labels. It should draw a probability sample for expert annotation, preserve sampling probabilities, estimate downstream quantities with a DSL-style correction or an equivalent measurement-error-aware method, and report uncertainty that includes annotation error.

## Links to canonical concept, method, dataset, synthesis, and project notes

- Concepts: [[30_concepts/llm-annotation-and-automated-coding.md]], [[30_concepts/text-as-data-computational-social-science.md]], [[30_concepts/foundation-models-and-pretrained-transformers.md]]
- Methods: [[40_methods/llm-few-shot-social-science.md]] as the related prompting/annotation method; design-based supervised learning should be considered for a future canonical method note if multiple vault sources use it.
- Datasets: no canonical vault dataset note applies directly.
- Projects: [[70_projects/bundesinnovationshaushalt-trl.md]]
- Synthesis: [[90_synthesis/llm-text-classification-and-annotation.md]]
