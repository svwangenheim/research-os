---
title: "Bundesinnovationshaushalt und Technologiereifegrade"
note_type: project
summary: "Research project investigating whether German federal R&D funding (Förderkatalog, 39,555 projects) supports a testable hypothesis: strong upstream research and institutions, weak downstream translation and possible incumbent bias in TRL and recipient structure. Four-pillar design: literature, TRL classification, recipient analysis, country comparison. Output: Working Paper."
status: active
institution: "[Your Institution]"
started: "2026-04-01"
updated: "2026-04-29"
tags:
  - project
  - bundesinnovationshaushalt
  - trl-classification
  - germany
  - innovation-policy
---

# Bundesinnovationshaushalt und Technologiereifegrade

## Forschungsfrage

**Führt der deutsche Bund bevorzugt etablierte Unternehmen, die Fördergelder für inkrementelle Innovation nutzen, anstatt junge, kleine Unternehmen zu unterstützen, die radikale und disruptive Innovationen vorantreiben – und ist das ein zentraler Grund für Deutschlands Rückstand gegenüber Innovationsführern trotz hoher FuE-Ausgaben?**

## Arbeitsthese

Das Working Paper ist um die These "Viel Wissen, wenig Wachstum" organisiert:

- Deutschland hat starke Forschungskapazitäten und starke Institutionen für Wissensproduktion.
- Der Schwachpunkt ist die Übersetzung dieses Wissens in neue Firmen, neue Märkte und Produktivitätswachstum.
- Im Förderkatalog sollte sich diese Schwäche, wenn überhaupt, als Konzentration der Förderung bei großen, alten, wiederkehrenden Empfängern und als Tendenz zu späteren TRLs zeigen.
- TRL ist hier nur ein Hypothesentest, kein vorweggenommener Befund. Das Paper sollte keinen TRL-Bias behaupten, solange die Klassifikation das nicht trägt.
- Die politische Frage ist, ob Bundesförderung neue Pfade öffnet oder vor allem etablierte Pfade stabilisiert.

## Status (Stand: 2026-04-22)

| Komponente                  | Status          | Nächster Schritt                                      |
| --------------------------- | --------------- | ----------------------------------------------------- |
| Säule A: Literatur          | DONE            | 38+ Papers heruntergeladen, Wiki-Ingest abgeschlossen |
| Säule B: TRL-Klassifikation | Scripts ready   | Script 07 ausführen (ANTHROPIC_API_KEY)               |
| Säule C: Empfängeranalyse   | Pending         | Scripts 14-15 (Cap IQ Matching)                       |
| Säule D: Ländervergleich    | Data downloaded | Script 13 Plots fertig; GII noch ausstehend           |
| Paper: Working Paper        | In progress     | Theorie + Methodik bereits vorhanden                  |

## Vier Säulen

### Säule A - Theorie & Literatur
**Theoretische Basis:**
- [[20_summaries/acemoglu2006-distance-to-frontier.md]] - Frontier-Theorie: Subsidien an Incumbents trapping frontier economies
- [[20_summaries/akcigit2018-heterogeneous-innovations.md]] - Internal vs. external innovation; firm-size distribution shapes innovation type and growth contribution
- [[20_summaries/aghion1992-creative-destruction.md]] - Schumpeterian growth; business-stealing externality
- [[20_summaries/dosi1982-technological-paradigms.md]] - Paradigmen/Trajektorien; Pfadabhängigkeit

**Empirische Evidenz:**
- [[20_summaries/beck2016-radical-or-incremental.md]] - Policy-R&D signifikant nur für radikale Innovation (ZEW)
- [[20_summaries/aschhoff2010-who-gets-the-money.md]] - State dependence: prior recipients systematically favored
- [[20_summaries/czarnitzki2004-rd-subsidies-zew.md]] - Additionality: no crowding-out; but no TRL disaggregation
- [[20_summaries/howell2017-financing-innovation.md]] - RDD: early-stage grants (TRL 1-3) unlock VC; causal

**Kontext Deutschland:**
- [[20_summaries/rammer2024-innovationsindikator.md]] - Innovationsindikator: input-output gap
- [[20_summaries/stehnken2024-zim-evaluation.md]] - ZIM 2024: 65% additionality; typical SME recipient
- [[20_summaries/prognos2019-zim-evaluation.md]] - ZIM 2015 evaluation: additional R&D intensity and cooperation effects, but mainly deeper R&D among already R&D-active SMEs
- [[20_summaries/draghi2024-european-competitiveness.md]] - EU-weite Diagnose: radical innovation deficit
- [[20_summaries/bmbf2024-bundesbericht-datenband.md]] - Bundesbericht: institutionelle vs. direkte Förderung

### Säule B - TRL-Klassifikation
**Methodik:**
- [[40_methods/trl-klassifikation-pipeline.md]] - Vollständige Pipeline: Script 07 (LLM) + 07b (XLM-RoBERTa) + 08 (Kappa) + 09 (Aggregation)
- [[40_methods/llm-few-shot-social-science.md]] - Best practices: Prompt-Architektur, Validierung, Kalibrierung
- [[40_methods/xlm-roberta-multilingual-classification.md]] - XLM-RoBERTa: cross-lingual transfer EN-DE

**Daten:**
- [[50_datasets/foerderkatalog-des-bundes.md]] - FK: 39.555 aktive Projekte, 30 Spalten
- [[50_datasets/cordis-horizon-europe-h2020.md]] - CORDIS: 1.846 labeled EU-Projekte als Training/Few-Shot

**Scripts:** `scripts/python/07_llm_trl_classifier.py`, `08_validation_kappa.py`, `09_aggregate_results.py`

### Säule C - Empfängercharakteristika
**Datenbedarf:** Cap IQ (Compustat), OpenCorporates, Handelsregister
**Scripts:** `scripts/python/14_firm_matching.py`, `15_recipient_analysis.py` (noch nicht gestartet)

### Säule D - Internationaler Ländervergleich
**Daten heruntergeladen:** OECD MSTI, EIS 2025, Eurostat R&D
**Scripts fertig:** `scripts/python/10_download_oecd_msti.py` - DONE, `11_download_eis.py` - DONE, `12_download_eurostat_rd.py` - DONE, `13_country_comparison.py` - DONE
**Visualisierungen:** `paper/figures/` (5 Abbildungen fertig)

## Key Concepts

- [[30_concepts/creative-destruction-and-distance-to-frontier.md]] - Frontier and Schumpeter mechanism: why near-frontier policy needs entrant selection.
- [[30_concepts/rd-subsidy-additionality.md]] - Additionality: whether public support creates additional R&D, innovation, VC, patents, or commercialization.
- [[30_concepts/knowledge-spillovers-and-entrepreneurship.md]] - Spillover and entrepreneurship mechanism between research, start-ups, and growth.
- [[30_concepts/green-innovation-and-transition-policy.md]] - Climate, energy, and transition innovation as a funding and technology cluster.
- [[30_concepts/llm-annotation-and-automated-coding.md]] - LLM annotation as a measurement strategy for project classification.
- [[30_concepts/text-as-data-computational-social-science.md]] - Text-as-data as the research-design layer for Foerderkatalog classification.
- [[30_concepts/foundation-models-and-pretrained-transformers.md]] - BERT, XLM-R, and GPT model families behind the classification and robustness paths.
- [[30_concepts/innovation-paradox.md]] - Deutschlands Innovationsparadox: Mechanismen und Evidenz
- [[30_concepts/radical-vs-incremental-innovation.md]] - Radikal vs. inkrementell: Definitionen, TRL-Mapping, Marktversagen
- [[30_concepts/technology-readiness-levels.md]] - TRL-Skala: EU/DE Framework, Klassifikationsprobleme
- [[30_concepts/schluesseltechnologien-htad.md]] - HTAD-Taxonomie: 6 Schlüsseltechnologien mit Subtechnologien
- [[30_concepts/innovation-systems-comparison.md]] - NIS-Vergleich: DE vs. Innovationsführer

## Relevant Synthesis

- [[90_synthesis/innovation-paradox-incumbent-lock-in.md]] - central working synthesis for the allocation, TRL, and incumbent-lock-in hypothesis behind the project.

## Governance and Evaluation Layer

- [[90_synthesis/llm-text-classification-and-annotation.md]] - Synthesis bridge for LLM annotation, text-as-data validation, BERT/GPT model choice, and TRL classification.
- [[20_summaries/efi2023-gutachten.md]] - EFI 2023: mission-oriented governance, DATI/SPRIND, transfer, and data-economy policy.
- [[20_summaries/efi2024-gutachten.md]] - EFI 2024: Forschungszulage, IP transfer, data access, causal evaluation, and AI policy.
- [[30_concepts/mission-oriented-innovation-policy.md]] - Mission governance, mission teams, roadmaps, budgets, and policy mixes.
- [[30_concepts/data-access-for-innovation-policy.md]] - Data access as innovation and evaluation infrastructure.
- [[40_methods/causal-evaluation-innovation-policy.md]] - Boundary between descriptive portfolio mapping and causal impact evaluation.
- [[50_datasets/mannheimer-innovationspanel.md]] - Firm-level German innovation survey evidence.
- [[90_synthesis/innovation-policy-governance-and-evaluation.md]] - Synthesis bridge for mission governance, data access, transfer, and evaluation.
- [[90_synthesis/inbox-processing-plan-2026-04-30.md]] - Processed inbox audit and remaining source-acquisition queue.

## Output

**Datei:** `paper/brief.md` - DZ Working Paper (Deutsch)
**Format:** Wissenschaftliches Arbeitspapier im DZ-Stil (policy-orientiert, akademisch rigoros)
**Zielgruppe:** Politikentscheider, Innovationspolitik-Stakeholder, deutsche Wirtschaftsforschung

## Offene Punkte

### Daten (Recherche erforderlich)
1. GII 2025: Top-10-Tabelle + DE-Score (Rang 11) → für Tabelle 1 in §1
2. OECD MSTI 2026 (März/April): BERD-Sektorstruktur (Manufacturing vs. ICT/Services/Computer) für DE + Vergleichsländer
3. WIPO-Patentdaten: DE Patentoutput nach Technologiefeld (Hightech vs. Midtech) — Beleg für MTF-Hypothese
4. EIS 2025: Weitere Detailwerte (KMU-Indikator, HERD, Indirect Government Support) für DE + Leader
5. Produktivitätswachstum DE vs. Innovation Leaders: Zeitreihe (OECD/Eurostat)
6. Forschungszulage-Evaluation: Wer nutzt sie? (Größenklassen, Branchen) — BMBF-Bericht oder ZEW-Evaluation
7. KMU-Innovationsbeteiligung: Trendentwicklung (Innovationserhebung ZEW/MIP)

### Literatur (fehlend)
8. Dietrich, Dorn & Fuest (2024): Originalarbeit zur Mitteltechnologie-Falle (Bertelsmann/ifo) — Wiki-Ingest notwendig
9. Post-2024 Politikpapiere zu DEs Innovationsproblem: ifo, DIW, ZEW, Sachverständigenrat, OECD, BMWi, Think Tanks
10. Transfer-Problem/Valley of Death Literatur (TRL 4-6 Lücke): dedizierte Quellen für DE-Kontext
11. Internationaler Vergleich Förderinstrumente: Innosuisse (CH), Vinnova/RISE (SE), KIAT/KEIT (KOR), Catapult/Innovate UK (UK), SBIR (USA), Transferbrücken-Ansatz (DE)

### Skripte (wie bisher)
12. Script 07 ausführen (braucht ANTHROPIC_API_KEY)
13. Scripts 08+09: Kappa-Validierung + Aggregation
14. Scripts 14+15: Firm Matching + Empfängeranalyse

## Journal

### 2026-04-30 (Session 2)

**Done:**
- Nutzerfeedback zu erstem Draft (`Notizen_Claude_Draft.md`) analysiert
- Lückenanalyse des LLM-Wiki abgeschlossen: 11 Datenlücken + Literaturlücken identifiziert
- Vault-Offene-Punkte aktualisiert mit vollständiger Recherche-Agenda
- Neues Konzept-Page `Mitteltechnologie-Falle` angelegt
- `innovation-systems-comparison.md` aktualisiert (GII 2025, KMU-Trend, HERD)
- Forschungsplan (Planner-Agent) erstellt: Research + Rewrite-Agenda für Draft v2

**Erkenntnisse aus Nutzerfeedback:**
- §1: Zu kurz, zu wenig Daten. GII 2025 (DE Rang 11), EIS 2025 (DE Rang 13), BERD-Sektorstruktur, WIPO-Patente, Produktivität, KMU-Trend — alles noch fehlend
- §2: MTF-Mechanismus zu knapp. Growth-Share-Matrix besser erklären; Frontier-Ökonomie-Argument stärker; Forschungszulage-Kontext einbauen
- §3: Transferproblem hinzufügen (TRL 4-6 Lücke, HERD-Vergleich, Kommerzialisierungsrate)
- §4+§5: Umstrukturieren — §3 endet mit Synthese der 3 Probleme; §4 = internationale Lösungen je Problem; §5 = nur Empfehlungen
- Allgemein: Text muss doppelt bis dreimal so lang werden; post-2024 Quellen vollständig fehlen

**Next:**
- Forschungsphase: `/discover data` (OECD MSTI, EIS, GII, WIPO, Produktivität, Forschungszulage) + Deep-Research (post-2024 Politikpapiere, Transferliteratur, internationale Instrumente)
- Wiki-Ingest: Neue Quellen ingesten (insb. Dietrich/Dorn/Fuest 2024)
- Draft v2: Vollständiger Rewrite basierend auf Forschungsergebnissen + Nutzerfeedback

