---
title: "Schlüsseltechnologien und HTAD-Taxonomie"
note_type: concept
summary: "Taxonomy of 6 key technology fields (Schlüsseltechnologien) identified in Germany's High Technology Action Programme (HTAD) and BCG Wachstumspfade report. Each field has subtechnology categories used for classifying Förderkatalog projects in the TRL analysis. Based on BCG (2026) and HTAD policy documents."
related_notes:
  - "20_summaries/wachstumspfade-deutschland.md"
projects: [bundesinnovationshaushalt-trl]
tags:
  - concept
  - schluesseltechnologien
  - htad
  - classification
  - technology-fields
updated: "2026-04-22"
---

# Schlüsseltechnologien und HTAD-Taxonomie

## Kontext

Die HTAD-Taxonomie basiert auf dem Bundesregierungsprogramm "Hightech-Agenda" (HTAP) und wurde durch die BCG-Studie "Wachstumspfade für Deutschland" (Februar 2026) operationalisiert. Für die TRL-Klassifikation des Förderkatalogs werden die 6 Schlüsseltechnologiefelder als zweite Klassifikationsdimension neben den TRL-Gruppen genutzt.

## Die 6 Schlüsseltechnologien

### 1. Künstliche Intelligenz (KI)

**4-Level-Hierarchie:**
- **KI-Anwendungen:** Horizontale (sektorübergreifend: Predictive Analytics, NLP-Assistenten) und vertikale (sektorspezifisch: autonomes Fahren, Medizin-KI, industrielle Bildverarbeitung)
- **KI-Modelle:** Large Language Models (LLM), Large Multimodal Models (LMM), Weltmodelle (World Models für autonome Systeme)
- **KI-Plattformen:** Cloud-AI-Infrastruktur, MLOps, Foundation-Model-Hosting, AI-APIs
- **Recheninfrastruktur:** GPU-Cluster, spezialisierte AI-Chips (NPUs, TPUs), Edge-AI-Hardware

**5 HTAD-Fokustechnologien:** KI-Chips, KI-gestützte Simulation, Quantencomputing-KI-Hybride, Erklärbarer KI, KI-Sicherheit (Robustheit/Alignment)

### 2. Quantentechnologien

**Subkategorien:**
- **Quantencomputing:** Supraleitende Qubits (IBM/Google Paradigma), Ionenfallen, Photonik, Topologisch, Hybrid-classical-quantum
- **Quantensensorik:** Gravimetrische Sensoren, magnetische Feldmessung, Atomuhren, Quantenbildgebung, Navigations-Gyros
- **Quantenkommunikation / QKD:** Quantenschlüsselverteilung, Quantennetzwerke, Quanten-Internet
- **Quantensimulation:** Digitale Simulation (Chemie, Materialien), analoge Quantensimulatoren

**Deutsche Stärken:** Quantensensorik (Physikalisch-Technische Bundesanstalt, Fraunhofer); **Schwächen:** Quantencomputing (Abstand zu IBM/Google groß)

### 3. Mikroelektronik und Halbleiter

**Subkategorien:**
- **Chip-Design:** EDA-Tools, SoC-Design, RISC-V-basierte Prozessoren, Automotive-Chips
- **Advanced Packaging:** Chiplet-Integration, 3D-Stacking, Fan-Out-Wafer-Level
- **Halbleiter-Equipment und -Materialien:** Lithografie, Ätzanlagen, Epitaxie (ZEISS, AIXTRON, Merck KGaA als deutsche Anker)
- **Speziall-Applikationen:** SiC/GaN-Leistungshalbleiter (EV-Antriebe), Automotive-ICs, Space-Grade-Chips

**Deutsche Stärken:** Equipment & Materials (Weltmarktführer in mehreren Segmenten); **Schwächen:** Leading-Edge-Logik (kein <7nm in DE)

### 4. Biotechnologie und Life Sciences

**Subkategorien:**
- **Synthetische Biologie / Genomics:** Gen-Editing (CRISPR), Metabolic Engineering, DNA-Datenspeicherung
- **Biomanufacturing:** Fermentations-Plattformen, Biokatalysatoren, Bioplastik, Biopharmazeutika-Produktion
- **Computational Biology / Bioinformatik:** Protein-Struktur-Vorhersage (AlphaFold), Drug Discovery (KI-gestützt), Genomik-Datenanalyse
- **Zell- und Gentherapie:** CAR-T-Therapien, mRNA-Plattformen (post-COVID), Gentherapie-Vektoren

**Deutsche Stärken:** Biomanufacturing-Infrastruktur, Biopharmazeutische Produktion; **Schwächen:** Biotech-Startups (Silicon-Valley-Lücke)

### 5. Fusionsenergie und Neue Energiesysteme

**Subkategorien:**
- **Fusionsreaktoren:** Tokamak (ITER-Beitrag), Stellaratoren (Wendelstein 7-X als dt. Weltklasse), Inertial Confinement
- **Fortgeschrittene Fission:** Kleine Modulare Reaktoren (SMR), Generation-IV-Konzepte, Thorium-Reaktoren
- **Netzinfrastruktur / Speicher:** Grid-Scale-Batterien (Vanadium-Redox, CAES), Power-to-X, Smart Grids
- **Wasserstoff-Infrastruktur:** Elektrolyseure (PEM, AEL, SOEC), H2-Transport/-Speicherung, Brennstoffzellen-Systeme

**Deutsche Stärken:** Wendelstein-7X als Weltführer in Stellarator-Fusion; Elektrolyseur-Hersteller (Siemens Energy, thyssenkrupp)

### 6. Klimaneutrale Mobilität

**Subkategorien:**
- **Elektro-/Brennstoffzellen-Antriebe:** BEV-Antriebsstränge, Batteriemanagement, Brennstoffzellen-Trucks
- **Autonomes und vernetztes Fahren:** Sensorik (LiDAR, Radar), Entscheidungsalgorithmen, V2X-Kommunikation
- **Nachhaltige Luftfahrt:** Sustainable Aviation Fuels (SAF), elektrische Kurzstreckenflugzeuge, H2-Propulsion
- **Ladeinfrastruktur:** Ultra-Fast-Charging, bidirektionales Laden (V2G), Lademanagement-Software

**Deutsche Stärken:** Traditionell Automotive-Kern (BMW, VW, Mercedes); Schwächen im Software-Stack (gegenüber Tesla, chinesischen OEMs)

## Randfelder (für FK-Klassifikation: nicht Schlüsseltechnologie)

- Produktionstechnologien (Robotik, Additive Manufacturing)
- Materialtechnologien (Advanced Materials, Composites)
- New Space (Satelliten, Raketen)
- Verteidigung/Dual-Use (sofern zivil anwendbar → andere Schlüsseltechnologie)
- Klassische Technologiefelder: Automotive (konventionell), Chemie (konventionell), Maschinenbau

## Operational Decision Rules für FK-Klassifikation

```
IF Projekt-Thema ∈ {KI, ML, Maschinelles Lernen, Neuronale Netze, NLP}: → KI
IF Projekt-Thema ∈ {Quanten, Quantencomputing, Quantensensorik}: → Quantentechnologien
IF Projekt-Thema ∈ {Chip, Halbleiter, Mikroelektronik, IC, FPGA, GPU, ASIC}: → Mikroelektronik
IF Projekt-Thema ∈ {Biotech, CRISPR, Genomics, mRNA, Fermentation, Biopharma}: → Biotechnologie
IF Projekt-Thema ∈ {Fusion, Kernfusion, Elektrolyse, H2, Wasserstoff, Speicher}: → Fusionsenergie/Neue Energien
IF Projekt-Thema ∈ {Elektromobilität, BEV, autonomes Fahren, SAF, V2G}: → Klimaneutrale Mobilität
ELSE: → Kein Schlüsseltechnologiefeld (klassisches Technologiefeld)
```

## Links
- [[20_summaries/wachstumspfade-deutschland.md]]
- [[40_methods/trl-klassifikation-pipeline.md]]
- [[70_projects/bundesinnovationshaushalt-trl.md]]

## Definition

The HTAD key-technology taxonomy is a project-facing classification layer for
identifying strategically important technology fields in German federal funding
data. It groups project descriptions into a manageable set of technology fields
such as AI, quantum technologies, microelectronics, biotechnology, new energy,
and climate-neutral mobility.

## Scope boundaries

This is an operational taxonomy for portfolio analysis. It is not a claim that
all important innovation occurs only in these fields, and it should not erase
traditional sectors such as machinery, chemicals, or automotive. It should be
used together with [[30_concepts/technology-readiness-levels.md]] and
[[30_concepts/radical-vs-incremental-innovation.md]].

## Papers that discuss this concept

The main source is [[20_summaries/wachstumspfade-deutschland.md]], with
supporting policy context from [[20_summaries/efi2023-gutachten.md]],
[[20_summaries/efi2024-gutachten.md]], [[20_summaries/draghi2024-european-competitiveness.md]],
and [[20_summaries/diw2025-strategic-industrial-policy.md]].

## How the papers use the concept

The taxonomy turns broad strategic-technology discussions into classification
rules for the Foerderkatalog project. EFI and Draghi provide the strategic
sovereignty and key-technology rationale; the TRL pipeline uses the taxonomy as
a label layer for project-level classification.

## Open questions

- Which key technologies should be grouped together for robust classification?
- How should cross-cutting projects be labeled when they combine AI, energy,
  mobility, or biotechnology?
- Does the funding portfolio support strategic capabilities or mostly legacy
  sectoral applications?
