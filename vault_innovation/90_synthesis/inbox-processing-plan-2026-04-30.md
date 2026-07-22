---
title: "Inbox Processing Plan 2026-04-30"
note_type: synthesis
summary: "Wiki-librarian audit of the 00_inbox folder: which inbox notes were already captured in the maintained wiki, which source leads still require acquisition or verification, and how future wiki-maintain runs should process the remaining literature leads without reintroducing duplicate stubs."
projects:
  - "[[70_projects/bundesinnovationshaushalt-trl.md]]"
included_notes:
  - "[[20_summaries/prognos2019-zim-evaluation.md]]"
  - "[[20_summaries/struss2016-zim-wirkungsanalyse.md]]"
  - "[[20_summaries/bdi2025-innovationsindikator.md]]"
  - "[[20_summaries/biodeutschland2024-tech-transfer.md]]"
  - "[[20_summaries/diw2025-strategic-industrial-policy.md]]"
  - "[[20_summaries/ec2025-eis-scoreboard.md]]"
  - "[[20_summaries/efi2024-gutachten.md]]"
  - "[[20_summaries/heimberger2024-ai-production.md]]"
  - "[[20_summaries/kas2025-research-to-business.md]]"
  - "[[20_summaries/kfw2024-sme-innovation.md]]"
  - "[[20_summaries/lerch2024-industry4.0-progress.md]]"
  - "[[20_summaries/naud_nagler2022-ossified-economy.md]]"
  - "[[20_summaries/oecd2022-innovation-policy-germany.md]]"
  - "[[20_summaries/oecd2026-financing-smes-germany.md]]"
  - "[[20_summaries/rammer-schubert2025-ikt-branchenbild.md]]"
  - "[[20_summaries/schubert-rammer2026-maschinenbau.md]]"
related_concepts:
  - "[[30_concepts/innovation-paradox.md]]"
  - "[[30_concepts/creative-destruction-and-distance-to-frontier.md]]"
  - "[[30_concepts/innovation-systems-comparison.md]]"
  - "[[30_concepts/rd-subsidy-additionality.md]]"
  - "[[30_concepts/sme-innovation-participation.md]]"
  - "[[30_concepts/technology-transfer-and-translation.md]]"
  - "[[30_concepts/llm-annotation-and-automated-coding.md]]"
related_methods:
  - "[[40_methods/trl-project-level-reporting.md]]"
  - "[[40_methods/causal-evaluation-innovation-policy.md]]"
related_synthesis:
  - "[[90_synthesis/germany-innovation-policy-evidence-map.md]]"
  - "[[90_synthesis/innovation-policy-governance-and-evaluation.md]]"
  - "[[90_synthesis/llm-text-classification-and-annotation.md]]"
tags:
  - synthesis
  - maintenance
  - inbox
  - wiki-librarian
updated: "2026-04-30"
---

# Inbox Processing Plan 2026-04-30

## Scope

This note preserves the durable research value from the former `00_inbox` queue after a wiki-librarian audit. The cleanup rule was strict: an inbox note could be removed only if its information was already captured in a maintained source summary, canonical concept/method/dataset/synthesis note, or this processing plan. Inbox notes were not treated as source summaries; they were citation stubs, acquisition leads, or short reminders. The maintained wiki remains the source of truth.

## Main synthesis

Most inbox files were stale remnants of the 2026-04-27 Germany innovation-policy ingest batch. Their sources now have full source markdown and A-tier summaries connected to concepts, methods, datasets, project notes, and synthesis pages. Keeping those inbox stubs would make `wiki-pull` noisier because project queries could retrieve obsolete "PDF needed" reminders even where the real source had already been processed.

One inbox item was materially incomplete but had a local source available: `prognos2019-zim-evaluation.md`. The local PDF `10_sources/evaluation-zim-2019-07.pdf` was converted into source markdown and processed as [[20_summaries/prognos2019-zim-evaluation.md]]. That summary now connects the ZIM 2015 evaluation to [[30_concepts/rd-subsidy-additionality.md]], [[30_concepts/sme-innovation-participation.md]], [[40_methods/causal-evaluation-innovation-policy.md]], [[90_synthesis/innovation-policy-governance-and-evaluation.md]], and [[90_synthesis/germany-innovation-policy-evidence-map.md]].

Several inbox files still represented legitimate but unprocessed research leads. They were not turned into summaries because the underlying source text was unavailable, paywalled, or still needs citation verification. Their metadata and action items are preserved below so the inbox folder can be cleaned without losing work.

## Captured and safe to remove from inbox

The following inbox notes were already captured in maintained wiki notes and did not need to remain in `00_inbox`:

| Inbox file | Captured in maintained wiki |
| --- | --- |
| `bdi2025-innovationsindikator.md` | [[20_summaries/bdi2025-innovationsindikator.md]] |
| `biodeutschland2024-tech-transfer.md` | [[20_summaries/biodeutschland2024-tech-transfer.md]] |
| `diw2025-strategic-industrial-policy.md` | [[20_summaries/diw2025-strategic-industrial-policy.md]] |
| `ec2025-eis-scoreboard.md` | [[20_summaries/ec2025-eis-scoreboard.md]] |
| `efi2024-gutachten.md` | [[20_summaries/efi2024-gutachten.md]] |
| `heimberger2024-ai-production.md` | [[20_summaries/heimberger2024-ai-production.md]] |
| `kas2025-research-to-business.md` | [[20_summaries/kas2025-research-to-business.md]] |
| `kfw2024-sme-innovation.md` | [[20_summaries/kfw2024-sme-innovation.md]] |
| `lerch2024-industry4.0-progress.md` | [[20_summaries/lerch2024-industry4.0-progress.md]] |
| `naud_nagler2022-ossified-economy.md` | [[20_summaries/naud_nagler2022-ossified-economy.md]] |
| `oecd2022-innovation-policy-germany.md` | [[20_summaries/oecd2022-innovation-policy-germany.md]] |
| `oecd2026-financing-smes-germany.md` | [[20_summaries/oecd2026-financing-smes-germany.md]] |
| `rammer-schubert2025-ikt-branchenbild.md` | [[20_summaries/rammer-schubert2025-ikt-branchenbild.md]] |
| `schubert-rammer2026-maschinenbau.md` | [[20_summaries/schubert-rammer2026-maschinenbau.md]] |
| `rkw2016-zim-wirtschaftliche-wirkung.md` | [[20_summaries/struss2016-zim-wirkungsanalyse.md]] |
| `prognos2019-zim-evaluation.md` | [[20_summaries/prognos2019-zim-evaluation.md]] |
| `GERMANY_INNOVATION_POLICY_2024-2026_BIBLIOGRAPHY.md` | Superseded by the processed summaries above plus the acquisition queue in this note. |

## Source acquisition and verification todos

These items should not be silently forgotten. They should be processed only after source text is obtained and verified.

| Priority | Source lead | Why it matters | Next action |
| --- | --- | --- | --- |
| 1 | Aghion, Akcigit, and Howitt (2014), "What Do We Learn From Schumpeterian Growth Theory?", DOI `10.1016/B978-0-444-53540-5.00001-X` | Theory bridge for [[30_concepts/creative-destruction-and-distance-to-frontier.md]] and [[30_concepts/innovation-paradox.md]]. | Obtain the Elsevier handbook chapter through library access; then run wiki-ingest and connect to the innovation-paradox synthesis. |
| 2 | Bengel, Luedeke-Freund, and Schaltegger (2020), "Identifying Gaps in Automating the Assessment of Technology Readiness Levels", DOI `10.1017/dsd.2020.101` | Direct support for coarse TRL bins and automated TRL-assessment limitations in [[40_methods/trl-project-level-reporting.md]]. | Obtain the Cambridge/Design Society paper; verify the stated coarser-bin finding before creating a summary. |
| 2 | Britt, Buede, and Koen (2008), "Document Classification Techniques for Automated Technology Readiness Level Analysis", DOI `10.1002/asi.20770` | Foundational automated TRL document-classification paper relevant to [[40_methods/trl-project-level-reporting.md]] and [[40_methods/xlm-roberta-multilingual-classification.md]]. | Obtain the Wiley article through institutional access; create a source summary and method cross-links only after reading the paper. |
| 2 | Heseltine and Clemm von Hohenberg (2024), "Large Language Models as a Substitute for Human Experts in Annotating Political Text", DOI `10.1177/20531680241236239` | Important validation evidence for [[30_concepts/llm-annotation-and-automated-coding.md]] and [[90_synthesis/llm-text-classification-and-annotation.md]], especially because it involves German political text. | Download the open-access article from Research and Politics; ingest and compare against the current LLM annotation synthesis. |
| 2 | Lundvall (ed.) (1992), "National Systems of Innovation" | Foundational NIS theory for [[30_concepts/innovation-systems-comparison.md]]. | Obtain library access if the project needs deeper NIS theory beyond current summaries; do not summarize from secondary memory. |
| 2 | Nelson (ed.) (1993), "National Innovation Systems: A Comparative Analysis" | Foundational comparative NIS work for country-comparison framing. | Obtain the book or relevant chapter via library access; ingest only the sections used by the project. |
| 3 | Aschhoff and Rammer/Schubert (2023), "Dokumentation zur Innovationserhebung 2023" | Documentation for [[50_datasets/mannheimer-innovationspanel.md]] and MIP-based evaluation evidence. | Locate the ZEW documentation PDF; update the dataset note if it contains survey design, sample, or variable metadata not already captured. |
| 3 | Breznitz (2007), "Innovation and the State" | International innovation-state comparison for Israel, Taiwan, and Ireland. | Obtain the Yale University Press book only if the comparison layer needs cases beyond current OECD/EIS evidence. |
| 3 | Celebi and Penczynski (2024), "Using Large Language Models for Text Classification in Experimental Economics" | Potential additional LLM classification validation source. | Verify the working-paper PDF and relevance before adding; avoid duplicating existing LLM annotation notes unless it adds new validation findings. |
| 3 | Murayama and Yoshida (2021), "Quantifying the Proportion of Basic and Applied Research" | Possible science-of-science/R&D text-classification source, but the citation is unverified. | Verify author, title, venue, and availability before any wiki-ingest action. |
| 3 | Stiftung Mercator/BMFTR (2023), "Transferbruecken" | Possible German technology-transfer and spin-off policy source relevant to [[30_concepts/technology-transfer-and-translation.md]]. | Locate the real PDF or report page; ingest if it adds evidence beyond BIO Deutschland and KAS. |

## Comparison and retrieval implications

The cleanup improves retrieval because `wiki-pull` should no longer retrieve obsolete inbox stubs for sources that already have summaries. A query such as "ZIM additionality SME breadth depth" should retrieve [[20_summaries/prognos2019-zim-evaluation.md]], [[30_concepts/rd-subsidy-additionality.md]], [[30_concepts/sme-innovation-participation.md]], and [[40_methods/causal-evaluation-innovation-policy.md]], not an inbox reminder. A query such as "automated TRL classification foundational paper" should retrieve [[40_methods/trl-project-level-reporting.md]] plus this plan until Britt 2008 and Bengel 2020 are acquired and summarized. A query such as "German political text LLM annotation validation" should retrieve [[90_synthesis/llm-text-classification-and-annotation.md]], [[30_concepts/llm-annotation-and-automated-coding.md]], and this plan until Heseltine 2024 is ingested.

## Open questions

- Which paywalled books and articles are worth library acquisition for the active paper, rather than being background theory?
- Should Britt 2008 and Bengel 2020 become full summaries or be summarized only inside the TRL method notes after source verification?
- Does the 2023 MIP documentation contain enough reusable dataset detail to justify a dedicated source summary, or should it only update [[50_datasets/mannheimer-innovationspanel.md]]?
- Should the unresolved acquisition queue live in a dedicated project task file if the active project needs a formal literature-acquisition checklist?

## Maintenance rule

Future wiki-librarian runs should keep `00_inbox` transient. If an inbox note contains only a source lead, either ingest the source into the normal wiki structure or move the lead into a maintained acquisition/processing note like this one. Do not let stale inbox stubs become competing retrieval targets.
