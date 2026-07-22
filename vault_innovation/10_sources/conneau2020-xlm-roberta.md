|     | Unsupervised |              |                  | Cross-lingual  |     | Representation      |                 |     | Learning        |                  | at  | Scale |     |
| --- | ------------ | ------------ | ---------------- | -------------- | --- | ------------------- | --------------- | --- | --------------- | ---------------- | --- | ----- | --- |
|     |              |              |                  | AlexisConneau∗ |     | KartikayKhandelwal∗ |                 |     |                 |                  |     |       |     |
|     | NamanGoyal   |              | VishravChaudhary |                |     |                     | GuillaumeWenzek |     |                 | FranciscoGuzma´n |     |       |     |
|     |              | EdouardGrave |                  | MyleOtt        |     | LukeZettlemoyer     |                 |     | VeselinStoyanov |                  |     |       |     |
FacebookAI
|     |     |     | Abstract |     |     |     | Multilingual |     | masked | language |     | models | (MLM) |
| --- | --- | --- | -------- | --- | --- | --- | ------------ | --- | ------ | -------- | --- | ------ | ----- |
likemBERT(Devlinetal.,2018)andXLM(Lam-
Thispapershowsthatpretrainingmultilingual ple and Conneau, 2019) have pushed the state-
| language              |     | models | at scale | leads                | to significant |        |            |             |               |       |               |     |       |
| --------------------- | --- | ------ | -------- | -------------------- | -------------- | ------ | ---------- | ----------- | ------------- | ----- | ------------- | --- | ----- |
|                       |     |        |          |                      |                |        | of-the-art | on          | cross-lingual |       | understanding |     | tasks |
| performance           |     | gains  | for      | a wide range         | of             | cross- |            |             |               |       |               |     |       |
|                       |     |        |          |                      |                |        | by jointly | pretraining |               | large | Transformer   |     | mod-  |
| lingualtransfertasks. |     |        |          | WetrainaTransformer- |                |        |            |             |               |       |               |     |       |
basedmaskedlanguagemodelononehundred els (Vaswani et al., 2017) on many languages.
|     |     |     |     |     |     |     | These models |     | allow | for | effective | cross-lingual |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ----- | --- | --------- | ------------- | --- |
languages,usingmorethantwoterabytesoffil-
teredCommonCrawldata.Ourmodel,dubbed transfer, as seen in a number of benchmarks in-
XLM-R,significantlyoutperformsmultilingual cluding cross-lingual natural language inference
BERT (mBERT) on a variety of cross-lingual (Bowmanetal.,2015;Williamsetal.,2017;Con-
| benchmarks, |     | including |     | +14.6% | average | accu- |     |     |     |     |     |     |     |
| ----------- | --- | --------- | --- | ------ | ------- | ----- | --- | --- | --- | --- | --- | --- | --- |
neauetal.,2018),questionanswering(Rajpurkar
| racy | on  | XNLI, | +13% | average | F1 score | on  |               |     |       |         |        |           |     |
| ---- | --- | ----- | ---- | ------- | -------- | --- | ------------- | --- | ----- | ------- | ------ | --------- | --- |
|      |     |       |      |         |          |     | et al., 2016; |     | Lewis | et al., | 2019), | and named | en- |
MLQA,and+2.4%F1scoreonNER.XLM-R
tityrecognition(Piresetal.,2019;WuandDredze,
performsparticularlywellonlow-resourcelan-
|         |     |           |       |         |          |     | 2019). | However, | all | of these | studies | pre-train | on  |
| ------- | --- | --------- | ----- | ------- | -------- | --- | ------ | -------- | --- | -------- | ------- | --------- | --- |
| guages, |     | improving | 15.7% | in XNLI | accuracy |     |        |          |     |          |         |           |     |
for Swahili and 11.4% for Urdu over previ- Wikipedia,whichprovidesarelativelylimitedscale
ous XLM models. We also present a detailed especiallyforlowerresourcelanguages.
empirical analysis of the key factors that are Inthispaper,wefirstpresentacomprehensive
| required |     | to achieve | these | gains, | including | the |     |     |     |     |     |     |     |
| -------- | --- | ---------- | ----- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
analysisofthetrade-offsandlimitationsofmulti-
trade-offsbetween(1)positivetransferandca-
|     |     |     |     |     |     |     | lingual | language | models |     | at scale, | inspired | by re- |
| --- | --- | --- | --- | --- | --- | --- | ------- | -------- | ------ | --- | --------- | -------- | ------ |
pacitydilutionand(2)theperformanceofhigh
centmonolingualscalingefforts(Liuetal.,2019).
| and | low   | resource | languages | at scale. | Finally,    |     |            |     |           |     |         |               |     |
| --- | ----- | -------- | --------- | --------- | ----------- | --- | ---------- | --- | --------- | --- | ------- | ------------- | --- |
|     |       |          |           |           |             |     | We measure | the | trade-off |     | between | high-resource |     |
| we  | show, | for the  | first     | time, the | possibility | of  |            |     |           |     |         |               |     |
multilingualmodelingwithoutsacrificingper- andlow-resourcelanguagesandtheimpactoflan-
languageperformance;XLM-Risverycompet- guagesamplingandvocabularysize. Theexperi-
itive with strong monolingual models on the ments expose a trade-off as we scale the number
GLUEandXNLIbenchmarks. Wewillmake oflanguagesforafixedmodelcapacity: morelan-
ourcode,dataandmodelspubliclyavailable.1
|     |     |     |     |     |     |     | guages          | leads | to better | cross-lingual |          | performance |       |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ----- | --------- | ------------- | -------- | ----------- | ----- |
|     |     |     |     |     |     |     | on low-resource |       | languages |               | up until | a point,    | after |
1 Introduction
whichtheoverallperformanceonmonolingualand
Thegoalofthispaperistoimprovecross-lingual cross-lingual benchmarks degrades. We refer to
languageunderstanding(XLU),bycarefullystudy- this tradeoff as the curse of multilinguality, and
|     |             |     |          |              |     |        | show that | it can | be  | alleviated | by  | simply | increas- |
| --- | ----------- | --- | -------- | ------------ | --- | ------ | --------- | ------ | --- | ---------- | --- | ------ | -------- |
| ing | the effects | of  | training | unsupervised |     | cross- |           |        |     |            |     |        |          |
lingual representations at a very large scale. We ing model capacity. We argue, however, that this
present XLM-R a transformer-based multilingual remains an important limitation for future XLU
maskedlanguagemodelpre-trainedontextin100 systems which may aim to improve performance
withmoremodestcomputationalbudgets.
| languages, |     | which | obtains | state-of-the-art |     | perfor- |     |     |     |     |     |     |     |
| ---------- | --- | ----- | ------- | ---------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
manceoncross-lingualclassification,sequencela- OurbestmodelXLM-RoBERTa(XLM-R)out-
belingandquestionanswering. performsmBERToncross-lingualclassificationby
|     |     |     |     |     |     |     | upto23%accuracyonlow-resourcelanguages. |     |     |     |     |     | It  |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------- | --- | --- | --- | --- | --- | --- |
∗Equalcontribution.
outperformsthepreviousstateoftheartby5.1%av-
Correspondenceto{aconneau,kartikayk}@fb.com
1 https://github.com/facebookresearch/(fairseq-py,pytext,xlm) erageaccuracyonXNLI,2.42%averageF1-score
8440
Proceedingsofthe58thAnnualMeetingoftheAssociationforComputationalLinguistics,pages8440–8451
July5-10,2020.(cid:13)c2020AssociationforComputationalLinguistics

onNamedEntityRecognition,and9.1%average data,ascomparedtoourapproach.
F1-scoreoncross-lingualQuestionAnswering. We Thebenefitsofscalinglanguagemodelpretrain-
alsoevaluatemonolingualfinetuningontheGLUE ingbyincreasingthesizeofthemodelaswellas
andXNLIbenchmarks,whereXLM-Robtainsre- thetrainingdatahasbeenextensivelystudiedinthe
sultscompetitivewithstate-of-the-artmonolingual literature. For the monolingual case, Jozefowicz
models, including RoBERTa (Liu et al., 2019). etal.(2016)showhowlarge-scaleLSTMmodels
These results demonstrate, for the first time, that canobtainmuchstrongerperformanceonlanguage
it is possible to have a single large model for all modelingbenchmarkswhentrainedonbillionsof
languages,withoutsacrificingper-languageperfor- tokens. GPT(Radfordetal.,2018)alsohighlights
mance. Wewillmakeourcode, modelsanddata theimportanceofscalingtheamountofdataand
publiclyavailable,withthehopethatthiswillhelp RoBERTa (Liu et al., 2019) shows that training
researchinmultilingualNLPandlow-resourcelan- BERT longer on more data leads to significant
| guageunderstanding. |     |     |     |     |     |     | boostinperformance. |     | InspiredbyRoBERTa,we |     |     |     |
| ------------------- | --- | --- | --- | --- | --- | --- | ------------------- | --- | -------------------- | --- | --- | --- |
showthatmBERTandXLMareundertuned,and
| 2 RelatedWork |     |     |     |     |     |     | thatsimpleimprovementsinthelearningprocedure |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- |
ofunsupervisedMLMleadstomuchbetterperfor-
Frompretrainedwordembeddings(Mikolovetal., mance. WetrainoncleanedCommonCrawls(Wen-
2013b;Penningtonetal.,2014)topretrainedcon- zeketal.,2019),whichincreasetheamountofdata
| textualized | representations |     |     | (Peters | et al., | 2018; |     |     |     |     |     |     |
| ----------- | --------------- | --- | --- | ------- | ------- | ----- | --- | --- | --- | --- | --- | --- |
forlow-resourcelanguagesbytwoordersofmagni-
| Schuster | et al., | 2019) | and transformer |     | based | lan- |                |                             |     |     |     |     |
| -------- | ------- | ----- | --------------- | --- | ----- | ---- | -------------- | --------------------------- | --- | --- | --- | --- |
|          |         |       |                 |     |       |      | tudeonaverage. | Similardatahasalsobeenshown |     |     |     |     |
guagemodels(Radfordetal.,2018;Devlinetal., tobeeffectiveforlearninghighqualitywordem-
| 2018), | unsupervised |     | representation |     | learning | has |     |     |     |     |     |     |
| ------ | ------------ | --- | -------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
beddingsinmultiplelanguages(Graveetal.,2018).
| significantly | improved |     | the | state of | the art | in nat- |     |     |     |     |     |     |
| ------------- | -------- | --- | --- | -------- | ------- | ------- | --- | --- | --- | --- | --- | --- |
Severaleffortshavetrainedmassivelymultilin-
ural language understanding. Parallel work on gual machine translation models from large par-
cross-lingualunderstanding(Mikolovetal.,2013a;
|     |     |     |     |     |     |     | allel corpora. | They | uncover | the high | and | low re- |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ---- | ------- | -------- | --- | ------- |
Schusteretal.,2019;LampleandConneau,2019)
sourcetrade-offandtheproblemofcapacitydilu-
extendsthesesystemstomorelanguagesandtothe
|     |     |     |     |     |     |     | tion (Johnson | et al., | 2017; | Tan et al., | 2019). | The |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ------- | ----- | ----------- | ------ | --- |
cross-lingualsettinginwhichamodelislearnedin work most similar to ours is Arivazhagan et al.
onelanguageandappliedinotherlanguages.
|      |           |        |     |            |     |      | (2019), which                           | trains | a single | model | in 103 | lan- |
| ---- | --------- | ------ | --- | ---------- | --- | ---- | --------------------------------------- | ------ | -------- | ----- | ------ | ---- |
| Most | recently, | Devlin | et  | al. (2018) | and | Lam- |                                         |        |          |       |        |      |
|      |           |        |     |            |     |      | guagesonover25billionparallelsentences. |        |          |       |        | Sid- |
ple and Conneau (2019) introduced mBERT and dhantetal.(2019)furtheranalyzetherepresenta-
XLM-maskedlanguagemodelstrainedonmulti- tionsobtainedbytheencoderofamassivelymulti-
| ple languages, |     | without | any | cross-lingual |     | supervi- |     |     |     |     |     |     |
| -------------- | --- | ------- | --- | ------------- | --- | -------- | --- | --- | --- | --- | --- | --- |
lingualmachinetranslationsystemandshowthatit
sion. LampleandConneau(2019)proposetransla- obtainssimilarresultstomBERToncross-lingual
tionlanguagemodeling(TLM)asawaytoleverage NLI.Ourwork,incontrast,focusesontheunsuper-
paralleldataandobtainanewstateoftheartonthe visedlearningofcross-lingualrepresentationsand
| cross-lingual |     | natural | language | inference |     | (XNLI) |     |     |     |     |     |     |
| ------------- | --- | ------- | -------- | --------- | --- | ------ | --- | --- | --- | --- | --- | --- |
theirtransfertodiscriminativetasks.
| benchmark   | (Conneau     |     | et al., | 2018).          | They | further |                |     |     |     |     |     |
| ----------- | ------------ | --- | ------- | --------------- | ---- | ------- | -------------- | --- | --- | --- | --- | --- |
|             |              |     |         |                 |      |         | 3 ModelandData |     |     |     |     |     |
| show strong | improvements |     |         | on unsupervised |      | ma-     |                |     |     |     |     |     |
chinetranslationandpretrainingforsequencegen-
|     |     |     |     |     |     |     | In this section, | we  | present | the training | objective, |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------- | ------------ | ---------- | --- |
eration. Wuetal.(2019)showsthatmonolingual
|     |     |     |     |     |     |     | languages,anddataweuse. |     |     | WefollowtheXLM |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | -------------- | --- | --- |
BERTrepresentationsaresimilaracrosslanguages,
approach(LampleandConneau,2019)asclosely
explaininginpartthenaturalemergenceofmulti-
aspossible,onlyintroducingchangesthatimprove
| linguality | in bottleneck |     | architectures. |     | Separately, |     |     |     |     |     |     |     |
| ---------- | ------------- | --- | -------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
performanceatscale.
Piresetal.(2019)demonstratedtheeffectiveness
ofmultilingualmodelslikemBERTonsequencela- Masked Language Models. We use a Trans-
belingtasks. Huangetal.(2019)showedgainsover formermodel(Vaswanietal.,2017)trainedwith
XLMusingcross-lingualmulti-tasklearning,and the multilingual MLM objective (Devlin et al.,
Singhetal.(2019)demonstratedtheefficiencyof 2018; Lample and Conneau, 2019) using only
cross-lingualdataaugmentationforcross-lingual monolingualdata. Wesamplestreamsoftextfrom
NLI.However,allofthisworkwasatarelatively each language and train the model to predict the
modest scale, in terms of the amount of training maskedtokensintheinput. Weapplysubwordtok-
8441

103
)BG ni( ezis tesataD
102
101
100
10-1
ne ur di iv af ku vs ht ed or uh gb rf if ok se on tp le hz ad lp eh ti ln ra ks ih rh rt sc tl at ac ls ak rs vl nb sm lm za kk te ru yh qs km et eb en is si nk lt lg nm rm al ue ug ws mk yk oe ma ap yc sp zu ro ag ym uk os gu as iy gm yf dg rb sb sa us
|     |     | aj  |     |     |             |           |     | fa  |     | vj  |     |
| --- | --- | --- | --- | --- | ----------- | --------- | --- | --- | --- | --- | --- |
|     |     |     |     |     | CommonCrawl | Wikipedia |     |     |     |     |     |
Figure1: AmountofdatainGiB(log-scale)forthe88languagesthatappearinboththeWiki-100corpususedfor
mBERTandXLM-100,andtheCC-100usedforXLM-R.CC-100increasestheamountofdatabyseveralorders
ofmagnitude,inparticularforlow-resourcelanguages.
enizationdirectlyonrawtextdatausingSentence ScalingtheAmountofTrainingData. Follow-
Piece(KudoandRichardson,2018)withaunigram ingWenzeketal.(2019)2,webuildacleanCom-
languagemodel(Kudo,2018). Wesamplebatches monCrawl Corpus in 100 languages. We use an
fromdifferentlanguagesusingthesamesampling internallanguageidentificationmodelincombina-
distribution as Lample and Conneau (2019), but tionwiththeonefromfastText(Joulinetal.,2017).
withα = 0.3. UnlikeLampleandConneau(2019), Wetrainlanguagemodelsineachlanguageanduse
wedonotuselanguageembeddings,whichallows ittofilterdocumentsasdescribedinWenzeketal.
ourmodeltobetterdealwithcode-switching. We (2019). WeconsideroneCommonCrawldumpfor
usealargevocabularysizeof250Kwithafullsoft- Englishandtwelvedumpsforallotherlanguages,
maxandtraintwodifferentmodels: XLM-R (L which significantly increases dataset sizes, espe-
Base
=12,H=768,A=12,270Mparams)andXLM-R
ciallyforlow-resourcelanguageslikeBurmeseand
| (L=24,H=1024,A=16,550Mparams). |     |     |     |     | Forall | Swahili. |     |     |     |     |     |
| ------------------------------ | --- | --- | --- | --- | ------ | -------- | --- | --- | --- | --- | --- |
ofourablationstudies,weuseaBERT architec- Figure 1 shows the difference in size between
Base
turewithavocabularyof150Ktokens. AppendixB theWikipediaCorpususedbymBERTandXLM-
goesintomoredetailsaboutthearchitectureofthe 100, and the CommonCrawl Corpus we use. As
differentmodelsreferencedinthispaper. we show in Section 5.3, monolingual Wikipedia
corporaaretoosmalltoenableunsupervisedrep-
| Scaling | to a | hundred | languages. |     | XLM-R is |             |           |       |        |              |     |
| ------- | ---- | ------- | ---------- | --- | -------- | ----------- | --------- | ----- | ------ | ------------ | --- |
|         |      |         |            |     |          | resentation | learning. | Based | on our | experiments, |     |
trainedon100languages;weprovideafulllistof we found that a few hundred MiB of text data is
languagesandassociatedstatisticsinAppendixA.
usuallyaminimalsizeforlearningaBERTmodel.
| Figure                              | 1 specifies | the | iso codes   | of  | 88 languages   |              |     |     |     |     |     |
| ----------------------------------- | ----------- | --- | ----------- | --- | -------------- | ------------ | --- | --- | --- | --- | --- |
| thataresharedacrossXLM-RandXLM-100, |             |     |             |     | the            | 4 Evaluation |     |     |     |     |     |
| model                               | from Lample |     | and Conneau |     | (2019) trained |              |     |     |     |     |     |
onWikipediatextin100languages. Weconsiderfourevaluationbenchmarks. Forcross-
lingualunderstanding,weusecross-lingualnatural
| Compared |     | to previous | work, | we  | replace some |     |     |     |     |     |     |
| -------- | --- | ----------- | ----- | --- | ------------ | --- | --- | --- | --- | --- | --- |
languageinference,namedentityrecognition,and
| languages | with | more | commonly | used | ones such |     |     |     |     |     |     |
| --------- | ---- | ---- | -------- | ---- | --------- | --- | --- | --- | --- | --- | --- |
as romanized Hindi and traditional Chinese. In questionanswering. WeusetheGLUEbenchmark
toevaluatetheEnglishperformanceofXLM-Rand
ourablationstudies,wealwaysincludethe7lan-
compareittootherstate-of-the-artmodels.
| guages                              | for which | we       | have     | classification | and se-     |               |                                |     |          |           |     |
| ----------------------------------- | --------- | -------- | -------- | -------------- | ----------- | ------------- | ------------------------------ | --- | -------- | --------- | --- |
| quencelabelingevaluationbenchmarks: |           |          |          |                | English,    |               |                                |     |          |           |     |
|                                     |           |          |          |                |             | Cross-lingual | Natural                        |     | Language | Inference |     |
| French,                             | German,   | Russian, | Chinese, |                | Swahili and |               |                                |     |          |           |     |
|                                     |           |          |          |                |             | (XNLI).       | TheXNLIdatasetcomeswithground- |     |          |           |     |
Urdu. Wechosethissetasitcoversasuitablerange
|     |     |     |     |     |     | truth dev | and test | sets | in 15 languages, |     | and a |
| --- | --- | --- | --- | --- | --- | --------- | -------- | ---- | ---------------- | --- | ----- |
oflanguagefamiliesandincludeslow-resourcelan-
|                             |     |         |        |                |            | ground-truthEnglishtrainingset. |                    |           | Thetrainingset |           |     |
| --------------------------- | --- | ------- | ------ | -------------- | ---------- | ------------------------------- | ------------------ | --------- | -------------- | --------- | --- |
| guagessuchasSwahiliandUrdu. |     |         |        | Wealsoconsider |            |                                 |                    |           |                |           |     |
|                             |     |         |        |                |            | has been                        | machine-translated |           | to the         | remaining | 14  |
| larger sets                 | of  | 15, 30, | 60 and | all 100        | languages. |                                 |                    |           |                |           |     |
|                             |     |         |        |                |            | languages,                      | providing          | synthetic | training       | data      | for |
Whenreportingresultsonhigh-resourceandlow-
|           |     |          |             |     |             | these languages | as  | well. | We evaluate | our | model |
| --------- | --- | -------- | ----------- | --- | ----------- | --------------- | --- | ----- | ----------- | --- | ----- |
| resource, | we  | refer to | the average | of  | English and |                 |     |       |             |     |       |
oncross-lingualtransferfromEnglishtootherlan-
Frenchresults,andtheaverageofSwahiliandUrdu
resultsrespectively. 2 https://github.com/facebookresearch/ccnet
8442

guages. Wealsoconsiderthreemachinetranslation 2019)hasfocusedonanalyzingtheperformanceof
baselines: (i) translate-test: dev and test sets are fixed pretrained models on downstream tasks. In
machine-translatedtoEnglishandasingleEnglish thissection,wepresentacomprehensivestudyof
model is used (ii) translate-train (per-language): differentfactorsthatareimportanttopretraining
the English training set is machine-translated largescalemultilingualmodels. Wehighlightthe
to each language and we fine-tune a multiligual trade-offs and limitations of these models as we
modeloneachtrainingset(iii)translate-train-all scaletoonehundredlanguages.
| (multi-language): |                      | we  | fine-tune | a      | multilingual |      |                   |     |           |     |       |         |
| ----------------- | -------------------- | --- | --------- | ------ | ------------ | ---- | ----------------- | --- | --------- | --- | ----- | ------- |
|                   |                      |     |           |        |              |      | Transfer-dilution |     | Trade-off | and | Curse | of Mul- |
| model             | on the concatenation |     |           | of all | training     | sets |                   |     |           |     |       |         |
from translate-train. For the translations, we use tilinguality. Modelcapacity(i.e. thenumberof
theofficialdataprovidedbytheXNLIproject. parametersinthemodel)isconstrainedduetoprac-
ticalconsiderationssuchasmemoryandspeeddur-
| Named | Entity | Recognition. |     | For NER, | we  | con- |                          |     |     |                      |     |     |
| ----- | ------ | ------------ | --- | -------- | --- | ---- | ------------------------ | --- | --- | -------------------- | --- | --- |
|       |        |              |     |          |     |      | ingtrainingandinference. |     |     | Forafixedsizedmodel, |     |     |
sidertheCoNLL-2002(Sang,2002)andCoNLL-
theper-languagecapacitydecreasesasweincrease
| 2003 (Tjong | Kim         | Sang   | and De  | Meulder, |             | 2003) |                       |     |     |                       |     |     |
| ----------- | ----------- | ------ | ------- | -------- | ----------- | ----- | --------------------- | --- | --- | --------------------- | --- | --- |
|             |             |        |         |          |             |       | thenumberoflanguages. |     |     | Whilelow-resourcelan- |     |     |
| datasets    | in English, | Dutch, | Spanish |          | and German. |       |                       |     |     |                       |     |     |
guageperformancecanbeimprovedbyaddingsim-
Wefine-tunemultilingualmodelseither(1)onthe
ilarhigher-resourcelanguagesduringpretraining,
| English | set to evaluate |     | cross-lingual |     | transfer, | (2) |     |     |     |     |     |     |
| ------- | --------------- | --- | ------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
theoveralldownstreamperformancesuffersfrom
oneachsettoevaluateper-languageperformance, this capacity dilution (Arivazhagan et al., 2019).
or(3)onallsetstoevaluatemultilinguallearning.
|     |     |     |     |     |     |     | Positive | transfer | and capacity |     | dilution | have to be |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | ------------ | --- | -------- | ---------- |
WereporttheF1score,andcomparetobaselines
tradedoffagainsteachother.
fromLampleetal.(2016)andAkbiketal.(2018).
|                                 |     |     |     |     |          |     | We illustrate                 |             | this trade-off |     | in Figure      | 2, which |
| ------------------------------- | --- | --- | --- | --- | -------- | --- | ----------------------------- | ----------- | -------------- | --- | -------------- | -------- |
|                                 |     |     |     |     |          |     | shows XNLI                    | performance |                | vs  | the number     | of lan-  |
| Cross-lingualQuestionAnswering. |     |     |     |     | Weusethe |     |                               |             |                |     |                |          |
|                                 |     |     |     |     |          |     | guagesthemodelispretrainedon. |             |                |     | Initially,aswe |          |
MLQAbenchmarkfromLewisetal.(2019),which
extendstheEnglishSQuADbenchmarktoSpanish, go from 7 to 15 languages, the model is able to
German,Arabic,Hindi,VietnameseandChinese. takeadvantageofpositivetransferwhichimproves
performance,especiallyonlowresourcelanguages.
WereporttheF1scoreaswellastheexactmatch
(EM)scoreforcross-lingualtransferfromEnglish. Beyondthispointthecurseofmultilingualitykicks
inanddegradesperformanceacrossalllanguages.
GLUEBenchmark. Finally,weevaluatetheEn- Specifically,theoverallXNLIaccuracydecreases
| glish performance |     | of our | model | on  | the GLUE |     |            |     |       |          |      |          |
| ----------------- | --- | ------ | ----- | --- | -------- | --- | ---------- | --- | ----- | -------- | ---- | -------- |
|                   |     |        |       |     |          |     | from 71.8% | to  | 67.7% | as we go | from | XLM-7 to |
benchmark(Wangetal.,2018)whichgathersmul-
|     |     |     |     |     |     |     | XLM-100. | The | same | trend can | be observed | for |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | ---- | --------- | ----------- | --- |
tipleclassificationtasks,suchasMNLI(Williams
modelstrainedonthelargerCommonCrawlCor-
| et al., | 2017), | SST-2 (Socher |     | et al., | 2013), | or  |     |     |     |     |     |     |
| ------- | ------ | ------------- | --- | ------- | ------ | --- | --- | --- | --- | --- | --- | --- |
pus.
| QNLI(Rajpurkaretal.,2018). |     |     |     | WeuseBERT |     |       |                                       |     |     |     |     |     |
| -------------------------- | --- | --- | --- | --------- | --- | ----- | ------------------------------------- | --- | --- | --- | --- | --- |
|                            |     |     |     |           |     | Large | Theissueisevenmoreprominentwhentheca- |     |     |     |     |     |
andRoBERTaasbaselines.
|     |     |     |     |     |     |     | pacity of | the model | is  | small. | To show | this, we |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------- | --- | ------ | ------- | -------- |
5 AnalysisandResults pretrain models on Wikipedia Data in 7, 30 and
|     |     |     |     |     |     |     | 100 languages. |     | As we | add more | languages, | we  |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ----- | -------- | ---------- | --- |
Inthissection,weperformacomprehensiveanal- maketheTransformerwiderbyincreasingthehid-
ysisofmultilingualmaskedlanguagemodels. We densizefrom768to960to1152. InFigure4,we
conductmostoftheanalysisonXNLI,whichwe showthattheaddedcapacityallowsXLM-30tobe
foundtoberepresentativeofourfindingsonother onparwithXLM-7,thusovercomingthecurseof
tasks. We then present the results of XLM-R on multilinguality. TheaddedcapacityforXLM-100,
| cross-lingual | understanding |     | and | GLUE. | Finally, |     |     |     |     |     |     |     |
| ------------- | ------------- | --- | --- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- |
however,isnotenoughanditstilllagsbehinddue
wecomparemultilingualandmonolingualmodels, tohighervocabularydilution(recallfromSection3
andpresentresultsonlow-resourcelanguages. that we used a fixed vocabulary size of 150K for
allmodels).
5.1 ImprovingandUnderstanding
MultilingualMaskedLanguageModels
|     |     |     |     |     |     |     | High-resource |     | vs  | Low-resource |     | Trade-off. |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | ------------ | --- | ---------- |
Muchoftheworkdoneonunderstandingthecross- The allocation of the model capacity across
lingual effectiveness of mBERT or XLM (Pires languagesiscontrolledbyseveralparameters: the
et al., 2019; Wu and Dredze, 2019; Lewis et al., training set size, the size of the shared subword
8443

80
70
60
50
40
7 15 30 60 100
Number of languages
8444
ycaruccA
80
70
60
50
40
Low res. High res. All
Low res. High res. All
Figure 2: The transfer-
interference trade-off: Low-
resource languages benefit from
scaling to more languages, until
dilution (interference) kicks in
anddegradesoverallperformance.
ycaruccA
74
72
70
68
66
7 30 100
Number of languages
Wikipedia CommonCrawl
Figure 3: Wikipedia versus Com-
monCrawl: An XLM-7 obtains
significantly better performance
when trained on CC, in particular
onlow-resourcelanguages.
ycaruccA
Fixed capacity Increased capacity
Figure4:Addingmorecapacityto
the model alleviates the curse of
multilinguality, but remains an is-
sueformodelsofmoderatesize.
80
70
60
50
40
0.01 0.3 0.7 1.0
Language sampling
ycaruccA
68
66
64
62
60
32k 64k 128k256k 512k
Vocabulary size
Low res. High res. All
Figure 5: On the high-resource
versuslow-resourcetrade-off: im-
pact of batch language sampling
forXLM-100.
ycaruccA
68
66
64
62
60
2048 4096 8192 BPE SPM
Batch size Preproc.
Fixed capacity Increased capacity
Figure6:Ontheimpactofvocabu-
larysizeatfixedcapacityandwith
increasing capacity for XLM-100.
ycaruccA
.
Figure 7: On the impact of large-
scale training, and preprocessing
simplificationfromBPEwithtok-
enizationtoSPMonrawtextdata.
vocabulary, and the rate at which we sample shared vocabulary (the vocabulary capacity) can
trainingexamplesfromeachlanguage. Westudy improvetheperformanceofmultilingualmodelson
theeffectofsamplingontheperformanceofhigh- downstreamtasks. Toillustratethiseffect,wetrain
resource (English and French) and low-resource XLM-100modelsonWikipediadatawithdifferent
(Swahili and Urdu) languages for an XLM-100 vocabulary sizes. We keep the overall number of
modeltrainedonWikipedia(weobserveasimilar parametersconstantbyadjustingthewidthofthe
trend for the construction of the subword vocab). transformer. Figure6showsthatevenwithafixed
Specifically,weinvestigatetheimpactofvarying capacity,weobservea2.8%increaseinXNLIav-
the α parameter which controls the exponential erageaccuracyasweincreasethevocabularysize
smoothingofthelanguagesamplingrate. Similar from32Kto256K.Thissuggeststhatmultilingual
toLampleandConneau(2019),weuseasampling models can benefit from allocating a higher pro-
rate proportional to the number of sentences in portion of the total number of parameters to the
each corpus. Models trained with higher values embeddinglayereventhoughthisreducesthesize
ofαseebatchesofhigh-resourcelanguagesmore of the Transformer. For simplicity and given the
often. Figure 5 shows that the higher the value softmaxcomputationalconstraints,weuseavocab-
ofα,thebettertheperformanceonhigh-resource ularyof250kforXLM-R.
languages, and vice-versa. When considering
overallperformance,wefound0.3tobeanoptimal
We further illustrate the importance of this pa-
valueforα,andusethisforXLM-R.
rameter, by training three models with the same
Importance of Capacity and Vocabulary. In transformerarchitecture(BERT )butwithdif-
Base
previoussectionsandinFigure4,weshowedthe ferent vocabulary sizes: 128K, 256K and 512K.
importanceofscalingthemodelsizeasweincrease Weobservemorethan3%gainsinoverallaccuracy
the number of languages. Similar to the overall onXNLIbysimplyincreasingthevocabsizefrom
model size, we argue that scaling the size of the 128kto512k.

Larger-scaleDatasetsandTraining. Asshown performsallprevioustechniquesoncross-lingual
inFigure1,theCommonCrawlCorpusthatwecol- benchmarkswhilegettingperformanceonparwith
lectedhassignificantlymoremonolingualdatathan RoBERTaontheGLUEbenchmark.
| the previously |     | used Wikipedia |     | corpora. |     | Figure 3 |     |     |     |     |     |     |
| -------------- | --- | -------------- | --- | -------- | --- | -------- | --- | --- | --- | --- | --- | --- |
showsthatforthesameBERT architecture,all XNLI. Table 1 shows XNLI results and adds
Base
|        |         |                |     |     |        |          | someadditionaldetails: |     |     | (i)thenumberofmodels |     |     |
| ------ | ------- | -------------- | --- | --- | ------ | -------- | ---------------------- | --- | --- | -------------------- | --- | --- |
| models | trained | on CommonCrawl |     |     | obtain | signifi- |                        |     |     |                      |     |     |
cantlybetterperformance. theapproachinduces(#M),(ii)thedataonwhich
Apart from scaling the training data, Liu et al. themodelwastrained(D),and(iii)thenumberof
|     |     |     |     |     |     |     | languagesthemodelwaspretrained |     |     |     |     | on(#lg). As |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- | ----------- |
(2019)alsoshowedthebenefitsoftrainingMLMs
|         |        |              |     |             |     |         | we show | in our | results, | these | parameters | signifi- |
| ------- | ------ | ------------ | --- | ----------- | --- | ------- | ------- | ------ | -------- | ----- | ---------- | -------- |
| longer. | In our | experiments, |     | we observed |     | similar |         |        |          |       |            |          |
effects of large-scale training, such as increasing cantlyimpactperformance. Column#Mspecifies
batch size (see Figure 7) and training time, on whether model selection was done separately on
|       |              |     |               |     |          |      | the dev | set of | each | language | (N models), | or on |
| ----- | ------------ | --- | ------------- | --- | -------- | ---- | ------- | ------ | ---- | -------- | ----------- | ----- |
| model | performance. |     | Specifically, |     | we found | that |         |        |      |          |             |       |
usingvalidationperplexityasastoppingcriterion thejointdevsetofallthelanguages(singlemodel).
for pretraining caused the multilingual MLM in Weobservea0.6decreaseinoverallaccuracywhen
|        |             |             |        |     |                 |     | we go from      | N   | models                    | to  | a single model | - going |
| ------ | ----------- | ----------- | ------ | --- | --------------- | --- | --------------- | --- | ------------------------- | --- | -------------- | ------- |
| Lample | and         | Conneau     | (2019) | to  | be under-tuned. |     |                 |     |                           |     |                |         |
|        |             |             |        |     |                 |     | from71.3to70.7. |     | Weencouragethecommunityto |     |                |         |
| In our | experience, | performance |        |     | on downstream   |     |                 |     |                           |     |                |         |
tasks continues to improve even after validation adoptthissetting. Forcross-lingualtransfer,while
perplexityhasplateaued. Combiningthisobserva- this approach is not fully zero-shot transfer, we
arguethatinrealapplications,asmallamountof
tionwithourimplementationoftheunsupervised
XLM-MLM objective, we were able to improve superviseddataisoftenavailableforvalidationin
| the performance |     | of Lample |     | and Conneau |     | (2019) | eachlanguage. |     |     |     |     |     |
| --------------- | --- | --------- | --- | ----------- | --- | ------ | ------------- | --- | --- | --- | --- | --- |
from 71.3% to more than 75% average accuracy XLM-RsetsanewstateoftheartonXNLI.On
onXNLI,whichwasonparwiththeirsupervised cross-lingualtransfer,XLM-Robtains80.9%accu-
translation language modeling (TLM) objective. racy, outperforming the XLM-100 and mBERT
Based on these results, and given our focus on open-source models by 10.2% and 14.6% aver-
|              |     |           |     |         |        |         | age accuracy. |     | On  | the Swahili | and | Urdu low- |
| ------------ | --- | --------- | --- | ------- | ------ | ------- | ------------- | --- | --- | ----------- | --- | --------- |
| unsupervised |     | learning, | we  | decided | to not | use the |               |     |     |             |     |           |
supervisedTLMobjectivefortrainingourmodels. resourcelanguages,XLM-RoutperformsXLM-100
by15.7%and11.4%,andmBERTby23.5%and
| Simplifying |     | Multilingual |     | Tokenization |     | with |        |                                  |     |     |     |     |
| ----------- | --- | ------------ | --- | ------------ | --- | ---- | ------ | -------------------------------- | --- | --- | --- | --- |
|             |     |              |     |              |     |      | 15.8%. | WhileXLM-Rhandles100languages,we |     |     |     |     |
SentencePiece. Thedifferentlanguage-specific also show that it outperforms the former state of
tokenizationtoolsusedbymBERTandXLM-100
|            |        |      |           |     |        |        | the art | Unicoder | (Huang | et  | al., 2019) | and XLM |
| ---------- | ------ | ---- | --------- | --- | ------ | ------ | ------- | -------- | ------ | --- | ---------- | ------- |
| make these | models | more | difficult |     | to use | on raw |         |          |        |     |            |         |
(MLM+TLM),whichhandleonly15languages,by
text. Instead, we train a Sentence Piece model 5.5%and5.8%averageaccuracyrespectively. Us-
| (SPM) | and apply | it directly |     | on raw | text | data for |     |     |     |     |     |     |
| ----- | --------- | ----------- | --- | ------ | ---- | -------- | --- | --- | --- | --- | --- | --- |
ingthemultilingualtrainingoftranslate-train-all,
| alllanguages. |     | Wedidnotobserveanylossinper- |     |     |     |     |     |     |     |     |     |     |
| ------------- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
XLM-Rfurtherimprovesperformanceandreaches
formanceformodelstrainedwithSPMwhencom-
83.6%accuracy,anewoverallstateoftheartfor
paredtomodelstrainedwithlanguage-specificpre- XNLI, outperforming Unicoder by 5.1%. Multi-
| processing | and | byte-pair | encoding |     | (see Figure | 7)  |     |     |     |     |     |     |
| ---------- | --- | --------- | -------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
lingualtrainingissimilartopracticalapplications
andhenceuseSPMforXLM-R.
|     |     |     |     |     |     |     | where training |         | sets | are available | in          | various lan- |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ------- | ---- | ------------- | ----------- | ------------ |
|     |     |     |     |     |     |     | guages         | for the | same | task.         | In the case | of XNLI,     |
5.2 Cross-lingualUnderstandingResults
|     |     |     |     |     |     |     | datasets | have | been translated, |     | and translate-train- |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---- | ---------------- | --- | -------------------- | --- |
Basedontheseresults,weadaptthesettingofLam-
allcanbeseenassomeformofcross-lingualdata
| ple and | Conneau | (2019) | and | use | a large | Trans- |     |     |     |     |     |     |
| ------- | ------- | ------ | --- | --- | ------- | ------ | --- | --- | --- | --- | --- | --- |
augmentation(Singhetal.,2019),similartoback-
former model with 24 layers and 1024 hidden translation(Xieetal.,2019).
| states,witha250kvocabulary. |     |     |     | Weusethemulti- |     |     |     |     |     |     |     |     |
| --------------------------- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
lingualMLMlossandtrainourXLM-Rmodelfor Named Entity Recognition. In Table 2, we re-
1.5Millionupdatesonfive-hundred32GBNvidia port results of XLM-R and mBERT on CoNLL-
V100GPUswithabatchsizeof8192. Weleverage 2002 and CoNLL-2003. We consider the LSTM
the SPM-preprocessed text data from Common- + CRF approach from Lample et al. (2016) and
Crawlin100languagesandsamplelanguageswith theFlairmodelfromAkbiketal.(2018)asbase-
α = 0.3. In this section, we show that it out- lines. We evaluate the performance of the model
8445

Model D #M #lg en fr es de el bg ru tr ar vi th zh hi sw ur Avg
Fine-tunemultilingualmodelonEnglishtrainingset(Cross-lingualTransfer)
LampleandConneau(2019) Wiki+MT N 15 85.0 78.7 78.9 77.8 76.6 77.4 75.3 72.5 73.1 76.1 73.2 76.5 69.6 68.4 67.3 75.1
Huangetal.(2019) Wiki+MT N 15 85.1 79.0 79.4 77.8 77.2 77.2 76.3 72.8 73.5 76.4 73.6 76.2 69.4 69.7 66.7 75.4
Devlinetal.(2018) Wiki N 102 82.1 73.8 74.3 71.1 66.4 68.9 69.0 61.6 64.9 69.5 55.8 69.3 60.0 50.4 58.0 66.3
LampleandConneau(2019) Wiki N 100 83.7 76.2 76.6 73.7 72.4 73.0 72.1 68.1 68.4 72.0 68.2 71.5 64.5 58.0 62.4 71.3
LampleandConneau(2019) Wiki 1 100 83.2 76.7 77.7 74.0 72.7 74.1 72.7 68.7 68.6 72.9 68.9 72.5 65.6 58.2 62.4 70.7
XLM-RBase CC 1 100 85.8 79.7 80.7 78.7 77.5 79.6 78.1 74.2 73.8 76.5 74.6 76.7 72.4 66.5 68.3 76.2
XLM-R CC 1 100 89.1 84.1 85.1 83.9 82.9 84.0 81.2 79.6 79.8 80.8 78.1 80.2 76.9 73.9 73.8 80.9
TranslateeverythingtoEnglishanduseEnglish-onlymodel(TRANSLATE-TEST)
BERT-en Wiki 1 1 88.8 81.4 82.3 80.1 80.3 80.9 76.2 76.0 75.4 72.0 71.9 75.6 70.0 65.8 65.8 76.2
RoBERTa Wiki+CC 1 1 91.3 82.9 84.3 81.2 81.7 83.1 78.3 76.8 76.6 74.2 74.1 77.5 70.9 66.7 66.8 77.8
Fine-tunemultilingualmodeloneachtrainingset(TRANSLATE-TRAIN)
LampleandConneau(2019) Wiki N 100 82.9 77.6 77.9 77.9 77.1 75.7 75.5 72.6 71.2 75.8 73.1 76.2 70.4 66.5 62.4 74.2
Fine-tunemultilingualmodelonalltrainingsets(TRANSLATE-TRAIN-ALL)
LampleandConneau(2019)† Wiki+MT 1 15 85.0 80.8 81.3 80.3 79.1 80.9 78.3 75.6 77.6 78.5 76.0 79.5 72.9 72.8 68.5 77.8
Huangetal.(2019) Wiki+MT 1 15 85.6 81.1 82.3 80.9 79.5 81.4 79.7 76.8 78.2 77.9 77.1 80.5 73.4 73.8 69.6 78.5
LampleandConneau(2019) Wiki 1 100 84.5 80.1 81.3 79.3 78.6 79.4 77.5 75.2 75.6 78.3 75.7 78.3 72.1 69.2 67.7 76.9
XLM-RBase CC 1 100 85.4 81.4 82.2 80.3 80.4 81.3 79.7 78.6 77.3 79.7 77.9 80.2 76.1 73.1 73.0 79.1
XLM-R CC 1 100 89.1 85.1 86.6 85.7 85.3 85.9 83.5 83.2 83.1 83.7 81.5 83.7 81.6 78.0 78.1 83.6
Table1:Resultsoncross-lingualclassification.Wereporttheaccuracyoneachofthe15XNLIlanguagesandthe
averageaccuracy. WespecifythedatasetDusedforpretraining,thenumberofmodels#Mtheapproachrequires
and the number of languages #lg the model handles. Our XLM-R results are averaged over five different seeds.
Weshowthatusingthetranslate-train-allapproachwhichleveragestrainingsetsfrommultiplelanguages,XLM-R
obtainsanewstateoftheartonXNLIof83.6%averageaccuracy. Resultswith†arefromHuangetal.(2019).
Model train #M en nl es de Avg cross-lingualtransferapproachby8.49%.
| Lampleetal.(2016) | each N 90.74 | 81.74 85.75 78.76 | 84.25 |     |     |     |
| ----------------- | ------------ | ----------------- | ----- | --- | --- | --- |
Akbiketal.(2018) each N 93.18 90.44 - 88.27 - QuestionAnswering. Wealsoobtainnewstate
mBERT† each N 91.97 90.94 87.38 82.82 88.28 oftheartresultsontheMLQAcross-lingualques-
|     | en 1 91.97   | 77.57 74.96 69.56 | 78.52          |            |            |          |
| --- | ------------ | ----------------- | -------------- | ---------- | ---------- | -------- |
|     |              |                   | tion answering | benchmark, | introduced | by Lewis |
|     | each N 92.25 | 90.39 87.99 84.60 | 88.81          |            |            |          |
XLM-RBase en 1 92.25 78.08 76.53 69.60 79.11 etal.(2019). Wefollowtheirprocedurebytraining
|     | all 1 91.08 | 89.09 87.28 83.17 | 87.66 |     |     |     |
| --- | ----------- | ----------------- | ----- | --- | --- | --- |
ontheEnglishtrainingdataandevaluatingonthe
|     | each N 92.92 | 92.53 89.72 85.81 | 90.24 |     |     |     |
| --- | ------------ | ----------------- | ----- | --- | --- | --- |
XLM-R en 1 92.92 80.80 78.64 71.40 80.94 7 languages of the dataset. We report results in
|     | all 1 92.00 | 91.60 89.52 84.60 | 89.43   |                                   |     |     |
| --- | ----------- | ----------------- | ------- | --------------------------------- | --- | --- |
|     |             |                   | Table3. | XLM-RobtainsF1andaccuracyscoresof |     |     |
70.7%and52.7%whilethepreviousstateoftheart
| Table 2: | Results on named | entity recognition | on  |     |     |     |
| -------- | ---------------- | ------------------ | --- | --- | --- | --- |
CoNLL-2002 and CoNLL-2003 (F1 score). Results was 61.6% and 43.5%. XLM-R also outperforms
| with † | are from Wu and Dredze | (2019). | Note that |                   |           |           |
| ------ | ---------------------- | ------- | --------- | ----------------- | --------- | --------- |
|        |                        |         | mBERT     | by 13.0% F1-score | and 11.1% | accuracy. |
mBERTandXLM-Rdonotusealinear-chainCRF,as ItevenoutperformsBERT-LargeonEnglish,con-
opposedtoAkbiketal.(2018)andLampleetal.(2016).
firmingitsstrongmonolingualperformance.
|         |                         |          | 5.3 MultilingualversusMonolingual |                                |     |     |
| ------- | ----------------------- | -------- | --------------------------------- | ------------------------------ | --- | --- |
| on each | of the target languages | in three | different                         |                                |     |     |
|         |                         |          | Inthissection,                    | wepresentresultsofmultilingual |     |     |
settings: (i)trainonEnglishdataonly(en)(ii)train XLMmodelsagainstmonolingualBERTmodels.
ondataintargetlanguage(each)(iii)trainondata
in all languages (all). Results of mBERT are re- GLUE: XLM-R versus RoBERTa. Our goal is
portedfromWuandDredze(2019). Notethatwe toobtainamultilingualmodelwithstrongperfor-
do not use a linear-chain CRF on top of XLM-R manceonboth,cross-lingualunderstandingtasks
andmBERTrepresentations,whichgivesanadvan- as well as natural language understanding tasks
tagetoAkbiketal.(2018). WithouttheCRF,our foreachlanguage. Tothatend,weevaluateXLM-
XLM-Rmodelstillperformsonparwiththestate RontheGLUEbenchmark. WeshowinTable4,
of the art, outperforming Akbik et al. (2018) on thatXLM-Robtainsbetteraveragedevperformance
Dutch by 2.09 points. On this task, XLM-R also thanBERT by1.6%andreachesperformance
Large
outperforms mBERT by 2.42 F1 on average for onparwithXLNet . TheRoBERTamodelout-
Large
cross-lingual transfer, and 1.86 F1 when trained performs XLM-R by only 1.0% on average. We
oneachlanguage. Trainingonalllanguagesleads believe future work can reduce this gap even fur-
toanaverageF1scoreof89.43%,outperforming therbyalleviatingthecurseofmultilingualityand
8446

| Model       |     | train #lgs | en        |     | es  | de  | ar  | hi  | vi  |     | zh  | Avg |
| ----------- | --- | ---------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BERT-Large† |     | en 1       | 80.2/67.4 |     | -   | -   | -   | -   | -   |     | -   | -   |
mBERT† en 102 77.7/65.2 64.3/46.6 57.9/44.3 45.7/29.8 43.8/29.7 57.1/38.6 57.5/37.3 57.7/41.6
XLM-15† en 15 74.9/62.4 68.0/49.8 62.2/47.6 54.8/36.3 48.8/27.3 61.4/41.8 61.1/39.6 61.6/43.5
XLM-RBase en 100 77.1/64.6 67.4/49.6 60.9/46.7 54.9/36.6 59.4/42.9 64.5/44.7 61.8/39.3 63.7/46.3
XLM-R en 100 80.6/67.8 74.1/56.0 68.5/53.6 63.1/43.5 69.2/51.6 71.3/50.9 68.0/45.4 70.7/52.7
Table 3: Results on MLQA question answering We report the F1 and EM (exact match) scores for zero-shot
classification where models are fine-tuned on the English Squad dataset and evaluated on the 7 languages of
MLQA.Resultswith†aretakenfromtheoriginalMLQApaperLewisetal.(2019).
vocabularydilution. Theseresultsdemonstratethe particulartaskcanovercomethecapacitydilution
possibility of learning one model for many lan- problemtoobtainbetteroverallperformance.
guageswhilemaintainingstrongperformanceon
per-languagedownstreamtasks. Model D #vocab en fr de ru zh sw ur Avg
Monolingualbaselines
|     |     |     |     |     |     |     | BERT Wiki | 40k 84.5 | 78.6 | 80.0 75.5 | 77.7 60.1 | 57.3 73.4 |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------- | ---- | --------- | --------- | --------- |
Model #lgs MNLI-m/mm QNLI QQP SST MRPC STS-B Avg CC 40k 86.7 81.2 81.2 78.2 79.5 70.8 65.1 77.5
BERTLarge † 1 86.6/- 92.3 91.3 93.2 88.0 90.0 90.2 Multilingualmodels(cross-lingualtransfer)
| XLNetLarge | † 1 | 89.8/- | 93.9 91.8 | 95.6 | 89.2 | 91.8 92.0 |     |     |     |     |     |     |
| ---------- | --- | ------ | --------- | ---- | ---- | --------- | --- | --- | --- | --- | --- | --- |
RoBERTa† 1 90.2/90.2 94.7 92.2 96.4 90.9 92.4 92.8 XLM-7 Wiki 150k 82.3 76.8 74.7 72.5 73.1 60.8 62.3 71.8
XLM-R 100 88.9/89.0 93.8 92.3 95.0 89.5 91.2 91.8 CC 150k 85.7 78.6 79.5 76.4 74.8 71.2 66.9 76.2
Multilingualmodels(translate-train-all)
| Table 4: | GLUE | dev results. |     | Results | with | † are from |            |           |      |           |         |           |
| -------- | ---- | ------------ | --- | ------- | ---- | ---------- | ---------- | --------- | ---- | --------- | ------- | --------- |
|          |      |              |     |         |      |            | XLM-7 Wiki | 150k 84.6 | 80.1 | 80.2 75.7 | 78 68.7 | 66.7 76.3 |
Liuetal.(2019).WecomparetheperformanceofXLM- CC 150k 87.2 82.5 82.9 79.7 80.4 75.7 71.5 80.0
| R to BERT |       | , XLNet | and RoBERTa |     | on the | English |          |              |        |             |     |        |
| --------- | ----- | ------- | ----------- | --- | ------ | ------- | -------- | ------------ | ------ | ----------- | --- | ------ |
|           | Large |         |             |     |        |         | Table 5: | Multilingual | versus | monolingual |     | models |
GLUEbenchmark.
(BERT-BASE).Wecomparetheperformanceofmono-
|     |     |     |     |     |     |     | lingual models | (BERT) | versus | multilingual |     | models |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ------ | ------ | ------------ | --- | ------ |
XNLI: XLM versus BERT. A recurrent criti- (XLM)onsevenlanguages,usingaBERT-BASEarchi-
cismagainstmultilingualmodelsisthattheyobtain
tecture. Wechooseavocabularysizeof40kand150k
worse performance than their monolingual coun- formonolingualandmultilingualmodels.
| terparts. | InadditiontothecomparisonofXLM-R |     |     |     |     |     |     |     |     |     |     |     |
| --------- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and RoBERTa, we provide the first comprehen- 5.4 RepresentationLearningfor
sivestudytoassessthisclaimontheXNLIbench-
Low-resourceLanguages
mark. Weextendourcomparisonbetweenmultilin-
|     |     |     |     |     |     |     | We observed | in  | Table | 5 that | pretraining | on  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----- | ------ | ----------- | --- |
gualXLMmodelsandmonolingualBERTmodels
|                |     |             |     |             |     |        | Wikipedia | for Swahili | and | Urdu | performed | sim- |
| -------------- | --- | ----------- | --- | ----------- | --- | ------ | --------- | ----------- | --- | ---- | --------- | ---- |
| on 7 languages |     | and compare |     | performance |     | in Ta- |           |             |     |      |           |      |
ilarlytoarandomlyinitializedmodel;mostlikely
ble5. Wetrain14monolingualBERTmodelson
duetothesmallsizeofthedatafortheselanguages.
WikipediaandCommonCrawl(cappedat60GiB),
|         |         |                  |     |          |     |            | On the other               | hand, | pretraining | on              | CC  | improved |
| ------- | ------- | ---------------- | --- | -------- | --- | ---------- | -------------------------- | ----- | ----------- | --------------- | --- | -------- |
| and two | XLM-7   | models.          | We  | increase |     | the vocab- |                            |       |             |                 |     |          |
|         |         |                  |     |          |     |            | performancebyupto10points. |       |             | Thisconfirmsour |     |          |
| ulary   | size of | the multilingual |     | model    | for | a better   |                            |       |             |                 |     |          |
assumptionthatmBERTandXLM-100relyheav-
| comparison. |     | We found | that | multilingual |     | models |     |     |     |     |     |     |
| ----------- | --- | -------- | ---- | ------------ | --- | ------ | --- | --- | --- | --- | --- | --- |
ilyoncross-lingualtransferbutdonotmodelthe
canoutperformtheirmonolingualBERTcounter-
low-resourcelanguagesaswellasXLM-R.Specifi-
| parts. | Specifically, | in  | Table | 5, we | show | that for |     |     |     |     |     |     |
| ------ | ------------- | --- | ----- | ----- | ---- | -------- | --- | --- | --- | --- | --- | --- |
cally,inthetranslate-train-allsetting,weobserve
cross-lingualtransfer,monolingualbaselinesout-
thatthebiggestgainsforXLMmodelstrainedon
| perform | XLM-7 | for both | Wikipedia |     | and | CC by |     |     |     |     |     |     |
| ------- | ----- | -------- | --------- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
CC,comparedtotheirWikipediacounterparts,are
| 1.6% | and 1.3% | average | accuracy. |     | However, | by  |     |     |     |     |     |     |
| ---- | -------- | ------- | --------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
onlow-resourcelanguages;7%and4.8%improve-
makinguseofmultilingualtraining(translate-train-
mentonSwahiliandUrdurespectively.
all)andleveragingtrainingsetscomingfrommul-
| tiplelanguages,XLM-7canoutperformtheBERT |     |     |     |     |     |     | 6 Conclusion |     |     |     |     |     |
| ---------------------------------------- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- |
models: ourXLM-7trainedonCCobtains80.0%
average accuracy on the 7 languages, while the Inthiswork,weintroducedXLM-R,ournewstate
averageperformanceofBERTmodelstrainedon of the art multilingual masked language model
CCis77.5%. Thisisasurprisingresultthatshows trained on 2.5 TB of newly created clean Com-
thatthecapacityofmultilingualmodelstoleverage monCrawldatain100languages. Weshowthatit
trainingdatacomingfrommultiplelanguagesfora provides strong gains over previous multilingual
8447

models like mBERT and XLM on classification, TakuKudo.2018. Subwordregularization: Improving
neuralnetworktranslationmodelswithmultiplesub-
| sequencelabelingandquestionanswering. |     |     |     |     |     | Weex- |     |     |     |     |     |     |
| ------------------------------------- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
posed the limitations of multilingual MLMs, in wordcandidates. InACL,pages66–75.
particularbyuncoveringthehigh-resourceversus TakuKudoandJohnRichardson.2018. Sentencepiece:
low-resourcetrade-off,thecurseofmultilinguality A simple and language independent subword tok-
|                    |     |     |                      |     |     |     | enizer and | detokenizer |     | for neural | text | processing. |
| ------------------ | --- | --- | -------------------- | --- | --- | --- | ---------- | ----------- | --- | ---------- | ---- | ----------- |
| and the importance |     | of  | key hyperparameters. |     |     | We  |            |             |     |            |      |             |
EMNLP.
alsoexposethesurprisingeffectivenessofmultilin-
gualmodelsovermonolingualmodels,andshow Guillaume Lample, Miguel Ballesteros, Sandeep Sub-
ramanian,KazuyaKawakami,andChrisDyer.2016.
strongimprovementsonlow-resourcelanguages.
|     |     |     |     |     |     |     | Neural    | architectures | for      | named | entity | recognition. |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------------- | -------- | ----- | ------ | ------------ |
|     |     |     |     |     |     |     | In NAACL, | pages         | 260–270, | San   | Diego, | California.  |
AssociationforComputationalLinguistics.
References
|                     |                          |         |            |            |              |           | Guillaume                        | Lample     | and Alexis | Conneau. | 2019.    | Cross-      |
| ------------------- | ------------------------ | ------- | ---------- | ---------- | ------------ | --------- | -------------------------------- | ---------- | ---------- | -------- | -------- | ----------- |
| Alan Akbik,         | Duncan                   | Blythe, |            | and Roland |              | Vollgraf. |                                  |            |            |          |          |             |
|                     |                          |         |            |            |              |           | linguallanguagemodelpretraining. |            |            |          | NeurIPS. |             |
| 2018.               | Contextual               | string  | embeddings |            | for sequence |           |                                  |            |            |          |          |             |
| labeling.           | InCOLING,pages1638–1649. |         |            |            |              |           |                                  |            |            |          |          |             |
|                     |                          |         |            |            |              |           | Patrick Lewis,                   | Barlas     | Og˘uz,     | Ruty     | Rinott,  | Sebastian   |
|                     |                          |         |            |            |              |           | Riedel,                          | and Holger | Schwenk.   | 2019.    |          | Mlqa: Eval- |
| Naveen Arivazhagan, |                          | Ankur   |            | Bapna,     | Orhan        | Firat,    |                                  |            |            |          |          |             |
|                     |                          |         |            |            |              |           | uating cross-lingual             |            | extractive | question |          | answering.  |
| Dmitry              | Lepikhin,                | Melvin  | Johnson,   |            | Maxim        | Krikun,   |                                  |            |            |          |          |             |
arXivpreprintarXiv:1910.07475.
| Mia Xu | Chen, | Yuan | Cao, | George | Foster, | Colin |     |     |     |     |     |     |
| ------ | ----- | ---- | ---- | ------ | ------- | ----- | --- | --- | --- | --- | --- | --- |
Cherry, et al. 2019. Massively multilingual neural YinhanLiu,MyleOtt,NamanGoyal,JingfeiDu,Man-
machine translation in the wild: Findings and chal- dar Joshi, Danqi Chen, Omer Levy, Mike Lewis,
lenges. arXivpreprintarXiv:1907.05019. Luke Zettlemoyer, and Veselin Stoyanov. 2019.
Roberta:ArobustlyoptimizedBERTpretrainingap-
| Samuel R.       | Bowman, | Gabor       | Angeli, | Christopher |         | Potts, |         |                                |     |     |     |     |
| --------------- | ------- | ----------- | ------- | ----------- | ------- | ------ | ------- | ------------------------------ | --- | --- | --- | --- |
|                 |         |             |         |             |         |        | proach. | arXivpreprintarXiv:1907.11692. |     |     |     |     |
| and Christopher |         | D. Manning. |         | 2015.       | A large | anno-  |         |                                |     |     |     |     |
tatedcorpusforlearningnaturallanguageinference.
TomasMikolov,QuocVLe,andIlyaSutskever.2013a.
InEMNLP.
|                 |     |              |           |     |         |     | Exploiting        | similarities |                               | among | languages | for ma- |
| --------------- | --- | ------------ | --------- | --- | ------- | --- | ----------------- | ------------ | ----------------------------- | ----- | --------- | ------- |
|                 |     |              |           |     |         |     | chinetranslation. |              | arXivpreprintarXiv:1309.4168. |       |           |         |
| Alexis Conneau, |     | Ruty Rinott, | Guillaume |     | Lample, | Ad- |                   |              |                               |       |           |         |
inaWilliams,SamuelR.Bowman,HolgerSchwenk,
TomasMikolov,IlyaSutskever,KaiChen,GregSCor-
andVeselinStoyanov.2018. Xnli: Evaluatingcross- rado, andJeffDean.2013b. Distributedrepresenta-
lingual sentence representations. In EMNLP. Asso- tionsofwordsandphrasesandtheircompositional-
ciationforComputationalLinguistics. ity. InNIPS,pages3111–3119.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and JeffreyPennington,RichardSocher,andChristopherD.
KristinaToutanova.2018. Bert:Pre-trainingofdeep Manning.2014. Glove:Globalvectorsforwordrep-
| bidirectional | transformers |     | for | language | understand- |     |              |                         |     |     |     |     |
| ------------- | ------------ | --- | --- | -------- | ----------- | --- | ------------ | ----------------------- | --- | --- | --- | --- |
|               |              |     |     |          |             |     | resentation. | InEMNLP,pages1532–1543. |     |     |     |     |
ing. NAACL.
|                |     |                   |     |         |        |     | MatthewEPeters, |             | MarkNeumann, |        | MohitIyyer, | Matt     |
| -------------- | --- | ----------------- | --- | ------- | ------ | --- | --------------- | ----------- | ------------ | ------ | ----------- | -------- |
| Edouard Grave, |     | Piotr Bojanowski, |     | Prakhar | Gupta, | Ar- |                 |             |              |        |             |          |
|                |     |                   |     |         |        |     | Gardner,        | Christopher | Clark,       | Kenton | Lee,        | and Luke |
mand Joulin, and Tomas Mikolov. 2018. Learning Zettlemoyer.2018. Deepcontextualizedwordrepre-
| wordvectorsfor157languages. |     |     |     | InLREC. |     |     | sentations. | NAACL. |     |     |     |     |
| --------------------------- | --- | --- | --- | ------- | --- | --- | ----------- | ------ | --- | --- | --- | --- |
HaoyangHuang,YaoboLiang,NanDuan,MingGong, Telmo Pires, Eva Schlinger, and Dan Garrette. 2019.
Linjun Shou, Daxin Jiang, and Ming Zhou. 2019. Howmultilingualismultilingualbert? InACL.
| Unicoder: | A   | universal | language | encoder |     | by pre- |     |     |     |     |     |     |
| --------- | --- | --------- | -------- | ------- | --- | ------- | --- | --- | --- | --- | --- | --- |
trainingwithmultiplecross-lingualtasks. ACL. Alec Radford, Karthik Narasimhan, Tim Salimans,
|     |     |     |     |     |     |     | and Ilya | Sutskever. | 2018. | Improving |     | language |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | ----- | --------- | --- | -------- |
Melvin Johnson, Mike Schuster, Quoc V Le, Maxim understanding by generative pre-training. URL
| Krikun, | YonghuiWu, |     | ZhifengChen, |     | NikhilThorat, |     |     |     |     |     |     |     |
| ------- | ---------- | --- | ------------ | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
https://s3-us-west-2.amazonaws.com/openai-
FernandaVie´gas,MartinWattenberg,GregCorrado, assets/research-covers/language-
et al. 2017. Google’s multilingual neural machine unsupervised/language understanding paper.pdf.
| translation | system: | Enabling |     | zero-shot | translation. |     |     |     |     |     |     |     |
| ----------- | ------- | -------- | --- | --------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
TACL,5:339–351. Alec Radford, Jeffrey Wu, Rewon Child, David Luan,
|     |     |     |     |     |     |     | DarioAmodei,andIlyaSutskever.2019. |     |     |     |     | Language |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | --- | -------- |
Armand Joulin, Edouard Grave, and Piotr Bo- modelsareunsupervisedmultitasklearners. OpenAI
| janowski | Tomas | Mikolov. | 2017. | Bag | of tricks | for | Blog,1(8). |     |     |     |     |     |
| -------- | ----- | -------- | ----- | --- | --------- | --- | ---------- | --- | --- | --- | --- | --- |
EACL2017,page427.
efficienttextclassification.
ColinRaffel,NoamShazeer,AdamRoberts,Katherine
RafalJozefowicz,OriolVinyals,MikeSchuster,Noam Lee, Sharan Narang, Michael Matena, Yanqi Zhou,
Shazeer, and Yonghui Wu. 2016. Exploring WeiLi,andPeterJ.Liu.2019. Exploringthelimits
the limits of language modeling. arXiv preprint of transfer learning with a unified text-to-text trans-
| arXiv:1602.02410. |     |     |     |     |     |     | former. | arXivpreprintarXiv:1910.10683. |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- | ------- | ------------------------------ | --- | --- | --- | --- |
8448

Pranav Rajpurkar, Robin Jia, and Percy Liang. 2018. Adina Williams, Nikita Nangia, and Samuel R Bow-
Know what you don’t know: Unanswerable ques- man. 2017. A broad-coverage challenge corpus
tionsforsquad. ACL. for sentence understanding through inference. Pro-
ceedingsofthe2ndWorkshoponEvaluatingVector-
PranavRajpurkar,JianZhang,KonstantinLopyrev,and SpaceRepresentationsforNLP.
| PercyLiang.2016. |     | SQuAD:100,000+questionsfor |     |     |     |     |     |     |     |
| ---------------- | --- | -------------------------- | --- | --- | --- | --- | --- | --- | --- |
machine comprehension of text. In EMNLP, pages Shijie Wu, Alexis Conneau, Haoran Li, Luke Zettle-
|            |     |                |             |     |     |        | moyer,        | and Veselin Stoyanov.   | 2019. Emerging |
| ---------- | --- | -------------- | ----------- | --- | --- | ------ | ------------- | ----------------------- | -------------- |
| 2383–2392, |     | Austin, Texas. | Association |     | for | Compu- |               |                         |                |
|            |     |                |             |     |     |        | cross-lingual | structure in pretrained | language mod-  |
tationalLinguistics.
ACL.
els.
| Erik F Sang. | 2002. | Introduction |     | to  | the conll-2002 |     |     |     |     |
| ------------ | ----- | ------------ | --- | --- | -------------- | --- | --- | --- | --- |
shared task: Language-independent named entity Shijie Wu and Mark Dredze. 2019. Beto, bentz, be-
recognition. CoNLL. cas: The surprising cross-lingual effectiveness of
bert. EMNLP.
| Tal Schuster, | Ori | Ram, | Regina | Barzilay, |     | and Amir |     |     |     |
| ------------- | --- | ---- | ------ | --------- | --- | -------- | --- | --- | --- |
QizheXie,ZihangDai,EduardHovy,Minh-ThangLu-
| Globerson. | 2019. | Cross-lingual |     | alignment |     | of con- |                      |     |                      |
| ---------- | ----- | ------------- | --- | --------- | --- | ------- | -------------------- | --- | -------------------- |
|            |       |               |     |           |     |         | ong,andQuocVLe.2019. |     | Unsuperviseddataaug- |
textualwordembeddings,withapplicationstozero-
|                        |     |     |        |     |     |     | mentation | for consistency training. | arXiv preprint |
| ---------------------- | --- | --- | ------ | --- | --- | --- | --------- | ------------------------- | -------------- |
| shotdependencyparsing. |     |     | NAACL. |     |     |     |           |                           |                |
arXiv:1904.12848.
AdityaSiddhant,MelvinJohnson,HenryTsai,Naveen
| Arivazhagan,              |               | Jason Riesa, | Ankur     | Bapna,              |     | Orhan Fi- |     |     |     |
| ------------------------- | ------------- | ------------ | --------- | ------------------- | --- | --------- | --- | --- | --- |
| rat,andKarthikRaman.2019. |               |              |           | Evaluatingthecross- |     |           |     |     |     |
| lingual                   | effectiveness | of           | massively | multilingual        |     | neu-      |     |     |     |
AAAI.
ralmachinetranslation.
| Jasdeep Singh, |           | Bryan McCann,     |          | Nitish     | Shirish     | Keskar, |     |     |     |
| -------------- | --------- | ----------------- | -------- | ---------- | ----------- | ------- | --- | --- | --- |
| Caiming        | Xiong,    | and Richard       |          | Socher.    | 2019.       | Xlda:   |     |     |     |
| Cross-lingual  |           | data augmentation |          |            | for natural | lan-    |     |     |     |
| guage          | inference | and               | question | answering. |             | arXiv   |     |     |     |
preprintarXiv:1905.11471.
| Richard     | Socher,     | Alex         | Perelygin, | Jean   | Wu,  | Jason   |     |     |     |
| ----------- | ----------- | ------------ | ---------- | ------ | ---- | ------- | --- | --- | --- |
| Chuang,     | Christopher | D            | Manning,   | Andrew |      | Ng, and |     |     |     |
| Christopher |             | Potts. 2013. | Recursive  |        | deep | models  |     |     |     |
forsemanticcompositionalityoverasentimenttree-
bank. InEMNLP,pages1631–1642.
XuTan,YiRen,DiHe,TaoQin,ZhouZhao,andTie-
| YanLiu.2019. |     | Multilingualneuralmachinetransla- |     |     |     |     |     |     |     |
| ------------ | --- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- |
ICLR.
tionwithknowledgedistillation.
| ErikFTjongKimSangandFienDeMeulder.2003. |     |                |              |        |       | In-       |     |     |     |
| --------------------------------------- | --- | -------------- | ------------ | ------ | ----- | --------- | --- | --- | --- |
| troduction                              | to  | the conll-2003 |              | shared | task: | language- |     |     |     |
| independent                             |     | named entity   | recognition. |        | In    | CoNLL,    |     |     |     |
pages142–147.AssociationforComputationalLin-
guistics.
| Ashish Vaswani, |           | Noam        | Shazeer,  | Niki        | Parmar,   | Jakob  |     |     |     |
| --------------- | --------- | ----------- | --------- | ----------- | --------- | ------ | --- | --- | --- |
| Uszkoreit,      | Llion     | Jones,      | Aidan     | N.          | Gomez,    | Lukasz |     |     |     |
| Kaiser,         | and Illia | Polosukhin. |           | 2017.       | Attention | is all |     |     |     |
| you need.       | In        | Advances    | in Neural | Information |           | Pro-   |     |     |     |
cessingSystems,pages6000–6010.
| Alex Wang, | Amapreet | Singh,    |        | Julian | Michael, | Felix |     |     |     |
| ---------- | -------- | --------- | ------ | ------ | -------- | ----- | --- | --- | --- |
| Hill, Omer |          | Levy, and | Samuel | R      | Bowman.  | 2018. |     |     |     |
Glue:Amulti-taskbenchmarkandanalysisplatform
| for natural | language | understanding. |     |     | arXiv | preprint |     |     |     |
| ----------- | -------- | -------------- | --- | --- | ----- | -------- | --- | --- | --- |
arXiv:1804.07461.
GuillaumeWenzek,Marie-AnneLachaux,AlexisCon-
| neau,                            | Vishrav | Chaudhary, | Francisco |     | Guzman, | Ar- |     |     |     |
| -------------------------------- | ------- | ---------- | --------- | --- | ------- | --- | --- | --- | --- |
| mandJoulin,andEdouardGrave.2019. |         |            |           |     | Ccnet:  | Ex- |     |     |     |
tractinghighqualitymonolingualdatasetsfromweb
| crawldata. | arXivpreprintarXiv:1911.00359. |     |     |     |     |     |     |     |     |
| ---------- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
8449

Appendix
A LanguagesandstatisticsforCC-100usedbyXLM-R
InthissectionwepresentthelistoflanguagesintheCC-100corpuswecreatedfortrainingXLM-R.We
alsoreportstatisticssuchasthenumberoftokensandthesizeofeachmonolingualcorpus.
ISOcode Language Tokens(M) Size(GiB) ISOcode Language Tokens(M) Size(GiB)
| af Afrikaans         | 242   | 1.3 lo   | Lao                  | 17    | 0.6   |
| -------------------- | ----- | -------- | -------------------- | ----- | ----- |
| am Amharic           | 68    | 0.8 lt   | Lithuanian           | 1835  | 13.7  |
| ar Arabic            | 2869  | 28.0 lv  | Latvian              | 1198  | 8.8   |
| as Assamese          | 5     | 0.1 mg   | Malagasy             | 25    | 0.2   |
| az Azerbaijani       | 783   | 6.5 mk   | Macedonian           | 449   | 4.8   |
| be Belarusian        | 362   | 4.3 ml   | Malayalam            | 313   | 7.6   |
| bg Bulgarian         | 5487  | 57.5 mn  | Mongolian            | 248   | 3.0   |
| bn Bengali           | 525   | 8.4 mr   | Marathi              | 175   | 2.8   |
| - BengaliRomanized   | 77    | 0.5 ms   | Malay                | 1318  | 8.5   |
| br Breton            | 16    | 0.1 my   | Burmese              | 15    | 0.4   |
| bs Bosnian           | 14    | 0.1 my   | Burmese              | 56    | 1.6   |
| ca Catalan           | 1752  | 10.1 ne  | Nepali               | 237   | 3.8   |
| cs Czech             | 2498  | 16.3 nl  | Dutch                | 5025  | 29.3  |
| cy Welsh             | 141   | 0.8 no   | Norwegian            | 8494  | 49.0  |
| da Danish            | 7823  | 45.6 om  | Oromo                | 8     | 0.1   |
| de German            | 10297 | 66.6 or  | Oriya                | 36    | 0.6   |
| el Greek             | 4285  | 46.9 pa  | Punjabi              | 68    | 0.8   |
| en English           | 55608 | 300.8 pl | Polish               | 6490  | 44.6  |
| eo Esperanto         | 157   | 0.9 ps   | Pashto               | 96    | 0.7   |
| es Spanish           | 9374  | 53.3 pt  | Portuguese           | 8405  | 49.1  |
| et Estonian          | 843   | 6.1 ro   | Romanian             | 10354 | 61.4  |
| eu Basque            | 270   | 2.0 ru   | Russian              | 23408 | 278.0 |
| fa Persian           | 13259 | 111.6 sa | Sanskrit             | 17    | 0.3   |
| fi Finnish           | 6730  | 54.3 sd  | Sindhi               | 50    | 0.4   |
| fr French            | 9780  | 56.8 si  | Sinhala              | 243   | 3.6   |
| fy WesternFrisian    | 29    | 0.2 sk   | Slovak               | 3525  | 23.2  |
| ga Irish             | 86    | 0.5 sl   | Slovenian            | 1669  | 10.3  |
| gd ScottishGaelic    | 21    | 0.1 so   | Somali               | 62    | 0.4   |
| gl Galician          | 495   | 2.9 sq   | Albanian             | 918   | 5.4   |
| gu Gujarati          | 140   | 1.9 sr   | Serbian              | 843   | 9.1   |
| ha Hausa             | 56    | 0.3 su   | Sundanese            | 10    | 0.1   |
| he Hebrew            | 3399  | 31.6 sv  | Swedish              | 77.8  | 12.1  |
| hi Hindi             | 1715  | 20.2 sw  | Swahili              | 275   | 1.6   |
| - HindiRomanized     | 88    | 0.5 ta   | Tamil                | 595   | 12.2  |
| hr Croatian          | 3297  | 20.5 -   | TamilRomanized       | 36    | 0.3   |
| hu Hungarian         | 7807  | 58.4 te  | Telugu               | 249   | 4.7   |
| hy Armenian          | 421   | 5.5 -    | TeluguRomanized      | 39    | 0.3   |
| id Indonesian        | 22704 | 148.3 th | Thai                 | 1834  | 71.7  |
| is Icelandic         | 505   | 3.2 tl   | Filipino             | 556   | 3.1   |
| it Italian           | 4983  | 30.2 tr  | Turkish              | 2736  | 20.9  |
| ja Japanese          | 530   | 69.3 ug  | Uyghur               | 27    | 0.4   |
| jv Javanese          | 24    | 0.2 uk   | Ukrainian            | 6.5   | 84.6  |
| ka Georgian          | 469   | 9.1 ur   | Urdu                 | 730   | 5.7   |
| kk Kazakh            | 476   | 6.4 -    | UrduRomanized        | 85    | 0.5   |
| km Khmer             | 36    | 1.5 uz   | Uzbek                | 91    | 0.7   |
| kn Kannada           | 169   | 3.3 vi   | Vietnamese           | 24757 | 137.3 |
| ko Korean            | 5644  | 54.2 xh  | Xhosa                | 13    | 0.1   |
| ku Kurdish(Kurmanji) | 66    | 0.4 yi   | Yiddish              | 34    | 0.3   |
| ky Kyrgyz            | 94    | 1.2 zh   | Chinese(Simplified)  | 259   | 46.9  |
| la Latin             | 390   | 2.5 zh   | Chinese(Traditional) | 176   | 16.6  |
Table 6: Languages and statistics of the CC-100 corpus. We report the list of 100 languages and include
the number of tokens (Millions) and the size of the data (in GiB) for each language. Note that we also include
romanizedvariantsofsomenonlatinlanguagessuchasBengali,Hindi,Tamil,TeluguandUrdu.
8450

B ModelArchitecturesandSizes
Asweshowedinsection5,capacityisanimportantparameterforlearningstrongcross-lingualrepresen-
tations. Inthetablebelow,welistmultiplemonolingualandmultilingualmodelsusedbytheresearch
communityandsummarizetheirarchitecturesandtotalnumberofparameters.
| Model | #lgs tokenization | L H    | H       | A V #params |
| ----- | ----------------- | ------ | ------- | ----------- |
|       |                   |        | m ff    |             |
| BERT  | 1 WordPiece       | 12 768 | 3072 12 | 30k 110M    |
Base
| BERT Large | 1 WordPiece   | 24 1024 | 4096 16 | 30k 335M   |
| ---------- | ------------- | ------- | ------- | ---------- |
| mBERT      | 104 WordPiece | 12 768  | 3072 12 | 110k 172M  |
| RoBERTa    | 1 bBPE        | 12 768  | 3072    | 8 50k 125M |
Base
| RoBERTa  | 1 bBPE  | 24 1024 | 4096 16 | 50k 355M   |
| -------- | ------- | ------- | ------- | ---------- |
| XLM-15   | 15 BPE  | 12 1024 | 4096    | 8 95k 250M |
| XLM-17   | 17 BPE  | 16 1280 | 5120 16 | 200k 570M  |
| XLM-100  | 100 BPE | 16 1280 | 5120 16 | 200k 570M  |
| Unicoder | 15 BPE  | 12 1024 | 4096    | 8 95k 250M |
| XLM-R    | 100 SPM | 12 768  | 3072 12 | 250k 270M  |
Base
| XLM-R      | 100 SPM     | 24 1024 | 4096 16  | 250k 550M |
| ---------- | ----------- | ------- | -------- | --------- |
| GPT2       | 1 bBPE      | 48 1600 | 6400 32  | 50k 1.5B  |
| wide-mmNMT | 103 SPM     | 12 2048 | 16384 32 | 64k 3B    |
| deep-mmNMT | 103 SPM     | 24 1024 | 16384 32 | 64k 3B    |
| T5-3B      | 1 WordPiece | 24 1024 | 16384 32 | 32k 3B    |
| T5-11B     | 1 WordPiece | 24 1024 | 65536 32 | 32k 11B   |
Table7: Detailsonmodelsizes. WeshowthetokenizationusedbyeachTransformermodel,thenumberoflayers
L, the number of hidden states of the model H , the dimension of the feed-forward layer H , the number of
m ff
attention heads A, the size of the vocabulary V and the total number of parameters #params. For Transformer
encoders, the number of parameters can be approximated by 4LH2 + 2LH H + VH . GPT2 numbers
|     |     |     | m   | m ff m |
| --- | --- | --- | --- | ------ |
are from Radford et al. (2019), mm-NMT models are from the work of Arivazhagan et al. (2019) on massively
multilingualneuralmachinetranslation(mmNMT),andT5numbersarefromRaffeletal.(2019). WhileXLM-R
is among the largest models partly due to its large embedding layer, it has a similar number of parameters than
XLM-100,andremainssignificantlysmallerthatrecentlyintroducedTransformermodelsformultilingualMTand
transferlearning. Whilethistablegivesmorehindsightonthedifferenceofcapacityofeachmodel,noteitdoes
nothighlightothercriticaldifferencesbetweenthemodels.
8451