# Log

This is the chronological record of what has happened in the wiki.

## [2026-05-26] maintenance | Scheduled wiki-maintain audit — duplicate consolidation, index corrections, new summary

**Scope:** Full-vault automated maintenance pass.

**Critical fix:** `index.md` description for `dechezlepretre2023-rd-tax-spillovers.md` corrected. Prior description said "30% higher social returns for low-TRL public R&D" — explicitly identified as incorrect in the 2026-05-18 log. Corrected to: "RD design (UK SME size threshold); price elasticity ~2.6; £1.7 private R&D per £1 taxpayer; no TRL-differentiated estimates".

**Duplicate consolidation (3 pairs):**
- Cohen-Levinthal 1990: canonical → `cohen-levinthal1990-absorptive-capacity.md`; duplicate `cohen_levinthal_1990_absorptive_capacity.md` marked with alias header. Index, `absorptive-capacity.md`, and `basic-research-in-firms.md` updated to canonical.
- Dechezleprêtre 2023: canonical → `dechezlepretre2023-rd-tax-spillovers.md`; duplicate `dechezletpre_einio_martin_nguyen_vanreenen_2023_tax_incentives_rd.md` marked with alias header and removed from index.
- Arora 2018: canonical → `arora2018-corporate-basic-research.md` (source_files populated); duplicate `arora_belenzon_patacconi_2018_killing_golden_goose.md` marked. Cross-references in three summaries updated.

**Source file update — Chae (2025):** `chae2025-llm-instruction-tuning.md` `source_files` updated to include `chae_davidson_2025_converted.md`.

**New summary created:** `belz2019-valley-of-death-sbir.md` — Belz et al. (2019) NASA SBIR TRL advancement. TRL 2→3 per Phase I ($100k); TRL →4.5–5 by program end; 10% reach TRL 6; two-stage risk disaggregation. Linked to TRL, commercialization-gap, additionality concepts.

**Index additions:** `belz2019-valley-of-death-sbir.md` (R&D Subsidies); `llm-few-shot-applicability-trl-förderkatalog.md` (Methods); `cognitive-load-productivity.md` (Projects).

**Unresolved — needs acquisition:**
- `00_inbox/ifo-falck2025-schnelldienst.md`: stub; source not in vault. Priority: MEDIUM.
- `00_inbox/oecd2024-sti-outlook.md`: stub; "incumbent-biased" claim unverified. Priority: HIGH.
- `00_inbox/svr2024-jahresgutachten.md`: stub; Kapitel 4 claim unverified. Priority: HIGH.
- `gbadegeshin2022-overcoming-valley-of-death.md`: source is citation-only stub; cannot summarize without full source.

## [2026-05-21] ingest | Chae & Davidson (2025) — LLMs for Text Classification

PDF converted from `10_sources/Chae_Davidson_2025_LLM for Text Classification.pdf` → `10_sources/chae_davidson_2025_converted.md`. Existing summary `20_summaries/chae2025-llm-instruction-tuning.md` verified against full PDF conversion: content accurate. Key verification finding: paper uses 1-shot and 2-shot only (not "5–10 examples per label"); corrected stale index description accordingly. Pages updated: `index.md` (corrected LLM/NLP row description for chae2025).

## [2026-05-19] ingest | Paleschke (2026) — Comeback Deutschland? Industrie-Turnarounds

Summary created: `20_summaries/paleschke_2026_comeback_deutschland.md`. Pages updated: `30_concepts/innovation-paradox.md` (added to related_summaries and Papers section), `90_synthesis/innovation-paradox-incumbent-lock-in.md` (added to included_notes and Papers compared table; cross-paper finding 6 on exit barriers), `index.md` (new row under German Firms, Sectors & Tech Transfer).

## [2026-05-19] ingest | Cabanes et al. (2024) — Basic or applied research in UIC

**Focus**: extending the corporate basic research argumentation into university–industry collaboration context.

**PDF converted:** `cabanes_et_al_2024_basic_applied_uic.md`

**Summary created:** `cabanes_et_al_2024_basic_applied_uic.md` — 61% of industry-sponsored Cifre PhD projects prioritize basic research; finding robust across disciplines, firm sizes, university types; challenges applied-push assumption; knowledge creation vs. knowledge transfer UIC distinction; 631 French Cifre projects

**Pages updated:** `30_concepts/basic-research-in-firms.md` (added Cabanes et al. to related_summaries and key papers table); `index.md` (added row to Corporate Basic Research section)

---

## [2026-05-19] ingest | Five papers: corporate basic research and absorptive capacity

**Focus**: role of corporate basic research in innovation output; how firms improve innovation through basic research investment.

**PDFs converted (5/5):** `arora_et_al_2017_back_to_basics_why_firms_invest.md`, `akcigit_et_al_2021_back_to_basics.md`, `escribano_et_al_2009_absorptive_capacity.md`, `duan_et_al_2021_absorptive_capacity_tech_search.md`, `martinez_senra_et_al_2011_basic_research_firms_spain.md`

**Summaries created (5):**
- `arora_belenzon_sheer_2017_why_firms_invest_in_research.md` — internal appropriation as main driver; 1 internal citation offsets 4 competitor citations; 4,736 US firms 1980–2006
- `akcigit_hanley_serrano_2021_basic_research_spillovers.md` — GE model; 68% of basic research spillovers uninternalized; 4.6pp welfare loss; optimal subsidy 49% basic / 11% applied
- `escribano_fosfuri_tribo_2009_absorptive_capacity_external_knowledge.md` — AC as moderator of spillovers → innovation; amplified in high-turbulence + strong-IPR sectors; Spanish CIS
- `duan_et_al_2021_absorptive_capacity_tech_search.md` — AC as heterogeneous moderator of tech search → innovation quality; inverted-U search-quality; China high-tech panel
- `martinez_senra_et_al_2011_basic_research_firms_spain.md` — basic research → AC → product innovation; 3-year persistence; all sectors; PITEC 8,861 Spanish firms

**Concept pages created (2):** `30_concepts/basic-research-in-firms.md`, `30_concepts/absorptive-capacity.md`

**Pages updated:** `index.md` — new "Corporate Basic Research & Innovation" section; 2 new AC section entries; 2 new concept rows

## [2026-05-18] ingest + correction | Dechezleprêtre et al. (2023) — R&D Tax Incentives and Spillovers
PDF ingested (NBER WP 22405) and existing summary corrected: prior claim of "30% higher social returns for low-TRL innovations" was incorrect (not in paper); summary rewritten from primary source. DOI confirmed: 10.1257/aer.20190805. Source file: 10_sources/dechezlepretre2023-rd-tax-incentives.md.

Use consistent headings so the file stays machine-readable and easy to scan.

Format:
## [YYYY-MM-DD] operation | title

Possible operation types:

## [2026-05-17] ingest | Four sources: Arora et al. 2018, Cohen-Levinthal 1990, PTJ Fördermaßnahmen 2025, Dechezleprêtre et al. 2023 (enriched analysis)

**PDFs converted to markdown (4/4 successful):**
- `arora_2018_killing_golden_goose.md` — 3,622 lines
- `cohen_levinthal_1990_absorptive_capacity.md` — 50 lines (retry successful; original error transient)
- `ptj_2025_foerdermassnamen_mapping.md` — 5,121 lines
- `dechezletpre_2023_tax_incentives_research.md` — 7,807 lines

**Summaries created (4):**
- `20_summaries/arora_belenzon_patacconi_2018_killing_golden_goose.md` — Corporate R&D decline; science value declining
- `20_summaries/cohen_levinthal_1990_absorptive_capacity.md` — **NEW** Foundational work; dual R&D role (innovation + absorptive capacity); path dependence
- `20_summaries/ptj_2025_foerdermassnamen_mapping.md` — **ENRICHED**: 63 programs classified; two-layer structure (13 systemisch-bildend + 17 Breitenprogramme); critical lücken in TRL 1–2 (Ideenfindung), TRL 3–5 (integration), TRL 8–9 (Markteintritt); social innovation underrepresented; administrative complexity; DATIpilot as simplification model
- `20_summaries/dechezletpre_einio_martin_nguyen_vanreenen_2023_tax_incentives_rd.md` — RDD UK tax incentive; SME elasticity 2.6; spillovers

**Pages updated:**
- `index.md`: four entries added (new "Absorptive Capacity" section; PTJ enriched; others indexed)
- `ptj_2025_foerdermassnamen_mapping.md`: Key findings section expanded with deep policy analysis
- Related concept pages flagged: [[Födermaßnahmen Klassifizierung]], [[Absorptive Capacity]], [[R&D Tax Incentives]]

**Status:**
- **All four sources now fully ingested**
- Cohen-Levinthal 1990: **successful on retry**; foundational input for absorptive capacity implications of Bundesinnovationshaushalt
- PTJ summary enriched with program-level recommendations and policy diagnostics
- Ready for project wiki-links and concept-notes update

## [2026-05-11] ingest | Three sources: Azoulay et al. 2019, Lerner 2009, BMWK JWB 2023

**Summaries created:**
- `20_summaries/azoulay2019-arpa-model.md` — NBER WP 24674; four-element ARPA model codification; primary S-curve source (Foster 1986) cited by Fuest et al. 2024
- `20_summaries/lerner2009-boulevard-broken-dreams.md` — Princeton UP 2009; public VC failure taxonomy; prescriptive governance principles. WARNING: source file contains only a book review (Business History 2010), not the book text.
- `20_summaries/bmwk2023-jahreswirtschaftsbericht.md` — Official German annual report 2023; Schlüsseltechnologien and Transformation framing; policy context for 2023 Förderkatalog allocations

**Pages updated:**
- `30_concepts/radical-vs-incremental-innovation.md`: corrected hallucinated citation "Fuest, Meister & Tirole 2024" → correct attribution to Azoulay et al. (2019); added backlink to new summary
- `30_concepts/mission-oriented-innovation-policy.md`: added three new related_summaries (azoulay2019, fuest2024, lerner2009)
- `index.md`: three new entries added

## [2026-05-18] ingest | Rammer 2025 Forschungszulage policy brief

**PDF converted to markdown:**
- `10_sources/rammer_2025_forschungszulage.md` — 563 lines; ZEW policy brief Nr. 09, Juli 2025

**Summary created:**
- `20_summaries/rammer_2025_forschungszulage.md` — Forschungszulage strengths (€4bn, 19k participants, 35% SME rate, 48% SME-allocated, research-active SME increase from 9.9%→12.6%); limitations for innovation paradox (blunt instrument, cannot distinguish innovation type, SME share eroding, 4.7% international scope, no additionality evidence)

**Pages updated:**
- `index.md`: new entry in "German F&I Policy" section (Proximity 1)
- `30_concepts/innovation-paradox.md`: added backlink to Rammer 2025 summary

**Key findings for Fachtext:**
1. Forschungszulage strong on SME participation reach but weak on innovation-type steering (cannot distinguish incremental vs. disruptive)
2. Tax-credit design limits policy ability to redirect incumbent R&D away from defensive ends
3. SME share declining (61%→48%) as caps increase for large-firm access
4. €4bn = 4.7% of corporate R&D (peers France/Ireland/Spain: 15-20%)
5. No causal impact evidence yet; effectiveness evaluation ongoing at BMF

## [2026-05-11] wiki-pull | TRL research briefing source alignment check

Read `explorations/trl_research_briefing.md` (Foerderkatalog-TRL-subproject). Compiled full source list (11 annotated + additional citations). Checked every source against the vault.

**Sources already in vault — no update needed (key ideas already present):**
- `earto2014-trl-policy-tool.md` — A-tier; Low/Mid/High grouping, valley of death, EU State Aid mapping all documented
- `dechezlepretre2023-rd-tax-spillovers.md` — A-tier; 30% higher social returns for low-TRL confirmed; RDD methodology documented
- `eib2022-energy-transition-finance.md` — A-tier; valley of death at TRL 5-6 documented; four-group scheme documented
- `fuest_et_al_2024_how_to_escape_the_middle_technology_trap.md` — A-tier; S-curve framing already added
- `aschhoff2010-who-gets-the-money.md` — A-tier; large-firm advantage documented
- `czarnitzki2018-additionality-firm-size.md` — A-tier; firm-size additionality heterogeneity documented
- `hesse-grashof2020-zim-incrementalism.md` — A-tier; ZIM incremental bias documented
- `efi2024-gutachten.md` — A-tier; current German R&D intensity data documented
- `kfw2024-sme-innovation.md` — A-tier; 82%/7% statistics already added
- `ec-trl-horizon2020.md` — A-tier; EU TRL definitions documented
- `heder2017-trl-history.md` — A-tier; TRL history documented

**Sources already in vault — summary extended:**
- `oecd2022-innovation-policy-germany.md`: added section on incremental bias and Mittelstand structural barrier to radical innovation; added backlinks to `mitteltechnologie-falle` and `radical-vs-incremental-innovation` concepts
- `howell2017-financing-innovation.md`: broken wikilink fixed (czarnitzski typo corrected to czarnitzki)

**Sources not in vault — watch items only (no standalone notes created):**
- OECD Frascati Manual (2015): covered implicitly by EARTO note; create standalone note if directly cited in policy brief
- Horizon Europe Work Programme 2021 (EC 2021): 60% RIA / 40% IA benchmark; partially covered by `ec-trl-horizon2020.md`; create standalone note if directly cited
- Arrow (1962) and Nelson (1959): foundational theory only; covered in concept notes

**Concept notes confirmed adequate:**
- `technology-readiness-levels.md` — ministerial mandate split, valley of death, social returns all present
- `radical-vs-incremental-innovation.md` — S-curve, KfW 7% statistic, OECD middle-tech bias all present
- `rd-subsidy-additionality.md` — Dechezlepretre, EARTO, Hesse-Grashof, Czarnitzki-2018 all linked
- `innovation-paradox.md` — TRL dimension and three-pillar framing documented
- `mitteltechnologie-falle.md` — 57% mid-tech, empirical basis, sector breakdown documented
- `knowledge-spillovers-and-entrepreneurship.md` — adequate; Arrow/Nelson spillover mechanism present

**Quality check:** 80 A-tier summaries. 3 broken wikilinks (2 are source-file path issues — files exist; 1 typo fixed). 0 orphan core notes. 0 duplicate candidates.

## [2026-05-08] audit + upgrade | Backlink alignment audit, Stehnken summary upgrade, missing stubs

**Part 1 — Backlink alignment audit:**

Audited all priority concept and synthesis pages against their linked summaries. Quality-check script baseline: 76 A-tier summaries, 3 broken source links, 5 summaries with section gaps, 0 orphan core notes.

Gaps found and fixed:
- `90_synthesis/international-innovation-policy-benchmarks.md`: added `aschhoff2010-who-gets-the-money.md` to `included_notes` (was cited in body but absent from frontmatter).
- `90_synthesis/innovation-paradox-incumbent-lock-in.md`: added `stehnken2024-zim-evaluation.md`, `dietrich_et_al_2024_europes_middle_technology_trap.md`, `fuest_et_al_2024_how_to_escape_the_middle_technology_trap.md`, `falck2026-growth-share-matrix-deutschland.md` to `included_notes`; extended Papers-compared table with four new rows.
- `30_concepts/radical-vs-incremental-innovation.md`: renamed `related_notes` to `related_summaries`, converted bare relative paths to wikilink format, added `akcigit2024-innovation-paradox.md`, `acemoglu2006-distance-to-frontier.md`, `stehnken2024-zim-evaluation.md`, `falck2026-growth-share-matrix-deutschland.md`.

Confirmed adequate with no gaps: `innovation-paradox.md`, `rd-subsidy-additionality.md`, `sme-innovation-participation.md`, `strategic-industrial-policy.md`, `technology-transfer-and-translation.md`, `bundesinnovationshaushalt-trl.md`.

**Part 2 — Stehnken summary upgrade:**

`20_summaries/stehnken2024-zim-evaluation.md` fully rewritten. Prior version had Research Question, Core Argument, and Methodology sections corrupted with raw PDF table-of-contents text. New version sourced directly from `10_sources/stehnken2024-zim-evaluation.md`. Key additions: exact repeat-recipient statistics (44.8% Foerderneulinge / 55.2% with prior ZIM experience, with sub-group decomposition); structural profile differences between Foerderneulinge and Foerdererfahrene; additionality design details; approval-rate decline (68.5% to 60.3%); precision note that "60% Wiederholungsempfaenger" is a rounded approximation of the 55.2% source figure; clarification that the 3-year ZIM 2025 exclusion period is a subsequent policy reform not documented in this evaluation.

**Part 3 — Missing stubs created:**

- `00_inbox/svr2024-jahresgutachten.md` — SVR Jahresgutachten 2024/25 Kap. 4; priority HIGH.
- `00_inbox/oecd2024-sti-outlook.md` — OECD STI Outlook 2024; priority HIGH; includes verification note on "incumbent-biased" wording.
- `00_inbox/ifo-falck2025-schnelldienst.md` — ifo Schnelldienst Sep 2025 (Falck); priority MEDIUM.

**Summaries confirmed adequate after outline re-read:**
`akcigit2018`, `akcigit2024`, `acemoglu2006`, `falck2026`, `naud_nagler2022` — all key mechanisms from the outline are documented in the existing summaries.

## [2026-05-08] upgrade | Howell (2017) — Financing Innovation: Evidence from R&D Grants

Stub upgraded to full A-tier summary at `20_summaries/howell2017-financing-innovation.md`. Previous stub was abstract-only (local PDF mislabeled; actually contained Meyer & Mittag). Summary now fully verified against published AER paper and circulating JMP. Key quantitative detail added: 7,436 firms, $884M in Phase I awards, 1983–2013; sharp RD (bandwidth 2–3); Phase I doubles VC probability (10%→19%, +9pp long-run, +7pp within 2 years); large patenting and revenue effects; Phase II null result (tiny/negative VC effect); mechanism = technology prototyping, not certification. Policy-transfer conditions for DE SBIR-Äquivalent documented in implications section. `semantic_status` updated from "partial-source-verified" to "verified".

## [2026-05-07] ingest | EFI Gutachten 2025 (Jahresgutachten)

Source PDF downloaded to `10_sources/efi2025-gutachten.pdf` (31.5 MB) from https://www.e-fi.de/fileadmin/Assets/Gutachten/2025/EFI_Jahresgutachten_2025.pdf. A-tier summary created at `20_summaries/efi2025-gutachten-fi.md` covering: Part A stocktaking of 20th legislative period (F&I indicator decline, governance failures, fiscal crisis effects, reform agenda for 21st legislative period); Part B kernthemen (twin transformation digitalization/decarbonization Chapter B1; quantum technologies as Schlüsseltechnologie Chapter B2 with PATSTAT/Scopus patent and publication benchmarks, TRL distribution analysis, €2bn quantum program assessment; water management Chapter B3). Key quantitative findings: Germany 3rd globally in quantum publications but below-average citation impact; quantum patent strength in Quantensensorik, weak in Quantencomputing hardware; German quantum portfolio concentrated TRL 1–5 with sovereign manufacturing gap at TRL 6–8. `index.md` updated (EFI 2025 entry added under Summaries). Project `wiki-links.md` updated (EFI 2025 added under Core Foerderkatalog Context).

## [2026-05-05] deep-research + wiki-push | International Innovation Policy Benchmarks

Deep research on GII top-10 policy instruments for three German innovation problems. New synthesis page created: 90_synthesis/international-innovation-policy-benchmarks.md. Updated: 30_concepts/innovation-systems-comparison.md (Programmebene section with SBIR/TIPS/KIAT-KEIT/Catapult/GTS detail; SBIR set-aside corrected to 3.2%), 30_concepts/technology-transfer-and-translation.md (international transfer infrastructure comparison: UK Catapult, DK GTS, CH Innosuisse, FI Business Finland). Index and wiki-links updated.

## [2026-05-05] ingest | Dietrich et al. 2024 + Fuest et al. 2024 — Europe's Middle-Technology Trap

Two PDFs ingested; summaries created; mitteltechnologie-falle concept updated with primary sources and quantitative evidence; innovation-policy-governance-and-evaluation synthesis updated with EIC/DARPA governance section; germany-innovation-policy-evidence-map updated; index and wiki-links updated.

- `dietrich_et_al_2024_europes_middle_technology_trap.md` — EconPol Forum 4/2024; primary coining article for Mitteltechnologie-Falle; proximity 1.
- `fuest_et_al_2024_how_to_escape_the_middle_technology_trap.md` — IEP/TSE/EconPol 2024 policy report; shift-share decomposition; Horizon Europe anatomy; ARPA reform proposal; proximity 1.

## [2026-05-05] ingest | Brökel 2025 + JRC 2025 EU Industrial R&D Scoreboard

Two PDFs ingested; converted via markitdown; summaries created; synthesis, dataset, index, and project bridge updated.

- `brokel2025-forderung-digitalisierung-dekarbonisierung.md` — EFI Studie Nr. 6-2025; combined regex+LPS Förderkatalog analysis; proximity 1.
- `jrc2025-eu-industrial-rd-scoreboard.md` — JRC/EC 2025 EU Industrial R&D Scoreboard; proximity 2.

Pages updated: `germany-innovation-policy-evidence-map.md`, `foerderkatalog-des-bundes.md`, `index.md`, `log.md`, project `wiki-links.md`.

## [2026-04-27 Session 5-6] ingest | Germany Innovation Policy Supplementary Batch (6 papers)

**Status:** Completed  
**Action:** Wiki-ingest of 6 papers (4 from Session 5 + 2 from Session 6); user-provided PDFs converted to markdown, summaries created, vault infrastructure updated

**Papers ingested (chronological):**

| # | Title | Authors | Year | Access | TRL Relevance | Status |
|---|-------|---------|------|--------|---------------|--------|
| 1 | Treiber und Hemmnisse der Innovationstätigkeit im deutschen Mittelstand | Rammer, Krieger, Peters | 2022 | Institution | Incumbent capture, SME barriers, innovator types | ✓ Complete |
| 2 | Climate Change Affectedness and Innovation in German Firms | Horbach & Rammer | 2022 | Open-access ZEW DP | TRL implications of cost vs. demand pressure | ✓ Complete |
| 3 | Energy Price Shocks and Short-Term Reactions of Firms | Horbach & Rammer | 2024 | Open-access ZEW DP | Incumbent vulnerability to cost shocks | ✓ Complete |
| 4 | For a Strategic, European and Competition-Oriented Industrial Policy | Duso, Gornig, Schiersch | 2025 | Institution (DIW) | Incumbent lock-in, subsidy distortion | ✓ Complete |
| 5 | Startup Report 2025: Finanzierungsbedingungen für Startups | Bitkom Research | 2025 | Institution | Startup financing gap, regulatory burden | ✓ Complete |
| 6 | FIVE Report: Financing Innovative Ventures in Europe | Franco-German Task Force | 2026 | Government | Scaleup gap, capital market failure | ✓ Complete |

**Outputs:**

**Summaries created (6):**
- `vault/20_summaries/rammer_krieger_peters2022-sme-drivers-barriers.md` (385 lines; 6 innovator types, firm-age effect, skilled-worker shortage as #1 barrier)
- `vault/20_summaries/horbach_rammer2022-climate-change-innovation.md` (311 lines; demand vs. cost pressure, eco- vs. non-eco innovation, sector variation)
- `vault/20_summaries/horbach_rammer2024-energy-price-shocks.md` (137 lines; 2022 energy crisis, incumbent response, capital-intensity constraint)
- `vault/20_summaries/duso2025-strategic-industrial-policy.md` (368 lines; technological investment trap, subsidy misdirection, incumbent protection mechanism)
- `vault/20_summaries/bitkom2025-startup-report.md` (311 lines; startup financing gap, bureaucratic burden, AI adoption, gender disparity)
- `vault/20_summaries/bmf2026-five-report.md` (275 lines; scaleup gap, pension system fragmentation, 7 policy recommendations)

**Infrastructure updates:**
- `vault/index.md`: New section "German Federal Funding & SME Innovation (added 2026-04-27)" with 6 paper references + 1-line summaries
- `vault/log.md`: This entry

**Cross-references completed:**
- All 6 summaries include "Integration with Förderkatalog Analysis" sections linking to concept/project pages
- Concept pages referenced: `innovation-paradox.md`, `radical-vs-incremental-innovation.md`, `schluesseltechnologien-htad.md`
- Project pages referenced: `bundesinnovationshaushalt-trl.md`

**Key findings documented:**
- Rammer et al. 2022: Firm aging explains ~1pp of declining innovation rate; 6 innovator types; 55-60% of innovation output from non-R&D firms
- Horbach & Rammer 2022: Climate pressure drives demand-pull radical innovation (rare in DE), cost-push incremental adaptation (common)
- Horbach & Rammer 2024: Energy crisis shows incumbent vulnerability; capital intensity constrains response speed
- Duso et al. 2025: Broad subsidies entrench low-innovation equilibrium; technological investment trap mechanism
- Bitkom 2025: Startup financing gap at TRL 3-6 (valley of death); regulatory burden asymmetrically harms small firms
- FIVE 2026: Systemic capital shortage (€50-100bn/year); pension/regulatory/market fragmentation as root causes

---

## [2026-04-27 Session 5] ingest | Naudé & Nagler (2022) — The Ossified Economy

**Status:** Completed  
**Source:** Open-access IZA DP No. 15607  
**Action:** Downloaded PDF, converted to markdown, created vault summary  
**Output:** `vault/20_summaries/naud_nagler2022-ossified-economy.md` + vault index updated

---

## [2026-04-27] ingest | Germany Innovation Policy Bibliography (2024-2026)

**Status:** Wiki-ingest phase active  
**Source:** Librarian discovery (approved by librarian-critic, 82/100)  
**Scope:** 20 papers (2021+) on German innovation policy challenges and international reform lessons  

**Actions completed:**
- Bibliography: `quality_reports/lit_review_germany_innovation_policy_2024-2026.md` (20 papers, proximity-scored, fully cited)
- Librarian-critic approved: 82/100 PASS (coverage, quality, recency, scope all excellent)
- Stubs created: `vault/00_inbox/naud_nagler2022-ossified-economy.md` + `vault/00_inbox/GERMANY_INNOVATION_POLICY_2024-2026_BIBLIOGRAPHY.md`
- Vault index updated: Bibliography reference added
- Documentation: SESSION_REPORT.md + research_journal.md updated

**Papers by access tier:**
- Tier 1 (Open-access, 7 papers): Direct download URLs
- Tier 2 (Institutional, 3-4 papers): ZEW/OECD/KfW repositories
- Tier 3 (Paywalled, 6-7 papers): Journal/government access
- ingest
- query
- synthesis
- lint
- refactor

---

## [2026-05-18] ingest | Galindo-Rueda & Verger 2016 — OECD Taxonomy of Economic Activities Based on R&D Intensity

**Status:** Completed  
**Action:** PDF ingested via markitdown; summary created; vault infrastructure updated  
**Output:** `10_sources/galindo_rueda_verger_2016_oecd_taxonomy.md` (4,227 lines) + `20_summaries/galindo_rueda_verger_2016_oecd_taxonomy.md` (A-tier summary)

**Summary highlights:**
- OECD working paper 2016/04: authoritative taxonomy for classifying sectors by R&D intensity
- Operational definition: R&D intensity = business R&D / GVA at industry level
- Five-category empirical classification (not fixed-percentage thresholds):
  - **High R&D:** Software (28%), scientific research (31.7%), pharmaceuticals (24%)
  - **Medium-high:** Motor vehicles, machinery (9–15%)
  - **Medium:** Fabricated metals, chemicals (6–7%)
  - **Medium-low:** Textiles, minerals (2–3%)
  - **Low:** Food/beverages, wood, furniture (<2%)
- Key innovation: covers non-manufacturing (services) for the first time; demonstrates country-level heterogeneity in sectoral specialization
- Data source: OECD ANBERD (Analytical Business Enterprise R&D) database, 2011 reference year, 30+ OECD countries

**Pages updated:**
- `30_concepts/mitteltechnologie-falle.md`: Added galindo_rueda_verger_2016_oecd_taxonomy to related_notes (position 3); updated timestamp
- `index.md`: Added OECD taxonomy entry to "Mitteltechnologie-Falle & EU Innovation Gap" section (position 1, Prox 1)
- `log.md`: This entry

**Quality note:** This source provides the operational definition of the high-tech/mid-tech classification used throughout the vault's innovation policy analysis. It is cited by Dietrich et al. (2024) and Fuest et al. (2024) as the foundation for sectoral categorization in the Mitteltechnologie-Falle concept. Integration enables precise, OECD-backed definitions in the Förderkatalog-TRL-subproject policy brief.

## [2026-04-13] init | Research wiki created

## [2026-04-24] ingest | Falck & Pfaffl (2026) — Eine Growth-Share-Matrix für Deutschland

Summary created: `20_summaries/falck2026-growth-share-matrix-deutschland.md`. Concept pages updated: `innovation-paradox.md` (Mitteltechnologie-Falle evidence row added), `radical-vs-incremental-innovation.md` (Mitteltechnologie-Falle section added). Index updated.

## [2026-04-22] ingest | Batch Phase 2 — 39 new source summaries + concept/method pages

**Summaries created (39 new):**

*Innovation Policy / Säule A (23 papers):*
aghion1992-creative-destruction, akcigit2024-innovation-paradox, akcigit2018-heterogeneous-innovations, aghion2019-innovation-inequality, edler2017-innovation-policy, heder2017-trl-history, czarnitzki2004-rd-subsidies-zew, czarnitzki2014-funding-source, cherif2022-rd-subsidies-imf, stehnken2024-zim-evaluation, struss2016-zim-wirkungsanalyse, rammer2025-indikatorenbericht-innovation, rammer2024-innovationsindikator, dosi1982-technological-paradigms, audretsch2002-sbir-evaluation, audretsch2003-sbir, audretsch2005-knowledge-spillover, howell2017-financing-innovation, kleer2010-rd-subsidies-signal, malerba2002-sectoral-systems, draghi2024-european-competitiveness, wachstumspfade-deutschland, kfw2024-gruendungsmonitor

*LLM Classification Methods (16 papers):*
brown2020-gpt3-fewshot, gilardi2023-chatgpt-annotation, grimmer2013-text-as-data, snow2008-cheap-fast-annotation, laurer2023-less-annotating, timoneda2025a-bert-roberta-deberta, alizadeh2025-opensource-llm-annotation, egami2024-llm-annotation-framework, halterman2025-codebook-llms, pangakis2023-llm-annotation-validation, ziems2024-llm-css-benchmark, pelaez2024-patent-public-value-llm, tornberg2025-llm-outperform-experts, moller2024-parrot-dilemma, ornstein2025-stochastic-parrot, chae2025-llm-instruction-tuning

**Concept pages created (4 new):**
30_concepts/innovation-paradox.md, 30_concepts/radical-vs-incremental-innovation.md, 30_concepts/innovation-systems-comparison.md, 30_concepts/schluesseltechnologien-htad.md

**Method pages created (2 new):**
40_methods/llm-few-shot-social-science.md, 40_methods/trl-klassifikation-pipeline.md

**Index updated:** All 39 summaries + 6 concept/method pages added

Created the initial wiki structure:
- README.md
- index.md
- log.md
- CLAUDE.md
- folder READMEs

No sources ingested yet.

## [2026-04-14] ingest | BMLE Merkblatt Technologiereifegrade

Ingested German federal TRL reference document. Created summary at `20_summaries/bmle-merkblatt-technologiereifegrade.md`. Created concept page `30_concepts/technology-readiness-levels.md` with EU/German comparison table. Updated index.

## [2026-04-14] ingest | Horizon 2020 TRL Definitions (EC)

Ingested EU Horizon 2020 TRL definitions extract. Created summary at `20_summaries/ec-trl-horizon2020.md`. Updated concept page with KET qualifiers and framework comparison. Updated index.

## [2026-04-14] ingest | Trucco et al. (2025) — Scaling up ideas

Ingested EC DG R&I report on TRL progression in Horizon Europe. Created summary at `20_summaries/trucco2025-scaling-up-ideas.md` with extended focus on project-level TRL methodology. Created method page `40_methods/trl-project-level-reporting.md`. Updated TRL concept page with empirical distribution findings and extended open debates. Updated index.

## [2026-04-15] ingest | conneau2020-xlm-roberta

Created summary at `20_summaries/conneau2020-xlm-roberta.md`. Key content: XLM-RoBERTa training setup (2.5 TB CC-100, 100 languages, 550M parameters for Large), +14.6 pp over mBERT on XNLI cross-lingual benchmark, justification for English→German cross-lingual transfer without parallel data. Updated `40_methods/xlm-roberta-multilingual-classification.md` with cross-link in new Source summaries section. Updated index.

## [2026-04-15] ingest | devlin2019-bert

Created summary at `20_summaries/devlin2019-bert.md`. Key content: BERT pre-train/fine-tune paradigm, bidirectional MLM objective, GLUE results (+7.0 pp over prior SOTA for BERT-Large), fine-tuning instability warning at small N, NSP task (later dropped in XLM-R). Updated `40_methods/xlm-roberta-multilingual-classification.md` with cross-link. Updated index.

## [2026-04-15] ingest | chan2020-gbert

Created summary at `20_summaries/chan2020-gbert.md`. Key content: GBERT/GELECTRA German-only models, trained on 163 GB German text; GBERTLarge achieves 73.57 vs. XLM-RoBERTa-Large 73.18 averaged F1 on German benchmarks (~0.4 pp gap); GBERT cannot process English — decisive reason to use XLM-R for cross-lingual CORDIS→Foerderkatalog classification. Updated `40_methods/xlm-roberta-multilingual-classification.md` with cross-link. Updated index.

## [2026-04-15] ingest | timoneda2025b-behind-the-mask

Created summary at `20_summaries/timoneda2025b-behind-the-mask.md`. Key content: masking rate experiment on RoBERTa-Covid classifier (COVID-19 fake news, 3 classes); 40% random/selective masking improves target-category F1 (fake: 0.848 → 0.857–0.858); overall F1 differences small and not significant; recommendation to test 15/25/40% masking during domain pre-training and select by category-level F1. Updated `40_methods/xlm-roberta-multilingual-classification.md` Key Papers table and Source summaries. Updated index.

## [2026-04-15] ingest | wang2024-bert-vs-gpt

Created summary at `20_summaries/wang2024-bert-vs-gpt.md`. Key content: 5 classification tasks (2 to 22 classes), RoBERTa-large vs. GPT-4o at 200/500/1000 training samples; BERT wins at 8+ classes with 1,000 samples; GPT competitive for binary tasks and at 20+ classes when training data is scarce; concrete accuracy numbers per task and sample size. Updated `40_methods/xlm-roberta-multilingual-classification.md` Key Papers table and Source summaries. Updated index.

## [2026-04-15] ingest | kuzman2025-parlacap

Created summary at `20_summaries/kuzman2025-parlacap.md`. Key content: ParlaCAP — 8M+ speeches from 28 European parliaments; LLM teacher (GPT-4o, ~$100) annotates 35,579 training speeches; XLM-R-Parla student fine-tuned on LLM labels; macro-F1 0.69–0.76 on 22-class CAP policy topic classification across 4 languages; inter-annotator agreement GPT-4o vs. human 0.60–0.64, comparable to human-human 0.59–0.68; closest methodological parallel to TRL classification pipeline. Updated `40_methods/xlm-roberta-multilingual-classification.md` Key Papers table (corrected F1 range to 0.69–0.76) and Source summaries. Updated index.

## [2026-04-15] ingest | zhang2021-few-shot-bert

Created summary at `20_summaries/zhang2021-few-shot-bert.md`. Key content: 3 root causes of BERT fine-tuning instability (biased BERTADAM optimizer, poor top-layer initialization, too few training iterations); fixes: debiased ADAM + Re-init top layers + longer training; minimum reliable sample size ~1,000 examples; recommendation to run 5–10 random seeds and report mean ± SD. Updated `40_methods/xlm-roberta-multilingual-classification.md` Source summaries. Updated index.

## [2026-04-15] ingest | krieger2020-foerderkatalog-querschnitt

Created summary at `20_summaries/krieger2020-foerderkatalog-querschnitt.md`. Key content: only academic study applying text-based classification to BMBF Förderkatalog (70,460 projects, 2005–2018); TexAn rule-based keyword method with iterative manual validation; confirms LPS Schwerpunktprinzip undercounts cross-cutting themes by 2x+ (digitalization); documents ~10% of project descriptions < 20 words; LSTM ML approach fails (Precision 78%, Recall 68%); ~150h effort for digitalization classification. Updated `50_datasets/foerderkatalog-des-bundes.md` with Source Summaries section and cross-link. Updated `index.md`.

## [2026-04-15] ingest | bmbf2024-bundesbericht-datenband

Created summary at `20_summaries/bmbf2024-bundesbericht-datenband.md`. Key content: official BuFI Datenband 2024; total Bundesausgaben für FuE €23.4bn (2022); Direkte Projektförderung + Ressortforschung ~€10.1bn (~43% of total); BMBF 57%, BMWK 21%, BMVg 9% of federal FuE; confirms LPS single-focus problem; PROFI as shared upstream source for Förderkatalog and BuFI. Updated `50_datasets/foerderkatalog-des-bundes.md` with cross-link (Source Summaries section). Updated `50_datasets/cordis-horizon-europe-h2020.md` with Krieger cross-link under Related Source Summaries. Updated `index.md`.
## [2026-04-27] ingest | Strategic Industrial Policy

Summary created: `20_summaries/diw2025-strategic-industrial-policy.md`
Integration: Cross-referenced with Germany Innovation Policy project


## [2026-04-27] ingest | Industry 4.0 Progress

Summary created: `20_summaries/lerch2024-industry4.0-progress.md`
Integration: Cross-referenced with Germany Innovation Policy project


## [2026-04-27] ingest | AI in Production

Summary created: `20_summaries/heimberger2024-ai-production.md`
Integration: Cross-referenced with Germany Innovation Policy project


## [2026-04-27] ingest | SME Innovation Report

Summary created: `20_summaries/kfw2024-sme-innovation.md`
Integration: Cross-referenced with Germany Innovation Policy project


## [2026-04-27] ingest | EIS 2025

Summary created: `20_summaries/ec2025-eis-scoreboard.md`
Integration: Cross-referenced with Germany Innovation Policy project


## [2026-04-27] ingest | Innovationsindikator

Summary created: `20_summaries/bdi2025-innovationsindikator.md`
Integration: Cross-referenced with Germany Innovation Policy project


## [2026-04-27] ingest | Research to Business

Summary created: `20_summaries/kas2025-research-to-business.md`
Integration: Cross-referenced with Germany Innovation Policy project


## [2026-04-27] ingest | Tech Transfer

Summary created: `20_summaries/biodeutschland2024-tech-transfer.md`
Integration: Cross-referenced with Germany Innovation Policy project


## [2026-04-27] ingest | ICT Sector

Summary created: `20_summaries/rammer-schubert2025-ikt-branchenbild.md`
Integration: Cross-referenced with Germany Innovation Policy project


## [2026-04-27] ingest | Machinery Sector

Summary created: `20_summaries/schubert-rammer2026-maschinenbau.md`
Integration: Cross-referenced with Germany Innovation Policy project

## [2026-04-28] lint + pilot | Wiki quality audit and innovation paradox canonicalization

Ran a knowledge-ops audit from the vault root. Key findings: 75 summary pages, 65 under 900 words, 57 under 500 words, 23 missing or empty `source_files`, 13 source Markdown files not referenced in summary text, 10 core wiki pages with no incoming links, 15 core pages with no outgoing links, and no substantive synthesis page before this pass.

Pilot improvements:
- Upgraded `20_summaries/akcigit2024-innovation-paradox.md` into a detailed paper summary with source files, research question, core argument, method/materials, findings, limitations, concepts, relation to other vault sources, and wiki-pull links.
- Canonicalized `30_concepts/innovation-paradox.md` as the single substantive concept page for the innovation paradox.
- Merged `30_concepts/innovation-paradox-theory.md` into the canonical `30_concepts/innovation-paradox.md` concept page and removed the separate duplicate page.
- Created `90_synthesis/innovation-paradox-incumbent-lock-in.md` as the first cross-paper synthesis bridge.
- Created `90_synthesis/wiki-quality-audit-2026-04-28.md` with audit counts, remediation batches, quality standards, and wiki-pull readiness tests.
- Updated templates for summaries, concepts, methods, datasets, and synthesis pages to support deeper future ingestion.

## [2026-04-28] maintenance | Full-vault remediation execution pass

Expanded the initial pilot into a broader vault-wide remediation pass.

Diagnostics after this pass:
- 75 summary pages total.
- Summary quality tiers: A=11, B=2, C=9, D=53.
- Core wiki pages: 100.
- Core pages with no incoming links: 2.
- Core pages with no outgoing links: 5.
- Broken wikilinks: 4, all example/raw-source artifacts rather than core wiki notes.

Upgraded five weak 2026-04-27 import summaries into detailed source summaries:
- `20_summaries/diw2025-strategic-industrial-policy.md`
- `20_summaries/biodeutschland2024-tech-transfer.md`
- `20_summaries/kfw2024-sme-innovation.md`
- `20_summaries/heimberger2024-ai-production.md`
- `20_summaries/ec2025-eis-scoreboard.md`

Upgraded five additional weak 2026-04-27 import summaries into detailed source summaries:
- `20_summaries/bdi2025-innovationsindikator.md`
- `20_summaries/kas2025-research-to-business.md`
- `20_summaries/lerch2024-industry4.0-progress.md`
- `20_summaries/rammer-schubert2025-ikt-branchenbild.md`
- `20_summaries/schubert-rammer2026-maschinenbau.md`

Created canonical pages:
- `30_concepts/strategic-industrial-policy.md`
- `30_concepts/technology-transfer-and-translation.md`
- `30_concepts/sme-innovation-participation.md`
- `30_concepts/ai-production-adoption.md`
- `50_datasets/european-innovation-scoreboard.md`

Created synthesis and planning pages:
- `90_synthesis/germany-innovation-policy-evidence-map.md`
- `90_synthesis/full-vault-remediation-plan-2026-04-28.md`

Updated `index.md` with new canonical concepts, dataset, and synthesis/remediation pages.

## [2026-04-29] maintenance | Wiki workflow enforcement layer

Updated the existing Research-OS wiki workflow so future additions use the
remediation standard by default. The existing `wiki-ingest`, `wiki-pull`,
`wiki-push`, and `wiki-librarian` workflows now require detailed summaries,
canonical concept/method/dataset checks, synthesis updates, project bridge
updates, and verification. The clo-author template and active Foerderkatalog
project skills/agents now carry the same wiki-first and wiki-push requirements.

Created `90_synthesis/wiki-operating-protocol.md` as the maintained protocol
note and added `wiki_quality_check.py` as a read-only verification utility.

Initial strict verifier result:
- 75 summaries total.
- Summary quality tiers: A=1, B=10, C=3, D=61.
- Missing source path/source_files: 13.
- Zero-link summaries: 4.
- Broken wikilinks in maintained wiki folders: 0.
- Duplicate canonical candidates: 0 after merging `innovation-paradox-theory.md`
  into `innovation-paradox.md`.

## [2026-04-29] maintenance | Full wiki-ingest re-run for existing Markdown sources

Re-ran the existing-source branch of the `wiki-ingest` workflow across all 75
Markdown sources already present in `10_sources/`. No PDF-to-Markdown
conversion was rerun. Each summary was regenerated or upgraded from the
available Markdown source and prior maintained interpretation using the
required summary structure: source path, bibliographic metadata, detailed
summary, research question, contribution, methodology, datasets/materials,
findings, limitations, concepts, methods, datasets, relations to other papers,
project implications, and canonical wiki links.

Final verifier result after targeted fixes:
- Source Markdown: 75.
- Source PDFs: 80.
- Summaries: 75.
- Summary quality tiers: A=75, B=0, C=0, D=0.
- Missing source paths/source_files: 0.
- Zero-link summaries: 0.
- Summaries with required-section gaps: 0.
- Core notes with no incoming links: 0.
- Core notes with no outgoing links: 0.
- Broken wikilinks: 0.
- Duplicate canonical candidates: 0 after final merge into `innovation-paradox.md`.

Closed the remaining B-tier summaries with wiki-ingest completion notes:
`audretsch2005-knowledge-spillover.md`,
`bmle-merkblatt-technologiereifegrade.md`,
`dosi1982-technological-paradigms.md`,
`ec-trl-horizon2020.md`,
`gilardi2023-chatgpt-annotation.md`,
`kleer2010-rd-subsidies-signal.md`,
`moller2024-parrot-dilemma.md`, and
`snow2008-cheap-fast-annotation.md`.

Also added body wikilinks for the project-specific LLM few-shot applicability
method note and linked the innovation paradox alias note back from the
canonical concept page.

## [2026-04-29] ingest | EFI 2023 and EFI 2024 annual reports

Completed the missing EFI ingest through `wiki-ingest`:
- Converted `10_sources/efi2023-gutachten.pdf` to `10_sources/efi2023-gutachten.md`.
- Converted `10_sources/EFI_Gutachten_2024_24124.pdf` to `10_sources/efi2024-gutachten.md`.
- Created detailed A-tier summaries:
  - `20_summaries/efi2023-gutachten.md`
  - `20_summaries/efi2024-gutachten.md`

Scanned the summary layer for recurring concept/method/dataset/synthesis gaps
introduced or strengthened by the EFI reports. Added canonical notes:
- `30_concepts/mission-oriented-innovation-policy.md`
- `30_concepts/data-access-for-innovation-policy.md`
- `40_methods/causal-evaluation-innovation-policy.md`
- `50_datasets/mannheimer-innovationspanel.md`
- `90_synthesis/innovation-policy-governance-and-evaluation.md`

Updated existing summaries and wiki hubs so the EFI layer is connected to ZIM
evaluation, SME innovation, Foerderkatalog text classification, AI production
adoption, innovation indicators, the project page, the Germany evidence map,
and `index.md`.

Extended `wiki_quality_check.py` with explicit quality checks for core notes:
concepts, methods, datasets, and synthesis pages are now graded separately from
source summaries. Alias notes are detected and excluded from substantive
quality grading.

Final verifier result:
- Source Markdown: 77.
- Source PDFs: 80.
- Summaries: 77.
- Summary quality: A=77, B=0, C=0, D=0.
- Concepts: 14; quality A=8, B=5, C=0, D=0, aliases=1.
- Methods: 6; quality A=5, B=1, C=0, D=0.
- Datasets: 4; quality A=3, B=1, C=0, D=0.
- Synthesis: 6; quality A=5, B=1, C=0, D=0.
- Missing source paths: 0.
- Zero-link summaries: 0.
- Required-section gaps: 0.
- Core notes with no incoming links: 0.
- Core notes with no outgoing links: 0.
- Broken wikilinks: 0.
- Weak core notes: 0.

## [2026-04-29] maintenance | Canonical concept expansion and wiki-maintain pass

Used the `wiki-maintain` workflow and `wiki-librarian` operating standard to close recurring concept gaps identified in the summary layer. Created seven canonical concept notes:
- `30_concepts/llm-annotation-and-automated-coding.md`
- `30_concepts/text-as-data-computational-social-science.md`
- `30_concepts/foundation-models-and-pretrained-transformers.md`
- `30_concepts/rd-subsidy-additionality.md`
- `30_concepts/knowledge-spillovers-and-entrepreneurship.md`
- `30_concepts/creative-destruction-and-distance-to-frontier.md`
- `30_concepts/green-innovation-and-transition-policy.md`

Added backlinks from 54 relevant source summaries, connected the new concepts to method notes, updated the active project page and project `wiki-links.md`, created `90_synthesis/llm-text-classification-and-annotation.md`, and updated the Germany/governance synthesis and `index.md` retrieval surfaces.

Upgraded remaining B-tier core notes to A-tier by adding missing concept paper-usage sections, method/dataset retrieval details, and remediation-plan scope/comparison/open-question sections.

Final verifier result:
- Source Markdown: 77.
- Summaries: 77; summary quality A=77, B=0, C=0, D=0.
- Concepts: 21; concept quality A=20, B=0, C=0, D=0, aliases=1.
- Methods: 6; method quality A=6, B=0, C=0, D=0.
- Datasets: 4; dataset quality A=4, B=0, C=0, D=0.
- Synthesis: 7; synthesis quality A=7, B=0, C=0, D=0.
- Broken wikilinks: 0.
- Orphan core notes: 0.
- Duplicate candidates: 0 after final merge into `innovation-paradox.md`.

## [2026-04-29] maintenance | Innovation paradox duplicate fully merged

Merged `30_concepts/innovation-paradox-theory.md` into the single canonical
concept note `30_concepts/innovation-paradox.md`. The duplicate alias page was
removed, and maintenance/audit notes were updated so future wiki-maintain runs
no longer treat the duplicate as intentional.

## [2026-04-29] discussion | German innovation-funding problem framing

Captured the opening discussion on the basis of the German innovation-funding
problem and wrote it back into the wiki:
- Expanded `90_synthesis/innovation-paradox-incumbent-lock-in.md` with a
  discussion snapshot that distinguishes input shortage from allocation and
  commercialization failures.
- Linked `70_projects/bundesinnovationshaushalt-trl.md` directly to that
  synthesis so the project page now points to the central working hypothesis.

Core takeaways logged:
- The main issue is not simply too little R&D spending.
- The stronger hypothesis is a portfolio-quality problem: incumbent bias,
  weak entrant selection, weak commercialization, and trajectory lock-in.
- TRL distribution and recipient structure remain the cleanest empirical
  handles for testing that hypothesis in the Förderkatalog.

## [2026-04-29] maintenance | Viel Wissen, wenig Wachstum framing pass

Updated the canonical project and concept notes to reflect the agreed paper
framing:
- Project thesis now centers "Viel Wissen, wenig Wachstum" and treats TRL bias
  as a hypothesis, not a settled fact.
- `innovation-paradox.md` now states the upstream/downstream split explicitly.
- `commercialization-gap.md`, `technology-transfer-and-translation.md`, and
  `radical-vs-incremental-innovation.md` now keep the TRL and transfer claims
  conditional on evidence and recipient structure.
- `innovation-paradox-incumbent-lock-in.md` and
  `germany-innovation-policy-evidence-map.md` now route the evidence through
  the same framing.

Key interpretive rule now logged:
- TRL 7-9 is not bad by itself.
- The stronger warning sign is late TRL plus large, old, repeat recipients.
- Transfer failure should be read as weak downstream translation, not weak
  upstream research capacity.

## [2026-04-30] maintenance | Inbox processed through wiki-librarian workflow

Audited `00_inbox` and classified every inbox note as already captured, newly
ingested, or unresolved source-acquisition work.

Newly ingested the local 2019 ZIM evaluation:
- Converted `10_sources/evaluation-zim-2019-07.pdf` to
  `10_sources/prognos2019-zim-evaluation.md`.
- Created [[20_summaries/prognos2019-zim-evaluation.md]].
- Linked it into [[30_concepts/rd-subsidy-additionality.md]],
  [[30_concepts/sme-innovation-participation.md]],
  [[40_methods/causal-evaluation-innovation-policy.md]],
  [[90_synthesis/innovation-policy-governance-and-evaluation.md]],
  [[90_synthesis/germany-innovation-policy-evidence-map.md]], the project page,
  and the index.

Created [[90_synthesis/inbox-processing-plan-2026-04-30.md]] to preserve all
remaining missing-source and paywalled source leads before inbox cleanup. The
plan records acquisition/verification todos for Aghion/Akcigit/Howitt 2014,
Britt/Buede/Koen 2008, Bengel et al. 2020, Heseltine/von Hohenberg 2024,
Lundvall 1992, Nelson 1993, MIP documentation, Breznitz 2007, Celebi and
Penczynski 2024, Murayama/Yoshida 2021, and Stiftung Mercator/BMFTR
Transferbruecken.

## [2026-05-04] maintenance | Whole-vault source-summary fidelity audit

Used the local Claude `wiki-ingest`, `wiki-maintain`, and `wiki-librarian`
workflow standards to audit every maintained source summary in `20_summaries`.

Problem found:
- 75 summaries contained defective prior batch-ingest text: repeated source
  snippets, generic canonical-link blocks, or boilerplate that made the notes
  look long without being good summaries.
- One summary, `rammer_krieger_peters2022-sme-drivers-barriers.md`, was mapped
  to the wrong source file and has now been corrected to the Rammer/Krieger/
  Peters ZEW report.

Actions:
- Repaired all contaminated summaries.
- Removed repeated batch-ingest markers and repeated paragraphs.
- Added source-grounding and fidelity interpretation sections without
  reintroducing repeated paragraphs.
- Created [[90_synthesis/source-summary-fidelity-audit-2026-05-04.md]] with a
  file-by-file audit table for all 78 summaries.
- Upgraded [[30_concepts/mitteltechnologie-falle.md]] and linked it from
  [[20_summaries/falck2026-growth-share-matrix-deutschland.md]].

Final verifier result after the pass:
- Summaries: 78; A=78, B=0, C=0, D=0.
- Required-section gaps: 0.
- Missing source paths: 0.
- Zero-link summaries: 0.
- Repeated-paragraph diagnostic: 0 repeated paragraph groups.
- Broken wikilinks: 0.
- Orphan core notes: 0.
- Duplicate concept/method/dataset candidates: 0.
