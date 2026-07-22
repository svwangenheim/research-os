---
title: "Source Summary Fidelity Audit 2026-05-04"
note_type: synthesis
summary: "Whole-vault wiki-librarian audit of every source summary for source mapping, repeated batch-ingest artifacts, and source-grounding risks."
tags: [synthesis, maintenance, audit, wiki-librarian]
projects:
  - "[[70_projects/bundesinnovationshaushalt-trl.md]]"
related_synthesis:
  - "[[90_synthesis/wiki-operating-protocol.md]]"
  - "[[90_synthesis/germany-innovation-policy-evidence-map.md]]"
updated: "2026-05-04"
---

# Source Summary Fidelity Audit 2026-05-04

## Scope

This audit covers every maintained source summary in `20_summaries/` except the folder README. It was run because the previous structural quality checker could grade notes as A-tier even when a summary contained repeated source snippets or generic boilerplate. The audit therefore checked source mapping, repeated batch-ingest artifacts, stale generic links, and whether the note still needs source-verification caution.

## Main synthesis

The vault had a systemic quality issue from a prior batch re-ingest: many summaries contained the marker text `This note was re-ingested from the existing Markdown source` and repeated the same source snippets across multiple sections. Those notes could look long while being low-information. This pass repaired the contaminated summaries by rebuilding them from the clean maintained interpretation, correcting source paths where needed, removing repeated source-snippet blocks, and keeping only retrieval-relevant canonical links.

## Counts

- Summaries audited: 78
- Summaries repaired in this pass: 75
- Source mappings needing caution: 5
- Contaminated batch-ingest summaries found: 75

## File-by-file audit table

| Summary | Source file | Source exists | Title/content match | Action | Pre-audit status |
| --- | --- | --- | --- | --- | --- |
| `acemoglu2006-distance-to-frontier.md` | `10_sources/acemoglu2006-distance-frontier.md` | yes | yes | repaired | contaminated |
| `aghion1992-creative-destruction.md` | `10_sources/aghion1992-creative-destruction.md` | yes | yes | repaired | contaminated |
| `aghion2019-innovation-inequality.md` | `10_sources/aghion2019-innovation-inequality.md` | yes | yes | repaired | contaminated |
| `akcigit2018-heterogeneous-innovations.md` | `10_sources/akcigit2018-heterogeneous-innovations.md` | yes | corrected | source Markdown regenerated from correct Akcigit/Kerr PDF; summary repaired | prior source file was wrong paper |
| `akcigit2024-innovation-paradox.md` | `10_sources/akcigit2024-innovation-paradox.md` | yes | yes | repaired | contaminated |
| `alizadeh2025-opensource-llm-annotation.md` | `10_sources/alizadeh2025-opensource-llm-annotation.md` | yes | weak | repaired | contaminated |
| `aschhoff2010-who-gets-the-money.md` | `10_sources/aschhoff2010-who-gets-money.md` | yes | yes | repaired | contaminated |
| `audretsch2002-sbir-evaluation.md` | `10_sources/audretsch2002-sbir-evaluation.md` | yes | yes | repaired | contaminated |
| `audretsch2003-sbir.md` | `10_sources/audretsch2003-sbir.md` | yes | yes | repaired | contaminated |
| `audretsch2005-knowledge-spillover.md` | `10_sources/audretsch2005-knowledge-spillover.md` | yes | yes | repaired | contaminated |
| `bdi2025-innovationsindikator.md` | `10_sources/bdi2025-innovationsindikator.md` | yes | yes | repaired | contaminated |
| `beck2016-radical-or-incremental.md` | `10_sources/beck2016-radical-incremental.md` | yes | yes | repaired | contaminated |
| `biodeutschland2024-tech-transfer.md` | `10_sources/biodeutschland2024-tech-transfer.md` | yes | yes | repaired | contaminated |
| `bitkom2025-startup-report.md` | `10_sources/bitkom-studienbericht-startup-report-2025-1.md` | yes | yes | repaired | contaminated |
| `bloom2020-are-ideas-getting-harder.md` | `10_sources/bloom2020-ideas-harder.md` | yes | yes | repaired | contaminated |
| `bmbf2024-bundesbericht-datenband.md` | `10_sources/bmbf2024-bundesbericht-datenband.md` | yes | yes | repaired | contaminated |
| `bmf2026-five-report.md` | `10_sources/BMF_2026_report-five-taskforce.md` | yes | yes | repaired | contaminated |
| `bmle-merkblatt-technologiereifegrade.md` | `10_sources/bmle_merkblatt_technologiereifegrade.md` | yes | weak | repaired | contaminated |
| `brown2020-gpt3-fewshot.md` | `10_sources/brown2020-gpt3-fewshot.md` | yes | yes | repaired | contaminated |
| `chae2025-llm-instruction-tuning.md` | `10_sources/chae2025-llm-instruction-tuning.md` | yes | yes | repaired | contaminated |
| `chan2020-gbert.md` | `10_sources/chan2020-gbert.md` | yes | yes | repaired | contaminated |
| `cherif2022-rd-subsidies-imf.md` | `10_sources/cherif2022-rd-subsidies-imf.md` | yes | yes | repaired | contaminated |
| `conneau2020-xlm-roberta.md` | `10_sources/conneau2020-xlm-roberta.md` | yes | yes | repaired | contaminated |
| `czarnitzki2004-rd-subsidies-zew.md` | `10_sources/czarnitzki2004-rd-subsidies-zew.md` | yes | yes | repaired | contaminated |
| `czarnitzki2014-funding-source.md` | `10_sources/czarnitzki2014-funding-source.md` | yes | yes | repaired | contaminated |
| `devlin2019-bert.md` | `10_sources/devlin2019-bert.md` | yes | yes | repaired | contaminated |
| `diw2025-strategic-industrial-policy.md` | `10_sources/diw2025-strategic-industrial-policy.md` | yes | yes | repaired | contaminated |
| `dosi1982-technological-paradigms.md` | `10_sources/dosi1982-technological-paradigms.md` | yes | yes | repaired | contaminated |
| `draghi2024-european-competitiveness.md` | `10_sources/draghi2024-european-competitiveness.md` | yes | yes | repaired | contaminated |
| `duso2025-strategic-industrial-policy.md` | `10_sources/diw2025-strategic-industrial-policy.md` | yes | yes | repaired | contaminated |
| `ec-trl-horizon2020.md` | `10_sources/dfg_trl_horizon_2020.md` | yes | yes | repaired | contaminated |
| `ec2025-eis-scoreboard.md` | `10_sources/ec2025-eis-scoreboard.md` | yes | yes | repaired | contaminated |
| `edler2017-innovation-policy.md` | `10_sources/edler2017-innovation-policy.md` | yes | yes | repaired | contaminated |
| `efi2023-gutachten.md` | `10_sources/efi2023-gutachten.md` | yes | yes | checked | clean |
| `efi2024-gutachten.md` | `10_sources/efi2024-gutachten.md` | yes | yes | checked | clean |
| `egami2024-llm-annotation-framework.md` | `10_sources/egami2024-llm-annotation-framework.md` | yes | yes | repaired | contaminated |
| `falck2026-growth-share-matrix-deutschland.md` | `10_sources/industriedynamiken_deutschland_teil3.md` | yes | yes | repaired | contaminated |
| `gilardi2023-chatgpt-annotation.md` | `10_sources/gilardi2023-chatgpt-annotation.md` | yes | yes | repaired | contaminated |
| `grimmer2013-text-as-data.md` | `10_sources/grimmer2013-text-as-data.md` | yes | yes | repaired | contaminated |
| `halterman2025-codebook-llms.md` | `10_sources/halterman2025-codebook-llms.md` | yes | yes | repaired | contaminated |
| `heder2017-trl-history.md` | `10_sources/heder2017-trl-history.md` | yes | yes | repaired | contaminated |
| `heimberger2024-ai-production.md` | `10_sources/heimberger2024-ai-production.md` | yes | yes | repaired | contaminated |
| `horbach_rammer2022-climate-change-innovation.md` | `10_sources/Horbach_Rammer_2022_Climate changes affectedness and innovation in German firms.md` | yes | yes | repaired | contaminated |
| `horbach_rammer2024-energy-price-shocks.md` | `10_sources/Energy_Price_Shocks_and_Short-Term_Reactions_of_Fi.md` | yes | yes | repaired | contaminated |
| `howell2017-financing-innovation.md` | `10_sources/howell2017-financing-innovation.md` | yes | weak | repaired | contaminated |
| `kas2025-research-to-business.md` | `10_sources/kas2025-research-to-business.md` | yes | yes | repaired | contaminated |
| `kfw2024-gruendungsmonitor.md` | `10_sources/kfw2024-gruendungsmonitor.md` | yes | yes | repaired | contaminated |
| `kfw2024-sme-innovation.md` | `10_sources/kfw2024-sme-innovation.md` | yes | yes | repaired | contaminated |
| `kleer2010-rd-subsidies-signal.md` | `10_sources/kleer2010-rd-subsidies-signal.md` | yes | yes | repaired | contaminated |
| `krieger2020-foerderkatalog-querschnitt.md` | `10_sources/krieger2020-foerderkatalog-querschnitt.md` | yes | yes | repaired | contaminated |
| `kuzman2025-parlacap.md` | `10_sources/kuzman2025-parlacap.md` | yes | yes | repaired | contaminated |
| `laurer2023-less-annotating.md` | `10_sources/laurer2023-less-annotating.md` | yes | yes | repaired | contaminated |
| `lerch2024-industry4.0-progress.md` | `10_sources/lerch2024-industry4.0-progress.md` | yes | yes | repaired | contaminated |
| `malerba2002-sectoral-systems.md` | `10_sources/malerba2002-sectoral-systems.md` | yes | yes | repaired | contaminated |
| `moller2024-parrot-dilemma.md` | `10_sources/moller2024-parrot-dilemma.md` | yes | yes | repaired | contaminated |
| `naud_nagler2022-ossified-economy.md` | `10_sources/naud_nagler2022-ossified-economy.md` | yes | yes | repaired | contaminated |
| `oecd2022-innovation-policy-germany.md` | `10_sources/oecd2022-innovation-policy-germany.md` | yes | yes | repaired | contaminated |
| `oecd2026-financing-smes-germany.md` | `10_sources/oecd2026-financing-smes-germany.md` | yes | yes | repaired | contaminated |
| `ornstein2025-stochastic-parrot.md` | `10_sources/ornstein2025-stochastic-parrot.md` | yes | weak | repaired | contaminated |
| `pangakis2023-llm-annotation-validation.md` | `10_sources/pangakis2023-llm-annotation-validation.md` | yes | yes | repaired | contaminated |
| `pelaez2024-patent-public-value-llm.md` | `10_sources/pelaez2024-patent-public-value-llm.md` | yes | yes | repaired | contaminated |
| `prognos2019-zim-evaluation.md` | `10_sources/prognos2019-zim-evaluation.md` | yes | yes | checked | clean |
| `rammer-schubert2025-ikt-branchenbild.md` | `10_sources/rammer-schubert2025-ikt-branchenbild.md` | yes | yes | repaired | contaminated |
| `rammer2024-innovationsindikator.md` | `10_sources/rammer2024-innovationsindikator.md` | yes | yes | repaired | contaminated |
| `rammer2025-indikatorenbericht-innovation.md` | `10_sources/rammer2025-indikatorenbericht-innovation.md` | yes | yes | repaired | contaminated |
| `rammer_krieger_peters2022-sme-drivers-barriers.md` | `10_sources/Rammer et al_2022_Treiber und Hemmnisse der Innovationst?tigkeit im deutschen Mittelstand.md` | yes | yes | repaired; source mapping corrected | contaminated |
| `schubert-rammer2026-maschinenbau.md` | `10_sources/schubert-rammer2026-maschinenbau.md` | yes | yes | repaired | contaminated |
| `snow2008-cheap-fast-annotation.md` | `10_sources/snow2008-cheap-fast-annotation.md` | yes | yes | repaired | contaminated |
| `stehnken2024-zim-evaluation.md` | `10_sources/stehnken2024-zim-evaluation.md` | yes | yes | repaired | contaminated |
| `struss2016-zim-wirkungsanalyse.md` | `10_sources/struss2016-zim-wirkungsanalyse.md` | yes | yes | repaired | contaminated |
| `timoneda2025a-bert-roberta-deberta.md` | `10_sources/timoneda2025a-bert-roberta-deberta.md` | yes | yes | repaired | contaminated |
| `timoneda2025b-behind-the-mask.md` | `10_sources/timoneda2025b-behind-the-mask.md` | yes | yes | repaired | contaminated |
| `tornberg2025-llm-outperform-experts.md` | `10_sources/tornberg2025-llm-outperform-experts.md` | yes | yes | repaired | contaminated |
| `trucco2025-scaling-up-ideas.md` | `10_sources/ec_jrc_scaling_up_ideas.md` | yes | yes | repaired | contaminated |
| `wachstumspfade-deutschland.md` | `10_sources/wachstumspfade-deutschland.md` | yes | yes | repaired | contaminated |
| `wang2024-bert-vs-gpt.md` | `10_sources/wang2024-bert-vs-gpt.md` | yes | yes | repaired | contaminated |
| `zhang2021-few-shot-bert.md` | `10_sources/zhang2021-few-shot-bert.md` | yes | yes | repaired | contaminated |
| `ziems2024-llm-css-benchmark.md` | `10_sources/ziems2024-llm-css-benchmark.md` | yes | yes | repaired | contaminated |

## Comparison

The audit distinguishes three quality states. Clean summaries already had the required structure, a correct mapped source, and no repeated batch-ingest markers. Repaired summaries had a usable maintained interpretation but were contaminated by repeated source snippets, generic link lists, or source-grounding boilerplate. Weak-match summaries had an existing source file but needed citation caution because titles were abbreviated, translated, noisy after PDF conversion, or initially mapped incorrectly.

This comparison matters because the old A-tier checker rewarded length, required headings, and links. It did not penalize a note for repeating the same source paragraph across methodology, data, findings, limitations, and conclusion. The fidelity audit therefore adds a semantic maintenance layer: A-tier structure is necessary, but not sufficient, unless source mapping and repetition checks also pass.

## Open questions and remaining manual checks

- A weak title/content match does not necessarily mean the summary is wrong; it often reflects abbreviated titles, translated German titles, or converted PDF noise. It does mean citation-level claims should be checked against the mapped source file before use.
- This audit removed the known repetition failure mode. It does not replace expert rereading of every full PDF for publication-grade citation checking.
- Future `wiki-maintain` should treat repeated auto-ingest marker text as a blocking failure even if the structural verifier reports A-tier.

## Implications

Future wiki-ingest and wiki-maintain runs should treat repeated paragraphs, generic canonical-link blocks, and wrong source paths as blocking defects. A summary is not good merely because it is long. It must be source-specific, non-repetitive, correctly mapped to a source, and useful for retrieval without polluting `wiki-pull` with boilerplate.

For project work, this audit should be retrieved when a paper summary appears suspiciously long or generic. It documents the remediation logic and the remaining source-verification caution flags so future agents can avoid repeating the same batch-ingest failure.

Related maintenance surfaces:
- [[90_synthesis/wiki-operating-protocol.md]]
- [[90_synthesis/wiki-quality-audit-2026-04-28.md]]
- [[90_synthesis/full-vault-remediation-plan-2026-04-28.md]]
- [[90_synthesis/germany-innovation-policy-evidence-map.md]]
- [[70_projects/bundesinnovationshaushalt-trl.md]]

## Retrieval map

| Query | Expected retrieval |
| --- | --- |
| "which summaries were repaired after repeated paragraph issue" | this audit, `log.md`, affected `20_summaries/` notes |
| "source summary source verification weak match" | this audit table plus the mapped summary/source file |
| "wiki summary quality standards" | [[90_synthesis/wiki-operating-protocol.md]], this audit |

