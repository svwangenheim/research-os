---
title: "How to Train Your Stochastic Parrot: Large Language Models for Political Texts"
note_type: source_summary
summary: "Ornstein, Blasingame, and Truscott show how few-shot prompts to GPT-style large language models can be used for political text-as-data tasks including sentiment analysis, political-ad tone classification, ideology scaling, and topic labeling. Across pre-registered applications, the approach outperforms conventional automated baselines and can approximate human crowd/expert coding at lower cost, but the authors stress validation, prompt sensitivity, reproducibility, and bias risks."
authors: [Joseph T. Ornstein, Elise N. Blasingame, Jake S. Truscott]
year: 2024
source_files: ["10_sources/ornstein2025-stochastic-parrot.md", "10_sources/ornstein2025-stochastic-parrot.pdf"]
source_urls:
  - "https://joeornstein.github.io/publications/ornstein-blasingame-truscott.pdf"
projects: [bundesinnovationshaushalt-trl]
tags:
  - source-summary
  - llm-annotation
  - political-texts
  - few-shot-prompting
  - text-as-data
updated: "2026-05-04"
---

# Ornstein, Blasingame & Truscott - How to Train Your Stochastic Parrot

## Source paper link/path

- Source file: `10_sources/ornstein2025-stochastic-parrot.md`
- Source PDF: `10_sources/ornstein2025-stochastic-parrot.pdf`
- Source status: corrected on 2026-05-04. The previous local PDF/Markdown were an unrelated mathematics paper on coupler curves and rigid graphs.

## Bibliographic metadata

- Title: "How to Train Your Stochastic Parrot: Large Language Models for Political Texts"
- Authors: Joseph T. Ornstein, Elise N. Blasingame, and Jake S. Truscott
- Local PDF date: July 23, 2024
- Software: `promptr` R package, referenced by the authors as open-source tooling for the workflow

## Detailed summary

The paper argues that large language models can be adapted to political text-as-data tasks by converting document-labeling problems into next-word prediction prompts. The authors position this as a social-science measurement workflow, not simply a generic automation shortcut. Political scientists often need to label documents for latent quantities such as sentiment, tone, ideology, or topic. Traditional approaches rely on dictionaries, bag-of-words supervised learning, crowd coding, or expert coding, each of which can be costly, brittle, or insensitive to context. The paper tests whether few-shot prompts to GPT-style LLMs can provide a better alternative.

The authors emphasize two model properties that matter for social-science text measurement. First, LLMs are trained through self-supervised next-word prediction on very large corpora, allowing researchers to reuse general language knowledge without collecting large task-specific training sets. Second, transformer-based contextualized embeddings let the model interpret words in context, which is especially useful for political language where sarcasm, references, and issue context can change meaning.

The empirical section evaluates four applications. The first classifies sentiment in 945 tweets about controversial US Supreme Court decisions. The authors compare GPT-3 and GPT-4 prompts against dictionary-based sentiment, Naive Bayes, and a RoBERTa Twitter-sentiment model, using author-coded sentiment labels as the comparison point. The second application classifies tone in American political ads from Carlson and Montgomery, comparing LLM classifications with crowd-coded and expert-coded tone estimates. The third replicates manifesto ideology scaling from Benoit et al. by treating the LLM as a non-expert coder that places text units into ideological categories. The fourth uses GPT-3 to assign topic labels to 9,704 one-minute US House floor speeches, then validates label quality through an optimal-label task in which a blinded human coder chooses among the actual GPT label and intruder labels.

Across these applications, the paper reports that few-shot LLM prompting often outperforms conventional automated methods and can be comparable to human crowd-coding or expert-coded measures at substantially lower time and financial cost. The most important practical claim is not that LLMs are always correct, but that a single pretrained model can be adapted to multiple measurement tasks with prompt engineering and validation rather than with large labeled training sets.

The discussion is unusually important for using the paper responsibly. The authors warn that LLM outputs are sensitive to researcher choices, especially prompt design. They recommend a three-step validation process: hand-label a small random subset for prompt design; apply the prompt to a larger hand-labeled validation set; only then use the model on unlabeled data if validation shows strong correspondence with human labels. They also warn that newer RLHF-tuned chat models may not always be best for measurement, because models optimized for helpful conversation can be overconfident or less calibrated than earlier completion models. Finally, they emphasize reproducibility risks from proprietary closed models and bias risks from pretrained corpora.

## Research question

Can few-shot prompts to large language models reliably perform political text-as-data measurement tasks, and what validation workflow should researchers use before applying LLM-generated labels at scale?

## Core argument or contribution

The paper contributes a practical framework for using few-shot LLM prompting in political text analysis. Its core contribution is the demonstration that prompt-adapted LLMs can perform several common social-science text measurement tasks with strong performance and lower labeling costs, provided researchers validate the prompts against human-coded data and treat the outputs as measurement instruments subject to bias and reproducibility checks.

## Methodology

- Few-shot prompting of GPT-style LLMs.
- Reformulation of classification, scaling, and topic-labeling tasks as next-word prediction problems.
- Pre-registered analyses for the applications.
- Comparisons against dictionary, Naive Bayes, RoBERTa, crowd-coded, and expert-coded baselines where relevant.
- Application-specific validation against author-coded labels, expert labels, crowd labels, and optimal-label human review.

## Datasets/materials used

- 945 Twitter/X posts about US Supreme Court rulings, author-coded for sentiment.
- Political advertisement tone data from Carlson and Montgomery, compared with expert and crowd-coded ratings.
- Party-manifesto ideology scaling materials from Benoit et al.
- 9,704 one-minute US House floor speeches from Wilkerson and Casas for topic-labeling/discovery.
- Prompt templates and the authors' `promptr` R package.

## Key findings

- Few-shot LLM prompts can perform several political text-as-data tasks effectively, including sentiment analysis, ad-tone classification, manifesto ideology scaling, and topic labeling.
- In the reported applications, the few-shot LLM approach often outperforms conventional automated approaches such as dictionary methods, Naive Bayes, and task-specific supervised classifiers.
- LLM measures can approximate crowd-coded or expert-coded measures at lower cost, making large-scale text measurement more feasible for researchers without large annotation budgets.
- Contextual understanding is especially valuable for texts whose meaning depends on political context, sarcasm, or implicit references.
- GPT-4 can be strongly correlated with human labels but may be overconfident; the authors caution that the newest or most chat-optimized model is not automatically the best measurement model.
- The authors' central operational advice is validation first: prompt design and model choice must be checked against human-coded data before scaling to unlabeled corpora.

## Limitations

- Prompt design choices can materially affect results.
- LLM labels should not be used without validation against human-coded data.
- Proprietary model deprecation creates reproducibility problems; the GPT-3 models used for the paper's results were removed from the public API in January 2024.
- LLMs inherit falsehoods, stereotypes, and biases from training corpora and may be harmful for tasks requiring current factual knowledge or sensitive judgments.
- Findings are based on political text applications and need project-specific validation before transfer to technical funding descriptions or TRL classification.

## Important concepts discussed

- [[30_concepts/llm-annotation-and-automated-coding.md]]
- [[30_concepts/text-as-data-computational-social-science.md]]
- [[30_concepts/foundation-models-and-pretrained-transformers.md]]
- Few-shot prompting
- Measurement validity
- Prompt sensitivity
- Reproducibility of proprietary LLMs

## Methods discussed

- [[40_methods/llm-few-shot-social-science.md]]
- Prompt-based classification
- Prompt-based scaling
- LLM-assisted topic labeling
- Human-label validation

## Datasets discussed

- US Supreme Court tweet sentiment dataset
- Political advertisement tone dataset
- Party manifesto ideology-scaling materials
- US House floor-speech corpus
- Human-coded validation labels

## Relation to other papers in the vault

This paper complements [[20_summaries/grimmer2013-text-as-data.md]] by applying the classic validation-first text-as-data principle to LLM prompting. It also complements [[20_summaries/gilardi2023-chatgpt-annotation.md]], [[20_summaries/pangakis2023-llm-annotation-validation.md]], [[20_summaries/halterman2025-codebook-llms.md]], and [[20_summaries/moller2024-parrot-dilemma.md]] on when LLM annotation works, how it should be validated, and where prompt/model choices create risks.

## Implications for LLM research or the project domain

For [[70_projects/bundesinnovationshaushalt-trl.md]], the paper supports few-shot prompting as a candidate approach for coding project descriptions, but only after project-specific validation against human labels. It is especially relevant for designing prompts, creating a small gold-standard validation set, comparing models, monitoring overconfidence, and documenting model/version reproducibility.

The paper should not be cited as proof that LLMs can directly infer TRLs or policy relevance from funding texts. Its usable implication is narrower: LLM prompting can be a strong text-measurement method when the concept is clearly specified, examples are provided, and validation demonstrates that outputs correspond to human judgment.

## Links to canonical concept, method, dataset, synthesis, and project notes

- Concepts: [[30_concepts/llm-annotation-and-automated-coding.md]], [[30_concepts/text-as-data-computational-social-science.md]], [[30_concepts/foundation-models-and-pretrained-transformers.md]]
- Methods: [[40_methods/llm-few-shot-social-science.md]]
- Datasets: no canonical dataset note linked
- Synthesis: [[90_synthesis/llm-text-classification-and-annotation.md]]
- Project: [[70_projects/bundesinnovationshaushalt-trl.md]]
