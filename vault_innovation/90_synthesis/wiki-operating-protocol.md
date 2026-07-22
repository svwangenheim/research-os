---
title: "Wiki Operating Protocol"
note_type: synthesis
summary: "Mandatory operating protocol for adding, pulling, pushing, and verifying knowledge in the Research-OS LLM wiki."
projects:
  - "[[70_projects/bundesinnovationshaushalt-trl.md]]"
tags:
  - synthesis
  - wiki-maintenance
  - operating-protocol
updated: "2026-04-29"
---

# Wiki Operating Protocol

## Purpose

This protocol makes the remediation standard operational. It applies to Claude,
Codex, clo-author agents, and any manual wiki maintenance.

The goal is a retrieval-ready knowledge graph, not a larger pile of weak notes.
Every new addition should make source summaries deeper, canonical notes cleaner,
synthesis stronger, and project retrieval more reliable.

## Pull Before Project Work

Before substantial research, data, writing, strategy, or literature work:

1. Read [[index.md]].
2. Check relevant synthesis pages in [[90_synthesis/]].
3. Check canonical concept, method, and dataset pages.
4. Check detailed source summaries.
5. Update the project `wiki-links.md` when a project should reuse these notes.

Prefer synthesis and canonical notes over isolated paper mentions.

## Ingest Standard

Every ingested source must create or update one detailed summary in
[[20_summaries/]]. The summary must include:

- source paper link/path;
- bibliographic metadata;
- detailed summary;
- research question;
- core argument or contribution;
- methodology;
- datasets/materials used;
- key findings;
- limitations;
- important concepts discussed;
- methods discussed;
- datasets discussed;
- relation to other papers in the vault;
- implications for LLM research or the project domain;
- links to canonical concept, method, dataset, synthesis, and project notes.

If the source is unavailable or unclear, mark the affected section as
`needs source verification`. Do not fabricate findings.

## Canonical Notes

Before creating concept, method, or dataset notes:

1. Search the relevant folder.
2. Search likely aliases, singular/plural forms, abbreviations, and translated
   terms.
3. Update the existing canonical note when the idea already exists.
4. Create a new canonical note only when the object is genuinely distinct.
5. Convert duplicate pages into aliases or merge candidates; do not delete them
   without explicit approval.

There must be exactly one substantive note per concept, method, or dataset.

## Synthesis Layer

Update or create synthesis pages when a source:

- changes the interpretation of several papers;
- introduces a tension or disagreement;
- strengthens a recurring mechanism;
- connects a project result to the broader literature;
- clarifies a method/dataset choice across papers.

Synthesis pages should compare papers, name agreements and disagreements, link
to canonical notes, and make future wiki-pull retrieval easier.

## Project Bridge

Every active project with `wiki-links.md` should track:

- relevant summaries;
- concepts used;
- methods documented;
- datasets used;
- synthesis pages;
- open questions to push back to the wiki;
- durable project findings that should update canonical notes.

## Verification Gate

After every wiki-ingest or wiki-push, run:

```bash
python wiki_quality_check.py --vault <path/to/your/vault>
```

If the script is unavailable, manually report:

- summary counts and quality tiers;
- summaries missing `source_files` or source path;
- missing required summary sections;
- zero-link or weakly linked summaries;
- duplicate concept/method/dataset candidates;
- canonical pages missing backlinks;
- orphan or weakly linked core notes;
- concept, method, dataset, and synthesis note quality tiers;
- broken wikilinks;
- whether `index.md`, `log.md`, and project `wiki-links.md` were updated.

Do not call an ingest or push complete if it creates shallow, unsupported, or
disconnected notes. Report unresolved issues explicitly.

## Full-Vault Remediation

The existing backlog remains tracked in
[[90_synthesis/full-vault-remediation-plan-2026-04-28.md]]. The whole wiki
should be upgraded in batches: first low-quality summaries, then canonical
concept/method/dataset cleanup, then synthesis and project bridge readiness.
