# Förderkatalog des Bundes

*Added: 2026-04-15 | Source: lit_review_cordis_foerderkatalog.md + notes/data-notes.md*

---

## Overview

The Förderkatalog des Bundes (Federal Funding Catalog) is the official public registry of all active German federal direct project funding in research, technology, and innovation. Administered by the Förderportal des Bundes (foerderportal.bund.de); technical operations handled by DLR on behalf of BMBF. The upstream system is PROFI (project database); aggregate statistics are compiled from PROFI via DASTAT (maintained by DZHW) and published in the Bundesbericht Forschung und Innovation (BuFI).

**Access:** foerderportal.bund.de (public, no registration)

---

## Coverage

| Property | Value |
|----------|-------|
| Active projects (our extract, April 2026) | 39,555 |
| Full database (all projects incl. completed) | >110,000 |
| Funding scope | German federal **direct project** funding only |
| Unit of observation | Individual funded project |
| Language | German |

**Not included:**
- Institutional core funding (Grundfinanzierung) of Helmholtz (~5.6 bn EUR/year), MPG, Fraunhofer, Leibniz centres — these flow through separate budget lines
- DFG-funded basic research
- Defense R&D (BMVg) — likely systematically underrepresented due to restricted disclosure
- Very recent approvals (60-day publication delay)

---

## File Characteristics

| Property | Value |
|----------|-------|
| Delimiter | Semicolon (`;`) — German CSV standard |
| Encoding | Likely Latin-1 (ISO-8859-1) or UTF-8 with BOM — verify empirically |
| Header row | Yes (row 1) |
| Data rows | 39,555 |
| Columns | 30 (cols 27–30 unlabelled in initial inspection) |
| File size | ~21 MB |

---

## Column Reference

| # | Column Name (German) | English Translation | Type | Classification Relevance |
|---|---------------------|---------------------|------|--------------------------|
| 1 | FKZ | Funding Reference Number | ID | Unique project identifier |
| 2 | Ressort | Ministry/Department | Categorical | Yes — ministry signals field context |
| 3 | Referat | Desk unit | Categorical | Supplementary |
| 4 | Administrierende Stelle | Administering body (e.g., DLR, VDI/VDE) | Categorical | Supplementary |
| 5 | Arb.-Einh. | Work unit | Categorical | Supplementary |
| 6 | Förderempfänger/Auftragnehmer | Funding recipient / contractor | Text | Supplementary (institution type may signal TRL) |
| 7 | Gemeindekennziffer (Empfänger) | Municipal ID (recipient) | Numeric | Geographic only |
| 8 | Stadt/Gemeinde (Empfänger) | City/municipality (recipient) | Text | Geographic only |
| 9 | Ort (Empfänger) | Location (recipient) | Text | Geographic only |
| 10 | Bundesland (Empfänger) | Federal state (recipient) | Categorical | Geographic only |
| 11 | Staat (Empfänger) | Country (recipient) | Categorical | Filter: keep Germany-based |
| 12 | Ausführende Stelle | Executing body | Text | Supplementary |
| 13 | Gemeindekennziffer (Ausführende) | Municipal ID (executor) | Numeric | Geographic only |
| 14 | Stadt/Gemeinde (Ausführende) | City/municipality (executor) | Text | Geographic only |
| 15 | Ort (Ausführende) | Location (executor) | Text | Geographic only |
| 16 | Bundesland (Ausführende) | Federal state (executor) | Categorical | Geographic only |
| 17 | Staat (Ausführende) | Country (executor) | Categorical | Geographic only |
| 18 | **Thema des geförderten Vorhabens** | **Project description / title** | **Text** | **PRIMARY — main classification input** |
| 19 | Leistungsplansystematik | Performance plan code | Categorical | Yes — structured funding category code |
| 20 | **Klartext Leistungsplansystematik** | **Performance plan plain text** | **Text** | **Yes — human-readable funding category** |
| 21 | Laufzeit von | Start date | Date (DD.MM.YYYY) | Filter: time period |
| 22 | Laufzeit bis | End date | Date (DD.MM.YYYY) | Filter: time period |
| 23 | Förder-/Auftragssumme (Anteil des Bundes) in EUR | Funding amount — federal share (EUR) | Numeric (German format) | Yes — weight TRL distribution by funding volume |
| 24 | Förderprofil | Funding profile / category | Categorical | Yes — e.g., "Technologie- und Innovationsförderung" |
| 25 | Projekt | Project flag | Categorical | TBD |
| 26 | Förderart | Funding type | Categorical | Yes — e.g., "Direkte Projektförderung" vs. "Auftragsforschung" |
| 27–30 | (unlabelled) | Not yet identified | — | To verify during exploration |

---

## Key Fields for TRL Classification

Ordered by information value for TRL inference:

1. **`Thema des geförderten Vorhabens`** — Project description (title + abstract in one field). Primary text input for classification. Variable length: some entries are long abstracts, others just one-sentence titles. Krieger et al. (2020) document that ~10% of BMBF project descriptions have fewer than 20 words.
2. **`Klartext Leistungsplansystematik`** — Human-readable funding category. Provides domain/sector signal. Cannot substitute for text-based TRL assignment (see biases below) but useful as a supplementary feature.
3. **`Leistungsplansystematik`** — Code version of LPS. Hierarchical taxonomy; revised in 2009. Partially maps to R&D phases.
4. **`Förderprofil`** — Broad funding profile. Useful to filter non-R&D projects before classification.
5. **`Ressort`** — Ministry. BMBF and BMWK are R&D-heavy; BMG, BMUV, BMI are sector-specific applied; BMVg defense R&D requires separate handling.

---

## Ministry Breakdown (Approximate)

| Ministry | Abbrev. | R&D Focus | Approximate TRL Range |
|----------|---------|-----------|----------------------|
| Bundesministerium für Bildung und Forschung | BMBF | Largest R&D funder; all levels | TRL 1–9 |
| Bundesministerium für Wirtschaft und Klimaschutz | BMWK | Tech/innovation focus | TRL 4–8 |
| Bundesministerium für Digitales und Verkehr | BMDV | Transport + digital | TRL 4–8 |
| Bundesministerium der Verteidigung | BMVg | Defense R&D | TRL 3–8 (underrepresented) |
| Bundesministerium für Gesundheit | BMG | Health/sector-specific applied | TRL 3–7 |
| Bundesministerium für Umwelt, Naturschutz | BMUV | Environmental applied | TRL 3–7 |

---

## TRL Field

**Does NOT exist.** German federal funding programmes do not require TRL reporting from grantees (as of 2026). TRL must be inferred from `Thema des geförderten Vorhabens` and `Klartext Leistungsplansystematik` using text-based NLP methods.

---

## Known Biases and Quality Issues

**Coverage limitations:**

1. **Selective publication:** Each federal ministry independently decides which projects to enter into the Förderkatalog. Coverage is not 100% of all approved federal grants — only projects deemed suitable for public disclosure are included.
2. **60-day delay:** New projects appear approximately 60 days after formal approval. Very recent projects are absent.
3. **Institutional funding gap:** Helmholtz (~5.6 bn EUR/year), MPG, Fraunhofer, Leibniz core funding, and DFG-funded basic research flow through separate budget lines and are entirely absent. The Förderkatalog captures "Direkte Projektförderung" — a subset of total German federal R&D spending. This means basic research (TRL 1–3) is structurally underrepresented relative to total federal R&D.
4. **Non-R&D projects included:** Infrastructure, cultural, social, and other non-R&D projects are included alongside R&D. Filter on `Förderprofil` and `Ressort` required before TRL classification.
5. **Defense underrepresentation:** BMVg projects are likely subject to restricted disclosure; defense R&D is systematically underrepresented.

**Classification limitations (Leistungsplansystematik):**

6. **Focus principle (Schwerpunktprinzip):** Each project receives only one LPS code, even if interdisciplinary. Cross-cutting topics (digitalization, sustainability, AI) are systematically assigned to the dominant theme and undercounted in secondary themes. Krieger et al. (2020) empirically demonstrate that LPS codes alone capture significantly fewer digitalization-relevant projects than text-based methods.
7. **LPS cannot substitute for TRL classification:** LPS codes are domain categories (e.g., "Lebenswissenschaften", "Energieforschung"), not technology maturity indicators. No mapping to TRL exists.
8. **LPS retroactive reclassification:** The LPS system was revised in 2009; comparisons with pre-2009 data require harmonization.

**Text field quality:**

9. **Variable description length:** Some `Thema` entries are only one-sentence titles; others are multi-paragraph abstracts. Krieger et al. (2020) document ~10% of BMBF descriptions have fewer than 20 words — below reliable classification threshold.
10. **German-language only:** All descriptions in German. Requires German-language NLP models (e.g., German BERT, XLM-RoBERTa) or translation for cross-lingual comparison with CORDIS.
11. **German number formatting:** Funding amounts use period as thousands separator and comma as decimal (`872.500,00`). Parse with `locale` or regex before float conversion.
12. **Date format:** DD.MM.YYYY — not ISO 8601. Parse with `pd.to_datetime(..., format='%d.%m.%Y')`.
13. **Possible duplicate FKZ:** Multiple rows per project number possible (sub-projects). Verify with `df['FKZ'].duplicated().sum()`.

---

## Data Provenance Chain

```
Project approval → PROFI database
                        ↓
              Förderkatalog (public, project-level)
              DASTAT (statistical aggregation, DZHW)
                        ↓
              BuFI Datenband (macro R&D statistics, biennial)
```

The Förderkatalog and the BuFI aggregate statistics derive from the same upstream PROFI source. Discrepancies between them reflect aggregation choices (LPS focus principle, OECD/Frascati R&D definition applied in BuFI but not in Förderkatalog).

---

## Access

Grade A — Public download, CSV format, no registration.

- Portal: `https://foerderportal.bund.de/foekat/jsp/StartAction.do`
- Direct CSV export available via portal search interface

---

## Key Papers and Documentation

| Source | What It Documents |
|--------|------------------|
| Förderportal des Bundes (continuously updated) | Official variable documentation; conditional publication policy |
| BMBF BuFI Datenband 2024 | Macro R&D spending; DASTAT/LPS methodology; authoritative source for total federal R&D figures |
| DZHW DASTAT project page | Provenance chain: PROFI → DASTAT → BuFI |
| Krieger, Rammer & Breithaupt (2020) — EconStor/ZEW | Direct methodological predecessor: text classification of Förderkatalog for cross-cutting themes; confirms LPS undercounting; ~10% short-description problem |
| Beckert et al. (2016) — EFI StuDIS 15/2016 | Keyword-based Förderkatalog analysis (robotics); flags data validity limitations |
| Brökel (2025) — EFI Studie Nr. 6-2025 | Combined regex + LPS filter approach for digitalization and decarbonization; documents LPS-regex overlap of only 12–37%; validates complementarity of both methods; extends Krieger et al. to decarbonization and network analysis. See [[20_summaries/brokel2025-forderung-digitalisierung-dekarbonisierung.md]]. |
| Kinne & Axenbeck (2024) — Int. J. Hydrogen Energy | Place-based R&D analysis using Förderkatalog; most recent peer-reviewed use (UNVERIFIED: verify author names against journal record) |

---

## Source Summaries

Detailed wiki summaries exist for the two most important references for this dataset:

- [[20_summaries/krieger2020-foerderkatalog-querschnitt.md]] — Krieger, Rammer & Breithaupt (2020): ZEW feasibility study on text-based classification of BMBF project descriptions. The only academic study doing thematic text classification on Förderkatalog data. Documents TexAn rule-based method, LPS undercounting evidence, short-text problem (~10% < 20 words), and failure of early ML (LSTM) approach on project abstracts. Direct methodological predecessor for TRL classification.

- [[20_summaries/bmbf2024-bundesbericht-datenband.md]] — BMBF (2024) Bundesbericht Forschung und Innovation Datenband: Official government statistics confirming the macro envelope around the Förderkatalog. Documents that Förderkatalog (direct Projektförderung, ~€10.1bn/year) is ~43% of total Bundesausgaben für FuE (~€23.4bn). Ministry breakdown: BMBF 57%, BMWK 21%, BMVg 9%. Confirms LPS Schwerpunktprinzip limitation and PROFI as the shared upstream data source.

---

## Comparison with CORDIS

| Dimension | Förderkatalog | CORDIS (H2020 + HE) |
|-----------|--------------|---------------------|
| Language | German | English |
| Funding scope | German federal direct project funding | EU collaborative R&D |
| Census completeness | No — selective ministerial disclosure | Yes — all EU-funded projects |
| TRL native field | No | No |
| Text length | Shorter on average (~10% under 20 words) | Generally longer; undocumented truncation risk |
| Financial completeness | Generally complete (federal share) | ~49% of HE projects missing total cost |
| Basic research coverage | Structurally low (institutional funding excluded) | Minority (ERC only) |
| Classification system | LPS (manual, single-topic) | EuroSciVoc (NLP, multi-label possible) |

---

## What it covers

The Foerderkatalog covers public records of German federal direct project
funding. For the Bundesinnovationshaushalt project it is the primary dataset
for project-level analysis of funding volume, ministry, recipient, project
description, topic code, and inferred TRL.

## Unit of observation

The unit of observation is an individual funded project or project row. Some
funding reference numbers may represent subprojects or related records, so
deduplication and FKZ handling must be checked before aggregation.

## Key variables

Key variables include FKZ, Ressort, recipient, location, project title/topic,
Leistungsplansystematik, funding period, funding amount, funding profile, and
funding type. The main NLP input is the project topic text plus the plain-text
Leistungsplansystematik field.

## Papers that discuss this dataset

Relevant linked sources include [[20_summaries/krieger2020-foerderkatalog-querschnitt.md]],
[[20_summaries/bmbf2024-bundesbericht-datenband.md]], [[20_summaries/efi2023-gutachten.md]],
and [[20_summaries/efi2024-gutachten.md]].

## Related methods and concepts

- [[40_methods/trl-klassifikation-pipeline.md]]
- [[40_methods/llm-few-shot-social-science.md]]
- [[30_concepts/technology-readiness-levels.md]]
- [[30_concepts/data-access-for-innovation-policy.md]]
- [[70_projects/bundesinnovationshaushalt-trl.md]]

## Relevant Projects

- **Bundesinnovationshaushalt TRL classification** — primary classification target; 39,555 active projects (April 2026 extract); primary text field: `Thema des geförderten Vorhabens`; no TRL labels; German-language NLP required
