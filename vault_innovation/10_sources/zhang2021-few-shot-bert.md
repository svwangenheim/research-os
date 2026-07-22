PublishedasaconferencepaperatICLR2021
REVISITING FEW-SAMPLE BERT FINE-TUNING
TianyiZhang∗(cid:52)§ FelixWu∗† ArzooKatiyar(cid:52)(cid:51) KilianQ.Weinberger†‡ YoavArtzi†‡
†ASAPPInc. §StanfordUniversity (cid:51) PennStateUniversity ‡CornellUniversity
tz58@stanford.edu {fwu, kweinberger, yoav}@asapp.com arzoo@psu.edu
ABSTRACT
Thispaperisastudyoffine-tuningofBERTcontextualrepresentations,withfocus
oncommonlyobservedinstabilitiesinfew-samplescenarios. Weidentifyseveral
factorsthatcausethisinstability: thecommonuseofanon-standardoptimization
method with biased gradient estimation; the limited applicability of significant
partsoftheBERTnetworkfordown-streamtasks;andtheprevalentpracticeof
usingapre-determined,andsmallnumberoftrainingiterations. Weempirically
testtheimpactofthesefactors,andidentifyalternativepracticesthatresolvethe
commonlyobservedinstabilityoftheprocess. Inlightoftheseobservations,we
re-visitrecentlyproposedmethodstoimprovefew-samplefine-tuningwithBERT
and re-evaluate their effectiveness. Generally, we observe the impact of these
methodsdiminishessignificantlywithourmodifiedprocess.
1 INTRODUCTION
Fine-tuningself-supervisedpre-trainedmodelshassignificantlyboostedstate-of-the-artperformance
onnaturallanguageprocessing(NLP)tasks(Liu,2019;Yangetal.,2019a;Waddenetal.,2019;Zhu
etal.,2020;Guuetal.,2020). OneofthemosteffectivemodelsforthisprocessisBERT(Devlin
etal.,2019). However,despitesignificantsuccess,fine-tuningremainsunstable,especiallywhen
usingthelargevariantofBERT(BERT )onsmalldatasets,wherepre-trainingstandstoprovide
Large
themostsignificantbenefit. Identicallearningprocesseswithdifferentrandomseedsoftenresultin
significantlydifferentandsometimesdegeneratemodelsfollowingfine-tuning,eventhoughonlya
few,seeminglyinsignificantaspectsofthelearningprocessareimpactedbytherandomseed(Phang
etal.,2018;Leeetal.,2020;Dodgeetal.,2020).1 Asaresult,practitionersresorttomultiplerandom
trialsformodelselection. Thisincreasesmodeldeploymentcostsandtime,andmakesscientific
comparisonchallenging(Dodgeetal.,2020).
Thispaperisastudyofdifferentaspectsofthefew-samplefine-tuningoptimizationprocess. Our
goalistobetterunderstandtheimpactofcommonchoiceswithregardtotheoptimizationalgorithm,
modelinitialization,andthenumberoffine-tuningtrainingiterations. Weidentifysuboptimalitiesin
commoncommunitypractices: theuseofanon-standardoptimizerintroducesbiasinthegradient
estimation;thetoplayersofthepre-trainedBERTmodelprovideabadinitializationpointforfine-
tuning;andtheuseofapre-determined,butcommonlyadoptednumberoftrainingiterationshurts
convergence. Westudytheseissuesandtheirremediesthroughexperimentsonmultiplecommon
benchmarks,focusingonfew-samplefine-tuningscenarios.
Oncethesesuboptimalpracticesareaddressed,weobservethatdegeneraterunsareeliminatedand
performancebecomesmuchmorestable. Thismakesitunnecessarytoexecutenumerousrandom
restarts as proposed in Dodge et al. (2020). Our experiments show the remedies we experiment
withforeachissuehaveoverlappingeffect. Forexample, allocatingmoretrainingiterationscan
eventuallycompensateforusingthenon-standardbiasedoptimizer,eventhoughthecombinationof
abias-correctedoptimizerandre-initializingsomeofthepre-trainedmodelparameterscanreduce
fine-tuningcomputationalcosts. Thisempiricallyhighlightshowdifferentaspectsoffine-tuning
influencethestabilityoftheprocess,attimesinasimilarmanner. Inthelightofourobservations,
were-evaluateseveraltechniques(Phangetal.,2018;Leeetal.,2020;Howard&Ruder,2018)that
*Equalcontribution,(cid:52)WorkdoneatASAPP.
1Fine-tuning instability is also receiving significant practitioner attention. For example:
https://github.com/zihangdai/xlnet/issues/96andhttps://github.com/huggingface/transformers/issues/265.
1
1202
raM
11
]LC.sc[
3v78950.6002:viXra

PublishedasaconferencepaperatICLR2021
wererecentlyproposedtoincreasefew-samplefine-tuningstabilityandshowasignificantdecrease
intheirimpact. Ourworkfurtherstheempiricalunderstandingofthefine-tuningprocess,andthe
optimizationpracticesweoutlineidentifyimpactfulavenuesforthedevelopmentoffuturemethods.
2 BACKGROUND AND RELATED WORK
BERT TheBidirectionalEncoderRepresentationsfromTransformers(BERT;Devlinetal.,2019)
modelisaTransformerencoder(Vaswanietal.,2017)trainedonrawtextusingmaskedlanguage
modelingandnext-sentencepredictionobjectives. Itgeneratesanembeddingvectorcontextualized
throughastackofTransformerblocksforeachinputtoken. BERTprependsaspecial[CLS]token
totheinputsentenceorsentencepairs. Theembeddingofthistokenisusedasasummarytokenfor
theinputforclassificationtasks. Thisembeddingiscomputedwithanadditionalfully-connected
layerwithatanhnon-linearity,commonlyreferredtoasthepooler,toaggregatetheinformationfor
the[CLS]embedding.
Fine-tuning Thecommonapproachforusingthepre-trainedBERTmodelistoreplacetheoriginal
outputlayerwithanewtask-specificlayerandfine-tunethecompletemodel. Thisincludeslearning
thenewoutputlayerparametersandmodifyingalltheoriginalweights,includingtheweightsofword
embeddings,Transformerblocks,andthepooler. Forexample,forsentence-levelclassification,an
addedlinearclassifierprojectsthe[CLS]embeddingtoanunnormalizedprobabilityvectoroverthe
outputclasses. Thisprocessintroducestwosourcesofrandomness: theweightinitializationofthe
newoutputlayerandthedataorderinthestochasticfine-tuningoptimization. Existingwork(Phang
et al., 2018; Lee et al., 2020; Dodge et al., 2020) shows that these seemingly benign factors can
influencetheresultssignificantly,especiallyonsmalldatasets(i.e.,<10Kexamples). Consequently,
practitioners often conduct many random trials of fine-tuning and pick the best model based on
validationperformance(Devlinetal.,2019).
Fine-tuningInstability TheinstabilityoftheBERTfine-tuningprocesshasbeenknownsinceits
introduction(Devlinetal.,2019), andvariousmethodshavebeenproposedtoaddressit. Phang
etal.(2018)showthatfine-tuningthepre-trainedmodelonalargeintermediatetaskstabilizeslater
fine-tuningonsmalldatasets. Leeetal.(2020)introduceanewregularizationmethodtoconstrainthe
fine-tunedmodeltostayclosetothepre-trainedweightsandshowthatitstabilizesfine-tuning.Dodge
etal.(2020)proposeanearlystoppingmethodtoefficientlyfilteroutrandomseedslikelytoleadto
badperformance. Concurrentlytoourwork,Mosbachetal.(2020)alsoshowthatBERTADAMleads
toinstabilityduringfine-tuning. Ourexperimentsstudyingtheeffectoftraininglongerarerelatedto
previousworkstudyingthisquestioninthecontextoftrainingmodelsfromscratch(Popel&Bojar,
2018;Nakkiranetal.,2019).
BERTRepresentationTransferability BERTpre-trainedrepresentationshavebeenwidelystud-
iedusingprobingmethodsshowingthatthepre-trainedfeaturesfromintermediatelayersaremore
transferable(Tenneyetal.,2019b;a;Liuetal.,2019a;Hewitt&Manning,2019;Hewitt&Liang,
2019)orapplicable(Zhangetal.,2020)tonewtasksthanfeaturesfromlaterlayers,whichchange
moreafterfine-tuning(Petersetal.,2019;Merchantetal.,2020). Ourworkisinspiredbythese
findings,butfocusesonstudyinghowthepre-trainedweightsinfluencethefine-tuningprocess. Li
etal.(2020)proposetore-initializethefinalfully-connectedlayerofaConvNetandshowperfor-
mancegainforimageclassification.2 Concurrenttoourwork,Tamkinetal.(2020)adoptasimilar
methodologyofweightre-initialization(Section5)tostudythetransferabilityofBERT.Incontrastto
ourstudy,theirworkemphasizespinpointingthelayersthatcontributethemostintransferlearning,
andtherelationbetweenprobingperformanceandtransferability.
3 EXPERIMENTAL METHODOLOGY
Data Wefollowthedatasetupofpreviousstudies(Leeetal.,2020;Phangetal.,2018;Dodge
etal.,2020)tostudyfew-samplefine-tuningusingeightdatasetsfromtheGLUEbenchmark(Wang
et al., 2019b). The datasets cover four tasks: natural language inference (RTE, QNLI, MNLI),
paraphrasedetection(MRPC,QQP),sentimentclassification(SST-2),andlinguisticacceptability
(CoLA). Appendix A provides dataset statistics and a description of each dataset. We primarily
2Thisconcurrentworkwaspublishedshortlyafterourstudywasposted.
2

PublishedasaconferencepaperatICLR2021
Algorithm 1: the ADAM pseudocode adapted from Kingma & Ba (2014), and provided for
|     | g2  |     | (cid:12)g |     |     |
| --- | --- | --- | --------- | --- | --- |
reference. t denotes the elementwise square g t t . β 1 and β 2 to the power t are denoted
βt βt.
as All operations on vectors are element-wise. The suggested hyperparameter values
1 2
according to Kingma & Ba (2014) are: α = 0.001, β = 0.9, β = 0.999, and (cid:15) = 10−8.
1 2
BERTADAM(Devlinetal.,2019)omitsthebiascorrection(lines9–10),andtreatsm andv as
t t
| m andv | inline11. |     |     |     |     |
| ------ | --------- | --- | --- | --- | --- |
(cid:98)t (cid:98)t
Require: α:learningrate;β ,β ∈[0,1):exponentialdecayratesforthemomentestimates;f(θ):stochastic
1 2
objectivefunctionwithparametersθ;θ 0:initialparametervector;λ∈[0,1):decoupledweightdecay.
1: m ←0(Initializefirstmomentvector)
0
2: v ←0(Initializesecondmomentvector)
0
3: t←0(Initializetimestep)
| 4: whileθ | tnotconvergeddo |     |     |     |     |
| --------- | --------------- | --- | --- | --- | --- |
5: t←t+1
| 6: g ←∇   | f (θ )(Getgradientsw.r.t.stochasticobjectiveattimestept) |                                              |     |     |     |
| --------- | -------------------------------------------------------- | -------------------------------------------- | --- | --- | --- |
| t         | θ t t−1                                                  |                                              |     |     |     |
| 7: m      | ←β ·m                                                    | +(1−β )·g t(Updatebiasedfirstmomentestimate) |     |     |     |
| t         | 1 t−1                                                    | 1                                            |     |     |     |
| 8: v ←β   | ·v +(1−β                                                 | )·g 2(Updatebiasedsecondrawmomentestimate)   |     |     |     |
| t         | 2 t−1                                                    | 2 t                                          |     |     |     |
| 9: m      | ←m /(1−β                                                 | t)(Computebias-correctedfirstmomentestimate) |     |     |     |
| (cid:98)t | t                                                        | 1                                            |     |     |     |
| 10: v     | ←v /(1−β t)(Co                                           | mputebias-correctedsecondrawmomentestimate)  |     |     |     |
| (cid:98)t | t 2                                                      | √                                            |     |     |     |
| 11: θ     | ←θ −α·m                                                  | /( v +(cid:15))(Updateparameters)            |     |     |     |
| t         | t−1                                                      | (cid:98)t (cid:98)t                          |     |     |     |
12: endwhile
| 13: return | θ t(Resultingparameters) |     |     |     |     |
| ---------- | ------------------------ | --- | --- | --- | --- |
focus on four datasets (RTE, MRPC, STS-B, CoLA) that have fewer than 10k training samples,
becauseBERTfine-tuningonthesedatasetsisknowntobeunstable(Devlinetal.,2019). Wealso
complementourstudybydownsamplingalleightdatasetsto1ktrainingexamplesfollowingPhang
etal.(2018). Whilepreviousstudies(Leeetal.,2020;Phangetal.,2018;Dodgeetal.,2020)focus
onthevalidationperformance,wesplitheld-outtestsetsforourstudy.3 ForRTE,MRPC,STS-B,
andCoLA,wedividetheoriginalvalidationsetinhalf,usingonehalfforvalidationandtheotherfor
test. Fortheotherfourlargerdatasets,weonlystudythedownsampledversions,andsplitadditional
1ksamplesfromthetrainingsetasourvalidationdataandtestontheoriginalvalidationset.
Experimental Setup Unless noted otherwise, we follow the hyperparameter setup of Lee et al.
(2020). Wefine-tunetheuncased,24-layerBERT modelwithbatchsize32,dropout0.1,and
Large
peaklearningrate2×10−5
|     |     | forthreeepochs. | Weclipthegradientstohaveamaximumnormof |     |     |
| --- | --- | --------------- | -------------------------------------- | --- | --- |
1. Weapplylinearlearningratewarm-upduringthefirst10%oftheupdatesfollowedbyalinear
decay. WeusemixedprecisiontrainingusingApex4tospeedupexperiments. Weshowthatmixed
precisiontrainingdoesnotaffectfine-tuningperformanceinAppendixC.Weevaluatetentimeson
thevalidationsetduringtrainingandperformearlystopping. Wefine-tunewith20randomseedsto
comparedifferentsettings.
| 4 OPTIMIZATION |     | ALGORITHM: | DEBIASING | OMISSION | IN BERTADAM |
| -------------- | --- | ---------- | --------- | -------- | ----------- |
Themostcommonlyusedoptimizerforfine-tuningBERTisBERTADAM,amodifiedversionof
the ADAM first-order stochastic optimization method. It differs from the original ADAM algo-
rithm(Kingma&Ba,2014)inomittingabiascorrectionstep. ThischangewasintroducedbyDevlin
etal.(2019),andsubsequentlymadeitswayintocommonopensourcelibraries,includingtheofficial
implementation,5 huggingface’sTransformers(Wolfetal.,2019),6 AllenNLP(Gardneretal.,2018),
GluonNLP(Guoetal.,2019),jiant(Wangetal.,2019c),MT-DNN(Liuetal.,2020),andFARM.7As
aresult,thisnon-standardimplementationiswidelyusedinbothindustryandresearch(Wangetal.,
2019a;Phangetal.,2018;Leeetal.,2020;Dodgeetal.,2020;Sunetal.,2019;Clarketal.,2020;
Lanetal.,2020;Houlsbyetal.,2019;Stickland&Murray,2019;Liuetal.,2019b). Weobservethat
thebiascorrectionomissioninfluencesthelearningrate,especiallyearlyinthefine-tuningprocess,
andisoneoftheprimaryreasonsforinstabilityinfine-tuningBERT(Devlinetal.,2019;Phangetal.,
2018;Leeetal.,2020;Dodgeetal.,2020).
Algorithm 1 shows the ADAM algorithm, and highlights the omitted line in the non-standard
BERTADAMimplementation. Ateachoptimizationstep(lines4–11),ADAMcomputestheexponen-
3Theoriginaltestsetsarenotpubliclyavailable.
4https://github.com/NVIDIA/apex
5https://github.com/google-research/bert/blob/f39e881/optimization.py#L108-L157
6ThedefaultwaschangedfromBERTADAMtodeb3iasedADAMincommitec07cf5aonJuly11,2019.
7https://github.com/deepset-ai/FARM

PublishedasaconferencepaperatICLR2021
6
5
4
3
2
1
100 101 102 103 104 105 106
TrainingIterations(logscale)
nisaiB
edutingaMetadpU
1.0
Bias
RTE 0.8
MRPC
STS-B 0.6 CoLA
MNLI
0.4
0.2
0.0
RTE MRPC CoLA STS-B
Figure1: Biasinthe ADAM up-
dateasafunctionoftrainingiter-
ations. Verticallinesindicatethe
typicalnumberofiterationsused
tofine-tuneBERTonfoursmall
datasets and one large dataset
(MNLI).Smalldatasetsusefewer
iterationsandaremostaffected.
ecnamrofrePtseT
PerformanceDistribution
1.00
0.75
Correction 0.50
NoCorrection
Median 0.25
Outlier 23 92 161 230
Steps
Figure 2: Performance dis-
tribution box plot across 50
random trials and the four
datasets with and without
ADAM bias correction. Bias
correction reduces the vari-
anceoffine-tuningresultsby
alargemargin.
ssoLniarT
RTE
Correction
NoCorrection
Figure 3: Mean (solid lines)
and range (shaded region)
of training loss during fine-
tuning BERT, across 50 ran-
dom trials. Bias correction
speeds up convergence and
shrinks the range of training
loss.
tialmovingaverageofthegradients(m )andthesquaredgradients(v ),whereβ ,β parameterize
t t 1 2
theaveraging(lines7–8). BecauseADAMinitializesm
t
andv
t
to0andsetsexponentialdecayrates
β andβ closeto1,theestimatesofm andv areheavilybiasedtowards0earlyduringlearning
1 2 t t
when t is small. Kingma & Ba (2014) computes the ratio between the biased and the unbiased
estimatesofm andv as(1−βt)and(1−βt). Thisratioisindependentofthetrainingdata. The
t t 1 2
modelparametersθareupdatedinthedirectionoftheaveragedgradientm dividedbythesquare
√ t
rootofthesecondmoment v
t
(line11). BERTADAMomitsthedebiasing(lines9–10),anddirectly
usesthebiasedestimatesintheparametersupdate.
Figure 1 shows the ratio √mˆt between the update using the biased and the unbiased estimation
vˆt
as a function of training iterations. The bias is relatively high early during learning, indicating
overestimation. Iteventuallyconvergestoone,suggestingthatwhentrainingforsufficientiterations,
theestimationbiaswillhavenegligibleeffect.8 Therefore,thebiasratiotermismostimportantearly
duringlearningtocounteracttheoverestimationofm andv duringearlyiterations. Inpractice,
√ t t
1−βt
ADAM adaptivelyre-scalesthelearningrateby
1−βt
2. ThiscorrectioniscrucialforBERTfine-
1
tuningonsmalldatasetswithfewerthan10ktrainingsamplesbecausetheyaretypicallyfine-tuned
withlessthan1kiterations(Devlinetal.,2019). Thefigureshowsthenumberoftrainingiterations
forRTE,MRPC,STS-B,CoLA,andMNLI.MNLIistheonlyoneofthissetwithalargenumberof
supervisedtrainingexamples. Forsmalldatasets,thebiasratioissignificantlyhigherthanonefor
theentirefine-tuningprocess,implyingthatthesedatasetssufferheavilyfromoverestimationinthe
updatemagnitude. Incomparison,forMNLI,themajorityoffine-tuningoccursintheregionwhere
thebiasratiohasconvergedtoone. Thisexplainswhyfine-tuningonMNLIisknowntoberelatively
stable(Devlinetal.,2019).
We evaluate the importance of the debiasing step empirically by fine-tuning BERT with both
BERTADAM andthedebiased ADAM9 for50randomseedsonRTE,MRPC,STS-B,andCoLA.
Figure 2 summarizes the performance distribution. The bias correction significantly reduces the
performancevarianceacrossdifferentrandomtrialsandthefourdatasets. Withoutthebiascorrection
weobservemanydegenerateruns,wherefine-tunedmodelsfailtooutperformtherandombaseline.
Forexample,onRTE,48%offine-tuningrunshaveanaccuracylessthan55%,whichiscloseto
randomguessing. Figure3furtherillustratesthisdifferencebyplottingthemeanandtherangeof
traininglossduringfine-tuningacrossdifferentrandomtrialsonRTE.Figure11inAppendixFshows
similarplotsforMRPC,STS-B,andCoLA.ThebiasedBERTADAM consistentlyleadstoworse
averagedtrainingloss,andonalldatasetstohighermaximumtrainingloss. Thisindicatesmodels
trainedwithBERTAdamareunderfittingandtherootofinstabilityliesinoptimization.
8OurexperimentsonthecompletelyMNLIdatasetconfirmusingtheunbiasedestimationdoesnotimprove
nordegradeperformanceforlargedatasets(AppendixD).
9WeusethePyTorchADAMimplementationhttps://pytorch.org/docs/1.4.0/_modules/torch/optim/adamw.html.
4

PublishedasaconferencepaperatICLR2021
|              | RTE |     |                 |     | MRPC |              | STS-B |                   | CoLA |
| ------------ | --- | --- | --------------- | --- | ---- | ------------ | ----- | ----------------- | ---- |
| 0.75         |     |     | 0.95            |     |      | 0.90         |       | 0.70              |      |
| .CCMtseT.pxE |     |     |                 |     |      | .ccAtseT.pxE |       | .CCStseT.pxE 0.65 |      |
| 0.70         |     |     | 1FtseT.pxE 0.92 |     |      | 0.89         |       |                   |      |
0.60
| 0.65 |     |     | 0.89 |     |     | 0.88 |     |     |     |
| ---- | --- | --- | ---- | --- | --- | ---- | --- | --- | --- |
0.55
| 0.60 |     |     | 0.86 |     |     | 0.87 |     |      |              |
| ---- | --- | --- | ---- | --- | --- | ---- | --- | ---- | ------------ |
|      |     |     |      |     |     |      |     | 0.50 | Correction   |
| 0.55 |     |     | 0.83 |     |     | 0.86 |     | 0.45 | NoCorrection |
| 0.50 |     |     | 0.80 |     |     | 0.85 |     | 0.40 |              |
1 10 20 30 40 50 1 10 20 30 40 50 1 10 20 30 40 50 1 10 20 30 40 50
#ofRandomTrials #ofRandomTrials #ofRandomTrials #ofRandomTrials
Figure4: Expectedtestperformance(solidlines)withstandarddeviation(shadedregion)overthe
numberofrandomtrialsallocatedforfine-tuningBERT.Withbiascorrection,wereliablyachieve
goodresultswithfew(i.e.,5or10)randomtrials.
| Dataset |         | RTE |        |         | MRPC |        | STS-B          |     | CoLA           |
| ------- | ------- | --- | ------ | ------- | ---- | ------ | -------------- | --- | -------------- |
|         | 3Epochs |     | Longer | 3Epochs |      | Longer | 3Epochs Longer |     | 3Epochs Longer |
Standard 69.5±2.5 72.3±1.9 90.8±1.3 90.5±1.5 89.0±0.6 89.6±0.3 63.0±1.5 62.4±1.7
Re-init 72.6±1.6 73.1±1.3 91.4±0.8 91.0±0.4 89.4±0.2 89.9±0.1 63.9±1.9 61.9±2.3
| Dataset |         | RTE(1k) |        |         | MRPC(1k) |        | STS-B(1k)      |     | CoLA(1k)       |
| ------- | ------- | ------- | ------ | ------- | -------- | ------ | -------------- | --- | -------------- |
|         | 3Epochs |         | Longer | 3Epochs |          | Longer | 3Epochs Longer |     | 3Epochs Longer |
Standard 62.5±2.8 65.2±2.1 80.5±3.3 83.8±2.1 84.7±1.4 88.0±0.4 45.9±1.6 48.8±1.4
Re-init 65.6±2.0 65.8±1.7 84.6±1.6 86.0±1.2 87.2±0.4 88.4±0.2 47.6±1.8 48.4±2.1
| Dataset |         | SST(1k) |        |         | QNLI(1k) |        | QQP(1k)        |     | MNLI(1k)       |
| ------- | ------- | ------- | ------ | ------- | -------- | ------ | -------------- | --- | -------------- |
|         | 3Epochs |         | Longer | 3Epochs |          | Longer | 3Epochs Longer |     | 3Epochs Longer |
89.7±1.5 90.9±0.5 78.6±2.0 81.4±0.9 74.0±2.7 77.4±0.8 52.2±4.2 67.5±1.1
Standard
Re-init 90.8±0.4 91.2±0.5 81.9±0.5 82.1±0.3 77.2±0.7 77.6±0.6 66.4±0.6 68.8±0.5
Table1: Meantestperformanceandstandarddeviation. Wecomparefine-tuningwiththecomplete
BERTmodel(Standard)andfine-tuningwiththepartiallyre-initializedBERT(Re-init). Weshow
resultsoffine-tuningfor3epochsandforlongertraining(Sec6). Weunderlineandhighlightinblue
thebestandnumberstatisticallyequivalenttoitamongeachgroupof4numbers. Weuseaone-tailed
Student’st-testandrejectthenullhypothesiswhenp<0.05.
We simulate a realistic setting of multiple random trials following Dodge et al. (2020). We use
bootstrapping for the simulation: given the 50 fine-tuned models we trained, we sample models
with replacement, perform model selection on the validation set, and record the test results; we
repeatthisprocess1ktimestoestimatemeanandvariance. Figure4showsthesimulatedtestresults
asafunctionofthenumberofrandomtrials. AppendixEprovidesthesameplotsforvalidation
performance. UsingthedebiasedADAMwecanreliablyachievegoodresultsusingfewerrandom
trials;thedifferenceinexpectedperformanceisespeciallypronouncedwhenweperformlessthan
10trials. Whereastheexpectedvalidationperformancemonotonicallyimproveswithmorerandom
trials(Dodgeetal.,2020),theexpectedtestperformancedeteriorateswhenweperformtoomany
randomtrialsbecausethemodelselectionprocesspotentiallyoverfitsthevalidationset. Basedon
theseobservations,werecommendperformingamoderatenumberofrandomtrials(i.e.,5or10).
| 5 INITIALIZATION: |     |     | RE-INITIALIZING |     |     | BERT | PRE-TRAINED | LAYERS |     |
| ----------------- | --- | --- | --------------- | --- | --- | ---- | ----------- | ------ | --- |
Theinitialvaluesofnetworkparametershavesignificantimpactontheprocessoftrainingdeepneural
networks,andvariousmethodsexistforcarefulinitialization(Glorot&Bengio,2010;Heetal.,2015;
Zhangetal.,2019;Radfordetal.,2019;Dauphin&Schoenholz,2019).Duringfine-tuning,theBERT
parameterstaketheroleoftheinitializationpointforthefine-tuningoptimizationprocess,whilealso
capturingtheinformationtransferredfrompre-training. ThecommonapproachforBERTfine-tuning
istoinitializealllayersexceptonespecializedoutputlayerwiththepre-trainedweights. Westudy
thevalueoftransferringallthelayersincontrasttosimplyignoringtheinformationlearnedinsome
layers. Thisismotivatedbyobjectrecognitiontransferlearningresultsshowingthatlowerpre-trained
layerslearnmoregeneralfeatureswhilehigherlayersclosertotheoutputspecializemoretothe
pre-trainingtasks(Yosinskietal.,2014). ExistingmethodsusingBERTshowthatusingthecomplete
networkisnotalwaysthemosteffectivechoice,aswediscussinSection2. Ourempiricalresults
furtherconfirmthis: weobservethattransferringthetoppre-trainedlayersslowsdownlearningand
hurtsperformance.
5

PublishedasaconferencepaperatICLR2021
|       | RTE |      | MRPC |     |     |     |      |
| ----- | --- | ---- | ---- | --- | --- | --- | ---- |
|       |     |      |      |     | RTE |     | MRPC |
| 0.775 |     | 0.92 |      |     |     |     |      |
1.00
| ycaruccA.laV 0.750 |     |        |     |           | Standard |                |     |
| ------------------ | --- | ------ | --- | --------- | -------- | -------------- | --- |
|                    |     | 1F.laV |     | ssoLniarT | Re-init  | ssoLniarT 0.75 |     |
| 0.725              |     | 0.90   |     | 0.75      |          |                |     |
0.50
| 0.700 |     | 0.88 |     | 0.50 |     |     |     |
| ----- | --- | ---- | --- | ---- | --- | --- | --- |
Standard Re-init
| 0.675 | Median Outlier |     |     |     |     | 0.25 |     |
| ----- | -------------- | --- | --- | --- | --- | ---- | --- |
0.25
| rd le r 1              | 2 3 4 5 init6          | rd le     | r 1 2 3 4 5 init6                   |     |     |     |     |
| ---------------------- | ---------------------- | --------- | ----------------------------------- | --- | --- | --- | --- |
| n d a o o -i ni t i ni | t i ni t i ni t i ni t | n d a o o | -i ni t i ni t i ni t i ni t i ni t |     |     |     |     |
S t a it P R e R e - R e - R e - R e - R e - S t a it P R e R e - R e - R e - R e - R e - 23 92 161 230 34 136 238 340
| e - i n |     | e - i n |     |     |       |     |       |
| ------- | --- | ------- | --- | --- | ----- | --- | ----- |
| R       |     | R       |     |     | Steps |     | Steps |
Figure5: Validationperformancedistributionof Figure6: Mean(solidlines)andRange(shaded
re-initializingdifferentnumberoflayersofthe region)oftraininglossduringfine-tuningBERT,
| BERTmodel. |     |     |     | across20randomtrials. |     | Re-initleadstofaster |     |
| ---------- | --- | --- | --- | --------------------- | --- | -------------------- | --- |
convergenceandshrinkstherange.
Wetestthetransferabilityofthetoplayersusingasimpleablationstudy. Insteadofusingthepre-
trainedweightsforalllayers,were-initializethepoolerlayersandthetopL∈NBERTTransformer
blocksusingtheoriginalBERTinitialization,N(0,0.022). Wecomparetwosettings: (a)standard
fine-tuning with BERT, and (b) Re-init fine-tuning of BERT. We evaluate Re-init by selecting
L ∈ {1,...,6}basedonmeanvalidationperformance. Allexperimentsusethedebiased ADAM
(Section4)with20randomseeds.
Re-initImpactonPerformance
|     |     |     | Table1showsourresultsonallthedatasetsfromSection3. |     |     |     | We  |
| --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- |
showresultsforthecommonsettingofusing3epochs,andalsoforlongertraining,whichwediscuss
andstudyinSection6. Re-initconsistentlyimprovesmeanperformanceonallthedatasets,showing
thatnotall layersarebeneficialfor transferring. Itusually alsodecreasesthevarianceacrossall
datasets. AppendixFshowssimilarbenefitsforpre-trainedmodelsotherthanBERT.
SensitivitytoNumberofLayersRe-initialized Figure5showstheeffectofthechoiceofL,the
numberofblockswere-initialize,onRTEandMRPC.Figure13inAppendixFshowssimilarplots
fortherestofthedatasets. Weobservemoresignificantimprovementintheworst-caseperformance
thanthebestperformance,suggestingthatRe-initismorerobusttounfavorablerandomseed. We
alreadyseeimprovementswhenonlythepoolerlayerisre-initialized. Re-initializingfurtherlayers
helps more. For larger L though, the performance plateaus and even decreases as re-initialize
| pre-trainedlayerswithgeneralimportantfeatures. |     |     |     | ThebestLvariesacrossdatasets. |     |     |     |
| ---------------------------------------------- | --- | --- | --- | ----------------------------- | --- | --- | --- |
Effect on Convergence and Parameter Change Figure 6 shows the training loss for both the
standard fine-tuning and Re-init on RTE and MRPC. Figure 13, Appendix F shows the training
lossforallotherdatasets. Re-initleadstofasterconvergence. Westudytheweightsofdifferent
Transformer blocks. For each block, we concatenate all parameters and record the L2 distance
L2
between these parameters and their initialized values during fine-tuning. Figure 7 plots the
distanceforfourdifferenttransformerblocksasafunctionoftrainingstepsonRTE,andFigures15–
18inAppendixFshowalltransformerblocksonfourdatasets. Ingeneral,Re-initdecreasestheL2
distancetoinitializationfortopTransformerblocks(i.e.,18–24). Re-initializingmorelayersleadsto
alargerreduction,indicatingthatRe-initdecreasesthefine-tuningworkload. TheeffectofRe-init
isnotlocal;evenre-initializingonlythetopmostTransformerblockcanaffectthewholenetwork.
WhilesettingL=1orL=3continuestobenefitthebottomTransformerblocks,re-initializingtoo
manylayers(e.g.,L=10)canincreasetheL2distanceinthebottomTransformerblocks,suggesting
atradeoffbetweenthebottomandthetopTransformerblocks. Collectively,theseresultssuggest
thatRe-initfindsabetterinitializationforfine-tuningandthetopLlayersofBERTarepotentially
overspecializedtothepre-trainingobjective.
| 6 TRAINING | ITERATIONS: |     | FINE-TUNING | BERT | FOR LONGER |     |     |
| ---------- | ----------- | --- | ----------- | ---- | ---------- | --- | --- |
BERTistypicallyfine-tunedwithaslantedtriangularlearningrate,whichapplieslinearwarm-upto
thelearningratefollowedbyalineardecay. Thislearningschedulewarrantsdecidingthenumber
oftrainingiterationsupfront. Devlinetal.(2019)recommendfine-tuningGLUEdatasetsforthree
epochs. Thisrecommendationhasbeenadoptedbroadlyforfine-tuning(Phangetal.,2018;Leeetal.,
2020;Dodgeetal.,2020). Westudytheimpactofthischoice,andobservethatthisone-size-fits-all
6

PublishedasaconferencepaperatICLR2021
TransformerBlock6 TransformerBlock12 TransformerBlock18 TransformerBlock24
| noitazilaitinIot.tsiD2L 0.90 |     |     | 0.90 |     |     | 0.90 |     |     |     |
| ---------------------------- | --- | --- | ---- | --- | --- | ---- | --- | --- | --- |
0.90
| 0.72 |     |     | 0.72 |     |     | 0.72 |     | 0.72 |     |
| ---- | --- | --- | ---- | --- | --- | ---- | --- | ---- | --- |
| 0.54 |     |     | 0.54 |     |     | 0.54 |     |      |     |
0.54
| 0.36 | Standard | Re-init6  | 0.36 |     |     | 0.36 |     | 0.36 |     |
| ---- | -------- | --------- | ---- | --- | --- | ---- | --- | ---- | --- |
| 0.18 | Re-init1 | Re-init10 | 0.18 |     |     | 0.18 |     | 0.18 |     |
Re-init3
| 0.00 |     |     | 0.00 |     |     | 0.00 |     | 0.00 |     |
| ---- | --- | --- | ---- | --- | --- | ---- | --- | ---- | --- |
0 50 100 150 200 250 0 50 100 150 200 250 0 50 100 150 200 250 0 50 100 150 200 250
|     |     | Steps |     |     | Steps |     | Steps |     | Steps |
| --- | --- | ----- | --- | --- | ----- | --- | ----- | --- | ----- |
Figure7: L2distancetotheinitialparametersduringfine-tuningBERTonRTE.Re-initreducesthe
amountofchangeintheweightsoftopTransformerblocks. However,re-initializingtoomanylayers
causesalargerchangeinthebottomTransformerblocks.
|                     | RTE(1k) |     |                | MRPC(1k) |     |                | STS-B(1k) |                | CoLA(1k) |
| ------------------- | ------- | --- | -------------- | -------- | --- | -------------- | --------- | -------------- | -------- |
| ecnamrofrePlaV 0.75 |         |     | ecnamrofrePlaV |          |     | ecnamrofrePlaV |           | ecnamrofrePlaV |          |
|                     |         |     | 0.875          |          |     | 0.88           |           |                |          |
0.60
0.70
0.86
0.850
0.65
|     |     | Re-init6 |       |     | Re-init5 |      | Re-init4 |      | Re-init1 |
| --- | --- | -------- | ----- | --- | -------- | ---- | -------- | ---- | -------- |
|     |     |          |       |     |          | 0.84 |          | 0.55 |          |
|     |     | Standard | 0.825 |     | Standard |      | Standard |      | Standard |
0.60
0.82
96 200 400 800 16003200 96 200 400 800 16003200 96 200 400 800 16003200 96 200 400 800 16003200
TrainingIterations TrainingIterations TrainingIterations TrainingIterations
Figure 8: Mean (solid lines) and range (shaded region) of validation performance trained with
differentnumberofiterations,acrosseightrandomtrials.
three-epochspracticeforBERTfine-tuningissub-optimal. Fine-tuningBERTlongercanimprove
bothtrainingstabilityandmodelperformance.
Experimentalsetup
Westudytheeffectofincreasingthenumberoffine-tuningiterationsforthe
datasetsinSection3. Forthe1kdownsampleddatasets,wherethreeepochscorrespondto96steps,
wetunethenumberofiterationsin{200,400,800,1600,3200}. Forthefoursmalldatasets,wetune
thenumberofiterationsinthesamerangebutskipvaluessmallerthanthenumberofiterationsused
inthreeepochs. Weevaluateourmodelstentimesonthevalidationsetduringfine-tuning. This
numberisidenticaltotheexperimentsinSections4–5,andcontrolsforthesetofmodelstochoose
from. Wetunewitheightdifferentrandomseedsandselectthebestsetofhyperparametersbasedon
themeanvalidationperformancetosaveexperimentalcosts. Afterthehyperparametersearch,we
fine-tunewiththebesthyperparametersfor20seedsandreportthetestperformance.
| Results |     |     |     |     |     | Longer |     |     |     |
| ------- | --- | --- | --- | --- | --- | ------ | --- | --- | --- |
Table 1 shows the result under the column. Training longer can improve over
thethree-epochssetupmostofthetime,intermsofbothperformanceandstability. Thisismore
pronounced on the 1k downsampled datasets. We also find that training longer reduces the gap
betweenstandardfine-tuningandRe-init,indicatingthattrainingformoreiterationscanhelpthese
modelsrecoverfrombadinitializations. However,ondatasetssuchasMRPCandMNLI,Re-initstill
improvesthefinalperformanceevenwithtraininglonger. Weshowthevalidationresultsonthefour
downsampleddatasetswithdifferentnumberoftrainingiterationsinFigure8. Weprovideasimilar
plotinFigure14,AppendixGfortheotherdownsampleddatasets. Weobservethatdifferenttasks
generallyrequiredifferentnumberoftrainingiterationsanditisdifficulttoidentifyaone-size-fits-all
solution. Therefore,werecommendpractitionerstotunethenumberoftrainingiterationsontheir
datasetswhentheydiscoverinstabilityinfine-tuning. Wealsoobservethatonmostofthedatasets,
Re-initrequiresfeweriterationstoachievethebestperformance,corroboratingthatRe-initprovides
abetterinitializationforfine-tuning.
| 7 REVISITING |     |     | EXISTING | METHODS |     | FEW-SAMPLE |     | BERT | FINE-TUNING |
| ------------ | --- | --- | -------- | ------- | --- | ---------- | --- | ---- | ----------- |
FOR
InstabilityinBERTfine-tuning,especiallyinfew-samplesettings,isreceivingincreasingattention
recently(Devlinetal.,2019;Phangetal.,2018;Leeetal.,2020;Dodgeetal.,2020). Werevisit
these methods given our analysis of the fine-tuning process, focusing on the impact of using the
debiasedADAMinsteadofBERTADAM(Section4). Generally,wefindthatwhenthesemethods
arere-evaluatedwiththeunbiasedADAMtheyarelesseffectivewithrespecttotheimprovementin
fine-tuningstabilityandperformance.
7

PublishedasaconferencepaperatICLR2021
Standard Int.Task LLRD Mixout Pre-trainedWD WD Re-init Longer
RTE 69.5±2.5 81.8±1.7 69.7±3.2 71.3±1.4 69.6±2.1 69.5±2.5 72.6±1.6 72.3±1.9
MRPC 90.8±1.3 91.8±1.0 91.3±1.1 90.4±1.4 90.8±1.3 90.8±1.3 91.4±0.8 91.0±1.3
STS-B 89.0±0.6 89.2±0.3 89.2±0.4 89.2±0.4 89.0±0.5 89.0±0.6 89.4±0.2 89.6±0.3
CoLA 63.0±1.5 63.9±1.8 63.0±2.5 61.6±1.7 63.4±1.5 63.0±1.5 64.2±1.6 62.4±1.7
Table2:Meantestperformanceandstandarddeviationonfourdatasets. Numbersthatarestatistically
significantlybetterthanthestandardsetting(leftcolumn)areinblueandunderlined. Theresultsof
Re-initandLongerarecopiedfromTable1. AllexperimentsuseADAMwithdebiasing(Section4).
ExceptLonger,allmethodsaretrainedwiththreeepochs. “Int. Task”standsfortransferingviaan
intermediatetask(MNLI).
7.1 OVERVIEW
Pre-trainedWeightDecay Weightdecay(WD)isacommonregularizationtechnique(Krogh&
Hertz,1992). Ateachoptimizationiteration,λwissubtractedfromthemodelparameters,whereλis
ahyperparameterfortheregularizationstrengthandwisthemodelparameters. Pre-trainedweight
decay adapts this method for fine-tuning pre-trained models (Chelba & Acero, 2004; Daumé III,
2007)bysubtractingλ(w−wˆ)fromtheobjective,wherewˆ isthepre-trainedparameters. Leeetal.
(2020)empiricallyshowthatpre-trainedweightdecayworksbetterthanconventionalweightdecay
inBERTfine-tuningandcanstabilizefine-tuning.
Mixout Mixout(Leeetal.,2020)isastochasticregularizationtechniquemotivatedbyDropout(Sri-
vastavaetal.,2014)andDropConnect(Wanetal.,2013). Ateachtrainingiteration, eachmodel
parameterisreplacedwithitspre-trainedvaluewithprobabilityp. Thegoalistopreventcatastrophic
forgetting,and(Leeetal.,2020)provesitconstrainsthefine-tunedmodelfromdeviatingtoomuch
fromthepre-trainedinitialization.
Layer-wise Learning Rate Decay (LLRD) LLRD (Howard & Ruder, 2018) is a method that
applies higher learning rates for top layers and lower learning rates for bottom layers. This is
accomplishedbysettingthelearningrateofthetoplayerandusingamultiplicativedecayrateto
decreasethelearningratelayer-by-layerfromtoptobottom. Thegoalistomodifythelowerlayers
thatencodemoregeneralinformationlessthanthetoplayersthataremorespecifictothepre-training
task. Thismethodisadoptedinfine-tuningseveralrecentpre-trainedmodels,includingXLNet(Yang
etal.,2019b)andELECTRA(Clarketal.,2020).
TransferringviaanIntermediateTask Phangetal.(2018)proposetoconductsupplementary
fine-tuningonalarger,intermediatetaskbeforefine-tuningonfew-sampledatasets. Theyshowthat
thisapproachcanreducevarianceacrossdifferentrandomtrialsandimprovemodelperformance.
Theirresultsshowthattransferringmodelsfine-tunedonMNLI(Williamsetal.,2018)canleadto
significantimprovementonseveraldownstreamtasksincludingRTE,MRPC,andSTS-B.Incontrast
totheothermethods,thisapproachrequireslargeamountofadditionalannotateddata.
7.2 EXPERIMENTS
WeevaluateallmethodsonRTE,MRPC,STS-B,andCoLA.Wefine-tuneaBERT modelusing
Large
theADAMoptimizerwithdebiasingforthreeepochs,thedefaultnumberofepochsusedwitheachof
themethods. Forintermediatetaskfine-tuning,wefine-tuneaBERT modelonMNLIandthen
Large
fine-tuneforourevaluation. Forothermethods,weperformhyperparametersearchwithasimilar
sizesearchspaceforeachmethod,asdescribedinAppendixH.Wedomodelselectionusingthe
averagevalidationperformanceacross20randomseeds. Weadditionallyreportresultsforstandard
fine-tuningwithlongertrainingtime(Section6),weightdecay,andRe-init(Section5).
Table2providesourresults. Comparedtopublishedresults(Phangetal.,2018;Leeetal.,2020),
our test performance for Int. Task (transferring via an intermediate task), Mixout, Pre-trained
WD,andWDaregenerallyhigherwhenusingtheADAMwithdebiasing.10 However,weobserve
less pronounced benefits for all surveyed methods compared to results originally reported. At
10ThenumbersinTable2arenotdirectlycomparablewithpreviouslypublishedvalidationresults(Phang
etal.,2018;Leeetal.,2020)becausewearereportingtestperformance.However,therelativelylargemargin
betweenourresultsandpreviouslypublishedresultsindicatesanimprovement.Moreimportant,ourfocusisthe
relativeimprovement,orlackofimprovementcomparedtosimplytraininglonger.
8

PublishedasaconferencepaperatICLR2021
times, these methods do not outperform the standard baselines or simply training longer. Using
additionalannotateddataforintermediatetasktrainingcontinuestobeeffective,leadingtoconsistent
improvementovertheaverageperformanceacrossalldatasets.LLRDandMixoutshowlessconsistent
performanceimpact. Weobservenonoticeableimprovementusingpre-trainedweightdecayand
conventionalweightdecayinimprovingorstabilizingBERTfine-tuninginourexperiments,contrary
toexistingwork(Leeetal.,2020). Thisindicatesthatthesemethodspotentiallyeasetheoptimization
difficultybroughtbythedebiasingomissioninBERTADAM,andwhenweaddthedebiasing,the
positiveeffectsarereduced.
8 CONCLUSION
Wehavedemonstratedthatoptimizationplaysavitalroleinthefew-sampleBERTfine-tuning. First,
weshowthatthedebiasingomissioninBERTADAMisthemaincauseofdegeneratemodelsonsmall
datasetscommonlyobservedinpreviouswork(Phangetal.,2018;Leeetal.,2020;Dodgeetal.,
2020). Second,weobservethetoplayersofthepre-trainedBERTprovideadetrimentalinitialization
forfine-tuninganddelaylearning. Simplyre-initializingtheselayersnotonlyspeedsuplearning
butalsoleadstobettermodelperformance. Third,wedemonstratethatthecommonone-size-fits-all
three-epochspracticeforBERTfine-tuningissub-optimalandallocatingmoretrainingtimecan
stabilizefine-tuning. Finally,werevisitseveralmethodsproposedforstabilizingBERTfine-tuning
andobservethattheirpositiveeffectsarereducedwiththedebiasedADAM. Inthefuture,weplanto
extendourstudytodifferentpre-trainingobjectivesandmodelarchitectures,andstudyhowmodel
parametersevolveduringfine-tuning.
ACKNOWLEDGMENTS
WethankCheolhyoungLeeforhishelpinreproducingpreviouswork. WethankLiliYu,EthanR.
Elenberg,VarshaKishore,andRishiBommasanifortheirinsightfulcomments,andHuggingFace
fortheTransformersproject,whichenabledourwork.
REFERENCES
LuisaBentivogli,IdoKalmanDagan,DangHoa,DaniloGiampiccolo,andBernardoMagnini. The
fifthpascalrecognizingtextualentailmentchallenge. InTAC2009Workshop,2009.
DanielCer,MonaDiab,EnekoAgirre,IñigoLopez-Gazpio,andLuciaSpecia. Semeval-2017task1:
Semantictextualsimilaritymultilingualandcrosslingualfocusedevaluation. InSemEval-2017,
2017.
CiprianChelbaandAlexAcero. Adaptationofmaximumentropycapitalizer: Littledatacanhelpa
lot. InEMNLP,2004.
KevinClark,Minh-ThangLuong,QuocV.Le,andChristopherD.Manning. ELECTRA:Pre-training
textencodersasdiscriminatorsratherthangenerators. InICLR,2020.
HalDauméIII. Frustratinglyeasydomainadaptation. InACL,2007.
YannNDauphinandSamuelSchoenholz. Metainit: Initializinglearningbylearningtoinitialize. In
NeurIPS,2019.
JacobDevlin,Ming-WeiChang,KentonLee,andKristinaToutanova. BERT:Pre-trainingofdeep
bidirectionaltransformersforlanguageunderstanding. InNAACL-HLT,2019.
JesseDodge,GabrielIlharco,RoySchwartz,AliFarhadi,HannanehHajishirzi,andNoahSmith.
Fine-tuningpretrainedlanguagemodels: Weightinitializations,dataorders,andearlystopping.
arXivpreprintarXiv:2002.06305,2020.
WilliamBDolanandChrisBrockett. Automaticallyconstructingacorpusofsententialparaphrases.
InIWP,2005.
9

PublishedasaconferencepaperatICLR2021
MattGardner,JoelGrus,MarkNeumann,OyvindTafjord,PradeepDasigi,NelsonFLiu,Matthew
Peters, MichaelSchmitz, andLukeZettlemoyer. Allennlp: Adeepsemanticnaturallanguage
processingplatform. InNLP-OSS,2018.
XavierGlorotandYoshuaBengio. Understandingthedifficultyoftrainingdeepfeedforwardneural
networks. InAISTATS,2010.
JianGuo,HeHe,TongHe,LeonardLausen,MuLi,HaibinLin,XingjianShi,ChenguangWang,
JunyuanXie,ShengZha,AstonZhang,HangZhang,ZhiZhang,ZhongyueZhang,andShuai
Zheng. Gluoncvandgluonnlp: Deeplearningincomputervisionandnaturallanguageprocessing.
arXivpreprintarXiv:1907.04433,2019.
KelvinGuu,KentonLee,ZoraTung,PanupongPasupat,andMing-WeiChang. Realm: Retrieval-
augmentedlanguagemodelpre-training. arXivpreprintarXiv:2002.08909,2020.
KaimingHe,XiangyuZhang,ShaoqingRen,andJianSun. Delvingdeepintorectifiers: Surpassing
human-levelperformanceonimagenetclassification. InICCV,2015.
J.HewittandP.Liang. Designingandinterpretingprobeswithcontroltasks. InEMNLP,2019.
JohnHewittandChristopherD.Manning. Astructuralprobeforfindingsyntaxinwordrepresenta-
tions. InNAACL,2019.
Neil Houlsby, Andrei Giurgiu, Stanislaw Jastrzebski, Bruna Morrone, Quentin De Laroussilhe,
AndreaGesmundo,MonaAttariyan,andSylvainGelly. Parameter-efficienttransferlearningfor
NLP. InICML,2019.
JeremyHowardandSebastianRuder. Universallanguagemodelfine-tuningfortextclassification. In
ACL,2018.
Shankar Iyer, Nikhil Dandekar, and Kornel Csernai. First quora dataset release: Question pairs.
https://tinyurl.com/y2y8u5ed,2017.
DiederikPKingmaandJimmyBa. Adam: Amethodforstochasticoptimization. arXivpreprint
arXiv:1412.6980,2014.
AndersKroghandJohnA.Hertz. Asimpleweightdecaycanimprovegeneralization. InNeurIPS,
1992.
Zhenzhong Lan, Mingda Chen, Sebastian Goodman, Kevin Gimpel, Piyush Sharma, and Radu
Soricut. Albert: Alitebertforself-supervisedlearningoflanguagerepresentations. InICLR,2020.
CheolhyoungLee,KyunghyunCho,andWanmoKang. Mixout: Effectiveregularizationtofinetune
large-scalepretrainedlanguagemodels. InICLR,2020.
MikeLewis,YinhanLiu,NamanGoyal,MarjanGhazvininejad,AbdelrahmanMohamed,OmerLevy,
VeselinStoyanov,andLukeZettlemoyer. Bart: Denoisingsequence-to-sequencepre-trainingfor
naturallanguagegeneration,translation,andcomprehension. arXivpreprintarXiv:1910.13461,
2019.
XingjianLi,HaoyiXiong,HaozheAn,ChengzhongXu,andDejingDou. Rifle: Backpropagationin
depthfordeeptransferlearningthroughre-initializingthefully-connectedlayer. InICML,2020.
NelsonF.Liu,MattGardner,YonatanBelinkov,MatthewE.Peters,andNoahA.Smith. Linguistic
knowledgeandtransferabilityofcontextualrepresentations. arXivpreprintarXiv:1903.08855,
2019a.
XiaodongLiu,PengchengHe,WeizhuChen,andJianfengGao. Multi-taskdeepneuralnetworksfor
naturallanguageunderstanding. InACL,2019b.
Xiaodong Liu, Yu Wang, Jianshu Ji, Hao Cheng, Xueyun Zhu, Emmanuel Awa, Pengcheng He,
WeizhuChen,HoifungPoon,GuihongCao,andJianfengGao. Themicrosofttoolkitofmulti-task
deepneuralnetworksfornaturallanguageunderstanding. arXivpreprintarXiv:2002.07972,2020.
YangLiu. Fine-tuneBERTforextractivesummarization. arXivpreprintarXiv:1903.10318,2019.
10

PublishedasaconferencepaperatICLR2021
YinhanLiu,MyleOtt,NamanGoyal,JingfeiDu,MandarJoshi,DanqiChen,OmerLevy,MikeLewis,
LukeZettlemoyer,andVeselinStoyanov. RoBERTa: ARobustlyOptimizedBERTPretraining
| Approach. arXivpreprintarXiv:1907.11692,2019c. |     |     |     |
| ---------------------------------------------- | --- | --- | --- |
Brian W Matthews. Comparison of the predicted and observed secondary structure of t4 phage
| lysozyme. BiochimicaetBiophysicaActa(BBA)-ProteinStructure,1975. |     |     |     |
| ---------------------------------------------------------------- | --- | --- | --- |
AmilMerchant,ElaheRahimtoroghi,ElliePavlick,andIanTenney.Whathappenstobertembeddings
arXivpreprintarXiv:2004.14448,2020.
duringfine-tuning?
MariusMosbach,MaksymAndriushchenko,andDietrichKlakow. Onthestabilityoffine-tuning
bert: Misconceptions,explanations,andstrongbaselines. arXivpreprintarXiv:2006.04884,2020.
PreetumNakkiran,GalKaplun,YaminiBansal,TristanYang,BoazBarak,andIlyaSutskever. Deep
| doubledescent: | Wherebiggermodelsandmoredatahurt. |     | InICLR,2019. |
| -------------- | --------------------------------- | --- | ------------ |
MatthewE.Peters,SebastianRuder,andNoahA.Smith. Totuneornottotune? adaptingpretrained
| representationstodiversetasks. |     | arXivpreprintarXiv:1903.05987,2019. |     |
| ------------------------------ | --- | ----------------------------------- | --- |
JasonPhang,ThibaultFévry,andSamuelRBowman. Sentenceencodersonstilts: Supplementary
trainingonintermediatelabeled-datatasks. arXivpreprintarXiv:1811.01088,2018.
MartinPopelandOndˇrejBojar. Trainingtipsforthetransformermodel. ThePragueBulletinof
MathematicalLinguistics,2018.
AlecRadford,JeffWu,RewonChild,DavidLuan,DarioAmodei,andIlyaSutskever. Language
modelsareunsupervisedmultitasklearners. 2019.
RichardSocher,AlexPerelygin,JeanWu,JasonChuang,ChristopherDManning,AndrewYNg,
andChristopherPotts. Recursivedeepmodelsforsemanticcompositionalityoverasentiment
| treebank. InEMNLP,2013. |     |     |     |
| ----------------------- | --- | --- | --- |
Nitish Srivastava, Geoffrey Hinton, Alex Krizhevsky, Ilya Sutskever, and Ruslan Salakhutdinov.
Dropout: asimplewaytopreventneuralnetworksfromoverfitting. JMLR,2014.
Asa Cooper Stickland and Iain Murray. Bert and pals: Projected attention layers for efficient
| adaptationinmulti-tasklearning. |     | InICML,2019. |     |
| ------------------------------- | --- | ------------ | --- |
ChiSun,XipengQiu,YigeXu,andXuanjingHuang. Howtofine-tunebertfortextclassification? In
CCL,2019.
AlexTamkin,TrishaSingh,DavideGiovanardi,andNoahGoodman. Investigatingtransferabilityin
| pretrainedlanguagemodels. |     | InEMNLP,2020. |     |
| ------------------------- | --- | ------------- | --- |
IanTenney,DipanjanDas,andElliePavlick. Bertrediscoverstheclassicalnlppipeline. InACL,
2019a.
IanTenney,PatrickXia,BerlinChen,AlexWang,AdamPoliak,RThomasMcCoy,NajoungKim,
BenjaminVanDurme,SamBowman,DipanjanDas,andElliePavlick. Whatdoyoulearnfrom
context? probingforsentencestructureincontextualizedwordrepresentations. InICLR,2019b.
AshishVaswani,NoamShazeer,NikiParmar,JakobUszkoreit,LlionJones,AidanNGomez,Łukasz
| Kaiser,andIlliaPolosukhin. |     | Attentionisallyouneed. | InNeurIPS,2017. |
| -------------------------- | --- | ---------------------- | --------------- |
David Wadden, Ulme Wennberg, Yi Luan, and Hannaneh Hajishirzi. Entity, relation, and event
| extractionwithcontextualizedspanrepresentations. |     |     | InEMNLP-IJCNLP,2019. |
| ------------------------------------------------ | --- | --- | -------------------- |
Li Wan, Matthew Zeiler, Sixin Zhang, Yann Le Cun, and Rob Fergus. Regularization of neural
| networksusingdropconnect. |     | InICML,2013. |     |
| ------------------------- | --- | ------------ | --- |
AlexWang,YadaPruksachatkun,NikitaNangia,AmanpreetSingh,JulianMichael,FelixHill,Omer
Levy, and Samuel Bowman. Superglue: A stickier benchmark for general-purpose language
InNeurIPS,2019a.
understandingsystems.
11

PublishedasaconferencepaperatICLR2021
AlexWang,AmanpreetSingh,JulianMichael,FelixHill,OmerLevy,andSamuelBowman. Glue: A
multi-taskbenchmarkandanalysisplatformfornaturallanguageunderstanding. InICLR,2019b.
AlexWang,IanF.Tenney,YadaPruksachatkun,PhilYeres,JasonPhang,HaokunLiu,PhuMonHtut,
KatherinYu, JanHula, PatrickXia, RaghuPappagari, ShuningJin, R.ThomasMcCoy, Roma
Patel,YinghuiHuang,EdouardGrave,NajoungKim,ThibaultFévry,BerlinChen,NikitaNangia,
AnhadMohananey,KatharinaKann,ShikhaBordia,NicolasPatry,DavidBenton,ElliePavlick,
andSamuelR.Bowman. jiant1.3: Asoftwaretoolkitforresearchongeneral-purposetext
understandingmodels. http://jiant.info/,2019c.
AlexWarstadt,AmanpreetSingh,andSamuelRBowman. Neuralnetworkacceptabilityjudgments.
TACL,2019.
Adina Williams, Nikita Nangia, and Samuel Bowman. A broad-coverage challenge corpus for
sentenceunderstandingthroughinference. InACL,2018.
ThomasWolf,LysandreDebut,VictorSanh,JulienChaumond,ClementDelangue,AnthonyMoi,
Pierric Cistac, Tim Rault, R’emi Louf, Morgan Funtowicz, and Jamie Brew. Huggingface’s
transformers: State-of-the-art natural language processing. arXiv preprint arXiv:1910.03771,
2019.
Wei Yang, Haotian Zhang, and Jimmy Lin. Simple applications of BERT for ad hoc document
retrieval. arXivpreprintarXiv:1903.10972,2019a.
ZhilinYang,ZihangDai,YimingYang,JaimeCarbonell,RussRSalakhutdinov,andQuocVLe.
Xlnet: Generalizedautoregressivepretrainingforlanguageunderstanding. InNeurIPS,2019b.
JasonYosinski,JeffClune,YoshuaBengio,andHodLipson. Howtransferablearefeaturesindeep
neuralnetworks? InNeurIPS,2014.
HongyiZhang,YannN.Dauphin,andTengyuMa. Residuallearningwithoutnormalizationviabetter
initialization. InICLR,2019.
Tianyi Zhang, Varsha Kishore, Felix Wu, Kilian Q. Weinberger, and Yoav Artzi. BERTScore:
EvaluatingTextGenerationwithBERT. InICLR,2020.
JinhuaZhu,YingceXia,LijunWu,DiHe,TaoQin,WengangZhou,HouqiangLi,andTieyanLiu.
Incorporatingbertintoneuralmachinetranslation. InICLR,2020.
12

PublishedasaconferencepaperatICLR2021
|     | RTE | MRPC STS-B | CoLA | SST-2 QNLI | QQP MNLI |
| --- | --- | ---------- | ---- | ---------- | -------- |
Task NLI Paraphrase Similarity Acceptibility Sentiment NLI Paraphrase NLI
| #oftrainingsamples     | 2.5k | 3.7k 5.8k | 8.6k | 61.3k 104k | 363k 392k |
| ---------------------- | ---- | --------- | ---- | ---------- | --------- |
| #ofvalidationsamples   | 139  | 204 690   | 521  | 1k 1k      | 1k 1k     |
| #oftestsamples         | 139  | 205 690   | 521  | 1.8k 5.5k  | 40k 9.8k  |
| Evaluationmetric       | Acc. | F1 SCC    | MCC  | Acc. Acc.  | Acc. Acc. |
| Majoritybaseline(val)  | 52.9 | 81.3 0    | 0    | 50.0 50.0  | 50.0 33.3 |
| Majoritybaseline(test) | 52.5 | 81.2 0    | 0    | 49.1 50.5  | 63.2 31.8 |
Table3: Thedatasetsusedinthiswork. Weapplynon-standarddatasplitstocreatetestsets. SCC
standsforSpearmanCorrelationCoefficientandMCCstandsforMatthewsCorrelationCoefficient.
A DATASETS
Table3summarizesdatasetstatisticsanddescribesourvalidation/testsplits. Wealsoprovideabrief
introductionforeachdatasets:
RTE RecognizingTextualEntailment(Bentivoglietal.,2009)isabinaryentailmentclassification
task. WeusetheGLUEversion.
MRPC MicrosoftResearchParaphraseCorpus(Dolan&Brockett,2005)isbinaryclassification
task. Givenapairofsentences,amodelhastopredictwhethertheyareparaphrasesofeachother.
WeusetheGLUEversion.
STS-B SemanticTextualSimilarityBenchmark(Ceretal.,2017)isaregressiontasksforestimating
| sentencesimilaritybetweenapairofsentences. |     | WeusetheGLUEversion. |     |     |     |
| ------------------------------------------ | --- | -------------------- | --- | --- | --- |
CoLA Corpus of Linguistic Acceptability (Warstadt et al., 2019) is a binary classification task
forverifyingwhetherasequenceofwordsisagrammaticallycorrectEnglishsentence. Matthews
correlationcoefficient(Matthews,1975)isusedtoevaluatetheperformance. WeusetheGLUE
version.
MNLI Multi-GenreNaturalLanguageInferenceCorpus(Williamsetal.,2018)isatextualentail-
mentdataset,whereamodelisaskedtopredictwhetherthepremiseentailsthehypothesis,predicts
| thehypothesis,orneither. | WeusetheGLUEversion. |     |     |     |     |
| ------------------------ | -------------------- | --- | --- | --- | --- |
QQP QuoraQuestionPairs(Iyeretal.,2017)isabinaryclassificationtasktodeterminewhether
twoquestionsaresemanticallyequivalent(i.e.,paraphraseeachother). WeusetheGLUEversion.
SST-2 The binary version of the Stanford Sentiment Treebank (Socher et al., 2013) is a binary
classification task for whether a sentence has positive or negative sentiment. We use the GLUE
version.
| B ISOLATING | THE IMPACT | OF DIFFERENT | SOURCES | OF RANDOMNESS |     |
| ----------- | ---------- | ------------ | ------- | ------------- | --- |
TherandomnessinBERTfine-tuningcomesfromthreesources: (a)weightinitialization,(b)data
order,and(c)Dropoutregularization(Srivastavaetal.,2014). Wecontroltherandomnessusingtwo
separaterandomnumbergenerators: oneforweightinitializationandtheotherforbothdataorder
andDropout(bothofthemaffectthestochasticlossateachiteration). Wefine-tuneBERTonRTE
forthreeepochsusingADAMwith10seedsforbothrandomnumbergenerators. Wecomparethe
standardsetupwithRe-init5,whereL=5. ThisexperimentissimilartoDodgeetal.(2020),butwe
useADAMwithdebiasinginsteadofBERTADAMandcontrolfortherandomnessinDropoutaswell.
Whenfixingarandomseedforweightinitialization,Re-init5sharesthesameinitializedclassifier
weightswiththestandardbaseline. Figure9showsthevalidationaccuracyofeachindividualrunas
wellastheminimum,average,andmaximumscoreswhenfixingoneoftherandomseeds. Figure10
summarizesthestandarddeviationswhenoneoftherandomseedsiscontrolled. Weobserveseveral
trends.Re-init5usuallyimprovestheperformanceregardlessoftheweightinitializationordataorder
andDropout. Second,Re-init5stillreducestheinstabilitywhenoneofthesourcesofrandomnessis
controlled. Third,thestandarddeviationoffixingtheweightinitializationroughlymatchestheone
ofcontrolleddataorderandDropout,whichalignswiththeobservationofDodgeetal.(2020).
13

PublishedasaconferencepaperatICLR2021
|     | Standard                               |     |     |                                        | Re-init 5 |     |
| --- | -------------------------------------- | --- | --- | -------------------------------------- | --------- | --- |
|     | Random Seed for Data Order and Dropout |     |     | Random Seed for Data Order and Dropout |           |     |
0 1 2 3 4 5 6 7 8 9 MinMeanMax 0 1 2 3 4 5 6 7 8 9 MinMeanMax
0 69.5774.6473.9172.4668.1271.0174.6473.1971.7473.1968.1272.2574.64 0 72.4675.3673.1977.5473.9174.6473.9175.3674.6474.6472.4674.5777.54
78 78
1 73.9173.1971.0168.8470.2968.8476.0971.7471.7473.9168.8471.9676.09 1 75.3677.5473.1976.0972.4676.0975.3676.0973.1977.5472.4675.2977.54
2 71.0167.3968.8475.3669.5768.1269.5768.1268.1270.2967.3969.6475.36 76 2 73.9174.6471.7473.9173.1974.6473.9174.6472.4676.0971.7473.9176.09 76
noitazilaitinI rof deeS modnaR 3 70.2968.1271.7471.0172.4673.1963.7771.7471.7468.1263.7770.2273.19 noitazilaitinI rof deeS modnaR 3 75.3675.3671.7478.9975.3676.0974.6476.8173.9176.0971.7475.4378.99
74 74
4 73.1970.2967.3971.0170.2971.7469.5771.0167.3967.3967.3969.9373.19 4 75.3675.3673.1975.3673.1976.0973.1973.1973.9176.8173.1974.5776.81
5 73.1971.7470.2971.7470.2971.7470.2973.1971.7473.1970.2971.7473.19 5 71.0173.1969.5773.1973.1973.9173.9171.0171.0173.9169.5772.3973.91
72 72
6 72.4668.8472.4669.5769.5769.5771.0171.0168.1271.7468.1270.4372.46 6 77.5475.3673.9173.9176.0976.8174.6473.9173.9176.0973.9175.2277.54
7 71.7471.7473.1968.1271.7471.7469.5773.9172.4673.1968.1271.7473.91 70 7 75.3674.6471.0173.9173.9176.0976.0974.6475.3676.0971.0174.7176.09 70
71.7473.9169.5767.3972.4670.2971.7472.4673.9168.8467.3971.2373.91 73.9173.1971.7474.6473.1972.4673.9173.1972.4673.1971.7473.1974.64
| 8   |     |     |     | 8   |     |     |
| --- | --- | --- | --- | --- | --- | --- |
68 68
9 76.0973.1971.0171.0172.4673.1973.9171.7473.1975.3671.0173.1276.09 9 74.6473.1973.9175.3673.1973.9174.6476.0973.1973.9173.1974.2076.09
Min 69.5767.3967.3967.3968.1268.1263.7768.1267.3967.3963.7769.6472.46 Min 71.0173.1969.5773.1972.4672.4673.1971.0171.0173.1969.5772.3973.91
66 66
Mean 72.3271.3070.9470.6570.7270.9471.0171.8171.0171.5268.0471.2274.20 Mean 74.4974.7872.3275.2973.7775.0774.4274.4973.4175.4372.1074.3576.52
Max 76.0974.6473.9175.3672.4673.1976.0973.9173.9175.3671.0173.1276.09 64 Max 77.5477.5473.9178.9976.0976.8176.0976.8175.3677.5473.9175.4378.99 64
Figure9: ValidationaccuracyonRTEwithcontrolledrandomseeds. Themin,mean,andmaxvalues
ofcontrollingoneoftherandomseedsarealsoincluded. Re-init5usuallyimprovesthevalidation
accuracy.
|     | Standard                               |       |           |                                        | Re-init 5 |               |
| --- | -------------------------------------- | ----- | --------- | -------------------------------------- | --------- | ------------- |
|     | Random Seed for Data Order and Dropout |       |           | Random Seed for Data Order and Dropout |           |               |
|     |                                        |       | Avg.      |                                        |           | Avg.          |
| 0   | 1 2 3 4 5                              | 6 7 8 | 9 Std Std | 0 1 2                                  | 3 4 5 6   | 7 8 9 Std Std |
| 0   |                                        |       | 2.16 3.5  | 0                                      |           | 1.39 3.5      |
| 1   |                                        |       | 2.34      | 1                                      |           | 1.79          |
3.0 3.0
| 2                              |     |     | 2.30                           | 2   |     | 1.23     |
| ------------------------------ | --- | --- | ------------------------------ | --- | --- | -------- |
| noitazilaitinI rof deeS modnaR |     |     | noitazilaitinI rof deeS modnaR |     |     |          |
| 3                              |     |     | 2.83 2.5                       | 3   |     | 1.88 2.5 |
| 4                              |     |     | 2.00                           | 4   |     | 1.39     |
2.0 2.0
| 5   |     |     | 1.18 | 5   |     | 1.58 |
| --- | --- | --- | ---- | --- | --- | ---- |
| 6   |     |     | 1.52 | 6   |     | 1.36 |
1.5 1.5
| 7   |     |     | 1.74 | 7   |     | 1.54 |
| --- | --- | --- | ---- | --- | --- | ---- |
| 8   |     |     | 2.16 | 8   |     | 0.84 |
1.0 1.0
| 9   |     |     | 1.69 | 9   |     | 0.98 |
| --- | --- | --- | ---- | --- | --- | ---- |
1.90 2.54 2.00 2.32 1.50 1.72 3.45 1.62 2.29 2.71 2.21 0.5 1.80 1.36 1.40 1.82 1.12 1.37 0.84 1.74 1.23 1.43 1.41 0.5
| Std      |     |     |      | Std      |     |      |
| -------- | --- | --- | ---- | -------- | --- | ---- |
| Avg. Std |     |     | 1.99 | Avg. Std |     | 1.40 |
0.0 0.0
Figure10: ThestandarddeviationofthevalidationaccuracyonRTEwithcontrolledrandomseeds.
WeshowthestandarddeviationoffixingeithertheinitializationordataorderandDropout. Re-init5
consistentlyreducestheinstabilityregardlessofthesourcesoftherandomness.
| C MIXED | PRECISION | TRAINING |     |     |     |     |
| ------- | --------- | -------- | --- | --- | --- | --- |
Mixedprecisiontrainingcanacceleratemodeltrainingwhilepreservingperformancebyreplacing
some 32-bit floating-point computation with 16-bit floating-point computation. We use mixed
precision training in all our experiments using huggingface’s Transformers (Wolf et al., 2019).
TransformersusesO1-leveloptimizedmixedprecisiontrainingimplementedwiththeApexlibrary.11
Weevaluateifthismixedprecisionimplementationinfluencesourresults.Wefine-tuneBERTwith20
randomtrialsonRTE,MRPC,STS-B,andCoLA.Weusetwo-tailedt-testtotestifthedistributions
ofthetwomethodsarestatisticallydifferent. Table4showsthemeanandstandarddeviationofthe
11https://github.com/NVIDIA/apex
14

PublishedasaconferencepaperatICLR2021
|     |                |     | CoLA     |     | MRPC     | RTE      | STS-B    |
| --- | -------------- | --- | -------- | --- | -------- | -------- | -------- |
|     | Mixedprecision |     | 60.3±1.5 |     | 89.2±1.2 | 71.8±2.1 | 90.1±0.7 |
|     |                |     | 59.9±1.5 |     | 88.7±1.4 | 71.4±2.2 | 90.1±0.7 |
Fullprecision
Table 4: Comparing BERT fine-tuning with mixed precision and full precision. The difference
betweenthetwonumbersonanydatasetisnotstatisticallysignificant.
|     |     |     |     |     | DevAcc. (%) | TestAcc. | (%) |
| --- | --- | --- | --- | --- | ----------- | -------- | --- |
|     |     |     |     |     | 86.0±0.3    | 87.0±0.4 |     |
Nobiascorrection
|     |     | Biascorrection |     |     | 85.9±0.3 | 86.9±0.3 |     |
| --- | --- | -------------- | --- | --- | -------- | -------- | --- |
Table5: ComparingBERTfine-tuningwithandwithoutbiascorrectionontheMNLIdataset. When
wehavealargedataset,thereisnosignificantdifferenceinusingbiascorrectionornot.
testperformance. Theperformanceofmixedprecisionmatchesthesingleprecisioncounterpart,and
thereisnostatisticallysignificantdifference.
| D BIAS-CORRECTION |     |     | ON MNLI |     |     |     |     |
| ----------------- | --- | --- | ------- | --- | --- | --- | --- |
Thefocusofthispaperisfew-samplelearning. However,wealsoexperimentwiththefullMNLI
dataset. Table 5 shows that average accuracy over three random runs. The results confirm that
there is no significant difference in using bias correction or not on such a large dataset. While
our recommended practices do not improve training on large datasets, this result shows there is
nodisadvantagetofine-tunesuchmodelswiththesameprocedureasweproposeforfew-sample
training.
| E SUPPLEMENTARY |     |     | MATERIAL |     | SECTION | 4   |     |
| --------------- | --- | --- | -------- | --- | ------- | --- | --- |
FOR
EffectofADAMwithDebiasingonConvergence. Figure11showsthetraininglossasafunction
ofthenumberoftrainingiterations. Usingbiascorrectioneffectivelyspeedsupconvergenceand
reducestherangeofthetrainingloss,whichisconsistentwithourobservationinFigure3.
EffectofADAMwithDebiasingontheExpectedValidationPerformance. Figure12showsthe
expectedvalidationperformanceasafunctionofthenumberofrandomtrials. ComparingtoFigure4,
weobserveseveraltrends. First,usingADAMwithdebiasingconsistentlyleadstofasterconvergence
andimprovedvalidationperformance,whichissimilartoourobservationaboutthetestperformance.
Second, we observe that the expected validation performance monotonically increases with the
numberofrandomtrials,contrarytoourobservationaboutthetestperformance. Thissuggeststhat
usingtoomanyrandomtrialsmayoverfittothevalidationsetandhurtgeneralizationperformance.
| F SUPPLEMENTARY |     |     | MATERIAL | FOR | SECTION | 5   |     |
| --------------- | --- | --- | -------- | --- | ------- | --- | --- |
EffectofLonRe-init Figure13showstheeffectofRe-initinfine-tuningontheeightdownsampled
datasets. We observe similar trends in Figure 13 and Figure 5. Re-init’s improvement is more
pronouncedinthewort-caseperformanceacrossdifferentrandomtrials. Second,thebestvalueofL
isdifferentforeachdataset.
EffectofRe-initonModelParameters WeusethesamesetupasinFigure7toplotthechange
intheweightsofdifferentTransformerblocksduringfine-tuningonRTE,MRPC,STS-B,andCoLA
inFigures15–18.
EffectofRe-initonOtherModels Westudymorerecentpre-trainedcontexualembeddingmodels
beyond BERT . We investigate whether Re-init provides better fine-tuning initialization in
Large
XLNet Yangetal.(2019b),RoBERTa Liuetal.(2019c),BART Lewisetal.(2019),and
| Large |     |     |     | Large |     |     | Large |
| ----- | --- | --- | --- | ----- | --- | --- | ----- |
ELECTRA Large Clarketal.(2020). XLNetisanautoregressivelanguagemodeltrainedbylearning
15

PublishedasaconferencepaperatICLR2021
|      | RTE |     | MRPC |     | STS-B |     | CoLA |
| ---- | --- | --- | ---- | --- | ----- | --- | ---- |
| 1.00 |     |     |      | 10  |       |     |      |
Correction
0.6
| ssoLniarT |     | 0.75 |     |     | NoCorrection |     |     |
| --------- | --- | ---- | --- | --- | ------------ | --- | --- |
0.75
|     |     | 0.50 |     | 5   |     | 0.4 |     |
| --- | --- | ---- | --- | --- | --- | --- | --- |
0.50
|     |     | 0.25 |     |     |     | 0.2 |     |
| --- | --- | ---- | --- | --- | --- | --- | --- |
0.25
|     |        |        |         | 0      |         | 0.0    |             |
| --- | ------ | ------ | ------- | ------ | ------- | ------ | ----------- |
| 23  | 92 161 | 230 34 | 136 238 | 340 54 | 216 378 | 540 80 | 320 560 800 |
|     | Steps  |        | Steps   |        | Steps   |        | Steps       |
Figure11: Mean(solidlines)andrange(shadedregion)oftraininglossduringfine-tuningBERT,
across50randomtrials. Biascorrectionspeedsupconvergenceandreducestherangeofthetraining
loss.
|                  | RTE |      | MRPC |                  | STS-B |                  | CoLA |
| ---------------- | --- | ---- | ---- | ---------------- | ----- | ---------------- | ---- |
| 0.80             |     | 0.95 |      | 0.92             |       | 0.70             |      |
| .CCMlaV.pxE 0.74 |     | 0.92 |      | .ccAlaV.pxE 0.91 |       | .CCSlaV.pxE 0.65 |      |
1FlaV.pxE
0.60
| 0.68 |     | 0.89 |     | 0.90 |     |     |     |
| ---- | --- | ---- | --- | ---- | --- | --- | --- |
0.55
| 0.62 |     | 0.86 |     | 0.89 |     |     | Correction |
| ---- | --- | ---- | --- | ---- | --- | --- | ---------- |
0.50
| 0.56 |     | 0.83 |     | 0.88 |     |     | NoCorrection |
| ---- | --- | ---- | --- | ---- | --- | --- | ------------ |
0.45
0.50 1 10 20 30 40 50 0.80 1 10 20 30 40 50 0.87 1 10 20 30 40 50 0.40 1 10 20 30 40 50
#ofRandomTrials #ofRandomTrials #ofRandomTrials #ofRandomTrials
Figure12:Expectedvalidationperformance(solidlines)withstandarddeviation(shadedregion)over
thenumberofrandomtrialsallocatedforfine-tuningBERT.Withbiascorrection,wecanreliably
achievegoodresultswithfew(i.e.,5or10)randomtrials.
|     | RTE |     | MRPC |     | STS-B |     | CoLA |
| --- | --- | --- | ---- | --- | ----- | --- | ---- |
0.66
|     |     | 0.92 |     | 0.910 |     |     |     |
| --- | --- | ---- | --- | ----- | --- | --- | --- |
0.775
| ecnamrofreP.laV |     | ecnamrofreP.laV |     | ecnamrofreP.laV 0.905 |     | ecnamrofreP.laV 0.64 |     |
| --------------- | --- | --------------- | --- | --------------------- | --- | -------------------- | --- |
| 0.750           |     | 0.90            |     |                       |     | 0.62                 |     |
0.900
0.725
|       |     |      |     | 0.895 |     | 0.60 |     |
| ----- | --- | ---- | --- | ----- | --- | ---- | --- |
| 0.700 |     | 0.88 |     | 0.890 |     | 0.58 |     |
Standard Re-init
| 0.675 |     |     |     |       | Median | Outlier |     |
| ----- | --- | --- | --- | ----- | ------ | ------- | --- |
|       |     |     |     | 0.885 |        | 0.56    |     |
ar d ol e r it 1 it 2 it 3 it 4 it 5 init6 ar d ol e r it 1 it 2 it 3 it 4 it 5 init6 ar d ol e r it 1 it 2 it 3 it 4 it 5 init6 ar d ol e r it 1 it 2 it 3 it 4 it 5 init6
ta n d P o - in e- in e- in e- in e- in e- ta n d P o - in e- in e- in e- in e- in e- ta n d P o - in e- in e- in e- in e- in e- ta n d P o - in e- in e- in e- in e- in e-
S n it R e R R R R R S n it R e R R R R R S n it R e R R R R R S n it R e R R R R R
| R e -i |         | R e -i |          | R e -i |           | R e -i |          |
| ------ | ------- | ------ | -------- | ------ | --------- | ------ | -------- |
|        | RTE(1k) |        | MRPC(1k) |        | STS-B(1k) |        | CoLA(1k) |
0.62
|     |     | 0.88 |     | 0.88 |     |     |     |
| --- | --- | ---- | --- | ---- | --- | --- | --- |
0.700
| ecnamrofreP.laV |     | ecnamrofreP.laV |     | ecnamrofreP.laV |     | ecnamrofreP.laV 0.60 |     |
| --------------- | --- | --------------- | --- | --------------- | --- | -------------------- | --- |
| 0.675           |     | 0.86            |     | 0.86            |     |                      |     |
0.58
0.650
0.56
| 0.625 |     | 0.84 |     | 0.84 |     |     |     |
| ----- | --- | ---- | --- | ---- | --- | --- | --- |
0.54
| 0.600 |     | 0.82 |     |     |     |     |     |
| ----- | --- | ---- | --- | --- | --- | --- | --- |
0 . 8 2
ar d ol e r it 1 it 2 it 3 it 4 it 5 init6 ar d ol e r it 1 it 2 it 3 it 4 it 5 init6 ar d ol e r it 1 it 2 it 3 it 4 it 5 init6 ar d ol e r it 1 it 2 it 3 it 4 it 5 init6
ta n d P o e - in e- in e- in e- in e- in e- ta n d P o e - in e- in e- in e- in e- in e- a n d P o e - in e- in e- in e- in e- in e- ta n d P o e - in e- in e- in e- in e- in e-
S -i n it R R R R R R S -i n it R R R R R R S t i n it R R R R R R S -i n it R R R R R R
| R e |         | R e |          | R e - |         | R e  |          |
| --- | ------- | --- | -------- | ----- | ------- | ---- | -------- |
|     | SST(1k) |     | QNLI(1k) |       | QQP(1k) |      | MNLI(1k) |
|     |         |     |          | 0.82  |         | 0.70 |          |
0.90
| ecnamrofreP.laV |     | ecnamrofreP.laV 0.82 |     | ecnamrofreP.laV |     | ecnamrofreP.laV 0.65 |     |
| --------------- | --- | -------------------- | --- | --------------- | --- | -------------------- | --- |
0.81
| 0.88 |     | 0.80 |     |     |     |     |     |
| ---- | --- | ---- | --- | --- | --- | --- | --- |
0.60
0.80
|      |     | 0.78 |     |      |     | 0.55 |     |
| ---- | --- | ---- | --- | ---- | --- | ---- | --- |
| 0.86 |     |      |     | 0.79 |     |      |     |
0.50
0.76
| 0.84 |     |     |     | 0.78 |     |     |     |
| ---- | --- | --- | --- | ---- | --- | --- | --- |
0.45
ar d ol e r it 1 it 2 it 3 it 4 it 5 init6 ar d ol e r it 1 it 2 it 3 it 4 it 5 init6 ar d ol e r it 1 it 2 it 3 it 4 it 5 init6 ar d ol e r it 1 it 2 it 3 it 4 it 5 init6
ta n d P o e - in e- in e- in e- in e- in e- ta n d P o e - in e- in e- in e- in e- in e- ta n d P o e - in e- in e- in e- in e- in e- ta n d P o e - in e- in e- in e- in e- in e-
S -i n it R R R R R R S -i n it R R R R R R S -i n it R R R R R R S -i n it R R R R R R
| R e |     | R e |     | R e |     | R e |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
Figure13: Validationperformancedistributionofre-initializingdifferentnumberoflayersofBERT
onthedownsampleddatasets.
all permutations of natural language sentences. RoBERTa is similar to BERT in terms of model
architecturebutisonlypre-trainedonthemasklanguagemodelingtaskonly,butforlongerandon
16

PublishedasaconferencepaperatICLR2021
Model Dataset LearningRate TrainingEpochs/Steps BatchSize WarmupRatio/Steps LLRD
| BERT |     | all | 2×10−5 | 3epochs |     | 32  | 10% |     | -   |
| ---- | --- | --- | ------ | ------- | --- | --- | --- | --- | --- |
3×10−5
|     |     | RTE |     | 800steps |     | 32  | 200steps |     | -   |
| --- | --- | --- | --- | -------- | --- | --- | -------- | --- | --- |
5×10−5
| XLNet   |     | MRPC  |        | 800steps  |     | 32  | 200steps |     | -   |
| ------- | --- | ----- | ------ | --------- | --- | --- | -------- | --- | --- |
|         |     | STS-B | 5×10−5 | 3000steps |     | 32  | 500steps |     | -   |
|         |     | CoLA  | 3×10−5 | 1200steps |     | 128 | 120steps |     | -   |
|         |     | RTE   | 2×10−5 | 2036steps |     | 16  | 122steps |     | -   |
| RoBERTa |     | MRPC  | 1×10−5 | 2296steps |     | 16  | 137steps |     | -   |
2×10−5
|     |     | STS-B |     | 3598steps |     | 16  | 214steps |     | -   |
| --- | --- | ----- | --- | --------- | --- | --- | -------- | --- | --- |
1×10−5
|     |     | CoLA |        | 5336steps |     | 16  | 320steps |     | -   |
| --- | --- | ---- | ------ | --------- | --- | --- | -------- | --- | --- |
|     |     | RTE  | 5×10−5 | 10epochs  |     | 32  | 10%      |     | 0.9 |
|     |     | MRPC | 5×10−5 | 3epochs   |     | 32  | 10%      |     | 0.9 |
ELECTRA
|     |     | STS-B | 5×10−5 | 10epochs |     | 32  | 10% |     | 0.9 |
| --- | --- | ----- | ------ | -------- | --- | --- | --- | --- | --- |
5×10−5
|     |     | CoLA |     | 3epochs |     | 32  | 10% |     | 0.9 |
| --- | --- | ---- | --- | ------- | --- | --- | --- | --- | --- |
1×10−5
|     |     | RTE  |        | 1018steps |     | 32  | 61steps |     | -   |
| --- | --- | ---- | ------ | --------- | --- | --- | ------- | --- | --- |
|     |     | MRPC | 2×10−5 | 1148steps |     | 64  | 68steps |     | -   |
BART
|     |     | STS-B | 2×10−5 | 1799steps |     | 32  | 107steps |     | -   |
| --- | --- | ----- | ------ | --------- | --- | --- | -------- | --- | --- |
|     |     | CoLA  | 2×10−5 | 1334steps |     | 64  | 80steps  |     | -   |
Table6: Fine-tuninghyper-parametersofBERTanditsvariantsasreportedintheofficialrepository
ofeachmodel.
|     |          | RTE |                  | MRPC    |          | STS-B   |          | CoLA |         |
| --- | -------- | --- | ---------------- | ------- | -------- | ------- | -------- | ---- | ------- |
|     | Standard |     | Re-init Standard | Re-init | Standard | Re-init | Standard |      | Re-init |
XLNet 71.7±12.6 80.1±1.6 92.3±4.3 94.5±0.8 86.8±20.4 91.7±0.3 51.8±22.5 62.0±2.1
RoBERTa 78.2±12.1 83.5±1.4 94.4±0.9 94.8±0.9 91.8±0.3 91.8±0.2 68.4±2.2 67.6±1.5
87.1±1.2 86.1±1.9 95.7±0.8 95.3±0.8 91.8±1.9 92.1±0.5 62.1±20.4 61.3±20.1
ELECTRA
BART 84.1±2.0 83.5±1.5 93.5±0.9 93.7±1.2 91.7±0.3 91.8±0.3 65.4±1.9 64.9±2.3
Table7: AverageTestperformancewithstandarddeviationonfoursmalldatasetswithfourdifferent
pre-trainedmodels. Foreachsetting,thebetternumbersareboldedandareinblueiftheimprovement
isstatisticallysignificant.
moredata. BARTisasequence-to-sequencemodeltrainedasadenoisingautoencoder. ELECTRAis
aBERT-likemodeltrainedtodistinguishtokensgeneratedbymaskedlanguagemodelfromtokens
drawnfromthenaturaldistribution. Together,theyrepresentadiverserangeofmodelingchoices
inpre-training,includingdifferentmodelarchitectures,objectives,data,andtrainingstrategies. We
useADAMwithdebiasingtofine-tunethesemodelsonRTE,MRPC,STS-B,andCOLA,usingthe
hyperparametersthatareeitherdescribedinthepaperorintheofficialrepositoryofeachmodel.
Table6summarizesthehyper-parametersofeachmodelforeachdataset. Weusethehuggingface’s
Transformers library (Wolf et al., 2019). The experimental setup is kept the same as our other
experiments. Table 7 displays the average test performance on these datasets. We observe that
severalmodelssufferfromhighinstabilityonthesedatasetsandinmostcases,Re-initcanreducethe
performancevariance. Weobservethatforsomemodels,likeXLNet Large orRoBERTa Large ,Re-init
canimprovetheaverageperformanceandreducevariance. However,thebehaviorofRe-initvaries
significantlyacrossdifferentmodelsandRe-inithavelesssignificantimprovementforELECTRA
Large
andBART . Furtherstudyoftheentiremodelfamilyrequiressignificantcomputationalresources,
Large
andweleaveitasanimportantdirectionforfuturework.
| G SUPPLEMENTARY |     |     | MATERIAL | FOR SECTION |     | 6   |     |     |     |
| --------------- | --- | --- | -------- | ----------- | --- | --- | --- | --- | --- |
Figure14plotsthevalidationperformanceasafunctionofthenumberoftrainingiteration,using
thesamesettingasinFigure8. SimilartoourobservationsinFigure8,wefindthattraininglonger
generallyimprovesfine-tuningperformanceandreducesthegapbetweenstandardfine-tuningand
Re-init. OnMNLI,Re-initstilloutperformsstandardfine-tuning.
17

PublishedasaconferencepaperatICLR2021
|                | SST(1k) |                | QNLI(1k) |                | QQP(1k) |                    | MNLI(1k) |
| -------------- | ------- | -------------- | -------- | -------------- | ------- | ------------------ | -------- |
| ecnamrofrePlaV |         | ecnamrofrePlaV |          | ecnamrofrePlaV |         | ecnamrofrePlaV 0.7 |          |
0.82
0.90
|     |     | 0.80 |     |     |     | 0.6 |     |
| --- | --- | ---- | --- | --- | --- | --- | --- |
0.80
| 0.88 | Re-init2 |     | Re-init4 |     | Re-init3 |     | Re-init5 |
| ---- | -------- | --- | -------- | --- | -------- | --- | -------- |
|      | Standard |     | Standard |     | Standard | 0.5 | Standard |
0.75
0.78
96 200 400 800 16003200 96 200 400 800 16003200 96 200 400 800 16003200 96 200 400 800 16003200
TrainingIterations TrainingIterations TrainingIterations TrainingIterations
Figure 14: Mean (solid lines) and range (shaded region) of validation performance trained with
differentnumberofiterations,acrosseightrandomtrials.
| H EXPERIMENTAL |     | DETAILS | IN SECTION | 7   |     |     |     |
| -------------- | --- | ------- | ---------- | --- | --- | --- | --- |
Thehyperparametersearchspaceallocatedforeachmethodinourexperimentsis:
LayerwiseLearningRateDecay(LLRD) Wegridsearchtheinitiallearningratein{2×10−5,5×
10−5,1×10−4}andthelayerwisedecayratein{0.9,0.95}.
| Mixout | Wetunethemixoutprobabilityp∈{0.1,0.3,0.5,0.7,0.9}. |     |     |     |     |     |     |
| ------ | -------------------------------------------------- | --- | --- | --- | --- | --- | --- |
Weight decay toward the pre-trained weight We tune the regularization strength λ ∈
{10−3,10−2,10−1,100}.
| Weightdecay | Wetunetheregularizationstrengthλ∈{10−4,10−3,10−2,10−1}. |     |     |     |     |     |     |
| ----------- | ------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
18

PublishedasaconferencepaperatICLR2021
TransformerBlock1 TransformerBlock2 TransformerBlock3 TransformerBlock4
| noitazilaitinIot.tsiD2L |                    | noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     |
| ----------------------- | ------------------ | ----------------------- | --- | ----------------------- | --- | ----------------------- | --- |
| 0.8                     |                    | 0.8                     |     | 0.8                     |     | 0.8                     |     |
| 0.6                     |                    | 0.6                     |     | 0.6                     |     | 0.6                     |     |
| 0.4                     |                    | 0.4                     |     | 0.4                     |     | 0.4                     |     |
|                         | Standard Re-init6  |                         |     |                         |     |                         |     |
| 0.2                     | Re-init1 Re-init10 | 0.2                     |     | 0.2                     |     | 0.2                     |     |
Re-init3
| 0.0 |     | 0.0 |     | 0.0 |     | 0.0 |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
0 50 100 150 200 250 0 50 100 150 200 250 0 50 100 150 200 250 0 50 100 150 200 250
|     | Steps |     | Steps |     | Steps |     | Steps |
| --- | ----- | --- | ----- | --- | ----- | --- | ----- |
TransformerBlock5 TransformerBlock6 TransformerBlock7 TransformerBlock8
| noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     |
| ----------------------- | --- | ----------------------- | --- | ----------------------- | --- | ----------------------- | --- |
| 0.8                     |     | 0.8                     |     | 0.8                     |     | 0.8                     |     |
| 0.6                     |     | 0.6                     |     | 0.6                     |     | 0.6                     |     |
| 0.4                     |     | 0.4                     |     | 0.4                     |     | 0.4                     |     |
| 0.2                     |     | 0.2                     |     | 0.2                     |     | 0.2                     |     |
| 0.0                     |     | 0.0                     |     | 0.0                     |     | 0.0                     |     |
0 50 100 150 200 250 0 50 100 150 200 250 0 50 100 150 200 250 0 50 100 150 200 250
|     | Steps |     | Steps |     | Steps |     | Steps |
| --- | ----- | --- | ----- | --- | ----- | --- | ----- |
TransformerBlock9 TransformerBlock10 TransformerBlock11 TransformerBlock12
| noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     |
| ----------------------- | --- | ----------------------- | --- | ----------------------- | --- | ----------------------- | --- |
| 0.8                     |     | 0.8                     |     | 0.8                     |     | 0.8                     |     |
| 0.6                     |     | 0.6                     |     | 0.6                     |     | 0.6                     |     |
| 0.4                     |     | 0.4                     |     | 0.4                     |     | 0.4                     |     |
| 0.2                     |     | 0.2                     |     | 0.2                     |     | 0.2                     |     |
| 0.0                     |     | 0.0                     |     | 0.0                     |     | 0.0                     |     |
0 50 100 150 200 250 0 50 100 150 200 250 0 50 100 150 200 250 0 50 100 150 200 250
|     | Steps |     | Steps |     | Steps |     | Steps |
| --- | ----- | --- | ----- | --- | ----- | --- | ----- |
TransformerBlock13 TransformerBlock14 TransformerBlock15 TransformerBlock16
| noitazilaitinIot.tsiD2L 0.8 |     | noitazilaitinIot.tsiD2L 0.8 |     | noitazilaitinIot.tsiD2L 0.8 |     | noitazilaitinIot.tsiD2L 0.8 |     |
| --------------------------- | --- | --------------------------- | --- | --------------------------- | --- | --------------------------- | --- |
| 0.6                         |     | 0.6                         |     | 0.6                         |     | 0.6                         |     |
| 0.4                         |     | 0.4                         |     | 0.4                         |     | 0.4                         |     |
| 0.2                         |     | 0.2                         |     | 0.2                         |     | 0.2                         |     |
| 0.0                         |     | 0.0                         |     | 0.0                         |     | 0.0                         |     |
0 50 100 150 200 250 0 50 100 150 200 250 0 50 100 150 200 250 0 50 100 150 200 250
|     | Steps |     | Steps |     | Steps |     | Steps |
| --- | ----- | --- | ----- | --- | ----- | --- | ----- |
TransformerBlock17 TransformerBlock18 TransformerBlock19 TransformerBlock20
| noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     |
| ----------------------- | --- | ----------------------- | --- | ----------------------- | --- | ----------------------- | --- |
| 0.8                     |     | 0.8                     |     | 0.8                     |     | 0.8                     |     |
| 0.6                     |     | 0.6                     |     | 0.6                     |     | 0.6                     |     |
| 0.4                     |     | 0.4                     |     | 0.4                     |     | 0.4                     |     |
| 0.2                     |     | 0.2                     |     | 0.2                     |     | 0.2                     |     |
| 0.0                     |     | 0.0                     |     | 0.0                     |     | 0.0                     |     |
0 50 100 150 200 250 0 50 100 150 200 250 0 50 100 150 200 250 0 50 100 150 200 250
|     | Steps |     | Steps |     | Steps |     | Steps |
| --- | ----- | --- | ----- | --- | ----- | --- | ----- |
TransformerBlock21 TransformerBlock22 TransformerBlock23 TransformerBlock24
| noitazilaitinIot.tsiD2L 0.8 |     | noitazilaitinIot.tsiD2L 0.8 |     | noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     |
| --------------------------- | --- | --------------------------- | --- | ----------------------- | --- | ----------------------- | --- |
0.8
0.8
| 0.6 |     | 0.6 |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
0.6
0.6
| 0.4 |     | 0.4 |     | 0.4 |     | 0.4 |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.2 |     | 0.2 |     | 0.2 |     | 0.2 |     |
| 0.0 |     | 0.0 |     | 0.0 |     | 0.0 |     |
0 50 100 150 200 250 0 50 100 150 200 250 0 50 100 150 200 250 0 50 100 150 200 250
|     | Steps     |                                                          | Steps |     | Steps |     | Steps |
| --- | --------- | -------------------------------------------------------- | ----- | --- | ----- | --- | ----- |
|     | Figure15: | L2distancetotheinitializationduringfine-tuningBERTonRTE. |       |     |       |     |       |
19

PublishedasaconferencepaperatICLR2021
TransformerBlock1 TransformerBlock2 TransformerBlock3 TransformerBlock4
| noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     |
| ----------------------- | --- | ----------------------- | --- | ----------------------- | --- | ----------------------- | --- |
| 1.00                    |     | 1.00                    |     | 1.00                    |     | 1.00                    |     |
| 0.75                    |     | 0.75                    |     |                         |     |                         |     |
|                         |     |                         |     | 0.75                    |     | 0.75                    |     |
0.50
|      |                    | 0.50 |     | 0.50 |     | 0.50 |     |
| ---- | ------------------ | ---- | --- | ---- | --- | ---- | --- |
|      | Standard Re-init6  |      |     |      |     |      |     |
| 0.25 | Re-init1 Re-init10 | 0.25 |     | 0.25 |     | 0.25 |     |
Re-init3
| 0.00 |     | 0.00 |     | 0.00 |     | 0.00 |     |
| ---- | --- | ---- | --- | ---- | --- | ---- | --- |
0 74 148 222 296 370 0 74 148 222 296 370 0 74 148 222 296 370 0 74 148 222 296 370
|     | Steps |     | Steps |     | Steps |     | Steps |
| --- | ----- | --- | ----- | --- | ----- | --- | ----- |
TransformerBlock5 TransformerBlock6 TransformerBlock7 TransformerBlock8
| noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     |
| ----------------------- | --- | ----------------------- | --- | ----------------------- | --- | ----------------------- | --- |
| 1.00                    |     | 1.00                    |     | 1.00                    |     | 1.00                    |     |
| 0.75                    |     | 0.75                    |     | 0.75                    |     | 0.75                    |     |
| 0.50                    |     | 0.50                    |     | 0.50                    |     | 0.50                    |     |
| 0.25                    |     | 0.25                    |     | 0.25                    |     | 0.25                    |     |
| 0.00                    |     | 0.00                    |     | 0.00                    |     | 0.00                    |     |
0 74 148 222 296 370 0 74 148 222 296 370 0 74 148 222 296 370 0 74 148 222 296 370
|     | Steps |     | Steps |     | Steps |     | Steps |
| --- | ----- | --- | ----- | --- | ----- | --- | ----- |
TransformerBlock9 TransformerBlock10 TransformerBlock11 TransformerBlock12
| noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L 1.00 |     |
| ----------------------- | --- | ----------------------- | --- | ----------------------- | --- | ---------------------------- | --- |
| 1.00                    |     | 1.00                    |     | 1.00                    |     |                              |     |
0.75
| 0.75 |     | 0.75 |     | 0.75 |     |      |     |
| ---- | --- | ---- | --- | ---- | --- | ---- | --- |
| 0.50 |     | 0.50 |     | 0.50 |     | 0.50 |     |
| 0.25 |     | 0.25 |     | 0.25 |     | 0.25 |     |
| 0.00 |     | 0.00 |     | 0.00 |     | 0.00 |     |
0 74 148 222 296 370 0 74 148 222 296 370 0 74 148 222 296 370 0 74 148 222 296 370
|     | Steps |     | Steps |     | Steps |     | Steps |
| --- | ----- | --- | ----- | --- | ----- | --- | ----- |
TransformerBlock13 TransformerBlock14 TransformerBlock15 TransformerBlock16
| noitazilaitinIot.tsiD2L 1.00 |     | noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     |
| ---------------------------- | --- | ----------------------- | --- | ----------------------- | --- | ----------------------- | --- |
|                              |     | 1.00                    |     | 1.00                    |     | 1.00                    |     |
| 0.75                         |     | 0.75                    |     | 0.75                    |     | 0.75                    |     |
| 0.50                         |     | 0.50                    |     | 0.50                    |     | 0.50                    |     |
| 0.25                         |     | 0.25                    |     | 0.25                    |     | 0.25                    |     |
| 0.00                         |     | 0.00                    |     | 0.00                    |     | 0.00                    |     |
0 74 148 222 296 370 0 74 148 222 296 370 0 74 148 222 296 370 0 74 148 222 296 370
|     | Steps |     | Steps |     | Steps |     | Steps |
| --- | ----- | --- | ----- | --- | ----- | --- | ----- |
TransformerBlock17 TransformerBlock18 TransformerBlock19 TransformerBlock20
| noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     |
| ----------------------- | --- | ----------------------- | --- | ----------------------- | --- | ----------------------- | --- |
| 1.00                    |     | 1.00                    |     |                         |     |                         |     |
0.75
| 0.75 |     | 0.75 |     | 0.75 |     |      |     |
| ---- | --- | ---- | --- | ---- | --- | ---- | --- |
| 0.50 |     | 0.50 |     | 0.50 |     | 0.50 |     |
|      |     |      |     | 0.25 |     | 0.25 |     |
| 0.25 |     | 0.25 |     |      |     |      |     |
| 0.00 |     | 0.00 |     | 0.00 |     | 0.00 |     |
0 74 148 222 296 370 0 74 148 222 296 370 0 74 148 222 296 370 0 74 148 222 296 370
|     | Steps |     | Steps |     | Steps |     | Steps |
| --- | ----- | --- | ----- | --- | ----- | --- | ----- |
TransformerBlock21 TransformerBlock22 TransformerBlock23 TransformerBlock24
| noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L 1.00 |     |
| ----------------------- | --- | ----------------------- | --- | ----------------------- | --- | ---------------------------- | --- |
0.8
| 0.75 |     |     |     | 0.75 |     |     |     |
| ---- | --- | --- | --- | ---- | --- | --- | --- |
0.75
0.6
| 0.50 |     |     |     | 0.50 |     |      |     |
| ---- | --- | --- | --- | ---- | --- | ---- | --- |
|      |     | 0.4 |     |      |     | 0.50 |     |
| 0.25 |     | 0.2 |     | 0.25 |     | 0.25 |     |
| 0.00 |     | 0.0 |     | 0.00 |     | 0.00 |     |
0 74 148 222 296 370 0 74 148 222 296 370 0 74 148 222 296 370 0 74 148 222 296 370
|     | Steps |     | Steps |     | Steps |     | Steps |
| --- | ----- | --- | ----- | --- | ----- | --- | ----- |
L2distancetotheinitializationduringfine-tuningBERTonMRPC.
Figure16:
20

PublishedasaconferencepaperatICLR2021
TransformerBlock1 TransformerBlock2 TransformerBlock3 TransformerBlock4
| noitazilaitinIot.tsiD2L |                    | noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     |
| ----------------------- | ------------------ | ----------------------- | --- | ----------------------- | --- | ----------------------- | --- |
| 1.0                     |                    | 1.0                     |     | 1.0                     |     | 1.0                     |     |
| 0.5                     |                    | 0.5                     |     | 0.5                     |     | 0.5                     |     |
|                         | Standard Re-init6  |                         |     |                         |     |                         |     |
|                         | Re-init1 Re-init10 |                         |     |                         |     |                         |     |
Re-init3
| 0.0 |     | 0.0 |     | 0.0 |     | 0.0 |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
0 110 220 330 440 550 0 110 220 330 440 550 0 110 220 330 440 550 0 110 220 330 440 550
|     | Steps |     | Steps |     | Steps |     | Steps |
| --- | ----- | --- | ----- | --- | ----- | --- | ----- |
TransformerBlock5 TransformerBlock6 TransformerBlock7 TransformerBlock8
| noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     |
| ----------------------- | --- | ----------------------- | --- | ----------------------- | --- | ----------------------- | --- |
| 1.0                     |     | 1.0                     |     | 1.0                     |     | 1.0                     |     |
| 0.5                     |     | 0.5                     |     | 0.5                     |     | 0.5                     |     |
| 0.0                     |     | 0.0                     |     | 0.0                     |     | 0.0                     |     |
0 110 220 330 440 550 0 110 220 330 440 550 0 110 220 330 440 550 0 110 220 330 440 550
|     | Steps |     | Steps |     | Steps |     | Steps |
| --- | ----- | --- | ----- | --- | ----- | --- | ----- |
TransformerBlock9 TransformerBlock10 TransformerBlock11 TransformerBlock12
| noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     |
| ----------------------- | --- | ----------------------- | --- | ----------------------- | --- | ----------------------- | --- |
| 1.0                     |     | 1.0                     |     | 1.0                     |     | 1.0                     |     |
| 0.5                     |     | 0.5                     |     | 0.5                     |     | 0.5                     |     |
| 0.0                     |     | 0.0                     |     | 0.0                     |     | 0.0                     |     |
0 110 220 330 440 550 0 110 220 330 440 550 0 110 220 330 440 550 0 110 220 330 440 550
|     | Steps |     | Steps |     | Steps |     | Steps |
| --- | ----- | --- | ----- | --- | ----- | --- | ----- |
TransformerBlock13 TransformerBlock14 TransformerBlock15 TransformerBlock16
| noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     |
| ----------------------- | --- | ----------------------- | --- | ----------------------- | --- | ----------------------- | --- |
|                         |     |                         |     | 1.00                    |     | 1.00                    |     |
| 1.0                     |     | 1.0                     |     |                         |     |                         |     |
|                         |     |                         |     | 0.75                    |     | 0.75                    |     |
| 0.5                     |     | 0.5                     |     | 0.50                    |     | 0.50                    |     |
|                         |     |                         |     | 0.25                    |     | 0.25                    |     |
| 0.0                     |     | 0.0                     |     | 0.00                    |     | 0.00                    |     |
0 110 220 330 440 550 0 110 220 330 440 550 0 110 220 330 440 550 0 110 220 330 440 550
|     | Steps |     | Steps |     | Steps |     | Steps |
| --- | ----- | --- | ----- | --- | ----- | --- | ----- |
TransformerBlock17 TransformerBlock18 TransformerBlock19 TransformerBlock20
| noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     |
| ----------------------- | --- | ----------------------- | --- | ----------------------- | --- | ----------------------- | --- |
|                         |     | 1.00                    |     | 1.00                    |     | 1.00                    |     |
1.00
| 0.75 |     | 0.75 |     | 0.75 |     | 0.75 |     |
| ---- | --- | ---- | --- | ---- | --- | ---- | --- |
| 0.50 |     | 0.50 |     | 0.50 |     | 0.50 |     |
| 0.25 |     | 0.25 |     | 0.25 |     | 0.25 |     |
| 0.00 |     | 0.00 |     | 0.00 |     | 0.00 |     |
0 110 220 330 440 550 0 110 220 330 440 550 0 110 220 330 440 550 0 110 220 330 440 550
|     | Steps |     | Steps |     | Steps |     | Steps |
| --- | ----- | --- | ----- | --- | ----- | --- | ----- |
TransformerBlock21 TransformerBlock22 TransformerBlock23 TransformerBlock24
| noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     |
| ----------------------- | --- | ----------------------- | --- | ----------------------- | --- | ----------------------- | --- |
| 1.00                    |     | 1.00                    |     |                         |     |                         |     |
1.00
1.0
| 0.75 |     | 0.75 |     | 0.75 |     |     |     |
| ---- | --- | ---- | --- | ---- | --- | --- | --- |
| 0.50 |     | 0.50 |     | 0.50 |     |     |     |
0.5
| 0.25 |     | 0.25 |     | 0.25 |     |     |     |
| ---- | --- | ---- | --- | ---- | --- | --- | --- |
| 0.00 |     | 0.00 |     | 0.00 |     | 0.0 |     |
0 110 220 330 440 550 0 110 220 330 440 550 0 110 220 330 440 550 0 110 220 330 440 550
|     | Steps |     | Steps |     | Steps |     | Steps |
| --- | ----- | --- | ----- | --- | ----- | --- | ----- |
L2distancetotheinitializationduringfine-tuningBERTonSTS-B.
Figure17:
21

PublishedasaconferencepaperatICLR2021
TransformerBlock1 TransformerBlock2 TransformerBlock3 TransformerBlock4
| noitazilaitinIot.tsiD2L |                    | noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     |
| ----------------------- | ------------------ | ----------------------- | --- | ----------------------- | --- | ----------------------- | --- |
| 1.5                     |                    | 1.5                     |     | 1.5                     |     | 1.5                     |     |
| 1.0                     |                    | 1.0                     |     | 1.0                     |     | 1.0                     |     |
| 0.5                     | Standard Re-init6  | 0.5                     |     | 0.5                     |     | 0.5                     |     |
|                         | Re-init1 Re-init10 |                         |     |                         |     |                         |     |
Re-init3
| 0.0 |     | 0.0 |     | 0.0 |     | 0.0 |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
0 164 328 492 656 820 0 164 328 492 656 820 0 164 328 492 656 820 0 164 328 492 656 820
|     | Steps |     | Steps |     | Steps |     | Steps |
| --- | ----- | --- | ----- | --- | ----- | --- | ----- |
TransformerBlock5 TransformerBlock6 TransformerBlock7 TransformerBlock8
| noitazilaitinIot.tsiD2L 1.5 |     | noitazilaitinIot.tsiD2L 1.5 |     | noitazilaitinIot.tsiD2L 1.5 |     | noitazilaitinIot.tsiD2L 1.5 |     |
| --------------------------- | --- | --------------------------- | --- | --------------------------- | --- | --------------------------- | --- |
| 1.0                         |     | 1.0                         |     | 1.0                         |     |                             |     |
1.0
| 0.5 |     | 0.5 |     | 0.5 |     | 0.5 |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.0 |     | 0.0 |     | 0.0 |     | 0.0 |     |
0 164 328 492 656 820 0 164 328 492 656 820 0 164 328 492 656 820 0 164 328 492 656 820
|     | Steps |     | Steps |     | Steps |     | Steps |
| --- | ----- | --- | ----- | --- | ----- | --- | ----- |
TransformerBlock9 TransformerBlock10 TransformerBlock11 TransformerBlock12
| noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     |
| ----------------------- | --- | ----------------------- | --- | ----------------------- | --- | ----------------------- | --- |
| 1.5                     |     | 1.5                     |     | 1.5                     |     | 1.5                     |     |
| 1.0                     |     | 1.0                     |     | 1.0                     |     | 1.0                     |     |
| 0.5                     |     | 0.5                     |     | 0.5                     |     | 0.5                     |     |
| 0.0                     |     | 0.0                     |     | 0.0                     |     | 0.0                     |     |
0 164 328 492 656 820 0 164 328 492 656 820 0 164 328 492 656 820 0 164 328 492 656 820
|     | Steps |     | Steps |     | Steps |     | Steps |
| --- | ----- | --- | ----- | --- | ----- | --- | ----- |
TransformerBlock13 TransformerBlock14 TransformerBlock15 TransformerBlock16
| noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     |
| ----------------------- | --- | ----------------------- | --- | ----------------------- | --- | ----------------------- | --- |
1.0
|     |     | 1.0 |     | 1.0 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
1.0
0.5
| 0.5 |     | 0.5 |     | 0.5 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.0 |     | 0.0 |     | 0.0 |     | 0.0 |     |
0 164 328 492 656 820 0 164 328 492 656 820 0 164 328 492 656 820 0 164 328 492 656 820
|     | Steps |     | Steps |     | Steps |     | Steps |
| --- | ----- | --- | ----- | --- | ----- | --- | ----- |
TransformerBlock17 TransformerBlock18 TransformerBlock19 TransformerBlock20
| noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L |     |
| ----------------------- | --- | ----------------------- | --- | ----------------------- | --- | ----------------------- | --- |
|                         |     |                         |     | 1.00                    |     | 1.00                    |     |
| 1.0                     |     | 1.0                     |     |                         |     |                         |     |
|                         |     |                         |     | 0.75                    |     | 0.75                    |     |
|                         |     | 0.5                     |     | 0.50                    |     | 0.50                    |     |
0.5
|     |     |     |     | 0.25 |     | 0.25 |     |
| --- | --- | --- | --- | ---- | --- | ---- | --- |
| 0.0 |     | 0.0 |     | 0.00 |     | 0.00 |     |
0 164 328 492 656 820 0 164 328 492 656 820 0 164 328 492 656 820 0 164 328 492 656 820
|     | Steps |     | Steps |     | Steps |     | Steps |
| --- | ----- | --- | ----- | --- | ----- | --- | ----- |
TransformerBlock21 TransformerBlock22 TransformerBlock23 TransformerBlock24
| noitazilaitinIot.tsiD2L |     | noitazilaitinIot.tsiD2L 1.00 |     | noitazilaitinIot.tsiD2L 1.00 |     | noitazilaitinIot.tsiD2L |     |
| ----------------------- | --- | ---------------------------- | --- | ---------------------------- | --- | ----------------------- | --- |
| 1.00                    |     |                              |     |                              |     | 1.00                    |     |
| 0.75                    |     | 0.75                         |     | 0.75                         |     | 0.75                    |     |
| 0.50                    |     | 0.50                         |     | 0.50                         |     | 0.50                    |     |
| 0.25                    |     | 0.25                         |     | 0.25                         |     | 0.25                    |     |
| 0.00                    |     | 0.00                         |     | 0.00                         |     | 0.00                    |     |
0 164 328 492 656 820 0 164 328 492 656 820 0 164 328 492 656 820 0 164 328 492 656 820
|     | Steps |     | Steps |     | Steps |     | Steps |
| --- | ----- | --- | ----- | --- | ----- | --- | ----- |
L2distancetotheinitializationduringfine-tuningBERTonCoLA.
Figure18:
22