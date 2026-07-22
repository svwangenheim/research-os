---
title: "Full Vault Remediation Plan - 2026-04-28"
note_type: synthesis
summary: "Vault-wide diagnostic and execution plan for upgrading the LLM research wiki to detailed summaries, canonical concepts/methods/datasets, synthesis pages, and wiki-pull-ready links."
projects:
  - "[[70_projects/bundesinnovationshaushalt-trl.md]]"
included_notes:
  - "[[90_synthesis/wiki-quality-audit-2026-04-28.md]]"
  - "[[90_synthesis/germany-innovation-policy-evidence-map.md]]"
  - "[[90_synthesis/innovation-paradox-incumbent-lock-in.md]]"
tags:
  - synthesis
  - wiki-maintenance
  - remediation-plan
updated: "2026-04-28"
---

# Full Vault Remediation Plan - 2026-04-28

## Scope

This synthesis is a maintenance and remediation plan, not a substantive literature synthesis. It covers the vault-wide workflow for source summaries, canonical concepts, methods, datasets, synthesis pages, project pages, indexes, backlinks, duplicate handling, and verification. It should be retrieved when a future agent needs to understand how the wiki was upgraded or how to keep it from regressing.

## Purpose

This note is the full execution plan for turning the research vault into a detailed, canonical, synthesis-oriented wiki that can support `wiki-pull` from future projects.

The target is not a larger pile of notes. The target is a retrieval-ready knowledge graph:

- every important source has a detailed summary;
- every important concept, method, and dataset has one canonical page;
- duplicate pages become aliases or merge candidates;
- synthesis pages connect findings across papers;
- project pages point to the correct summaries, concepts, methods, datasets, and syntheses.

## Papers compared

This note compares maintenance states rather than academic papers. The relevant sources are [[90_synthesis/wiki-quality-audit-2026-04-28.md]], [[90_synthesis/wiki-operating-protocol.md]], [[90_synthesis/germany-innovation-policy-evidence-map.md]], [[90_synthesis/innovation-paradox-incumbent-lock-in.md]], [[90_synthesis/innovation-policy-governance-and-evaluation.md]], and [[90_synthesis/llm-text-classification-and-annotation.md]]. Together they define what was weak, what became canonical, and which synthesis hubs now support project-level retrieval.

## Open questions and tensions

- How strict should A-tier grading be for maintenance plans compared with substantive synthesis notes?
- When a recurring idea appears in only a few papers but is theoretically central, should it become a concept note immediately or remain a watch item?
- How much summary boilerplate should be tolerated when it improves structural consistency but risks overlinking unrelated notes?
- How often should the entire wiki be rechecked after new source ingest?
- Should future verifier versions distinguish semantic overlinking from broken or missing links?

## Enforcement update - 2026-04-29

The remediation plan is now tied to an operating workflow rather than a one-off
cleanup. Future additions must follow [[90_synthesis/wiki-operating-protocol.md]]:

- existing `wiki-ingest`, `wiki-pull`, `wiki-push`, and `wiki-librarian`
  workflows enforce detailed summaries, canonical notes, synthesis updates, and
  verification;
- the clo-author template and the active Foerderkatalog project require wiki
  retrieval before substantial research work and wiki-push after durable
  findings;
- `wiki_quality_check.py` provides the read-only verification layer for summary
  quality, source paths, duplicate canonical candidates, weak links, orphan
  notes, and broken wikilinks.

## Completion update - 2026-04-29

The existing-source branch of the true `wiki-ingest` workflow has now been run
across all 75 Markdown sources already present in `10_sources/`. Existing
Markdown conversions were reused; no new PDF-to-Markdown conversion was
performed. The pass upgraded every source summary into the required detailed
structure, linked summaries to canonical concept/method/dataset/synthesis and
project notes, and then closed the remaining verifier failures with targeted
wiki-ingest completion notes and backlink fixes.

Final verifier result:

| Area | Current state |
| --- | --- |
| Source Markdown files in `10_sources/` | 75 |
| Source PDFs in `10_sources/` | 80 |
| Summary pages in `20_summaries/` | 75, excluding README |
| Summary quality tiers | A: 75, B: 0, C: 0, D: 0 |
| Remaining summaries below target structure | 0 |
| Missing source paths/source_files | 0 |
| Zero-link summaries | 0 |
| Required-section gaps | 0 |
| Core pages with no incoming links | 0 |
| Core pages with no outgoing links | 0 |
| Broken wikilinks | 0 |
| Duplicate canonical candidates | 0 after final merge into `innovation-paradox.md` |

## Current diagnostic snapshot

Measured after the pilot, canonicalization pass, and two summary-upgrade batches on 2026-04-28:

| Area | Current state |
| --- | --- |
| Source Markdown files in `10_sources/` | 75 |
| Source PDFs in `10_sources/` | 80 |
| Summary pages in `20_summaries/` | 75, excluding README |
| Summary quality tiers | A: 1, B: 10, C: 3, D: 61 under the stricter 2026-04-29 verifier |
| Remaining summaries below target structure | 74 are below strict A-tier |
| Worst remaining summaries | `bloom2020-are-ideas-getting-harder.md`, `acemoglu2006-distance-to-frontier.md`, `horbach_rammer2024-energy-price-shocks.md`, `duso2025-strategic-industrial-policy.md`, `beck2016-radical-or-incremental.md`, `aschhoff2010-who-gets-the-money.md`, `oecd2022-innovation-policy-germany.md`, `bmf2026-five-report.md`, `bitkom2025-startup-report.md`, `oecd2026-financing-smes-germany.md` |
| Source Markdown not referenced in summary text | 13 |
| Core wiki pages | 100 |
| Core pages with no incoming links | 2 |
| Core pages with no outgoing links | 5 |
| Broken wikilinks | 4 total: 3 example links in `CLAUDE.md`, 1 raw-source artifact in `10_sources/devlin2019-bert.md` |
| Substantive synthesis/planning pages | 4 after this pass |

## Summary quality tiers

The current scoring uses:

- word count;
- required frontmatter;
- required sections;
- wikilink density;
- explicit source files.

Target A-tier summary:

- 1,200+ words where the source is substantial;
- explicit `source_files`;
- bibliographic metadata;
- all required sections;
- links to canonical concepts, methods, datasets, projects, and synthesis pages;
- no unsupported claims.

Current strict A-tier summaries:

- [[20_summaries/akcigit2024-innovation-paradox.md]]

Current B-tier summaries from the first remediation batches:

- [[20_summaries/diw2025-strategic-industrial-policy.md]]
- [[20_summaries/biodeutschland2024-tech-transfer.md]]
- [[20_summaries/kfw2024-sme-innovation.md]]
- [[20_summaries/heimberger2024-ai-production.md]]
- [[20_summaries/ec2025-eis-scoreboard.md]]
- [[20_summaries/bdi2025-innovationsindikator.md]]
- [[20_summaries/kas2025-research-to-business.md]]
- [[20_summaries/lerch2024-industry4.0-progress.md]]
- [[20_summaries/rammer-schubert2025-ikt-branchenbild.md]]
- [[20_summaries/schubert-rammer2026-maschinenbau.md]]

## Phase 1: Upgrade detailed paper/source summaries

### Acceptance criteria

Each upgraded summary must contain:

- Source paper/path.
- Bibliographic metadata.
- Detailed summary.
- Research question.
- Core argument or contribution.
- Methodology.
- Datasets/materials used.
- Key findings.
- Limitations.
- Important concepts discussed.
- Methods discussed.
- Datasets discussed.
- Relation to other vault sources.
- Implications for LLM research or the active project domain.
- Links to canonical concept, method, dataset, synthesis, and project pages.

### Batch order

#### Batch 1A: Worst 2026-04-27 imports

Already upgraded:

- [[20_summaries/diw2025-strategic-industrial-policy.md]]
- [[20_summaries/biodeutschland2024-tech-transfer.md]]
- [[20_summaries/kfw2024-sme-innovation.md]]
- [[20_summaries/heimberger2024-ai-production.md]]
- [[20_summaries/ec2025-eis-scoreboard.md]]
- [[20_summaries/bdi2025-innovationsindikator.md]]
- [[20_summaries/kas2025-research-to-business.md]]
- [[20_summaries/lerch2024-industry4.0-progress.md]]
- [[20_summaries/rammer-schubert2025-ikt-branchenbild.md]]
- [[20_summaries/schubert-rammer2026-maschinenbau.md]]

Batch 1A is now complete. Remaining urgent summaries were moved into the next core-theory and policy batches.

Next urgent:

- `bloom2020-are-ideas-getting-harder.md`
- `acemoglu2006-distance-to-frontier.md`
- `horbach_rammer2024-energy-price-shocks.md`
- `duso2025-strategic-industrial-policy.md`
- `beck2016-radical-or-incremental.md`
- `aschhoff2010-who-gets-the-money.md`

Reason: these remain structurally weak or weakly linked despite being important to the innovation-paradox, incumbent-lock-in, and policy-design argument.

#### Batch 1B: Core innovation-paradox theory

- `acemoglu2006-distance-to-frontier.md`
- `bloom2020-are-ideas-getting-harder.md`
- `beck2016-radical-or-incremental.md`
- `aschhoff2010-who-gets-the-money.md`
- `akcigit2018-heterogeneous-innovations.md`
- `aghion2019-innovation-inequality.md`

Reason: these are central to the active project and many are currently D-tier by structure even if conceptually important.

#### Batch 1C: Finance, commercialization, SME barriers

- `oecd2022-innovation-policy-germany.md`
- `oecd2026-financing-smes-germany.md`
- `bmf2026-five-report.md`
- `bitkom2025-startup-report.md`
- `rammer_krieger_peters2022-sme-drivers-barriers.md`
- `kfw2024-gruendungsmonitor.md`

Reason: these explain the commercialization and equity-gap mechanisms.

#### Batch 1D: LLM classification and annotation methods

- `alizadeh2025-opensource-llm-annotation.md`
- `gilardi2023-chatgpt-annotation.md`
- `egami2024-llm-annotation-framework.md`
- `halterman2025-codebook-llms.md`
- `ornstein2025-stochastic-parrot.md`
- `moller2024-parrot-dilemma.md`
- `pangakis2023-llm-annotation-validation.md`
- `ziems2024-llm-css-benchmark.md`

Reason: these feed the TRL classification method layer and should support future LLM-evaluation pulls.

## Phase 2: Canonical concept notes

### Rule

Exactly one substantive note per important concept. Duplicate pages should become aliases or merge candidates, not parallel concept pages.

### Completed canonicalization

- `innovation-paradox.md` is canonical.
- `innovation-paradox-theory.md` has been merged into `innovation-paradox.md` and removed as a separate page.

### New canonical concepts created in this pass

- [[30_concepts/strategic-industrial-policy.md]]
- [[30_concepts/technology-transfer-and-translation.md]]
- [[30_concepts/sme-innovation-participation.md]]
- [[30_concepts/ai-production-adoption.md]]

### Next concept candidates

Create only if at least two summaries need the page:

- state dependence in subsidy receipt;
- incumbent capture;
- technological investment trap;
- validation studies;
- scale-up gap;
- non-R&D innovation;
- coordination failure;
- absorptive capacity;
- digital production systems;
- technology diffusion.

## Phase 3: Canonical method and dataset notes

### Existing method strengths

The current method layer is strongest around TRL classification and LLM/text-classification workflows:

- [[40_methods/trl-klassifikation-pipeline.md]]
- [[40_methods/llm-few-shot-social-science.md]]
- [[40_methods/xlm-roberta-multilingual-classification.md]]
- [[40_methods/trl-project-level-reporting.md]]

### Dataset pages

Existing:

- [[50_datasets/foerderkatalog-des-bundes.md]]
- [[50_datasets/cordis-horizon-europe-h2020.md]]

Created:

- [[50_datasets/european-innovation-scoreboard.md]]

### Next dataset candidates

- Modernisierung der Produktion survey.
- KfW SME panel / KfW SME innovation data.
- Mannheim Innovation Panel.
- OECD MSTI.
- German innovation survey / ZEW indicators.
- Patent data as innovation-output measure.

## Phase 4: Synthesis and connection layer

### Completed synthesis pages

- [[90_synthesis/innovation-paradox-incumbent-lock-in.md]]
- [[90_synthesis/germany-innovation-policy-evidence-map.md]]
- [[90_synthesis/wiki-quality-audit-2026-04-28.md]]

### Required next synthesis pages

1. `llm-classification-validation-evidence-map.md`
   - Scope: LLM annotation, validation, calibration, few-shot prompting, bias, human gold standards.

2. `trl-classification-and-innovation-stage-map.md`
   - Scope: TRL concepts, CORDIS, Foerderkatalog, Horizon Europe reporting, federal project classification.

3. `germany-commercialization-and-scaleup-gap.md`
   - Scope: BIO Deutschland, OECD, BMF/FIVE, KfW, Bitkom, equity gap, transfer infrastructure.

4. `sme-innovation-and-recipient-targeting.md`
   - Scope: SME innovation participation, funding selection, state dependence, non-R&D innovation, ZIM and Foerderkatalog implications.

## Phase 5: wiki-pull readiness

### Current retrieval hubs

- Innovation paradox queries should retrieve [[30_concepts/innovation-paradox.md]] and [[90_synthesis/innovation-paradox-incumbent-lock-in.md]].
- Germany innovation-policy queries should retrieve [[90_synthesis/germany-innovation-policy-evidence-map.md]].
- Project-specific TRL queries should retrieve [[70_projects/bundesinnovationshaushalt-trl.md]], [[40_methods/trl-klassifikation-pipeline.md]], and [[50_datasets/foerderkatalog-des-bundes.md]].

### Link standards

Every upgraded summary should link to:

- one project page;
- at least one concept page;
- method pages where methods are reusable;
- dataset pages where datasets are reusable;
- one synthesis page where a cluster exists.

Every concept/method/dataset page should link back to:

- all relevant summaries;
- relevant synthesis pages;
- the active project if applicable.

## Verification protocol after each batch

Run checks for:

- number of A/B/C/D summaries;
- summaries still missing `source_files`;
- summaries with zero outgoing wikilinks;
- core pages with no incoming links;
- broken wikilinks;
- duplicate concept/method/dataset candidates;
- new files added to `index.md`;
- `log.md` maintenance entry.

## Remaining unresolved issues

- The full vault is not yet fully upgraded. This plan identifies the remaining work explicitly.
- The weakest remaining summaries are now in the older core-theory and policy batches, plus several short 2026-04-27 imports.
- Many older summaries are conceptually useful but structurally below the new standard.
- Source/PDF mapping needs a more robust script because PDF filenames often differ from Markdown/summary filenames.
- Inbox notes are not yet triaged; they should be handled separately from core wiki quality.
