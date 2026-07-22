Codebook LLMs: Evaluating LLMs as Measurement Tools for
Political Science Concepts
Andrew Halterman Katherine A. Keith
Department of Political Science Department of Computer Science
Michigan State University Williams College
halterm3@msu.edu kak5@williams.edu
Abstract
Codebooks—documents that operationalize concepts and outline annotation procedures—are
used almost universally by social scientists when coding political texts. To code these texts
automatically, researchers are increasing turning to generative large language models (LLMs).
However, there is limited empirical evidence on whether “off-the-shelf” LLMs faithfully follow
real-worldcodebookoperationalizationsandmeasurecomplexpoliticalconstructswithsufficient
accuracy. To address this, we gather and curate three real-world political science codebooks—
covering protest events, political violence and manifestos—along with their unstructured texts
and human labels. We also propose a five-stage framework for codebook-LLM measurement:
preparing a codebook for both humans and LLMs, testing LLMs’ basic capabilities on a code-
book, evaluating zero-shot measurement accuracy (i.e. off-the-shelf performance), analyzing
errors, and further (parameter-efficient) supervised training of LLMs. We provide an empirical
demonstrationofthisframeworkusingourthreecodebookdatasetsandseveralpretrained7-12
billion open-weight LLMs. We find current open-weight LLMs have limitations in following
codebooks zero-shot, but that supervised instruction tuning can substantially improve perfor-
mance. Ratherthansuggestingthe“best”LLM,ourcontributionliesinourcodebookdatasets,
evaluation framework, and guidance for applied researchers who wish to implement their own
codebook-LLM measurement projects.
1 Introduction
Political scientists are increasingly turning to generative large language models (LLMs) for text
analysis due in part to their potential to classify documents with no labeled examples, i.e. “zero-
shot”(Atrejaetal.,2024;Egamietal.,2023;Gilardietal.,2023;Heseltine&ClemmvonHohenberg,
2024;Peskoff&Stewart,2023;Ryttingetal.,2023;Ziemsetal.,2024). Researcherstypicallyprovide
the LLM with a set of categorical labels (e.g., protest or riot), (sometimes) brief label descriptions,
and instructions to classify texts given the labels. When given a document to be classified, the
LLM generates the predicted (natural-language) label of each document (e.g., the LLM generates
“protest”). While this approach enables cheap and fast analysis of large text corpora, it implicitly
assumesthatthesesimpleinstructionsaloneoperationalizethepreciseconceptsthatresearchersaim
1
5202
naJ
9
]LC.sc[
2v74701.7042:viXra

to measure. Because LLMs are pretrained on extremely large text corpora, the models often have
reasonable zero-shot predictive accuracy on concepts that have broad coverage and straightforward
definitions in the pretraining data.
However, this use of LLMs is in tension with foundational concepts of measurement in political
science. In the standard conception of measurement validity (Adcock & Collier, 2001), researchers
must transform broad “background” concepts into precise, systematized constructs through careful
operationalization. In many projects that produce structured data form text, researchers rely on
codebooks—documentsthatdefineconceptsinprecisetermsandoutlineannotationprocedures. As
a brief example, while an LLM may have an ability to recognize a “protest” from its training data,
different projects systematize this concept in substantively different ways. For instance, the Crowd
Counting Consortium (Crowd Counting Consortium, 2024) includes rallies in support of a person
or issue, while the CAMEO event ontology (Gerner et al., 2002) explicitly excludes gatherings in
support of a person or policy from its protest class. Using an LLM’s predictions of a background
conceptof“protest”withoutregardtothesesystematizeddefinitionsthreatensmeasurementvalidity
and could lead to incorrect substantive conclusions.
This mismatch between measurement theory and current LLM usage arises from two potential
problems. First,researchersoftenprovideLLMswithonlysimplecategorylabelsorbriefdefinitions
rather than complete codebooks, meaning the LLM’s outputs may not reflect the specific construct
theresearcheraimstomeasure. Second, evenwhengivenfullcodebookinstructions, LLMsmaynot
actuallyattendtothedetaileddefinitionswhengeneratinglabels,insteadrelyingontheirpretraining
representation of the concepts. Without faithfully following the codebook definitions, the LLM’s
outputs may reflect the general background concept rather than the systematized construct.
In this work, we introduce a framework to rigorously evaluate and improve codebook-LLM mea-
surement and provide an empirical demonstration of the framework. We make four main contribu-
tions. First,wedevelopafive-stageevaluationframeworkthatguidesresearchersthroughcodebook
preparation, label-free testing, zero-shot evaluation, robustness evaluations, and training LLMs on
supervised examples. Within these stages, we contribute seven new codebook-specific behavioral
tests (Ribeiro et al., 2020)—controllable interventions on LLM inputs test LLMs basic capabilities
andfailuremodes—manyofwhichrequirenoground-truthlabelssocanbeusedearlyinaproject’s
lifecycle. Second, we collect, format, and release three real-world political science codebooks, their
2

associated hand-coded datasets, and source texts covering contentious politics in the United States,
political violence in Pakistan, and party manifestos. The codebook settings are realistic but po-
tentially challenging for LLMs due to their domain-specific concepts, large number of class labels
(up to 142), and lengthy codebook definitions. Third, we provide an empirical demonstration of
open-weight LLMs classifying documents from these datasets, and find limitations in select LLMs’
abilitytocomplywithcodebookinstructionsinzero-shotsettings. Finally, weshowthatsupervised
instruction tuning—updatingLLMweightsdirectlyfromhuman-codedexamples—cansubstantially
improveperformance(byupto55%),andprovidedetailedguidanceforresearchersonimplementing
| parameter-efficient | versions  | of  | this training. |     |             |     |
| ------------------- | --------- | --- | -------------- | --- | ----------- | --- |
| 2 A                 | Framework | for | Codebook-LLM   |     | Measurement |     |
In this section, we provide an overview of our framework to evaluate codebook-LLM measurement,
classifyingunlabeleddocumentswithLLMsgivenahuman-writtencodebook. Inthiswork,wefocus
on multi-class (single-label) classificationof N documents, {Zˆ ∈Z|X }N where Z is the finite set
|     |     |     |     |     | i i | i=1 |
| --- | --- | --- | --- | --- | --- | --- |
of labels described in the codebook, Zˆ is an LLM-predicted class of a document i, and X is the
i i
document text. Most often these measurements, Zˆ, are then used in downstream analysis (Knox
i
etal.,2022). Althoughrecentworkhasshownonecanadjustfornoisymeasurement-inducedbiasin
downstream analysis (Egami et al., 2023), more accurate measurement will often yield more precise
| estimates | (and thus tighter | valid | confidence | intervals). |     |     |
| --------- | ----------------- | ----- | ---------- | ----------- | --- | --- |
Our proposed codebook-LLM measurement evaluation framework consists of five stages. The rest
| of this article | expands | on each | stage. |     |     |     |
| --------------- | ------- | ------- | ------ | --- | --- | --- |
• Stage 0: Codebook preparation: Even when using LLMs, researchers must prepare their
codebook by operationalizing their social science concepts. We suggest a semi-structured
format with standardized components including definitions, clarifications, and examples that
| can | be used by both | humans | and machines. |     |     |     |
| --- | --------------- | ------ | ------------- | --- | --- | --- |
•
Stage 1: Label-free behavioral testing: Before investing in hand-labeling, we suggest
researchers use our proposed label-free behavioral tests to assess an LLM’s ability to follow
instructions and make consistent predictions “off-the-shelf”. The results can help guide both
| LLM | selection and | the choice | between | zero-shot | use and supervised | learning. |
| --- | ------------- | ---------- | ------- | --------- | ------------------ | --------- |
3

• Stage 2: Zero-shot evaluation with labels: The next stage requires researchers to hand-
code a small evaluation set and then assess LLM zero-shot performance. Quantitative results
canrevealweaknessesineitherthecodebookortheLLM’sabilitytopredictfromit,potentially
requiring codebook revision or a different LLM.
• Stage 3: Zero-shot error analysis: We suggest thorough error analysis using ablation
experiments, behavioral tests requiring labels, and manual analysis of outputs to understand
systematic errors.
• Stage 4: Supervised finetuning: If zero-shot performance proves inadequate, researchers
can update the LLM weights directly via instruction tuning on human-coded examples. We
provide guidance on parameter-efficient techniques to make this computationally feasible.
The stages can be performed sequentially or iteratively as needed, with results from later stages
potentially informing revisions to earlier decisions. The rest of the paper details each stage.
3 Related Work
Recent work has has examined using LLMs to classifysocial science concepts, in both zero-shot (no
labeled training examples) or few-shot (some labeled examples) settings. Halterman et al. (2021)
use a BERT model finetuned for a natural language inference (NLI) task for zero-shot classifica-
tion of political events and achieve up to 0.74 F1 on some classes. Ziems et al. (2024) collect 25
English-language computational social science benchmarks and find that although LLMs’ zero-shot
results rarely exceed the carefully tuned supervised RoBERTa baseline, for some tasks LLMs have
respectablezero-shotperformance. Gilardietal.(2023)findzero-shotChatGPToutperformscrowd
workers on relevance, stance, topics, and frame detection tasks, using short class descriptions for
each label. Mellon et al. (2024) use LLMs to code open-text survey responses and found similar
accuracy to human annotators. Pangakis and Wolken (2024) gather 14 classification tasks from
recently published CSS articles; they generate labels using LLMs and then use these labels in (more
classical)supervisedNLPpipelinesandfindtheclassifiersperformcomparablytomodelswithlabels
from human annotators. Atreja et al. (2024) examine four social science datasets/tasks—toxicity,
sentiment analysis, rumor stance detection, news frame classification—and use a factorial design to
vary aspects of the prompt; they find results are very task and model dependent. Halterman (2024)
4

shows that careful prompting with social science concepts can generate useful synthetic data for
training document classifiers. Burnham (2024) discusses the importance of providing the LLM with
definitions and broader context. In the subsequent sections, we describe how our codebook datasets
differ, and go beyond previous work by demonstrating instruction tuning LLMs.
SIsectionCdiscusseshowcodebook-LLMmeasurementdiffersfromcommoncomputerscienceLLM
benchmarks.
Recent work, which is complementary to our work here, examines the consequences of using noisy
“proxy” labels in downstream inference (Chen et al., 2024; Egami et al., 2023; Knox et al., 2022).
Specifically,Egamietal.(2023)findthatevenwhenLLMsarequiteaccurateinlabelingdocuments,
using these “surrogate” labels in downstream analysis as independent variables can induce severe
bias and coverage issues and suggests a correction.
4 Empirical Set-up: Data and LLMs
4.1 Codebook Datasets
To serve as real-world training and evaluation datasets, we collect three separate English-language
political science datasets, each of which provide document-level or (quasi-) sentence-level labels ac-
cordingtoacodebook-definedschema: theCrowdCountingConsortium(CCC)datasetonprotests
intheUnitedStates(CrowdCountingConsortium,2024),theBFRSdatasetonviolenceinPakistan
(Bueno de Mesquita et al., 2015), and the Manifesto Project corpus (Lehmann et al., 2017). We
obtaintheiroriginalcodebooksandaselectionoftheEnglish-languagetextthatthedatawascoded
from (see Section D.1 for additional details). We believe this collection reflects the real-world diffi-
cultyofthecodebook-LLMmeasurementduetothedatasets’(1)constructionbysocialscientiststo
measure specific political concepts that potentially do not exist in LLMs supervised training data;
(2) large number of classes (up to 142; see Table 1); (3) longer documents (in the CCC dataset),
and (4) long codebook lengths.
In our curation effort, we reformat these datasets for single-label, multi-class classification. For the
Manifestos dataset, we use the Manifesto Project policy/ideology label for a (quasi) sentence in
a political party’s manifesto. The For BFRS and CCC, we focus solely on classifying event type
from news articles. We randomly split the data 70-15-15 into training, development, and test splits
5

|     | Dataset   |                |            |            |       | BFRS CCC     | Manifestos |       |
| --- | --------- | -------------- | ---------- | ---------- | ----- | ------------ | ---------- | ----- |
|     | Num.      | classes        |            |            |       | 12           | 8          | 142   |
|     | Per-class | definition     | median     | whitespace | toks. | 20 28        |            | 14    |
|     | Codebook  | total          | whitespace | toks.      |       | 1,614 608    |            | 3,910 |
|     | Codebook  | total          | Llama      | toks.      |       | 2,083 721    |            | 5,145 |
|     | Input     | text (doc.)    | median     | whitespace | toks. | 28 437       |            | 16    |
|     | Num.      | train          | instances  |            |       | 20,978 4,710 |            | 8,081 |
|     | Num.      | dev. instances |            |            |       | 4,495 1,009  |            | 1,732 |
|     | Num.      | test           | instances  |            |       | 4,496 1,010  |            | 1,732 |
Table 1: Descriptive statistics about the codebook datasets. For length of the codebooks,
we report both whitespace tokens and number of tokens after using the Llama-3 tokenizer (Llama
toks.).
respectively. Inthiswork,weonlyusethetraininganddevelopmentsetstoguardagainstoverfitting
| to the test | set. |     |     |     |     |     |     |     |
| ----------- | ---- | --- | --- | --- | --- | --- | --- | --- |
SI D.1 provides more details on the dataset preprocessing, including the process of scraping or
obtaining raw text, sampling documents, converting multi-label examples to single-label multi-class
labels, and in the case of BFRS, using an alternative text source. We believe that all three of these
datasets are mostly safe from training set contamination, that is, that they are not present in the
| LLM’s pretraining |     | data; | see SI D.2. |     |     |     |     |     |
| ----------------- | --- | ----- | ----------- | --- | --- | --- | --- | --- |
| 4.2 Choosing      |     | LLMs  |             |     |     |     |     |     |
Ourevaluationframeworkismodel-agnostic,butweconstrainourempiricaldemonstrationtoopen-
weight LLMs for reproducibility and to models that fit on a consumer GPU (24GB VRAM). We
select four high-performing LLMs in the 7-12 billion (B) parameter range: Mistral-7B-Instruct-v0.2
(“Mistral-7B”),Mistral-NeMo-Instruct-2407(“Mistral-NeMo-12B”),Llama-3.1-8B-Instruct(“Llama-
8B”), OLMo-7B-0724-Instruct-hf (“OLMo-7B”). Section F provides details and citations for these
models. We emphasize that we select open weight models to ensure reproducibility. Applied re-
searchers may make a different accuracy–reproducibility tradeoff and select larger closed-weight
| models (Palmer |     | et al., 2024). |     |     |     |     |     |     |
| -------------- | --- | -------------- | --- | --- | --- | --- | --- | --- |
These models have varying context lengths: Llama-8B and Mistral-NeMo-12B handle 128K tokens,
Mistral-7B handles 32K, and OLMo-7B a maximum input of 4096 tokens. We note that effective
| context | length | for information | retrieval | may be | shorter | (Hsieh et al., 2024). |     |     |
| ------- | ------ | --------------- | --------- | ------ | ------- | --------------------- | --- | --- |
6

4.3 LLMs for multi-class classification
WeuseLLMsformulti-classclassificationbyprovidingtheentirecodebookanddocumentasinput,
then selecting the first generated token sequence matching a valid label as the predicted label Zˆ.
Other work has attempted to constrain the output vocabulary or bias the generated tokens towards
the valid set of labels (Ziems et al., 2024). However, other work has found using the generated text
outputs is more accurate (X. Wang et al., 2024) and our choice of LLMs almost always outputted
valid labels (see Test I in Stage 1 and Figure 3) so we did not modify the LLM generation process
for simplicity.
As an alternative to inputting the entire codebook with all class labels and descriptions, one could
use LLMs in a one-versus-rest approach. In this approach, the LLM takes as input a single class
description and makes binary prediction, the document is that label or not, e.g., Burnham et al.
(2024). However, in preliminary experiments we found no accuracy improvements in a one-versus-
rest set-up. We hypothesize that for the datasets we gathered the full codebook and all labels
together are required to delineate between classes (see SI F). For example, an LLM used in a
one-versus-rest set-up might incorrectly predict that a drone strike meets the BFRS codebook’s
definition of an Assassination, unless it has access to the full codebook with the (correct) Drone
Assassination category. Furthermore, one-versus-rest significantly increases the computational
time.
We leave to future work a full engineering effort comparing these implementation details. Fur-
thermore, with the rapid advancement of LLM development, we believe the quantitative results
we present about particular LLMs will quickly be surpassed. However, we believe our evaluation
framework, behavioral test templates, and curated codebook datasets will stand the test of time.
Wenowdescribeinmoredetailourfivestagesofourempiricalevaluationframeworkandprovidean
empirical demonstration of this framework with our codebook datasets and selected LLMs.
5 Stage 0: Codebook preparation
Instage0,researchersmustpreparethecodebookbywritingnatural-languageoperationalizationsof
the variables and putting the codebook in a format that is readable by both machines and humans.
While LLMs offer exciting possibilities for scaling up measurement, this stage cannot be bypassed
7

or automated.
Codebook operationalization. Codebook-LLM measurement is fundamentally different than
typical NLP classification because the same background concept or label—e.g., a “protest”—could
have several different possible natural-language written operationalizations in the codebook. The
goalistohaveanLLMcorrectlyattendtothespecificoperationalization,otherwisedifferentpolitical
| variables | may | be incorrectly | conflated | or correlated |     | in downstream | analysis. |
| --------- | --- | -------------- | --------- | ------------- | --- | ------------- | --------- |
Machine-readable semi-structured codebook format. We propose a new generalizable and
consistent format for codebooks that is both human and machine readable. Previous instruction
tuningresearchsuggeststhatexplicitlyprovidingadefinition,positiveexample,andnegativeexample
canimprovezero-shotperformanceonadiversesetofNLPtasks(Y.Wangetal.,2022). Separating
partsofeachcodebookdefinitionintocomponentsalsoallowsustoexperimentallyisolateandablate
| components | to  | evaluate | changes in performance |     | (see | Table 4). |     |
| ---------- | --- | -------- | ---------------------- | --- | ---- | --------- | --- |
Anexcerptof therestructuredBFRScodebookisshownin Figure1. Wemanuallyrestructureeach
of the codebooks into this format. Future researchers could write codebooks from the outset to be
| both human- | and      | machine-readable. |                        |            |            |                |            |
| ----------- | -------- | ----------------- | ---------------------- | ---------- | ---------- | -------------- | ---------- |
| Our format  | consists | of                | the following codebook |            | components | (see           | Figure 1): |
| 1. Label:   | The      | exact             | label that the         | LLM should |            | return for the | class.     |
2. Label Definition. We provide a succinct definition of the class, which is generally a single
sentence.
3. Clarification&NegativeClarification. Mostclassesrequirefurtherdetailstodefinethem. This
includes both extra inclusion criteria, as well as what does not fit into the class. For example,
riot
the BFRS category for does not apply if one of the groups involved is a police force.
4. Positive & Negative Examples. Optionally, a codebook can provide examples of documents
that both fit and do not fit, with explations. “Few shot” or “in-context learning”, where an
LLM is provided example input–output pairs in the prompt, has been shown to improve LLM
| performance |     | on new | tasks (Brown | et al., | 2020). |     |     |
| ----------- | --- | ------ | ------------ | ------- | ------ | --- | --- |
IntheLLMprompt,wealsoincludeanoverallcodebook-specificinstructiondescribingthetaskand
8

PromptexcerptfromtheBFRSCodebook
Instructions:
You’reanexpertpoliticalscientistcategorizingnewsstoriesfromPakistanintocategories.
Carefullyreadthedefinitionsbelow,readthestory,andwritetheLabelthatbestmatches
| thestory. Useonlytheprovidedlabels. |     |     |     |     |     |     |
| ----------------------------------- | --- | --- | --- | --- | --- | --- |
Classes:
Label: RIOT
| Definition: | A riot is a violent | clash between two | or more | sizeable | groups | or when a |
| ----------- | ------------------- | ----------------- | ------- | -------- | ------ | --------- |
singleinformallyassembledcrowdbecomesviolent.
| Clarification: | Neither group can | be a state force. | However, | if there | are | two or more |
| -------------- | ----------------- | ----------------- | -------- | -------- | --- | ----------- |
clashesaroundasingleeventinwhichthepoliceareinvolved,thenitwouldbeaclassified
asariot.
| Negative Clarification: | For example, | the students | of the | Lal Masjid | versus | the police |
| ----------------------- | ------------ | ------------ | ------ | ---------- | ------ | ---------- |
wouldnotbeconsideredariot,itwouldbeaViolentPoliticalDemonstration.
| Positive Example: | “Five workers | of the Muslim | Students | Federation, |     | the student |
| ----------------- | ------------- | ------------- | -------- | ----------- | --- | ----------- |
wingoftherulingMuslimconference,sustainedbulletwoundsinaclashwiththeactivists
ofpro-independenceNationalStudentsFederation.”
| Negative Example: | “An angry | mob thrashed police | personnel, | accusing |     | them of man- |
| ----------------- | --------- | ------------------- | ---------- | -------- | --- | ------------ |
handlingpeopleandusingobscenelanguagewhenthey(thepolice)raidedagamblingden.”
Thisincidentinvolvespolice,soitiscodedasa“violentpoliticaldemonstration.”
Label: VIOLENTPOLITICALDEMONSTRATION
| Definition: | Aviolentpoliticaldemonstrationischaracterizedasmobilizationofcrowdsin |     |     |     |     |     |
| ----------- | --------------------------------------------------------------------- | --- | --- | --- | --- | --- |
responsetoapoliticaleventthatatsomepointbecomesviolent.
| Clarification:          | Violencemaybeinitiatedbythecrowdorbythepoliceuponthecrowd. |               |               |        |     |               |
| ----------------------- | ---------------------------------------------------------- | ------------- | ------------- | ------ | --- | ------------- |
| Negative Clarification: | A violent                                                  | clash between | two non-state | groups | is  | a riot, not a |
violentpoliticaldemonstration.
| Positive Example:                                     | “Hundreds       | of school children | and armed            | supporters            |     | of Lashkar-i- |
| ----------------------------------------------------- | --------------- | ------------------ | -------------------- | --------------------- | --- | ------------- |
| Islam stormed                                         | the Bara bazaar | and set the main   | tehsil, Qambaraband, |                       | Al  | Haaj Market,  |
| SheikhanandQasabancheckpostsoftheKhasadarforceonfire. |                 |                    |                      | TheLashkar-i-Islamhad |     |               |
warnedofprotestsiftheirdemandswerenotmet.”
| Negative Example: | “A man | killed and his brother | injured | when | they | were attacked |
| ----------------- | ------ | ---------------------- | ------- | ---- | ---- | ------------- |
bytheirrivalsoveralanddispute.”Themotivationhereisnotapoliticalevent,thusthis
eventisariot,notaviolentpoliticaldemonstration.
...plus10additionalclasses[omittedforspace]
Document:
ShiaschoolboysheldademonstrationdemandingreleaseofastudentdetainedbyRangers
| inconnectionwithanearlierdisturbance. |     | Thestudentswereabouttodisperseafternegoti- |     |     |     |     |
| ------------------------------------- | --- | ------------------------------------------ | --- | --- | --- | --- |
ationswiththepolicewhentheywereencounteredbyRangersatabarricadewhichledto
scufflesandfiring.
| Output reminder:               | WritethenameoftheLabelthatfitsbest,withnoothertext. |                                     |     |     |     | Forexample, |
| ------------------------------ | --------------------------------------------------- | ----------------------------------- | --- | --- | --- | ----------- |
| “Label: ASSASSINATION”,“Label: |                                                     | VIOLENTPOLITICALDEMONSTRATION”,etc. |     |     |     |             |
Figure 1: BFRS codebook as part of an LLM prompt. From the BFRS codebook, this is a
(truncated to 2/12 labels) example of how the codebook is formatted as the LLM input.
9

LLM generated output
VIOLENT POLITICAL DEMONSTRATION
Explanation: The news story describes a demonstration by Shia schoolboys demand-
ingthereleaseofadetainedstudent,whichturnedviolentwhentheywereencountered
by Rangers at a barricade leading to scuffles and firing. This fits the definition of a
violent political demonstration as it involves mobilization of crowds in response to a
political event that at some point becomes violent.
Note: The use of the term “scuffles and firing” indicates that violence was initiated
by both the crowd and the Rangers, making it a violent political demonstration and
not a riot, as the crowd was not clashing with another group.
Therefore
Figure 2: Zero-shot output generated by Mistral-7B given the full BFRS prompt, an excerpt
of which appears in Figure 1. We deterministically match the first part of the beginning of the
output with the set of valid labels to determine the predicted label.
an “Output reminder”. Depending on the measurement task, researchers can omit components or
add others, e.g., adding a structured output (JSON) requirement).
6 Stage 1: Label-free behavioral testing
Attheoutsetofaproject,appliedresearcherscanbenefitfromcheap(i.e.requiringnogroundtruth
labels) and interpretable tests to assure themselves that an LLM can perform basic tasks with the
codebook and choose between LLMs early on in their project’s lifecycle. We propose four label-
free “behavioral tests” (Ribeiro et al., 2020) to measure an LLM’s ability to recall basic parts of
the codebook, to comply with codebook instructions, and to “comprehend” the definitions in the
codebook. Table 2 provides a summary of the tests.
Test I provides a simple test of the LLM’s ability to follow prompt instructions to only return the
valid labels defined in the codebook. Specifically, we check if any of the legal labels appear in the
output text. Tests II and III measure the basic ability of the LLM to “memorize” parts of the
prompt/codebook. For Test II, we provide the LLM with a prompt that contains the structured
codebook, along with a a (verbatim) class definition and an instruction to provide the label for the
class definition. Passing the test requires the basic ability to match the provided definition with
the (identical) definition in the codebook. For Test III, we provide verbatim positive and negative
examples from the codebook and ask for their labels. None of these tasks require “reasoning”, just
10

simple pattern matching. Failure on these tasks may indicate problems with the LLM’s ability
to recall components of the codebook which could have serious ramifications for codebook-LLM
measurement as a whole.
If the LLM is “comprehending” the codebook, then its predicted labels should not change if the
order that the categories are presented in the codebook changes (Test IV). We evaluate the LLM
senstitivity to codebook order in two ways. First, we calculate the percentage of predicted labels
that remain the same between the original codebook and predictions when the category order is
(1) reversed or (2) randomly shuffled. Second, we calculate the inter-“coder” agreement, measured
using Fleiss’s kappa, in predictions across the original, reversed, and shuffled codebooks.
Results. We evaluate the four LLMs described in Section 4.2 on these four codebook-specific
behavioral label-free tests. Because only the BFRS codebook has positive and negative examples,
we conduct these tests only the BFRS dataset. See Figure 3 for results. Mistral-7B, Mistral-NeMo-
12B, and Llama-8B perform well on Tests I through III, checking for legal outputs and verbatim
definition and example recovery. We find that all models are sensitive to the order that categories
are described in the codebook (IV), which may indicate problems with the LLM’s attention for our
long prompt contexts; see Liu et al. (2024) and Zhao et al. (2021).
Just as an applied researcher using our framework may do after this stage, we omit OLMo-7B from
our later evaluation stages since its performance is so poor compared to the other models. Mistral-
NeMo-12Bperformswellonsometests,buttheimprovementisnotgreatenoughtojustifythelarger
model size and increased computational costs. Thus, we only compare Mistral-7B and Llama-8B in
the next stages.
7 Stage 2: Zero-shot evaluation with labels
Afteridentifyingpromisingmodelsthroughlabel-freebehavioraltests,appliedresearcherscanhand-
label a subset of their data and evaluate the zero-shot performance of LLMs on labeled data. This
is not a new evaluation approach—see (Atreja et al., 2024; Ziems et al., 2024, inter alia)—but, in
this work, we evaluate LLMs on our curated codebook datasets which we believe provide a more
realistic picture of codebook-LLM measurement.
11

|     | Test       |            |     |       | Ramifications | of failed | test |
| --- | ---------- | ---------- | --- | ----- | ------------- | --------- | ---- |
|     | Label-free | behavioral |     | tests |               |           |      |
| I   | Legal      | Labels     |     |       |               |           |      |
Does the LLM only return labels defined Inability to follow basic instructions or to recall
in the codebook? the set of legal labels provided in the prompt.
| II  | Definition | recovery |     |     |     |     |     |
| --- | ---------- | -------- | --- | --- | --- | --- | --- |
Can the LLM correctly label a verbatim Inabilityto“memorize”orretrieveportionsofthe
|     | codebook | definition? |     |          | codebook. |     |     |
| --- | -------- | ----------- | --- | -------- | --------- | --- | --- |
| III | Classify | in-context  |     | examples |           |     |     |
CantheLLMcorrectlylabelverbatimex- Inabilityto“memorize”orretrieveportionsofthe
|     | amples   | provided | in    | the codebook? | codebook. |     |     |
| --- | -------- | -------- | ----- | ------------- | --------- | --- | --- |
| IV  | Codebook |          | order | invariance    |           |     |     |
Are LLM predictions unaffected by code- Inconsistent attention across the length of the
book category order? prompt or ordering effects. Predicted labels de-
|     |                 |          |            |             | pend on | the order of classes | in the prompt. |
| --- | --------------- | -------- | ---------- | ----------- | ------- | -------------------- | -------------- |
|     | Labels-required |          | behavioral | tests       |         |                      |                |
| V   | Exclusion       | criteria |            | consistency |         |                      |                |
Across the four combinations of (modi- Inability to follow instructions and ignore irrele-
fied, original) × (document, codebook), vant distractions. May reveal problems attending
are the LLM predictions consistently cor- to specific inclusion or exclusion criteria.
rect?
| VI  | Generic | Label | Accuracy |     |     |     |     |
| --- | ------- | ----- | -------- | --- | --- | --- | --- |
Can the LLM classify examples when Over-reliance on the label as opposed to the defi-
given non-informative labels? nitions. May indicate that the predicted label re-
|     |         |       |          |     | flectsthe   | backgroundconceptinsteadof | theoper- |
| --- | ------- | ----- | -------- | --- | ----------- | -------------------------- | -------- |
|     |         |       |          |     | ationalized | concept.                   |          |
| VII | Swapped | Label | Accuracy |     |             |                            |          |
CantheLLMclassifyexamplesaccording Over-reliance on the names of the labels (vs. def-
|     | tothecodebook’sdefinitionswhen(infor- |        |              |          | initions). |     |     |
| --- | ------------------------------------- | ------ | ------------ | -------- | ---------- | --- | --- |
|     | mative)                               | labels | are randomly | swapped? |            |     |     |
Table 2: Proposed behavioral tests for codebooks. See Section 6 for “label-free” tests and
| Section | 8 for | “labels-required” |     | tests. |     |     |     |
| ------- | ----- | ----------------- | --- | ------ | --- | --- | --- |
12

| Model Type | OLMo−8B | Mistral−7B | Mistral NeMo−12B | LLama−8B |     |
| ---------- | ------- | ---------- | ---------------- | -------- | --- |
TestI:LegalLabels
TestII:Definition
recovery
TestIIIa:Classify
(positive)in−contextexamples
TestIIIb:Classify
(negative)in−contextexamples
| 0%  | 25% | 50% |     | 75% | 100% |
| --- | --- | --- | --- | --- | ---- |
Percent Correct
TestIV:Codebookorder
invariance(agreement)
|      |      | Moderage | Substantial | Near Perfect |      |
| ---- | ---- | -------- | ----------- | ------------ | ---- |
| 0.00 | 0.25 | 0.50     |             | 0.75         | 1.00 |
Fleiss' Kappa (across original, reversed, and shuffled codebook order)
TestIV:Codebookorder
invariance(shuffledcodebook)
TestIV:Codebookorder
invariance(reversedcodebook)
| 0%  | 25% | 50% |     | 75% | 100% |
| --- | --- | --- | --- | --- | ---- |
Consistency in codebook predictions (1 − disagreement)
Figure 3: Label-free behavioral test results on the BFRS dataset. For all tests, higher numbers
are better. See Table 2 for details of each test. For Test IV, dashed lines are the Fleiss Kappa
heuristics from Landis (1977).
13

Zero-shot results. Table 3 shows the zero-shot weighted F1 scores1 on the development set of
each of our three datasets for Llama-8B and Mistral-7B. We compare our semi-structured codebook
format with the original codebooks as written by the original authors, only changing them by
prepending “Label:” to each label in the codebook to indicate what the LLM should predict in its
output.
From Table 3, we see that dev-set zero-shot results range from very poor with 0.21 (weighted) F1
on Manifestos, to marginal with 0.65 and 0.57 on CCC and BFRS respectively. There is no clear
“winner”betweenLlama-8BandMistral-7B.ThisweakperformancesuggeststhatusingeitherLLM
on complex codebook tasks, either with original or re-written codebooks, is unlikely to be useful to
applied analysts without fundamental improvements in the base LLMs to read, comprehend, and
comply with codebook instructions or further updating the LLM weights on supervised examples
(i.e. instruction tuning in Stage 4). We examine the robustness and further try to understand these
| zero-shot results | in Stage 3.      |        |                  |                  |
| ----------------- | ---------------- | ------ | ---------------- | ---------------- |
|                   | Dataset Codebook | format | Llama-8B         | Mistral-7B       |
|                   |                  | Ours   | 0.57 [0.55-0.58] | 0.53 [0.52-0.55] |
BFRS
|     |     | Original | 0.55 [0.53-0.56] | 0.44 [0.42-0.45] |
| --- | --- | -------- | ---------------- | ---------------- |
|     |     | Ours     | 0.61 [0.58-0.64] | 0.65 [0.62-0.68] |
CCC
|     |     | Original | 0.48 [0.45-0.52] | 0.51 [0.48-0.54] |
| --- | --- | -------- | ---------------- | ---------------- |
|     |     | Ours     | 0.19 [0.17-0.21] | 0.15 [0.13-0.17] |
Manifestos
|     |     | Original | 0.21 [0.19-0.23] | 0.14 [0.12-0.16] |
| --- | --- | -------- | ---------------- | ---------------- |
Table 3: Zero-shot weighted F1 scores for each LLM on each development dataset. We com-
pareoursemi-structuredcodebookformat(“ours”)andtheoriginalauthors’format(thelatteronly
changed by prepending “Label:” when appropriate). Square brackets indicate 95% confidence in-
| tervals via | 500 bootstrap resamples | of the (predicted, | true) pairs. |     |
| ----------- | ----------------------- | ------------------ | ------------ | --- |
| 8 Stage     | 3: Zero-shot            | error analysis     |              |     |
Stage 3 of our framework expands zero-shot evaluation of LLMs beyond aggregate performance
metricsinordertobetterunderstandtheLLMs’errorsandrobustness. Weusethreecomplementary
approaches: (1) we propose three additional behavioral tests that require labeled examples; (2)
we systematically ablate different components of the codebook to understand how these different
componentsaffectLLMperformance;and(3)weconductdetailedmanualanalysis oftheoutputand
1Specifically,weimplementthisviascikit-learn’sfunctionf1 score(y true, y pred, average=‘weighted’). This
takestheaverageofper-classF1scores,weightedbysamplesize,toaccountforimbalance.
14

explanations. Weencourageappliedresearcherstousealloftheseapproachesontheirowncodebook-
LLM measurement projects—regardless of the aggregate zero-shot performance—to understand the
errors their specific LLM is prone to make.
8.1 Labels-required behavioral tests
We build from the label-free behavioral tests in Stage 1, to conduct additional behavioral tests that
require ground-truth labels. We describe and implement three additional tests (Test V, VI, and
VII); see Table 2 and Figure 4.
Test V–Exclusion criteria consistencyborrowsatechniqueproposedbyKarpinskaetal.(2024)
to identify whether LLMs are not “right for the wrong reason”. We modify both documents and
codebooks with an exclusion criterion that makes a label invalid if a specific trigger word is present
(e.g., “elephant”). The LLM should only reject the label when both the trigger appears in the
document and the exclusion criterion appears in the codebook. This creates four test conditions,
and LLMs must respond correctly to all four to demonstrate they are following the codebook’s
instructions.2
TestsVIandVIIprovideadirectmeasureofhowmuchtheLLMisrelyingonthelabelitselfversus
following the instructions in the codebook. In Test VI–Generic Label Accuracy we replace the
original labels with a non-informative labels (e.g. LABEL 1). In VII–Swapped Label Accuracy
wepermutetheoriginallabelsinthecodebooksoeachlabelispairedwithadifferentdefinition. An
LLM should ideally follow the definitions despite the distraction of the swapped labels.
Results. Figure 4 shows the performance of Mistral-7B and Llama-8B on the labels-required be-
havioraltests,againusingtheBFRSdevelopmentdatasetandcodebook. Themodelsperformpoorly
on Test V, providing evidence that LLMs are not following specific codebook operationalizations.
Finally, tests VI and VII show that the LLMs are indeed relying on the semantic content of the la-
bels themselves, performing worse when the labels are replaced with generic terms or swapped. We
cautionappliedresearchersthatiftheirconstructsintheircodebooksdeviatetoofarfromtheback-
ground concepts an LLM has learned during pretraining, the zero-shot results may have systematic
errors that could affect overall substantive results.
2Specifically,weadd”IMPORTANTNOTE:Thiscategorydoesnotapplyifthedocumentdiscussesanelephant”
tothecodebookand”Andwealsosupportelephants”tothedocument.
15

Model Type Mistral−7B LLama−8B
TestV:Exclusionminimal
pairs(allcorrect)
TestV(baseline):
Exclusionminimalpairs
(normalcodebook,normaldoc)
0% 25% 50% 75% 100%
Percent correctly classified
BaselineF1
TestVI:GenericLabel
Accuracy
TestVII:SwappedLabel
Accuracy
0.00 0.25 0.50 0.75 1.00
F1 Score
Figure4: Labels-required behavioral testsofthetwoLLMsontheBFRSdevelopmentdataset.
See Table 2 for details of each test.
8.2 Zero-shot ablations
Codebook Component
n
o
Cl a s s D e
fi ni ti
o n
O u t p u t
R e mi
n d e r
P o si ti v e
E x a
m pl e
N e g a ti v e
E x a
m pl e
Cl a ri fi c a
ti o n
N e g a ti v e
Cl a
ri fi c a
ti
Dev F1
0.53 ∗
✗ 0.42
✗ ✗ 0.46
✗ ✗ ✗ ✗ 0.43
✗ ✗ ✗ ✗ ✗ 0.20
✗ ✗ ✗ ✗ ✗ ✗ 0.29
Table4: Codebook ablation results for zero-shot predictionsfromMistral-7BontheBFRS
development dataset. We report the weighted F1 scores, and ✗ indicates the component of the
codebook that we ablated. ∗The unablated zero-shot result in the first row is the same as Table 3.
Next, to understand how different components of the codebook affect LLM performance, we con-
duct an ablation experiment on the BFRS dataset by systematically removing (ablating) different
codebook elements (e.g. dropping “Negative Clarification” or “Positive Example”) and measuring
the impact on Mistral-7B’s zero-shot F1 scores. We used the BFRS codebook because its original
codebook was the most similar to our proposed new format (i.e. it already included positive and
negative examples). We explore a limited set of the 26 possible options, focusing on the ones we
16

believe are most relevant to applied researchers.
Results. Table 4 shows the results of five ablation experiments. As expected, systematically
ablating components decreases performance, indicating most components are necessary to achieve
eventheoriginaltF1scoreof0.53. Notably,comparingthethefifthtosixthrowsinTable4results
insurprisinglybetter performancewhendroppingtheclassdefinition,providingonlythelabelitself.
In combination with our other error analysis results in this stage, this finding may suggest that the
LLM is not fully adhering to the label definition in the codebook, which could be consequential
for any codebook-LLM measurement that compared the same label across two operationalizations
(e.g., the two “protest” operationalizations we mentioned in the introduction). In this codebook–
LLM combination, including all codebook components improves performance, but we are cautious
about drawing universal conclusions about optimal codebook components.
8.3 Manual analysis of zero-shot generative outputs
We recommend applied researchers manually analyze LLM outputs. Although the explanations
generated by an LLM are not necessarily always logically consistent or “faithful” to their internal
representations and predictions (Jacovi & Goldberg, 2020; Lyu et al., 2024), inspecting the output
canilluminatesomeoftheLLM’sfailuremodes. Asademonstration,weconductedacarefulmanual
analysis on a sample from each dataset of the zero-shot outputs from Mistral-7B. Then we (the two
authors) manually analyzed the model inputs, model outputs, and gold-standard labels. After an
initial pilot round, we developed manually labeled LLM’s outputs into one of six classes; see SI J
for details.
Results. Table 5 shows the aggregate results of the manual analysis. Mistral-7B compliance with
prompt instructions related to allowable labels was excellent for BFRS (0% non-compliance) and
CCC (2% non-compliance). However, for Manifestos, 45% of the sampled LLM outputs were non-
compliant. These included errors such as outputting multiple labels or more egregious errors such
as hallucinating labels (see Table SI 4).
We find evidence suggesting that Mistral-7B is relying on heuristics and shortcuts and not actually
“reading” the codebooks. In one instance, a Manifesto example supporting increased education
funding gets the predicted label “WELFARE POSITIVE (or EDUCATION POSITIVE)” (see Ta-
17

|     |              |                     |                      |         |          | BFRS CCC Manifestos |      |
| --- | ------------ | ------------------- | -------------------- | ------- | -------- | ------------------- | ---- |
|     | Sample:      | Num.                | Examples             |         |          | 24 50               | 62   |
|     | Sample:      | Num.                | of Unique            | Classes |          | 12 5                | 50   |
|     | A. LLM       | correct             |                      |         |          | 0.38 0.48           | 0.11 |
|     | B. Incorrect | gold                | standard             |         |          | 0.04 0.10           | 0.08 |
|     | C. Document  |                     | error (scraping/lack |         | context) | 0.04 0.02           | 0.03 |
|     | D. LLM       | non-compliance      |                      |         |          | 0.00 0.02           | 0.45 |
|     | E. LLM       | semantics/reasoning |                      | mistake |          | 0.50 0.26           | 0.29 |
|     | F. Other     |                     |                      |         |          | 0.04 0.10           | 0.02 |
Table 5: Manual error analysis results on a sample of the zero-shot generative outputs for
Mistral-7B given each development dataset. For each dataset, we report the number of examples
and the number of unique classes in that sample as well as the proportion of outputs in categories
| A-F as | judged by the | authors. | See | Section | J for definitions | of each category. |     |
| ------ | ------------- | -------- | --- | ------- | ----------------- | ----------------- | --- |
ble SI 4). However, an explicit constraint in the Manifesto’s codebook for the welfare positive
| label is | “This category | excludes | education.” |     |     |     |     |
| -------- | -------------- | -------- | ----------- | --- | --- | --- | --- |
We also find evidence that Mistral is using lexical overlap heuristics (Levy et al., 2023)—selecting
labelwordsthatappearinthetext,evenifthelabelisincorrect. Forexample,inCCC-1inTableSI
4, the word “rally” occurs in the first sentence of the text and the LLM predicts the rally label
even though the text clearly aligns with the codebook definition of a demonstration.
These errors reveal limitations in how Mistral-7B interprets and applies the precise definitional
boundaries that make codebooks valuable as measurement tools, and motivates Stage 4 to update
| the weights | of an LLM | given      | additional | supervised | examples. |     |     |
| ----------- | --------- | ---------- | ---------- | ---------- | --------- | --- | --- |
| 9 Stage     | 4:        | Supervised |            | finetuning |           |     |     |
If Stages 1-3 show zero-shot performance is inadequate, researchers may need to abandon the zero-
shot approach. If this is the case, they can return to (familiar) supervised classification techniques:
training a “classic” supervised machine learning model from scratch or finetuning a BERT-based
modeltopredictthelabelforeachdocument(Grimmeretal., 2022). Ratherthanrepeattheexten-
sive literature on supervised text classification, we describe and provide an empirical demonstration
forapromisingnewtechnique–instruction tuning inwhichanLLM’sweightsarefurtherupdatedon
supervised input/output pairs via a next token prediction objective function (Longpre et al., 2023;
Sanh et al., 2022; Y. Wang et al., 2022, 2023; Wei, Bosma, et al., 2022). While zero-shot prompting
provides instructions to an off-the-shelf model at inference time, instruction tuning allows us to
18

improve the model’s ability to follow instructions, using supervised learning. This approach differs
from traditional supervised learning—rather than training a supervised model on (document, label)
pairs to return the correct label, we train it on (instruction, document, label) pairs, and obtain a
| generated |     | label (e.g, | y =“protest”). |     | 3   |     |     |     |     |     |     |
| --------- | --- | ----------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Directly updating the weights in LLMs given supervised examples is very expensive in terms of
training time and memory because most LLMs consist of billions of weights. However, we describe
howtouseparameter-efficienttechniquesofquantization–loadingmodelweightswithlessprecision,
i.e. using fewer bits—and low-rank adaptation (LoRA) in which only a fraction of the weights are
updated.
In practice, instruction tuning involves providing the LLM with training examples from the original
| datasets, | consisting |          | of:         |     |     |     |     |     |     |     |     |
| --------- | ---------- | -------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.        | The        | codebook | (C)         |     |     |     |     |     |     |     |     |
| 2.        | A document |          | to classify | (X  | )   |     |     |     |     |     |     |
i
| 3.  | The | correct | natural-language |     | label | for that | document | e.g., | “protest” | (y ) |     |
| --- | --- | ------- | ---------------- | --- | ----- | -------- | -------- | ----- | --------- | ---- | --- |
i
For our instruction tuning set-up, a training dataset—BFRS, CCC, or Manifestos—consists of D
tuples {(m ,y )}D where m is the entire “prompt” (consisting of the concatenation of C and X
|         |     | i i       | i=1           | i   |            |     |     |     |     |     | i   |
| ------- | --- | --------- | ------------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
| as well | as  | any other | instructions; |     | see Figure | 1). |     |     |     |     |     |
Following previous work (Y. Wang et al., 2023), we do not compute the language modeling loss
on the prompt, only on the output (See SI G). For each example i = 1,...,D, let N mi be the
total number of tokens for the example’s prompt m and N be the total number of tokens for the
|     |     |     |     |     |     |     | i   | yi  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
corresponding output y . Then the negative log-likelihood loss function (masking inputs) is:
i

0
|     |     |     |      | D        |          |      |       |      | if j ∈N |     |     |
| --- | --- | --- | ---- | -------- | -------- | ---- | ----- | ---- | ------- | --- | --- |
|     |     |     |      | (cid:88) | (cid:88) |      |       |      |         | mi  |     |
|     |     |     | L ≡− |          |          | logp | (t |t | )×   |         |     | (1) |
|     |     |     | θ    |          |          |      | θ i,j | i,<j |         |     |     |
1
|     |     |     |     | i=1j∈[Nmi |     | ,Nyi ] |     |     | otherwise |     |     |
| --- | --- | --- | --- | --------- | --- | ------ | --- | --- | --------- | --- | --- |
where t is the gold-standard jth token in either the input m or output y . The model weights θ
|     | i,j          |     |             |      |      |           |     |     | i   | i   |     |
| --- | ------------ | --- | ----------- | ---- | ---- | --------- | --- | --- | --- | --- | --- |
| are | then updated |     | to minimize | this | loss | function. |     |     |     |     |     |
3Foraglossaryoftermsusedinthissection,seeSIA.
19

9.1 QLoRA training: quantization + low-rank adaptation
Fully updating all the weights in an LLM during instruction tuning is costly in computing time
and memory requirements. To address this, we use “quantized low-rank adaptation” (QLoRA)
(Dettmers et al., 2024; Hu et al., 2022), a technique that makes finetuning LLMs more efficient in
two ways. First, it “quantizes” each weight–representing them a lower precision value (here, 4 bits),
reducing memory requirements by around 75% compared to a full precision model. Second, instead
of updating the full matrix of weights, it decomposes the weight matrix into two low-rank weight
matrices to update.4 This approach closely matches the set-up described in (Jindal et al., 2024),
which won the 2023 NeurIPS challenge for efficient LLM instruction tuning.
We use a fixed rank of 16 in the results shown in Table 6. LoRA models have a broader set of
hyperparameters, which we keep fixed; future work could look to domain-specific hyperparameter
tuning. See SI Section G for details.
9.2 Instruction tuning results
Table6reportstheweightedF1scoresofourinstructiontunedmodels. Foreachmodel,weconduct
QLoRa finetuning on the entire training set and evaluate on the entire dev set. We find consistent
improvement in all instruction tuned models over their zero-shot results. For example, on BFRS,
Mistral-7B improves its performance over its zero-shot results by 0.29 F1 (from 0.53 zero-shot to
0.82 instruction tuned) which is a 55% relative improvement. Performance gains for CCC are lower
across both models and only slightly better than the baseline of the majority class. We hypothesize
thiscouldbeduetoCCCdocumentsbeingmuchlongerandthusmuchmoredifficulttoclassify. We
omittheresultforLlamaonManifestos–evenwithabatchsizeofone,thetrainingprocessexceeded
our GPU’s memory.
The finetuning process was quite costly in terms of total training time. However, the loss plateaued
after about 10% of the total training examples so future work might be able to speed this up by
trainingonfewerexamplesorbetter“earlystopping.” Overall,theseresultsindicatethatinstruction
tuningisaviableapproachforimprovingamodel’sabilitytopredictclassesgivenchallengingcode-
books and poor zero-shot results, albeit with increased computational and annotation costs.
4Thatis,ratherthanupdatingtheentireweightmatrixW ∈Rd×d,LoRAdecomposesW intod×r,r×dmatrices,
withsignificantlyfewerweightsthanthefullweightmatrix(withr=16,∼0.5%.)
20

|     | Dataset    | LLM        |          |       | Dev F1           | ∆ Zero-shot |     | Train   | time |
| --- | ---------- | ---------- | -------- | ----- | ---------------- | ----------- | --- | ------- | ---- |
|     |            | Baseline:  | Majority | class | 0.16             |             | –   |         | –    |
|     | BFRS       | Llama-8B   |          |       | 0.81 [0.80–0.82] | +0.24       |     | 6h 01m  | 11s  |
|     |            | Mistral-7B |          |       | 0.82 [0.81–0.83] | +0.29       |     | 6h 51m  | 59s  |
|     |            | Baseline:  | Majority | class | 0.51             |             | –   |         | –    |
|     | CCC        | Llama-8B   |          |       | 0.68 [0.64–0.70] | +0.07       |     | 1h 29m  | 52s  |
|     |            | Mistral-7B |          |       | 0.72 [0.69–0.75] | +0.07       |     | 1h 40m  | 38s  |
|     |            | Baseline:  | Majority | class | 0.03             |             | –   |         | –    |
|     | Manifestos | Llama-8B   |          |       | –∗               |             | –   |         | –    |
|     |            | Mistral-7B |          |       | 0.38 [0.35–0.40] | +0.23       |     | 17h 53m | 47s  |
Table 6: Results of LLMs after instruction tuning on each training dataset; for training
numberofexamplesseeTable1. Wereportabaselineofpredictingonlytheclasswasseenthemost
duringtraining(majorityclass),theweightedF1scoreonthedevelopmentset(DevF1),thechange
from the corresponding model’s zero-shot results in Table 3 (∆ zero-shot), and the total training
wall time on our single NVIDIA RTX 4090 GPU. Square brackets indicate 95% confidence intervals
via 500 bootstrap resamples of the (predicted, true) pairs. ∗We do not report Llama result on the
| Manifestos |        | due to out-of-memory | error | with | batch size=1. |     |     |     |     |
| ---------- | ------ | -------------------- | ----- | ---- | ------------- | --- | --- | --- | --- |
| 10         | Future | work                 |       |      |               |     |     |     |     |
We see several avenues for future research. Our set of three datasets and codebooks provide a
challenging test bed (especially Manifestos) for a real-world codebook-LLM measurement. Future
engineeringworkwillimproveonourzero-shotandinstructiontuningresultspresentedinthispaper
byusingnewermodels,employingtechniquessuchaschain-of-thoughtreasoning(Wei,Wang,etal.,
2022) or self-improving prompts (Khattab et al., 2023), and experimenting with different instruc-
tion tuning hyperparameters. We emphasize that our paper’s core contributions lie in formalizing
codebook-LLM measurement, proposing a set of behavioral tests, providing benchmark datasets,
and establishing baseline performance results. We fully expect future work to achieve improved
performance.
LLMscouldalsobeusedin-the-loopforcodebookdevelopment. Codebooksareoftendevelopediter-
atively during annotation as edge cases arise or annotators raise questions. Updating the codebook
during annotation requires retraining annotators and potentially re-annotating existing documents,
which can slow the annotation process. LLMs have the potential to reduce the number of changes
a codebook requires after annotation begins by identifying gaps in the codebook.
Finally, future work could explore different tasks, such as information extraction or multi-label
| classification, |     | and performance | on non-English |     | language text. |     |     |     |     |
| --------------- | --- | --------------- | -------------- | --- | -------------- | --- | --- | --- | --- |
21

11 Conclusion
LLMs offer exciting possibilities for analyzing and classifying text with less human effort. However,
using LLMs for codebook-based measurement is different than many other applications of LLMs: it
requires the LLM to follow the lengthy and detailed operationalization of concepts in a codebook
and to faithfully apply the provided coding criteria rather than solely relying on what it learned
from pretraining. We believe the three codebook datasets we gathered and curated in this paper
represent the real-world complexity of the codebook-LLM measurement task, and there likely exist
many more that could be added to this collection.
For applied researchers looking to use LLMs now, we recommend following our five-stage empirical
framework to systematically evaluate whether and how to employ LLMs for their specific measure-
ment tasks. As LLMs improve, we expect measurement accuracy to improve as well. Rather than
identifying a “best” LLM, we provide guidance and tools for researchers to make informed decisions
about codebook preparation, model selection, and the choice between zero-shot use and supervised
finetuning. Weexpectourframework,particularlyourbehavioraltestsanderroranalysistechniques,
will remain valuable tools for assessing measurement validity as the technology evolves.
12 Acknowledgments
We thank Dallas Card, Luke Sanford, Maria Antoniak, the anonymous reviewers, and attendees at
PolMeth 2024 for helpful comments on the manuscript.
13 Data availability statement
We will post on the Harvard Dataverse the three codebooks, restructured codebooks, and original
text (when possible given copyright and dataset restrictions) or code/instructions to compile the
original text. We will post them in encrypted format (with password available) to prevent them
from being automatically scraped as LLM training data and contaminating the benchmarks.
22

References
Adcock, R., & Collier, D. (2001). Measurement validity: A shared standard for qualitative and
|     | quantitative |     | research. American | Political | Science | Association. |
| --- | ------------ | --- | ------------------ | --------- | ------- | ------------ |
Atreja, S., Ashkinaze, J., Li, L., Mendelsohn, J., & Hemphill, L. (2024). Prompt design matters for
computational social science tasks but in unpredictable ways. arXiv:2406.11980.
Brown,T.,Mann,B.,Ryder,N.,Subbiah,M.,Kaplan,J.D.,Dhariwal,P.,Neelakantan,A.,Shyam,
P., Sastry, G., Askell, A., et al. (2020). Language models are few-shot learners. NeurIPS.
Bueno de Mesquita, E., Fair, C. C., Jordan, J., Rais, R. B., & Shapiro, J. N. (2015). Measuring
political violence in Pakistan: Insights from the BFRS dataset. Conflict Management and
|     | Peace | Science. |     |     |     |     |
| --- | ----- | -------- | --- | --- | --- | --- |
Burnham, M. (2024). Stance detection: A practical guide to classifying political beliefs in text.
|     | Political | Science | Research | and Methods. |     |     |
| --- | --------- | ------- | -------- | ------------ | --- | --- |
Burnham, M., Kahn, K., Wang, R. Y., & Peng, R. X. (2024). Political debate: Efficient zero-shot
|     | and | few-shot | classifiers | for political text. | arXiv | preprint arXiv:2409.02078. |
| --- | --- | -------- | ----------- | ------------------- | ----- | -------------------------- |
Chen, J. M., Bhattacharya, R., & Keith, K. A. (2024). Proximal causal inference with text data.
NeurIPS.
| Crowd | Counting | Consortium. | (2024). | crowdcounting.org. |     |     |
| ----- | -------- | ----------- | ------- | ------------------ | --- | --- |
Dettmers, T., Pagnoni, A., Holtzman, A., & Zettlemoyer, L. (2024). QLoRA: Efficient finetuning of
|     | quantized | LLMs. | NeurIPS. |     |     |     |
| --- | --------- | ----- | -------- | --- | --- | --- |
Egami, N., Hinck, M., Stewart, B., & Wei, H. (2023). Using imperfect surrogates for downstream
inference: Design-based supervised learning for social science applications of large language
|     | models. | NeurIPS. |     |     |     |     |
| --- | ------- | -------- | --- | --- | --- | --- |
Gerner, D. J., Schrodt, P. A., Yilmaz, O., & Abu-Jabr, R. (2002). Conflict and mediation event
observations (CAMEO): A new event data framework for the analysis of foreign policy
|     | interactions. |     | International | Studies Association, |     | New Orleans. |
| --- | ------------- | --- | ------------- | -------------------- | --- | ------------ |
Gilardi,F.,Alizadeh,M.,&Kubli,M.(2023).Chatgptoutperformscrowdworkersfortext-annotation
|     | tasks. | PNAS. |     |     |     |     |
| --- | ------ | ----- | --- | --- | --- | --- |
Grimmer, J., Roberts, M. E., & Stewart, B. M. (2022). Text as data: A new framework for machine
|     | learning | and | the social | sciences. Princeton | U.P. |     |
| --- | -------- | --- | ---------- | ------------------- | ---- | --- |
23

Halterman, A. (2024). Synthetically generated text for supervised text analysis. Political Analysis
(forthcoming).
Halterman,A.,Keith,K.,Sarwar,S.,&O’Connor,B.(2021).Corpus-levelevaluationforEventQA:
The IndiaPoliceEvents corpus covering the 2002 Gujarat violence. Findings of the ACL-
IJCNLP.
Heseltine,M.,&ClemmvonHohenberg,B.(2024).Largelanguagemodelsasasubstituteforhuman
| experts in | annotating |     | political | text. | Research | & Politics. |     |
| ---------- | ---------- | --- | --------- | ----- | -------- | ----------- | --- |
Hsieh,C.-P.,Sun,S.,Kriman,S.,Acharya,S.,Rekesh,D.,Jia,F.,Zhang,Y.,&Ginsburg,B.(2024).
Ruler: What’s the real context size of your long-context language models? arXiv preprint
arXiv:2404.06654.
Hu,E.J.,Shen,Y.,Wallis,P.,Allen-Zhu,Z.,Li,Y.,Wang,S.,Wang,L.,&Chen,W.(2022).LoRA:
| Low-rank | adaptation | of  | large | language | models. | ICLR. |     |
| -------- | ---------- | --- | ----- | -------- | ------- | ----- | --- |
Jacovi, A., & Goldberg, Y. (2020). Towards faithfully interpretable NLP systems: How should we
| define and | evaluate | faithfulness? |     | ACL, | 4198–4205. |     |     |
| ---------- | -------- | ------------- | --- | ---- | ---------- | --- | --- |
Jindal,A.K.,Rajpoot,P.K.,&Parikh,A.(2024).Birbal:Anefficient7binstruct-modelfine-tuned
| with curated | datasets. |     | arXiv:2403.02247. |     |     |     |     |
| ------------ | --------- | --- | ----------------- | --- | --- | --- | --- |
Karpinska, M., Thai, K., Lo, K., Goyal, T., & Iyyer, M. (2024). One thousand and one pairs: A
| “novel” challenge |     | for long-context |     | language |     | models. | EMNLP. |
| ----------------- | --- | ---------------- | --- | -------- | --- | ------- | ------ |
Khattab, O., Singhvi, A., Maheshwari, P., Zhang, Z., Santhanam, K., Vardhamanan, S., Haq, S.,
Sharma, A., Joshi, T. T., Moazam, H., Miller, H., Zaharia, M., & Potts, C. (2023). DSPy:
Compiling declarative language model calls into self-improving pipelines. ICLR.
Knox, D., Lucas, C., & Cho, W. K. T. (2022). Testing causal theories with learned proxies. Annual
| Review of | Political | Science. |     |     |     |     |     |
| --------- | --------- | -------- | --- | --- | --- | --- | --- |
Landis, J. (1977). The measurement of observer agreement for categorical data. Biometrics.
Lehmann, P., Matthieß, T., Merz, N., Regel, S., & Werner, A. (2017). Manifesto corpus. version:
| 2017b (tech. | rep.). | Berlin: | WZB | Berlin | Social | Science | Center. |
| ------------ | ------ | ------- | --- | ------ | ------ | ------- | ------- |
Levy, M., Ravfogel, S., & Goldberg, Y. (2023). Guiding LLM to fool itself: Automatically manipu-
lating machine reading comprehension shortcut triggers. Findings of EMNLP.
Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F., & Liang, P. (2024). Lost
| in the middle: | How | language |     | models | use long | contexts. | TACL, 12, 157–173. |
| -------------- | --- | -------- | --- | ------ | -------- | --------- | ------------------ |
24

Longpre,S.,Hou,L.,Vu,T.,Webson,A.,Chung,H.W.,Tay,Y.,Zhou,D.,Le,Q.V.,Zoph,B.,Wei,
J., et al. (2023). The Flan collection: Designing data and methods for effective instruction
tuning. ICML.
Lyu, Q., Apidianaki, M., & Callison-Burch, C. (2024). Towards faithful model explanation in NLP:
| A survey. | Computational |     | Linguistics. |     |     |     |
| --------- | ------------- | --- | ------------ | --- | --- | --- |
Mellon, J., Bailey, J., Scott, R., Breckwoldt, J., Miori, M., & Schmedeman, P. (2024). Do AIs know
what the most important issue is? using language models to code open-text social survey
| responses | at scale. | Research | &   | Politics. |     |     |
| --------- | --------- | -------- | --- | --------- | --- | --- |
Palmer, A., Smith, N. A., & Spirling, A. (2024). Using proprietary language models in academic
| research | requires | explicit | justification. | Nature | Computational | Science. |
| -------- | -------- | -------- | -------------- | ------ | ------------- | -------- |
Pangakis,N.,&Wolken,S.(2024).Knowledgedistillationinautomatedannotation:Supervisedtext
| classification | with | LLM-generated |     | training labels. | NLP+CSS | Workshop. |
| -------------- | ---- | ------------- | --- | ---------------- | ------- | --------- |
Peskoff, D., & Stewart, B. M. (2023). Credible without credit: Domain experts assess generative
| language | models. | ACL. |     |     |     |     |
| -------- | ------- | ---- | --- | --- | --- | --- |
Ribeiro, M. T., Wu, T., Guestrin, C., & Singh, S. (2020). Beyond accuracy: Behavioral testing of
| NLP models | with | checklist. | ACL. |     |     |     |
| ---------- | ---- | ---------- | ---- | --- | --- | --- |
Rytting,C.M.,Sorensen,T.,Argyle,L.,Busby,E.,Fulda,N.,Gubler,J.,&Wingate,D.(2023).To-
wardscodingsocialsciencedatasetswithlanguagemodels.arXivpreprintarXiv:2306.02177.
Sanh,V.,Webson,A.,Raffel,C.,Bach,S.,Sutawika,L.,Alyafeai,Z.,Chaffin,A.,Stiegler,A.,Raja,
A.,Dey,M.,etal.(2022).Multitaskpromptedtrainingenableszero-shottaskgeneralization.
ICLR.
Wang, X., Hu, C., Ma, B., R¨ottger, P., & Plank, B. (2024). Look at the text: Instruction-tuned
language models are more robust multiple choice selectors than you think. COLM.
Wang, Y., Ivison, H., Dasigi, P., Hessel, J., Khot, T., Chandu, K., Wadden, D., MacMillan, K.,
Smith, N. A., Beltagy, I., et al. (2023). How far can camels go? exploring the state of
| instruction | tuning | on open | resources. | NeurIPS. |     |     |
| ----------- | ------ | ------- | ---------- | -------- | --- | --- |
Wang,Y.,Mishra,S.,Alipoormolabashi,P.,Kordi,Y.,Mirzaei,A.,Naik,A.,Ashok,A.,Dhanasekaran,
A.S.,Arunkumar,A.,Stap,D.,etal.(2022).Super-NaturalInstructions:Generalizationvia
| declarative | instructions |     | on 1600+ | NLP tasks. | EMNLP. |     |
| ----------- | ------------ | --- | -------- | ---------- | ------ | --- |
Wei, J., Bosma, M., Zhao, V., Guu, K., Yu, A. W., Lester, B., Du, N., Dai, A. M., & Le, Q. V.
| (2022). | Finetuned | language | models | are zero-shot | learners. | ICLR. |
| ------- | --------- | -------- | ------ | ------------- | --------- | ----- |
25

Wei, J., Wang, X., Schuurmans, D., Bosma, M., Xia, F., Chi, E., Le, Q. V., Zhou, D., et al. (2022).
Chain-of-thought prompting elicits reasoning in large language models. NeurIPS.
Zhao, Z., Wallace, E., Feng, S., Klein, D., & Singh, S. (2021). Calibrate before use: Improving
| few-shot performance | of language | models. ICML. |     |
| -------------------- | ----------- | ------------- | --- |
Ziems,C.,Held,W.,Shaikh,O.,Chen,J.,Zhang,Z.,&Yang,D.(2024).Canlargelanguagemodels
| transform computational | social | science? Computational | Linguistics. |
| ----------------------- | ------ | ---------------------- | ------------ |
26

Supplemental Information
A Glossary for Applied Researchers
WedirectappliedresearcherstoGrimmeretal.(2022)’stextbookforgeneralandtechnicaloverviews
of the text-as-data field. In this glossary section, we define terms related to our work and LLMs
that may not be present in Grimmer et al. or new to applied readers.
• Ablation: Aevaluationapproachwherecomponentsofasystemareremovedoneatatimeto
understandtheircontribution. Inthecontextofourcodebookablation,wecanremove(ablate)
onecomponentatatime(e.g.,theNegativeClarification). Were-runtheentirepredictionstep
with the ablated codebook and check the performance. A decrease in performance compared
to the full-codebook baseline indicates that the abalated component is important for good
performance.
• Adaptation/Low-rank Adaptation (LoRA): A technique for efficiently updating large
language models for new tasks. Rather than modifying all of a model’s parameters (which
could be billions of parameters), LoRA approximates these changes using smaller matrices.
As an analogy, think about how singular value decomposition approximates a large matrix
with two smaller matrices. Similarly, the full weight matrix is decomposed into two smaller
matrices. In the case of Mistral 7B, our rank 16 LoRa has only 0.5% of the weights of the full
weight matrix. During training, the weights in the full weight matrix remain unchanged–only
the weights in the “low rank” approximation of the weights are updated. At inference time,
the low rank matrices are multiplied by the full weight matrix. See Hu et al. (2022).
• Self-Attention: A mechanism introduced in the Transformer architecture of Vaswani et al.
(2017)andthusakeycomponentinLLMs. Foreachself-attentionlayerandheadandforeach
token(typicallyaword),themodelcomputesthreevectors—aquery,key,andvalue—anduses
these to calculate “attention weights” that determine how much each other token influences
the current token’s representation (embedding). These weights are computed as normalized
dot products between query and key vectors, then used to create a weighted sum of value
vectors. The main text discusses previous empirical results that LLMs attend more to words
at the beginning or end of the prompt, putting less weight on words in the middle.
27

• Classification Head: An additional component added to BERT-style models to perform
classification tasks (Devlin et al., 2019). While the base BERT model learns (via pretraining)
contextual representations of text, and the classification head is a smaller (logistic regression)
modelthattakesBERT’stextrepresentationsandconvertsthemintospecificclasspredictions.
This is similar to how one might first create features from text (like topic model scores) and
then use those features in a logistic regression for classification. The classification head is
typically trained along with the main model to predict numerical class labels (like 0 or 1).
• Few-shot: An approach where the model sees a small number of examples before making
predictions. In the context of LLMs, few-shot learning typically occurs through “in-context
learning”, where examples are included in the prompt rather than used to update the model’s
parameters. Thisissimilartoshowingahumancoderseveralcorrectlycodedexamplesalong-
side the codebook before asking them to code new documents. This differs from traditional
machine learning approaches where models are updated using training examples. See also
zero-shot. See Brown et al. (2020).
• Lexical Overlap Heuristics: A heuristic (or “shortcut”) observed in some LLMs, where
they make predictions based on matching words rather than “understanding” meaning. For
example, a model might label any text containing the word “protest” as a protest event with-
out considering context. This is a familiar problem with dictionary-based approach that can
misclassifytextsbymatchingwordswithoutunderstandingtheirusage. SeeLevyetal.(2023).
• instructiontuning: Amethodforadaptinglanguagemodelstobetterfollowspecificinstruc-
tions by training them on examples of tasks paired with instructions. Instead of training the
model to simply predict the next word in a piece of text or to classify inputs into predefined
categories (like in traditional supervised learning), instruction tuning teaches the model to
generate appropriate responses to instructions. In our context, this means training the model
to read a codebook and document, then generate the correct category label as text. We point
readers to Wang et al. (2023) (which we found to be one of the more accessible instruction
tuning papers).
• LanguageModelingObjective/Loss: Theusualobjective/lossfunctionfortrainingLLMs.
The LLM predicts the next word in a sequence, the predicted token is compared to the true
next token, and the model’s parameters to improve these predictions. The “loss” measures
28

how far off the model’s predictions are from the correct next word. This is similar to how
regression models are trained by minimizing the squared distance between predictions and ac-
tualvalues,butinsteadofpredictingcontinuousnumbers,languagemodelspredictprobability
distributions over possible next words.
• Quantization: A technique for compressing the numerical precision of a model to make it
smallerinmemory. Insteadofstoringnumberswithhighprecision(like2.493827),quantization
might round them to simpler values (like 2.5). This reduces memory and computational
requirements while maintaining most of the model’s performance. See Dettmers et al. (2024).
• Weights: The numerical parameters in a language model. These weights are adjusted dur-
ing training (both pretraining or finetuning) to improve the model’s performance. This is
analogous to how the coefficients in a regression model are optimized to minimize prediction
error.
• Zero-shot: Describes when an LLM makes predictions using only the input prompt, without
seeing any examples (that is zero labeled examples). In our case, this means giving the model
just the codebook definitions and asking it to classify documents. This is analogous to giving
a human coder only a codebook and asking them to begin coding immediately (given their
previous experience and no background). See Wei et al. (2022).
B Ethics
We acknowledge the real-world harm associated with the events reported in the documents in the
datasetsweuse. Webelievequantitativestudyoftheseeventsisimportanttomitigatefutureharm,
but we also acknowledge that it should be paired with qualitative work, hopefully that which also
connectswithandadvocatesforthepeopleaffectedbytheevents(D’Ignazio&Klein,2020). Wealso
acknowledge that all our results focus on English-language codebooks and text documents (Bender,
2019). Our conclusions may not hold on non-English language texts.
Justifiable concerns exist about the use of LLMs, specifically their environmental cost and the
provenance of their training data.
Data provenance. Given the lack of transparency in LLM pretraining data (see Section F), we
cannot know the exact mix of text in the pretraining data. The question of whether pretraining
29

LLMs on copyrighted text is fair use is an open question that we hope for more clarity on.
Environmental Cost. The (marginal) CO costs from using pretrained LLMs is also a concern.
2
Zero-shot experiments were conducted on a server with a single Nvidia RTX 4080 16GB RAM.
instruction tuning experiments were run on a server with 4 x RTX A6000 48GB VRAM. Using a
generous estimate of 100 hours of GPU compute time and an emission factor of 0.50 kg/kWh yields
an estimated 20kg of emitted CO from our experiments. This is slightly less than the CO emitted
2 2
by an average internal combustion vehicle making an Ann Arbor–East Lansing round trip (Lacoste
et al., 2019).
C Comparison with NLP/CS tasks
Here, we provide more details for readers interested in the NLP/computer science literature on how
the codebook measurement task differs from existing techniques and datasets in NLP/CS.
C.1 Machine Reading Comprehension
In NLP, the closest task to our codebook task is machine reading comprehension, also known as
question answering. The task of machine reading comprehension presents text passages to NLP
models and then requires the models to answer questions about the passages.
Popular machine reading comprehension datasets include Stanford Question Answering Dataset
(SQuAD) (Rajpurkar et al., 2016) and SQuAD 2.0 (Rajpurkar et al., 2018) which consist of hun-
dreds of thousands of Wikipedia-based question-answer pairs. The answer to every question is an
extractive span (a segment of text from the text passage). Other variants of machine reading com-
prehensiondatasetsrequiremodelstoanswerquestionsaboutnewsarticles(Trischleretal.(2017)’s
NewsQA), find and reason over multiple supporting documents to answer questions (Yang et al.
(2018)’s HotPotQA), or contain questions derived from Google search users’ queries (Kwiatkowski
et al. (2019)’s Natural Questions).
In contrast with our codebook task, machine reading comprehension questions are usually factoid
questions (general world knowledge) or extractive questions (a simple question whose answer is a
direct quote from the provided passage), not questions constrained by context-specific definitions
crafted by domain experts in codebooks. Our work builds on these NLP literatures, but is distin-
30

guished from previous work by our focus on codebook-specific constructs and requiring reasoning
over both long documents and long codebook instructions with many categories.
| C.2 | LLM Benchmarks |     |     |     |
| --- | -------------- | --- | --- | --- |
New generative LLMs, especially instruction tuned LLMs, are evaluated on a small set of widely
| used benchmark |     | datasets. |     |     |
| -------------- | --- | --------- | --- | --- |
MMLU(MassiveMultitaskLanguageUnderstanding,Hendrycksetal.(2021))asksmultiplechoice
questions covering a range of academic and professional domains. Good performance requires rea-
soning and knowledge, but the instructions/questions are concise and do not require reasoning over
| complex | instructions | or long passages, | as our task | requires. |
| ------- | ------------ | ----------------- | ----------- | --------- |
IFEval (Instruction-Following Evaluation, Zhou et al. (2023)) measures the ability of LLMs to
complywithveryspecificinstructionsabouttheiroutput(e.g.,limitingtheresponsetoasetnumber
of words, using bullet points in the response, answering only in lowercase, etc.). This benchmark is
ausefultestofLLMcompliance,whichweidentifyasakeylimitationforcurrentmodelsincarrying
outthecodebookmeasurementtask. However,thebenchmarkdoesnotevaluatetheabilityofLLMs
| to reason | over long, | detailed instructions | in the | face of ambiguity. |
| --------- | ---------- | --------------------- | ------ | ------------------ |
ARC (AI2 Reasoning Challenge, Clark et al. (2018)) asks multiple choice questions about grade-
school-levelscience,requiringsubjectmatterknowledgeandlimitedreasoning. However,itdoesnot
| require | the LLM | to interpret complex | instructions. |     |
| ------- | ------- | -------------------- | ------------- | --- |
GPQA(Graduate-LevelGoogle-ProofQ&Abenchmark,Reinetal.(2023))asksverydifficultques-
tions written by domain experts in STEM that are challenging even for PhDs in the field. They
require careful domain-specific reasoning, but the questions are relatively straightforward and do
| not require | long-context | reasoning. |     |     |
| ----------- | ------------ | ---------- | --- | --- |
ZeroScrolls (Shaham etal., 2023) is acollection of tasksthat requirereasoning overlong contexts,
including long document summarization and question-answering that involves multi-step reasoning
over multiple paragraphs. Long context reasoning is an important aspect of the codebook mea-
surement task, but our task also requires attention to long, complex instructions, which this set of
| evaluations | does | not directly measure. |     |     |
| ----------- | ---- | --------------------- | --- | --- |
Performance on math and coding benchmarks is less relevant to our codebook measurement tasks
31

and we omit a discussion of the standard benchmarks here.
D Further illustration of codebook-LLM measurement
Here, we provide a second example to motivate the codebook-LLM measurement tasks. Asking
an LLM to label whether a news story describes a “protest” invites potential measurement prob-
lems. While all definitions of protests include a shared core (claim-making or demands for political
or social change outside of formal political channels), specific projects use different definitions of
protests, categorize protests at varying levels of granularity, and apply different exclusion criteria.
For example, the BFRS dataset on political violence in Pakistan (Bueno de Mesquita et al., 2015)
excludes all non-violent protests, while making a distinction between a “riot” and a “violent po-
litical demonstration”. In contrast, the common automated event data ontology CAMEO (Gerner
et al., 2002) collapses these two into a single “riot” category, while also coding other non-violent
protest tactics. CAMEO excludes resignations and complaints by elites as a form of protest, while
the Electoral Contestation and Violence (ECAV) dataset (Daxecker et al., 2019), which focuses ex-
clusively on subnational protests in the context of elections, includes these as protests. Applying
these different operationalizations of “protest” to the same corpus should not produce the same
measurements.
D.1 Dataset preprocessing
We make several changes to the original datasets as part of our preprocessing pipeline. The original
news stories used to code the BFRS dataset from the English-language Dawn newspaper in Pak-
istan were not obtainable. Instead, we rely on the short, free-text English language summary of
the event written by annotators that is provided in the structured BFRS dataset. In most cases,
using the hand-written summary makes the task easier, as the summary focuses on the main event
corresponding to the gold-standard label.5
TheCCCdatasetprovideshyperlinkstothesourcesusedtocodeeachevent.6 Weobtaintheoriginal
English language source text using a scraper provided by (Halterman & Radford, 2021). To make
the dataset comparable to the other two datasets, we limit their corpus to events that have (1) a
5Insomecases,thesummaryomitsdetailsthatarenecessaryfordeterminingthetruelabel. However,inTable5,
wefindthisisnotamajorconcerninpractice;only4%ofourBFRSsamplelackedthenecessarycontext.
6https://github.com/nonviolent-action-lab/crowd-counting-consortium
32

single event type, and (2) a single news source. Omitting stories with multiple event types yields a
single-label classification task that matches the other two datasets, while limited to events with a
single source avoids the need for the LLM to perform a challenging cross-document inference task.
We also omit events where the original text is not obtainable via the scraper.
We obtain the labeled Manifesto quasi-sentences from the Manifesto Project through their API7.
In total, the Manifesto Project provides more than 1 million labeled quasi-sentences across several
dozenlanguages. TheManifestoProjectemploysalargeteamofextensivelytrainednativelanguage
speakers to annotate each quasi-sentence in each manifesto (Merz et al., 2016). For this work, we
use a sample of 13 manifestos from English-speaking countries.
BFRS and CCC both label standalone, complete news stories, while Manifesto passages are often
sub-sentence fragments (quasi-sentences). Prototype manual analysis of LLM errors revealed that
identifying the correct label for some Manifesto passages was impossible without context from the
preceding passes. Thus, in our empirical pipeline, we input the Manifestos’ target quasi-sentence
(which is labeled) as well as the quasi-sentence just prior to the target one as context.
D.2 Contamination insulation
Contaminationofevaluationdatasets—whenanevaluationdatasetispartoftheLLMstrainingdata
andthusdoesnotadequatelyrepresentgeneralizationperformanceonanunseensetofexamples—isa
majorconcerninNLPresearch(Balloccuetal.,2024;Changetal.,2023;Golchin&Surdeanu,2024;
Li & Flanigan, 2024, inter alia). We believe that our datasets are insulated from contamination,
thatis,theyareunlikelytoappearintheircompleteforminLLMpre-trainingorinstructiontuning
data. The BFRS dataset is not available online and was provided directly to us by the authors
of the dataset. The structured CCC dataset includes hyperlinks to the sources used, but not the
raw text. Instead, we scrape the original news stories, where available, and combine them with the
structureddata. TheManifestocorpusisthemostatriskoftrainingcontamination,thoughwenote
that it has the lowest performance (see below). The original manifestos and the Manifesto Project
codebook (Version 2020a from July 22, 2020) are available on the internet and likely to present in
the LLM pre-training data, but the sentence-level annotations are provided through an API that
requires registration.
7urlhttps://manifesto-project.wzb.eu/information/documents/api
33

|     | Class         |     | Precision |      | Recall F1-score | Support |      |
| --- | ------------- | --- | --------- | ---- | --------------- | ------- | ---- |
|     | CARAVAN       |     |           | 0.17 | 0.50            | 0.25    | 2    |
|     | DEMONSTRATION |     |           | 0.02 | 0.18            | 0.04    | 17   |
|     | MARCH         |     |           | 0.60 | 0.22            | 0.32    | 109  |
|     | PROTEST       |     |           | 0.77 | 0.79            | 0.78    | 647  |
|     | RALLY         |     |           | 0.61 | 0.41            | 0.49    | 232  |
|     | Macro avg     |     |           | 0.35 | 0.34            | 0.32    | 1009 |
|     | Weighted      | avg |           | 0.70 | 0.63            | 0.65    | 1009 |
Table SI 1: Zero-shot performance of Mistral-7B on the development set of CCC (new codebook
| format). Here, | “support” | is the number | of      | examples | in the development | set. |     |
| -------------- | --------- | ------------- | ------- | -------- | ------------------ | ---- | --- |
| E Detailed     | zero-shot |               | results |          |                    |      |     |
In Tables SI 1, SI 2, and SI 3, we provide per-class performance and support information for the
three datasets in the zero-shot condition. For space, we include only results for Mistral-7B.
| F LLM | details |     |     |     |     |     |     |
| ----- | ------- | --- | --- | --- | --- | --- | --- |
Here, we provide greater justification of our choice of the four LLMs we examine, along with other
parameters we experimented with. Because the landscape and performance of LLMs is constantly
changing, we select four well performing open-weight LLMs between 7 billion and 12 billion pa-
rameters. Our purpose in the paper is to demonstrate our framework for using and evaluating
LLMs to conduct codebook-based measurement. We want to ensure that our framework is general-
izable to multiple models, but we re-emphasize that our objective is not to identify a single “best”
LLM.
We intentionally choose“local” LLMs, whose weights can be downloaded to a local machine and
updated. In our conception, “local” involves both open weights, but also a model small enough to
run on a commodity GPU. Others have emphasized the importance of local models for scientific
researchandhowlocalmodelsarereproducibleinawaythat“closed”, API-basedmodelswhichare
constantly changing and do not have version control (e.g., ChatGPT) are not (Palmer et al., 2024;
Rogers, 2023; Spirling, 2023). (See SI Section F for a detailed discussion of the “open” terminology
and other models we considered). A local weight model is also required in order to further train the
| model, as we | do. |     |     |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- | --- |
We use the following LLMs in the main text. All are instruction tuned or “chat” versions. We
34

| Class             |            |             |                |          | Precision |      | Recall | F1-score |      | Support |      |
| ----------------- | ---------- | ----------- | -------------- | -------- | --------- | ---- | ------ | -------- | ---- | ------- | ---- |
| AGRICULTURE       |            | POSITIVE    |                |          |           | 0.75 |        | 0.07     | 0.13 |         | 42   |
| ANTI-GROWTH       |            | ECONOMY     |                | POSITIVE |           | 0.00 |        | 0.00     | 0.00 |         | 8    |
| ANTI-IMPERALISM   |            |             |                |          |           | 0.00 |        | 0.00     | 0.00 |         | 1    |
| CIVIC             | MINDEDNESS |             | POSITIVE       |          |           | 0.00 |        | 0.00     | 0.00 |         | 9    |
| CONSTITUTION      |            | NEGATIVE    |                |          |           | 0.00 |        | 0.00     | 0.00 |         | 7    |
| CONSTITUTION      |            | POSITIVE    |                |          |           | 0.25 |        | 1.00     | 0.40 |         | 1    |
| CONTROLLED        |            | ECONOMY     |                |          |           | 0.00 |        | 0.00     | 0.00 |         | 4    |
| CORPORATISM/MIXED |            |             | ECONOMY        |          |           | 0.00 |        | 0.00     | 0.00 |         | 1    |
| CULTURE           | POSITIVE   |             |                |          |           | 0.75 |        | 0.28     | 0.41 |         | 32   |
| DECENTRALISATION  |            |             |                |          |           | 0.36 |        | 0.13     | 0.19 |         | 31   |
| DEMOCRACY         |            |             |                |          |           | 0.20 |        | 0.25     | 0.22 |         | 55   |
| ECONOMIC          |            | GOALS       |                |          |           | 0.00 |        | 0.00     | 0.00 |         | 13   |
| ECONOMIC          |            | GROWTH      | POSITIVE       |          |           | 0.33 |        | 0.11     | 0.17 |         | 36   |
| ECONOMIC          |            | ORTHODOXY   |                |          |           | 0.00 |        | 0.00     | 0.00 |         | 19   |
| ECONOMIC          |            | PLANNING    |                |          |           | 0.00 |        | 0.00     | 0.00 |         | 1    |
| EDUCATION         |            | NEGATIVE    |                |          |           | 0.00 |        | 0.00     | 0.00 |         | 1    |
| EDUCATION         |            | POSITIVE    |                |          |           | 0.52 |        | 0.47     | 0.49 |         | 62   |
| ENVIRONMENTALISM  |            |             | POSITIVE       |          |           | 0.54 |        | 0.30     | 0.38 |         | 94   |
| EQUALITY          | POSITIVE   |             |                |          |           | 0.58 |        | 0.12     | 0.20 |         | 92   |
| EUROPE            | NEGATIVE   |             |                |          |           | 0.25 |        | 0.40     | 0.31 |         | 5    |
| EUROPE            | POSITIVE   |             |                |          |           | 0.10 |        | 0.69     | 0.18 |         | 13   |
| FOREIGN           | SPECIAL    |             | POSITIVE       |          |           | 0.13 |        | 1.00     | 0.23 |         | 13   |
| FREEDOM           | AND        | HUMAN       |                | RIGHTS   |           | 0.08 |        | 0.03     | 0.04 |         | 40   |
| FREE              | MARKET     | ECONOMY     |                |          |           | 0.50 |        | 0.20     | 0.29 |         | 5    |
| GOV-ADMIN         |            | EFFICIENCY  |                |          |           | 0.08 |        | 0.72     | 0.14 |         | 39   |
| INCENTIVES        |            |             |                |          |           | 0.00 |        | 0.00     | 0.00 |         | 24   |
| INTERNATIONALISM  |            |             | NEGATIVE       |          |           | 0.00 |        | 0.00     | 0.00 |         | 2    |
| INTERNATIONALISM  |            |             | POSITIVE       |          |           | 0.13 |        | 0.32     | 0.18 |         | 44   |
| LABOUR            | GROUPS     |             | POSITIVE       |          |           | 0.29 |        | 0.17     | 0.22 |         | 29   |
| LAW AND           | ORDER      |             | POSITIVE       |          |           | 0.61 |        | 0.25     | 0.35 |         | 57   |
| MARKET            | REGULATION |             |                |          |           | 0.00 |        | 0.00     | 0.00 |         | 54   |
| MIDDLE            | CLASS      | AND         | PROF.          | GROUPS   |           | 0.67 |        | 1.00     | 0.80 |         | 2    |
| MILITARY          | NEGATIVE   |             |                |          |           | 0.00 |        | 0.00     | 0.00 |         | 3    |
| MILITARY          | POSITIVE   |             |                |          |           | 0.59 |        | 0.53     | 0.56 |         | 19   |
| MINORITY          | GROUPS     |             |                |          |           | 0.00 |        | 0.00     | 0.00 |         | 15   |
| MULTICULTURALISM  |            |             | NEGATIVE       |          |           | 0.00 |        | 0.00     | 0.00 |         | 3    |
| MULTICULTURALISM  |            |             | POSITIVE       |          |           | 0.00 |        | 0.00     | 0.00 |         | 14   |
| NATIONALISATION   |            |             |                |          |           | 0.00 |        | 0.00     | 0.00 |         | 7    |
| NATIONAL          | WAY        | OF          | LIFE           | NEGATIVE |           | 0.00 |        | 0.00     | 0.00 |         | 4    |
| NATIONAL          | WAY        | OF          | LIFE           | POSITIVE |           | 0.28 |        | 0.39     | 0.33 |         | 18   |
| NON-ECONOMIC      |            | DEMOGRAPHIC |                | GROUPS   |           | 0.20 |        | 0.03     | 0.05 |         | 33   |
| PEACE             |            |             |                |          |           | 0.24 |        | 0.50     | 0.32 |         | 8    |
| POLITICAL         | AUTHORITY  |             |                |          |           | 0.19 |        | 0.07     | 0.10 |         | 44   |
| POLITICAL         | CORRUPTION |             |                |          |           | 0.00 |        | 0.00     | 0.00 |         | 6    |
| PROTECTIONISM     |            |             | NEGATIVE       |          |           | 0.00 |        | 0.00     | 0.00 |         | 9    |
| PROTECTIONISM     |            |             | POSITIVE       |          |           | 1.00 |        | 0.17     | 0.29 |         | 6    |
| TECHNOLOGY        |            | AND         | INFRASTRUCTURE |          |           | 0.17 |        | 0.07     | 0.10 |         | 72   |
| TRADITIONAL       |            | MORALITY    |                | NEGATIVE |           | 0.00 |        | 0.00     | 0.00 |         | 4    |
| TRADITIONAL       |            | MORALITY    |                | POSITIVE |           | 0.00 |        | 0.00     | 0.00 |         | 7    |
| WELFARE           | NEGATIVE   |             |                |          |           | 0.00 |        | 0.00     | 0.00 |         | 2    |
| WELFARE           | POSITIVE   |             |                |          |           | 0.30 |        | 0.36     | 0.33 |         | 136  |
| Macro             | avg        |             |                |          | 35        | 0.18 |        | 0.17     | 0.13 |         | 1732 |
| Weighted          | avg        |             |                |          |           | 0.22 |        | 0.16     | 0.15 |         | 1732 |
TableSI2: Zero-shotperformanceofMistral-7BonthedevelopmentsetofManifestos(newcodebook
| format). | Here, “support” |     | is the | number of examples | in  | the development |     | set. |     |     |     |
| -------- | --------------- | --- | ------ | ------------------ | --- | --------------- | --- | ---- | --- | --- | --- |

| Class         |               |              |               |               | Precision |      | Recall F1-score |      | Support |      |
| ------------- | ------------- | ------------ | ------------- | ------------- | --------- | ---- | --------------- | ---- | ------- | ---- |
| ASSASSINATION |               |              |               |               |           | 0.90 | 0.52            | 0.66 |         | 1433 |
| ATTACK        | ON STATE      |              |               |               |           | 0.60 | 0.95            | 0.73 |         | 192  |
| CONVENTIONAL  |               | ATTACK       |               | ON GOV FORCES |           | 0.19 | 0.84            | 0.31 |         | 152  |
| DRONE         | ASSASSINATION |              |               |               |           | 0.93 | 1.00            | 0.97 |         | 43   |
| GOV ATTACK    |               | ON CIVILIANS |               |               |           | 0.09 | 0.47            | 0.15 |         | 90   |
| GOV ATTACK    |               | ON NONSTATE  |               | COMBATANTS    |           | 0.03 | 0.01            | 0.02 |         | 181  |
| GUERRILLA     | ATTACK        |              | ON GOV        | FORCES        |           | 0.31 | 0.12            | 0.17 |         | 199  |
| OTHER         |               |              |               |               |           | 0.20 | 0.28            | 0.24 |         | 291  |
| RIOT          |               |              |               |               |           | 0.83 | 0.33            | 0.47 |         | 443  |
| TERRORISM     |               |              |               |               |           | 0.80 | 0.37            | 0.51 |         | 872  |
| THREAT        | OF VIOLENCE   |              |               |               |           | 0.37 | 0.53            | 0.44 |         | 30   |
| VIOLENT       | POLITICAL     |              | DEMONSTRATION |               |           | 0.69 | 0.86            | 0.76 |         | 567  |
| Macro         | avg           |              |               |               |           | 0.35 | 0.37            | 0.32 |         | 4495 |
| Weighted      | avg           |              |               |               |           | 0.69 | 0.49            | 0.53 |         | 4495 |
Table SI 3: zero-shot performance of Mistral-7B on the development set of BFRS (new codebook
| format). | Here, “support” |     | is the    | number of examples | in the | development | set. |     |     |     |
| -------- | --------------- | --- | --------- | ------------------ | ------ | ----------- | ---- | --- | --- | --- |
| obtained | the weights     | for | each from | Huggingface.       |        |             |      |     |     |     |
Mistral-7B
WeuseMistral7BInstructv0.2forboththezero-shotandinstructiontuning(Jiang&etal.,2023).
Mistral’s weights can downloaded and can be run on a commodity GPU, fulfilling the requirements
wesetforreproducibilityandmodelaccess. Atthetimewebeganrunningourexperiments,Mistral
7B Instruct was considered one of the “best” 7B open weight LLMs available. It outperformed
both Llama2-7b and Llama2-13b on most important benchmarks, including MMLU, HellaSwag,
and Winograd and outperformed all other 7b models on MT-Bench (Jiang & et al., 2023). In both
conditions, we apply a 4 bit quantization to the model to enable the use of a consumer-grade GPU
| for both         | inference | and training.                                             |     |     |     |     |     |     |     |     |
| ---------------- | --------- | --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| Link to weights: |           | https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2 |     |     |     |     |     |     |     |     |
OLMo-7B
WeusetheinstructiontunedversionofOLMo-7BasanLLM,primarilybecauseitismuchmorefully
documentedthanotherLLMs(Groeneveldetal.,2024). OLMo’strainingdata,trainingparameters,
and logs are available, making it a useful LLM for academic research into LLMs.
| Link to weights: |     | https://huggingface.co/allenai/OLMo-7B-Instruct-hf |     |     |     |     |     |     |     |     |
| ---------------- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
36

Mistral-NeMo-12B
We consider one larger model, Mistral’s NeMo model with 12 billion parameters (AI, 2024). NeMo
hasalargercontextwindowthanMistral-7B(128,000)tokens,animprovedtokenizer,andimproved
instruction tuning. However, details about the training data, training parameters, and instruction
tuning step are not disclosed.
Link to weights: https://huggingface.co/mistralai/Mistral-Nemo-Instruct-2407
Llama-8B
Finally, we use Llama 3.1 8B (Meta, 2024), an 8B open weight model from Meta. Version 3.1 offers
improved instruction following capabilities and a larger context window than the original Llama 3
models.
Link to weights: https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct
Otherdetails. Wenotethatlocalmodelsarestillnot“open”modelsinthatlocalmodeldevelopers
may still withhold details about the model’s training data or training conditions (Groeneveld et al.,
2024). For example, we still have limited information on the nature of the training data in Mistral
7BInstruct. ThemostdetaileddescriptionfromJiangandetal.(2023)is“wefinetuned[Mistral7B]
on instruction datasets publicly available on the Hugging Face repository. No proprietary data or
training tricks were utilized [...]” However, we believe the performance advantage of “open weight”
models over fully open source models makes the trade-off worth their lack of full information about
training details.
We experimented with Llama 2 and Phi-3 earlier in the project but had preliminary evidence that
they were less accurate than Mistral.
EarlierLLMshadacontextwindowshorterthanourcodebook+textinput,soweinitiallyposedthe
taskasasetofbinaryclassificationtasks: givenadocumentandasinglelabelanddefinitionfromthe
codebook,inferwhetherprovidedlabelappliestothedocument. However,thiswascomputationally
expensiveand rapidimprovementsinLLM contextwindow sizenow makeit possible toprovide the
entire codebook at once. As we discuss in the main text, we also believe that binary classification is
not a fruitful approach: selecting the best category depends on reading all categories to understand
the boundaries between them.
37

Weexperimentedearlierintheprojectwithconstrainedgeneration,biasingtheLLM’stokenproba-
bilitiestotokensthatappearintheprompt,toreducelabelhallucination. Wefoundveryslightgains
on Manifestos and no gains on CCC and BFRS, and leave a deeper exploration of this technique for
future work.
G Instruction tuning details
According to Wang et al. (2023), “Instruction datasets targeted at specific domains and/or capa-
bilities are extremely effective at improving model performance in those aspects.” If this statement
holds true, it lends to the hypothesize that instruction tuning on many social science codebook
datasets will also lead to improved performance.
Wheninstructionfinetuningontheseinput-outputpairs, amodel’slanguagemodelinglossfunction
can either be computed from both the input and output or the output only. Some research shows
that computing the loss on both input and output improves performance (Shi et al., 2024), while
others only compute the loss on only output (Wang et al., 2023). We opt for the latter and mask
thelossfortheinputandonlyupdateweightsviathelosscomputedontheoutput. Doingsospeeds
the training, and we hypothesize that it may improve cross-domain generalizability.
Unlike Wang et al. (2023), our training does not include teacher forcing, when a model generating a
sequence of tokens conditions on the gold-standard tokens instead of the token generated by model
from the previous time steps. Teacher forcing has been shown to be important on long generative
texts but our desired gold-standard labels are just a few tokens long and an error on the first
generated token means the LLM has already mis-predicted the label.
LoRA models have three main hyperparameters–the rank, the scaling factor α, and which layers to
update. The rank determines the size of the row-rank weight matrices. Lower rank approximations
aremoreefficientandinvolvetuningfewerparameters,whilehigherrankLoRAsallowformoreflex-
ibility, but at greater computational and storage cost and risk of overfitting. The scaling parameter
α affects how much weight the LoRA weights get when multiplied with the original weight matrix.
Guidance on how to select the α parameter is mixed–common advice is to select a value that is one
half, the same, or twice the value of the rank (Raschka, 2024a).
The original LoRA paper tunes only the query and value components of the attention (Hu et al.,
38

2022). However, recent research has shown that tuning all weights in the LLM can improve per-
formance over only tuning part of the attention weights, albeit at increased computational cost
| (Raschka, | 2024b). |     |     |     |
| --------- | ------- | --- | --- | --- |
We initially experimented with varying each of these hyperparameters. In our initial experiments,
usingarankof16(withα=rank)andupdatingallweightsperformedbest,albeitwithinconsistent
results. In the main text, we report only experiments with these hyperparameters and leave further
| exploration | of the hyperparameters |     | for future work. |     |
| ----------- | ---------------------- | --- | ---------------- | --- |
We also leave for future work cross-codebook performance. That is, does instruction tuning on one
dataset improve performance on a second dataset that was not seen during training? Improvements
in performance over the zero-shot baseline would indicate the model has an improved, generalizable
ability to conduct codebook-LLM measurement. Decreased performance would indicate instead
that the model has overfit to the dataset seen during training and has not learned a generalizable
| codebook-following | ability. |     |     |     |
| ------------------ | -------- | --- | --- | --- |
| H Prompt           | Example  |     |     |     |
Example complete zero-shot prompt for BFRS showing the Llama2-style special instruction tokens
for Mistral 7B instruct. The special <s> token is applied during tokenization.
[INST]
<<SYS>>
Instructions: You’re an expert political scientist categorizing news stories from Pakistan
into categories. Carefully read the definitions below, read the story, and write the
| Label      | that best    | matches the | story. Use only | the provided labels. |
| ---------- | ------------ | ----------- | --------------- | -------------------- |
| Task Type: | single label | multiclass  |                 |                      |
<</SYS>>
Categories:
| Category: | assassination |     |     |     |
| --------- | ------------- | --- | --- | --- |
Label: ASSASSINATION
Definition: An attempt (successful or failed) by a non-state entity aimed to kill a
| specific | individual. |     |     |     |
| -------- | ----------- | --- | --- | --- |
39

Clarification: Targets may include military, political, civil society or civilian state or
federal leadership. In some case, there may be a suspected government agency behind the
assassination. This Label applies when a body is found with bullet wounds or other
| marks of | violence and/or | torture. |     |     |
| -------- | --------------- | -------- | --- | --- |
Negative Clarification: Does not include assassination using drone attacks (coded
separately) or deaths from attacks on military, paramilitary, police or intelligence
| targets, | or state violence | against | a group of civilians. |     |
| -------- | ----------------- | ------- | --------------------- | --- |
Positive Example: ""An Imam of a mosque was brutally murdered by unknown assailants in
Jehanian on Friday."" This is an ASSASSINATION because the imam appears to have been
| deliberately | targeted. |     |     |     |
| ------------ | --------- | --- | --- | --- |
Negative Example: ""A woman and her son were injured by unidentified assailants in
Mominabad on Sunday."" This is an example of TERRORISM, not ASSASSINATION, because the
| attack                  | does not appear | to be specifically | targeted | at the victims. |
| ----------------------- | --------------- | ------------------ | -------- | --------------- |
| Category: assassination |                 | (drone attack)     |          |                 |
Label: DRONE_ASSASSINATION
Definition: An assassination (failed or successful attempt) carried out using an unmanned
| aerial | vehicle (drone | strike). |     |     |
| ------ | -------------- | -------- | --- | --- |
Negative Clarification: Non-drone assassination attempts are coded under the ‘Assassination
| ’ category, | not under | this category. |     |     |
| ----------- | --------- | -------------- | --- | --- |
Positive Example: ""Drone fired missiles at a heavily fortified mud-house in Asoray Village
in the Mirali sub-division kiliing 5 people and injuring 1.;a senior Al Qaeda
| commander, | Hamza Rabia, | was killed | in the attack"" |     |
| ---------- | ------------ | ---------- | --------------- | --- |
Negative Example: ""Two soldiers were injured in a bomb blast near an army outpost in the
| Hamrang          | area."" No | mention of a | drone strike. |     |
| ---------------- | ---------- | ------------ | ------------- | --- |
| Category: attack | on state   |              |               |     |
Label: ATTACK_ON_STATE
Definition: An attack on Pakistani territory targeted at the state of Pakistan or its
representatives that was conducted by the armed forces of another state. This includes
shelling across the Line of Control, attacks on Pakistani forces mistaken for militants
| near the | Afghan border. |     |     |     |
| -------- | -------------- | --- | --- | --- |
Clarification: All these incidents were attributed to the government of India or United
40

| States and NATO | forces. |     |     |     |
| --------------- | ------- | --- | --- | --- |
Positive Example: ""Indian forces resorted to machine gun firing across the LoC in what the
Pakistani officials termed a clear violation of the ceasefire."" This is an example of
| another state’s | military | conducting | an attack | on Pakistan. |
| --------------- | -------- | ---------- | --------- | ------------ |
Negative Example: ""Five rockets were fired at a Frontier Corps checkpost in Sangsilla
Chashma area of Pir Koh."" Not attributable to the armed forces of another state.
Category: conventional attack on military/paramilitary/police/intelligence
Label: CONVENTIONAL_ATTACK_ON_GOV_FORCES
Definition: Incidents that involve a direct conventional attack on a military, police,
paramilitary, or intelligence target, such that violence has the potential to be
| exchanged between | the attackers. |     |     |     |
| ----------------- | -------------- | --- | --- | --- |
Clarification: Conventional tactics are those that would be employed by state forces.
Conventional attacks include ambushes, direct fire, artillery, pitched battle, and
troop captures. This includes but is not limited to: attacks against military
checkposts, police headquarters, the Federal Investigative Agency (FIA), the ISI.
Negative Clarification: ‘‘Guerilla" tactics are described in a separate category. Attacks
| by state actors | (e.g. India) | are | coded as ‘‘attack | on state" |
| --------------- | ------------ | --- | ----------------- | --------- |
Positive Example: ""At least two security personnel were injured in skirmishes between
security forces and armed tribesmen. The attackers escaped after security forces
retaliated using gunfire. No arrest was reported."" Skirmishes involving gunfire is a
| conventional | attack. |     |     |     |
| ------------ | ------- | --- | --- | --- |
Negative Example: ""A vehicle carrying security personnel hit a landmine in Loti gas field
area resulting in injuries to three soldiers."" This is a guerilla attack because it
| involves a road-side | bomb.     |                                           |     |     |
| -------------------- | --------- | ----------------------------------------- | --- | --- |
| Category: guerilla   | attack on | military/paramilitary/police/intelligence |     |     |
Label: GUERILLA_ATTACK_ON_GOV_FORCES
Definition: Incidents that involve a guerilla-like attack (e.g., a car or suicide-bombing,
a kidnapping) on a military, police, paramilitary, or intelligence target.
Clarification: Guerilla attacks employ tactics that conventional forces do not. For example
, guerilla attacks will employ road-side bombs, improvised explosive devices (IEDs),
| suicide attacks | (e.g. on | a checkpoint), | car bombs | and the like. |
| --------------- | -------- | -------------- | --------- | ------------- |
41

Negative Clarification: Gun battles between soldiers and militants are coded as
| conventional | attacks. |     |     |     |     |
| ------------ | -------- | --- | --- | --- | --- |
Positive Example: ""A suicide bomber blew himself up in an army training area in Guliana
near Kharian cantonment, where the soldiers were busy training."" Suicide attacks are
| examples of | guerilla attacks. |     |     |     |     |
| ----------- | ----------------- | --- | --- | --- | --- |
Negative Example: ""Mewind Rifles received information about the presence of militants in
the area. When security forces reached there, militants started firing."" This
describes a conventional battle between militants and state forces and is thus not a
| guerilla attack.                       |     |        |              |            |     |
| -------------------------------------- | --- | ------ | ------------ | ---------- | --- |
| Category: military/paramilitary/police |     | attack | on non-state | combatants |     |
Label: GOV_ATTACK_ON_NONSTATE_COMBATANTS
Definition: Violence initiated by state (federal or provincial) combatants against
| combatant | non-state, sub-national | groups, | or clandestine | agents. |     |
| --------- | ----------------------- | ------- | -------------- | ------- | --- |
Clarification: Includes attacks by the US and NATO on militants in Pakistan that involve
manned aircraft or artillery systems. For example, these may be brief episodes such as
the Pakistan Army and Police assault on the Lal Masjid OR they may be sustained as the
army offensive in South Waziristan in 2011 or the Frontier Corps in Aurakzai.
| Negative Clarification: | drone attacks | have their | own category |     |     |
| ----------------------- | ------------- | ---------- | ------------ | --- | --- |
Positive Example: ""In a continuation of the crackdown on militants by the army, four more
| militants | were killed."" State | forces attacked | non-state | armed | actors. |
| --------- | -------------------- | --------------- | --------- | ----- | ------- |
Negative Example: ""A personnel of the Balochistan Reserve Police was injured when some
armed men opened indiscriminate fire on them which they later returned."" This is a non
| -state attack                          | on state forces, | so this label | does not | apply. |     |
| -------------------------------------- | ---------------- | ------------- | -------- | ------ | --- |
| Category: military/paramilitary/police |                  | selective     | violence |        |     |
Label: GOV_ATTACK_ON_CIVILIANS
Definition: Violence initiated by state (federal or provincial) combatants against
civilians.
Clarification: These may include incidents where a newspaper reports that a political
activist is picked up by the intelligence services and detained and beaten overnight.
Negative Clarification: Does not include attacks on combatants or violence in the context
of a protest.
42

Positive Example: ""Advocate Ghulam Nabi of the Peshawer High Court was allegedly picked up
by personnel of an intelligence agency in three vehicles near the NWFP assembly, and
released after a severe over night thrashing. He is associated with Jamaat-i-Islami and
a critic of the army and intelligence agencies.""
Negative Example: ""The police baton charged lawyers and other political activists as they
tried to enter the city in order to join the throng of people outside the Supreme Court
who were there supporting the sacked Chief Justice. Hundereds of people tried entering
Islamabad for the purpose, which the police tried to stop by baton-charging the crowd
."" This violence takes place in the context of a protest, and thus should get the
label ""violent political demonstration"".
Category: riot
Label: RIOT
Definition: A riot is a violent clash between two or more sizeable groups or when a single
informally assembled crowd becomes violent.
Clarification: Neither group can be a state force. However, if there are two or more
clashes around a single event in which the police are involved, then it would be a
classified as a riot.
Negative Clarification: For example, the students of the Lal Masjid versus the police would
not be considered a riot, it would be a Violent Political Demonstration.
Positive Example: ""Five workers of the Muslim Students Federation, the student wing of the
ruling Muslim conference, sustained bullet wounds in a clash with the activists of pro
-independence National Students Federation.""
Negative Example: ""An angry mob thrashed police personnel, accusing them of manhandling
people and using obscene language when they (the police) raided a gambling den."" This
incident involves police, so it is coded as a ""violent political demonstration.""
Category: terrorism
Label: TERRORISM
Definition: Premeditated, politically motivated violence perpetrated against noncombatant
targets by subnational groups or clandestine agents (22 U.S.C. \S 2656f(d)(2)).
Positive Example: ""Security forces foiled an attempt to blow up a 12-inch diameter gas
pipeline in Sui tehsil."" Even though this attack was unsuccessful, it still involved
43

| an attack | by non-state | groups on | non-combatant | targets. |
| --------- | ------------ | --------- | ------------- | -------- |
Negative Clarification: In contrast, an attack on a police check point is not considered to
be terrorism even if civilians are harmed in the conduct of the attack provided that
the primary target was the check point. This is coded as an attack on police,
paramilitary or military target. The intended targets of the attacks is key. A targeted
attack on a specific figure is an instance of assassination, not terrorism.
Negative Example: ""The grandson of Mohmand Agency MNA Maulana Ghulam Mohammad Sadiq was
killed when gunmen entered his house and opened fire."" The attack seems directed at a
specific prominent person, so even though it’s carried out by non-state actors, it
| should be        | coded as an | assassination, | not terrorism. |     |
| ---------------- | ----------- | -------------- | -------------- | --- |
| Category: threat | of violence |                |                |     |
Label: THREAT_OF_VIOLENCE
Definition: Incidents in which the threat of violence is reported as being used for
| political | purposes. |     |     |     |
| --------- | --------- | --- | --- | --- |
Clarification: A typical example is when a spokesman for a banned militant group threatens
attacks if certain policy changes were not made, or when a party spokesman threatens
violent protest if certain changes are not made. This also includes incidents in which
| a particular | individual | is threatened. |     |     |
| ------------ | ---------- | -------------- | --- | --- |
Positive Example: ""The President of the All Pakistan Clerks Association...alleged that he
| had received | a phone | call warning | him of an | explosion at his house."" |
| ------------ | ------- | ------------ | --------- | ------------------------- |
Negative Example: ""A man killed his cousin, accusing her of having illicit relations with
a youth of the same village."" This is an instance of violence actually being carried
| out, not          | a threat of | violence.     |     |     |
| ----------------- | ----------- | ------------- | --- | --- |
| Category: violent | political   | demonstration |     |     |
Label: VIOLENT_POLITICAL_DEMONSTRATION
Definition: A violent political demonstration is characterized as mobilization of crowds in
| response | to a political | event that | at some | point becomes violent. |
| -------- | -------------- | ---------- | ------- | ---------------------- |
Clarification: Violence may be initiated by the crowd or by the police upon the crowd.
Negative Clarification: A violent clash between two non-state groups is a riot, not a
| violent political | demonstration. |     |     |     |
| ----------------- | -------------- | --- | --- | --- |
Positive Example: ""Hundreds of school children and armed supporters of Lashkar-i-Islam
44

stormed the Bara bazaar and set the main tehsil, Qambaraband, Al Haaj Market, Sheikhan
and Qasaban checkposts of the Khasadar force on fire. The Lashkar-i-Islam had warned
| of protests | if  | their | demands | were | not met."" |     |     |     |
| ----------- | --- | ----- | ------- | ---- | ---------- | --- | --- | --- |
Negative Example: ""A man killed and his brother injured when they were attacked by their
rivals over a land dispute."" The motivation here is not a political event, thus this
| event     | is a riot, | not | a violent | political |     | demonstration. |     |     |
| --------- | ---------- | --- | --------- | --------- | --- | -------------- | --- | --- |
| Category: | other      |     |           |           |     |                |     |     |
Label: OTHER
Definition: Incidents that are not easily categorized such as people being hurt by
| unexploded | ordnance |     | or when | the | source of | the violence | is  | unclear. |
| ---------- | -------- | --- | ------- | --- | --------- | ------------ | --- | -------- |
Clarification: An event that does not fit into the other categories (assassination, attack
on state, conventional attack on military/paramilitary/police/intelligence, guerilla
attack on military/paramilitary/police/intelligence, military/paramilitary/police
| selective | violence) |     | should | be coded | as OTHER. |     |     |     |
| --------- | --------- | --- | ------ | -------- | --------- | --- | --- | --- |
Positive Example: ""A man allegedly opened fire on his wife while she was offering prayers,
and later proceeded to kill his brother on the pretext that his wife and his brother
| had illicit | relations. |     | He  | then escaped."" |     |     |     |     |
| ----------- | ---------- | --- | --- | --------------- | --- | --- | --- | --- |
Negative Example: ""A suicide bomber blew himself up in an army training area in Guliana
| near Kharian  |     | cantonment, |       | where the      | soldiers | were busy | training."" |     |
| ------------- | --- | ----------- | ----- | -------------- | -------- | --------- | ----------- | --- |
| The following | is  | a news      | story | from Pakistan. |          |           |             |     |
Document: A presiding officer was kidnapped allgedly by the supporters of a PML Q candidate
.
Write the name of the Label that fits best, with no other text. For example, ""Label:
| ASSASSINATION"", |     | ""Label: |     | VIOLENT_POLITICAL_DEMONSTRATION"", |     |     |     | etc. |
| ---------------- | --- | -------- | --- | ---------------------------------- | --- | --- | --- | ---- |
---------
[/INST]
Label: "
45

I Cross-codebook training
During instruction tuning, we also experimented with evaluating the instruction tuned LLM on previously
unseen codebooks, as well as training on multiple codebooks. We initially hypothesized that instruction
tuning, especially when masking the language modeling loss on the prompt, would yield a model that
could generalize to unseen codebooks. We anticipated that the benefits would be especially strong when
trainingonmultiplecodebooks. However,wefoundthatcross-codebookperformance,evenwhentrainingon
multiplecodebooks,wasquitepoor. OurapproachtoinstructiontuningMistral-7Bdoesnotseemtoyielda
modelwithimprovedcodebookcomplianceabilities,comparedtozero-shotperformance. Weinterpretthese
results as showing overfitting to the training codebook(s), rather than learning a generalizable codebook-
followingability. However,wehypothesizethatscalingthetrainingtomorecodebooks,restructuredintothe
consistent format we propose, could yield instruction tuned models with improved codebook measurement
performance.
J Manual analysis
Our manual analysis began with a exploratory annotation round. In the pilot annotation round, we sam-
pled roughly 50 errors on the Manifestos development set, which we used to develop the following six
mutually exclusive categories which we subsequently used to categorize the BFRS, CCC, and Manifestos
samples:
A. LLMcorrect. WeassignedthiscategorytheLLMgenerativeoutput(includingtheLLMexplanation)
and the parsed label from the output were correct.
B. Incorrect gold standard. We assigned this category if after inspection of the text, gold-standard
label (from the original annotators), and codebook, we disagreed with the gold-standard label.
C. Document error. We assigned this category if we determined something was wrong with the text
itself. Forexample,sometimesscrapingerrorsmeantpartofthetextwasmissingorthechunkoftext
given as input need more context (e.g., the Manifestos’ sub-sentences required more context than we
provided).
D. LLM non-compliance. We assigned this category if the LLM did not comply with the output
reminderintheprompt: “Writethenameofthelabelthatfitsbest,withnoothertext. Forexample,
[...]” Weborrowthecompliance/non-compliancelanguagefromAtrejaetal.(2024)whoalsoanalyzed
LLM non-compliance. In our work, this category includes instances for which an LLM hallucinated
a label or the LLM had more than one label in its output. We did not assign this category to when
46

the LLM outputted explanations despite the prompt specifying “no other text” since Mistral almost
always included an explanation.
E. LLM semantics/reasoning mistake. We assigned this category if the LLM was compliant with
the output reminder (i.e. outputted only a single label from the valid label set), but the label and/or
explanation were incorrect. Almost always, the mistaken label was due to semantics, reasoning,
and/orworldknowledge. Thiswasoneofthemostimportantcategoriesforusasitrevealssignificant
weaknesses in LLMs compiling with the codebook-contextual label assumption.
F. Other. This was our catch-all category for any other manual analyses that did not fit wihtin the
categories above. For example, if we determined there was sufficient ambiguity in the codebook
descriptions of the classes; if there was a parsing error on the model output8; ambiguity in the text
itself; or ambiguity in the label precedence.9
J.1 More details on the manual analysis.
Over-reliance on heuristics (also called short-cuts or spurious correlations in the literature) in other NLP
models besides LLMs has been a major concern of past work in NLP (Gardner et al., 2021; Gururangan
etal.,2018;McCoyetal.,2019,inter alia). Inourempiricalresults,lexicaloverlapheuristicsoccurbothin
correct and incorrect predictions.
In our manual analysis, we found several of the LLM correct predictions on Manifestos came from heavy
lexicaloverlapbetweentheinputtextandlabel. Forexample,theLLMcorrectlypredictedthelabelpeace
for the text “Plaid Cymru supports peaceful negotiations over destructive warfare” and correctly predicted
the label political corruption for the text “The EFF Government will end government corruption and
incompetence, which currently cost the State more than R30 billion per year.”
Original annotation and codebook quality remains a concern; we (the authors) disagreed with the gold-
standardlabelin4%, 10%and8%ofinstancesinoursamplesofBFRS,CCC,andManifestosrespectively.
We also identified some mismatches between LLM predictions and gold standard labels that result from
ambiguity in the codebook, especially in the CCC dataset. For instance, an event that involves a march
near the target of the action could be considered either a protest (a crowd gathering near the target of
their claims) or a march. In practice, the march label seems to take precedence over rally, protest, or
demonstration,butthecodebookisnotexplicitlyclearonthispoint.10 UsingLLMsaspartofaniterative
8For example, on a CCC instance the model output was “COUNTER PROTEST” and our deterministic parser
thanmarked“PROTEST”but“PROTEST”wasstilltheincorrectlabel.
9Forexample,inCCCdoesmarchtakeprecedenceoverrally?
10In practice, CCC allows multiple labels per story. Our sample of CCC stories include only stories for which a
singleeventwasidentified.
47

process of codebook development is a promising direction for future work (Section 10).
48

| K Lemon-picked |     | examples | from | manual error analysis |
| -------------- | --- | -------- | ---- | --------------------- |
D.LLMnon-compliance
| Dataset-Ex. | Text |     | GoldLabel | LLMoutput |
| ----------- | ---- | --- | --------- | --------- |
Manif.-1 Context:willpromotealearningand EDUCATION WELFAREPOSITIVE(orEDUCATIONPOSITIVE,
knowledgesocietybyadvancingtechnology, POSITIVE dependingonthespecificfocusoftheparty’smanifesto)
enhancingresearchandcreatingasociety Explanation:ThestatementfromtheSouthAfricanpolitical
withloveoflearningandengagedinsocietal party’smanifestoindicatesacommitmenttoimprovingfinancial
development;workwiththeUniversitiesand supportforuniversitystudentsfrompoorfamiliesand
otherInstitutesofHigherlearningtoimprove encouragingwork/studyopportunitiesforstudents.Thisaligns
theircoordinationwiththeFETsystemand withthe“Welfare”or“Education”categories,asthepartyis
thebusinesssectortoensurethattheir focusingonenhancingthequalityoflifeforstudentsby
graduateshavethekindofeducationthatis addressingtheirfinancialneedsandprovidingopportunitiesfor
relevanttotheneedsoftheeconomyand practicalexperience.The“Positive”labelisusedtoindicatethat
society; theparty’sstanceissupportiveandconstructiveinthisregard.
|     | Text:furtherimprovethelevelsoffinancial |     |     | Note:Dependingon |
| --- | --------------------------------------- | --- | --- | ---------------- |
supportespeciallytouniversitystudentswho
comefrompoorfamilies,andbyencouraging
work/studyopportunitiesforstudents;
Manif.-2 Context:Wewillprovidemoreopportunities MINORITY IMMEDIATEPERMANENTRESIDENCYFORNEW-
|     | forapplicantswhohaveCanadiansiblingsby |     | GROUPS | SPOUSESPOSITIVE |
| --- | -------------------------------------- | --- | ------ | --------------- |
givingadditionalpointsundertheExpress Explanation:Thisstatementfallsunderthecategory
Entrysystem,andwewillrestorethe “immigration”andspecifically“permanentresidency”withinthe
|     | maximumagefordependentsto22from19, |     |     | “ExternalRelations”aggregation.Thelabel |
| --- | ---------------------------------- | --- | --- | --------------------------------------- |
toallowmoreCanadianstobringtheir “IMMEDIATEPERMANENTRESIDENCYFOR-
|     | childrentoCanada. |     |     | NEWSPOUSESPOSITIVE”isthebestmatchforthis |
| --- | ----------------- | --- | --- | ---------------------------------------- |
Text:Wewillalsograntimmediate statementasitaccuratelyreflectsthepositivenatureofthe
permanentresidencytonewspousesentering party’sstanceongrantingimmediatepermanentresidencyto
|     | Canada,eliminatingthetwo-yearwaiting |     |     | newspousesenteringCanada. |
| --- | ------------------------------------ | --- | --- | ------------------------- |
period. Additionally,it’simportanttonotethattheprovidedpassage
doesnotcontainanynegativestatements,sononegativelabels
E.LLMsemantics/reasoningmistakes
| Dataset-Ex. | Text                               |     | GoldLabel      | LLMoutput     |
| ----------- | ---------------------------------- | --- | -------------- | ------------- |
| BFRS-1      | Thearmypicketcameunderheavygunfire |     | GUERILLAATTACK | ATTACKONSTATE |
andthemilitarycounteredtheattackand ONGOVFORCES Explanation:Thenewsstorydescribesanattackonamilitary
firedartilleryshells.Thisattacktookplace checkpoint,whichfitsthedefinitionofanattackonPakistani
twodaysaftertheexpiryofthedeadline territorytargetedatthestateofPakistanoritsrepresentatives.
givenbyTalibanthatthemilitaryshould Theattackwascarriedoutbynon-stateentities,specificallythe
halttheSwatoperationorfaceretaliation. Taliban,andwasinresponsetoadeadlinegivenbytheTaliban
forthemilitarytohaltanoperation.
Therefore,thebestlabelforthisnewsstoryis
”ATTACKONSTATE”.
Note:It’simportanttorememberthatthelabelsprovidedare
basedonthegivendefinitionsandtheinformationinthenews
story.Theactualclassificationofaneventcandependon
additionalcontextandinformationthat
| CCC-1 | Holdingasignandwearingapinkhat,Mary |     | DEMONSTRATION | RALLY |
| ----- | ----------------------------------- | --- | ------------- | ----- |
Counterlookedaroundandlamentedthefact Explanation:Thenewsstorydescribesacrowdgatheringto
thatonlyaboutthreedozenpeopleshowed demonstratetheirsupportfortheimpeachmentandremovalof
upFridayafternoonoutsidetheStatehouse PresidentDonaldTrump.Thecrowdisholdingsignsand
forarallysupportingtheimpeachmentand marchingtoabuilding,whichfitsthedefinitionofarally.
removalofPresidentDonaldTrump. Additionalcontext:Thecrowdissponsoringtheeventandis
“We’relikefrogsinboilingwater,”shesaid. drawingsupportfrompassersby,indicatingthatitisadeliberate
Theever-increasingpileofwrongdoingby andorganizeddemonstrationofsupportforapoliticalcause.
TrumphassimplynumbedmanyAmericans Thefactthattheeventincludesashortmarchtoabuildingalso
intoinactiondespitethethreattotheir supportsthelabelofrally,asmarchesareaseparatecategory.
nation,saidCounter,aretired Therefore,thelabelforthisnewsstoryis”RALLY”.
|     | communicationsprofessionalfromthe |     |     | Note:Thelabel”PROTEST”could |
| --- | --------------------------------- | --- | --- | --------------------------- |
NorthwestSide.
[...truncatedforspace...]
| Manif.-3 | Context:TaxBreaksforGreenBuildings |     | ENVIRONMENT- | INCENTIVES |
| -------- | ---------------------------------- | --- | ------------ | ---------- |
From1July2011,businessesthatinvestin ALISMPOSITIVE Explanation:Thetextdescribesataxincentiveforbusinessesto
eligibleassetsorcapitalworkstoimprovethe investinenergy-efficientbuildings.Theincentiveisabonustax
energyefficiencyoftheirexistingbuildings– deduction,whichfallsunderthecategoryofincentivesinthe
|     | from2starsorlowerto4starsorhigher– |     |     | providedlist. |
| --- | ---------------------------------- | --- | --- | ------------- |
willbeabletoapplyforaone-offbonustax Therefore,thelabelforthisexcerptis”INCENTIVES”.
deduction. Additionally,thelabelfortheaggregationlevelforthistext
|     | Text:Theincentivewillenablebusinessesto |     |     | wouldbe”Economy”. |
| --- | --------------------------------------- | --- | --- | ----------------- |
claimabonustaxdeductionof50percentof So,thecompletelabelforthisexcerptwouldbe”Economy:
|     | thecostoftheeligibleassetsorcapitalworks. |     |     | Incentives”. |
| --- | ----------------------------------------- | --- | --- | ------------ |
Thislabelindicatesthatthetextdiscussesapolicyrelatedto
incentiveswithintheeconomiccontextofthepoliticalparty’s
manifesto.
Table SI 4: Lemon-picked examples of LLM errors discovered during manual error analysis.
49

| Appendix | References |     |     |     |
| -------- | ---------- | --- | --- | --- |
AI, M. (2024). Mistral nemo. Blog: Mistral AI, https://mistral.ai/news/mistral-nemo/.
Atreja, S., Ashkinaze, J., Li, L., Mendelsohn, J., & Hemphill, L. (2024). Prompt design matters for
computational social science tasks but in unpredictable ways. arXiv:2406.11980.
Balloccu, S., Schmidtov´a, P., Lango, M., & Duˇsek, O. (2024). Leak, cheat, repeat: Data contami-
nation and evaluation malpractices in closed-source llms. EACL (Volume 1: Long Papers),
67–93.
Bender, E. (2019). The #benderrule: On naming the languages we study and why it matters. The
| Gradient, | 14, 34. |     |     |     |
| --------- | ------- | --- | --- | --- |
Brown,T.,Mann,B.,Ryder,N.,Subbiah,M.,Kaplan,J.D.,Dhariwal,P.,Neelakantan,A.,Shyam,
P., Sastry, G., Askell, A., et al. (2020). Language models are few-shot learners. NeurIPS.
Bueno de Mesquita, E., Fair, C. C., Jordan, J., Rais, R. B., & Shapiro, J. N. (2015). Measuring
political violence in Pakistan: Insights from the BFRS dataset. Conflict Management and
| Peace | Science. |     |     |     |
| ----- | -------- | --- | --- | --- |
Chang, K., Cramer, M., Soni, S., & Bamman, D. (2023). Speak, memory: An archaeology of books
| known | to chatgpt/gpt-4. | EMNLP, | 7312–7327. |     |
| ----- | ----------------- | ------ | ---------- | --- |
Clark, P., Cowhey, I., Etzioni, O., Khot, T., Sabharwal, A., Schoenick, C., & Tafjord, O. (2018).
Thinkyouhavesolvedquestionanswering?tryARC,theAI2reasoningchallenge.arXiv:1803.05457.
Daxecker, U., Amicarelli, E., & Jung, A. (2019). Electoral contention and violence (ecav): A new
| dataset. | Journal | of Peace Research, | 56(5), 714–723. |     |
| -------- | ------- | ------------------ | --------------- | --- |
Dettmers, T., Pagnoni, A., Holtzman, A., & Zettlemoyer, L. (2024). QLoRA: Efficient finetuning of
| quantized | LLMs. | NeurIPS. |     |     |
| --------- | ----- | -------- | --- | --- |
Devlin,J.,Chang,M.-W.,Lee,K.,&Toutanova,K.(2019).BERT:Pre-trainingofdeepbidirectional
transformers for language understanding. NAACL-HLT (Long and Short Papers).
| D’Ignazio, | C., & Klein, | L. F. (2020). Data | feminism. MIT | press. |
| ---------- | ------------ | ------------------ | ------------- | ------ |
Gardner, M., Merrill, W., Dodge, J., Peters, M. E., Ross, A., Singh, S., & Smith, N. A. (2021).
Competencyproblems:Onfindingandremovingartifactsinlanguagedata.EMNLP,1801–
1813.
50

Gerner, D. J., Schrodt, P. A., Yilmaz, O., & Abu-Jabr, R. (2002). Conflict and mediation event
observations (CAMEO): A new event data framework for the analysis of foreign policy
|     | interactions. | International | Studies | Association, | New Orleans. |
| --- | ------------- | ------------- | ------- | ------------ | ------------ |
Golchin, S., & Surdeanu, M. (2024). Time travel in llms: Tracing data contamination in large lan-
|     | guage models. | ICLR. |     |     |     |
| --- | ------------- | ----- | --- | --- | --- |
Grimmer, J., Roberts, M. E., & Stewart, B. M. (2022). Text as data: A new framework for machine
|     | learning | and the | social sciences. | Princeton U.P. |     |
| --- | -------- | ------- | ---------------- | -------------- | --- |
Groeneveld, D., Beltagy, I., Walsh, P., Bhagia, A., Kinney, R., Tafjord, O., Jha, A. H., Ivison, H.,
Magnusson,I.,Wang,Y.,etal.(2024).OLMo:Acceleratingthescienceoflanguagemodels.
arXiv:2402.00838.
Gururangan, S., Swayamdipta, S., Levy, O., Schwartz, R., Bowman, S., & Smith, N. A. (2018).
Annotationartifactsinnaturallanguageinferencedata.NAACL-HLT (Short Papers),107–
112.
Halterman, A., & Radford, B. J. (2021). Few-shot upsampling for protest size detection. Findings
|     | of the ACL, | 3713–3720. |     |     |     |
| --- | ----------- | ---------- | --- | --- | --- |
Hendrycks, D., Burns, C., Basart, S., Zou, A., Mazeika, M., Song, D., & Steinhardt, J. (2021).
|     | Measuring | massive | multitask | language understanding. | ICLR. |
| --- | --------- | ------- | --------- | ----------------------- | ----- |
Hu,E.J.,Shen,Y.,Wallis,P.,Allen-Zhu,Z.,Li,Y.,Wang,S.,Wang,L.,&Chen,W.(2022).LoRA:
|        | Low-rank    | adaptation  | of large | language models.      | ICLR. |
| ------ | ----------- | ----------- | -------- | --------------------- | ----- |
| Jiang, | A. Q., & et | al. (2023). | Mistral  | 7b. arXiv:2310.06825. |       |
Kwiatkowski, T., Palomaki, J., Redfield, O., Collins, M., Parikh, A., Alberti, C., Epstein, D., Polo-
sukhin, I., Kelcey, M., Devlin, J., Lee, K., Toutanova, K. N., Jones, L., Chang, M.-W., Dai,
A., Uszkoreit, J., Le, Q., & Petrov, S. (2019). Natural questions: A benchmark for question
|     | answering | research. | TACL. |     |     |
| --- | --------- | --------- | ----- | --- | --- |
Lacoste, A., Luccioni, A., Schmidt, V., & Dandres, T. (2019). Quantifying the carbon emissions of
|     | machine | learning. | arXiv preprint | arXiv:1910.09700. |     |
| --- | ------- | --------- | -------------- | ----------------- | --- |
Levy, M., Ravfogel, S., & Goldberg, Y. (2023). Guiding LLM to fool itself: Automatically manipu-
lating machine reading comprehension shortcut triggers. Findings of EMNLP.
Li, C., & Flanigan, J. (2024). Task contamination: Language models may not be few-shot anymore.
Proceedings of the AAAI Conference on Artificial Intelligence, 38(16), 18471–18480.
51

McCoy, T., Pavlick, E., & Linzen, T. (2019). Right for the wrong reasons: Diagnosing syntactic
| heuristics | in natural | language | inference. ACL, | 3428–3448. |     |
| ---------- | ---------- | -------- | --------------- | ---------- | --- |
Merz,N.,Regel,S.,&Lewandowski,J.(2016).Themanifestocorpus:Anewresourceforresearchon
politicalpartiesandquantitativetextanalysis.Research&Politics,3(2),2053168016643346.
Meta.(2024).Introducingllama3.1:Ourmostcapablemodelstodate.Blog:Meta,https://ai.meta.com/blog/meta-
llama-3-1/.
Palmer, A., Smith, N. A., & Spirling, A. (2024). Using proprietary language models in academic
| research | requires explicit | justification. | Nature | Computational | Science. |
| -------- | ----------------- | -------------- | ------ | ------------- | -------- |
Rajpurkar, P., Jia, R., & Liang, P. (2018). Know what you don’t know: Unanswerable questions for
| squad. ACL | (Volume | 2: Short | Papers), 784–789. |     |     |
| ---------- | ------- | -------- | ----------------- | --- | --- |
Rajpurkar, P., Zhang, J., Lopyrev, K., & Liang, P. (2016). Squad: 100,000+ questions for machine
| comprehension | of text. | EMNLP, | 2383–2392. |     |     |
| ------------- | -------- | ------ | ---------- | --- | --- |
Raschka, S. (2024a). Build a large language model (from scratch). Simon; Schuster.
Raschka,S.(2024b).Practicaltipsforfinetuningllmsusinglora(low-rankadaptation).Blog: Ahead
of AI, https://magazine.sebastianraschka.com/p/practical-tips-for-finetuning-llms.
Rein, D., Hou, B. L., Stickland, A. C., Petty, J., Pang, R. Y., Dirani, J., Michael, J., & Bow-
man, S. R. (2023). GPQA: A graduate-level Google-proof Q&A benchmark. arXiv preprint
arXiv:2311.12022.
Rogers,A.(2023).ClosedAImodelsmakebadbaselines[Accessed:2024-07-10].https://hackingsemantics.
xyz/2023/closed-baselines/
Shaham, U., Ivgi, M., Efrat, A., Berant, J., & Levy, O. (2023). Zeroscrolls: A zero-shot benchmark
| for long | text understanding. |     | EMNLP. |     |     |
| -------- | ------------------- | --- | ------ | --- | --- |
Shi,Z.,Yang,A.X.,Wu,B.,Aitchison,L.,Yilmaz,E.,&Lipani,A.(2024).Instructiontuningwith
| loss over | instructions. | arXiv:2405.14394. |     |     |     |
| --------- | ------------- | ----------------- | --- | --- | --- |
Spirling, A. (2023). Why open-source generative ai models are an ethical way forward for science.
| Nature, | 616(7957), 413–413. |     |     |     |     |
| ------- | ------------------- | --- | --- | --- | --- |
Trischler, A., Wang, T., Yuan, X., Harris, J., Sordoni, A., Bachman, P., & Suleman, K. (2017).
Newsqa: A machine comprehension dataset. Proceedings of the 2nd Workshop on Represen-
| tation Learning | for NLP, | 191–200. |     |     |     |
| --------------- | -------- | -------- | --- | --- | --- |
52

Vaswani, A., Shazeer, N. M., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, L., &
Polosukhin, I. (2017). Attention is all you need. Neural Information Processing Systems.
https://api.semanticscholar.org/CorpusID:13756489
Wang, Y., Ivison, H., Dasigi, P., Hessel, J., Khot, T., Chandu, K., Wadden, D., MacMillan, K.,
Smith, N. A., Beltagy, I., et al. (2023). How far can camels go? exploring the state of
| instruction | tuning | on open resources. | NeurIPS. |     |
| ----------- | ------ | ------------------ | -------- | --- |
Wei, J., Bosma, M., Zhao, V., Guu, K., Yu, A. W., Lester, B., Du, N., Dai, A. M., & Le, Q. V.
| (2022). | Finetuned | language models | are zero-shot | learners. ICLR. |
| ------- | --------- | --------------- | ------------- | --------------- |
Yang, Z., Qi, P., Zhang, S., Bengio, Y., Cohen, W., Salakhutdinov, R., & Manning, C. D. (2018).
Hotpotqa: A dataset for diverse, explainable multi-hop question answering. EMNLP, 2369–
2380.
Zhou,J.,Lu,T.,Mishra,S.,Brahma,S.,Basu,S.,Luan,Y.,Zhou,D.,&Hou,L.(2023).Instruction-
| following | evaluation | for large language | models. | arXiv:2311.07911. |
| --------- | ---------- | ------------------ | ------- | ----------------- |
53