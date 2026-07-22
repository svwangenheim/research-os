---
title: "German's Next Language Model"
note_type: source_summary
authors: ["Branden Chan", "Stefan Schweter", "Timo Moeller"]
year: 2020
source_files: ["10_sources/chan2020-gbert.md"]
source_urls:
  - "https://aclanthology.org/2020.coling-main.598"
projects: [bundesinnovationshaushalt-trl]
tags: [source-summary, nlp, german-nlp, bert, gbert, gelectra, text-classification, monolingual]
updated: "2026-05-04"
---

# Chan, Schweter & Moeller (2020) - German's Next Language Model

## Source paper link/path

- Source file: `10_sources/chan2020-gbert.md`
- Source status: available as converted Markdown in `10_sources/`
- Audit status: checked one-by-one against the mapped source on 2026-05-04.

## Bibliographic metadata

- Title: German's Next Language Model
- Authors: Branden Chan, Stefan Schweter, Timo Moeller
- Venue: Proceedings of the 28th International Conference on Computational Linguistics (COLING 2020)
- Year: 2020
- URL: https://aclanthology.org/2020.coling-main.598

## Detailed summary

Chan, Schweter, and Moeller introduce GBERT and GELECTRA, German-language transformer models based on BERT and ELECTRA. The paper is an applied model-development and evaluation study: it asks how German NLP performance changes when the authors vary pretraining data, model size, model architecture, and Whole Word Masking.

The motivation is that German NLP can benefit from language-specific pretrained models rather than relying only on multilingual models such as mBERT or XLM-RoBERTa. The authors train German BERT and ELECTRA variants and evaluate them on German document classification and named entity recognition tasks. Their best model, GELECTRALarge, sets new state-of-the-art results on the evaluated German benchmarks at the time.

The pretraining corpus combines several German text sources. OSCAR, a German Common Crawl-derived corpus, contributes 145 GB and makes up the dominant share of the training data. OPUS contributes about 10 GB from sources such as subtitles, parliamentary speech, and books. German Wikipedia contributes about 6 GB. OpenLegalData contributes about 2.4 GB of German court decisions. In total, the source describes roughly 163 GB of German text.

The paper trains seven new models. The BERT variants include GBERTData, GBERTWWM, GBERTData + WWM, and GBERTLarge. These vary whether they use all available data, Whole Word Masking, and base versus large model size. The ELECTRA variants include GELECTRA, GELECTRAData, and GELECTRALarge. ELECTRA uses replaced-token detection instead of masked language modeling, allowing training signal at every token position rather than only masked tokens.

Evaluation is downstream-driven. Rather than simply saving a model after a fixed number of pretraining steps, the authors checkpoint during pretraining, fine-tune checkpoints on downstream tasks, and select the checkpoint with the best downstream performance. The downstream tasks are GermEval18 Coarse and GermEval18 Fine for offensive-language classification, plus GermEval14 for German named entity recognition.

The results show that more German pretraining data helps, but the gains are modest; Whole Word Masking consistently improves BERT variants; larger models outperform base models; and GELECTRA is especially efficient. GELECTRALarge improves over prior state of the art by about 3.93 percentage points on GermEval18 Coarse, 2.45 points on GermEval18 Fine, and 4.3 points on GermEval14. The paper reports that GBERTLarge reaches an average F1 of 73.57 across the three tasks and GELECTRALarge reaches 74.94, compared with 73.18 for XLM-RoBERTaLarge in their evaluation table.

The paper also explicitly warns about biases and harmful content in web-derived pretraining data. Because OSCAR is scraped from the internet and makes up most of the training corpus, the authors caution that the models may reflect explicit content, misinformation, and gender, racial, or religious biases. They advise careful consideration before deployment in sensitive settings.

## Research question

How can German BERT and ELECTRA models be trained and evaluated so that they improve German document classification and named entity recognition, and how do pretraining data volume, Whole Word Masking, model size, and ELECTRA-style pretraining affect performance?

## Core argument or contribution

The paper contributes publicly available German GBERT and GELECTRA models and shows that more German pretraining data, Whole Word Masking, larger model size, and ELECTRA-style replaced-token detection can improve German NLP performance on the evaluated benchmarks.

## Methodology

The authors pretrain German BERT and ELECTRA variants using German corpora, checkpoint models during training, fine-tune checkpoints on downstream tasks, and select final checkpoints based on downstream performance. They compare their models with existing German BERT models, mBERT, and XLM-RoBERTaLarge.

Downstream evaluation tasks:

- GermEval18 Coarse: binary offensive-language classification.
- GermEval18 Fine: four-class offensive-language classification.
- GermEval14: German named entity recognition with nested annotation categories.

## Datasets/materials used

Pretraining data:

- OSCAR German Common Crawl corpus: 145 GB.
- OPUS: 10 GB.
- German Wikipedia: 6 GB.
- OpenLegalData: 2.4 GB.

Evaluation data:

- GermEval18 Coarse and Fine offensive-language classification datasets.
- GermEval14 named entity recognition dataset.

No Foerderkatalog, CORDIS, or TRL-labeled dataset is used.

## Key findings

- GELECTRALarge is the strongest model in the paper's benchmark table, with average F1 of 74.94 across GermEval18 Coarse, GermEval18 Fine, and GermEval14.
- GBERTLarge reaches average F1 of 73.57 across the three tasks.
- XLM-RoBERTaLarge reaches average F1 of 73.18 in the same table, making it competitive but below the best German-specific models in this evaluation.
- Adding all available data produces consistent but modest improvements: the paper reports +0.25, +0.93, and +1.59 percentage-point improvements in relevant comparisons.
- Whole Word Masking improves BERT variants: GBERTWWM outperforms DBMDZ BERTBase by +1.70 points, and GBERTData + WWM outperforms GBERTData by +2.38 points.
- Larger models outperform base models, though the paper notes that large models also saw more tokens under their training regimes, so pure model-size effects are not fully isolated.
- GELECTRALarge outperforms GBERTLarge despite seeing fewer tokens, supporting the efficiency of ELECTRA-style pretraining.

## Limitations

- The evaluation is limited to German offensive-language classification and German NER benchmarks; results may not transfer to all German NLP tasks.
- Model-size effects are not perfectly isolated because large models saw different amounts of data under the training regimes.
- Some models may still be undertrained, and the authors note upward trends late in training.
- The dominant OSCAR training corpus is web-derived and may contain explicit material, misinformation, and social biases.
- The paper evaluates German NLP benchmarks, not TRL classification, innovation-policy text, or Foerderkatalog project descriptions.
- GBERT/GELECTRA are monolingual German models and do not solve cross-lingual transfer from English labeled data to German inference data.

## Important concepts discussed

- [[30_concepts/foundation-models-and-pretrained-transformers.md]]
- [[30_concepts/text-as-data-computational-social-science.md]]
- [[30_concepts/llm-annotation-and-automated-coding.md]]

## Methods discussed

- [[40_methods/xlm-roberta-multilingual-classification.md]]

The XLM-RoBERTa method link is relevant as a comparison point; the source itself is about German monolingual GBERT/GELECTRA models.

## Datasets discussed

No canonical vault dataset note is linked. The paper uses German NLP pretraining corpora and GermEval benchmarks, not innovation-policy datasets.

## Relation to other papers in the vault

- Builds on BERT-style transformer pretraining described in [[20_summaries/devlin2019-bert.md]].
- Provides a German-language comparison point for multilingual approaches such as [[20_summaries/conneau2020-xlm-roberta.md]].
- Relates to later classification-method papers such as [[20_summaries/timoneda2025a-bert-roberta-deberta.md]] and [[20_summaries/chae2025-llm-instruction-tuning.md]] through the choice between encoder fine-tuning, multilingual models, and generative LLMs.

## Implications for LLM research or the project domain

For the Bundesinnovationshaushalt/TRL project, this paper is useful as evidence that German-specific transformer models can perform strongly on German classification and NER benchmarks. It does not itself determine the best model for TRL classification. A project model choice between GBERT/GELECTRA and XLM-RoBERTa should depend on whether labeled training data are German, whether cross-lingual transfer is needed, and whether validation on Foerderkatalog-like texts confirms the expected performance.

## Links to canonical concept, method, dataset, synthesis, and project notes

- [[30_concepts/foundation-models-and-pretrained-transformers.md]]
- [[30_concepts/text-as-data-computational-social-science.md]]
- [[30_concepts/llm-annotation-and-automated-coding.md]]
- [[40_methods/xlm-roberta-multilingual-classification.md]]
- [[90_synthesis/llm-text-classification-and-annotation.md]]
- [[70_projects/bundesinnovationshaushalt-trl.md]]

## Semantic verification details

Checked one-by-one against `10_sources/chan2020-gbert.md` on 2026-05-04. Use this note for GBERT/GELECTRA, German monolingual transformer pretraining, Whole Word Masking, ELECTRA-style replaced-token detection, German benchmark performance, and web-corpus bias cautions. Do not cite it as direct evidence about Foerderkatalog, CORDIS, TRL classification accuracy, R&D subsidy effects, or German innovation-policy outcomes.
