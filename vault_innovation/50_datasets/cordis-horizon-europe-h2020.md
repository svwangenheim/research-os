# CORDIS: Horizon Europe and Horizon 2020

*Added: 2026-04-15 | Source: lit_review_cordis_foerderkatalog.md*

---

## Overview

CORDIS (Community Research and Development Information Service) is the European Commission's official public database of all EU-funded research projects, covering Framework Programmes FP1 through Horizon Europe (FP10 forthcoming). Bulk CSV downloads are available monthly from data.europa.eu and cordis.europa.eu. The Horizon Europe and Horizon 2020 sub-datasets are the two most commonly used by researchers.

**Bulk download:** cordis.europa.eu (monthly updates, public, no registration)
**Open data portal:** data.europa.eu

---

## Coverage

| Programme | Projects (our extract) | Period |
|-----------|------------------------|--------|
| Horizon Europe (HE) | ~19,476 | 2021– |
| Horizon 2020 (H2020) | ~34,135 | 2014–2020 |

Note: Both active and closed projects are included. Download date determines cut-off. Extract should be verified against official programme statistics from the European Commission.

---

## Dataset Structure

For both programmes, the bulk download is structured as multiple sub-tables. The primary file `project.csv` (HE: `HORIZON_projects.csv`) contains:

| Field | Description |
|-------|-------------|
| `id` | Unique project identifier |
| `title` | Project title |
| `objective` | Full project description — **primary free-text field for NLP** |
| `topics` | Call topic codes (e.g., `HORIZON-CL4-2023-TWIN-TRANSITION-01-17`) |
| `keywords` | Self-submitted applicant tags (unstandardised) |
| `fundingscheme` | ERC, RIA, IA, CSA, MSCA, etc. |
| `startdate`, `enddate` | Project duration |
| `totalcost` | Total project cost (incomplete — see biases) |
| `ecmaxcontribution` | EC grant amount |

Horizon Europe adds further sub-tables: `HORIZON_projectDeliverables`, `HORIZON_projectPublications`, `HORIZON_reportSummaries`, `HORIZON_ERC` (Principal Investigators).

**TRL field:** Does NOT exist in the public CORDIS bulk download. TRL must be inferred from `objective` text. The internal EC system (CORDA) contains self-reported TRL for approximately 16% of Horizon Europe projects (Trucco et al. 2025) — but CORDA is not publicly accessible.

---

## Key Text Field: `objective`

The `objective` field (plain text, English) is the primary input for any NLP-based classification of CORDIS projects. Known quality dimensions:

1. **Mandatory status:** Derived from signed grant agreements — in practice, virtually all funded projects have non-empty objectives.
2. **Length variation:** Character limits from Horizon Europe proposal templates apply on submission; whether the bulk CSV contains full text or a truncated display version is not documented in official sources. Researchers should compare a sample against the live CORDIS portal to check for truncation.
3. **Language quality:** Required in English regardless of consortium working language. Variable quality from non-anglophone consortia (machine-translated, formulaic, non-native).
4. **Boilerplate risk:** Some applicants reproduce call topic descriptions verbatim, inflating thematic similarity within a call and potentially misattributing call-level TRL ranges to specific projects.
5. **NLP precedent:** CORDIS's own Semi-Automatic Classification System (SACS) applies NLP to assign EuroSciVoc taxonomy codes to project texts, establishing that the objective field supports large-scale text classification.

---

## Known Biases and Quality Issues

**Structural selection biases (by design — not data errors):**

1. **Applied-research structural bias:** EU Horizon programmes require collaborative consortia and explicitly target "close-to-market" and "grand challenge" research (TRL 3–7). Pure basic science (TRL 1–2) is a minority even within the ERC pillar. Trucco et al. (2025) find ~68% of EU funding clusters at TRL 5–7.
2. **Consortium size requirement:** Minimum consortium sizes for most Horizon calls systematically exclude small single-PI research. CORDIS over-represents large collaborative applied projects.
3. **Geographic concentration:** High-capacity regions (Germany, Netherlands, Nordic countries) attract disproportionate funding. CORDIS is not representative of all EU member states equally (Buesa et al. 2024).
4. **No national funding:** National funding (BMBF, DFG, ANR, etc.) is entirely absent. CORDIS captures only the EU-funded portion of European R&D. German institutions can appear in both CORDIS (for EU-funded work) and the Förderkatalog (for German-funded parallel work) without deduplication.

**Data quality gaps:**

5. **`keywords` unstandardised:** Self-submitted by applicants; the same concept appears under different terms across projects.
6. **Organisation names not standardised:** Same organisation may appear under multiple name variants (documented by Varga et al. 2025 and Franke et al. 2025/EUPRO).
7. **Financial data incomplete:** ~49% of Horizon Europe projects report only EC contribution, not total cost. Financial weighting of TRL distributions is unreliable for a near-half of projects.
8. **TRL not in public data:** 83.7% of Horizon Europe projects have no TRL data even in the internal CORDA system (Trucco et al. 2025). Public bulk download contains no TRL field whatsoever.
9. **Monthly lag:** Datasets produced monthly; may lag real-time project approvals by up to one month.
10. **EuroSciVoc classification:** Semi-automatic NLP; human validation is incomplete and inconsistent. EuroSciVoc categories do not map to TRL.

---

## EU TRL Benchmark Distribution

From Trucco et al. (2025) — 2,462 Horizon Europe projects with TRL data (16.3% of portfolio):

| TRL Range | Share of EU Funding |
|-----------|---------------------|
| TRL 1–2 | ~16% |
| TRL 3–4 | ~16% |
| TRL 5–7 | ~68% |
| TRL 8–9 | ~16% |

Typical progression: 2–3 TRL steps per grant. This is the reference benchmark for comparing German federal R&D TRL distributions.

---

## Access

Grade A — Public download, no registration, monthly updates.

| Programme | URL |
|-----------|-----|
| Horizon Europe | `https://cordis.europa.eu/data/cordis-HORIZONprojects-csv.zip` |
| Horizon 2020 | `https://cordis.europa.eu/data/cordis-h2020projects-csv.zip` |
| Open data portal (HE) | `https://data.europa.eu/data/datasets/cordis-eu-research-projects-under-horizon-europe-2021-2027` |
| Open data portal (H2020) | `https://data.europa.eu/data/datasets/cordish2020projects` |

---

## Related Source Summaries

- [[20_summaries/krieger2020-foerderkatalog-querschnitt.md]] — Krieger et al. (2020) use the BMBF LPS taxonomy to compare German federal R&D funding across research areas, providing a benchmark for the relative scale of German vs. EU digitalization and AI funding. Relevant for interpreting German–EU comparative analyses that use both CORDIS and Förderkatalog.

---

## Key Papers Using This Dataset

| Paper | What It Does |
|-------|-------------|
| Trucco et al. (2025) — EC DG R&I | TRL distribution across 2,462 HE projects; confirms no TRL field in public data |
| Breschi & Malerba (2011) — Scientometrics | Early peer-reviewed use of CORDIS; establishes it is a complete census of EU-funded projects |
| Kosztyán et al. (2024) — Scientometrics | Institutional concentration across FP5–H2020; longitudinal CORDIS use |
| Buesa et al. (2024) — Scientometrics | Regional (NUTS-2) allocation of FP7 and H2020 funding |
| Varga et al. (2025) — Open Research Europe | Network analysis from CORDIS; documents org-name inconsistency |
| Franke et al. (2025) — Scientific Data | EUPRO reference database built on CORDIS; documents practical quality issues at scale |
| Moura Ferreira et al. (2022) — MDPI Documents | Bibliometric analysis; confirms objective text supports thematic keyword classification |

---

## TRL Classification from Text: Key Findings

- No prior academic work has classified CORDIS projects by TRL using text-based NLP methods (as of 2026-04-14 literature review).
- Regex scan of our HE + H2020 extract (53,611 projects total) identified 1,846 projects with explicit TRL mentions in `objective` text.
- Text-based TRL classification from `objective` is the only feasible approach given the absence of a native TRL field.
- CORDIS's own SACS system establishes methodological precedent for NLP classification of project objective text.

---

## What it covers

CORDIS covers EU-funded research and innovation projects under Horizon Europe
and Horizon 2020. In this vault it is used as the EU benchmark and training or
few-shot source for project-text classification.

## Unit of observation

The primary unit is a funded EU project. Related sub-tables contain
deliverables, publications, organizations, report summaries, and other project
metadata.

## Key variables

Key variables include project ID, title, objective text, call topic, keywords,
funding scheme, dates, total cost, EC contribution, participants, deliverables,
and publications. The `objective` field is the main text field for NLP.

## Related methods and concepts

- [[40_methods/trl-klassifikation-pipeline.md]]
- [[40_methods/xlm-roberta-multilingual-classification.md]]
- [[40_methods/llm-few-shot-social-science.md]]
- [[30_concepts/technology-readiness-levels.md]]
- [[30_concepts/data-access-for-innovation-policy.md]]

## Relevant Projects

- **Bundesinnovationshaushalt TRL classification** — downloaded HE (19,476 projects) and H2020 (34,135 projects); used as international comparison benchmark against Förderkatalog; 1,846 projects with explicit TRL regex matches identified
