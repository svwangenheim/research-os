---
title: "LLM Few-Shot Classification for TRL: Applicability Analysis & Best Practices"
note_type: method
summary: "Detailed analysis of when LLM few-shot classification is appropriate, why it's suitable for TRL classification of the German Förderkatalog, and comprehensive best practices based on latest research (Egami 2024, Ornstein 2025, Chae 2025, Pelaez 2024, Gilardi 2023)."
related_notes:
  - "40_methods/llm-few-shot-social-science.md"
  - "40_methods/trl-klassifikation-pipeline.md"
  - "20_summaries/gilardi2023-chatgpt-annotation.md"
  - "20_summaries/egami2024-llm-annotation-framework.md"
  - "20_summaries/ornstein2025-stochastic-parrot.md"
  - "20_summaries/pelaez2024-patent-public-value-llm.md"
  - "20_summaries/chae2025-llm-instruction-tuning.md"
projects: [bundesinnovationshaushalt-trl]
tags:
  - llm
  - few-shot
  - classification
  - applicability
  - best-practices
updated: "2026-04-27"
---

# LLM Few-Shot Classification for TRL: When & How

## Canonical links

- [[40_methods/llm-few-shot-social-science.md]]
- [[40_methods/trl-klassifikation-pipeline.md]]
- [[20_summaries/gilardi2023-chatgpt-annotation.md]]
- [[20_summaries/egami2024-llm-annotation-framework.md]]
- [[20_summaries/ornstein2025-stochastic-parrot.md]]
- [[20_summaries/pelaez2024-patent-public-value-llm.md]]
- [[20_summaries/chae2025-llm-instruction-tuning.md]]
- [[70_projects/bundesinnovationshaushalt-trl.md]]

This note is a project-facing method interpretation. The broader canonical
method note for LLM annotation in social-science workflows remains
[[40_methods/llm-few-shot-social-science.md]], and the project implementation
method remains [[40_methods/trl-klassifikation-pipeline.md]].

## Part 1: When is Few-Shot Classification Appropriate?

Based on Egami et al. (2024), Ornstein et al. (2025), and Chae & Davidson (2025), use **LLM few-shot classification** when:

### ✅ **Use Few-Shot When All of These Are True:**

| Criterion                                      | Your Project                                    | Status                                |
| ---------------------------------------------- | ----------------------------------------------- | ------------------------------------- |
| **Labeled training data scarce**               | <500 examples with ground-truth TRL labels      | ✅ YES — CORDIS has 1,846; FK has none |
| **Task has clear, discrete labels**            | TRL 1-3 / 4-6 / 7-9 are well-defined categories | ✅ YES — clear official definitions    |
| **Text is short-to-medium length**             | Avg 15-20 keywords per project                  | ✅ YES — perfect for few-shot          |
| **Text is specialized/technical**              | Project titles + budget themes use domain vocab | ✅ YES — requires domain examples      |
| **Cost/speed matters**                         | 39,555 projects; manual annotation = €80-150k   | ✅ YES — API cost ~€15-20              |
| **Single-pass classification** (not iterative) | TRL is inferred once per project                | ✅ YES                                 |

**Your Project:** ✅ **Meets all criteria. Few-shot is appropriate.**

### ❌ **Do NOT Use Few-Shot When:**

- You have 5,000+ labeled examples → fine-tune instead (cheaper, more control)
- The task is highly interpretive (no agreed definition) → requires human review, not automation
- Annotation consistency is mandatory → fine-tuned models are deterministic; LLMs have stochasticity
- Deterministic reproducibility across runs is required → use `temperature=0` or fine-tune instead

---

## Part 2: Why Few-Shot is Ideal for TRL Classification

### **Direct Precedent: Pelaez et al. (2024) — Patent Public Value Classification**

Pelaez classifies **5M+ US patents** by "public value orientation" using GPT-4 few-shot:
- **Setup:** Technical text (patent abstracts, similar to FK "Thema")
- **Challenge:** Latent construct requiring domain expertise (public value = TRL)
- **Solution:** Few-shot with 100 expert-coded seed patents
- **Result:** High Cohen's Kappa agreement with expert test set; scales to millions of documents

**Why this is your exact use case:**
- Patent abstracts ≈ FK project titles/themes (both short, technical, specialized)
- "Public value orientation" ≈ "TRL level" (both latent constructs, not explicitly marked in source text)
- "Expert seed examples" = CORDIS training data (1,846 EU projects with official TRL labels)

**Pelaez's key finding:** "Few-shot approach (not zero-shot) essential for domain-specific text — zero-shot misses technical vocabulary"

→ Your implementation (using CORDIS examples) is exactly right.

---

## Part 3: Your Current Implementation vs. Best Practices

### **What You're Doing Right ✅**

| Best Practice                     | Source                 | Your Implementation                  |
| --------------------------------- | ---------------------- | ------------------------------------ |
| Use instruction-tuned LLM         | Chae & Davidson (2025) | ✅ Claude Haiku (instruction-tuned)   |
| Include ≥1 example per label      | Chae & Davidson (2025) | ✅ 3 examples per TRL group (9 total) |
| Domain-specific examples          | Pelaez et al. (2024)   | ✅ CORDIS EU projects (same domain)   |
| Temperature=0 for reproducibility | Ornstein et al. (2025) | ✅ Deterministic                      |
| JSON output with confidence       | Egami et al. (2024)    | ✅ Confidence scores included         |
| Prompt caching (cost efficiency)  | —                      | ✅ Smart optimization                 |
| Few-shot count 5-10 optimal       | Chae & Davidson (2025) | ✅ 9 examples is ideal                |

### **What's Missing or Should Improve ⚠️**

#### **CRITICAL (Required before deployment):**

1. **Human Validation with Cohen's Kappa** ❌ NOT DONE
   - **What:** Sample 300-600 projects; have 2 independent human annotators label them; compare to your LLM labels
   - **Threshold:** κ ≥ 0.60 (acceptable); κ ≥ 0.80 (excellent)
   - **Why:** Egami et al., Ornstein et al., Gilardi et al. all require this before using LLM annotations in analysis
   - **Effort:** 2-3 days (recruiting + annotation + analysis)

2. **Explicit Chain-of-Thought in Prompts** ⚠️ IMPLICIT, SHOULD FORMALIZE
   - **Current:** You ask for "reasoning" field
   - **Recommended:** Add explicit step-by-step instruction: "First identify the development phase. Then check TRL criteria. Finally assign."
   - **Why:** Ornstein et al. (2025) shows CoT improves accuracy 5-10pp on ambiguous items
   - **Effort:** 30 minutes to edit prompts

3. **Calibration Analysis** ❌ NOT DONE
   - **What:** Plot LLM's confidence score vs. actual accuracy on validation sample
   - **Why:** Ornstein et al. (2025): "LLMs may produce correct individual classifications but incorrect aggregate distributions"
   - **Importance:** If you want to publish TRL distributions by ministry/year, you MUST check: does "90% confidence" actually mean 90% right?
   - **Effort:** 1 day after validation

#### **IMPORTANT (Robustness check):**

4. **Multi-Prompt Testing** ⚠️ NOT DONE
   - **What:** Test 2-3 different prompt phrasings; see if results are stable
   - **Why:** Pangakis et al. (2023): prompt sensitivity is real; if results vary wildly, you're overfitting to wording
   - **Quick version:** Test German vs. English prompts; formal vs. conversational
   - **Effort:** 1 day

5. **XLM-RoBERTa Cross-Check** ⚠️ NOT DONE
   - **What:** Train a traditional ML model on CORDIS; apply to FK; compare classifications
   - **Why:** If both LLM and RoBERTa agree, you're confident; if they disagree, you found edge cases
   - **Effort:** 2-3 days (but lower priority — do after validation)

---

## Part 4: Detailed Best Practices from Literature

### **A. Prompt Architecture** (Ornstein et al. 2025, Halterman et al. 2025)

Your current approach uses:
- System role ✅
- Task description ✅
- Few-shot examples ✅
- Classification instruction ✅

**Enhancement: Add explicit chain-of-thought:**

```
[SYSTEM ROLE]
Du bist ein Experte für Technologiereifegrade (TRL).

[LABEL DEFINITIONS]
TRL 1-3 (Grundlagenforschung): ...
TRL 4-6 (Industrielle Forschung): ...
TRL 7-9 (Experimentelle Entwicklung): ...

[FEW-SHOT EXAMPLES]
Text: [Example]
Reasoning: [Why this TRL?]
Label: TRL_4_6

[CLASSIFICATION INSTRUCTION]
Klassifiziere folgendes Projekt SCHRITT FÜR SCHRITT:
1. Identifiziere die Entwicklungsphase (Grundlagenforschung? Prototyp? Marktreife?)
2. Ordne Kriterien aus der Definition zu
3. Vergib das TRL-Label

Text: {thema}
```

### **B. Few-Shot Exemplar Selection** (Pelaez 2024, Chae 2025)

**Your approach:**
- Source: CORDIS (domain-specific) ✅
- Count: 3 per TRL group ✅
- Selection: "Clear, unambiguous" — verify this ✅

**Enhancement: Check rare categories**
- Chae & Davidson (2025): "Few-shot corrects systematic underclassification of rare categories"
- **Question:** Is TRL 1-3 rare in FK? (Early research often minority)
- **If yes:** Explicitly oversample TRL 1-3 in your few-shot (e.g., 5 examples instead of 3)

### **C. Validation Protocol** (Egami et al., Ornstein et al., Grimmer & Stewart 2013)

**Mandatory steps before using results:**

1. **Stratified sampling:** 300-600 projects
   - Stratify by: Leistungsplansystematik (budget code), ministry (Ressort), project size
   - Randomize within strata
   
2. **Independent annotators:** 2 domain experts with TRL training
   - Blind: they don't see your LLM labels
   - Use official definitions: BMWK TRL Merkblatt + EU Horizon definitions
   
3. **Agreement metrics:**
   - **Cohen's Kappa:** Main metric (κ ≥ 0.60 acceptable; ≥ 0.80 excellent)
   - **F1 macro:** Secondary, reports per-category performance
   - **Confusion matrix:** Which TRL groups does LLM confuse?

4. **Error analysis:**
   - Which projects does LLM misclassify? (Find patterns)
   - Are errors random or systematic? (e.g., always overestimate TRL 7-9?)
   - Identify problematic text patterns (e.g., "prototype" text that could be TRL 3 or 5)

5. **Calibration curve:**
   - Plot LLM confidence (x-axis) vs. accuracy (y-axis)
   - Ideal: 90% confidence = 90% accuracy
   - Reality often: LLM overconfident or underconfident
   - Use for post-hoc calibration if needed

### **D. Aggregate-Level Bias** (Ornstein et al. 2025, Egami et al. 2024)

**Critical concern for your use case:**

Individual classifications can be high-accuracy, but aggregate distributions can be wrong.

**Example:**
- Individual accuracy: 85% (good)
- But: LLM systematically over-classifies TRL 7-9 (says "deployed" when really "prototype")
- Result: Your reported TRL distribution is wrong, even if individual labels are mostly correct

**Mitigation:**
1. Compare LLM aggregate distribution to human aggregate on validation sample
2. If they differ, calculate calibration weights (e.g., "multiply TRL 7-9 by 0.8")
3. Report both: raw LLM counts + calibrated counts

---

## Part 5: Specific Recommendations for Your Project

### **Priority 1 (CRITICAL — Do Before Full Run):**

1. **Run validation on 400-project sample** (2-3 days)
   - Get Cohen's Kappa
   - If κ ≥ 0.60: proceed to full run
   - If κ < 0.60: revise prompts, re-validate

2. **Add explicit chain-of-thought to prompts** (30 min)

3. **Compute calibration curve** (1 day, after validation)

### **Priority 2 (IMPORTANT — Can Be Done in Parallel):**

4. **Multi-prompt sensitivity test** (1 day)
   - German vs. English prompts
   - Formal vs. casual language
   - Check variance

5. **Check for class imbalance bias**
   - How many FK projects are TRL 1-3? (If <5%, you're biased)
   - Adjust few-shot oversampling if needed

### **Priority 3 (ROBUSTNESS — After Full Run):**

6. **XLM-RoBERTa comparison** (2-3 days)
   - Train on CORDIS; apply to FK
   - Compare agreement with LLM classifications

---

## Part 6: Applicability Verdict

### **Is LLM Few-Shot Right for TRL Classification of FK?**

**✅ YES — STRONGLY RECOMMENDED**

**Reasoning:**
1. **Task matches perfect use case:** Short technical text, specialized vocabulary, clear discrete labels
2. **Precedent exists:** Pelaez et al. (2024) did almost exactly this with patents; succeeded
3. **Constraints align:** No labeled FK data (few-shot needed); 39,555 projects (cost/speed critical)
4. **Research consensus:** Gilardi (2023), Egami (2024), Ornstein (2025), Chae (2025) all support LLM for this type of classification
5. **Your implementation is sound:** Instruction-tuned LLM + domain examples + temperature=0

**Caveats:**
1. Validation is MANDATORY — don't skip Cohen's Kappa check
2. Aggregate calibration matters — individual accuracy ≠ correct distribution estimates
3. Short text limitation (Krieger 2020, noted in trl-klassifikation-pipeline.md) — project descriptions are only 15-20 keywords
4. Budget line item issue (recent discovery): Leistungsplansystematik is theme/topic, not programme → TRL may vary within same code by ministry

---

## Part 7: Next Steps

| Step | Effort | Blocker? | Timeline |
|------|--------|----------|----------|
| Validation (Cohen's Kappa on 400 projects) | 2-3 days | YES | Week 1 |
| Chain-of-thought prompt enhancement | 30 min | NO | Week 1 |
| Calibration analysis | 1 day | NO | Week 1 |
| Full run (627 codes) | ~$5 + 1 hour | NO | Week 1 |
| Multi-prompt test | 1 day | NO | Week 2 |
| XLM-RoBERTa comparison | 2-3 days | NO | Week 2-3 |

---

## What it does

This method note evaluates whether few-shot LLM classification is appropriate
for assigning TRL labels to German Foerderkatalog project text.

## When to use it

Use it when deciding whether to run the LLM-based TRL classifier, how many
examples to include, and which validation checks are mandatory before using
classifications in analysis.

## Assumptions

- The label set is discrete and source-backed by [[30_concepts/technology-readiness-levels.md]].
- Few-shot examples are drawn from relevant project texts, especially [[50_datasets/cordis-horizon-europe-h2020.md]].
- Human validation remains required.

## Papers using or discussing this method

Key sources include [[20_summaries/gilardi2023-chatgpt-annotation.md]],
[[20_summaries/egami2024-llm-annotation-framework.md]],
[[20_summaries/ornstein2025-stochastic-parrot.md]],
[[20_summaries/pelaez2024-patent-public-value-llm.md]], and
[[20_summaries/moller2024-parrot-dilemma.md]].

## Strengths and limitations

The strength is low-cost scalable labeling for short technical texts. The
limitations are prompt sensitivity, calibration risk, possible LLM bias, and the
need for independent human gold-standard validation.

## Related concepts and datasets

- [[40_methods/llm-few-shot-social-science.md]]
- [[40_methods/trl-klassifikation-pipeline.md]]
- [[50_datasets/foerderkatalog-des-bundes.md]]
- [[50_datasets/cordis-horizon-europe-h2020.md]]

## References

- Egami, N., Hinck, E., Stewart, B., & Wei, H. (2024). Using LLMs as research assistants in social science. arXiv preprint.
- Ornstein, J., Blasingame, E., & Truscott, J. (2025). How to train your stochastic parrot. Working paper.
- Pelaez, S., Funk, J., & Owen-Smith, J. (2024). Classifying patent public value with LLMs. Working paper.
- Chae, Y., & Davidson, T. (2025). Instruction tuning and in-context learning for text classification. arXiv preprint.
- Gilardi, F., Alizadeh, M., & Kubli, M. (2023). ChatGPT outperforms crowd workers for text annotation. PNAS.
- Grimmer, J., & Stewart, B. (2013). Text as data. Annual Review of Political Science, 16.
