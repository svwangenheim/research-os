---
title: "Large Language Models for Text Classification: From Zero-Shot Learning to Instruction-Tuning"
note_type: source_summary
authors:
  - Youngjin Chae
  - Thomas Davidson
year: 2025
source_files:
  - 10_sources/chae_davidson_2025_converted.md
  - 10_sources/chae2025-llm-instruction-tuning.md
projects:
  - bundesinnovationshaushalt-trl
tags:
  - source-summary
  - instruction-tuning
  - few-shot-learning
  - text-classification
  - llm
  - computational-social-science
updated: 2026-05-04
---

# Chae & Davidson (2025) - Large Language Models for Text Classification

## Source paper link/path

- Source file: `10_sources/chae2025-llm-instruction-tuning.md`
- Source status: available as converted Markdown in `10_sources/`
- Audit status: checked one-by-one against the mapped source on 2026-05-04.

## Bibliographic metadata

- Title: Large Language Models for Text Classification: From Zero-Shot Learning to Instruction-Tuning
- Authors: Youngjin Chae and Thomas Davidson
- Venue/status: forthcoming at Sociological Methods & Research, according to the source
- Year: 2025
- Keywords in source: large language models, supervised text classification, natural language processing, stance detection, computational social science

## Detailed summary

Chae and Davidson evaluate how large language models perform as tools for supervised text classification in social-science research. Their empirical case is stance detection: classifying whether social-media texts express support, opposition, or neutrality toward political candidates in the 2016 US presidential election.

The paper is designed as a practical methodological comparison. It asks how predictive accuracy varies across model architectures, model sizes, learning regimes, prompt designs, amounts of training data, and task complexity. The authors compare ten models ranging from small encoder models to state-of-the-art proprietary LLMs. The model set includes BERT, SBERT, DeBERTa, FLAN-T5 XXL, Mistral-7B, Llama3-8B, Llama3-70B, GPT-3 Ada, GPT-3 Davinci, and GPT-4o, along with conventional baselines such as SVM and CNN variants using bag-of-words or GloVe features.

The paper studies three main text-classification settings. First, it evaluates prompt-based zero-shot classification, where models receive task instructions without training examples. Second, it evaluates few-shot prompting, where examples are placed in the prompt. Third, it evaluates fine-tuning with annotated data. It also introduces a more complex structured-output setting for comment-reply threads, where a model predicts the stance of an original comment and the stances of associated replies. For this thread task, the paper uses instruction tuning: training models with instructions and paired structured inputs/outputs.

The evidence comes from three stance-detection datasets: a benchmark Twitter stance-detection dataset from Mohammad et al. (2016) and two newly annotated Facebook datasets. The Facebook tasks focus on comments and comment-reply threads about Hillary Clinton and Donald Trump. This lets the authors compare performance on related but distinct stance-detection tasks, and it lets them test both simple single-text classification and more structured conversational classification.

The main pattern is that the strongest proprietary models perform well with little or no task-specific training, but the cost/accuracy tradeoff is not one-dimensional. GPT-4o performs very strongly, including on Facebook comment stance prediction without task-specific training. However, smaller fine-tuned models can be competitive because they are cheaper and accurate when annotated training data are available. The paper also finds that open-weights models have become much stronger: Llama3-70B performs comparably to GPT-4o on thread prediction using prompts alone and improves further after instruction tuning.

The authors emphasize that prompt-based performance is sensitive to the prompt and to the examples used. They also emphasize that model choice depends on corpus size, available labeled data, computational resources, privacy constraints, reproducibility needs, and whether researchers need a proprietary API or an open-weights workflow. The paper's practical message is not "always use the largest model"; it is that researchers should choose learning regimes and model families based on task complexity, data availability, cost, and validation evidence.

## Research question

How well do LLMs perform on supervised text classification for social-science research, and how does performance vary across model architecture, model size, zero-shot prompting, few-shot prompting, fine-tuning, and instruction tuning?

## Core argument or contribution

The paper contributes a systematic empirical comparison of LLM-based text-classification strategies for sociological research. It shows that large proprietary LLMs can be strong zero-shot and prompt-based classifiers, that smaller fine-tuned models remain competitive and cost-effective when labeled data are available, and that instruction-tuned open-weights models can handle more complex structured classification tasks.

## Methodology

The authors use supervised stance detection as a case study. They compare conventional machine-learning baselines, encoder models, encoder-decoder and decoder-only open-weights LLMs, and proprietary GPT models across zero-shot prompting, few-shot prompting, fine-tuning, and instruction tuning. They evaluate predictive performance using held-out data and report task-specific F1, precision, and recall metrics.

For larger open-weights models, the paper uses fine-tuning approaches including QLoRA to adapt models efficiently. For proprietary models, experiments are run through the OpenAI API. For thread prediction, the authors construct structured prompts/outputs so the model predicts multiple stances within comment-reply threads.

## Datasets/materials used

- Twitter stance-detection benchmark dataset from Mohammad et al. (2016).
- Two newly annotated Facebook stance-detection datasets focused on 2016 US presidential-candidate discussions.
- Comment-reply thread materials for structured stance prediction.
- Model families: BERT, SBERT, DeBERTa, FLAN-T5 XXL, Mistral-7B, Llama3-8B, Llama3-70B, GPT-3 Ada, GPT-3 Davinci, GPT-4o, and conventional SVM/CNN baselines.

No Foerderkatalog or CORDIS data is used.

## Key findings

- Large proprietary models can deliver strong zero-shot and prompt-based performance on stance detection.
- GPT-4o outperforms fine-tuned models for Facebook comment stance prediction without task-specific training in the authors' experiments.
- Prompt-based performance depends on prompt length, prompt detail, and example selection.
- Fine-tuned smaller models can be competitive because they combine relatively high accuracy with lower deployment cost when labeled training data are available.
- Large open-weights models are increasingly competitive: Llama3-70B performs comparably to GPT-4o for thread prediction using prompts alone and improves after instruction tuning.
- Fine-tuning large open-weights models is not always the best use of resources; the paper reports that smaller models can rival or beat larger open-weights models in some fine-tuning settings.
- Instruction tuning is especially useful for complex structured-output tasks such as predicting multiple stances within comment-reply threads.
- Researchers should choose between proprietary models and open-weights models by considering accuracy, cost, transparency, reproducibility, privacy, and infrastructure.

## Limitations

- The empirical case is stance detection around the 2016 US presidential election; results may not generalize to all classification tasks or domains.
- Prompt-based models are sensitive to prompt wording and example composition.
- Proprietary APIs create reproducibility, transparency, cost, and privacy concerns.
- Open-weights models require local or cloud compute infrastructure and technical expertise.
- The paper evaluates text classification, not causal inference or downstream substantive validity of social-science claims.
- The paper does not validate TRL classification, German-language innovation-policy coding, or Foerderkatalog project classification.

## Important concepts discussed

- [[30_concepts/llm-annotation-and-automated-coding.md]]
- [[30_concepts/text-as-data-computational-social-science.md]]
- [[30_concepts/foundation-models-and-pretrained-transformers.md]]

## Methods discussed

- [[40_methods/llm-few-shot-social-science.md]]

Candidate method for wiki-maintain: instruction tuning for structured text classification.

## Datasets discussed

No canonical vault dataset note is linked. The paper uses political stance-detection datasets rather than innovation-policy datasets.

## Relation to other papers in the vault

- Extends the few-shot paradigm introduced in [[20_summaries/brown2020-gpt3-fewshot.md]] into an applied social-science classification setting.
- Complements [[20_summaries/gilardi2023-chatgpt-annotation.md]], [[20_summaries/pangakis2023-llm-annotation-validation.md]], [[20_summaries/egami2024-llm-annotation-framework.md]], and [[20_summaries/ziems2024-llm-css-benchmark.md]] by focusing on model/regime choice rather than only human-versus-LLM annotation.
- Contrasts with encoder/fine-tuning baselines in [[20_summaries/devlin2019-bert.md]], [[20_summaries/conneau2020-xlm-roberta.md]], [[20_summaries/chan2020-gbert.md]], and [[20_summaries/timoneda2025a-bert-roberta-deberta.md]].

## Implications for LLM research or the project domain

For the Bundesinnovationshaushalt/TRL project, this paper supports a validation-first approach to LLM classification. It justifies comparing prompt-only, few-shot, fine-tuned, and possibly instruction-tuned approaches depending on the amount of labeled data and the complexity of the coding scheme. It also cautions that project classification should not rely on an untested prompt: prompts, exemplars, model choice, cost, reproducibility, privacy, and error patterns must be evaluated on labeled validation data.

The paper does not itself prove that Claude, GPT-4o, or any other model can classify German Foerderkatalog projects by TRL. That remains a downstream project-specific validation task.

## Links to canonical concept, method, dataset, synthesis, and project notes

- [[30_concepts/llm-annotation-and-automated-coding.md]]
- [[30_concepts/text-as-data-computational-social-science.md]]
- [[30_concepts/foundation-models-and-pretrained-transformers.md]]
- [[40_methods/llm-few-shot-social-science.md]]
- [[90_synthesis/llm-text-classification-and-annotation.md]]
- [[70_projects/bundesinnovationshaushalt-trl.md]]

## Semantic verification details

Checked one-by-one against `10_sources/chae2025-llm-instruction-tuning.md` on 2026-05-04. Use this note for LLM text-classification regime comparisons, stance-detection evidence, instruction tuning, model/cost tradeoffs, and methodological cautions. Do not cite it as direct evidence about Foerderkatalog, CORDIS, TRL classifier accuracy, or German innovation-policy coding without separate validation.
