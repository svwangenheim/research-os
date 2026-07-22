# XLM-RoBERTa: Multilingual Text Classification

*Added: 2026-04-15 | Source: lit_review_xlm_roberta_social_science.md*

---

## What Is XLM-RoBERTa? (Plain Language)

A language model is a computer program that has been trained on massive amounts of text — not to memorize it, but to learn patterns about how words, sentences, and ideas relate to each other. XLM-RoBERTa (pronounced "X-L-M Roberta," often shortened to XLM-R) is a language model developed by Meta AI and published in 2020 (Conneau et al., ACL 2020). What makes it unusual is that it was trained on more than 2.5 terabytes of text — roughly the equivalent of several million books — drawn from 100 different languages at the same time. Because it learned all of these languages together, it can work in German and English without needing separate models for each.

The underlying architecture is called a **transformer** (Vaswani et al., NeurIPS 2017). The key intuition: older language programs read text word by word, left to right, like a person reading a sentence for the first time. Transformers read the entire sentence at once and can immediately weigh every word against every other word. This means XLM-RoBERTa understands that "bank" means something completely different in "river bank" and "central bank" — not because it memorized these phrases, but because it learned that context determines meaning. For text that is dense with jargon and technical qualifiers (like R&D project descriptions), this context-sensitivity is essential.

A useful analogy: XLM-RoBERTa is like a highly educated person who grew up reading books and articles in 100 languages simultaneously. Before they ever see a single document about technology readiness levels, they already have an intuitive feel for how language works across all those languages — how technical vocabulary is structured, what hedging phrases look like, what distinguishes a description of a laboratory test from a description of a market-ready product. That accumulated background knowledge is called **pre-training**, and it is the model's most important advantage.

---

## What Is Fine-Tuning? (Plain Language)

Pre-training gives the model general language knowledge, but not task-specific knowledge. **Fine-tuning** is the step where we teach the model a specific task by showing it labeled examples. For TRL classification, this means showing the model roughly 1,000–2,500 project descriptions that have already been labeled with TRL scores (e.g., "this project is at TRL 3 — it has produced experimental proof of concept in a laboratory setting") and letting the model learn which patterns of language correspond to which TRL level.

The analogy is a doctor who already understands medicine in general being trained specifically in radiology: they already know anatomy and physiology; they just need to learn to read X-rays. The background knowledge dramatically reduces how much task-specific training is needed. For BERT-family models like XLM-RoBERTa, the literature consistently shows that 1,000–2,500 labeled examples are sufficient to substantially outperform classical machine learning methods that would require tens of thousands of examples (Timoneda and Vallejo Vera 2025, Journal of Politics; Laurer et al. 2023, Political Analysis; Zhang et al. 2021, ICLR). With fewer than 200 examples, results become unreliable; above 1,000, performance is generally stable, though running fine-tuning with multiple random seeds and reporting the mean and variance is still good practice (Zhang et al. 2021).

---

## Cross-Lingual Transfer: English Training → German Inference

Cross-lingual transfer means training a model on labeled data in one language and then applying it to text in a different language — without any translation. This is exactly the situation in the Bundesinnovationshaushalt TRL project: the labeled training data comes from CORDIS (EU Horizon Europe project descriptions, in English), while the inference target is the Foerderkatalog (German federal R&D projects, in German).

This works because XLM-RoBERTa was trained on German text too, at high quality. The model learned shared internal representations across languages — "Grundlagenforschung" and "basic research" map to similar places in the model's internal space, even though the model was never explicitly told they are translations of each other. Conneau et al. (2020) show that on cross-lingual benchmarks, XLM-RoBERTa substantially outperforms multilingual BERT: +14.6 percentage points average accuracy on XNLI (a multilingual inference benchmark) and +13% F1 on multilingual question answering. For high-resource language pairs like English and German, the typical accuracy loss from training in English and inferring in German is only **2–8 percentage points** on macro-F1 — a modest cost.

The more important risk is **domain shift**, not language shift. CORDIS project descriptions are EU-funded collaborative projects (often longer, more structured, international). Foerderkatalog entries are German federal projects (often shorter, different vocabulary, different funding logic). The model may encounter writing styles in the German data that look different from what it was trained on — even after language is held constant. Validating on a manually labeled German sample is therefore essential, and should be treated as a higher priority than worrying about the language boundary per se.

---

## Why Not Use a German-Only Model?

The main German-language BERT-family model is GBERT (Chan, Schweter, and Möller 2020, COLING), also available as `deepset/gbert-large` on Hugging Face. GBERT was trained exclusively on German text and performs marginally better than XLM-RoBERTa on German-only benchmarks: on GermEval 2018 document classification, GBERT-Large achieves a macro-F1 of 80.08 versus 78.38 for XLM-RoBERTa-Large — a gap of about 1–2 percentage points.

However, GBERT has no English pre-training and cannot process English text. This is decisive: because the labeled training data is in English (CORDIS), fine-tuning GBERT is not possible without first translating all training examples into German. XLM-RoBERTa handles both languages natively, making it the only practical choice when the training language and inference language differ. The 1–2 pp performance gap in GBERT's favor on German tasks is not worth sacrificing the cross-lingual capability. The only scenario where GBERT would be preferable is if all training data were machine-translated into German before fine-tuning — a feasible but unnecessary complication if XLM-RoBERTa achieves adequate performance on the task.

---

## What Accuracy to Expect

Accuracy for multi-class text classification is usually reported as **macro-F1**, a composite score between 0 and 1 that combines precision and recall for each class and averages them with equal weight across classes. "Equal weight" means that a rare category (say, TRL 1 projects) counts as much as a common one (TRL 6) — it is not diluted by class size. A macro-F1 of 1.0 would mean perfect classification on every class; 0.0 means the classifier is useless.

Based on the closest comparable studies in the literature, realistic benchmarks for XLM-RoBERTa fine-tuned on social science and policy text are:

- **Coarse 4-class classification** (like the BMLE groupings — Grundlagenforschung, Industrielle Forschung, Experimentelle Entwicklung, Marktreif): **macro-F1 typically 0.70–0.85**. Categories are more distinct and the decision boundaries are cleaner.
- **Fine-grained 9-class TRL classification** (TRL 1 through TRL 9): **macro-F1 typically 0.60–0.75**. Adjacent TRL levels share very similar language and are hard to distinguish even for domain experts.

These figures come from: Timoneda and Vallejo Vera (2025, Journal of Politics) on 8- and 20-class political science classification at 1,000 training examples; Kuzman Pungeršek et al. (2025) on 20+ class parliamentary speech classification achieving macro-F1 of 0.65–0.72; and Wang et al. (2024) on binary-to-multiclass political science tasks comparing fine-tuned BERT against GPT zero-shot at similar training set sizes. The coarser grouping will consistently outperform the fine-grained one because the language signals for "basic research" vs. "market-ready product" are much stronger than the signals for "TRL 4" vs. "TRL 5."

---

## Validation Protocol

The core rule for automated text classification in social science, established by Grimmer and Stewart (2013, Political Analysis), is: **all automated classifiers must be validated against human judgment on held-out data**. No classifier output should be reported as ground truth. The standard validation protocol has three components:

1. **Human annotation of a held-out test set.** Reserve a random sample of the target-language documents (100–200 is typically sufficient) from fine-tuning. Have at least two researchers independently assign TRL labels to this sample. Compute **Cohen's kappa** between raters. Kappa is a measure of agreement that adjusts for the amount of agreement you would expect by chance alone — a kappa of 0 means no better than random, a kappa of 1.0 means perfect agreement. The accepted threshold for "substantial" agreement is **kappa > 0.6** (Artstein and Poesio 2008, Computational Linguistics); kappa > 0.8 is "almost perfect." If human annotators cannot agree at kappa > 0.6, the classification task is probably not well-defined enough for a classifier to succeed.

2. **Compare model to human labels.** Report accuracy separately for each class, not just the overall score. **Grundlagenforschung (TRL 1–2) predictions are typically the least reliable** because the training examples are fewest and the language most abstract. Do not average this class-level variation away.

3. **Robustness check.** Following Grimmer and Stewart (2013), substantive findings (e.g., "German federal R&D spending is concentrated at TRL 4–6") should be checked against reasonable alternative specifications: different TRL grouping schemes, different confidence thresholds for class assignment, and direct comparison to the human-annotated subsample.

For the Bundesinnovationshaushalt project specifically, the CORDIS TRL labels are self-reported by project teams — not annotated by researchers. This self-reporting introduces label noise that puts a ceiling on achievable accuracy independent of model quality. Validation against a manually labeled German sample is therefore the most important quality check in the entire pipeline.

---

## Key Papers

| Paper                             | Venue                     | What It Shows                                                                                                                |
| --------------------------------- | ------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Conneau et al. (2020)             | ACL                       | XLM-RoBERTa foundation; multilingual pre-training at scale; +14.6 pp over multilingual BERT on cross-lingual benchmarks      |
| Timoneda and Vallejo Vera (2025)  | Journal of Politics       | Performance of XLM-RoBERTa vs. BERT/DeBERTa on 8–20 class policy text at 200–1,000 labeled examples                          |
| Laurer et al. (2023)              | Political Analysis        | NLI-based zero-shot classification as a strong low-annotation-cost baseline; 10.7–18.3 pp gain over classical ML             |
| Chan et al. (2020)                | COLING                    | XLM-RoBERTa vs. GBERT on German NLP benchmarks; small performance gap (~1–2 pp)                                              |
| Grimmer and Stewart (2013)        | Political Analysis        | Foundational validation standards for text classifiers in social science; the "validate, validate, validate" framework       |
| Zhang et al. (2021)               | ICLR                      | Fine-tuning instability at small sample sizes; recommendation to run multiple random seeds                                   |
| Artstein and Poesio (2008)        | Computational Linguistics | Inter-annotator agreement measures; kappa thresholds (>0.6 substantial, >0.8 almost perfect)                                 |
| Kuzman Pungeršek et al. (2025)    | arXiv                     | Real-world macro-F1 benchmark (0.69–0.76) for XLM-RoBERTa on 22-class EU parliamentary text via LLM teacher-student pipeline |
| Devlin et al. (2019)              | NAACL-HLT                 | BERT: foundational pre-train-then-fine-tune paradigm; bidirectional transformer; direct architectural ancestor of XLM-R      |
| Wang, Qu, and Ye (2024)           | arXiv                     | BERT vs. GPT-4o for 2–22-class political text classification: BERT wins at 8+ classes with ≥1,000 training examples          |
| Timoneda and Vallejo Vera (2025b) | PLOS ONE                  | Effect of masking rate (15–80%) on BERT/RoBERTa category-specific performance; 40% masking optimal for target categories     |

## Source summaries

- [[20_summaries/conneau2020-xlm-roberta.md]] — XLM-RoBERTa original paper: training setup, +14.6 pp over mBERT on XNLI, justification for English→German cross-lingual transfer
- [[20_summaries/devlin2019-bert.md]] — BERT original paper: pre-train/fine-tune paradigm, bidirectionality, fine-tuning instability at small N
- [[20_summaries/chan2020-gbert.md]] — GBERT/GELECTRA: German-only models; head-to-head vs. XLM-R on German benchmarks; justification for choosing XLM-R over GBERT
- [[20_summaries/zhang2021-few-shot-bert.md]] — Zhang et al. (ICLR 2021): root causes of fine-tuning instability; minimum ~1,000 training examples for reliable results; run 5–10 random seeds; use debiased ADAM
- [[20_summaries/wang2024-bert-vs-gpt.md]] — Wang, Qu, Ye (2024): BERT vs. GPT-4o across 2–22 class tasks; BERT dominates at 8+ classes with 1,000 samples; GPT competitive for binary tasks and as an annotator
- [[20_summaries/kuzman2025-parlacap.md]] — Kuzman Pungeršek et al. (2025): ParlaCAP — 8M European parliamentary speeches labeled via LLM teacher / XLM-RoBERTa student; macro-F1 0.69–0.76 on 22-class CAP labeling; closest methodological parallel to TRL project
- [[20_summaries/timoneda2025b-behind-the-mask.md]] — Timoneda and Vallejo Vera (2025b, PLOS ONE): masking rate tuning for domain-adaptive BERT pre-training; 40% masking improves target-category F1; recommendation to test 15%, 25%, 40%

---

## What it does

XLM-RoBERTa multilingual classification trains or fine-tunes a transformer
model on labeled text in one or more languages and applies it to target text in
another language. In this vault it is used as a robustness path for English
CORDIS labels to German Foerderkatalog project text.

## When to use it

Use it when labeled examples exist in one language but the target corpus is in
another, or when a non-generative robustness check is needed alongside LLM
classification.

## Assumptions

- Label definitions are stable across source and target languages.
- Training data are large and clean enough for fine-tuning.
- The target text has enough semantic content for classification.
- Multiple seeds and validation checks are used because small-sample fine-tuning
  can be unstable.

## Strengths and limitations

The strength is scalable, reproducible multilingual classification without API
dependence at inference time. Limitations include class imbalance, domain shift,
short-text ambiguity, and possible loss of nuance compared with human coding.

## Related concepts and datasets

- [[30_concepts/foundation-models-and-pretrained-transformers.md]]
- [[30_concepts/text-as-data-computational-social-science.md]]
- [[30_concepts/llm-annotation-and-automated-coding.md]]
- [[90_synthesis/llm-text-classification-and-annotation.md]]
- [[40_methods/trl-klassifikation-pipeline.md]]
- [[40_methods/llm-few-shot-social-science.md]]
- [[50_datasets/cordis-horizon-europe-h2020.md]]
- [[50_datasets/foerderkatalog-des-bundes.md]]
- [[30_concepts/technology-readiness-levels.md]]

## Relevant Projects

- [[70_projects/bundesinnovationshaushalt-trl]] — Bundesinnovationshaushalt TRL classification (Foerderkatalog-TRL-subproject): trains XLM-RoBERTa on CORDIS English labels, infers on German Foerderkatalog (39,555 active projects)
