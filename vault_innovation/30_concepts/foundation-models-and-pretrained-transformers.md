---
title: "Foundation Models and Pretrained Transformers"
note_type: concept
summary: "Foundation models and pretrained transformers are large neural language models trained on broad corpora and adapted to downstream tasks through prompting, fine-tuning, or transfer. In this vault they explain the model family behind BERT, RoBERTa, DeBERTa, GPT, XLM-R, and LLM classification workflows."
canonical: true
aliases:
  - foundation models
  - pretrained transformers
  - pretrained language models
  - transformer language models
  - BERT-family models
  - GPT-style models
related_notes:
  - "[[30_concepts/llm-annotation-and-automated-coding.md]]"
  - "[[30_concepts/text-as-data-computational-social-science.md]]"
  - "[[30_concepts/ai-production-adoption.md]]"
related_summaries:
  - "[[20_summaries/devlin2019-bert.md]]"
  - "[[20_summaries/conneau2020-xlm-roberta.md]]"
  - "[[20_summaries/brown2020-gpt3-fewshot.md]]"
  - "[[20_summaries/timoneda2025a-bert-roberta-deberta.md]]"
  - "[[20_summaries/timoneda2025b-behind-the-mask.md]]"
  - "[[20_summaries/wang2024-bert-vs-gpt.md]]"
  - "[[20_summaries/chan2020-gbert.md]]"
related_methods:
  - "[[40_methods/xlm-roberta-multilingual-classification.md]]"
  - "[[40_methods/llm-few-shot-social-science.md]]"
projects:
  - "[[70_projects/bundesinnovationshaushalt-trl.md]]"
tags:
  - concept
  - llm
  - transformer
  - pretrained-models
updated: "2026-04-29"
---

# Foundation Models and Pretrained Transformers

## Definition

Foundation models and pretrained transformers are language models trained on large, general corpora before being adapted to specific tasks. Transformer architecture makes it possible to model contextual relationships across tokens at scale. Pretraining gives the model broad linguistic and factual representations; downstream use then happens through fine-tuning, zero-shot prompting, one-shot or few-shot prompting, instruction tuning, or classifier heads.

In this vault, the concept covers the model family behind BERT, RoBERTa, DeBERTa, XLM-RoBERTa, GBERT, GPT-3, GPT-4-style models, and related LLM classifiers. It is a concept note, not a method note: specific workflows such as [[40_methods/xlm-roberta-multilingual-classification.md]] and [[40_methods/llm-few-shot-social-science.md]] describe how to use these models.

## Scope boundaries

Included:

- Transformer-based language models trained before downstream use.
- Encoder models such as BERT, RoBERTa, DeBERTa, GBERT, and XLM-R.
- Decoder/generative models such as GPT-3 and GPT-4-style LLMs.
- Transfer learning, pretraining, fine-tuning, prompting, and instruction tuning as adaptation modes.
- Model-family choice for social-science and administrative text classification.

Excluded:

- Non-language AI systems unless they are directly connected to text classification.
- General AI adoption in firms, which belongs in [[30_concepts/ai-production-adoption.md]].
- The project-specific TRL classification procedure, which belongs in [[40_methods/trl-klassifikation-pipeline.md]].

## Papers that discuss this concept

- [[20_summaries/devlin2019-bert.md]]: introduces BERT's pretrain-then-fine-tune paradigm and bidirectional transformer representation.
- [[20_summaries/conneau2020-xlm-roberta.md]]: extends the RoBERTa-style approach to multilingual pretraining and cross-lingual transfer.
- [[20_summaries/brown2020-gpt3-fewshot.md]]: shows that scaling autoregressive language models enables few-shot task performance through prompting.
- [[20_summaries/chan2020-gbert.md]]: discusses German-language BERT-style models and their relevance for German NLP.
- [[20_summaries/timoneda2025a-bert-roberta-deberta.md]]: compares BERT, RoBERTa, and DeBERTa for political text classification.
- [[20_summaries/timoneda2025b-behind-the-mask.md]]: examines domain-adaptive pretraining choices for classification.
- [[20_summaries/wang2024-bert-vs-gpt.md]]: compares fine-tuned BERT-family models with GPT-style models for political text classification.
- [[20_summaries/chae2025-llm-instruction-tuning.md]]: studies the interaction of instruction tuning and in-context learning.

## How the papers use, support, challenge, or modify it

The BERT and XLM-R papers support the encoder model tradition: pretrain a contextual representation and fine-tune it for classification. The GPT-3 paper supports the prompting tradition: at sufficient scale, a model can perform a task from a natural-language instruction plus examples. The newer political and social-science papers compare these traditions under practical constraints: label count, training examples, multilinguality, domain vocabulary, cost, and validation burden.

For the Foerderkatalog project, this concept keeps model-family choices separate from project-specific method claims. XLM-R is attractive because it supports multilingual transfer and classification; GPT-style models are attractive because they can classify with few examples and rich prompts; both require validation against the TRL construct and German administrative text.

## Related concepts

- [[30_concepts/llm-annotation-and-automated-coding.md]]
- [[30_concepts/text-as-data-computational-social-science.md]]
- [[30_concepts/ai-production-adoption.md]]
- [[30_concepts/data-access-for-innovation-policy.md]]

## Related methods and datasets

- [[40_methods/xlm-roberta-multilingual-classification.md]]
- [[40_methods/llm-few-shot-social-science.md]]
- [[40_methods/llm-few-shot-applicability-trl-förderkatalog.md]]
- [[40_methods/trl-klassifikation-pipeline.md]]
- [[50_datasets/foerderkatalog-des-bundes.md]]

## Open questions and tensions

- When does task-specific fine-tuning beat few-shot prompting for small or imbalanced label sets?
- How stable are LLM classifications across repeated runs and prompt variants?
- How well do English benchmark findings transfer to German administrative text?
- When does domain-adaptive pretraining improve classification enough to justify cost?
- How should model choice be explained to non-technical policy audiences?

## Retrieval links

Use this note for model-family queries about BERT, RoBERTa, DeBERTa, GPT, XLM-R, pretrained language models, foundation models, transformers, and the tradeoff between prompting and fine-tuning.
