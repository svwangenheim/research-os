Supercharging Agenda Setting Research:
The ParlaCAP Dataset of 28 European Parliaments
and a Scalable Multilingual LLM-Based Classification
Taja Kuzman Pungeršek∗, Peter Rupnik∗, Daniela Širinic´§, Nikola Ljubešic´∗†‡
∗JožefStefanInstitute;†FacultyofComputerandInformationScience,UniversityofLjubljana;
‡InstituteofContemporaryHistory;§FacultyofPoliticalScience,UniversityofZagreb
∗†‡Ljubljana,Slovenia;§Zagreb,Croatia
{taja.kuzman,peter.rupnik,nikola.ljubesic}@ijs.si;§dsirinic@fpzg.hr
Abstract
ThispaperintroducesParlaCAP,alarge-scaledatasetforanalyzingparliamentaryagendasettingacrossEurope,
andproposesacost-effectivemethodforbuildingdomain-specificpolicytopicclassifiers. ApplyingtheComparative
AgendasProject(CAP)schematothemultilingualParlaMintcorpusofover8millionspeechesfrom28parliaments
ofEuropeancountriesandautonomousregions,wefollowateacher-studentframeworkinwhichahigh-performing
largelanguagemodel(LLM)annotatesin-domaintrainingdataandamultilingualencodermodelisfine-tunedon
theseannotationsforscalabledataannotation. Weshowthatthisapproachproducesaclassifiertailoredtothe
targetdomain. AgreementbetweentheLLMandhumanannotatorsiscomparabletointer-annotatoragreement
amonghumans,andtheresultingmodeloutperformsexistingCAPclassifierstrainedonmanually-annotatedbut
out-of-domaindata. InadditiontotheCAPannotations,theParlaCAPdatasetoffersrichspeakerandpartymetadata,
aswellassentimentpredictionscomingfromtheParlaSentmultilingualtransformermodel,enablingcomparative
research on political attention and representation across countries. We illustrate the analytical potential of the
datasetwiththreeusecases,examiningthedistributionofparliamentaryattentionacrosspolicytopics,sentiment
patternsinparliamentaryspeech,andgenderdifferencesinpolicyattention.
Keywords:parliamentary dataset, European parliaments, topic classification, policy topics, comparative
agendasproject
1. Introduction parliamentary agendas. New methods in natural
languageprocessingandmachinelearning,partic-
Parliaments are at the heart of democratic gov- ularlytransformer-basedlanguagemodels,makeit
ernance, serving as places where elected repre- possibletoautomaticallyanalyzelargecollections
sentativessetpoliticalprioritiesanddiscusspolicy of political texts in different languages and coun-
issues. Understandingwhatparliamentarianstalk tries (Sebo˝k et al., 2024). These developments
aboutandhowtheyallocatetheirattentionacross offernewpossibilitiesforunderstandingparliamen-
different policy areas provides valuable insights tarydebatesatamuchlargerscaleandatamuch
into how democracy works in practice. However, lowercostthanwaspreviouslypossible. However,
studyingparliamentarydebateagendashasbeen significant challenges remain. Current datasets
challenging,particularlywhenresearcherswantto often cover only limited time periods and a small
comparemultiplecountriesacrossextendedtime numberofcountries.
periods(Sebo˝ketal.,2023). Our project, ParlaCAP, aims to address these
The Comparative Agendas Project (CAP) has limitations by building on the ParlaMint corpus
been particularly influential in addressing these collection (Erjavec et al., 2024b), the result of a
challenges,developingsystematicwaystotrackpo- CLARIN ERIC flagship project, which provides
liticalattentionacrossdifferentpolicytopics(Baum- transcriptsofparliamentarydebatesfrom29coun-
gartner et al., 2019). CAP provides a coherent triesandautonomousregionsacrossEurope.1 We
frameworkfortrackingmediaandgovernmentat- apply CAP’s policy topic labels to this corpus us-
tentiontoawiderangeofpolicyissues,enabling ingnewmultilingualnaturallanguageprocessing
researchers,students,policy-makers,andjournal- methods. Our method combines the latest large
iststoexaminepolicy-makingtrendsovertimeand languagemodelsforannotatingtrainingdatasets,
between countries. However, this research has which are then used for fine-tuning smaller mul-
traditionallyrequiredextensivemanualworktoan- tilingual encoder models to process millions of
alyzepoliticaltexts,limitingthescopeandscaleof
comparativestudies. 1More information on the ParlaCAP project and its
Recentadvancesincomputer-assistedtextanal- classifiers,datasetsandtutorialsisavailableathttps:
ysisarebeginningtotransformthewaywestudy //clarinsi.github.io/parlacap/.
6202
beF
81
]LC.sc[
1v61561.2062:viXra

speeches,whilemaintainingthequalityofhuman sourcedfromtheCAPwebsite2 andadditionalin-
analysis,followingtheLLMteacher-studentframe- ternalcollectionsofmembersoftheCAPnetwork
work (Kuzman and Ljubešic´, 2025). The result- (Baumgartneretal.,2019). Theyreporthighper-
ing ParlaCAP dataset (Ljubešic´ et al., 2025) is formance,withweightedmacro-F1scoresranging
developed by integrating CAP topic coding with from 0.62 to 0.96, depending on the specific do-
sentimentanalysis(Mochtaketal.,2024)anden- main and language. However, for our use case,
riching the data with metadata from PartyFacts we assume that fine-tuning a model specifically
(DöringandRegel,2019)andV-DEM(Coppedge on ParlaMint data is more effective for the auto-
et al., 2025) databases, with the aim to create a matic annotation of these corpora than using ex-
comprehensiveresourceforstudyingdemocratic istingmodelsfine-tunedonfewerlanguagesand
politicsacrossEuropeanparliaments. Thispaper differentdomains. Weevaluatethishypothesisin
| shows how | enhanced |     | text-analysis | approaches |     | Section3.7. |     |     |     |     |     |     |
| --------- | -------- | --- | ------------- | ---------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
andtechniquescantransformover8millionparlia- Recent advances in large language models
mentaryspeechesinmorethan20languagesinto
|            |      |          |                 |     |           | (LLMs) | have enabled |     | alternative | approaches |     | to  |
| ---------- | ---- | -------- | --------------- | --- | --------- | ------ | ------------ | --- | ----------- | ---------- | --- | --- |
| structured | data | suitable | for comparative |     | political |        |              |     |             |            |     |     |
textclassificationthatreducerelianceonmanually-
| research. |     |     |     |     |     | annotateddata. |     | KuzmanandLjubešic´ |     |     | (2025)intro- |     |
| --------- | --- | --- | --- | --- | --- | -------------- | --- | ------------------ | --- | --- | ------------ | --- |
duceanLLMteacher-studentframeworkinwhicha
state-of-the-artdecoder-onlyLLMservesasadata
|     | 2.  | Related | Work |     |     |                                      |     |     |     |     |          |     |
| --- | --- | ------- | ---- | --- | --- | ------------------------------------ | --- | --- | --- | --- | -------- | --- |
|     |     |         |      |     |     | annotatorfornewstopicclassification. |     |     |     |     | Whenpro- |     |
videdwithdetailedlabeldescriptions,theLLMpro-
ducesannotationscomparabletothoseofhuman
Sebo˝ketal.(2023)provideanoverviewoffreely
availableEuropeanlegislativetextdatasetsused coders. BecauseLLMsarecomputationallyexpen-
sivetodeployatscale,theirroleislimitedtoanno-
forlarge-scalecomparativestudiesandtextanal-
ysis. Mostrelevantdatasetsoriginatefromafew tatingtrainingdata,whilesmallerpretrainedBERT-
large international projects: ParlSpeech (Rauh like student models, such as the XLM-RoBERTa
model(Conneauetal.,2020),arefine-tunedonthe
| and Schwalbach, |     | 2020), | the Comparative |     | Agen- |     |     |     |     |     |     |     |
| --------------- | --- | ------ | --------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
dasProject(CAP;Baumgartneretal.,2019),and LLM-annotatedcorpus. TheLLM-annotatedtrain-
ingdataareshowntosupportstrongdownstream
| ParlaMint | (Erjavec | et al., | 2022, | 2024b). | Among |     |     |     |     |     |     |     |
| --------- | -------- | ------- | ----- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- |
these, the ParlaMint project provides the broad- performanceofthefine-tunedmodel. Similarly,Ryt-
estcoverageofparliamentaryspeechesinEurope tingetal.(2023)evaluateLLMsasannotatorsfor
|     |     |     |     |     |     | social science | datasets. |     | Using | two | English | CAP |
| --- | --- | --- | --- | --- | --- | -------------- | --------- | --- | ----- | --- | ------- | --- |
(deJongetal.,2022).
CertaindatasetsinsidetheParlaMintcollection datasets, they find that LLM annotations match
humanperformanceand,insomecases,exceed
havealreadybeenenrichedwithpolicytopiclabels.
inter-annotatoragreementamonghumancoders.
Forexample,Navarrettaetal.(2024)appliedpolicy
Theyfurtherdemonstratethemodels’applicability
labelsadaptedfromtheCAPschematotheDan-
beyondCAPtopiccoding,includingtasksrelated
| ish ParlaMint |     | corpus (ParlaMint-DK), |     | part | of the |     |     |     |     |     |     |     |
| ------------- | --- | ---------------------- | --- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- |
ParlaMint 4.1 release. The annotation combined to partisan stereotypes and populism. Building
onthislineofwork,thepresentstudyappliesthe
| manual | labeling | of agenda | titles | with | automatic |     |     |     |     |     |     |     |
| ------ | -------- | --------- | ------ | ---- | --------- | --- | --- | --- | --- | --- | --- | --- |
teacher-studentLLMframeworktodeveloppolicy
| propagation | of                               | these labels | to all | corresponding |     |                      |     |        |     |           |     |       |
| ----------- | -------------------------------- | ------------ | ------ | ------------- | --- | -------------------- | --- | ------ | --- | --------- | --- | ----- |
|             |                                  |              |        |               |     | topic classification |     | models |     | using the | CAP | label |
| speeches.   | However,thisapproachcannotbeeas- |              |        |               |     |                      |     |        |     |           |     |       |
schema.
ilyextendedtoallotherParlaMintcorpora,asitre-
| quiresmanualannotation. |     |     | Additionally,itisbased |     |     |     |     |     |     |     |     |     |
| ----------------------- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
oninformativeagendatitleswhicharenotavailable
| in all ParlaMint |     | datasets. | This underscores |     | the |     |             |     |     |         |        |     |
| ---------------- | --- | --------- | ---------------- | --- | --- | --- | ----------- | --- | --- | ------- | ------ | --- |
|                  |     |           |                  |     |     | 3.  | Development |     | of  | the CAP | Policy |     |
needforautomatedmethodsoftopicclassification
|     |     |     |     |     |     |     |     | Topic | Classifier |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ---------- | --- | --- | --- |
usingCAPlabelstoenablescalableannotationof
speechesacrossalllanguagesandcorporainside
theParlaMintcollection. In this section, we describe the development of
|     |     |     |     |     |     | a fine-tuned | multilingual |     | BERT-like |     | transformer |     |
| --- | --- | --- | --- | --- | --- | ------------ | ------------ | --- | --------- | --- | ----------- | --- |
Acommonapproachtoautomatictopicclassifi-
|     |     |     |     |     |     | model that | is specialized |     | for | the classification |     | of  |
| --- | --- | --- | --- | --- | --- | ---------- | -------------- | --- | --- | ------------------ | --- | --- |
cationinvolvesfine-tuningdeepneuraltransformer-
basedmodels,suchaspretrainedBERT-likemod- CAP major labels in parliamentary speeches in
ParlaMintcorpora(Erjavecetal.,2024b)byfollow-
| els, on manually-annotated                |       |             | data.  | For | topic clas- |                     |                     |     |     |          |         |     |
| ----------------------------------------- | ----- | ----------- | ------ | --- | ----------- | ------------------- | ------------------- | --- | --- | -------- | ------- | --- |
|                                           |       |             |        |     |             | ing the             | LLM teacher-student |     |     | paradigm | (Kuzman |     |
| sification                                | using | CAP labels, | Sebo˝k | et  | al. (2024)  |                     |                     |     |     |          |         |     |
| introducetheCAPBabelMachine,anopen-source |       |             |        |     |             | andLjubešic´,2025). |                     |     |     |          |         |     |
systemforclassifyingtextsinto21CAPpolicytop-
| ics across | nine | languages. | The system |     | is based |     |     |     |     |     |     |     |
| ---------- | ---- | ---------- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
on the XLM-RoBERTa models (Conneau et al., 2https://www.comparativeagendas.net/
2020),fine-tunedonmanually-annotateddatasets datasets_codebooks

Dataset Lang #Instances #Labels %MostandLeastFrequentLabel
ParlaCAP-test-EN EN 876 22 6.4%(LawandCrime),2.1%(Culture)
ParlaCAP-test-HR HR 869 22 8.5%(GovernmentOperations),1.7%(Im-
migration)
ParlaCAP-test-SR SR 874 22 7.1%(GovernmentOperations),1.7%(Im-
migration)
ParlaCAP-test-BS BS 824 22 10.4%(Other),0.5%(Culture)
Table1: InformationontestdatasetsinEnglish(EN),Croatian(HR),Serbian(SR),andBosnian(BS)
languages,manuallyannotatedwithCAPlabels.
3.1. CAP Labels 8.3). Prediction through the OpenAI API batch
optioncostapproximately$100. Thesuitabilityof
TofollowthetraditionoftheComparativeAgendas
usinganLLMasadataannotatorisevaluatedin
Project, weusethe21majorCAPtopicsasthey
Section3.3.
aredefinedintheCAPMasterCodebook(Bevan,
An analysis of the resulting training data re-
2019).3 An inspection of the ParlaMint corpora
vealedasevereunderrepresentationofthePublic
revealed that some speeches do not address a
Lands category, which appeared only in around
policytopic,forexample,whenspeakersdiscuss
hundred training instances. To address this, we
meeting logistics, share personal stories, or en-
implementatargeteddataaugmentationpipeline
gage in arguments. To account for these cases,
inspired by the LLM-based “finding a needle in a
weintroducedanadditionallabel,Other. Thus,the
haystack” approach (Mochtak and Meijers, In re-
finallabelsetcomprises22categories. Thelabel
view). We define a list of keywords associated
descriptionsprovidedtothelargelanguagemodel
with the Public Lands category based on its defi-
andannotators(seeSection8.1inappendix)were
nition(e.g.,“nationalpark”,“forestfire”,“grazing”).
developedfromthelistofsubtopicsandtheirde-
SincetheParlaMintcorporahavebeenmachine-
scriptionsintheMasterCodebook,andwerefur-
translatedintoEnglish,wecanidentifyspeeches
therextendedusingtheCroatianCAPguidelines
containingspecifickeywordsacrossallParlaMint
(Širinic´ andCˇakar,2019)andexpertinput.
languages by searching for them in the English
ParlaMint.en-ana (Kuzman et al., 2024) corpus
3.2. LLM-Annotated Training Data available through the CLARIN.SI concordancer.
With this approach, we extract up to 2,000 ran-
Tospecializethemodelforclassificationofparlia-
dom candidate instances per keyword across all
mentary speeches in ParlaMint corpora (Erjavec
ParlaMintcorpora. UsingtheGPT-4omodelwith
et al., 2022), the training dataset is constructed
thesamepromptasfortheannotationofthetrain-
from all corpora in the ParlaMint 4.1 corpus col-
ingdata,weannotatethecandidatespeechesand
lection (Erjavec et al., 2024a). ParlaMint 4.1 is
identify779asbelongingtothePublicLands cate-
a collection of comparable corpora that contain
gory. Theseareaddedtothetrainingdata,increas-
transcriptionsofparliamentarydebatesof29Eu-
ingthetotalnumberofexamplesforthislabelfrom
ropeancountriesandautonomousregions,mostly
145to924.
covering the period from 2015 to mid-2022. The
The final training dataset (Kuzman Pungeršek
individual corpora comprise between 9 and 126
andLjubešic´,2026)consistsof35,579speeches.
millionwords,andthecompletecorpuscollection
Itincludesatrainingsplit(29,779instances–1,000
containsmorethan1.2billionwords.
percorpusandtheadditional779PublicLands in-
The development of the training data consists
stances)andadevelopmentsplit(5,800instances
of two steps: 1) preparation of suitable samples
– 200 per corpus), with stratification performed
ofspeechesfromeachParlaMintdataset,and2)
before augmenting the Public Lands label. The
automatic annotation of the training dataset with
datasetisfreelyaccessibleintheCLARIN.SIrepos-
a large language model. More specifically, we
itory4.
sample1,200instancespereachof29ParlaMint
corpora,resultinginadatasetof34,800speeches.
3.3. Manually-Annotated Test Data
AnnotationwithCAPlabelsisperformedautomati-
callyusingtheGPT-4omodel(OpenAI,2024),fol- We construct test datasets in four languages,
lowing the prompt and label description that are namely English, Croatian, Serbian, and Bosnian.
provided in the appendix (see Sections 8.1 and
4The training dataset can be downloaded from the
3https://www.comparativeagendas.net/ CLARIN.SI repository: http://hdl.handle.net/
pages/master-codebook 11356/2093.

thattheagreementbetweenthethreeannotators
rangesfrom0.59to0.68,whiletheagreementbe-
Ann3 tween annotators and the GPT-4o model ranges
from 0.60 to 0.64, as shown in Figure 1. The re-
0.68 0.64
sultsconfirmthattheLLMperformsasreliablyas
0.62
humanannotatorsonthistask,whichisconsistent
Ann1 0.63 GPT-4o
withfindingsfromsimilartopicclassificationtasks
0.59 0.60 (KuzmanandLjubešic´,2025),andsupportsitsuse
forannotatingthetrainingdata.
Ann2
In addition to serving for the evaluation of the
fine-tunedCAPclassificationmodels(seeSection
3.5), the test datasets can also be used to as-
sess the performance of large language models
Figure1: Theinter-annotatoragreementinterms
on this task. They have already been used in a
of nominal Krippendorff’s alpha between human
study that compared fine-tuned BERT-like mod-
annotators and the large language model (GPT-
els with various closed-source and open-source
4o).
largelanguagemodelsinazero-shotsetting(Kuz-
man Pungeršek et al., 2025). Accordingly, to
preserve the integrity of future evaluations, the
The test instances are extracted from the re-
datasets are not publicly released, as this would
spective ParlaMint 4.1 corpora (Erjavec et al.,
risktheirinclusioninLLMpretrainingorfine-tuning.
2024a), that is, ParlaMint-GB 4.1, ParlaMint-
Accesstothetestdatasetscanbegrantedupon
HR 4.1, ParlaMint-RS 4.1 and ParlaMint-BA 4.1.
requestfromthecorrespondingauthors.
From each corpus, we randomly sample 10,000
speeches, ensuring that none of them overlaps
3.4. Model Fine-Tuning
withthetrainingdataset. Thenweautomaticallyan-
notatethesamplewiththeGPT-4omodelusingthe
Toidentifythebestperformingmodelforourtask,
CAPlabelsfollowingthesamemethodologyasfor
weexperimentwithfine-tuningtwomultilingualpre-
annotatingthetrainingdataset. Tocreatealabel-
trained BERT-like models, namely, the large-size
balancedtestdataset,wesample40speechesper XLM-RoBERTamodel5 (Conneauetal.,2020)and
CAPlabelfromthe10,000speechesautomatically the XLM-R-Parla model6 (Ljubešic´ et al., 2023).
annotatedbytheLLM,resultingintestdatasetsof
The XLM-R-Parla model is based on the XLM-
approximately800–880instancesperlanguage.
RoBERTa-largearchitecture(Conneauetal.,2020)
Thetestdatasetsaremanuallyannotatedbyan and was further pretrained on 1.72 billion words
expertannotator. Thisannotatorwasselectedfrom from parliamentary proceedings in 30 European
agroupofthreeinitialannotatorswhoannotated languages,usingdatafromtheParlaMint3.0(Er-
asampleoftheCroatiantestdataset. Theanno- javec et al., 2023) and EuroParl (Koehn, 2011)
tator with the highest inter-annotator agreement corpora. Previousexperimentsonsentimentiden-
withtheothertwowaschosentoannotatethere- tificationshowedthatadditionalpretrainingonpar-
maining test datasets. The annotators had prior liamentary domain data improves performance
experiencewithnewstopicorpolicytopicannota- (Mochtaketal.,2024).
tion. Theyfollowedtheannotationguidelinesand Both models are fine-tuned on the initial Par-
labeldescriptions(seeSections8.1and8.2inthe laMint training split (29,000 instances) that was
appendix)andcompletedbrieftraining. Inaddition created before the augmentation with the Public
to the 21 CAP main labels and the label Other, Lands instances. The optimal hyperparameters
annotatorscouldassignthelabeldonotknow to were identified via a hyperparameter search per-
texts with unclear topics. These instances were formed on the development dataset. We use a
excludedfromthefinaltestdatasets. Table1pro- learningrateof1×10−5 and3epochs,andsave
videsdetailsonthesizeofeachtestdatasetand each model variant three times to enable signifi-
thedistributionofmanually-annotatedlabelswithin cancetesting.
them. The datasets are approximately balanced Initial experiments reveal low performance on
acrosslabels. the Public Lands category due to data sparsity.
Toevaluatetheannotatorperformanceandcom- We thus perform another experiment where we
pareitwiththeperformanceachievedbytheLLM fine-tune the XLM-R-Parla model on the training
onthistask,about400instancesoftheCroatian
testdatasetweremanuallyannotatedbythreehu- 5https://huggingface.co/
man annotators. The inter-annotator agreement xlm-roberta-large
is calculated using the Krippendorff’s alpha met- 6https://huggingface.co/classla/
ric (Krippendorff, 2018). The evaluation shows xlm-r-parla

dataset to which we have added additional in- 2025).7 The published model is based on the
stancesofthePublicLands (seeSection3.2),to- multilingualparliamentaryXLM-R-ParlaBERT-like
taling29,779instances. Weobserveasubstantial modelthatwasfine-tunedonLLM-annotatedPar-
improvement of the model’s performance on the laMint training data in 29 languages, extended
PublicLands label,withitsF1scoreonthislabel with additional Public Lands instances (29,779
increasingfrom0.30to0.80. speeches).
Fordownstreamapplications,8 werecommend
incorporating a confidence-based filtering mech-
3.5. Evaluation Results
anism to further improve the reliability of model
predictions. Specifically, to annotate the entire
TheresultspresentedinTable2demonstratethe
ParlaMint5.0corpuscollectionwiththeParlaCAP
effectiveness of domain-specific pretraining and
classifier,weapplyaconfidencethresholdof0.60
targeteddataaugmentationforclassificationtasks
andlabelanyinstancebelowthisthresholdasMix,
intheparliamentarydomain.
indicating that the model is uncertain about the
The XLM-R-Parla model, which is based on
dominantpolicytopic.
theXLM-RoBERTa-largearchitectureandfurther
Whenevaluatedonthetestdatasets,thisstrat-
pretrained on multilingual parliamentary corpora,
egy results in 9% of the instances being marked
slightly outperforms the baseline XLM-RoBERTa
asMix intheEnglishtestsetand11%intheother
modelonthreeoutoffourtestdatasets.
three test sets. Importantly, by excluding these
FurtherimprovementsareobservedwithXLM-
low-confidence predictions, the model achieves
R-Parlafine-tunedonextendedtrainingdatathat
strongperformanceontheremainingdata,ranging
incorporateadditionalLLM-annotatedPublicLands
from0.69ofmicro-F1,macro-F1andaccuracyin
instances. Itachievesmacro-F1scoresabove0.70
Bosnianto0.76inEnglish(seeTable3).
onEnglishandSerbian,andscoresbetween0.64
Thepublishedmodelachieveshighperformance
and 0.68 on Bosnian and Croatian test datasets,
on all labels, as shown in Figure 2 that presents
respectively. Thismodeloutperformstheoriginal
theperformanceontheEnglishtestdataset.
fine-tunedXLM-R-ParlaandXLM-RoBERTamod-
elsonalltestdatasets.
As shown in Table 2, the models perform the
worstontheBosniantestdataset. Amanualanal-
ysis of the dataset, together with feedback from
the annotator, indicates that this dataset is more
challengingduetolessstructureddebatesanda
higherfrequencyofvagueborderlinecasesinthe
Bosnianparliament. Notably,themostfrequentla-
belinthisdatasetisOther,whichcoverstopicsun-
relatedtopolicyagendas,suchaspersonalstories,
interjections,andexchangesbetweenmembers.
The best-performing fine-tuned XLM-R-Parla
model achieves performance comparable to the
muchlargerGPT-4omodel,whilebeingmorescal-
ableandcomputationallyefficient. Thishighlights
the effectiveness of the LLM teacher-student ap-
proachthatenabledthedevelopmentofascalable
domain-specific classifier by leveraging a larger
LLMasadataannotator. Moreover,thefine-tuned
modelachievesaperformancecomparabletothat
Figure 2: Performance of the ParlaCAP model
of human annotators. As shown in Figure 1, the
on the English test dataset after removal of Mix
levelofagreementbetweenthehumanannotators
instancespredictedwithlowconfidence.
issimilartotheiragreementwiththeLLMmodel,
andthebest-performingstudentBERT-likemodel
attainsperformancecomparabletothatoftheLLM.
7TheParlaCAPclassifierisavailableinHuggingFace
3.6. ParlaCAP Model athttps://www.doi.org/10.57967/hf/6684.
8The code for applying the ParlaCAP classi-
Wepublishthebest-performingfine-tunedmodelin fier to ParlaMint-style datasets is freely available
theHuggingFacerepositoryunderthenamePar- on GitHub at https://github.com/clarinsi/
laCAPclassifier(KuzmanPungeršekandLjubešic´, ParlaMint-Annotation-with-CAP-Topics.

| Model  |     | TrainingData |     | EN   |     | HR   |     | SR   | BS   |     |
| ------ | --- | ------------ | --- | ---- | --- | ---- | --- | ---- | ---- | --- |
| GPT-4o |     | -            |     | 0.74 |     | 0.68 |     | 0.72 | 0.63 |     |
XLM-R-Parla ParlaMint+PL 0.72±0.01 0.68±0.01 0.71±0.01 0.64±0.01
XLM-R-Parla ParlaMint 0.70±0.01 0.66±0.01 0.68±0.01 0.62±0.01
XLM-RoBERTa ParlaMint 0.68±0.01 0.65±0.01 0.67±0.01 0.63±0.01
Table2: Performanceoffine-tunedmodelsonEnglish(EN),Croatian(HR),Serbian(SR)andBosnian
(BS)testdataintermsofmacro-F1. Eachmodelwasfine-tunedandevaluatedthreetimes. Allmodels
were fine-tuned on the training data from the ParlaMint datasets (see Section 3.2). In one setting
(ParlaMint+PL), the training data were extended with additional instances of the Public Lands label.
PerformanceoftheGPT-4omodelisaddedasanupperthresholdasthemodelswerefine-tunedonthe
trainingdatathatwasannotatedbytheGPT-4omodel.
| Dataset | Micro-F1 |     | Macro-F1 | Accuracy |     |     | 4.  | The ParlaCAP | Dataset |     |
| ------- | -------- | --- | -------- | -------- | --- | --- | --- | ------------ | ------- | --- |
| EN      | 0.76     |     | 0.76     | 0.76     |     |     |     |              |         |     |
HR 0.72 0.73 0.72 TheParlaCAPclassifier,introducedinSection3.6,
SR 0.75 0.74 0.75 is applied to the ParlaMint 5.0 corpus collection
BS 0.69 0.68 0.69 (Erjavec et al., 2025), resulting in the ParlaCAP
dataset(Ljubešic´
|     |     |     |     |     |     |     |     | etal.,2025). | Thisdatasetbuilds |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ----------------- | --- |
Table3: PerformanceofthefinalpublishedParla- on the speeches and metadata provided in the
CAPpolicytopicclassifieronEnglish(EN),Croat- ParlaMintcorpora,andaddstopicandsentiment
ian(HR),Serbian(SR)andBosnian(BS)testdata labels,aswellasadditionalmetadata. Incontrast
intermsofmicro-F1,macro-F1andaccuracy. The totheParlaMintcorpora,whicharedistributedin
evaluationincludesonlyinstanceswithaprediction formats tailored to linguistic analyses, the Parla-
confidence score above 0.60, which account for CAP dataset is provided in a tabular format that
90%ofalltestinstances. followsthe“text-as-data”paradigmandisdesigned
tomeettheneedsofsocialscientists.
|     |     |     |     |     |     | The | ParlaCAP | dataset | comprises | 8 million |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------- | --------- | --------- |
speechesfrom28Europeannationalandregional
3.7. Comparison to Other CAP Models parliaments(seeFigure3),namely,Austrian(AT),
Bosnian(BA),Belgian(BE),Bulgarian(BG),Czech
We finally evaluate other publicly available mod- (CZ), Danish (DK), Estonian (EE), Spanish (ES),
elsfine-tunedtotheCAPschemabySebo˝ketal. Catalan(ES-CT),Galician(ES-GA),Basque(ES-
(2024), presented in Section 2.9 These models PV),French(FR),British(GB),Greek(GR),Croa-
arebasedonthelarge-sizedXLM-RoBERTapre- tian (HR), Hungarian (HU), Icelandic (IS), Italian
(IT),Latvian(LV),Dutch(NL),Norwegian(NO),Pol-
| trained | model | (Conneau | et al., | 2020) | and have |     |     |     |     |     |
| ------- | ----- | -------- | ------- | ----- | -------- | --- | --- | --- | --- | --- |
beenfine-tunedondifferentdomainsofmanually- ish(PL),Portuguese(PT),Serbian(RS),Swedish
annotatedCAPdatasetsinvariouslanguages. The (SE),Slovenian(SI),Turkish(TR),andUkrainian
(UA).Eachspeechisassignedasentimentlabel–
| models | use the | same | CAP major | labels | as our |     |     |     |     |     |
| ------ | ------- | ---- | --------- | ------ | ------ | --- | --- | --- | --- | --- |
models,andthecategoryNoPolicyContent which negative,neutral,orpositive–usingtheParlaSent
|     |     |     |     |     |     | classifier | for | sentiment analysis | in parliamentary |     |
| --- | --- | --- | --- | --- | --- | ---------- | --- | ------------------ | ---------------- | --- |
hasbeenmappedtoourcategoryOther.
|     |     |     |     |     |     | texts(Rupniketal.,2023,Mochtaketal.,2024). |     |     |     | In  |
| --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- |
SinceboththeParlaCAPmodelandotherevalu-
addition,eachspeechislabeledwithapolicytopic
atedmodelsarebasedonsimilarpretrainedmod-
accordingtotheCAPschema,usingtheParlaCAP
| els, the | performance |                | differences | shown   | in Table    |                                 |     |     |                |     |
| -------- | ----------- | -------------- | ----------- | ------- | ----------- | ------------------------------- | --- | --- | -------------- | --- |
|          |             |                |             |         |             | classifierpresentedinthispaper. |     |     | Thedatasetalso |     |
| 4 mainly | reflect     | the similarity |             | between | their fine- |                                 |     |     |                |     |
includesextensivemetadataonspeakers,political
| tuningdataandourtestdatasets. |     |     |     | Forourspecific |     |     |     |     |     |     |
| ----------------------------- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- |
parties,anddemocraticcontexts.
| objective | – enriching |     | the ParlaMint | datasets | with |     |     |     |     |     |
| --------- | ----------- | --- | ------------- | -------- | ---- | --- | --- | --- | --- | --- |
ThedatasetisfreelyavailableintheCROSSDA
topicinformation–wedemonstratethatfine-tuning
repository.10
Foreachparliament,itisdistributedin
| on data       | closely | aligned                     | with the | target | domain is |                         |     |                        |     |     |
| ------------- | ------- | --------------------------- | -------- | ------ | --------- | ----------------------- | --- | ---------------------- | --- | --- |
|               |         |                             |          |        |           | threetabular(TSV)files. |     | Thefirstfileisaspeech- |     |     |
| advantageous: |         | theParlaCAPmodeloutperforms |          |        |           |                         |     |                        |     |     |
levelTSVthatcontainsthefullspeechtext(along
modelsfine-tunedondatafromotherdomains.
withthetextmachine-translatedtoEnglish),theas-
signedtopiclabel,andtheaggregatedsentiment
label. ItalsoincludesrichmetadatafromParlaMint
9ThemodelsareavailableinHuggingFaceathttps:
//huggingface.co/collections/poltextlab/ 10TheParlaCAPdatasetisavailableathttps://doi.
| cap-babel-672b46e9d40b55aa6f55da3e. |     |     |     |     |     | org/10.23669/1ZTELP. |     |     |     |     |
| ----------------------------------- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- |

| Model                                |     |     |     | EN   | HR   |     | SR   |     | BS   |     |     |
| ------------------------------------ | --- | --- | --- | ---- | ---- | --- | ---- | --- | ---- | --- | --- |
| ParlaCAP                             |     |     |     | 0.72 | 0.69 |     | 0.71 |     | 0.65 |     |     |
| xlm-roberta-large-party-cap-v3       |     |     |     | 0.64 | 0.63 |     | 0.62 |     | 0.57 |     |     |
| xlm-roberta-large-parlspeech-cap-v3  |     |     |     | 0.64 | 0.57 |     | 0.60 |     | 0.55 |     |     |
| xlm-roberta-large-pooled-cap-v3      |     |     |     | 0.64 | 0.60 |     | 0.62 |     | 0.57 |     |     |
| xlm-roberta-large-execspeech-cap-v3  |     |     |     | 0.60 | 0.58 |     | 0.60 |     | 0.53 |     |     |
| xlm-roberta-large-execorder-cap-v3   |     |     |     | 0.60 | 0.59 |     | 0.58 |     | 0.51 |     |     |
| xlm-roberta-large-legislative-cap-v3 |     |     |     | 0.59 | 0.62 |     | 0.61 |     | 0.56 |     |     |
| xlm-roberta-large-media-cap-v3       |     |     |     | 0.57 | 0.56 |     | 0.58 |     | 0.49 |     |     |
| xlm-roberta-large-social-cap-v3      |     |     |     | 0.57 | 0.53 |     | 0.51 |     | 0.44 |     |     |
| xlm-roberta-large-budget-cap-v3      |     |     |     | 0.52 | 0.51 |     | 0.48 |     | 0.46 |     |     |
Table4: PerformanceoftheParlaCAPmodel,incomparisontotheperformanceofotherexistingfine-
tunedpolicytopicmodelsbySebo˝ketal.(2024). ThemodelsareevaluatedonEnglish(EN),Croatian
(HR),Serbian(SR)andBosnian(BS)testdataintermsofmacro-F1. Noconfidence-basedfilteringis
applied,i.e.,ParlaCAPpredictionsareevaluatedastheywereproduced.
|                |        |               |          |        |     |     | 5. Use | Cases |     |     |     |
| -------------- | ------ | ------------- | -------- | ------ | --- | --- | ------ | ----- | --- | --- | --- |
| (e.g. speaker, | party, | party status, | chairing | role), |     |     |        |       |     |     |     |
aswellasadditionalidentifierssuchastheParty-
TheParlaCAPdatasetopensnewpossibilitiesfor
FactsPartyID(DöringandRegel,2019)andthe
V-Dem Country ID (Coppedge et al., 2025). The studyingfundamentalquestionsindemocraticgov-
secondfileisaspeech-levelTSVwithoutspeech ernanceandpoliticalrepresentation. Weillustrate
text,whichreducesthefilesizebyapproximately the analytical potential of the ParlaCAP dataset
88%andfacilitatesmoreefficientquantitativeanal- with three examples: examining the distribution
ofparliamentaryattentionacrosspolicytopics,ex-
| yses. The | third file | is a sentence-level |     | TSV that |     |     |     |     |     |     |     |
| --------- | ---------- | ------------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
provides the speech ID, the sentiment label as- ploringsentimentpatternsinparliamentaryspeech,
signed to each sentence, and the sentence text. andshowinggenderdifferencesinpolicyattention.
Thisstructureallowsuserstoconductanalysesat For temporal consistency across parliaments,
boththespeechandsentencelevels, depending weincludeheredatafromyears2017–2022. We
ontheirresearchneeds.11
|     |     |     |     |     | include   | only speeches |          | given  | by members       |     | of par- |
| --- | --- | --- | --- | --- | --------- | ------------- | -------- | ------ | ---------------- | --- | ------- |
|     |     |     |     |     | liament   | and discard   | speeches |        | of chairpersons. |     |         |
|     |     |     |     |     | Speeches, | annotated     | with     | labels | Other            | and | Mix,    |
areomittedfromtheanalysis.
|     |     |     |     |     | 5.1. What | Do  | Parliamentarians |     |     | Talk |     |
| --- | --- | --- | --- | --- | --------- | --- | ---------------- | --- | --- | ---- | --- |
About?
|     |     |     |     |     | Figure | 4 presents | an  | illustrative | analysis |     | of the |
| --- | --- | --- | --- | --- | ------ | ---------- | --- | ------------ | -------- | --- | ------ |
ParlaCAPdataset,demonstratingtheresearchpo-
|     |     |     |     |     | tential of    | applying | the      | CAP topic | classification |     | to  |
| --- | --- | --- | --- | --- | ------------- | -------- | -------- | --------- | -------------- | --- | --- |
|     |     |     |     |     | parliamentary |          | speeches | across    | Europe.        | The | vi- |
sualizationshowsthedistributionofparliamentary
attentionacross21policytopics,withvaluesrep-
|     |     |     |     |     | resenting | the | percentage | of  | total parliamentary |     |     |
| --- | --- | --- | --- | --- | --------- | --- | ---------- | --- | ------------------- | --- | --- |
speechesdevotedtoeacharea(rangingfrom0.0
to0.25,or0%to25%).
Figure3: ScopeoftheParlaCAPdataset,showing Certainpolicyareas,Macroeconomics,Govern-
| the number | of speeches | in each | parliamentary |     |     |     |     |     |     |     |     |
| ---------- | ----------- | ------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
mentOperations,andHealth,areconsistentlyap-
datasetandtheirtemporalcoverage. pearingashigh-attentiontopicsacrossmostparlia-
|     |     |     |     |     | ments,reflectingsharedchallenges. |     |     |     |     | Otherareas, |     |
| --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- | --- | ----------- | --- |
suchasCulture,ForeignTrade,andPublicLands
|     |     |     |     |     | receive | relatively | limited | focus | across | countries. |     |
| --- | --- | --- | --- | --- | ------- | ---------- | ------- | ----- | ------ | ---------- | --- |
However,attentionintensityanddistributionvaries
| 11Tutorials | for analyzing | parliamentary |     | speeches |     |     |     |     |     |     |     |
| ----------- | ------------- | ------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
significantlyacrosscountries,withaparliamentary
| from multiple | European | countries | using | Python |     |     |     |     |     |     |     |
| ------------- | -------- | --------- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- |
focusrangingfromhighlyconcentrated(darkerred
| and R, | based on | the ParlaCAP | dataset, | are |     |     |     |     |     |     |     |
| ------ | -------- | ------------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
available at https://github.com/clarinsi/ patterns in Figure 4) to more dispersed engage-
ParlaCAP-Analysis-Tutorials. ment across topics. This variation demonstrates

that national political contexts, institutional struc- European parliaments use predominantly nega-
tures,anddomesticprioritiesshapetheparliamen- tive language across policy areas, as shown by
| taryagenda. |     |     |     | the widespread | blue | coloring. This finding | con- |
| ----------- | --- | --- | --- | -------------- | ---- | ---------------------- | ---- |
These patterns only point to deeper dynamics nects to recent research by Željko Poljak (2024),
of agenda competition and prioritization. When who showed that politicians frequently use nega-
corefunctionsofgovernment–suchasMacroeco- tive rhetoric because negative language attracts
nomics and Government Operations – dominate mediaattention. Accordingtohistheory,negative
parliamentarydebates,legislaturesappeartopur- storiesengageaudiencesmoreeffectively,creat-
sue a less diverse agenda, focusing the major- ing a cycle where politicians use more negativity
ity of their attention on fewer critical issues. This togetmoremediacoverage.
echoesbroaderfindingsfromJenningsetal.(2011) IfwelookatseparatetopicsinFigure5wesee
about executive agenda setting, where some is- severaldistinctpatterns. Culturereceivesthemost
sues prove to be “more equal than others” in the positivetreatmentacrosscountries,likelybecause
competitionforpoliticalattention. TopicslikeCul- cultural discussions tend to be celebratory and
|              |            |         |                | unifying. Law | and Crime | topics are consistently |     |
| ------------ | ---------- | ------- | -------------- | ------------- | --------- | ----------------------- | --- |
| ture, Public | Lands, and | Foreign | Trade might be |               |           |                         |     |
secondaryconcernsthatreceivefocusonlywhen themostnegative,whichmakessensegiventhese
urgentgovernancepressuresease. Thissuggests debates often emerge as a reaction on current
hierarchicalattentionallocation. Someissuesare problems,suchascriminalbehaviororpunishment
| permanentfixturesofparliamentarydebate,while |     |     |     | debates.      |               |            |         |
| -------------------------------------------- | --- | --- | --- | ------------- | ------------- | ---------- | ------- |
|                                              |     |     |     | Great Britain | is noticeably | different, | showing |
othersareallowedtoappearontheflooronlywhen
politicalspaceallows. However,morerigorousem- morepositivesentimentacrossmosttopicscom-
piricaltestsarerequiredtovalidatethesedescrip- pared to other European countries. This might
tiveobservations. reflectuniqueaspectsofBritishparliamentarycul-
tureordifferentmediadynamicsthatdonotreward
negativityasstrongly.
| Figure 4: | Probability | distribution | of automatically |     |     |     |     |
| --------- | ----------- | ------------ | ---------------- | --- | --- | --- | --- |
annotatedCAPlabelsforeachparliamentincluded
intheParlaCAPdataset.
|     |     |     |     | Figure5: MeansentimentacrossCAPtopics,senti- |          |                    |        |
| --- | --- | --- | --- | -------------------------------------------- | -------- | ------------------ | ------ |
|     |     |     |     | mentrangingfrom0(negative)to5(positive).     |          |                    | Red    |
|     |     |     |     | denotes more                                 | positive | sentiment and blue | repre- |
sentingmorenegativesentimenttowardsthetopic.
| 5.2. How | Do Parliamentarians |     | Talk? |     |     |     |     |
| -------- | ------------------- | --- | ----- | --- | --- | --- | --- |
TheParlaCAPdatasetallowsustostudynotjust
whatpoliticianstalkabout,buthowtheytalkabout
|            |               |                |        | 5.3. Do   | Men and Women | Talk about |     |
| ---------- | ------------- | -------------- | ------ | --------- | ------------- | ---------- | --- |
| it. It has | been enhanced | with sentiment | analy- |           |               |            |     |
|            |               |                |        | Different | Issues?       |            |     |
sis,revealingtheemotionaltoneofparliamentary
debatesacrossdifferentpolicytopicsin28Euro- Figure 6 demonstrates another dimension of the
pean countries. In Figure 5 the colors represent analyticalrichnessoftheParlaCAPdatasetbyin-
sentiment scores from 1.2 to 3.2, where darker corporating speaker gender metadata from Par-
blueindicatesmorenegativelanguageandlighter laMint. The visualization shows the difference
colorsshowmorepositivetone. in topic attention between female and male par-
Theanalysisrevealsseveralclearpatterns. Most liamentarians, with red indicating topics where

womenspeakproportionallymoreandblueshow- inparliamentarytextsbasedontheComparative
ingareaswheremendominatethedebate. AgendasProject(CAP)schema. Theclassifieris
TheresultsinFigure6alignwiththeoreticalex- developedwithintheLLMteacher-studentframe-
pectationsaboutgenderedpoliticalprioritiesand work(KuzmanandLjubešic´,2025),whichenables
role specialization in parliamentary work (de Vet scalable fine-tuning of BERT-like models without
and Devroe, 2023). Women speak more often relyingonmanually-annotatedtrainingdata.
aboutHealth,SocialWelfare,andEducation top- We show that large language models can re-
ics across most countries, as shown by the red place manual annotation for building domain-
coloringintheseareas. Menhaveastrongerpres- specifictopicclassifiers. Ourapproachissimple:
enceinareasliketransportation,economics,and usealargelanguagemodeltoannotateasubsetof
defense-relatedtopics,whichalignswithtraditional parliamentaryspeeches,thenfine-tuneasmaller
associationsbetweenmasculinityand“hard”pol- BERT-like model on this LLM-annotated training
icydomainsinvolvinginfrastructure,finance,and data. Thisprocedureproducesaclassifierthatis
| security. |            |        |        |        |      | specializedforthespecificdatasetofinterest. |     |     |     |     |     | We  |
| --------- | ---------- | ------ | ------ | ------ | ---- | ------------------------------------------- | --- | --- | --- | --- | --- | --- |
| In some   | countries, | we see | larger | gender | gaps |                                             |     |     |     |     |     |     |
showthattheLLMcanserveasareliableannotator
thaninothers,showingsignificantandinteresting forpolicytopicclassification,asitsagreementwith
cross-national variation (notable outliers include humanannotatorsiscomparabletointer-annotator
Turkeywithparticularlystronggenderdifferences agreement among humans. Moreover, smaller
| inCivilRights). |     |     |     |     |     | models | fine-tuned | on  | LLM-annotated |     | in-domain |     |
| --------------- | --- | --- | --- | --- | --- | ------ | ---------- | --- | ------------- | --- | --------- | --- |
dataachieveperformancecomparabletotheLLM
|     |     |     |     |     |     | itself. Comparedtoexistingmodelsthatwerefine- |                    |     |     |      |                |     |
| --- | --- | --- | --- | --- | --- | --------------------------------------------- | ------------------ | --- | --- | ---- | -------------- | --- |
|     |     |     |     |     |     | tuned on                                      | manually-annotated |     |     | data | from different |     |
datasetsanddomains,ourapproachperformsbet-
|     |     |     |     |     |     | teronthetargetparliamentarydata. |     |     |     |     | Thisfinding |     |
| --- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- | --- | ----------- | --- |
highlightstheimportanceofdomain-alignedtrain-
|     |     |     |     |     |     | ingdata: | amodeltrainedonin-domaindataanno- |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------- | --------------------------------- | --- | --- | --- | --- | --- |
tatedbyanLLMcanoutperformmodelstrainedon
|     |     |     |     |     |     | manually-annotatedbutout-of-domaindata. |     |     |     |     |     | Atthe |
| --- | --- | --- | --- | --- | --- | --------------------------------------- | --- | --- | --- | --- | --- | ----- |
sametime,theapproachremainscost-effective,as
manualannotationisrequiredonlyforevaluation
ratherthanforlarge-scaletraining.
|     |     |     |     |     |     | Secondly, | this | paper | introduces |     | the ParlaCAP |     |
| --- | --- | --- | --- | --- | --- | --------- | ---- | ----- | ---------- | --- | ------------ | --- |
2025),13
|                |              |            |      |                  |        | dataset           | (Ljubešic´ | et        | al.,             |                | which     | repre-  |
| -------------- | ------------ | ---------- | ---- | ---------------- | ------ | ----------------- | ---------- | --------- | ---------------- | -------------- | --------- | ------- |
|                |              |            |      |                  |        | sents a           | major      | step      | forward          | in comparative |           | po-     |
|                |              |            |      |                  |        | litical research, |            | providing | unprecedented    |                |           | access  |
|                |              |            |      |                  |        | to systematic     |            | analysis  | of parliamentary |                | attention |         |
|                |              |            |      |                  |        | in 28 countries   |            | and       | autonomous       |                | regions.  | With    |
| Figure 6:      | The absolute | difference |      | in topic         | proba- |                   |            |           |                  |                |           |         |
|                |              |            |      |                  |        | speech-level      |            | data on   | parties,         | speakers,      |           | topics, |
| bility between | female       | and        | male | parliament-level |        |                   |            |           |                  |                |           |         |
andsentence-leveldataonsentiment,thisfreely-
| distributions. | Red | color signals | that | female | PMs |           |         |          |     |                   |     |     |
| -------------- | --- | ------------- | ---- | ------ | --- | --------- | ------- | -------- | --- | ----------------- | --- | --- |
|                |     |               |      |        |     | available | dataset | provides |     | new opportunities |     | for |
discussthespecifictopicinthespecificparliament
politicalscientistsandsocialscienceresearchers
more,whilebluecolorsignalstheopposite.
toexplorehowparliamentswork.
7. Acknowledgments
6. Conclusion
|                |     |          |                |     |     | We would | like | to thank | the | annotators | of  | the test |
| -------------- | --- | -------- | -------------- | --- | --- | -------- | ---- | -------- | --- | ---------- | --- | -------- |
| In this paper, | we  | make two | contributions: |     | we  |          |      |          |     |            |     |          |
datasets,especiallyMirnaPotocˇnjak,themainan-
demonstrateaneffectiveandcomputationallyprac-
|     |     |     |     |     |     | notator, | for their | diligence | and | the | time devoted |     |
| --- | --- | --- | --- | --- | --- | -------- | --------- | --------- | --- | --- | ------------ | --- |
ticalmethodfordomain-specifictopicclassification;
|                  |        |                   |           |           |          | to manual                                | annotation, |     | which | resulted | in the | high- |
| ---------------- | ------ | ----------------- | --------- | --------- | -------- | ---------------------------------------- | ----------- | --- | ----- | -------- | ------ | ----- |
| and we introduce |        | ParlaCAP,         | a dataset | providing |          |                                          |             |     |       |          |        |       |
|                  |        |                   |           |           |          | qualityevaluationdatasetsusedinthiswork. |             |     |       |          |        | We    |
| speech-level     | policy | topic information |           | for       | 28 Euro- |                                          |             |     |       |          |        |       |
wouldalsoliketothanktheCLASSLAknowledge
peanparliaments.
centreforSouthSlaviclanguagesandtheSlove-
| The ParlaCAP   |         | classifier | (Kuzman         | Pungeršek |      |                |     |                |     |     |                |     |
| -------------- | ------- | ---------- | --------------- | --------- | ---- | -------------- | --- | -------------- | --- | --- | -------------- | --- |
|                |         |            |                 |           |      | nian CLARIN.SI |     | infrastructure |     | for | their valuable |     |
| and Ljubešic´, | 2025)12 | is a       | domain-specific |           | mul- |                |     |                |     |     |                |     |
support.
tilingualtransformermodelfortopicclassification
12The ParlaCAP topic classifier is available in Hug- 13The ParlaCAP dataset is available in the
ging Face at https://www.doi.org/10.57967/ CROSSDA repository at https://doi.org/10.
| hf/6684. |     |     |     |     |     | 23669/1ZTELP. |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- |

Thisworkwassupportedinpartbytheproject HolgerDöringandSvenRegel.2019. PartyFacts:
“Large Language Models for Digital Humanities” Adatabaseofpoliticalpartiesworldwide. Party
(GrantGC-0002), theresearchprogramme“Lan- Politics,25(2):97–109.
| guageResources |           | andTechnologiesforSlovene” |     |          |             |     |                |     |        |            |      |        |
| -------------- | --------- | -------------------------- | --- | -------- | ----------- | --- | -------------- | --- | ------ | ---------- | ---- | ------ |
|                |           |                            |     |          |             |     | Tomaž Erjavec, |     | Matyáš | Kopp,      | Taja | Kuz-   |
| (Grant         | P6-0411), | and                        | the | Research | Infrastruc- |     |                |     |        |            |      |        |
|                |           |                            |     |          |             |     | man Pungeršek, |     | Nikola | Ljubešic´, |      | Maciej |
tureDARIAH-SI(I0-E007),allfundedbytheARIS
|     |     |     |     |     |     |     | Ogrodniczuk, |     | Petya Osenova, |     | ..., and | Darja |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | -------------- | --- | -------- | ----- |
SlovenianResearchandInnovationAgency.
|     |     |     |     |     |     |     | Fišer.2025. | Multilingualcomparablecorporaof |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------------------------------- | --- | --- | --- | --- |
TheauthorsacknowledgetheOSCARSproject,
|                  |     |           |      |       |          |       | parliamentarydebatesParlaMint5.0. |          |            |     |            | Slovenian |
| ---------------- | --- | --------- | ---- | ----- | -------- | ----- | --------------------------------- | -------- | ---------- | --- | ---------- | --------- |
| and its ParlaCAP |     | cascading |      | grant | project, | which |                                   |          |            |     |            |           |
|                  |     |           |      |       |          |       | language                          | resource | repository |     | CLARIN.SI: |           |
| has received     |     | funding   | from | the   | European | Com-  |                                   |          |            |     |            |           |
http://hdl.handle.net/11356/2004.
| mission’s        | Horizon | Europe     |     | Research | and       | Inno- |                |              |            |           |         |        |
| ---------------- | ------- | ---------- | --- | -------- | --------- | ----- | -------------- | ------------ | ---------- | --------- | ------- | ------ |
| vation programme |         | under      |     | grant    | agreement | No.   |                |              |            |           |         |        |
|                  |         |            |     |          |           |       | Tomaž Erjavec, |              | Matyáš     | Kopp,     | Maciej  | Ogrod- |
| 101129751.       |         |            |     |          |           |       | niczuk,        | Petya        | Osenova,   | ..., and  | Darja   | Fišer. |
|                  |         |            |     |          |           |       | 2024a.         | Multilingual | comparable |           | corpora | of     |
|                  |         | References |     |          |           |       | parliamentary  |              | debates    | ParlaMint | 4.1.    | Slove- |
nianlanguageresourcerepositoryCLARIN.SI:
FrankRBaumgartner,ChristianBreunig,andEmil- http://hdl.handle.net/11356/1912.
ianoGrossman.2019.ComparativePolicyAgen-
|      |         |        |       |        |            |     | Tomaž Erjavec, |       | Matyáš   | Kopp, | Maciej | Ogrod-   |
| ---- | ------- | ------ | ----- | ------ | ---------- | --- | -------------- | ----- | -------- | ----- | ------ | -------- |
| das: | Theory, | Tools, | Data. | Oxford | University |     |                |       |          |       |        |          |
|      |         |        |       |        |            |     | niczuk,        | Petya | Osenova, | Darja | Fišer, | ..., and |
Press.
|     |     |     |     |     |     |     | Anna Kryvenko. |     | 2023. | Multilingual |     | compara- |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ----- | ------------ | --- | -------- |
ShaunBevan.2019. Gonefishing. Comparative blecorporaofparliamentarydebatesParlaMint
|                |     |                           |     |     |     |     | 3.0. Slovenian |     | language | resource | repository |     |
| -------------- | --- | ------------------------- | --- | --- | --- | --- | -------------- | --- | -------- | -------- | ---------- | --- |
| policyagendas: |     | Theory,tools,data,page17. |     |     |     |     |                |     |          |          |            |     |
CLARIN.SI:http://hdl.handle.net/11356/1486.
| Alexis Conneau, |     | Kartikay |     | Khandelwal, |     | Naman |     |     |     |     |     |     |
| --------------- | --- | -------- | --- | ----------- | --- | ----- | --- | --- | --- | --- | --- | --- |
Goyal,VishravChaudhary,GuillaumeWenzek, TomažErjavec,MatyášKopp,NikolaLjubešic´,Taja
Francisco Guzmán, Edouard Grave, Myle Ott, Kuzman, Paul Rayson, Petya Osenova, Ma-
|     |     |     |     |     |     |     | ciej Ogrodniczuk, |     | Çag˘rı | Çöltekin, | Danijel | Ko- |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ------ | --------- | ------- | --- |
LukeZettlemoyer,andVeselinStoyanov.2020.
Unsupervisedcross-lingualrepresentationlearn- ržinek, Katja Meden, Jure Skubic, Peter Rup-
|             |     |                              |     |     |     |     | nik, Tommaso    |     | Agnoloni, | José       | Aires, | Barkar- |
| ----------- | --- | ---------------------------- | --- | --- | --- | --- | --------------- | --- | --------- | ---------- | ------ | ------- |
| ingatscale. |     | InProceedingsofthe58thannual |     |     |     |     |                 |     |           |            |        |         |
|             |     |                              |     |     |     |     | son, StarkaDur, |     | Roberto   | Bartolini, | Núria  | Bel,    |
meetingoftheassociationforcomputationallin-
guistics,pages8440–8451. CalzadaMaríaPérez,RobertsDarg‘is,Sascha
Diwersy,MariaGavriilidou,vanRubenHeusden,
| Michael | Coppedge, |     | John | Gerring, | Carl | Henrik |     |     |     |     |     |     |
| ------- | --------- | --- | ---- | -------- | ---- | ------ | --- | --- | --- | --- | --- | --- |
MikelIruskieta,NeemeKahusk,AnnaKryvenko,
Knutsen,StaffanI.Lindberg,JanTeorell,David Noémi Ligeti-Nagy, Carmen Magariños, Mar-
Altman, Fabio Angiolillo, Michael Bernhard, tin Mölder, Costanza Navarretta, Kiril Simov,
Agnes Cornell, M. Steven Fish, Linnea Fox, Lars Magne Tungland, Jouni Tuominen, John
Lisa Gastaldi, Haakon Gjerløw, Adam Glynn, Vidler,AdinaIoanaVladu,TanjaWissik,Väinö
| Ana Good | God, | Sandra |     | Grahn, | Allen | Hicken, |                                 |     |     |     |              |     |
| -------- | ---- | ------ | --- | ------ | ----- | ------- | ------------------------------- | --- | --- | --- | ------------ | --- |
|          |      |        |     |        |       |         | Yrjänäinen,andDarjaFišer.2024b. |     |     |     | ParlaMintII: |     |
Katrin Kinzelbach, Kyle L. Marquardt, Kelly AdvancingComparableParliamentaryCorpora
McMann, Valeriya Mechkova, Anja Neundorf, AcrossEurope. LanguageResourcesandEval-
PamelaPaxton,DanielPemstein,Johannesvon
uation.
| Römer, | Brigitte | Seim, | Rachel |     | Sigman, | Svend- |     |     |     |     |     |     |
| ------ | -------- | ----- | ------ | --- | ------- | ------ | --- | --- | --- | --- | --- | --- |
ErikSkaaning,JeffreyStaton,AkselSundström, TomažErjavec,MaciejOgrodniczuk,PetyaOsen-
ova,NikolaLjubešic´,KirilSimov,AndrejPancˇur,
MarcusTannenberg,EitanTzelgov,YitingWang,
MichałRudolf,MatyášKopp,StarkaDurBarkar-
| Felix | Wiebrecht, | Tore | Wig, | and | Daniel | Ziblat. |     |     |     |     |     |     |
| ----- | ---------- | ---- | ---- | --- | ------ | ------- | --- | --- | --- | --- | --- | --- |
2025. V-DemCodebookv15. son, Steinþór Steingrímsson, Çag˘rı Çöltekin,
JessedeDoes,KatrienDepuydt,TommasoAg-
| Franciska | de  | Jong, | Dieter |     | Van | Uytvanck, |     |     |     |     |     |     |
| --------- | --- | ----- | ------ | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
noloni,GiuliaVenturi,MaríaCalzadaPérez,Lu-
FrancescaFrontini,AntalvandenBosch,Darja ciana D. de Macedo, Costanza Navarretta, Gi-
Fišer,andAndreasWitt.2022. LanguageMat- ancarloLuxardo,MatthewCoole,PaulRayson,
ters: The European Research Infrastructure VaidasMorkevicˇius,TomasKrilavicˇius,Roberts
CLARIN, Today and Tomorrow. In CLARIN, Darg´is, Orsolya Ring, Ruben van Heusden,
pages31–58.DeGruyter.
|     |     |     |     |     |     |     | Maarten | Marx, | and Darja | Fišer. | 2022. | The |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----- | --------- | ------ | ----- | --- |
ParlaMintcorporaofparliamentaryproceedings.
| Benjamin | de Vet | and | Robin | Devroe. | 2023. | Party |     |     |     |     |     |     |
| -------- | ------ | --- | ----- | ------- | ----- | ----- | --- | --- | --- | --- | --- | --- |
LanguageResourcesandEvaluation.
| Control, | Intraparty |     | Competition, |     | and | the Sub- |     |     |     |     |     |     |
| -------- | ---------- | --- | ------------ | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
stantiveFocusofWomen’sParliamentaryQues- Will Jennings, Shaun Bevan, Arco Timmear-
tions: EvidencefromBelgium. PoliticsandGen- mans,GerardBreeman,SylvainBrouard,Laura
der,19(1):247–271. Chaqués-Bonafont,ChristofferGreen-Pedersen,

Peter John, Peter B. Mortensen, and Anna M. MichalMochtak,PeterRupnik,andNikolaLjubešic´.
Palau.2011. Effectsofthecorefunctionsofgov- 2024. The ParlaSent Multilingual Training
ernmentonthediversityofexecutiveagendas. DatasetforSentimentIdentificationinParliamen-
ComparativePoliticalStudies,44(8):1001–1030. tary Proceedings. In Proceedings of the 2024
JointInternationalConferenceonComputational
| Philipp Koehn. | 2011. |     | European | parliament | pro- |              |          |     |           |     |     |        |
| -------------- | ----- | --- | -------- | ---------- | ---- | ------------ | -------- | --- | --------- | --- | --- | ------ |
|                |       |     |          |            |      | Linguistics, | Language |     | Resources |     | and | Evalu- |
ceedingsparallelcorpus1996-2011. ation (LREC-COLING 2024), pages 16024–
16036.
| Klaus Krippendorff. |     | 2018.            | Content |      | analysis: An |     |     |     |     |     |     |     |
| ------------------- | --- | ---------------- | ------- | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- |
| introduction        | to  | its methodology. |         | Sage | Publica-     |     |     |     |     |     |     |     |
CostanzaNavarretta,DorteHaltrupHansen,and
tions.
BartJongejan.2024.EnrichingtheParlaMint-DK
|             |     |        |            |     |           | corpuswithPolicyDomains. |     |     |     | InCLARINAnnual |     |     |
| ----------- | --- | ------ | ---------- | --- | --------- | ------------------------ | --- | --- | --- | -------------- | --- | --- |
| Taja Kuzman | and | Nikola | Ljubešic´. |     | 2025. LLM |                          |     |     |     |                |     |     |
Teacher-StudentFrameworkforTextClassifica- ConferenceProceedings,page130.
| tionWithNoManuallyAnnotatedData:    |     |     |     |     | ACase |                                 |     |       |         |     |          |     |
| ----------------------------------- | --- | --- | --- | --- | ----- | ------------------------------- | --- | ----- | ------- | --- | -------- | --- |
|                                     |     |     |     |     |       | OpenAI. 2024.                   |     | Hello | GPT-4o. |     | https:// |     |
| StudyinIPTCNewsTopicClassification. |     |     |     |     | IEEE  |                                 |     |       |         |     |          |     |
|                                     |     |     |     |     |       | openai.com/index/hello-gpt-4o/. |     |       |         |     |          | Ac- |
Access.
cessedSeptember11,2024.
| Taja Kuzman, | Nikola |     | Ljubešic´, | Tomaž | Erjavec, |     |     |     |     |     |     |     |
| ------------ | ------ | --- | ---------- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- |
Matyáš Kopp, Maciej Ogrodniczuk, Petya Christian Rauh and Jan Schwalbach. 2020. The
|          |      |         |      |     |              | ParlSpeechV2dataset: |     |     | Full-textcorporaof6.3 |     |     |     |
| -------- | ---- | ------- | ---- | --- | ------------ | -------------------- | --- | --- | --------------------- | --- | --- | --- |
| Osenova, | Paul | Rayson, | ..., | and | Darja Fišer. |                      |     |     |                       |     |     |     |
2024. Linguistically annotated multilingual million parliamentary speeches in the key leg-
comparable corpora of parliamentary debates islativechambersofninerepresentativedemoc-
|            |                  |     |     |      |        | racies. HarvardDataverse,1(1). |     |     |     |     |     |     |
| ---------- | ---------------- | --- | --- | ---- | ------ | ------------------------------ | --- | --- | --- | --- | --- | --- |
| in English | ParlaMint-en.ana |     |     | 4.1. | Slove- |                                |     |     |     |     |     |     |
nianlanguageresourcerepositoryCLARIN.SI:
PeterRupnik,NikolaLjubešic´,andMichalMochtak.
http://hdl.handle.net/11356/1910.
2023. Multilingualparliamentsentimentregres-
TajaKuzmanPungeršekandNikolaLjubešic´.2025. sion model XLM-R-ParlaSent. Hugging Face:
MultilingualParlaCAPmodelforCAPTopicClas- https://doi.org/10.57967/hf/6718.
| sificationinParliamentarySpeeches. |     |     |     |     | Hugging |     |     |     |     |     |     |     |
| ---------------------------------- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
Face: https://doi.org/10.57967/hf/6684. ChristopherMichaelRytting,TaylorSorensen,Lisa
|             |           |     |     |        |            | Argyle,                      | Ethan | Busby, | Nancy | Fulda, |             | Joshua |
| ----------- | --------- | --- | --- | ------ | ---------- | ---------------------------- | ----- | ------ | ----- | ------ | ----------- | ------ |
| Taja Kuzman | Pungeršek |     | and | Nikola | Ljubešic´. |                              |       |        |       |        |             |        |
|             |           |     |     |        |            | Gubler,andDavidWingate.2023. |       |        |       |        | TowardsCod- |        |
2026. MultilingualtrainingdatasetforCAPpol- ingSocialScienceDatasetswithLanguageMod-
| icy topic | classification |     | ParlaCAP-train. |     | Slove- |     |     |     |     |     |     |     |
| --------- | -------------- | --- | --------------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
els. arXivpreprintarXiv:2306.02177.
nianlanguageresourcerepositoryCLARIN.SI:
http://hdl.handle.net/11356/2093. Miklós Sebo˝k, Ákos Máté, Orsolya Ring, Viktor
|     |     |     |     |     |     | Kovács, | and Richárd |     | Lehoczki. |     | 2024. | Lever- |
| --- | --- | --- | --- | --- | --- | ------- | ----------- | --- | --------- | --- | ----- | ------ |
TajaKuzmanPungeršek,PeterRupnik,IvanPorup-
|                                        |     |     |     |     |       | aging Open     | Large | Language              |     | Models | for | Multi- |
| -------------------------------------- | --- | --- | --- | --- | ----- | -------------- | ----- | --------------------- | --- | ------ | --- | ------ |
| ski,VukDinic´,andNikolaLjubešic´.2025. |     |     |     |     | State |                |       |                       |     |        |     |        |
|                                        |     |     |     |     |       | lingual Policy |       | Topic Classification: |     |        | The | Babel  |
oftheArtinTextClassificationforSouthSlavic
|            |             |     |     |            |       | Machine | Approach. | Social |     | Science | Computer |     |
| ---------- | ----------- | --- | --- | ---------- | ----- | ------- | --------- | ------ | --- | ------- | -------- | --- |
| Languages: | Fine-Tuning |     | or  | Prompting? | arXiv |         |           |        |     |         |          |     |
Review.
preprintarXiv:2511.07989.
|                   |       |          |         |           |           | Miklós Sebo˝k,    |            | Sven-Oliver             |         | Proksch, | Christian   |     |
| ----------------- | ----- | -------- | ------- | --------- | --------- | ----------------- | ---------- | ----------------------- | ------- | -------- | ----------- | --- |
| Nikola Ljubešic´, |       | Peter    | Rupnik, |           | Taja Kuz- |                   |            |                         |         |          |             |     |
|                   |       |          |         |           |           | Rauh, Péter       | Visnovitz, |                         | Gergo˝  | Balázs,  | and         | Jan |
| man Pungeršek,    |       |          | Ivan    | Porupski, | Michal    |                   |            |                         |         |          |             |     |
|                   |       |          |         |           |           | Schwalbach.2023.  |            | ComparativeEuropeanLeg- |         |          |             |     |
| Mochtak,          | Vuk   | Dinic´,  | Daniela | Širinic´, | Matyáš    |                   |            |                         |         |          |             |     |
|                   |       |          |         |           |           | islative Research |            | In                      | The Age | Of       | Large-Scale |     |
| Kopp, and         | Tomaž | Erjavec. |         | 2025.     | ParlaCAP: |                   |            |                         |         |          |             |     |
Dataset for tracking political agenda-setting ComputationalTextAnalysis: AReviewArticle.
InternationalPoliticalScienceReview.
| across | European | parliaments. |     |     | CROSSDA: |     |     |     |     |     |     |     |
| ------ | -------- | ------------ | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
https://doi.org/10.23669/1ZTELP.
Cˇakar.2019.
|     |     |     |     |     |     | DanielaŠirinic´ | andDarioNikic´ |     |     |     |     | Croa- |
| --- | --- | --- | --- | --- | --- | --------------- | -------------- | --- | --- | --- | --- | ----- |
Nikola Ljubešic´, Peter Rupnik, and Rik van tian political agendas. In Comparative Policy
|            |              |     |              |         |            | Agendas: | Theory,Tools,Data.OxfordUniversity |     |     |     |     |     |
| ---------- | ------------ | --- | ------------ | ------- | ---------- | -------- | ---------------------------------- | --- | --- | --- | --- | --- |
| Noord.     | 2023.        |     | Multilingual |         | parliamen- |          |                                    |     |     |     |     |     |
| tary model | XLM-R-parla. |     |              | Hugging | Face:      | Press.   |                                    |     |     |     |     |     |
https://doi.org/10.57967/hf/6717.
|     |     |     |     |     |     | Željko Poljak. | 2024. | Give | the | media | what | they |
| --- | --- | --- | --- | --- | --- | -------------- | ----- | ---- | --- | ----- | ---- | ---- |
Michal Mochtak and Maurits Meijers. In review. need: Negativityasamediaaccesstoolforpoliti-
FindingtheNeedleinaHaystack: UsingLarge cians.TheInternationalJournalofPress/Politics,
LanguageModelstoDetectRareSpeechActs. 0(0):19401612241234861.
JournalofComputationalSocialScience.

|                  | 8.        | Appendix   |              |
| ---------------- | --------- | ---------- | ------------ |
| In the following | sections, | we provide | the descrip- |
tionsoftheCAPlabelsthatwereusedinmanual
annotationandautomaticannotationwithanLLM
(Section8.1),theannotationguidelinesthatwere
providedtotheannotatorsofthetestdata(Section
| 8.2), and | the prompt | used to guide | the large lan- |
| --------- | ---------- | ------------- | -------------- |
guagemodelintheautomaticannotationoftraining
data(Section8.3).
| 8.1. CAP        | Labels             | Description               |         |
| --------------- | ------------------ | ------------------------- | ------- |
| Tables          | 5, 6 and 7 provide | the descriptions          | of the  |
| majorCAPtopics. |                    | Thesedescriptionswereused |         |
| for manual      | annotation         | and for automatic         | annota- |
tionoftrainingdatawithalargelanguagemodel.
| They were | developed | based on the | descriptions |
| --------- | --------- | ------------ | ------------ |
ofCAPsubtopicsintheMasterCodebook(Bevan,
2019)14,andwerefurtherimprovedbasedonthe
andCˇakar,2019)
CroatianCAPguidelines(Širinic´
andexpertinput.
14https://www.comparativeagendas.net/
pages/master-codebook

MajorTopic Description
Macroeconomics(1) Issues related to domestic macroeconomic policy, such as the state and
prospect of the national economy, economic policy, inflation, interest rates,
monetary policy, cost of living, unemployment rate, national budget, public
debt,pricecontrol,taxenforcement,industrialrevitalizationandgrowth.
CivilRights(2) Issuesrelatedtocivilrightsandminorityrights,discriminationtowardsraces,
gender,sexualorientation,handicap,andotherminorities,votingrights,free-
domofspeech,religiousfreedoms,privacyrights,protectionofpersonaldata,
abortionrights,anti-governmentactivitygroups(e.g.,localinsurgencygroups),
religionandtheChurch.
Health(3) Issues related to health care, health care reforms, health insurance, drug
industry, medical facilities, medical workers, disease prevention, treatment,
and health promotion, drug and alcohol abuse, mental health, research in
medicine,medicalliabilityandunfairmedicalpractices.
Agriculture(4) Issues related to agriculture policy, fishing, agricultural foreign trade, food
marketing,subsidiestofarmers,foodinspectionandsafety,animalandcrop
disease, pest control and pesticide regulation, welfare for animals in farms,
pets,veterinarymedicine,agriculturalresearch.
Labor(5) Issuesrelatedtolabor,employment,employmentprograms,employeebenefits,
pensionsandretirementaccounts,minimumwage,laborlaw,jobtraining,labor
unions,workersafetyandprotection,youthemploymentandseasonalworkers.
Education(6) Issuesrelatedtoeducationalpolicies,primaryandsecondaryschools,student
loansandeducationfinance,theregulationofcollegesanduniversities,school
reforms, teachers, vocational training, evening schools, safety in schools,
effortstoimproveeducationalstandards,andissuesrelatedtolibraries,dictio-
naries,teachingmaterial,researchineducation.
Environment(7) Issuesrelatedtoenvironmentalpolicy,drinkingwatersafety,allkindsofpol-
lution (air, noise, soil), waste disposal, recycling, climate change, outdoor
environmentalhazards(e.g.,asbestos),speciesandforestprotection,marine
andfreshwaterenvironment,hunting,regulationoflaboratoryorperformance
animals, land and water resource conservation, research in environmental
technology.
Energy(8) Issues related to energy policy, electricity, regulation of electrical utilities,
nuclearenergyanddisposalofnuclearwaste,naturalgasandoil,drilling,oil
spills,oilandgasprices,heatsupply,shortagesandgasolineregulation,coal
production,alternativeandrenewableenergy,energyconservationandenergy
efficiency,energyresearch.
Immigration(9) Issues related to immigration, refugees, and citizenship, integration issues,
regulation of residence permits, asylum applications; criminal offences and
diseasescausedbyimmigration.
Transportation(10) Issuesrelatedtomasstransportationconstructionandregulation,bustrans-
port,regulationrelatedtomotorvehicles,roadconstruction,maintenanceand
safety, parking facilities, traffic accidents statistics, air travel, rail travel, rail
freight,maritimetransportation,inlandwaterwaysandchannels,transportation
researchanddevelopment.
Table5: DescriptionsofmajorCAPTopicsusedinthisstudy.

MajorTopic Description
LawandCrime(12) Issuesrelatedtothecontrol,prevention,andimpactofcrime;alllawenforce-
ment agencies, including border and customs, police, court system, prison
system; terrorism, white collar crime, counterfeiting and fraud, cyber-crime,
drugtrafficking,domesticviolence,childwelfare,familylaw,juvenilecrime.
SocialWelfare(13) Issuesrelatedtosocialwelfarepolicy,theMinistryofSocialAffairs,socialser-
vices,povertyassistanceforlow-incomefamiliesandfortheelderly,parental
leaveandchildcare,assistanceforpeoplewithphysicalormentaldisabilities,
including early retirement pension, discounts on public services, volunteer
associations(e.g.,RedCross),charities,andyouthorganizations.
Housing(14) Issuesrelatedtohousing,urbanaffairsandcommunitydevelopment,housing
market, property tax, spatial planning, rural development, location permits,
constructioninspection,illegalconstruction,industrialandcommercialbuilding
issues, national housing policy, housing for low-income individuals, rental
housing,housingfortheelderly,e.g.,nursinghomes,housingforthehomeless
andeffortstoreducehomelessness,researchrelatedtohousing.
DomesticCommerce Issues related to banking, finance and internal commerce, including stock
(15) exchange, investments, consumer finance, mortgages, credit cards, insur-
anceavailabilityandcost,accountingregulation,personal,commercial,and
municipal bankruptcies, programs to promote small businesses, copyrights
and patents, intellectual property, natural disaster preparedness and relief,
consumersafety;regulationandpromotionoftourism,sports,gambling,and
personalfitness;domesticcommerceresearch.
Defense(16) Issues related to defense policy, military intelligence, espionage, weapons,
militarypersonnel,reserveforces,militarybuildings,militarycourts,nuclear
weapons,civildefense, includingfirefightersandmountainrescueservices,
homeland security, military aid or arms sales to other countries, prisoners
of war and collateral damage to civilian populations, military nuclear and
hazardous waste disposal and military environmental compliance, defense
alliances and agreements, direct foreign military operations, claims against
military,defenseresearch.
Technology(17) Issuesrelatedtoscienceandtechnologytransferandinternationalscienceco-
operation,researchpolicy,governmentspaceprogramsandspaceexploration,
telephones and telecommunication regulation, broadcast media (television,
radio,newspapers,films),weatherforecasting,geologicalsurveys,computer
industry,cybersecurity.
ForeignTrade(18) Issues related to foreign trade, trade negotiations, free trade agreements,
importregulation,exportpromotionandregulation,subsidies,privatebusiness
investment and corporate development, competitiveness, exchange rates,
the strength of national currency in comparison to other currencies, foreign
investmentandsalesofcompaniesabroad.
International Affairs Issuesrelatedtointernationalaffairs,foreignpolicyandrelationstoothercoun-
(19) tries,issuesrelatedtotheMinistryofForeignAffairs,foreignaid,international
agreements (such as Kyoto agreement on the environment, the Schengen
agreement),internationalorganizations(includingUnitedNations,UNESCO,
InternationalOlympicCommittee,InternationalCriminalCourt),NGOs,issues
related to diplomacy, embassies, citizens abroad; issues related to border
control;issuesrelatedtointernationalfinance,includingtheWorldBankand
InternationalMonetaryFund,thefinancialsituationoftheEU;issuesrelated
to a foreign country that do not impact the home country; issues related to
humanrightsinothercountries,internationalterrorism.
Table6: SecondpartofthedescriptionsofmajorCAPTopicsusedinthisstudy.

MajorTopic Description
Government Opera- Issues related to general government operations, the work of multiple de-
tions(20) partments,publicemployees,postalservices,nominationsandappointments,
nationalmints, medals, andcommemorativecoins, managementofgovern-
mentproperty,governmentprocurementandcontractors,publicscandaland
impeachment,claimsagainstthegovernment,thestateinspectorateandaudit,
anti-corruptionpolicies,regulationofpoliticalcampaigns,politicaladvertising
andvoterregistration,censusandstatisticscollectionbygovernment;issues
relatedtolocalgovernment,capitalcityandmunicipalities,includingdecentral-
ization;issuesrelatedtonationalholidays.
PublicLands(21) Issuesrelatedtonationalparks,memorials,historicsites,andprotectedareas,
includingthemanagementandstaffingofculturalsites;museums;useofpublic
landsandforests, establishmentandmanagementofharborsandmarinas;
issuesrelatedtofloodcontrol,forestfires,livestockgrazing.
Culture(23) Issues related to cultural policies, Ministry of Culture, public spending on
culture,culturalemployees,issuesrelatedtosupportoftheatresandartists;
allocationoffundsfromthenationallottery,issuesrelatedtoculturalheritage.
Other(0) Othertopicsnotmentioningpolicyagendas,includingtheproceduresofparlia-
mentarymeetings,e.g.,pointsoforder,votingprocedures,meetinglogistics;
interpersonalspeech,e.g.,greetings,personalstories,tributes,interjections,
argumentsbetweenthemembers;rhetoricalspeech,e.g.,jokes,literaryrefer-
ences.
Table7: ThirdpartofthedescriptionsofmajorCAPTopicsusedinthisstudy.

| 8.2. Annotation | Guidelines |     |     |
| --------------- | ---------- | --- | --- |
Thefollowingguidelineswereprovidedtothean-
notatorsofEnglish,Croatian,SerbianandBosnian
testdatasets,alongwiththelabeldescriptions(see
Section8.1).
| Your | task is to classify | the provided | text into a |
| ---- | ------------------- | ------------ | ----------- |
policyagendatopiclabel,meaningthatyouneed
torecognizewhatisthepredominanttopicofthe
text. Thelabelsandtheirdescriptionsareprovided
above.
Youareprovidedwithexcerptsfromparliamen-
taryspeechesfromtheCroatian,Serbian,Bosnian
orBritishparliamentinCroatian,Serbian,Bosnian
orEnglishlanguage.
Alwaysprovidealabel,evenifyouarenotsure.
| Followthefollowingrule: |     | ifthespeechmentions |     |
| ----------------------- | --- | ------------------- | --- |
apolicyareaandapolicyinstrument(e.g.,taxes,
| laws), pick | the label based | on the area, | not the |
| ----------- | --------------- | ------------ | ------- |
instrument(e.g.,annotatemortgagetaxchanges
with14(Housing),lawoneducationwith6(Educa-
tion)).
Additionallabelforimpossiblyhardcases
Weareinterestedonlyinreasonableandinfor-
| mativeinstances. | Thatiswhyweaddedtothelist |     |     |
| ---------------- | ------------------------- | --- | --- |
anadditionalcategoryforyouto"discard"thetext:
| -"donotknow": | ifitisimpossibleforyoutodecide |     |     |
| ------------- | ------------------------------ | --- | --- |
underwhichlabelthisinstancefits.
8.3. Prompt
InFigure7,wepresentthepromptusedtoguide
| the large | language model | in the automatic | anno- |
| --------- | -------------- | ---------------- | ----- |
tationofparliamentaryspeecheswithCAPpolicy
topics.

Figure7: PromptusedfortheautomaticannotationofparliamentaryspeecheswithanLLMfollowingthe
CAPschema.