|                          |             |     | The Parrot    | Dilemma:                                    |                   |     |       |     |
| ------------------------ | ----------- | --- | ------------- | ------------------------------------------- | ----------------- | --- | ----- | --- |
| Human-Labeled            |             | vs. | LLM-augmented | Data                                        | in Classification |     | Tasks |     |
| AndersGiovanniMøller     |             |     |               |                                             | AriannaPera       |     |       |     |
| ITUniversityofCopenhagen |             |     |               | ITUniversityofCopenhagen                    |                   |     |       |     |
|                          | agmo@itu.dk |     |               |                                             | arpe@itu.dk       |     |       |     |
| JacobAarupDalsgaard      |             |     |               |                                             | LucaMariaAiello   |     |       |     |
| ITUniversityofCopenhagen |             |     |               | ITUniversityofCopenhagen                    |                   |     |       |     |
|                          | jacd@itu.dk |     |               |                                             | luai@itu.dk       |     |       |     |
|                          | Abstract    |     |               | tivessuchasLlama(Touvronetal.,2023a,b),Mis- |                   |     |       |     |
tral(Jiangetal.,2023),andFalcon(Penedoetal.,
IntherealmofComputationalSocialScience
|                      |       |          |          | 2023) have | emerged, | allowing | their | use at a sub- |
| -------------------- | ----- | -------- | -------- | ---------- | -------- | -------- | ----- | ------------- |
| (CSS), practitioners | often | navigate | complex, |            |          |          |       |               |
stantiallylowercostcomparedtoproprietarymod-
low-resourcedomainsandfacethecostlyand
|     |     |     |     | els. However, | the training | dataset | sizes | of these |
| --- | --- | --- | --- | ------------- | ------------ | ------- | ----- | -------- |
time-intensivechallengesofacquiringandan-
notating data. We aim to establish a set of open-source models do not match those of their
closed-sourcecounterparts,andtheirperformance
guidelinestoaddresssuchchallenges,compar-
ingtheuseofhuman-labeleddatawithsynthet- acrosstasksremainssomewhatuncertain.
icallygenerateddatafromGPT-4andLlama- As an alternative to zero-shot approaches, re-
| 2 in ten distinct   | CSS           | classification | tasks of |           |               |          |             |              |
| ------------------- | ------------- | -------------- | -------- | --------- | ------------- | -------- | ----------- | ------------ |
|                     |               |                |          | searchers | have explored | the      | use of LLMs | for an-      |
| varying complexity. | Additionally, |                | we exam- |           |               |          |             |              |
|                     |               |                |          | notating  | data that can | be later | used        | for training |
inetheimpactoftrainingdatasizesonperfor-
smaller,specializedmodels,thusreducingthenoto-
mance. Ourfindingsrevealthatmodelstrained
riouslyhighcostofmanualannotation(Wangetal.,
onhuman-labeleddataconsistentlyexhibitsu-
perior or comparable performance compared 2021). Previousworkhasprimarilyfocusedonus-
totheirsyntheticallyaugmentedcounterparts.
|     |     |     |     | ing LLMs | for zero- or | few-shot | annotation | tasks, |
| --- | --- | --- | --- | -------- | ------------ | -------- | ---------- | ------ |
Nevertheless, synthetic augmentation proves reportingthatsyntheticlabelsareoftenofhigher
| beneficial, particularly |     | in improving | perfor- |         |                  |       |             |      |
| ------------------------ | --- | ------------ | ------- | ------- | ---------------- | ----- | ----------- | ---- |
|                          |     |              |         | quality | and cheaper than | human | annotations | (Gi- |
manceonrareclasseswithinmulti-classtasks.
|     |     |     |     | lardietal.,2023;Heetal.,2023). |     |     | However,zero- |     |
| --- | --- | --- | --- | ------------------------------ | --- | --- | ------------- | --- |
Furthermore,weleverageGPT-4andLlama-2
shotannotationsstrugglewithcomplexComputa-
forzero-shotclassificationandfindthat,while
|     |     |     |     | tional Social | Science | (CSS) | concepts, | exhibiting |
| --- | --- | --- | --- | ------------- | ------- | ----- | --------- | ---------- |
theygenerallydisplaystrongperformance,they
oftenfallshortwhencomparedtospecialized lower quality and reliability compared to human
classifierstrainedonmoderatelysizedtraining
labelers(Wangetal.,2021;Dingetal.,2022;Zhu
| sets. |     |     |     | etal.,2023). |                   |     |             |       |
| ----- | --- | --- | --- | ------------ | ----------------- | --- | ----------- | ----- |
|       |     |     |     | Other        | work has proposed |     | to mitigate | these |
1 Introduction
|     |     |     |     | weaknesses | by using | LLMs | to augment | human- |
| --- | --- | --- | --- | ---------- | -------- | ---- | ---------- | ------ |
LargeLanguageModels(LLMs),suchasOpenAI’s generated training examples (Sahu et al., 2022)
GPT-4 (OpenAI, 2023), have demonstrated im- either through text completion of partial exam-
pressive zero-shot performance across a range of ples (Feng et al., 2020; Bayer et al., 2023) or
tasks, including code generation, composition of throughgeneration(Yooetal.,2021;Meyeretal.,
human-liketext,andvarioustypesoftextclassifi- 2022;BalkusandYan,2022;Daietal.,2023;Guo
cation (Bubeck et al., 2023; Zhang et al., 2022; etal.,2023). Researchondataaugmentationwith
Savelka, 2023; Gilardi et al., 2023). However, LLMs is still in its early stages, exhibiting two
LLMsarenotperfectgeneralistsastheyoftenun- mainlimitations. First,differentclassificationex-
derperformtraditionalfine-tuningmethods,espe- periments with synthetic augmentation produced
cially in tasks involving commonsense and logi- mixedresults;somedemonstratedimprovementsin
cal reasoning (Qin et al., 2023) or concepts that modelperformance (BalkusandYan,2022)while
go beyond their pre-training (Ziems et al., 2023). othersobservedminimalgainsorevennegativeim-
Additionally, thedeploymentofLLMsfordown- pacts(Meyeretal.,2022). Arecentreviewonthe
streamtasksishinderedeitherbytheirmassivesize topic contributes to the assessment of an unclear
orbythecostandlegallimitationsofproprietary landscape (Ollion et al., 2023), highlighting that
APIs. Recently, competitive open-source alterna- substantiallysmallermodelsfine-tunedonhuman-
179
Proceedingsofthe18thConferenceoftheEuropeanChapteroftheAssociationforComputationalLinguistics
Volume2:ShortPapers,pages179–192
March17-22,2024(cid:13)c2024AssociationforComputationalLinguistics

annotateddataoftenoutperformtheLLMs. Second, Task Non-English Smallsize Class Sensitive Num.
|                                            |     |      |         |               |     |      |           |     |     |     | imbalance |     | classes |
| ------------------------------------------ | --- | ---- | ------- | ------------- | --- | ---- | --------- | --- | --- | --- | --------- | --- | ------- |
| most previous                              |     | work | focuses | on benchmarks |     | that |           |     |     |     |           |     |         |
| tendtobehomogeneousintermsoftheirnatureand |     |      |         |               |     |      | Sentiment |     |     |     |           |     | 2       |
|                                            |     |      |         |               |     |      | Offensive |     |     |     |           |     | 2       |
|                                            |     |      |         |               |     |      |           |     | ✓   |     | ✓         |     | ✓       |
complexity (e.g., sentiment classification), while Social dimensions ✓ 9
|     |     |     |     |     |     |     | Emotions |     |     |     |     |     | 13  |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
✓
| disregardingmoredifficultorlow-resourcetasks. |     |     |     |     |     |     | Empathy |     |     |     |     |     | 2   |
| --------------------------------------------- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
Politeness
| Overall,thebenefitsofLLMs-basedaugmentation |     |     |     |     |     |     |           |     |     | ✓   |     |     | 2   |
| ------------------------------------------- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
|                                             |     |     |     |     |     |     | Hyperbole |     |     |     |     |     | 2   |
Intimacy
| arenotconclusive,especiallywhenusingthemfor |     |     |     |     |     |     |                  |     |     |     |     |     | 6   |
| ------------------------------------------- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- |
|                                             |     |     |     |     |     |     | Same side stance |     |     | ✓   |     |     | 2   |
trainingmodelsforcomplexandlow-resourceclas- Condescension ✓ 2
sificationtaskstypicalinComputationalSocialSci-
|                    |     |     |                           |     |     |     |          | Task | properties. |     |                 |     |        |
| ------------------ | --- | --- | ------------------------- | --- | --- | --- | -------- | ---- | ----------- | --- | --------------- | --- | ------ |
|                    |     |     |                           |     |     |     | Table 1: |      |             |     | Characteristics |     | of our |
| ence(CSS)research. |     |     | Suchprevailinguncertainty |     |     |     |          |      |             |     |                 |     |        |
tasksintermsofcomplexity.
| generates | a dilemma |     | of whether | it  | is best | to con- |     |     |     |     |     |     |     |
| --------- | --------- | --- | ---------- | --- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
centratemoreresourcesintomanualdatalabeling
| orintoartificialaugmentation. |     |     |     |     |     |     | 2 Methods |     |     |     |     |     |     |
| ----------------------------- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
Thisworkmakestwocontributionswiththeaim
|     |     |     |     |     |     |     | We address | ten | classification |     | tasks | within | the do- |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | -------------- | --- | ----- | ------ | ------- |
ofbringingmoreclaritytothiscomplexlandscape.
|     |     |     |     |     |     |     | main of | CSS: | (i) sentiment |     | analysis | (Rosenthal |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | ---- | ------------- | --- | -------- | ---------- | --- |
First,withthegoalofprovidingCSSpractitioners
offensive
|     |     |     |     |     |     |     | et al., 2017), |     | (ii) |     | language |     | detection |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ---- | --- | -------- | --- | --------- |
withasetofactionableguidelinesforusingLLMs
inDanish(SigurbergssonandDerczynski,2023),
inclassification,weexperimentwithsyntheticdata
|              |     |        |       |            |            |     | (iii) extraction |     | of social |     | dimensions |     | of lan- |
| ------------ | --- | ------ | ----- | ---------- | ---------- | --- | ---------------- | --- | --------- | --- | ---------- | --- | ------- |
| augmentation |     | on ten | tasks | of varying | complexity |     |                  |     |           |     |            |     |         |
emotions
|     |     |     |     |     |     |     | guage (Choi |     | et al., | 2020), | (iv) |     | clas- |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------- | ------ | ---- | --- | ----- |
typicalofthedomainofCSS.Second,weperform
|               |     |          |     |            |      |          | sification | (CrowdFlower, |     |     | 2016), | (v) presence | of  |
| ------------- | --- | -------- | --- | ---------- | ---- | -------- | ---------- | ------------- | --- | --- | ------ | ------------ | --- |
| a comparative |     | analysis | of  | strategies | that | incorpo- |            |               |     |     |        |              |     |
empathyintext(Buecheletal.,2018),(vi)identi-
| rate LLMs | into | classification |     | tasks | either | as data |     |     |     |     |     |     |     |
| --------- | ---- | -------------- | --- | ----- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- |
ficationofpoliteness(Hayatietal.,2021),(vii)
| augmentationtoolsorasdirectpredictors. |     |     |     |     |     | Specifi- |     |     |     |     |     |     |     |
| -------------------------------------- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
hyperboleretrieval(ZhangandWan,2022),(viii)
cally,weassesshowaugmentingdatawithLLMs-
levelofintimacyinonlinequestions(PeiandJu-
| generated          | examples |        | performs                   | compared |        | to man- |               |     |              |     |             |     |             |
| ------------------ | -------- | ------ | -------------------------- | -------- | ------ | ------- | ------------- | --- | ------------ | --- | ----------- | --- | ----------- |
|                    |          |        |                            |          |        |         | rgens, 2020), |     | (ix) whether |     | two stances |     | are at the  |
| ualdataannotation. |          |        | Wetrainourclassifiersusing |          |        |         |               |     |              |     |             |     |             |
|                    |          |        |                            |          |        |         | same side     |     |              |     |             |     |             |
|                    |          |        |                            |          |        |         |               | of  | an argument  |     | (Körner     | et  | al., 2021), |
| incrementally      |          | larger | datasets                   | derived  | either | from    |               |     |              |     |             |     |             |
and(x)detectionofcondescensiononsocialme-
crowdsourcedannotationsorgeneratedbyGPT-4
|     |     |     |     |     |     |     | diaposts(WangandPotts,2019). |     |     |     |     | Dataforalltasks |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --------------- | --- |
orLlama-270B,oneofthebest-performingopen-
|        |              |     |         |               |     |        | ispubliclyavailable. |     |     | Table1providesasummary |     |     |     |
| ------ | ------------ | --- | ------- | ------------- | --- | ------ | -------------------- | --- | --- | ---------------------- | --- | --- | --- |
| source | alternatives |     | against | closed-source |     | model. |                      |     |     |                        |     |     |     |
oftaskdifficultiesacrossmultipledimensions.
Wethencontrasttheirperformancetothezero-shot
|     |     |     |     |     |     |     | Our | experimental |     | setup | simulates |     | a scenario |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ----- | --------- | --- | ---------- |
abilitiesofboththeLLMsconsidered.
whereminimalmanuallylabeleddataisavailable,
Overall,ourworkcontributestothecurrentlitera-
|     |     |     |     |     |     |     | and additional |     | labels | are | acquired | either | through |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------ | --- | -------- | ------ | ------- |
turewiththreefindings:
humanannotationsorsyntheticaugmentation(Fig-
• Syntheticaugmentationtypicallyprovideslittle ure1). Iftestdataisalreadyavailableasseparate
tonoimprovementinperformancecomparedto
|     |     |     |     |     |     |     | from the | training | one | in the | original | sources, | we  |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | --- | ------ | -------- | -------- | --- |
modelstrainedonhuman-generateddataforbi-
|     |     |     |     |     |     |     | considersuchasetasthetestset. |     |     |     |     | Otherwise, | we  |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | --- | ---------- | --- |
narytasksorbalancedmulti-classtasks. Sucha reserve20%oftheoriginaldatafortesting. Given
findingholdsevenwithsmallamountsoftraining the diverse sizes of the datasets and the time and
dataandaffirmsthehighvalueofhumanlabels.
economicconstraintsassociatedwithusingLLMs
| • More | complex | tasks | benefit | more | from | LLMs- |          |      |       |           |     | 5,000 |         |
| ------ | ------- | ----- | ------- | ---- | ---- | ----- | -------- | ---- | ----- | --------- | --- | ----- | ------- |
|        |         |       |         |      |      |       | APIs, we | have | set a | threshold | of  |       | samples |
generated data. In the most challenging tasks to define the actual training set. We set aside a
| considered, |     | both | in terms | of  | the number | of  |     |     |     |     |     |     |     |
| ----------- | --- | ---- | -------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
fixedbasesetof10%samplesfromtheactualtrain-
classesandunbalanceddata,wedemonstratethat
ingdata,whichweaugmentbygenerating9times
syntheticaugmentationenhancesmodelperfor- the same amount of synthetic texts with GPT-4
mance,substantiallybeatingcrowdsourceddata. and Llama-2 70B Chat (§2.1). Subsequently, we
| • Zero-shot |     | classification |     | is generally |     | outper- |     |     |     |     |     |     |     |
| ----------- | --- | -------------- | --- | ------------ | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
constructtrainingsetsofincreasingsizes,starting
formed by specialized models trained on hu- fromthebasesetandincrementingby10%sample
manorsyntheticdata,challengingthebeliefthat size either from the original data (crowdsourced
LLMs’strongzero-shotperformanceisthekey
dataset)orthesyntheticdata(augmenteddataset),
tomasteringcomplexclassificationtasks.
|     |     |     |     |     |     |     | until reaching |     | a maximum |     | of 100% | of  | the actual |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --------- | --- | ------- | --- | ---------- |
180

uatethediversityofgenerateddatabyexamining
thecosinesimilarity(semanticdiversity,computed
|     |     |     |     |     |     | with pytorch | SentenceTransformer) |               |             |     | to the data |
| --- | --- | --- | --- | --- | --- | ------------ | -------------------- | ------------- | ----------- | --- | ----------- |
|     |     |     |     |     |     | sample used  | for                  | the synthetic | generation, |     | as well     |
asthefractionofoverlappingtokensbetweenthe
|     |     |     |     |     |     | twotexts(lexicaldiversity). |     |     | Weprovideadetailed |     |     |
| --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | ------------------ | --- | --- |
explanationoftheprocessintheAppendix.
|     |     |     |     |     |     | 2.2 Classifiertraining |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- |
WeusetheHuggingfaceTrainerinterfacetotrain
intfloat/e5-base(Wangetal.,2022a),a110M
parametermodel(Wangetal.,2022b)thatachieves
|     |     |     |     |     |     | state-of-the-art |             | performance | on           | tasks | similar to  |
| --- | --- | --- | --- | --- | --- | ---------------- | ----------- | ----------- | ------------ | ----- | ----------- |
|     |     |     |     |     |     | those we         | investigate |             | (Muennighoff | et    | al., 2023). |
Wetrainthemodelinseveraliterationsonthedif-
| Figure1:Experimental |     | framework.Foreachdataset, |     |     |     |                         |     |     |                        |     |     |
| -------------------- | --- | ------------------------- | --- | --- | --- | ----------------------- | --- | --- | ---------------------- | --- | --- |
|                      |     |                           |     |     |     | ferenttasksanddatasets. |     |     | Foreachiteration,werun |     |     |
westartfromabaseset(10%crowdsourcedsamples)
thetrainingfor10epochswithabatchsizeof32.
andaugmentiteitherbyaddingmanuallylabeledsam-
WeusetheAdamW(LoshchilovandHutter,2019)
| ples or synthetic                                | samples | obtained |     | with LLMs. | Aug- |                                |     |     |     |     |            |
| ------------------------------------------------ | ------- | -------- | --- | ---------- | ---- | ------------------------------ | --- | --- | --- | --- | ---------- |
|                                                  |         |          |     |            |      | optimizerwithalearningrateof2e |     |     |     |     | 5. Wetrack |
| mentedtrainingsetsofdifferentsizesareusedtotrain |         |          |     |            |      |                                |     |     |     | −   |            |
classifiers. Modelsaretestedonaholdoutsetandcom- evaluationperformanceforeveryepochiteration.
paredtozero-shotapproaches. Weselectthecheckpointwiththelowestvalidation
|     |     |     |     |     |     | loss and | use it | to evaluate | the test | set | via macro |
| --- | --- | --- | --- | --- | --- | -------- | ------ | ----------- | -------- | --- | --------- |
training data. For each dataset, we train a sepa- F1 and accuracy. The runtime for each training
rateclassifier(§2.2),validateiton10%randomly instancerangesfrom1to31minutes. Thetestper-
sampleddatapointsfromtheactualtrainingsetfor formanceisoverallcomparabletotheoneonthe
eachtraininginstance,andevaluateitsperformance validationset(detailinSupplementary).
| on the holdout                            | test | set. | To establish | a   | baseline, |           |     |     |     |     |     |
| ----------------------------------------- | ---- | ---- | ------------ | --- | --------- | --------- | --- | --- | --- | --- | --- |
| wecomparethetrainedmodels’performancewith |      |      |              |     |           | 3 Results |     |     |     |     |     |
zero-shotclassificationusingGPT-4andLlama-2
|                                         |         |     |            |      |          | Figure 2   | illustrates | the     | comparison | between | clas-      |
| --------------------------------------- | ------- | --- | ---------- | ---- | -------- | ---------- | ----------- | ------- | ---------- | ------- | ---------- |
| 70BChat. Weprovidethemodelswithatextand |         |     |            |      |          |            |             |         |            |         |            |
|                                         |         |     |            |      |          | sification | models      | trained | on varying |         | amounts of |
| a set of possible                       | labels, |     | requesting | them | to clas- |            |             |         |            |         |            |
human-labeledandsyntheticallyaugmenteddata
| sifythetextaccordingly(seeAppendix). |     |          |       |      | Weuse   |          |          |       |                  |          |           |
| ------------------------------------ | --- | -------- | ----- | ---- | ------- | -------- | -------- | ----- | ---------------- | -------- | --------- |
|                                      |     |          |       |      |         | in terms | of Macro | F1    | score            | (results | for other |
| identical prompts                    |     | for both | LLMs, | with | minimal |          |          |       |                  |          |           |
|                                      |     |          |       |      |         | metrics  | can be   | found | in Supplementary |          | and on    |
changestothetemplateofLlama-2toalignitwith W&B2).Threekeyfindingsemerge.
First,models
| itspre-trainingformat. |     | Allcodeandsynthetically |     |     |     |     |     |     |     |     |     |
| ---------------------- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
trainedonhuman-annotateddatagenerallyoutper-
generateddataareavailableonGitHub1.
formthosetrainedonsyntheticallyaugmenteddata
|     |     |     |     |     |     | and zero-shot | models |     | in the cases | of  | binary bal- |
| --- | --- | --- | --- | --- | --- | ------------- | ------ | --- | ------------ | --- | ----------- |
2.1 DataAugmentation
hyperbole),
|     |     |     |     |     |     | anced tasks | (cf. |     | sensitive |     | tasks (cf. |
| --- | --- | --- | --- | --- | --- | ----------- | ---- | --- | --------- | --- | ---------- |
We construct prompts consisting of an example condescension and offensiveness) and multi-
fromtheoriginaldataalongwithitscorresponding class balanced tasks (cf. intimacy), even with
label. WeinstructtheLLMstogenerate9similar
|                           |     |     |                  |     |     | limited sizes | of            | training | data.     | However, | models  |
| ------------------------- | --- | --- | ---------------- | --- | --- | ------------- | ------------- | -------- | --------- | -------- | ------- |
| exampleswiththesamelabel. |     |     | Weadoptabalanced |     |     |               |               |          |           |          |         |
|                           |     |     |                  |     |     | trained on    | synthetically |          | augmented | data     | perform |
augmentation strategy: we first balance the class wellonunbalancedmulti-classtasks(cf. social
distribution in the base set by oversampling the dimensionsandemotions),mostlikelyduetothe
| minorityclasses. | Then,weaugmentthismodified |     |     |     |     |     |     |     |     |     |     |
| ---------------- | -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
balanceddataaugmentationtechniquewhichsub-
set by generating 9 examples for each data point. stantiallyincreasesthenumberofsamplesforrare
To ensure that the synthetic examples generated classes. Inthespecificcaseofemotions,theclassi-
| from the oversampled |     | classes | exhibit | substantial |     |     |     |     |     |     |     |
| -------------------- | --- | ------- | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
ficationmodelbasedonLlama-2syntheticallygen-
differences,wesetthetemperatureto1. Weeval- erateddataoutperformsalltheothermethods. Syn-
1https://github.com/AndersGiovanni/worker_vs_ 2https://wandb.ai/cocoons/crowdsourced_vs_gpt_
| gpt.git |     |     |     |     |     | datasize_v2 |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- |
181

Figure2: Data augmentation experiment. MacroF1scoreonthetestsetforthetenclassificationtasks,given
varioustrainingdatasizesandaugmentationstrategies. Y-axisscalesaredefineddifferentlyforeachtasktoenhance
clarity. Eachsetoftrainingsamplescontains10%crowdsourcedsamples(baseset). Thedashedlinerepresents
thezero-shotperformanceofLLMs. Eachexperimentundergoes5runsoftrainingwithdifferentdatasampling
seedsandconfidenceintervalsaroundaveragemetricvaluesareshown. Tasksaregroupedbycomplexitylevels(cf.
icontagsdefinedinTable1)andsortedwithineachgroupbytherelativeimprovementinperformancebetween
crowdsourced-basedandothertypesoftraining.
theticdatacreatedviaLlama-2is,onaverage,more tasks. Llama-2 was unable to produce any syn-
diversefromoriginaldatathanthatgeneratedvia theticallyaugmentedtextinDanishforthetaskof
GPT-4,especiallyfromalexicalperspective(see offensiveness, thus we decided not to run the
diversity analysis in the Appendix), which might zero-shotLlamaclassificationforsuchatask.
bebeneficialformulti-classunbalancedtasksand
particularlyforemotions. 4 DiscussionandConclusion
Second,zero-shotperformanceisstrongonlyon Toenhanceourlimitedunderstandingoftheability
specific tasks. For GPT-4, this holds particularly ofLLMstoserveassubstitutesorcomplementsto
for sentiment, likely due to the vast amount of human-generated labels in data annotation tasks,
relateddatainGPT-4’strainingdataset,andsame weinvestigatetheeffectivenessofgenerativedata
side stancetasks,possiblybecauseofthesmall augmentationwithLLMsontenclassificationtasks
sizeofthetestdataavailable. GPT-4alsoperforms withvaryinglevelsofcomplexityinthedomainof
well in the second smallest dataset considered: ComputationalSocialScience. Augmentationhas
politeness. In comparison, Llama-2 performs minimalimpactonclassificationperformancefor
substantiallyworseonsentiment,on-paronsame binarybalancedtasks,butshowspromisingresults
side stance,andevenbetteronpoliteness. For incomplexoneswithmultipleandrareclasses. Our
othertasks,theperformanceofzero-shotmodelsis findings lead to three key conclusions. First, the
comparabletoorevenworsethanthatofclassifi- timetoreplacehumanannotatorswithLLMshas
cationmodelstrainedoneitherhuman-annotated yettocome—manualannotation,despiteitscostli-
or synthetically augmented data, particularly for ness(Williamson,2016),providesmorevaluable
intimacy and condescension. Such tasks are informationduringtrainingforcommonbinaryand
characterizedbyaverynuanceddifferencebetween balancedtaskscomparedtothegenerationofsyn-
classesandbyanotionofsocial“power”thatcan- theticdataaugmentations. Second, artificialdata
notbeextractedeasily,giventhecomplexparadigm augmentationcanbevaluablewhenencountering
ofsocialpragmatics. Asimilarcaseofnegativeim- extremelyrareclassesinmulti-classscenarios,as
positionof“power”isthatofoffensive,whichis finding new examples in real-world data can be
alsocharacterizedbyalowzero-shotperformance challenging. In such cases, our study shows that
likely due to the restrictions of LLMs on offen- class-balancingLLMs-basedaugmentationcanen-
sivelanguage. Overall,onlyfocusingonthezero- hancetheclassificationperformanceonrareclasses.
shot setting, we observe GPT-4 to be best on six Lastly, while zero-shot approaches are appealing
tasks,equalinonetask,andLlama-2bestonthree due to their ability to achieve impressive perfor-
182

mance without training, they are often beaten by structingLLMstorewriteexamplesentencesand
orcomparabletomodelstrainedonmodest-sized allowingthebaseexampletoimplicitlyencodeall
trainingsets. Overall,ourstudyprovidesadditional informationaboutstyleanddomain,asproposed
| empirical | evidence to inform | the ongoing | debate in(Daietal.,2023). |     |     |     |
| --------- | ------------------ | ----------- | ------------------------- | --- | --- | --- |
about the usefulness of LLMs as annotators and Lastly, we acknowledge the limitation of com-
suggests guidelines for CSS practitioners facing putational resources in our experiments. Due to
classification tasks. To address the persistent in- resourceconstraints,weconductedexperimentson
consistencyinresultsonLLMs’performance,we differentmachineswithvariousNvidiaGPUcon-
| emphasizetwoessentialrequirements: |     | (i)theestab- |     |     |     |     |
| ---------------------------------- | --- | ------------ | --- | --- | --- | --- |
figurations,includingV100,A30,andRTX8000.
lishment of a systematic approach for evaluating Thisvariationimpactedtrainingefficiencyandthe
data quality in the context of LLMs-based data choiceoftrainingconfigurations. Additionally,lim-
augmentation, particularly when using synthetic itationsonresourceallocationpreventedextensive
samplesand(ii),thecollaborativedevelopmentof hyperparametersearches,especiallygiventhehigh
astandardizedwayofdevelopingpromptstoguide numberofmodelswefittedinourexperiments. We
thegenerationofdatausingLLMs. encourage future work to optimize models using
hyperparametertuning,takingadvantageofgreater
| Limitations  |                   |         | computationalpowerwhenavailable. |     |     |     |
| ------------ | ----------------- | ------- | -------------------------------- | --- | --- | --- |
| Constructing | a human-validated | dataset | necessi-                         |     |     |     |
EthicsStatement
| tates meticulous | evaluation | of annotators’ | out- |     |     |     |
| ---------------- | ---------- | -------------- | ---- | --- | --- | --- |
puts, which can be a costly process and does TherapidandwidespreadadoptionofLLMsand
not guarantee complete data fidelity, as crowd theirincreasingaccessibilityhaveraisedconcerns
workers may leverage LLMs during annotation about their potential risks. Efforts by organiza-
tionsinvolvedinLLMdevelopmenttoimplement
| tasks (Veselovsky | et al., | 2023b). Synthetic | data |     |     |     |
| ----------------- | ------- | ----------------- | ---- | --- | --- | --- |
generationthroughLLMshasalsoraisedconcerns safetyprotocolsandaddressbiaseshavebeensig-
regardingitsdistributionoftendifferingfromreal- nificant (Perez et al., 2022; Ganguli et al., 2022).
LLMsundergothoroughevaluationforsafetymet-
| worlddata(Veselovskyetal.,2023a). |     | However,it |     |     |     |     |
| --------------------------------- | --- | ---------- | --- | --- | --- | --- |
ispossibletoincorporatereal-worlddiversityinto rics,suchastoxicityandbias(Gehmanetal.,2020;
theoutputofLLMsbycarefullydesigningprompts Nangia et al., 2020). However, to augment sam-
that enable these models to emulate specific de- ples of offensive content, our study bypasses the
|                               |     |             | safetyprotocolforLLMs. |     | Thisfindingemphasizes |     |
| ----------------------------- | --- | ----------- | ---------------------- | --- | --------------------- | --- |
| mographics(Argyleetal.,2022). |     | Whilewehave |                        |     |                       |     |
minimallyaddressedsuchdesignconsiderationsin theongoingneedforcontinuedresearchtoensure
ourprompts,thereisapressingneedforadeeper, thatLLMsdonotgenerateharmfulorbiasedout-
|     |     |     | puts. While | safety protocols | and regulations | are |
| --- | --- | --- | ----------- | ---------------- | --------------- | --- |
systematicexplorationofpromptdesignanditsin-
fluenceontheresultingoutput’squality,diversity, inplace,furtherinvestigationisrequiredtoensure
andlabelpreservation. EldanandLi(2023),inpar- that LLMs consistently produce ethical and safe
ticular,highlightdiversityasasignificantchallenge outputsacrossallscenarios.
insyntheticdatacreation. Theyproposeamethod The purpose of generating augmented data in
that randomly selects words and textual features, thisstudyisexclusivelyforexperimentalpurposes,
suchasdialogueandmoralvalues,toimprovethe aimed at assessing the augmentation capabilities
variety of generated samples. Future expansions of Large Language Models. It is crucial to note
ofourstudycouldexploresuchadirectionbyus- thatwedecisivelydisapproveofanyintentionsto
ingrandomtextualelementsasadditionalinputin degrade or insult individuals or groups based on
generation, or focus on a few-shot approach for nationality,ethnicity,religion,orsexualorientation.
syntheticdatageneration(Brownetal.,2020). Nevertheless,werecognizethelegitimateconcern
Overall,wechosetousesimplepromptsbased regardingthepotentialmisuseofhuman-likeaug-
on empirical best practices from diverse sources menteddataformaliciouspurposes.
| available | during our development | phase | (see |     |     |     |
| --------- | ---------------------- | ----- | ---- | --- | --- | --- |
https://www.promptingguide.ai/)
and from
| previousworksexploringthesamedatasets(Choi |                      |        | References |     |     |     |
| ------------------------------------------ | -------------------- | ------ | ---------- | --- | --- | --- |
| et al., 2023).                             | In future expansions | of our | work,      |     |     |     |
LisaP.Argyle,EthanC.Busby,NancyFulda,Joshua
wecouldexploreevensimplerpromptdesigns,in- Gubler, Christopher Rytting, and David Wingate.
183

2022. Out of One, Many: Using Language Mod- RonenEldanandYuanzhiLi.2023. TinyStories: How
els to Simulate Human Samples. In Proceedings SmallCanLanguageModelsBeandStillSpeakCo-
of the 60th Annual Meeting of the Association herentEnglish? ArXiv:2305.07759[cs].
| for Computational | Linguistics | (Volume | 1: Long |     |     |     |     |     |
| ----------------- | ----------- | ------- | ------- | --- | --- | --- | --- | --- |
StevenYFeng,VarunGangal,DongyeopKang,Teruko
| Papers),pages819–862. | ArXiv:2209.06899[cs]. |     |     |                              |     |     |     |              |
| --------------------- | --------------------- | --- | --- | ---------------------------- | --- | --- | --- | ------------ |
|                       |                       |     |     | Mitamura,andEduardHovy.2020. |     |     |     | Genaug: Data |
SalvadorBalkusandDonghuiYan.2022. Improving augmentation for finetuning text generators. In
shorttextclassificationwithaugmenteddatausing ProceedingsofDeepLearningInsideOut(DeeLIO):
gpt-3. arXivpreprintarXiv:2205.10981. The First Workshop on Knowledge Extraction and
|     |     |     |     | Integration | for Deep | Learning | Architectures, | pages |
| --- | --- | --- | --- | ----------- | -------- | -------- | -------------- | ----- |
MarkusBayer,Marc-AndréKaufhold,BjörnBuchhold,
29–42.
MarcelKeller,JörgDallmeyer,andChristianReuter.
2023. Data augmentation in natural language pro- DeepGanguli,LianeLovitt,JacksonKernion,Amanda
cessing: a novel text generation approach for long Askell, Yuntao Bai, Saurav Kadavath, Ben Mann,
and short text classifiers. International journal of Ethan Perez, Nicholas Schiefer, Kamal Ndousse,
machinelearningandcybernetics,14(1):135–150. AndyJones,SamBowman,AnnaChen,TomCon-
erly,NovaDasSarma,DawnDrain,NelsonElhage,
TomB.Brown,BenjaminMann,NickRyder,Melanie
SheerEl-Showk,StanislavFort,ZacHatfield-Dodds,
Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Tom Henighan, Danny Hernandez, Tristan Hume,
Neelakantan,PranavShyam,GirishSastry,Amanda Josh Jacobson, Scott Johnston, Shauna Kravec,
Askell, Sandhini Agarwal, Ariel Herbert-Voss, Catherine Olsson, Sam Ringer, Eli Tran-Johnson,
Gretchen Krueger, Tom Henighan, Rewon Child, DarioAmodei,TomBrown,NicholasJoseph,Sam
| Aditya Ramesh, | Daniel M. | Ziegler, | Jeffrey Wu, |             |       |       |               |          |
| -------------- | --------- | -------- | ----------- | ----------- | ----- | ----- | ------------- | -------- |
|                |           |          |             | McCandlish, | Chris | Olah, | Jared Kaplan, | and Jack |
ClemensWinter,ChristopherHesse,MarkChen,Eric Clark. 2022. Red Teaming Language Models to
Sigler,MateuszLitwin,ScottGray,BenjaminChess, Reduce Harms: Methods, Scaling Behaviors, and
Jack Clark, Christopher Berner, Sam McCandlish, LessonsLearned. ArXiv:2209.07858[cs].
| Alec Radford, | Ilya Sutskever, | and | Dario Amodei. |     |     |     |     |     |
| ------------- | --------------- | --- | ------------- | --- | --- | --- | --- | --- |
2020. Languagemodelsarefew-shotlearners. Samuel Gehman, Suchin Gururangan, Maarten Sap,
|     |     |     |     | Yejin Choi, | and Noah | A.  | Smith. 2020. | RealToxi- |
| --- | --- | --- | --- | ----------- | -------- | --- | ------------ | --------- |
Sébastien Bubeck, Varun Chandrasekaran, Ronen El- cityPrompts: EvaluatingNeuralToxicDegeneration
dan, Johannes Gehrke, Eric Horvitz, Ece Kamar, inLanguageModels. ArXiv:2009.11462[cs].
| Peter Lee, | Yin Tat Lee, Yuanzhi |     | Li, Scott Lund- |     |     |     |     |     |
| ---------- | -------------------- | --- | --------------- | --- | --- | --- | --- | --- |
berg, Harsha Nori, Hamid Palangi, Marco Tulio Fabrizio Gilardi, Meysam Alizadeh, and Maël Kubli.
Ribeiro, and Yi Zhang. 2023. Sparks of Artificial 2023. Chatgptoutperformscrowd-workersfortext-
GeneralIntelligence: EarlyexperimentswithGPT-4. annotationtasks. arXivpreprintarXiv:2303.15056.
ArXiv:2303.12712[cs].
ZhenGuo,PeiqiWang,YanweiWang,andShangdiYu.
SvenBuechel,AnnekeBuffone,BarrySlaff,LyleUn- 2023. Dr.llama: Improvingsmalllanguagemodels
gar,andJoaoSedoc.2018. Modelingempathyand indomain-specificqaviagenerativedataaugmenta-
distress in reaction to news stories. arXiv preprint tion. arXivpreprintarXiv:2305.07804.
arXiv:1808.10399.
|     |     |     |     | Shirley Anugrah | Hayati,                        | Dongyeop | Kang, | and Lyle |
| --- | --- | --- | --- | --------------- | ------------------------------ | -------- | ----- | -------- |
|     |     |     |     | Ungar.2021.     | Doesbertlearnashumansperceive? |          |       |          |
MinjeChoi,LucaMariaAiello,KrisztiánZsoltVarga,
andDanieleQuercia.2020. Tensocialdimensions understandinglinguisticstylesthroughlexica. arXiv
of conversationsand relationships. In Proceedings preprintarXiv:2109.02738.
ofTheWebConference2020.ACM.
XingweiHe,ZhenghaoLin,YeyunGong,AJin,Hang
MinjeChoi,JiaxinPei,SagarKumar,ChangShu,and Zhang,ChenLin,JianJiao,SiuMingYiu,NanDuan,
David Jurgens. 2023. Do llms understand social WeizhuChen,etal.2023. Annollm: Makinglarge
languagemodelstobebettercrowdsourcedannota-
| knowledge? | evaluatingthesociabilityoflargelan- |     |     |     |     |     |     |     |
| ---------- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- |
guagemodelswithsocketbenchmark. arXivpreprint tors. arXivpreprintarXiv:2303.16854.
arXiv:2305.14938.
AlbertQ.Jiang,AlexandreSablayrolles,ArthurMen-
CrowdFlower.2016. Theemotionintext,publishedby sch,ChrisBamford,DevendraSinghChaplot,Diego
crowdflower. Accessed: 2023-09-25. de las Casas, Florian Bressand, Gianna Lengyel,
|     |     |     |     | Guillaume | Lample, | Lucile | Saulnier, | Lélio Re- |
| --- | --- | --- | --- | --------- | ------- | ------ | --------- | --------- |
HaixingDai,ZhengliangLiu,WenxiongLiao,Xiaoke
|     |     |     |     | nard Lavaud, | Marie-Anne |     | Lachaux, | Pierre Stock, |
| --- | --- | --- | --- | ------------ | ---------- | --- | -------- | ------------- |
Huang, Zihao Wu, Lin Zhao, Wei Liu, Ninghao TevenLeScao,ThibautLavril,ThomasWang,Timo-
Liu, Sheng Li, Dajiang Zhu, et al. 2023. Chataug: théeLacroix,andWilliamElSayed.2023. Mistral
Leveragingchatgptfortextdataaugmentation. arXiv 7B. ArXiv:2310.06825[cs].
preprintarXiv:2302.13007.
|     |     |     |     | Erik Körner, | Gregor | Wiedemann, | Ahmad | Dawar |
| --- | --- | --- | --- | ------------ | ------ | ---------- | ----- | ----- |
BoshengDing,ChengweiQin,LinlinLiu,LidongBing, Hakimi,GerhardHeyer,andMartinPotthast.2021.
ShafiqJoty, andBoyangLi.2022. Isgpt-3agood On classifying whether two texts are on the same
dataannotator? arXivpreprintarXiv:2212.10450. side of an argument. In Proceedings of the
184

2021 conference on empirical methods in natural Jaromir Savelka. 2023. Unlocking practical applica-
languageprocessing,pages10130–10138. tionsinlegaldomain: Evaluationofgptforzero-shot
|                 |     |       |         |       |           | semantic | annotation | of  | legal | texts. arXiv | preprint |     |
| --------------- | --- | ----- | ------- | ----- | --------- | -------- | ---------- | --- | ----- | ------------ | -------- | --- |
| Ilya Loshchilov | and | Frank | Hutter. | 2019. | Decoupled |          |            |     |       |              |          |     |
arXiv:2305.04417.
weightdecayregularization.
|     |     |     |     |     |     | Gudbjartur | Ingi Sigurbergsson |     | and | Leon | Derczynski. |     |
| --- | --- | --- | --- | --- | --- | ---------- | ------------------ | --- | --- | ---- | ----------- | --- |
SelinaMeyer,DavidElsweiler,BerndLudwig,Marcos 2023. Offensivelanguageandhatespeechdetection
| Fernandez-Pichel,andDavidELosada.2022. |     |     |                       |                    | Dowe | fordanish. |     |     |     |     |     |     |
| -------------------------------------- | --- | --- | --------------------- | ------------------ | ---- | ---------- | --- | --- | --- | --- | --- | --- |
| stillneedhumanassessors?               |     |     | prompt-basedgpt-3user |                    |      |            |     |     |     |     |     |     |
| simulationinconversationalai.          |     |     |                       | InProceedingsofthe |      |            |     |     |     |     |     |     |
HugoTouvron,ThibautLavril,GautierIzacard,Xavier
| 4th Conference |     | on Conversational |     | User | Interfaces, |     |     |     |     |     |     |     |
| -------------- | --- | ----------------- | --- | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- |
Martinet,Marie-AnneLachaux,TimothéeLacroix,
| pages1–6. |     |     |     |     |     | BaptisteRozière,NamanGoyal,EricHambro,Faisal |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | --- |
Azhar,AurelienRodriguez,ArmandJoulin,Edouard
NiklasMuennighoff,NouamaneTazi,LoïcMagne,and Grave,andGuillaumeLample.2023a. Llama: Open
| NilsReimers.2023. |     | MTEB:MassiveTextEmbed- |     |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
andefficientfoundationlanguagemodels.
| dingBenchmark. |       | ArXiv:2210.07316[cs]. |        |           |     |               |            |         |         |         |         |     |
| -------------- | ----- | --------------------- | ------ | --------- | --- | ------------- | ---------- | ------- | ------- | ------- | ------- | --- |
|                |       |                       |        |           |     | Hugo Touvron, | Louis      | Martin, | Kevin   | Stone,  | Peter   | Al- |
| Nikita Nangia, | Clara | Vania,                | Rasika | Bhalerao, | and |               |            |         |         |         |         |     |
|                |       |                       |        |           |     | bert, Amjad   | Almahairi, |         | Yasmine | Babaei, | Nikolay |     |
Samuel R. Bowman. 2020. CrowS-Pairs: A Chal- Bashlykov,SoumyaBatra,PrajjwalBhargava,Shruti
lengeDatasetforMeasuringSocialBiasesinMasked
|                 |     |                       |     |     |     | Bhosale, | et al.     | 2023b. | Llama   | 2: Open |          | founda- |
| --------------- | --- | --------------------- | --- | --- | --- | -------- | ---------- | ------ | ------- | ------- | -------- | ------- |
| LanguageModels. |     | ArXiv:2010.00133[cs]. |     |     |     |          |            |        |         |         |          |         |
|                 |     |                       |     |     |     | tion and | fine-tuned | chat   | models. | arXiv   | preprint |         |
arXiv:2307.09288.
EtienneOllion,RubingShen,AnaMacanovic,andAr-
| nault Chatelain. |     | 2023. | ChatGPT | for Text | Annota- |                      |     |        |       |          |     |       |
| ---------------- | --- | ----- | ------- | -------- | ------- | -------------------- | --- | ------ | ----- | -------- | --- | ----- |
|                  |     |       |         |          |         | Veniamin Veselovsky, |     | Manoel | Horta | Ribeiro, |     | Akhil |
tion? MindtheHype! Arora, Martin Josifoski, Ashton Anderson, and
|              |                       |          |     |                   |     | Robert West.     | 2023a. | Generating |          | faithful | synthetic |       |
| ------------ | --------------------- | -------- | --- | ----------------- | --- | ---------------- | ------ | ---------- | -------- | -------- | --------- | ----- |
| OpenAI.2023. | Gpt-4technicalreport. |          |     |                   |     |                  |        |            |          |          |           |       |
|              |                       |          |     |                   |     | data with        | large  | language   | models:  | A        | case      | study |
|              |                       |          |     |                   |     | in computational |        | social     | science. | arXiv    | preprint  |       |
| Jiaxin Pei   | and David             | Jurgens. |     | 2020. Quantifying |     |                  |        |            |          |          |           |       |
arXiv:2305.15041.
| intimacy        | in language. |              | In  | Proceedings | of the     |     |     |     |     |     |     |     |
| --------------- | ------------ | ------------ | --- | ----------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| 2020 Conference |              | on Empirical |     | Methods     | in Natural |     |     |     |     |     |     |     |
LanguageProcessing(EMNLP),pages5307–5326. Veniamin Veselovsky, Manoel Horta Ribeiro, and
|     |     |     |     |     |     | RobertWest.2023b. |                                    | Artificialartificialartificialin- |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------------- | ---------------------------------- | --------------------------------- | --- | --- | --- | --- |
|     |     |     |     |     |     | telligence:       | Crowdworkerswidelyuselargelanguage |                                   |     |     |     |     |
GuilhermePenedo,QuentinMalartic,DanielHesslow,
|          |           |            |     |           |       | models | for text | production | tasks. | arXiv | preprint |     |
| -------- | --------- | ---------- | --- | --------- | ----- | ------ | -------- | ---------- | ------ | ----- | -------- | --- |
| Ruxandra | Cojocaru, | Alessandro |     | Cappelli, | Hamza |        |          |            |        |       |          |     |
arXiv:2306.07899.
| Alobeidli, | Baptiste | Pannier, | Ebtesam | Almazrouei, |         |     |     |     |     |     |     |     |
| ---------- | -------- | -------- | ------- | ----------- | ------- | --- | --- | --- | --- | --- | --- | --- |
| and Julien | Launay.  | 2023.    | The     | refinedweb  | dataset |     |     |     |     |     |     |     |
forfalconllm: outperformingcuratedcorporawith Liang Wang, Nan Yang, Xiaolong Huang, Binxing
Jiao,LinjunYang,DaxinJiang,RanganMajumder,
| web data, | and | web | data only. | arXiv | preprint |                   |     |                         |     |     |     |     |
| --------- | --- | --- | ---------- | ----- | -------- | ----------------- | --- | ----------------------- | --- | --- | --- | --- |
|           |     |     |            |       |          | andFuruWei.2022a. |     | Textembeddingsbyweakly- |     |     |     |     |
arXiv:2306.01116.
supervisedcontrastivepre-training.
| Ethan Perez, | Saffron | Huang, | Francis | Song, | Trevor |     |     |     |     |     |     |     |
| ------------ | ------- | ------ | ------- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- |
Cai, RomanRing, JohnAslanides, AmeliaGlaese, Liang Wang, Nan Yang, Xiaolong Huang, Binx-
Nat McAleese, and Geoffrey Irving. 2022. Red ing Jiao, Linjun Yang, Daxin Jiang, Rangan Ma-
|     |     |     |     |     |     | jumder, | and Furu | Wei. | 2022b. |     | Text Embed- |     |
| --- | --- | --- | --- | --- | --- | ------- | -------- | ---- | ------ | --- | ----------- | --- |
TeamingLanguageModelswithLanguageModels.
dingsbyWeakly-SupervisedContrastivePre-training.
ArXiv:2202.03286[cs].
ArXiv:2212.03533[cs].
ChengweiQin,AstonZhang,ZhuoshengZhang,Jiaao
Chen,MichihiroYasunaga,andDiyiYang.2023. Is ShuohangWang, YangLiu, YichongXu, Chenguang
chatgptageneral-purposenaturallanguageprocess- Zhu, and Michael Zeng. 2021. Want to reduce la-
ingtasksolver? arXivpreprintarXiv:2302.06476. beling cost? gpt-3 can help. In Findings of the
AssociationforComputationalLinguistics:EMNLP
SaraRosenthal,NouraFarra,andPreslavNakov.2017. 2021,pages4195–4205.
| SemEval-2017task4: |     | SentimentanalysisinTwitter. |     |     |     |     |     |     |     |     |     |     |
| ------------------ | --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
In Proceedings of the 11th International Workshop Zijian Wang and Christopher Potts. 2019. Talk-
onSemanticEvaluation(SemEval-2017),pages502– down: Acorpusforcondescensiondetectionincon-
518,Vancouver,Canada.AssociationforComputa- text. In Proceedings of the 2019 Conference on
EmpiricalMethodsinNaturalLanguageProcessing
tionalLinguistics.
|     |     |     |     |     |     | and the | 9th International |     | Joint | Conference |     | on  |
| --- | --- | --- | --- | --- | --- | ------- | ----------------- | --- | ----- | ---------- | --- | --- |
GauravSahu,PauRodriguez,IssamLaradji,Parmida Natural Language Processing (EMNLP-IJCNLP),
| Atighehchian, | David      | Vazquez,     |     | and Dzmitry | Bah-    | pages3711–3719. |     |     |     |     |     |     |
| ------------- | ---------- | ------------ | --- | ----------- | ------- | --------------- | --- | --- | --- | --- | --- | --- |
| danau.        | 2022. Data | augmentation |     | for intent  | classi- |                 |     |     |     |     |     |     |
fication with off-the-shelf large language models. Vanessa Williamson. 2016. On the Ethics of Crowd-
In Proceedings of the 4th Workshop on NLP for sourcedResearch. PS:PoliticalScience&Politics,
| ConversationalAI,pages47–57. |     |     |     |     |     | 49(01):77–81. |     |     |     |     |     |     |
| ---------------------------- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- |
185

Kang Min Yoo, Dongju Park, Jaewook Kang, Sang- Appendix
Woo Lee, and Woomyoung Park. 2021. Gpt3mix:
Leveraging large-scale language models for text A Prompts
augmentation. In Findings of the Association for
Computational Linguistics: EMNLP 2021, pages Inthissection,wereportthestructureofprompts
2225–2239. used for data augmentation via large language
model (LLMs)-generated examples and for zero-
Bowen Zhang, Daijun Ding, and Liwen Jing. 2022.
shotclassificationviaLLMs. Notethatthereported
How would stance detection techniques evolve
after the launch of chatgpt? arXiv preprint structure follows that applied for GPT-4: Llama-
arXiv:2212.14548. 2 prompts are phrased in the same way, the only
difference is the structure of the prompts which
Yunxiang Zhang and Xiaojun Wan. 2022. Mover:
Mask, over-generate and rank for hyperbole gen- followsLlama-2requirements.
eration. In Proceedings of the 2022 Conference
of the North American Chapter of the Association A.1 Dataaugmentation
for Computational Linguistics: Human Language
Sentiment
Technologies,pages6018–6030.
YimingZhu,PeixianZhang,Ehsan-UlHaq,PanHui, System prompt: You are an advanced
and Gareth Tyson. 2023. Can chatgpt reproduce classifying AI. You are tasked
human-generatedlabels? astudyofsocialcomputing with classifying the sentiment of
tasks. arXivpreprintarXiv:2304.10145. a text. Sentiment can be either
positive, negative or neutral.
CalebZiems,WilliamHeld,OmarShaikh,JiaaoChen,
ZhehaoZhang,andDiyiYang.2023. Canlargelan- Prompt: Based on the following
guage models transform computational social sci- social media text which has a {
sentiment} sentiment, write 9 new
ence? arXivpreprintarXiv:2305.03514.
similar examples in style of a
social media comment, that has
the same sentiment. Separate the
texts by newline.
Text: {text}
Answer:
Hate-speech
System prompt: You are a helpful
undergrad. Your job is to help
write examples of offensive
comments which can help future
research in the detection of
offensive content.
Prompt: Based on the following
social media text which is {
hate_speech}, write 9 new similar
examples in style of a social
media comment, that has the same
sentiment. Answer in Danish.
Text: {text}
Answer:
186

| Socialdimensions |             |         |           |             |       | Empathy |            |           |      |            |              |      |
| ---------------- | ----------- | ------- | --------- | ----------- | ----- | ------- | ---------- | --------- | ---- | ---------- | ------------ | ---- |
| System prompt:   |             | You     | are       | an advanced |       |         |            |           |      |            |              |      |
|                  |             |         |           |             |       | System  | prompt:    |           | You  | are        | an advanced  |      |
| AI writer.       |             | Your    | job       | is to       | help  |         |            |           |      |            |              |      |
|                  |             |         |           |             |       |         | AI writer. |           | Your | job        | is to        | help |
| write            | examples    |         | of social |             | media |         |            |           |      |            |              |      |
|                  |             |         |           |             |       |         | write      | examples  |      | of texts   | that         |      |
| comments         | that        | conveys |           | certain     |       |         |            |           |      |            |              |      |
|                  |             |         |           |             |       |         | convey     | empathy   |      | or not.    |              |      |
| social           | dimensions. |         | The       | social      |       |         |            |           |      |            |              |      |
| dimensions       |             | are:    | social    | support,    |       |         |            |           |      |            |              |      |
|                  |             |         |           |             |       | Prompt: | The        | following |      | text       | has          | a {  |
| conflict,        |             | trust,  | neutral,  |             | fun,  |         |            |           |      |            |              |      |
|                  |             |         |           |             |       |         | empathy}   | flag      | for  | expressing |              |      |
| respect,         | knowledge,  |         |           | power,      | and   |         |            |           |      |            |              |      |
|                  |             |         |           |             |       |         | empathy,   | write     |      | 9 new      | semantically |      |
similarity/identity.
|             |           |     |        |           |       |     | similar | examples |     | that    | show  | the |
| ----------- | --------- | --- | ------ | --------- | ----- | --- | ------- | -------- | --- | ------- | ----- | --- |
|             |           |     |        |           |       |     | same    | intent   | and | empathy | flag. |     |
| Prompt: The | following |     | social |           | media |     |         |          |     |         |       |     |
| text        | conveys   | the | social | dimension |       |     |         |          |     |         |       |     |
Text: {text}
| {social_dimension}. |     |     |     | {        |     |     |     |     |     |     |     |     |
| ------------------- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| social_dimension}   |     |     | in  | a social |     |     |     |     |     |     |     |     |
Answer:
| context | is  | defined | by  | {   |     |     |     |     |     |     |     |     |
| ------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
social_dimension_description}.
| Write    | 9 new    | semantically |            |          | similar  |            |            |     |      |     |             |      |
| -------- | -------- | ------------ | ---------- | -------- | -------- | ---------- | ---------- | --- | ---- | --- | ----------- | ---- |
| examples | in       | style        | of         | a social |          | Politeness |            |     |      |     |             |      |
| media    | comment, |              | that       | show     | the same |            |            |     |      |     |             |      |
| intent   | and      | social       | dimension. |          |          |            |            |     |      |     |             |      |
|          |          |              |            |          |          | System     | prompt:    |     | You  | are | an advanced |      |
|          |          |              |            |          |          |            | AI writer. |     | Your | job | is to       | help |
Text: {text}
|     |     |     |     |     |     |     | write    | examples |        | of social |            | media |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | ------ | --------- | ---------- | ----- |
|     |     |     |     |     |     |     | comments | that     | convey |           | politeness |       |
Answer:
or not.
|     |     |     |     |     |     | Prompt: | The  | following |              | social |      | media |
| --- | --- | --- | --- | --- | --- | ------- | ---- | --------- | ------------ | ------ | ---- | ----- |
|     |     |     |     |     |     |         | text | has a     | {politeness} |        | flag | for   |
Emotions
|     |     |     |     |     |     |     | politeness,  |     | write   | 9   | new      |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------- | --- | -------- | --- |
|     |     |     |     |     |     |     | semantically |     | similar |     | examples | in  |
System prompt: You are an advanced the style of a social media
| AI writer.  |           | Your     | job          | is to     | help     |           | comment,   | that           | show       | the        | same        |      |
| ----------- | --------- | -------- | ------------ | --------- | -------- | --------- | ---------- | -------------- | ---------- | ---------- | ----------- | ---- |
| write       | examples  |          | of social    |           | media    |           | intent     | and            | politeness |            | flag.       |      |
| comments    | that      | convey   |              | certain   |          |           |            |                |            |            |             |      |
| emotions.   |           | Emotions | to           | be        |          | Text:     | {text}     |                |            |            |             |      |
| considered  |           | are:     | sadness,     |           |          |           |            |                |            |            |             |      |
| enthusiasm, |           | empty,   | neutral,     |           | worry    | Answer:   |            |                |            |            |             |      |
| , love,     | fun,      | hate,    | happiness,   |           |          |           |            |                |            |            |             |      |
| relief,     | boredom,  |          | surprise,    |           | anger.   |           |            |                |            |            |             |      |
| Prompt: The | following |          | social       |           | media    | Hyperbole |            |                |            |            |             |      |
| text        | conveys   | the      | emotion      |           | {emotion |           |            |                |            |            |             |      |
| }. Write    | 9         | new      | semantically |           |          |           |            |                |            |            |             |      |
|             |           |          |              |           |          | System    | prompt:    |                | You        | are        | an advanced |      |
| similar     | examples  |          | in           | the style | of       |           |            |                |            |            |             |      |
|             |           |          |              |           |          |           | AI writer. |                | You        | are tasked |             | with |
| a social    | media     |          | comment,     | that      | show     |           |            |                |            |            |             |      |
|             |           |          |              |           |          |           | writing    | examples       |            | of         | sentences   |      |
| the         | same      | intent   | and          | emotion.  |          |           |            |                |            |            |             |      |
|             |           |          |              |           |          |           | that       | are hyperbolic |            |            | or not.     |      |
Text: {text}
|     |     |     |     |     |     | Prompt: | The    | following |     | sentence |            | has a |
| --- | --- | --- | --- | --- | --- | ------- | ------ | --------- | --- | -------- | ---------- | ----- |
|     |     |     |     |     |     |         | {hypo} | flag      | for | being    | hyperbolic |       |
Answer:
|     |     |     |     |     |     |     | . Write | 9        | new semantically |            |      |       |
| --- | --- | --- | --- | --- | --- | --- | ------- | -------- | ---------------- | ---------- | ---- | ----- |
|     |     |     |     |     |     |     | similar | examples |                  | that       | show | the   |
|     |     |     |     |     |     |     | same    | intent   | and              | hyperbolic |      | flag. |
Text: {text}
Answer:
187

| Intimacy |            |              |          |                |             | Condescension |                  |                 |                |             |          |
| -------- | ---------- | ------------ | -------- | -------------- | ----------- | ------------- | ---------------- | --------------- | -------------- | ----------- | -------- |
|          |            |              |          |                |             | System        | prompt:          |                 | You are        | an advanced |          |
| System   | prompt:    |              | You are  | an             | advanced    |               |                  |                 |                |             |          |
|          |            |              |          |                |             |               | AI writer.       |                 | Your job       | is to       | help     |
|          | AI writer. | Your         | job      | is             | to help     |               |                  |                 |                |             |          |
|          |            |              |          |                |             |               | write            | examples        | of social      |             | media    |
|          | write      | examples     | of       | questions      |             |               |                  |                 |                |             |          |
|          |            |              |          |                |             |               | comments         | that            | convey         |             |          |
|          | posted     | on social    |          | media          | that        |               |                  |                 |                |             |          |
|          |            |              |          |                |             |               | condescendence   |                 | or not.        |             |          |
|          | convey     | certain      | levels   |                | of intimacy |               |                  |                 |                |             |          |
|          | . The      | intimacy     | levels   |                | are: very   |               |                  |                 |                |             |          |
|          |            |              |          |                |             | Prompt:       | The              | following       |                | social      | media    |
|          | intimate,  | intimate,    |          | somewhat       |             |               |                  |                 |                |             |          |
|          |            |              |          |                |             |               | text             | has a           | {talkdown}     | flag        | for      |
|          | intimate,  | not          | very     | intimate,      | not         |               |                  |                 |                |             |          |
|          |            |              |          |                |             |               | showing          | condescendence, |                |             | write 9  |
|          | intimate,  | not          | intimate |                | at all.     |               |                  |                 |                |             |          |
|          |            |              |          |                |             |               | new semantically |                 | similar        |             | examples |
|          |            |              |          |                |             |               | in the           | style           | of a           | social      | media    |
| Prompt:  | The        | following    |          | social         | media       |               |                  |                 |                |             |          |
|          |            |              |          |                |             |               | comment,         | that            | show           | the same    |          |
|          | question   | conveys      |          | the {intimacy} |             |               |                  |                 |                |             |          |
|          |            |              |          |                |             |               | intent           | and             | condescendence |             | flag.    |
|          | level      | of question  |          | intimacy.      | Write       |               |                  |                 |                |             |          |
|          | 9 new      | semantically |          | similar        |             |               |                  |                 |                |             |          |
Text: {text}
|     | examples | in        | the style |      | of a social |     |     |     |     |     |     |
| --- | -------- | --------- | --------- | ---- | ----------- | --- | --- | --- | --- | --- | --- |
|     | media    | question, |           | that | show the    |     |     |     |     |     |     |
Answer:
|     | same | intent | and intimacy |     | level. |     |     |     |     |     |     |
| --- | ---- | ------ | ------------ | --- | ------ | --- | --- | --- | --- | --- | --- |
Text: {text}
Answer:
A.2 Zero-shotclassification
Samesidestance
Sentiment
| System | prompt: |     | You are | an  | advanced |     |     |     |     |     |     |
| ------ | ------- | --- | ------- | --- | -------- | --- | --- | --- | --- | --- | --- |
AI writer. Your job is to help System prompt: You are an advanced
|     | write | examples | of  | questions |     |     | classifying |     | AI. You | are | tasked |
| --- | ----- | -------- | --- | --------- | --- | --- | ----------- | --- | ------- | --- | ------ |
posted on social media that with classifying the sentiment of
convey certain levels of intimacy a text. Sentiment can be either
. The intimacy levels are: very positive, negative or neutral.
|     | intimate, | intimate, |     | somewhat |     |     |     |     |     |     |     |
| --- | --------- | --------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
intimate, not very intimate, not Prompt: Classify the following
intimate, not intimate at all. social media comment into either
|     |     |     |     |     |     |     | negative |     | ,   | neutral | or  |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | ------- | --- |
Prompt: The following social media positive . Your answer MUST
question conveys the {intimacy} be either one of ["negative", "
level of question intimacy. Write neutral", "positive"]. Your
|     | 9 new    | semantically |              | similar |             |       | answer | must | be lowercase. |     |     |
| --- | -------- | ------------ | ------------ | ------- | ----------- | ----- | ------ | ---- | ------------- | --- | --- |
|     | examples | in           | the style    |         | of a social |       |        |      |               |     |     |
|     | media    | question,    |              | that    | show the    | Text: | {text} |      |               |     |     |
|     | same     | intent       | and intimacy |         | level.      |       |        |      |               |     |     |
Answer:
Text: {text}
Answer:
Hate-speech
|     |     |     |     |     |     | System  | prompt:      |             | You are     | an advanced |          |
| --- | --- | --- | --- | --- | --- | ------- | ------------ | ----------- | ----------- | ----------- | -------- |
|     |     |     |     |     |     |         | classifying  |             | AI. You     | are         | tasked   |
|     |     |     |     |     |     |         | with         | classifying | whether     |             | a text   |
|     |     |     |     |     |     |         | is offensive |             | or not.     |             |          |
|     |     |     |     |     |     | Prompt: | The          | following   | is          | a           | comment  |
|     |     |     |     |     |     |         | on a         | social      | media post. |             | Classify |
|     |     |     |     |     |     |         | whether      | the         | post is     | offensive   | (        |
|     |     |     |     |     |     |         | OFF)         | or not      | (NOT).      | Your        | answer   |
|     |     |     |     |     |     |         | must         | be one      | of ["OFF",  | "NOT"].     |          |
Text: {text}
Answer:
188

| Socialdimensions |                  |            |         |            |          |     | Empathy |                  |          |         |             |        |      |
| ---------------- | ---------------- | ---------- | ------- | ---------- | -------- | --- | ------- | ---------------- | -------- | ------- | ----------- | ------ | ---- |
| System           | prompt:          |            | You are | an         | advanced |     |         |                  |          |         |             |        |      |
|                  |                  |            |         |            |          |     | System  | prompt:          | You      | are     | an advanced |        |      |
|                  | classifying      |            | AI. You | are        | tasked   |     |         |                  |          |         |             |        |      |
|                  |                  |            |         |            |          |     |         | classifying      | AI.      | You     | are         | tasked |      |
|                  | with classifying |            |         | the social |          |     |         |                  |          |         |             |        |      |
|                  |                  |            |         |            |          |     |         | with classifying |          | whether |             | the    | text |
|                  | dimension        | of         | a text. | The        | social   |     |         |                  |          |         |             |        |      |
|                  |                  |            |         |            |          |     |         | expresses        | empathy. |         |             |        |      |
|                  | dimensions       | are:       | social  |            | support, |     |         |                  |          |         |             |        |      |
|                  | conflict,        | trust,     |         | neutral,   | fun,     |     |         |                  |          |         |             |        |      |
|                  |                  |            |         |            |          |     | Prompt: | Based            | on       | the     | following   | text,  |      |
|                  | respect,         | knowledge, |         | power,     |          | and |         |                  |          |         |             |        |      |
|                  |                  |            |         |            |          |     |         | classify         | whether  |         | the text    |        |      |
similarity/identity.
|         |        |           |       |           |       |     |     | expresses   | empathy   |             | or not. | You    |     |
| ------- | ------ | --------- | ----- | --------- | ----- | --- | --- | ----------- | --------- | ----------- | ------- | ------ | --- |
|         |        |           |       |           |       |     |     | answer      | MUST only | be          | one     | of the |     |
| Prompt: | Based  | on        | the   | following |       |     |     |             |           |             |         |        |     |
|         |        |           |       |           |       |     |     | two labels. | Your      | answer      |         | MUST   | be  |
|         | social | media     | text, | classify  |       | the |     |             |           |             |         |        |     |
|         |        |           |       |           |       |     |     | exactly     | one of    | [’empathy’, |         | ’not   |     |
|         | social | dimension |       | of the    | text. | You |     |             |           |             |         |        |     |
|         |        |           |       |           |       |     |     | empathy’].  | The       | answer      | must    | be     |     |
|         | answer | MUST      | only  | be one    | of    | the |     |             |           |             |         |        |     |
lowercased.
|     | social  | dimensions. |     | Your | answer |     |     |     |     |     |     |     |     |
| --- | ------- | ----------- | --- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
|     | MUST be | exactly     | one | of   | ["     |     |     |     |     |     |     |     |     |
Text: {text}
|     | social_support", |            |     | "conflict", |     | "   |     |     |     |     |     |     |     |
| --- | ---------------- | ---------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | trust",          | "neutral", |     | "fun",      | "   |     |     |     |     |     |     |     |     |
Answer:
|     | respect",              | "knowledge", |     |     | "power", | "      |     |     |     |     |     |     |     |
| --- | ---------------------- | ------------ | --- | --- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- |
|     | similarity_identity"]. |              |     |     | The      | answer |     |     |     |     |     |     |     |
|     | must be                | lowercase.   |     |     |          |        |     |     |     |     |     |     |     |
Politeness
Text: {text}
|     |     |     |     |     |     |     | System | prompt: | You | are | an advanced |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------- | --- | --- | ----------- | --- | --- |
Answer:
|     |     |     |     |     |     |     |     | classifying      | AI.    | You | are       | tasked |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | ------ | --- | --------- | ------ | --- |
|     |     |     |     |     |     |     |     | with classifying |        | the | whether   |        | the |
|     |     |     |     |     |     |     |     | text is          | polite | or  | impolite. |        |     |
Emotions
|     |     |     |     |     |     |     | Prompt: | Based    | on  | the        | following | text,  |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | -------- | --- | ---------- | --------- | ------ | --- |
|     |     |     |     |     |     |     |         | classify | the | politeness |           | of the |     |
System prompt: You are an advanced text. You answer MUST only be one
classifying AI. You are tasked of the two labels. Your answer
with classifying the emotion of a MUST be exactly one of [’impolite
text. The emotions are: sadness, ’, ’polite’]. The answer must be
|     | enthusiasm, |          | empty, | neutral,  |           |     |       | lowercased. |     |     |     |     |     |
| --- | ----------- | -------- | ------ | --------- | --------- | --- | ----- | ----------- | --- | --- | --- | --- | --- |
|     | worry,      | love,    | fun,   | hate,     | happiness |     |       |             |     |     |     |     |     |
|     | , relief,   | boredom, |        | surprise, |           |     | Text: | {text}      |     |     |     |     |     |
anger.
Answer:
| Prompt: | Based          | on         | the           | following    |           |       |           |                  |             |     |             |        |     |
| ------- | -------------- | ---------- | ------------- | ------------ | --------- | ----- | --------- | ---------------- | ----------- | --- | ----------- | ------ | --- |
|         | social         | media      | text,         | classify     |           | the   |           |                  |             |     |             |        |     |
|         | emotion        | of the     | text.         | You          | answer    |       |           |                  |             |     |             |        |     |
|         | MUST only      | be         | one           | of the       | emotions. |       | Hyperbole |                  |             |     |             |        |     |
|         | Your answer    |            | MUST          | be exactly   |           | one   |           |                  |             |     |             |        |     |
|         | of [’sadness’, |            | ’enthusiasm’, |              |           | ’     |           |                  |             |     |             |        |     |
|         |                |            |               |              |           |       | System    | prompt:          | You         | are | an advanced |        |     |
|         | empty’,        | ’neutral’, |               | ’worry’,     |           | ’love |           |                  |             |     |             |        |     |
|         |                |            |               |              |           |       |           | classifying      | AI.         | You | are         | tasked |     |
|         | ’, ’fun’,      | ’hate’,    |               | ’happiness’, |           | ’     |           |                  |             |     |             |        |     |
|         |                |            |               |              |           |       |           | with classifying |             | the | whether     |        | the |
|         | relief’,       | ’boredom’, |               | ’surprise’,  |           | ’     |           |                  |             |     |             |        |     |
|         |                |            |               |              |           |       |           | text is          | a hyperbole |     | or not      | a      |     |
|         | anger’].       | The        | answer        | must         | be        |       |           |                  |             |     |             |        |     |
hyperbole.
lowercased.
|     |     |     |     |     |     |     | Prompt: | Based | on  | the | following | text, |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----- | --- | --- | --------- | ----- | --- |
Text: {text}
|     |     |     |     |     |     |     |     | classify     | the | text | is a    | hyperbole |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ---- | ------- | --------- | --- |
|     |     |     |     |     |     |     |     | . You answer |     | MUST | only be | one       | of  |
Answer:
|     |     |     |     |     |     |     |     | the two          | labels. | Your | answer        | MUST |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | ------- | ---- | ------------- | ---- | --- |
|     |     |     |     |     |     |     |     | be exactly       | one     | of   | [’hyperbole’, |      | ’   |
|     |     |     |     |     |     |     |     | not hyperbole’]. |         | The  | answer        | must |     |
be lowercased.
Text: {text}
Answer:
189

Intimacy Condescension
System prompt: You are an advanced System prompt: You are an advanced
classifying AI. You are tasked classifying AI. You are tasked
with classifying the intimacy of with classifying if the text is
the text. The different condescending or not
intimacies are ’Very intimate’, ’ condescending.
Intimate’, ’Somewhat intimate’, ’
Not very intimate’, ’Not intimate Prompt: Based on the following text,
’, and ’Not intimate at all’. classify if it is condescending.
You answer MUST only be one of
Prompt: Based on the following text, the two labels. Your answer MUST
classify how intimate the text be exactly one of [’not
is. You answer MUST only be one condescension’, ’condescension’].
of the six labels. Your answer
MUST be exactly one of [’Very- Text: {text}
intimate’, ’Intimate’, ’Somewhat-
intimate’, ’Not-very-intimate’, ’ Answer:
Not-intimate’, ’Not-intimate-at-
all’].
Text: {text}
B Performancereports
Answer:
Thissectionincludesadetailedperformancereport.
Table2describestheperformanceofclassification
models trained onthe full human-labeled dataset
Samesidestance
and the full LLMs-augmented datasets. We also
System prompt: You are an advanced report the zero-shot performance of GPT-4 and
classifying AI. You are tasked Llama-2asareference.
with classifying whether two
Giventhementionedpresenceofclassimbalance
texts, separated by [SEP], convey
the same stance or not. The two for some of the considered tasks, we provide a
stances are ’not same side’ and ’ generaloverviewoflabeldistributionsperclassin
same side’.
thetrainingdata(cf. Figure3). Detailedclass-wise
Prompt: Based on the following text, classificationreportsforallconsideredmodelsfor
classify the stance of the text. thetentasksofreferencesareavailableonW&B3.
You answer MUST only be one of
the stances. Your answer MUST be
exactly one of [’not same side’, C Diversity
’same side’]. The answer must be
lowercased. We investigate the diversity between the original
dataandtheonesyntheticallygeneratedviaLarge
Text: {text}
LanguageModels(LLMs)forthetentasksofrefer-
Answer: ence. Weemploytokenoverlapasanindicatorof
lexicaldiversityandcosinesimilarityasagaugeof
semanticdiversity. Toensureafaircomparison,for
eachtaskwecomputebaselinediversitymeasures
by considering the average similarity of random
pairsofanoriginalsampleandasyntheticsample,
both for GPT-4 and Llama-2 models. Our find-
ingsrevealthatthesyntheticdata,generatedboth
viaGPT-4andLlama-2, exhibitssubstantiallexi-
caldifferentiationfromtheoriginalsampleswhile
preservingsemanticsimilarity. Notably,Llama-2
displaysamorepronouncedlevelofdiversitycom-
paredtoGPT-4,asdemonstratedbylowervalues
inbothtokenoverlapandcosinesimilaritymetrics
3https://wandb.ai/cocoons/crowdsourced_vs_gpt_
datasize_v2
190

|                  |              | Figure3: | Classdistributionpertask. |                  |           |         |
| ---------------- | ------------ | -------- | ------------------------- | ---------------- | --------- | ------- |
|                  |              |          | Individual                |                  | Zero-shot |         |
|                  | Crowdsourced |          | GPT-4synthetic            | Llama-2synthetic | GPT-4     | Llama-2 |
| Sentiment        |              | 0.6901   | 0.6430                    | 0.6020           | 0.7126    | 0.5998  |
| Hyperbole        |              | 0.7163   | 0.6768                    | 0.6570           | 0.6781    | 0.5894  |
| Empathy          |              | 0.6268   | 0.6135                    | 0.6157           | 0.6488    | 0.6233  |
| Samesidestance   |              | 0.3462   | 0.6443                    | 0.4926           | 0.9403    | 0.9403  |
| Politeness       |              | 0.8266   | 0.8970                    | 0.7480           | 0.8982    | 0.9884  |
| Condescension    |              | 0.8391   | 0.7295                    | 0.7070           | 0.6362    | 0.4563  |
| Offensiveness    |              | 0.7764   | 0.5698                    | -                | 0.7170    | -       |
| Intimacy         |              | 0.4864   | 0.4093                    | 0.3738           | 0.0285    | 0.1445  |
| Emotions         |              | 0.1452   | 0.1578                    | 0.1911           | 0.1247    | 0.1681  |
| Socialdimensions |              | 0.2551   | 0.3002                    | 0.3038           | 0.3042    | 0.2765  |
Table2:MacroF1scoreofclassificationmodelstrainedonthefullhuman-labeleddataset,thefullLLMs-augmented
dataset(Individualdatasets)forthethreecomputationalsocialsciencetasksofinterest. Zero-shotperformanceof
GPT-4andLlama-2isalsoprovided.
| (refer to Figure | 4 for further | details). | Also, data |     |     |     |
| ---------------- | ------------- | --------- | ---------- | --- | --- | --- |
generatedbyLlama-2isonaverage,lexicallymore
differentfromthecorrespondingoriginaldatacom-
paredtoitsbaseline,whilesuchaconditiondoes
notholdforGPT-4.
191

Figure4: LexicalandsemanticdiversitybetweenoriginalandsyntheticallygenerateddataforGPT-4andLlama-2
models. We also include similarity between random samples of original and augmented data within each task,
denotedasbaseline. SyntheticdatafortheoffensivenesstaskcouldnotbegeneratedviaLlama-2.
192