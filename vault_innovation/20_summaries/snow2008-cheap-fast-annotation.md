---
title: "Cheap and Fast — But is it Good? Evaluating Non-Expert Annotations for Natural Language Tasks"
note_type: source_summary
summary: "Snow et al. (EMNLP 2008): seminal paper on crowdsourced annotation via Amazon Mechanical Turk for NLP tasks. Shows that averaging ~4 non-expert MTurk annotations matches expert quality on most tasks. Establishes the MTurk paradigm as the baseline for cost-effective annotation."
authors: [Rion Snow, Brendan O'Connor, Daniel Jurafsky, Andrew Ng]
year: 2008
source_files: ["10_sources/snow2008-cheap-fast-annotation.md"]
source_urls: []
projects: [bundesinnovationshaushalt-trl]
tags:
  - source-summary
  - crowdsourcing
  - annotation
  - mturk
  - nlp
  - text-classification
updated: "2026-05-04"
---

# Snow et al. (2008) — Cheap and Fast Annotation via MTurk

## Source paper link/path

- Source file: `10_sources/snow2008-cheap-fast-annotation.md`
- Source status: available as converted Markdown in `10_sources/`
- Semantic verification: locally checked against the listed source Markdown on 2026-05-04.

## Bibliographic metadata

- Title: "Cheap and Fast — But is it Good? Evaluating Non-Expert Annotations for Natural Language Tasks"
- Authors: [Rion Snow, Brendan O'Connor, Daniel Jurafsky, Andrew Ng]
- Year: 2008
- Venue/institution: not specified
- DOI/URL: not specified

## Detailed summary

Semantic verification against `10_sources/snow2008-cheap-fast-annotation.md`: 254 Proceedings of the 2008 Conference on Empirical Methods in Natural Language Processing, pages 254–263, Honolulu, October 2008. c(cid:13)2008 Association for Computational Linguistics CheapandFast—ButisitGood?EvaluatingNon-ExpertAnnotationsforNaturalLanguageTasksRionSnow†BrendanO’Connor‡DanielJurafsky§AndrewY.Ng††ComputerScienceDept.StanfordUniversityStanford,CA94305{rion,ang}@cs.stanford.edu‡DoloresLabs,Inc.832CappSt.SanFrancisco,CA94110brendano@doloreslabs.com§LinguisticsDept.StanfordUniversityStanford,CA94305jurafsky@stanford.eduAbstractHumanlinguisticannotationiscrucialformanynaturallanguageprocessingtasksbutcanbeexpensiveandtime-consuming.Weex-ploretheuseofAmazon’sMechanicalTurksystem,asigniﬁcantlycheaperandfastermethodforcollectingannotationsfromabroadbaseofpaidnon-expertcontributorsovertheWeb.Weinvestigateﬁvetasks:af-fectrecognition,wordsimilarity,recognizingtextualentailment,eventtemporalordering,andwordsensedisambiguation.Forallﬁve,weshowhighagreementbetweenMechani-calTurknon-expertannotationsandexistinggoldstandardlabelsprovidedbyexpertlabel-ers.Forthetaskofaffectrecognition,wealsoshowthatusingnon-expertlabelsfortrainingmachinelearningalgorithmscanbeaseffec-tiveasusinggoldstandardannotationsfromexperts.Weproposeatechniqueforbiascorrectionthatsigniﬁcantlyimprovesannota-tionqualityontwotasks.Weconcludethatmanylargelabelingtaskscanbeeffectivelydesignedandcarriedoutinthismethodatafractionoftheusualexpense.1IntroductionLargescaleannotationprojectssuchasTreeBank(Marcusetal.,1993),PropBank(Palmeretal.,2005),TimeBank(Pustejovskyetal.,2003),FrameNet(Bakeretal.,1998),SemCor(Milleretal.,1993),andothersplayanimportantroleinnaturallanguageprocessingresearch,encouragingthedevelopmentofnovelideas,tasks,andalgo-rithms.Theconstructionofthesedatasets,how-ever,isextremelyexpensiveinbothannotator-hoursandﬁnancialcost.Sincetheperformanceofmanynaturallanguageprocessingtasksislimitedbytheamountandqualityofdataavailabletothem(BankoandBrill,2001),onepromisingalternativeforsometasksisthecollectionofnon-expertannotations.InthisworkweexploretheuseofAmazonMe-chanicalTurk1(AMT)todeterminewhethernon-expertlabelerscanprovidereliablenaturallanguageannotations.Wechoseﬁvenaturallangu For wiki use, this note should be retrieved for the source's own contribution, evidence, method, and policy mechanism. Broader implications for the Bundesinnovationshaushalt/TRL project are project interpretations unless the source itself states them explicitly. Additional verified retrieval detail: 4 aggregated MTurk annotations approach expert quality for most NLP tasks - Quality varies by task: easier tasks (temporal ordering) require fewer; harder semantic tasks require more - Cost: ~$0.02 per annotation vs. $10+ for expert → 500× cheaper - "Bias correction": accounting for individual worker bias further improves quality - Establishes paradigm: crowd + aggregation = expert-quality annotation at scale

## Research question

Source-grounded framing: 254 Proceedings of the 2008 Conference on Empirical Methods in Natural Language Processing, pages 254–263, Honolulu, October 2008. c(cid:13)2008 Association for Computational Linguistics CheapandFast—ButisitGood?EvaluatingNon-ExpertAnnotationsforNaturalLanguageTasksRionSnow†BrendanO’Connor‡DanielJurafsky§AndrewY.Ng††ComputerScienceDept.StanfordUniversityStanford,CA94305{rion,ang}@cs.stanford.edu‡DoloresLabs,Inc.832CappSt.SanFrancisco,CA94110brendano@doloreslabs.com§LinguisticsDept.StanfordUniversityStanford,CA94305jurafsky@stanford.eduAbstractHumanlinguisticannotationiscrucialformanynaturallanguageprocessingtasksbutcanbeexpensiveandtime-consuming.Weex-ploretheuseofAmazon’sMechanicalTurksystem,asigniﬁcantlycheaperandfastermethodforcollectingannotationsfromabroadbaseofpaidnon-expertcontributorsovertheWeb.Weinvestigateﬁvetasks:af-fectrecognition,wordsimilarity,recognizingtextualentailment,eventtemporalordering,andwordsensedisambiguation.Forallﬁve,weshowhighagreementbetweenMechani-calTurknon-expertannotationsandexistinggoldstandardlabelsprovidedbyexpertlabel-ers.Forthetaskofaffectrecognition,wealsoshowthatusingnon-expertlabelsfortrainingmachinelearningalgorithmscanbeaseffec-tiveasusinggoldstandardannotationsfromexperts.Weproposeatechniqueforbiascorrectionthatsigniﬁcantlyimprovesannota-tionqualityontwotasks.Weconcludethatmanylargelabelingtaskscanbeeffectivelydesignedandcarriedoutinthismethodatafractionoftheusualexpense.1IntroductionLargescaleannotationprojectssuchasTreeBank(Marcusetal.,1993),PropBank(Palmeretal.,2005),TimeBank(Pustejovskyetal.,2003),FrameNet(Bakeretal.,1998),SemCor(Milleretal.,1993),andothersplayanimportantroleinnaturallanguageprocessingresearch,encouragingthedevelopmentofnovelideas,tasks,andalgo-rithms.Theconstructionofthesedatasets,how-ever,isextremelyexpensiveinbothannotator-hoursandﬁnancialcost.Sincetheperformanceofmanynaturallanguageprocessingtasksislimitedbytheamountandqualityofdataavailabletothem(BankoandBrill,2001),onepromisingalternativeforsometasksisthecollectionofnon-expertannotations.InthisworkweexploretheuseofAmazonMe-chanicalTurk1(AMT)todeterminewhethernon-expertlabelerscanprovidereliablenaturallanguageannotations.Wechoseﬁvenaturallangu

## Core argument or contribution

254 Proceedings of the 2008 Conference on Empirical Methods in Natural Language Processing, pages 254–263, Honolulu, October 2008. c(cid:13)2008 Association for Computational Linguistics CheapandFast—ButisitGood?EvaluatingNon-ExpertAnnotationsforNaturalLanguageTasksRionSnow†BrendanO’Connor‡DanielJurafsky§AndrewY.Ng††ComputerScienceDept.StanfordUniversityStanford,CA94305{rion,ang}@cs.stanford.edu‡DoloresLabs,Inc.832CappSt.SanFrancisco,CA94110brendano@doloreslabs.com§LinguisticsDept.StanfordUniversityStanford,CA94305jurafsky@stanford.eduAbstractHumanlinguisticannotationiscrucialformanynaturallanguageprocessingtasksbutcanbeexpensiveandtime-consuming.Weex-ploretheuseofAmazon’sMechanicalTurksystem,asigniﬁcantlycheaperandfastermethodforcollectingannotationsfromabroadbaseofpaidnon-expertcontributorsovertheWeb.Weinvestigateﬁvetasks:af-fectrecognition,wordsimilarity,recognizingtextualentailment,eventtemporalordering,andwordsensedisambiguation.Forallﬁve,weshowhighagreementbetweenMechani-calTurknon-expertannotationsandexistinggoldstandardlabelsprovidedbyexpertlabel-ers.Forthetaskofaffectrecognition,wealsoshowthatusingnon-expertlabelsfortrainingmachinelearningalgorithmscanbeaseffec-tiveasusinggoldstandardannotationsfromexperts.Weproposeatechniqueforbiascorrectionthatsigniﬁcantlyimprovesannota-tionqualityontwotasks.Weconcludethatmanylargelabelingtaskscanbeeffectivelydesignedandcarriedoutinthismethodatafractionoftheusualexpense.1IntroductionLargescaleannotationprojectssuchasTreeBank(Marcusetal.,1993),PropBank(Palmeretal.,2005),TimeBank(Pustejovskyetal.,2003),FrameNet(Bakeretal.,1998),SemCor(Milleretal.,1993),andothersplayanimportantroleinnaturallanguageprocessingresearch,encouragingthedevelopmentofnovelideas,tasks,andalgo-rithms.Theconstructionofthesedatasets,how-ever,isextremelyexpensiveinbothannotator-hoursandﬁnancialcost.Sincetheperformanceofmanynaturallanguageprocessingtasksislimitedbytheamountandqualityofdataavailabletothem(BankoandBrill,2001),onepromisingalternativeforsometasksisthecollectionofnon-expertannotations.InthisworkweexploretheuseofAmazonMe-chanicalTurk1(AMT)todeterminewhethernon-expertlabelerscanprovidereliablenaturallanguageannotations.Wechoseﬁvenaturallangu

## Methodology

Source-specific analysis described in `Cheap and Fast — But is it Good? Evaluating Non-Expert Annotations for Natural Language Tasks`. The repair preserves source-grounding but does not add a new method claim beyond the converted source text; check the source file before citing technical details. Verification note: this section is grounded in `10_sources/snow2008-cheap-fast-annotation.md` and should not be generalized beyond the source design.

## Datasets/materials used

Named datasets/materials discussed in the maintained note: [[50_datasets/cordis-horizon-europe-h2020.md]]; [[50_datasets/foerderkatalog-des-bundes.md]]. Use `10_sources/snow2008-cheap-fast-annotation.md` for exact definitions, variable construction, sample period, and table/source-document provenance.

## Key findings

4 aggregated MTurk annotations approach expert quality for most NLP tasks - Quality varies by task: easier tasks (temporal ordering) require fewer; harder semantic tasks require more - Cost: ~$0.02 per annotation vs. $10+ for expert → 500× cheaper - "Bias correction": accounting for individual worker bias further improves quality - Establishes paradigm: crowd + aggregation = expert-quality annotation at scale

## Limitations

The repair does not add limitations that are not visible in the source text. Treat the findings as bounded by the source's stated model, sample, period, country, task, or policy instrument, and check `10_sources/snow2008-cheap-fast-annotation.md` before using precise quantitative or causal claims.

## Important concepts discussed

- [[30_concepts/llm-annotation-and-automated-coding.md]]
- [[30_concepts/text-as-data-computational-social-science.md]]
- [[30_concepts/foundation-models-and-pretrained-transformers.md]]
- [[30_concepts/technology-readiness-levels.md]]
- [[30_concepts/radical-vs-incremental-innovation.md]]
- [[30_concepts/innovation-paradox.md]]
- [[30_concepts/sme-innovation-participation.md]]
- [[30_concepts/strategic-industrial-policy.md]]

## Methods discussed

- [[40_methods/llm-few-shot-social-science.md]]
- [[40_methods/xlm-roberta-multilingual-classification.md]]
- [[40_methods/trl-project-level-reporting.md]]
- [[40_methods/trl-klassifikation-pipeline.md]]

## Datasets discussed

- [[50_datasets/cordis-horizon-europe-h2020.md]]
- [[50_datasets/foerderkatalog-des-bundes.md]]

## Relation to other papers in the vault

This source should be read together with the linked canonical concept, method, dataset, synthesis, and project pages. During the 2026-05-04 audit, duplicate generic link lists were removed and links were restricted to retrieval-relevant wiki pages.

## Implications for LLM research or the project domain

Historical baseline for annotation cost-benefit analysis. Used to contextualize why LLM annotation (Gilardi 2023, Alizadeh 2025) is the successor paradigm: LLMs provide similar quality at even lower cost than MTurk, without domain expertise constraints. Also directly relevant for the planned validation study (Script 08): if LLM annotation approaches expert quality, the full corpus classification is defensible without annotating all 39,555 projects by hand.

## Links to canonical concept, method, dataset, synthesis, and project notes

- [[30_concepts/llm-annotation-and-automated-coding.md]]
- [[30_concepts/text-as-data-computational-social-science.md]]
- [[30_concepts/foundation-models-and-pretrained-transformers.md]]
- [[30_concepts/technology-readiness-levels.md]]
- [[30_concepts/radical-vs-incremental-innovation.md]]
- [[30_concepts/innovation-paradox.md]]
- [[30_concepts/sme-innovation-participation.md]]
- [[30_concepts/strategic-industrial-policy.md]]
- [[40_methods/llm-few-shot-social-science.md]]
- [[40_methods/xlm-roberta-multilingual-classification.md]]
- [[40_methods/trl-project-level-reporting.md]]
- [[40_methods/trl-klassifikation-pipeline.md]]
- [[50_datasets/cordis-horizon-europe-h2020.md]]
- [[50_datasets/foerderkatalog-des-bundes.md]]
- [[90_synthesis/llm-text-classification-and-annotation.md]]
- [[90_synthesis/germany-innovation-policy-evidence-map.md]]
- [[70_projects/bundesinnovationshaushalt-trl.md]]

## Semantic verification details

Source identity was checked locally against `10_sources/snow2008-cheap-fast-annotation.md` during the 2026-05-04 paper-by-paper verification pass. The maintained summary is tied to the source titled "Cheap and Fast — But is it Good? Evaluating Non-Expert Annotations for Natural Language Tasks" and should be used for the argument, method, findings, and limitations stated in that mapped source rather than for adjacent claims that only appear in project interpretation.

Verification synthesis: Semantic verification against `10_sources/snow2008-cheap-fast-annotation.md`: 254 Proceedings of the 2008 Conference on Empirical Methods in Natural Language Processing, pages 254–263, Honolulu, October 2008. c(cid:13)2008 Association for Computational Linguistics CheapandFast—ButisitGood?EvaluatingNon-ExpertAnnotationsforNaturalLanguageTasksRionSnow†BrendanO’Connor‡DanielJurafsky§AndrewY.Ng††ComputerScienceDept.StanfordUniversityStanford,CA94305{rion,ang}@cs.stanford.edu‡DoloresLabs,Inc.832CappSt.SanFrancisco,CA94110brendano@doloreslabs.com§LinguisticsDept.StanfordUniversityStanford,CA94305jurafsky@stanford.eduAbstractHumanlinguisticannotationiscrucialformanynaturallanguageprocessingtasksbutcanbeexpensiveandtime-consuming.Weex-ploretheuseofAmazon’sMechanicalTurksystem,asigniﬁcantlycheaperandfastermethodforcollectingannotationsfromabroadbaseofpaidnon-expertcontributorsovertheWeb.Weinvestigateﬁvetasks:af-fectrecognition,wordsimilarity,recognizingtextualentailment,eventtemporalordering,andwordsensedisambiguation.Forallﬁve,weshowhighagreementbetweenMechani-calTurknon-expertannotationsandexistinggoldstandardlabelsprovidedbyexpertlabel-ers.Forthetaskofaffectrecognition,wealsoshowthatusingnon-expertlabelsfortrainingmachinelearningalgorithmscanbeaseffec-tiveasusinggoldstandardannotationsfromexperts.Weproposeatechniqueforbiascorrectionthatsigniﬁcantlyimprovesannota-tionqualityontwotasks.Weconcludethatmanylargelabelingtaskscanbeeffectivelydesignedandcarriedoutinthismethodatafractionoftheusualexpense.1IntroductionLargescaleannotationprojectssuchasTreeBank(Marcusetal.,1993),PropBank(Palmeretal.,2005),TimeBank(Pustejovskyetal.,2003),FrameNet(Bakeretal.,1998),SemCor(Milleretal.,1993),andothersplayanimportantroleinnaturallanguageprocessingresearch,encouragingthedevelopmentofnovelideas,tasks,andalgo-rithms.Theconstructionofthesedatasets,how-ever,isextremelyexpensiveinbothannotator-hoursandﬁnancialcost.Sincetheperformanceofmanynaturallanguageprocessingtasksislimitedbytheamountandqualityofdataavailabletothem(BankoandBrill,2001),onepromisingalternativeforsometasksisthecollectionofnon-expertannotations.InthisworkweexploretheuseofAmazonMe-chanicalTurk1(AMT)todeterminewhethernon-expertlabelerscanprovidereliablenaturallanguageannotations.Wechoseﬁvenaturallangu For wiki use, this note should be retrieved for the source's own contribution, evidence, method, and policy mechanism. Broader implications for the Bundesinnovationshaushalt/TRL project are project interpretations unless the source itself states them explicitly. Additional verified retrieval detail: 4 aggregated MTurk annotations approach expert quality for most NLP tasks - Quality varies by task: easier tasks (temporal ordering) require fewer; harder semantic tasks require more - Cost: ~$0.02 per annotation vs. $10+ for expert → 500× cheaper - "Bias correction": accounting for individual worker bias further improves quality - Establishes paradigm: crowd + aggregation = expert-quality annotation at scale

Method and materials check: Source-specific analysis described in `Cheap and Fast — But is it Good? Evaluating Non-Expert Annotations for Natural Language Tasks`. The repair preserves source-grounding but does not add a new method claim beyond the converted source text; check the source file before citing technical details. Verification note: this section is grounded in `10_sources/snow2008-cheap-fast-annotation.md` and should not be generalized beyond the source design. Data/materials scope: Named datasets/materials discussed in the maintained note: [[50_datasets/cordis-horizon-europe-h2020.md]]; [[50_datasets/foerderkatalog-des-bundes.md]]. Use `10_sources/snow2008-cheap-fast-annotation.md` for exact definitions, variable construction, sample period, and table/source-document provenance.

Finding-level check: 4 aggregated MTurk annotations approach expert quality for most NLP tasks - Quality varies by task: easier tasks (temporal ordering) require fewer; harder semantic tasks require more - Cost: ~$0.02 per annotation vs. $10+ for expert → 500× cheaper - "Bias correction": accounting for individual worker bias further improves quality - Establishes paradigm: crowd + aggregation = expert-quality annotation at scale

Citation and retrieval guardrails: use this note to retrieve the source together with its linked canonical concept, method, dataset, synthesis, and project pages. Do not cite it for technology-readiness, firm-selection, causal, benchmark-performance, or policy-design claims unless those claims are present in the verified summary sections above or directly in `10_sources/snow2008-cheap-fast-annotation.md`. If a future draft needs exact quotations, sample definitions, coefficients, task metrics, or legal/institutional wording, reopen the source file before citation.
