---
title: "Language Models are Few-Shot Learners"
note_type: source_summary
authors: ["Tom B. Brown", "Benjamin Mann", "Nick Ryder", "Melanie Subbiah", "Jared Kaplan", "Prafulla Dhariwal", "Arvind Neelakantan", "Pranav Shyam", "Girish Sastry", "Amanda Askell", "Sandhini Agarwal", "Ariel Herbert-Voss", "Gretchen Krueger", "Tom Henighan", "Rewon Child", "Aditya Ramesh", "Daniel M. Ziegler", "Jeffrey Wu", "Clemens Winter", "Christopher Hesse", "Mark Chen", "Eric Sigler", "Mateusz Litwin", "Scott Gray", "Benjamin Chess", "Jack Clark", "Christopher Berner", "Sam McCandlish", "Alec Radford", "Ilya Sutskever", "Dario Amodei"]
year: 2020
source_files: ["10_sources/brown2020-gpt3-fewshot.md"]
source_urls: ["https://arxiv.org/abs/2005.14165"]
projects: [bundesinnovationshaushalt-trl]
tags: [source-summary, llm, few-shot-learning, gpt-3, nlp, in-context-learning]
updated: "2026-05-04"
---

# Brown et al. (2020) - Language Models are Few-Shot Learners

## Source paper link/path

- Source file: `10_sources/brown2020-gpt3-fewshot.md`
- Source status: available as converted Markdown in `10_sources/`
- Audit status: checked one-by-one against the mapped source on 2026-05-04.

## Bibliographic metadata

- Title: Language Models are Few-Shot Learners
- Authors: Tom B. Brown et al.
- Institution: OpenAI
- Year: 2020
- Venue/source: arXiv / NeurIPS 2020 paper version in the vault
- URL: https://arxiv.org/abs/2005.14165

## Detailed summary

Brown et al. introduce GPT-3, a 175-billion-parameter autoregressive transformer language model, and evaluate whether scaling language models improves task performance without task-specific fine-tuning. The paper is foundational for in-context learning: it shows that large language models can perform many tasks from natural-language instructions and a small number of demonstrations placed in the prompt, with no gradient updates at test time.

The motivation is a limitation of the dominant pretrain-then-fine-tune paradigm. Fine-tuned NLP models can perform well on benchmarks, but they usually require thousands or tens of thousands of task-specific labeled examples. Humans often learn a new language task from instructions or a few examples. The paper asks whether a sufficiently large pretrained language model can display similar sample efficiency at inference time.

The authors train a family of GPT-3 models from 125 million parameters to 175 billion parameters. The largest model, GPT-3, has 96 layers, a 12,288-dimensional model width, 96 attention heads, and a 2,048-token context window. All models are trained for 300 billion tokens. The architecture follows GPT-2-style autoregressive language modeling with modifications including alternating dense and locally banded sparse attention patterns.

The training corpus is a mixture of filtered Common Crawl, WebText2, Books1, Books2, and English-language Wikipedia. Common Crawl is filtered for quality using similarity to curated reference corpora, fuzzily deduplicated, and mixed with higher-quality corpora. The final training mix gives 60 percent weight to filtered Common Crawl, 22 percent to WebText2, 8 percent to Books1, 8 percent to Books2, and 3 percent to Wikipedia, with the authors intentionally oversampling higher-quality datasets relative to their raw size.

The evaluation design compares zero-shot, one-shot, and few-shot settings. In zero-shot evaluation, the model receives a natural-language task instruction but no examples. In one-shot evaluation, it receives one demonstration plus an instruction. In few-shot evaluation, it receives as many demonstrations as fit in the 2,048-token context window, typically 10 to 100 examples, but still no weight updates. This is the key distinction: GPT-3 adapts through conditioning on the prompt rather than through fine-tuning.

GPT-3 is evaluated across language modeling, cloze and completion, closed-book question answering, translation, Winograd-style tasks, commonsense reasoning, reading comprehension, SuperGLUE, natural language inference, arithmetic, word unscrambling, novel-word use, and synthetic news generation. The paper reports that performance generally improves with model scale, and that the performance gap between zero-shot, one-shot, and few-shot settings often widens for larger models, suggesting that larger models are better in-context learners.

The paper is careful about limitations. GPT-3 still struggles on some tasks, including ANLI and some reading-comprehension datasets such as RACE and QuAC. Its few-shot performance is often below fine-tuned state-of-the-art systems. The authors also study benchmark contamination because web-scale training data can contain benchmark examples; a filtering bug meant some overlaps remained, so the paper reports contamination analysis and flags affected results. The paper also discusses misuse, bias/fairness, representation, and energy use.

## Research question

Can very large autoregressive language models perform new NLP tasks from instructions and a few examples in the prompt, without task-specific gradient updates or fine-tuning?

## Core argument or contribution

Scaling language models substantially improves zero-shot, one-shot, and few-shot in-context performance. GPT-3 shows that a single pretrained model can perform many language tasks from prompt-based task descriptions and demonstrations, although it remains weaker than fine-tuned systems on some benchmarks and raises contamination, bias, misuse, and compute concerns.

## Methodology

The authors train eight autoregressive transformer language models from 125M to 175B parameters on a large mixed text corpus. They evaluate each model under zero-shot, one-shot, and few-shot prompting conditions across many NLP datasets. Few-shot examples are supplied only in the context window, with no gradient updates. The authors also conduct data-contamination analysis by checking overlap between training data and benchmark development/test sets.

## Datasets/materials used

Training materials:

- Filtered Common Crawl, downloaded from 41 monthly shards covering 2016-2019.
- WebText2.
- Books1.
- Books2.
- English-language Wikipedia.

Evaluation materials include many NLP benchmarks and tasks, such as LAMBADA, StoryCloze, closed-book QA datasets including CoQA and TriviaQA, translation benchmarks, Winograd-style tasks, commonsense reasoning tasks, reading-comprehension tasks, SuperGLUE, NLI tasks including ANLI, arithmetic tasks, word-scrambling tasks, novel-word-use tasks, and human evaluation of synthetic news samples.

No Foerderkatalog, CORDIS, or German innovation-policy dataset is used in the paper.

## Key findings

- GPT-3 has 175 billion parameters and is evaluated without task-specific fine-tuning.
- Larger models generally perform better in zero-shot, one-shot, and few-shot settings.
- Few-shot performance often improves more rapidly with scale than zero-shot performance, suggesting stronger in-context learning in larger models.
- GPT-3 is competitive with prior fine-tuned systems on some tasks, including some closed-book QA and language tasks, but not consistently across all benchmarks.
- Prompt demonstrations reduce the need for task-specific labeled data, but do not eliminate the need for careful task formulation and examples.
- GPT-3 performs well on several rapid-adaptation tasks, including arithmetic, word unscrambling, and novel-word use, while still failing or underperforming on other reasoning and reading-comprehension tasks.
- Large web-trained models create benchmark-contamination risks; the authors attempted filtering and then analyzed remaining overlap.
- Human evaluators had difficulty distinguishing some GPT-3-generated news articles from human-written articles, motivating broader-impact discussion.
- The paper highlights risks around misuse, bias and representation, and energy use.

## Limitations

- Few-shot GPT-3 often remains below fine-tuned task-specific systems.
- Results are sensitive to prompt format, task wording, context examples, and available context length.
- The paper does not show that GPT-3 learns from errors or updates its weights at inference time.
- Some benchmark results are affected by possible training-data contamination.
- The model struggles on tasks such as ANLI and some reading-comprehension datasets.
- The paper is not about social-science annotation reliability, German text classification, or policy-document coding; those are downstream applications that require separate validation.
- The paper predates later instruction tuning, RLHF, tool use, and modern chat-model interfaces.

## Important concepts discussed

- [[30_concepts/foundation-models-and-pretrained-transformers.md]]
- [[30_concepts/llm-annotation-and-automated-coding.md]]
- [[30_concepts/text-as-data-computational-social-science.md]]

## Methods discussed

- [[40_methods/llm-few-shot-social-science.md]]

The method link is a downstream social-science use of the few-shot paradigm; Brown et al. themselves evaluate general NLP tasks, not social-science coding protocols.

## Datasets discussed

No canonical vault dataset note is linked. The paper discusses model-training corpora and NLP benchmarks rather than the project's innovation-policy datasets.

## Relation to other papers in the vault

- Provides the foundational in-context learning mechanism used by later LLM annotation papers such as [[20_summaries/gilardi2023-chatgpt-annotation.md]], [[20_summaries/egami2024-llm-annotation-framework.md]], [[20_summaries/pangakis2023-llm-annotation-validation.md]], and [[20_summaries/ziems2024-llm-css-benchmark.md]].
- Contrasts with encoder/fine-tuning approaches represented by [[20_summaries/devlin2019-bert.md]], [[20_summaries/conneau2020-xlm-roberta.md]], [[20_summaries/chan2020-gbert.md]], and [[20_summaries/zhang2021-few-shot-bert.md]].
- Supports the LLM classification synthesis in [[90_synthesis/llm-text-classification-and-annotation.md]].

## Implications for LLM research or the project domain

For the Bundesinnovationshaushalt/TRL project, this paper supports the basic idea that a large language model can perform classification-like tasks from instructions and prompt examples without training a bespoke classifier. It does not by itself validate TRL classification of German funding projects. Any use for Foerderkatalog coding still needs task-specific prompt design, German-language evaluation, calibration examples, error analysis, and human review.

## Links to canonical concept, method, dataset, synthesis, and project notes

- [[30_concepts/foundation-models-and-pretrained-transformers.md]]
- [[30_concepts/llm-annotation-and-automated-coding.md]]
- [[30_concepts/text-as-data-computational-social-science.md]]
- [[40_methods/llm-few-shot-social-science.md]]
- [[90_synthesis/llm-text-classification-and-annotation.md]]
- [[70_projects/bundesinnovationshaushalt-trl.md]]

## Semantic verification details

Checked one-by-one against `10_sources/brown2020-gpt3-fewshot.md` on 2026-05-04. Use this note for GPT-3, in-context learning, zero/one/few-shot prompting, model scaling, web-scale pretraining, benchmark evaluation, and limitations. Do not cite it as direct evidence about Foerderkatalog, CORDIS, TRL classification performance, or German policy-document coding reliability.
