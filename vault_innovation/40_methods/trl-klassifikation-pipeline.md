---
title: "TRL-Klassifikationspipeline: Förderkatalog"
note_type: method
summary: "Complete methodology for automated TRL classification of 39,555 German federal R&D projects in the Förderkatalog using LLM few-shot (Claude Haiku) and XLM-RoBERTa fine-tuning. Documents data flow, prompt design, validation protocol, and output aggregation. Pipeline produces both TRL-group assignment and Schlüsseltechnologie identification."
related_notes:
  - "40_methods/llm-few-shot-social-science.md"
  - "40_methods/xlm-roberta-multilingual-classification.md"
  - "20_summaries/krieger2020-foerderkatalog-querschnitt.md"
  - "20_summaries/heder2017-trl-history.md"
  - "20_summaries/pelaez2024-patent-public-value-llm.md"
  - "50_datasets/foerderkatalog-des-bundes.md"
  - "50_datasets/cordis-horizon-europe-h2020.md"
projects: [bundesinnovationshaushalt-trl]
tags:
  - method
  - trl-classification
  - pipeline
  - förderkatalog
  - llm
  - xlm-roberta
updated: "2026-04-22"
---

# TRL-Klassifikationspipeline: Förderkatalog

## Überblick

Die Pipeline klassifiziert 39.555 aktive Projekte des deutschen Förderkatalogs (FK) entlang zweier Dimensionen:
1. **TRL-Gruppe** (1-3: Grundlagenforschung / 4-6: Industrielle Forschung / 7-9: Experimentelle Entwicklung)
2. **Schlüsseltechnologiefeld** (KI / Quantentechnologien / Mikroelektronik / Biotechnologie / Fusionsenergie / Klimaneutrale Mobilität / Kein Schlüsseltechnologiefeld)

## Warum automatisierte Klassifikation?

- Keine TRL-Felder im FK (im Gegensatz zu EU Horizon Europe) — Krieger et al. (2020)
- Kurze Texte (~15 Keywords pro Projekt) — regelbasierte Systeme unzuverlässig
- 39.555 Projekte — manuelle Annotation nicht skalierbar (€80-150k Kostenschätzung)
- LLMs outperform crowd workers für Text-Annotation — Gilardi et al. (2023), Törnberg (2025)
- Pelaez et al. (2024): analoges Setup für 5M+ US-Patente erfolgreich validiert

## Datenfluss

```
Förderkatalog.csv (39,555 Projekte, 30 Spalten)
         │
         ▼ [Preprocessing]
FK_classified_input.csv
  - Felder: Thema + Leistungsplansystematik (LPS) + Ressort + Jahr + Fördervolumen
  - Normalisierung: Sonderzeichen, Kodierung, Leerzeichen
         │
         ▼ [Script 07: LLM Klassifikation — Claude Haiku]
FK_classified.csv
  - trl_group (Basic/Applied/Development)
  - trl_score (1-9, numerisch)
  - key_tech (list: KI / Quanten / etc. / None)
  - confidence (0.0-1.0)
  - reasoning (CoT-Text)
         │
         ├──────────────────────────────────────────►
         │ [Script 07b: Robustness — XLM-RoBERTa]   │
         │ FK_classified_robustness.csv              │
         │                                           │
         ▼ [Script 08: Validation — Kappa]           ▼
Validation Report (600-project sample)    Concordance Analysis (LLM vs. RoBERTa)
  - Cohen's Kappa human vs. LLM           - Agreement metrics
  - Error analysis by TRL group           - Disagreement analysis
  - Calibration check                     - Final ensemble classification
         │
         ▼ [Script 09: Aggregation]
Analysis tables:
  - TRL distribution by Ressort / Ministerium
  - TRL distribution over time
  - TRL × Schlüsseltechnologie cross-tab
  - Fördervolumen by TRL group
  - Comparison with Horizon Europe TRL distribution (Trucco 2025)
```

## Primärmethode: LLM Few-Shot (Script 07)

### Modell
- **Modell:** Claude 3 Haiku (claude-haiku-20240307) — instruction-tuned, cost-efficient, multilingual
- **Temperatur:** 0.0 (deterministisch)
- **Format:** JSON-Output

### Prompt-Architektur

```python
SYSTEM_PROMPT = """
Sie sind ein Experte für die Klassifikation von öffentlich geförderten 
Forschungs- und Entwicklungsprojekten nach Technologiereifegrad (TRL).

Verwenden Sie folgende TRL-Gruppen:
- TRL 1-3 (Grundlagenforschung): Grundlegende Prinzipien, Technologiekonzept, 
  experimenteller Nachweis. Keine direkten Anwendungen, hohe Unsicherheit.
- TRL 4-6 (Industrielle Forschung): Nachweis im Labor/Umgebung, 
  Komponenten/Subsysteme validiert, Prototypen entwickelt.
- TRL 7-9 (Experimentelle Entwicklung): System demonstriert, 
  qualifiziert, vollständige Demonstration, Marktreife.
"""

FEW_SHOT_EXAMPLES = [
    # 3 Beispiele pro TRL-Gruppe aus CORDIS-Trainingsdaten
    # Ausgewählt: klar, einheitig, verschiedene Technologiefelder
    {"text": "...", "trl_group": "Basic", "trl_score": 2, "key_tech": ["KI"]},
    ...
]

USER_PROMPT = """
Klassifizieren Sie folgendes deutsches FuE-Projekt:

Thema: {thema}
Förderprogramm: {lps}

Antwort im JSON-Format:
{{"trl_group": "Basic|Applied|Development", 
  "trl_score": 1-9, 
  "key_tech": ["KI"|"Quanten"|"Mikroelektronik"|"Biotechnologie"|"Fusion"|"Mobilität"|null],
  "confidence": 0.0-1.0,
  "reasoning": "Kurze Begründung (1-2 Sätze)"}}
"""
```

### Few-Shot-Exemplare
- Quelle: CORDIS training data (1.846 EU-Projekte mit TRL-Labels 1-9)
- Auswahl: 3 Exemplare pro TRL-Gruppe (9 gesamt) — klar, unambig, verschiedene Technologiefelder
- Cross-linguale Übertragung: Englische Exemplare → Deutsches FK → via Haiku (multilingual kompetent)
- Sonderfall TRL 1-3: Explizit überrepräsentiert in Exemplaren (Korrektur für erwartete Klassenimbalance)

## Robustheitsprüfung: XLM-RoBERTa (Script 07b)

- **Modell:** `xlm-roberta-large` (HuggingFace)
- **Training:** Fine-tuning auf CORDIS training data (1.846 Projekte, stratifiziertes 80/20-Split)
- **Inference:** Zero-Shot auf FK-Texte (cross-lingual transfer EN→DE)
- **Output:** TRL-Klasse (1-3 / 4-6 / 7-9) + Softmax-Wahrscheinlichkeiten
- **Referenz:** Conneau et al. (2020) XLM-RoBERTa; Timoneda & Vallejo Vera (2025) fine-tuning best practices

## Validierungsprotokoll (Script 08)

### Design
- **Stichprobengröße:** 600 FK-Projekte
- **Stratifizierung:** Nach Ressort (BMBF/BMWK/andere), Projektgröße, Zufallsauswahl
- **Annotierende:** 2 unabhängige Annotator:innen (domain experts with TRL training)
- **Annotationsgrundlage:** BMWK TRL-Merkblatt + EU Horizon TRL definitions
- **Blind:** Annotator:innen sehen keine LLM-Outputs während der Annotation

### Metriken
- Cohen's Kappa (κ): Interrater-Reliabilität (Annotator:in 1 vs. 2)
- Cohen's Kappa: LLM vs. Annotator:in 1 / LLM vs. Annotator:in 2
- F1 (Makro) für 3-Klassen-Klassifikation
- Kalibrierungskurve: LLM-Konfidenz vs. tatsächliche Genauigkeit
- Konfusionsmatrix: welche TRL-Gruppen werden verwechselt?

### Akzeptanzschwellen
- κ ≥ 0.60: Substanzielle Übereinstimmung → 3-Klassen-Aggregation als primäre Messgröße
- κ ≥ 0.50: Moderate Übereinstimmung → Ausweitung auf 5-Klassen (1-3, 4-5, 6-7, 8-9) nicht möglich
- κ < 0.50: Methodologisches Problem → Prompt-Überarbeitung + Re-Validierung

## What it does

This method classifies German Foerderkatalog project records by technology
readiness group and key technology field. It combines source-backed TRL
definitions, short-text preprocessing, LLM few-shot classification, XLM-RoBERTa
robustness checks, human validation, and aggregation.

## When to use it

Use it for descriptive portfolio mapping of federal project funding by maturity
stage, technology field, ministry, recipient type, and funding volume. Do not
use it alone for causal claims about program effects.

## Assumptions

- Project text contains enough maturity signal for classification.
- The CORDIS examples are a reasonable calibration bridge.
- Human validation and calibration checks are completed before substantive use.
- [[50_datasets/foerderkatalog-des-bundes.md]] has been cleaned and documented.

## Papers using or discussing this method

Related sources include [[20_summaries/krieger2020-foerderkatalog-querschnitt.md]],
[[20_summaries/pelaez2024-patent-public-value-llm.md]],
[[20_summaries/bmle-merkblatt-technologiereifegrade.md]],
[[20_summaries/ec-trl-horizon2020.md]], and
[[20_summaries/trucco2025-scaling-up-ideas.md]].

## Strengths and limitations

The strength is scalable project-level maturity mapping. The limitation is that
TRL is inferred, not reported; short project text can be ambiguous; and the
pipeline measures portfolio composition rather than policy impact.

## Related concepts and datasets

- [[30_concepts/llm-annotation-and-automated-coding.md]]
- [[30_concepts/text-as-data-computational-social-science.md]]
- [[30_concepts/foundation-models-and-pretrained-transformers.md]]
- [[90_synthesis/llm-text-classification-and-annotation.md]]
- [[30_concepts/technology-readiness-levels.md]]
- [[30_concepts/schluesseltechnologien-htad.md]]
- [[40_methods/llm-few-shot-social-science.md]]
- [[40_methods/xlm-roberta-multilingual-classification.md]]
- [[50_datasets/foerderkatalog-des-bundes.md]]
- [[50_datasets/cordis-horizon-europe-h2020.md]]

## Aggregation (Script 09)

### Haupttabellen
1. TRL-Verteilung nach Ressort/Ministerium (Balkendiagramm)
2. TRL-Verteilung nach Fördervolumen (Weighted distribution)
3. TRL-Zeitreihe 2010-2024 (Hat sich die Verteilung verändert?)
4. TRL × Schlüsseltechnologie (Cross-Tab: Werden neue Felder früh gefördert?)
5. Vergleich mit Horizon Europe (Trucco 2025: 68% TRL 5-7 in EU)

### Robustheitstabellen
- LLM vs. XLM-RoBERTa Konkordanz (TRL-Gruppen)
- Sensitivitätsanalyse: 3-Klassen vs. 2-Klassen (low TRL 1-4 / high TRL 5-9)

## Bekannte Einschränkungen

1. **Short-text problem:** FK-Projekttexte sehr kurz (~15 Keywords) — Krieger et al. (2020) dokumentiert dies als Hauptproblem für BMBF-FK-Textanalyse
2. **No ground truth:** Keine offiziellen TRL-Labels im FK → Validation gegen human annotators, nicht gold standard
3. **Language mismatch:** CORDIS-Exemplare auf Englisch, FK auf Deutsch → cross-lingual transfer kann Fehler einführen
4. **TRL gaming:** Unternehmen könnten strategisch TRL-relevante Begriffe in Projektbeschreibungen verwenden (Héder 2017)
5. **Binary TRL ambiguity:** Projekte oft über mehrere TRL-Stufen hinweg → Klassifikation des "primären" TRL

## Links
- [[40_methods/llm-few-shot-social-science.md]]
- [[40_methods/xlm-roberta-multilingual-classification.md]]
- [[30_concepts/technology-readiness-levels.md]]
- [[30_concepts/schluesseltechnologien-htad.md]]
- [[50_datasets/foerderkatalog-des-bundes.md]]
- [[50_datasets/cordis-horizon-europe-h2020.md]]
- [[70_projects/bundesinnovationshaushalt-trl.md]]
