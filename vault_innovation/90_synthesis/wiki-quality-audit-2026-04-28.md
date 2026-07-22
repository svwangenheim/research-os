---
title: "Wiki Quality Audit - 2026-04-28"
note_type: synthesis
summary: "Maintenance audit of the LLM research vault: summary depth, source-summary coverage, canonical concept/method/dataset structure, synthesis gaps, and wiki-pull readiness."
projects:
  - "[[70_projects/bundesinnovationshaushalt-trl.md]]"
included_notes:
  - "[[index.md]]"
  - "[[CLAUDE.md]]"
related_concepts:
  - "[[30_concepts/innovation-paradox.md]]"
related_methods:
  - "[[40_methods/trl-klassifikation-pipeline.md]]"
related_datasets:
  - "[[50_datasets/foerderkatalog-des-bundes.md]]"
tags:
  - synthesis
  - wiki-maintenance
  - audit
updated: "2026-04-28"
---

# Wiki Quality Audit - 2026-04-28

## Scope

This audit covers the vault rooted at `<vault root>`, with `10_sources/` treated as immutable source material and all maintained interpretation living in the wiki folders:

- `20_summaries/`
- `30_concepts/`
- `40_methods/`
- `50_datasets/`
- `70_projects/`
- `90_synthesis/`

The goal is to make the wiki more useful for future project retrieval via `wiki-pull`: paper summaries should be detailed, concepts/methods/datasets should be canonical, and synthesis pages should connect findings across papers.

## Enforcement update - 2026-04-29

The audit now has an operating counterpart: [[90_synthesis/wiki-operating-protocol.md]].
Existing Research-OS wiki skills and clo-author skills/agents are expected to
use that protocol for all future ingest, pull, push, discovery, strategy,
writing, and checkpoint work. Verification should use `wiki_quality_check.py`
or the equivalent manual checklist.

## Full existing-source wiki-ingest rerun - 2026-04-29

The vault has now been reprocessed through the existing-source branch of the
true `wiki-ingest` workflow. Because Markdown conversions already existed in
`10_sources/`, the pass did not rerun PDF conversion. It read the existing
Markdown sources, updated the corresponding `20_summaries/` notes into the
required detailed structure, checked canonical concept/method/dataset/project
links, and reran the verifier.

Final verifier result:

| Area | Count / finding |
| --- | --- |
| Source Markdown files in `10_sources/` | 75 |
| Source PDFs in `10_sources/` | 80 |
| Summary pages in `20_summaries/` | 75, excluding README |
| Summary quality tiers under 2026-04-29 verifier | A: 75, B: 0, C: 0, D: 0 |
| Summary pages still below strict A-tier | 0 |
| Summary pages missing or empty `source_files` | 0 |
| Zero-link summaries | 0 |
| Summaries with required-section gaps | 0 |
| Core pages with no incoming links | 0 |
| Core pages with no outgoing links | 0 |
| Broken wikilinks found | 0 |
| Duplicate canonical candidates | 0 after final merge into `innovation-paradox.md` |

## EFI ingest and core-note quality gate - 2026-04-29

The two remaining EFI PDFs were ingested through the true `wiki-ingest`
conversion and summary workflow:

- [[20_summaries/efi2023-gutachten.md]]
- [[20_summaries/efi2024-gutachten.md]]

The ingest created or updated the canonical governance/evaluation layer:

- [[30_concepts/mission-oriented-innovation-policy.md]]
- [[30_concepts/data-access-for-innovation-policy.md]]
- [[40_methods/causal-evaluation-innovation-policy.md]]
- [[50_datasets/mannheimer-innovationspanel.md]]
- [[90_synthesis/innovation-policy-governance-and-evaluation.md]]

The verifier now checks quality tiers for concept, method, dataset, and
synthesis notes in addition to paper summaries. Latest result:

| Area | Count / finding |
| --- | --- |
| Source Markdown files in `10_sources/` | 77 |
| Source PDFs in `10_sources/` | 80 |
| Summary pages in `20_summaries/` | 77, excluding README |
| Summary quality tiers | A: 77, B: 0, C: 0, D: 0 |
| Concept quality tiers | A: 8, B: 5, C: 0, D: 0, aliases: 1 |
| Method quality tiers | A: 5, B: 1, C: 0, D: 0 |
| Dataset quality tiers | A: 3, B: 1, C: 0, D: 0 |
| Synthesis quality tiers | A: 5, B: 1, C: 0, D: 0 |
| Weak core notes | 0 |
| Broken wikilinks | 0 |

## Audit counts

| Area | Count / finding |
| --- | --- |
| Source Markdown files in `10_sources/` | 75 |
| Source PDFs in `10_sources/` | 80 |
| Summary pages in `20_summaries/` | 75, excluding README |
| Summary quality tiers under 2026-04-29 verifier | A: 1, B: 10, C: 3, D: 61 |
| Summary pages still below strict A-tier | 74 |
| Summary pages missing or empty `source_files` | 23 |
| Source Markdown files not referenced anywhere in summary text | 13 |
| Core wiki pages checked for link graph | 100 |
| Core pages with no incoming links | 2 |
| Core pages with no outgoing links | 5 |
| Broken wikilinks found | 0 in the maintained wiki folders under the 2026-04-29 verifier |
| Substantive concept pages | 12 canonical/substantive pages plus 1 alias |
| Method pages | 5, excluding README |
| Dataset pages | 3, excluding README |
| Synthesis/planning pages | 4 substantive or maintenance pages after this pass |

## Main diagnosis

### 1. Summary depth is the largest bottleneck

Most summary pages exist, but most are too short to serve as reusable research memory. The problem is not only missing summaries; it is shallow summaries. Many pages capture a title, a few claims, and a project relevance note, but not enough detail about research question, method, datasets, findings, limitations, concepts, and cross-paper connections.

Priority: expand summaries in batches, starting with sources that are central to active projects and sources that anchor many concepts.

### 2. Source-summary provenance is inconsistent

Several summary pages lack a usable `source_files` field, and 13 source Markdown files are not referenced anywhere in summary text. Some are likely covered under renamed summary files, but the mapping is not machine-reliable enough for `wiki-pull` or future maintenance.

Priority: every summary needs explicit `source_files`, preferably including both the extracted Markdown and the PDF when both exist.

### 3. Concepts need canonicalization

The vault already contained a concrete duplicate: `30_concepts/innovation-paradox.md` and `30_concepts/innovation-paradox-theory.md`. The pilot canonicalized `innovation-paradox.md` as the substantive concept page; the final maintenance pass merged the duplicate fully into `innovation-paradox.md` and removed the separate alias page.

Priority: repeat this process for all near-duplicate concept, method, and dataset pages before creating new pages.

### 4. Methods and datasets are under-modeled

The method layer is currently strong for the TRL/LLM classification pipeline, but many papers discuss empirical methods and datasets that are not yet canonicalized. This is acceptable for the first pilot, but future batches should extract recurring methods and datasets when they appear across multiple papers.

Priority: create method/dataset notes only when they are reusable across papers or projects. Avoid thin one-off stubs.

### 5. Synthesis layer was effectively empty

Before this pilot, `90_synthesis/` had only a README. This means the wiki mostly stored paper-level and concept-level notes without a durable cross-paper layer. The new synthesis page [[90_synthesis/innovation-paradox-incumbent-lock-in.md]] is the first retrieval bridge for the innovation-paradox cluster.

Priority: build synthesis pages around major clusters, not around individual papers.

## Quality standard for upgraded paper summaries

Every upgraded summary should include:

- Source files and source URLs.
- Bibliographic metadata.
- Detailed summary.
- Research question.
- Core argument or contribution.
- Method / identification.
- Datasets / materials.
- Main findings.
- Limitations.
- Important concepts.
- Methods discussed.
- Datasets discussed.
- Relation to other vault sources.
- Implications for the active project.
- Links to canonical concept, method, dataset, project, and synthesis pages.

## Canonicalization rules

1. Use exactly one substantive note per concept, method, or dataset.
2. Put aliases/synonyms in frontmatter on the canonical note.
3. If a duplicate page already exists, do not delete it without review. Convert it into an alias page pointing to the canonical note.
4. Update core wiki links to point to the canonical note.
5. Keep historical mentions in `log.md` unless they interfere with retrieval.

## Batch remediation plan

### Batch 1: Innovation paradox cluster

Status: pilot completed; follow-on summaries are queued in the full remediation plan.

Completed:

- Upgraded [[20_summaries/akcigit2024-innovation-paradox.md]] into a detailed summary.
- Canonicalized [[30_concepts/innovation-paradox.md]].
- Merged `30_concepts/innovation-paradox-theory.md` into `30_concepts/innovation-paradox.md` and removed the separate alias page.
- Created [[90_synthesis/innovation-paradox-incumbent-lock-in.md]].
- Updated templates for summary, concept, method, dataset, and synthesis notes.

Next candidates:

- [[20_summaries/akcigit2018-heterogeneous-innovations.md]]
- [[20_summaries/acemoglu2006-distance-to-frontier.md]]
- [[20_summaries/bloom2020-are-ideas-getting-harder.md]]
- [[20_summaries/aschhoff2010-who-gets-the-money.md]]
- [[20_summaries/naud_nagler2022-ossified-economy.md]]

### Batch 2: LLM annotation and classification methods

Goal: expand summaries and canonical method pages around LLM annotation, few-shot classification, validation, and model choice.

Likely pages:

- [[40_methods/llm-few-shot-social-science.md]]
- [[40_methods/xlm-roberta-multilingual-classification.md]]
- [[40_methods/trl-klassifikation-pipeline.md]]
- [[20_summaries/gilardi2023-chatgpt-annotation.md]]
- [[20_summaries/egami2024-llm-annotation-framework.md]]
- [[20_summaries/halterman2025-codebook-llms.md]]
- [[20_summaries/ornstein2025-stochastic-parrot.md]]
- [[20_summaries/moller2024-parrot-dilemma.md]]

### Batch 3: German innovation-policy reports from 2026-04-27

Goal: fix the thinnest new summaries and connect them to concepts/synthesis.

Completed in the first two remediation batches:

- [[20_summaries/schubert-rammer2026-maschinenbau.md]]
- [[20_summaries/kas2025-research-to-business.md]]
- [[20_summaries/rammer-schubert2025-ikt-branchenbild.md]]
- [[20_summaries/diw2025-strategic-industrial-policy.md]]
- [[20_summaries/ec2025-eis-scoreboard.md]]
- [[20_summaries/heimberger2024-ai-production.md]]
- [[20_summaries/biodeutschland2024-tech-transfer.md]]
- [[20_summaries/kfw2024-sme-innovation.md]]
- [[20_summaries/bdi2025-innovationsindikator.md]]
- [[20_summaries/lerch2024-industry4.0-progress.md]]

Next weakest pages are now listed in [[90_synthesis/full-vault-remediation-plan-2026-04-28.md]].

## wiki-pull readiness tests

These are expected retrieval paths after the pilot:

| Query | Expected retrieval |
| --- | --- |
| "innovation paradox" | [[30_concepts/innovation-paradox.md]], [[90_synthesis/innovation-paradox-incumbent-lock-in.md]], [[20_summaries/akcigit2024-innovation-paradox.md]] |
| "incumbent lock-in and R&D subsidies" | [[90_synthesis/innovation-paradox-incumbent-lock-in.md]], [[30_concepts/innovation-paradox.md]], [[20_summaries/aschhoff2010-who-gets-the-money.md]], [[20_summaries/akcigit2018-heterogeneous-innovations.md]] |
| "TRL and radical innovation in German funding" | [[70_projects/bundesinnovationshaushalt-trl.md]], [[40_methods/trl-klassifikation-pipeline.md]], [[30_concepts/radical-vs-incremental-innovation.md]], [[30_concepts/technology-readiness-levels.md]] |
| "commercialization gap Germany" | [[30_concepts/commercialization-gap.md]], [[30_concepts/equity-gap-sme-financing.md]], [[90_synthesis/innovation-paradox-incumbent-lock-in.md]] |

## Open issues

- The source-summary mapping needs a stricter machine-readable audit.
- Many summaries need expansion; the current pilot proves the target shape but does not solve the backlog.
- Method and dataset extraction should be done after summaries are expanded, because the summary pages should become the evidence base for canonical method/dataset pages.
- The inbox contains many orphan notes by design; they should be triaged separately from core wiki pages.
