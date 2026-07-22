---
title: "ChatGPT Outperforms Crowd Workers for Text-Annotation Tasks"
note_type: source_summary
summary: "Gilardi, Alizadeh, and Kubli (2023) evaluate zero-shot ChatGPT annotations against MTurk crowd workers and trained research assistants across four samples of tweets and news articles (n = 6,183). Using the same codebooks for all annotators, they find that ChatGPT's zero-shot accuracy exceeds MTurk by about 25 percentage points on average, its intercoder agreement exceeds both MTurk and trained annotators across tasks, and its per-annotation cost is below 0.003 dollars."
authors: ["Fabrizio Gilardi", "Meysam Alizadeh", "Mael Kubli"]
year: 2023
source_files: ["10_sources/gilardi2023-chatgpt-annotation.md", "10_sources/gilardi-et-al-2023-chatgpt-outperforms-crowd-workers-for-text-annotation-tasks.pdf"]
source_urls: ["https://doi.org/10.1073/pnas.2305016120"]
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
  - chatgpt
  - crowd-workers
  - text-classification
  - political-science
updated: "2026-05-04"
---

# Gilardi, Alizadeh & Kubli (2023) - ChatGPT Outperforms Crowd Workers

## Source paper link/path

- Source files: `10_sources/gilardi2023-chatgpt-annotation.md`, `10_sources/gilardi-et-al-2023-chatgpt-outperforms-crowd-workers-for-text-annotation-tasks.pdf`
- Source URL: https://doi.org/10.1073/pnas.2305016120
- Source status: available as converted Markdown in `10_sources/`; source identity verified against the PNAS title page and abstract during the 2026-05-04 one-by-one audit.

## Bibliographic metadata

- Title: "ChatGPT Outperforms Crowd Workers for Text-Annotation Tasks"
- Authors: Fabrizio Gilardi, Meysam Alizadeh, Mael Kubli
- Year: 2023
- Venue: PNAS, volume 120, number 30, e2305016120
- DOI: 10.1073/pnas.2305016120

## Detailed summary

Gilardi, Alizadeh, and Kubli test whether ChatGPT can perform social-science text annotation tasks more accurately and cheaply than MTurk crowd workers. The paper starts from a standard text-as-data problem: researchers need labeled examples to train supervised classifiers, evaluate unsupervised models, filter noisy corpora, assign topics, or code stance and frames. Traditionally, they use trained research assistants, crowd workers, or a combination of a small expert gold standard plus larger crowd annotation. The authors examine whether zero-shot ChatGPT can become a serious alternative for this annotation stage.

The study uses four samples of tweets and news articles totaling 6,183 documents. Three samples come from earlier work on content moderation discourse: tweets about content moderation from 2020-2021, news articles about content moderation from 2020-2021, and tweets by members of the US Congress from 2017-2022. A fourth 2023 tweet sample was added to reduce concern that ChatGPT might simply be memorizing texts included in its training data. The annotation tasks include relevance to content moderation, relevance to politics, stance toward Section 230, topic detection across predefined categories, a broad content-moderation frame task, and a policy-frame task with fourteen categories. The same codebooks were given to trained annotators, MTurk workers, and ChatGPT.

The source evaluates ChatGPT through the ChatGPT API using `gpt-3.5-turbo`, not GPT-4. The authors deliberately use zero-shot prompting and avoid ChatGPT-specific prompt optimization so that the comparison to MTurk is based on the same task instructions. They test two temperature settings, 1 and 0.2, and collect two ChatGPT responses for each temperature setting to compute ChatGPT intercoder agreement. MTurk workers were restricted to higher-quality profiles: MTurk Masters, approval rate above 90 percent, at least 50 approved HITs, and US location. Each text was annotated by two workers, and no worker could annotate more than 20 percent of a task.

The headline result is that ChatGPT's zero-shot accuracy is higher than MTurk for most tasks and about 25 percentage points higher on average across the four datasets. Accuracy is measured against trained annotators as the benchmark and only where trained annotators agreed. ChatGPT also has substantially higher intercoder agreement than both MTurk and trained annotators: the paper reports average agreement of roughly 56 percent for MTurk, 79 percent for trained annotators, 91 percent for ChatGPT at temperature 1, and 97 percent for ChatGPT at temperature 0.2. The lower temperature appears to increase consistency without reducing accuracy in this study. ChatGPT is also much cheaper, with per-annotation cost below 0.003 dollars, about thirty times cheaper than MTurk.

The paper is a performance and cost comparison, not a downstream-inference correction method. Its results support the claim that LLMs can be useful and efficient annotation tools for political-science text classification, but the source also flags limits. The tasks are demanding, performance varies by task, and ChatGPT struggled in one 2023 relevance task because the prompt lacked examples for tweets about specific user suspensions. The discussion calls for further research on multilingual performance, few-shot learning, semi-automated labeling systems, chain-of-thought prompting, and comparisons across LLM types.

## Research question

Can zero-shot ChatGPT perform common political-science text annotation tasks more accurately, consistently, and cheaply than MTurk crowd workers when both are given the same annotation codebooks?

## Core argument or contribution

The paper contributes early systematic evidence that ChatGPT can outperform crowd workers for several text-annotation tasks. Its core claim is comparative and practical: for the examined tweets and news articles, zero-shot ChatGPT produced more accurate and more internally consistent annotations than MTurk at a much lower cost. The paper therefore shows that LLMs can change the economics of creating labeled data for text-as-data research.

## Methodology

- Comparative annotation benchmark using four samples of tweets and news articles with trained-annotator labels as the benchmark.
- Annotation tasks: relevance, stance, topic detection, and frame detection, including a fourteen-category policy-frame task.
- Same task instructions/codebooks supplied to trained annotators, MTurk workers, and ChatGPT.
- ChatGPT annotations collected through the API with `gpt-3.5-turbo`, zero-shot prompts, temperatures 1 and 0.2, and two runs per temperature for agreement estimation.
- MTurk workers filtered for MTurk Masters status, high approval rate, minimum completed HITs, and US location.
- Evaluation metrics: accuracy against trained annotator agreement and intercoder agreement within annotator groups.
- Cost comparison between ChatGPT and MTurk.

## Datasets/materials used

The source uses four document samples totaling 6,183 texts: a random sample of 2,382 content-moderation tweets from January 2020 to April 2021, a random sample of 1,856 tweets by members of the US Congress from 2017-2022, a random sample of 1,606 content-moderation news articles from January 2020 to April 2021 collected via LexisNexis, and a January 2023 content-moderation tweet sample of 500 tweets, of which 339 were in English. The source also uses the authors' annotation codebooks and reports replication materials in Harvard Dataverse. It does not use Foerderkatalog, CORDIS, TRL, innovation-policy, or German industrial-policy datasets.

## Key findings

- ChatGPT's zero-shot accuracy exceeds MTurk accuracy by about 25 percentage points on average across the four datasets.
- ChatGPT outperforms MTurk for most tasks when trained annotator agreement is used as the benchmark.
- ChatGPT's intercoder agreement is higher than MTurk and trained annotators for all tasks in the study.
- Average intercoder agreement is reported as about 56 percent for MTurk, 79 percent for trained annotators, 91 percent for ChatGPT at temperature 1, and 97 percent for ChatGPT at temperature 0.2.
- ChatGPT's per-annotation cost is less than 0.003 dollars, around thirty times cheaper than MTurk.
- Lower temperature can improve consistency without reducing accuracy in this benchmark.
- Performance still varies by task, prompt, and task difficulty; the 2023 relevance task shows that missing examples or ambiguous cases can degrade performance.

## Limitations

The study covers English-language political-science annotation tasks based on tweets and news articles; it should not be generalized automatically to all languages, domains, or high-stakes coding settings. The benchmark uses trained annotator agreement as the reference, so disagreements among human experts remain relevant. The paper evaluates annotation accuracy and agreement, not whether downstream statistical analyses using ChatGPT labels remain unbiased. It uses `gpt-3.5-turbo` in early 2023 and does not evaluate GPT-4. The authors also note the need for further work on multilingual performance, few-shot prompting, semi-automated labeling, chain-of-thought, and comparisons across model types.

## Important concepts discussed

- [[30_concepts/llm-annotation-and-automated-coding.md]]
- [[30_concepts/text-as-data-computational-social-science.md]]
- [[30_concepts/foundation-models-and-pretrained-transformers.md]]
- Crowd annotation
- Gold-standard annotation
- Intercoder agreement
- Zero-shot annotation
- Annotation cost and scalability

## Methods discussed

- Zero-shot ChatGPT annotation
- Human expert annotation by trained research assistants
- MTurk crowd annotation
- Accuracy benchmarking against trained annotator agreement
- Intercoder-agreement comparison
- Temperature sensitivity checks
- [[40_methods/llm-few-shot-social-science.md]] as the closest canonical method note for LLM annotation/prompting, although this source's main design is zero-shot rather than few-shot

## Datasets discussed

- Content-moderation tweet samples from 2020-2021 and 2023
- US Congress tweet sample from 2017-2022
- Content-moderation news article sample from 2020-2021 via LexisNexis
- Harvard Dataverse replication materials for the PNAS article

## Relation to other papers in the vault

This paper provides one of the strongest early empirical justifications for using LLMs as annotation tools and should be read with [[20_summaries/pangakis2023-llm-annotation-validation.md]], [[20_summaries/halterman2025-codebook-llms.md]], [[20_summaries/ziems2024-llm-css-benchmark.md]], and [[20_summaries/tornberg2025-llm-outperform-experts.md]]. It also differs sharply from [[20_summaries/egami2024-llm-annotation-framework.md]]: Gilardi et al. evaluate annotation accuracy, agreement, and cost, while Egami et al. show why high annotation accuracy is still not sufficient when predicted labels are used in downstream statistical inference.

## Implications for LLM research or the project domain

For the Bundesinnovationshaushalt/TRL project, this paper supports the feasibility of using LLMs to reduce annotation cost and scale document coding. It does not by itself prove that LLM-generated TRL or policy-topic labels are valid for German funding data. The right project use is as evidence that LLM annotation can be competitive with crowd work when tasks are well specified, codebooks are clear, and validation against expert labels is possible. Any project claim about TRL classification should still run task-specific validation on Foerderkatalog texts and should use Egami et al. or a related measurement-error method if predicted labels enter statistical inference.

## Links to canonical concept, method, dataset, synthesis, and project notes

- Concepts: [[30_concepts/llm-annotation-and-automated-coding.md]], [[30_concepts/text-as-data-computational-social-science.md]], [[30_concepts/foundation-models-and-pretrained-transformers.md]]
- Methods: [[40_methods/llm-few-shot-social-science.md]]
- Datasets: no canonical vault dataset note applies directly
- Projects: [[70_projects/bundesinnovationshaushalt-trl.md]]
- Synthesis: [[90_synthesis/llm-text-classification-and-annotation.md]]
