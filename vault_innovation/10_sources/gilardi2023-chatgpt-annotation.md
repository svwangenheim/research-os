BRIEFREPORT POLITICALSCIENCES OPENACCESS
ChatGPT outperforms crowd workers for text-annotation tasks
FabrizioGilardia,1ID,MeysamAlizadehaID,andMaëlKubliaID
EditedbyMaryWaters,HarvardUniversity,Cambridge,MA;receivedMarch27,2023;acceptedJune2,2023
ManyNLPapplicationsrequiremanualtextannotationsforavarietyoftasks,notably
totrainclassifiersorevaluatetheperformanceofunsupervisedmodels.Dependingon
the size and degree of complexity, the tasks may be conducted by crowd workers on
platforms such as MTurk as well as trained annotators, such as research assistants.
Using four samples of tweets and news articles (n = 6,183), we show that ChatGPT
outperforms crowd workers for several annotation tasks, including relevance, stance,
topics, and frame detection. Across the four datasets, the zero-shot accuracy of
ChatGPT exceeds that of crowd workers by about 25 percentage points on average,
while ChatGPT’s intercoder agreement exceeds that of both crowd workers and
trained annotators for all tasks. Moreover, the per-annotation cost of ChatGPT is
lessthan$0.003—aboutthirtytimescheaperthanMTurk.Theseresultsdemonstrate
the potential of large language models to drastically increase the efficiency of text
classification.
ChatGPT|textclassification|largelanguagemodels|humanannotations|textasdata
ManyNLPapplicationsrequirehigh-qualitylabeleddata,notablytotrainclassifiersor
evaluatetheperformanceofunsupervisedmodels.Forexample,researchersoftenaimto
filternoisysocialmediadataforrelevance,assigntextstodifferenttopicsorconceptual
categories,ormeasuretheirsentimentorstance.Regardlessofthespecificapproachused
forthesetasks(supervised,semisupervised,orunsupervised),labeleddataareneededto
buildatrainingsetoragoldstandardagainstwhichperformancecanbeassessed.Such
datamaybeavailableforhigh-leveltaskssuchassemanticevaluation(1).Moretypically,
however,researchershavetoconductoriginalannotationstoensurethatthelabelsmatch
theirconceptualcategories(2).Untilrecently,twomainstrategieswereavailable.First,
researchers can recruit and train coders, such as research assistants. Second, they can
relyoncrowdworkersonplatformssuchasAmazonMechanicalTurk(MTurk).Often,
thesetwostrategiesareusedincombination:trainedannotatorscreatearelativelysmall
goldstandarddataset,andcrowdworkersareemployedtoincreasethevolumeoflabeled
data.Trainedannotatorstendtoproducehigh-qualitydatabutinvolvesignificantcosts.
Crowd workers are a much cheaper and more flexible option, but the quality may be
insufficient,particularlyforcomplextasksandlanguagesotherthanEnglish.Moreover,
there have been concerns that MTurk data quality has decreased (3), while alternative
platformssuchasCrowdFlowerandFigureEightarenolongerpracticableoptionsfor
academic research since they were acquired by Appen, a company that is focused on a
businessmarket.
This paper explores the potential of large language models (LLMs) for text-
annotation tasks, with a focus on ChatGPT, which was released in November 2022.
Itdemonstratesthatzero-shotChatGPTclassifications(thatis,withoutanyadditional
training) outperform MTurk annotations at a fraction of the cost. LLMs have been
shown to perform very well for a wide range of purposes, including ideological scaling
(4),theclassificationoflegislativeproposals(5),theresolutionofcognitivepsychology Author affiliations: aDepartment of Political Science,
UniversityofZurich,Zurich8050,Switzerland
tasks (6), and the simulation of human samples for survey research (7). While a few
studies suggested that ChatGPT might perform text-annotation tasks of the kinds we
havedescribed(8,9), ourworkprovidesasystematicevaluation.Ouranalysisrelieson
Author contributions: F.G., M.A., and M.K. designed
asampleof6,183documents,includingtweetsandnewsarticlesthatwecollectedfora research;performedresearch;analyzeddata;andwrote
previousstudy(10)aswellasanewsampleoftweetspostedin2023.Inourpreviousstudy, thepaper.
thetextswerelabeledbytrainedannotators(researchassistants)forfivedifferenttasks: Theauthorsdeclarenocompetinginterest.
relevance,stance,topics,andtwokindsofframedetection.Usingthesamecodebooks Copyright © 2023 the Author(s). Published by PNAS.
This open access article is distributed under Creative
thatwedevelopedtoinstructourresearchassistants,wesubmittedthetaskstoChatGPT CommonsAttributionLicense4.0(CCBY).
as zero-shot classifications, as well as to crowd workers on MTurk. We then evaluated 1Towhomcorrespondencemaybeaddressed.Email:
theperformanceofChatGPTagainsttwobenchmarks:i)itsaccuracy,relativetothatof gilardi@ipz.uzh.ch.
crowdworkers,andii)itsintercoderagreement,relativetothatofcrowdworkersaswell This article contains supporting information online at
https://www.pnas.org/lookup/suppl/doi:10.1073/pnas.
asofourtrainedannotators.Wefindthatacrossthefourdatasets,ChatGPT’szero-shot 2305016120/-/DCSupplemental.
accuracyishigherthanthatofMTurkformosttasks.Foralltasks,ChatGPT’sintercoder PublishedJuly18,2023.
PNAS 2023 Vol.120 No.30 e2305016120 https://doi.org/10.1073/pnas.2305016120 1of3
.69.87.431.49
sserdda
PI
morf
6202
,22
lirpA
no
69.87.431.49
yb
gro.sanp.www//:sptth
morf
dedaolnwoD

| A                    |                      | B                           |                      |     |     |     |
| -------------------- | -------------------- | --------------------------- | -------------------- | --- | --- | --- |
|   Tweets (2020−2021) |                      |   News Articles (2020−2021) |                      |     |     |     |
| Accuracy             | Intercoder Agreement | Accuracy                    | Intercoder Agreement |     |     |     |
Relevance
Relevance
Stance
Topics
Frames I
Frames I
Frames II
| 0% 25% 50% 75%100%0% | 25% 50% 75%100%      | 0% 25% 50% 75%100%0% | 25% 50% 75%100%      |                |           |                 |
| -------------------- | -------------------- | -------------------- | -------------------- | -------------- | --------- | --------------- |
| C                    |                      | D                    |                      |                |           |                 |
|   Tweets (2023)      |                      |   Tweets (2017−2022) |                      |                |           |                 |
| Accuracy             | Intercoder Agreement | Accuracy             | Intercoder Agreement |                |           |                 |
|                      |                      |                      |                      | Fig.1. ChatGPT | zero-shot | text annotation |
Relevance Relevance performance in four datasets (A: tweets, 2020-
|     |     |     |     | 2021; B: news | articles, 2020-2021; | C: tweets, |
| --- | --- | --- | --- | ------------- | -------------------- | ---------- |
2023;D:tweets,2017-2022),comparedtoMTurk
|          |           |     |     | and trained | annotators. ChatGPT’s | accuracy        |
| -------- | --------- | --- | --- | ----------- | --------------------- | --------------- |
| Frames I | Frames II |     |     |             |                       |                 |
|          |           |     |     | outperforms | that of MTurk         | for most tasks. |
|          |           |     |     | ChatGPT’s   | intercoder agreement  | outperforms     |
0% 25% 50% 75%100%0% 25% 50% 75%100% 0% 25% 50% 75%100%0% 25% 50% 75%100% that of both MTurk and trained annotators in
|     |     |     |     | all tasks. Accuracy | means agreement | with the |
| --- | --- | --- | --- | ------------------- | --------------- | -------- |
Trained annotators MTurk ChatGPT (temp 1) ChatGPT (temp 0.2) trainedannotators.
agreementexceedsthatofbothMTurkandtrainedannotators. Across the four datasets, we report ChatGPT’s zero-shot
Moreover, ChatGPT is significantly cheaper than MTurk. performance for two different metrics: accuracy and intercoder
ChatGPT’s per-annotation cost is about $0.003 or a third of agreement (Fig. 1). Accuracy is measured as the percentage
a cent—about thirty times cheaper than MTurk, with higher of correct annotations (using our trained annotators as a
quality.Atthiscost,itmightpotentiallybepossibletoannotate benchmark), while intercoder agreement is computed as the
entire samples or to create large training sets for supervised percentage of tweets that were assigned the same label by
learning. While further research is needed to better understand two different annotators (research assistant, crowd workers, or
how ChatGPT and other LLMs perform in a broader range of ChatGPTruns).Regardingaccuracy,Fig.1showsthatChatGPT
contexts, these results demonstrate their potential to transform outperforms MTurk for most tasks across the four datasets.
howresearchersconductdataannotationsandtodisruptpartsof On average, ChatGPT’s accuracy exceeds that of MTurk by
thebusinessmodelofplatformssuchasMTurk. about25percentagepoints.Moreover,ChatGPTdemonstrates
|     |     |     | adequate accuracy | overall, considering | the challenging | tasks, |
| --- | --- | --- | ----------------- | -------------------- | --------------- | ------ |
.69.87.431.49 sserdda PI morf 6202 ,22 lirpA no 69.87.431.49 yb gro.sanp.www//:sptth morf dedaolnwoD
numberofclasses,andzero-shotannotations.Accuracyratesfor
Results
relevancetasks,withtwoclasses(relevant/irrelevant)are70%for
We use four datasets (n = 6,183) including tweets and news content moderation tweets, 81% for content moderation news
articlesthatwecollectedandannotatedmanuallyforaprevious
articles,83%forUSCongresstweets,and59%for2023content
studyonthediscoursearoundcontentmoderation(10),aswellas moderation tweets. In the 2023 sample, ChatGPT performed
anewsampleoftweetspostedin2023toaddresstheconcernthat much better than MTurk in the second task but struggled
ChatGPTmightberelyingonmemorizationfortextspotentially withmisclassifyingtweetsaboutspecificusersuspensionsinthe
included in the model’s training dataset. We relied on trained relevance task due to a lack of examples in the prompt. While
annotators (research assistants) to construct a gold standard for thesefindingsdonotsuggestthatmemorizationisamajorissue,
six conceptual categories: relevance of tweets for the content theyunderscoretheimportanceofhigh-qualityprompts.
moderation issue (relevant/irrelevant); relevance of tweets for Regardingintercoderagreement,Fig.1showsthatChatGPT’s
political issues (relevant/irrelevant); stance regarding Section performance is very high. On average, intercoder agreement is
230,akeypartofUSinternetlegislation(keep/repeal/neutral); about 56% for MTurk, 79% for trained annotators, 91% for
topic identification (six classes); a first set of frames (content ChatGPT with temperature = 1, and 97% for ChatGPT with
moderationasaproblem,asasolution,orneutral);andasecond
temperature=0.2.Thecorrelationbetweenintercoderagreement
set of frames (fourteen classes). We then performed these exact andaccuracyispositive(Pearson’sr=0.36).Thissuggeststhata
same classifications with ChatGPT and with crowd workers lowertemperaturevaluemaybepreferableforannotationtasks,
recruited on MTurk, using the same codebook we developed asitseemstoincreaseconsistencywithoutdecreasingaccuracy.
for our research assistants (SI Appendix, S1). For ChatGPT, WeunderscorethatthetesttowhichwesubjectedChatGPT
we conducted four sets of annotations. To explore the effect of is hard. Our tasks were originally conducted in the context of
ChatGPT’stemperatureparameter,whichcontrolsthedegreeof a previous study (10) and required considerable resources. We
randomnessoftheoutput,weconductedtheannotationswiththe developed most of the conceptual categories for our particular
defaultvalueof1aswellaswithavalueof0.2,whichimpliesless research purposes. Moreover, some of the tasks involve a
randomness.Foreachtemperaturevalue,weconductedtwosets large number of classes and exhibit lower levels of intercoder
ofannotationstocomputeChatGPT’sintercoderagreement.For agreement, which indicates a higher degree of annotation
MTurk,weaimedtoselecthigh-qualitycrowdworkers,notably
difficulty(11).ChatGPT’saccuracyispositivelycorrelatedwith
byfilteringforworkerswhoareclassifiedas“MTurkMasters”by the intercoder agreement of trained annotators (Pearson’s r =
Amazon, who have an approval rate of over 90%, and who are 0.46),suggestingbetterperformanceforeasiertasks.Conversely,
locatedintheUnitedStates.Ourproceduresaredescribedmore ChatGPT’s outperformance of MTurk is negatively correlated
indetailinMaterialsandMethods. with the intercoder agreement of trained annotators (Pearson’s
| 2of 3 https://doi.org/10.1073/pnas.2305016120 |     |     |     |     |     | pnas.org |
| --------------------------------------------- | --- | --- | --- | --- | --- | -------- |

r = -0.37), potentially indicating stronger overperformance for textofinstructionforthefiveannotationtasksispresentedinSIAppendix,S1.
morecomplextasks. WeusedtheexactsamewordingsforChatGPTandMTurk.
| We conclude |     | that ChatGPT’s |     | performance |     | is  | impressive, |     |     |     |     |     |     |
| ----------- | --- | -------------- | --- | ----------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
particularlyconsideringthatitsannotationsarezero-shot. TrainedAnnotators.Wetrainedthreepoliticalsciencestudentstoconduct
theannotationtasks.Foreachtask,theyweregiventhesamesetofinstructions
describedaboveanddetailedinSIAppendix,S1.Thecodersannotatedthe
Discussion
tweetsindependentlytaskbytask.
| This paper | demonstrates |     | the potential |     | of LLMs | to  | transform |     |     |     |     |     |     |
| ---------- | ------------ | --- | ------------- | --- | ------- | --- | --------- | --- | --- | --- | --- | --- | --- |
text-annotationproceduresforavarietyoftaskscommontomany
|     |     |     |     |     |     |     |     | CrowdWorkers.We | employed | MTurk | workers to | perform | the same set of |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | -------- | ----- | ---------- | ------- | --------------- |
researchprojects.Theevidenceisconsistentacrossdifferenttypes tasksastrainedannotatorsandChatGPT,usingthesamesetofinstructions
oftextsandtimeperiods.ItstronglysuggeststhatChatGPTmay (SIAppendix,S1).Toensureannotationquality,werestrictedaccesstothetasks
already be a superior approach compared to crowd annotations toworkers whoareclassifiedas “MTurkMasters”byAmazon, whohavean
on platforms such as MTurk. At the very least, the findings HIT(HumanIntelligenceTask)approvalrategreaterthan90%withatleast50
demonstrate the importance of studying the text-annotation approvedHITs,andwhoarelocatedintheUnitedStates.Moreover,weensured
propertiesandcapabilitiesofLLMsmoreindepth.Thefollowing thatnoworkercouldannotatemorethan20%ofthetweetsforagiventask.As
withthetrainedhumanannotators,eachtweetwasannotatedbytwodifferent
| questions | seem | particularly | promising: |     | i) performance |     | across |     |     |     |     |     |     |
| --------- | ---- | ------------ | ---------- | --- | -------------- | --- | ------ | --- | --- | --- | --- | --- | --- |
crowdworkers.
multiplelanguages;ii)implementationoffew-shotlearning;iii)
| construction | of  | semiautomated |     | data | labeling | systems | in which |     |     |     |     |     |     |
| ------------ | --- | ------------- | --- | ---- | -------- | ------- | -------- | --- | --- | --- | --- | --- | --- |
amodellearnsfromhumanannotationsandthenrecommends ChatGPT.WeusedtheChatGPTAPIwiththe“gpt-3.5-turbo”.Theannotations
labelingprocedures(12);iv)usingchainofthoughtprompting were conducted between March 9–20 and April 27–May 4, 2023. For each
|           |            |     |          |     |             |     |           | task, we prompted | ChatGPT with | the corresponding |     | annotation | instruction |
| --------- | ---------- | --- | -------- | --- | ----------- | --- | --------- | ----------------- | ------------ | ----------------- | --- | ---------- | ----------- |
| and other | strategies | to  | increase | the | performance | of  | zero-shot |                   |              |                   |     |            |             |
text(SIAppendix,S1).WeintentionallyavoidedaddinganyChatGPT-specific
reasoning(13);andv)comparisonacrossdifferenttypesofLLMs.
promptstoensurecomparabilitybetweenChatGPTandMTurkcrowdworkers.
|     |     |     |     |     |     |     |     | After testing | several variations, | we decided | to feed | tweets | one by one to |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------------------- | ---------- | ------- | ------ | ------------- |
MaterialsandMethods ChatGPTusingthefollowingprompt:“Here’sthetweetIpicked,pleaselabel
|     |     |     |     |     |     |     |     | it as [Task Specific | Instruction | (e.g., ‘one | of the topics | in the | instruction’)].” |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | ----------- | ----------- | ------------- | ------ | ---------------- |
Datasets.Theanalysisreliesonfourdatasets:i)arandomsampleof2,382
tweetsdrawnfromadatasetof2.6milliontweetsoncontentmoderationposted We set the temperature parameter at 1 (default value) and 0.2 (which
makestheoutputmoredeterministic;highervaluesmaketheoutputmore
fromJanuary2020toApril2021;ii)arandomsampleof1,856tweetsposted
|     |     |     |     |     |     |     |     | random). For | each temperature | setting, | we collected | two | responses from |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ---------------- | -------- | ------------ | --- | -------------- |
bymembersoftheUSCongressfrom2017to2022,drawnfromadatasetof
|     |     |     |     |     |     |     |     | ChatGPT to | compute the intercoder | agreement. |     | That is, we | collected four |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---------------------- | ---------- | --- | ----------- | -------------- |
20milliontweets;iii)arandomsampleof1,606articlesnewspaperarticleson
ChatGPTresponsesforeachtweet.Wecreatedanewchatsessionforevery
contentmoderationpublishedfromJanuary2020toApril2021,drawnfroma
tweettoensurethattheChatGPTresultsarenotinfluencedbythehistoryof
datasetof980karticlescollectedviaLexisNexis.Thesamplesizewasdetermined
annotations.
bythenumberoftextsneededtobuildatrainingsetforamachinelearning
.69.87.431.49 sserdda PI morf 6202 ,22 lirpA no 69.87.431.49 yb gro.sanp.www//:sptth morf dedaolnwoD classifier.Thefourthdatasetiv)replicatedthedatacollectionfor(i),butfor
January2023.Itincludesarandomsampleof500tweets(ofwhich339werein EvaluationMetrics.First,wecomputedaverageaccuracy(i.e.,percentageof
English)drawnfromadatasetof1.3milliontweets. correctpredictions),thatis,thenumberofcorrectlyclassifiedinstancesoverthe
totalnumberofcasestobeclassified,usingtrainedhumanannotationsasour
goldstandardandconsideringonlytextsthatbothannotatorsagreedupon.
AnnotationTasks.Weimplementedseveralannotationtasks:1)relevance:
Second,intercoderagreementreferstothepercentageofinstancesforwhich
| whether a | tweet is | about content | moderation |     | or, in | a separate | task, about |     |     |     |     |     |     |
| --------- | -------- | ------------- | ---------- | --- | ------ | ---------- | ----------- | --- | --- | --- | --- | --- | --- |
bothannotatorsinagivengroupreportthesameclass.
politics;2)topicdetection:whetheratweetisaboutasetofsixpredefinedtopics
(i.e.,Section230,TrumpBan,Complaint,PlatformPolicies,TwitterSupport,
Data,Materials,andSoftwareAvailability.Replicationmaterialsareavail-
| and others); | 3) stance | detection: | whether | a   | tweet is | in favor of, | against, or |             |                    |                                    |     |     |       |
| ------------ | --------- | ---------- | ------- | --- | -------- | ------------ | ----------- | ----------- | ------------------ | ---------------------------------- | --- | --- | ----- |
|              |           |            |         |     |          |              |             | able at the | Harvard Dataverse, | https://doi.org/10.7910/DVN/PQYF6M |     |     | (15). |
neutralaboutrepealingSection230(apieceofUSlegislationcentraltocontent
|     |     |     |     |     |     |     |     | Some study | data are available | (only tweet | IDs can | be shared, | not tweets |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------------------ | ----------- | ------- | ---------- | ---------- |
moderation);4)generalframedetection:whetheratweetcontainsasetoftwo
themselves).
opposingframes(“problem”and“solution”).Thesolutionframedescribestweets
|     |     |     |     |     |     |     |     |     | This project | received | funding | from | the European |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | -------- | ------- | ---- | ------------ |
framingcontentmoderationasasolutiontootherissues(e.g.,hatespeech).The ACKNOWLEDGMENTS.
problemframedescribestweetsframingcontentmoderationasaproblemon ResearchCouncil(ERC)undertheEuropeanUnion’sHorizon2020researchand
itsownaswellastootherissues(e.g.,freespeech);5)policyframedetection: innovationprogram(grantagreementno.883121).WethankFabioMelliger,
whetheratweetcontainsasetoffourteenpolicyframesproposed(14).Thefull PaulaMoser,andSophievanIJzendoornforexcellentresearchassistance.
1. G.Emersonetal.,Proceedingsofthe16thInternationalWorkshoponSemantic 9. F.Huang,H.Kwak,J.An,IschatGPTbetterthanhumanannotators?Potentialandlimitationsof
Evaluation(SemEval-2022)(AssociationforComputationalLinguistics,Seattle, chatGPTinexplainingimplicithatespeech.arXiv[Preprint](2023).http://arxiv.org/abs/2302.
| 2022). |     |     |     |     |     |     |     | 07736(Accessed13March2023). |     |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | --- | --- |
2. K.Benoit,D.Conway,B.E.Lauderdale,M.Laver,S.Mikhaylov,Crowd-sourcedtextanalysis: 10. M.Alizadehetal.,Contentmoderationasapoliticalissue:TheTwitterdiscoursearoundtrump’s
Reproducibleandagileproductionofpoliticaldata.Am.Polit.Sci.Rev.116,278–295 ban.J.Quant.Des.:DigitalMedia2,1–44(2022).
(2016). 11. P.S.Bayerl,K.I.Paul,Whatdeterminesinter-coderagreementinmanualannotations?Ameta-
3. M.Chmielewski,S.C.Kucker,AnMTurkcrisis?Shiftsindataqualityandtheimpactonstudyresults analyticinvestigationComput.Linguist.37,699–725(2011).
Soc.Psychol.PersonalitySci.11,464–473(2020). 12. M.Desmond,E.Duesterwald,K.Brimijoin,M.Brachman,Q.Pan,Semi-automateddatalabeling,in
4. P.Y.Wu,J.A.Tucker,J.Nagler,S.Messing,LargeLanguageModelsCanBeUsedtoEstimatethe NeurIPS2020CompetitionandDemonstrationTrack,(PMLR,2021),pp.156–169.
IdeologiesofPoliticiansinaZero-ShotLearningSetting(2023). 13. T.Kojima,S.S.Gu,M.Reid,Y.Matsuo,Y.Iwasawa,Largelanguagemodelsarezero-shotreasoners.
5. J.J.Nay,LargeLanguageModelsasCorporateLobbyists(2023). arXiv[Preprint](2022).http://arxiv.org/abs/2205.11916(Accessed13March2023).
6. M.Binz,E.Schulz,UsingcognitivepsychologytounderstandGPT-3.Proc.Natl.Acad.Sci.U.S.A. 14. D.Card,A.Boydstun,J.H.Gross,P.Resnik,N.A.Smith,“Themediaframescorpus:Annotations
120,e2218523120(2023). offramesacrossissues”inProceedingsofthe53rdAnnualMeetingoftheAssociationfor
7. L.P.Argyleetal.,Outofone,many:Usinglanguagemodelstosimulatehumansamples.Polit. ComputationalLinguisticsandthe7thInternationalJointConferenceonNaturalLanguage
Anal.1–15(2023). Processing(Volume2:ShortPapers)(2015),pp.438–444.
8. T.Kuzman,I.Mozeticˇ,N.Ljubešic´,ChatGPT:Beginningofanendofmanuallinguisticdata 15. F.Gilardi,M.Alizadeh,M.Kubli,ReplicationDatafor:ChatGPToutperformscrowd-workersfortext-
annotation?Usecaseofautomaticgenreidentification.arXiveprints(2023).http://arxiv.org/ annotationtasks.HarvardDataverse.https://doi.org/10.7910/DVN/PQYF6M.Deposited16June
| abs/2303.03953(Accessed13March2023). |     |     |     |     |     |     |     | 2023. |     |     |     |     |     |
| ------------------------------------ | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
PNAS 2023 Vol.120 No.30 e2305016120 https://doi.org/10.1073/pnas.2305016120 3of 3