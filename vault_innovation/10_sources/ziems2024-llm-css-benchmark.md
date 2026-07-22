4
2
0
2

b
e
F
6
2

]
L
C
.
s
c
[

3
v
4
1
5
3
0
.
5
0
3
2
:
v
i
X
r
a

Can Large Language Models Transform
Computational Social Science?

Caleb Ziems∗
Stanford University

Omar Shaikh
Stanford University

Zhehao Zhang
Dartmouth College

William Held
Georgia Institute of Technology

Jiaao Chen
Georgia Institute of Technology

Diyi Yang∗∗
Stanford University

Large Language Models (LLMs) are capable of successfully performing many language process-
ing tasks zero-shot (without training data). If zero-shot LLMs can also reliably classify and
explain social phenomena like persuasiveness and political ideology, then LLMs could augment
the Computational Social Science (CSS) pipeline in important ways. This work provides a
road map for using LLMs as CSS tools. Towards this end, we contribute a set of prompting
best practices and an extensive evaluation pipeline to measure the zero-shot performance of 13
language models on 25 representative English CSS benchmarks. On taxonomic labeling tasks
(classification), LLMs fail to outperform the best fine-tuned models but still achieve fair levels
of agreement with humans. On free-form coding tasks (generation), LLMs produce explanations
that often exceed the quality of crowdworkers’ gold references. We conclude that the performance
of today’s LLMs can augment the CSS research pipeline in two ways: (1) serving as zero-
shot data annotators on human annotation teams, and (2) bootstrapping challenging creative
generation tasks (e.g., explaining the underlying attributes of a text). In summary, LLMs are
posed to meaningfully participate in social science analysis in partnership with humans.

1. Introduction

The most surprising scientific changes tend to arrive, not from accumulated facts and
discoveries, but from the invention of new tools and methodologies that trigger “paradigm
shifts” (Kuhn 1962).

∗ E-mail: Caleb Ziems: cziems@stanford.edu. William Held: wheld3@gatech.edu; Omar Shaikh:

oshaikh@stanford.edu; Jiaao Chen: jiaaochen@gatech.edu; Zhehao Zhang:
hehao.zhang.gr@dartmouth.edu; Diyi Yang: diyiy@stanford.edu

∗∗ Contribution distributed as follows. Caleb, Will, and Diyi decided the project scope and research

questions. Caleb performed the CSS literature review, as well as the subject and task selection. Will built
the evaluation pipeline and prompting guidelines. Will, Caleb, and Omar all contributed data
pre-processing, loading, and evaluation scripts. Caleb ran the OpenAI and Flan-T5/UL2 prompt
perturbation experiments and few-shot experiments. Zhehao was responsible for all baseline
experiments. Caleb managed the human evaluations. All authors contributed to discussion, results, error
analysis, and paper writing.

Action editor: Vivek Srikumar. Submission received: 26 April 2023; revised version received: 29 August 2023;
accepted for publication: 25 October 2023.

© 2024 Association for Computational Linguistics

Computational Linguistics

Volume 50, Number 1

Figure 1
We assess the potential of LLMs as multi-purpose tools for CSS. We identify core subject areas in
prior CSS work and select 24 diverse and representative tasks from across these fields (top).
Then, we segment tasks into distinct discourse types and evaluate both open and closed-source
LLMs across this benchmark using zero-shot prompting (bottom).

Computational Social Science (CSS) (Lazer et al. 2020) was born from the immense
growth of human data traces on the web and the rapid acceleration of computational
resources for processing this data. These developments allowed researchers to study
language and behavior at an unprecedented scale (Lazer et al. 2009), with both global
and fine-grained observations (Golder and Macy 2014). From the early days of content
dictionaries (Stone, Dunphy, and Smith 1966), statistical text analysis facilitated CSS
research by providing structure to non-numeric data. Now, Large Language Models
(LLMs) may be poised to change the computational social science landscape by provid-
ing such capabilities without custom training data.

The goal of this work is to assess the degree to which LLMs can transform Com-
putational Social Science (CSS). Solid computational approaches are needed to help an-
alyze textual data and to understand a variety of social phenomena across academic
disciplines. Current CSS methodologies typically use supervised text classification and
generation in order to scale up manual labeling efforts to unseen texts (also called coding
in the social sciences). Reliable supervised methods typically demand an extensive
amount of human-annotated training data. Alternatively, unsupervised methods can
run “for free,” but the resulting output can be uninterpretable. In the status quo, data
resources constrain the theories and subjects CSS can be applied to.

LLMs have the potential to remove these constraints. Recent LLMs have demon-
strated the striking ability to reliably classify text, summarize documents, answer ques-
tions, and generate interpretable explanations in a variety of domains, even exceeding
human performance without the need for supervision (Bang et al. 2023; Qin et al. 2023;
Zhuo et al. 2023; Goyal, Li, and Durrett 2022). If LLMs can similarly provide reliable la-
bels and summary codes through zero-shot prompting, CSS research can be broadened
to a wider range of hypotheses than current tools and data resources support. Zero-
shot viability in this space is our primary research question. To effectively harness the
power of LLMs, behavioral researchers should understand the pros and cons of different
modeling decisions (model-selection), as well as how these decisions intersect with their
fields of specialization (domain-utility) and downstream use-cases (functionality). By

2

Literary ThemesNarrative AnalysisCharacter TropesRelationship DynamicsHistorical EventsEvent ExtractionSemantic ChangeSociolinguistic VariationSocial Language UseCultural EvolutionDialect Feature IdentificationFigurative LanguagePersuasion StrategiesDiscourse ActsSocial PsychMental HealthEmpathyPositive ReframingEmotion SummarizationEmotionHumorPolitenessPsychologyLiteratureHistoryLinguisticsPol. SciFramingIdeologyMisinformationEvent FramingStanceStatement IdeologyMedia SlantSociologySocial DynamicsPersuasivenessPowerPowerAnti-Social BehaviorToxicity PredictionHate SpeechCultural AnalysisFigurative Language ExplanationSocial Bias InferenceZero Shot Prompt FormattingLLMWhich of the following leanings would a political scientist say that the above article has?
A: Liberal
B: Conservative
C: Neutral Discourse TypesUtterancesConversationsDocumentsZiems, Held, Shaikh, Chen, Zhang, Yang

Can LLMs Transform CSS?

evaluating LLMs on an extensive suite of CSS tasks, this work provides researchers a
roadmap with answers to the following research questions:

• (RQ1) Viability: Are LLMs able to augment the human annotation pipeline? Can

they match or exceed the reliability of human annotation?

• (RQ2) Model-Selection: How do different aspects of LLMs (e.g., model size,

pretraining) affect their performances on CSS tasks?

• (RQ3) Domain-Utility: Are zero-shot LLMs specially adapted for better results in

some fields of science rather than others?

• (RQ4) Functionality: Are zero-shot LLMs equipped to assist with labeling tasks

(classification) or summary-explanatory tasks (generation) or both?

The research pipeline in Figure 1 allows us to answer these questions. First, we
survey the social science literature to understand where LLMs could serve as ana-
lytical tools (§2). Then we operationalize each use-case with a set of representative
tasks (§3). Specifically, classification and parsing methods can help researchers code for
linguistic, psychological, and cultural categories (§3.1 - §3.3) while generative models
can explain underlying constructs (e.g., figurative language, emotional reactions, hate
speech, and misinformation), and restructure text according to established theories like
cognitive behavioral therapy (§3.4). With a final evaluation suite of 24 tasks, we test
the zero-shot performance of 13 language models with differing architectures, sizes,
pre-training, and fine-tuning paradigms (§5, §6). This allows us to suggest actionable
steps for social scientists interested in co-opting LLMs for research (§7). Specifically, we
suggest a blended supervised-unsupervised scheme for human-AI partnered labeling
and content analysis.

Concretely, our analysis reveals that, except in minority cases, prompted LLMs do
not match or exceed the performance of carefully fine-tuned classifiers, and the best
LLM performances are often too low to entirely replace human annotation. However,
LLMs can achieve fair levels of agreement with humans on labeling tasks (RQ1). These
results are not limited to a subset of academic fields, but rather span the social sciences
across a range of conversation, utterance, and document-level classification tasks (RQ2).
Furthermore, the benefits of LLMs are compounded as models scale up (RQ3). This
suggests that LLMs can augment the annotation process through iterative joint-labeling,
significantly speeding up and improving text analysis in the social sciences.

Importantly, some LLMs can also generate informative explanations for social sci-
ence constructs. Leading models can achieve parity with the quality of dataset refer-
ences, and can even exceed them in terms of relevance, coherence, faithfulness, and
fluency. Humans prefer model outputs 50% of the time, suggesting that human-AI
collaboration will extend beyond labeling tasks to the joint coding of new constructs,
analyses, and summaries.

2. An Overview of CSS

Following Lazer et al. (2020), we define Computational Social Science as the develop-
ment and application of computational methods to the scientific analysis of behavioral
and linguistic data. Critically, CSS centers around the scientific method, forming and
testing broad and objective hypotheses, while similar efforts in the Digital Humanities
(DH) focus more on the subjectivity and particularity of events, dialogues, cultures,
laws, value-systems, and human activities (Dobson 2019).

This section surveys the current needs of researchers in both the computational
social sciences and digital humanities. We choose to merge our discussion under the

3

Computational Linguistics

Volume 50, Number 1

banner of CSS, since solid computational approaches are needed to help analyze textual
data and to understand a variety of socio-behavioral phenomena across both scientific
and humanistic disciplines. We focus primarily on the most tractable text classification,
structured parsing, summarization, and natural language generation tasks for CSS.
Some other techniques like aggregate mining of massive datasets or topic modeling
may be largely outside the scope of transformer-based language models, which have a
fixed processing window size and quadratic space complexity.

The following subsections outline how computational methods can support specific
fields of inquiry regarding how people think (psychology; §2.5), communicate (linguistics;
§2.3), establish governance and value-systems (political science, economics; §2.4), collec-
tively operate (sociology; §2.6), and create culture (literature, anthropology; §2.2) across
time (history; §2.1).

2.1 History

Historians study events, or transitions between states (Box-Steffensmeier and Jones 2004;
Abbott 1990), like the onset of a war. Event extraction is a parsing task from unstruc-
tured text to more regular data structures which capture the location, time, cause, and
participants in the event (Xiang and Wang 2019). This task, which is central to a growing
number of computational studies on history (Lai et al. 2021; Sprugnoli and Tonelli 2019),
can be broken into (1) event detection, and (2) event argument extraction, which we
benchmark in §3.3.1 and §3.3.2 respectively. Historians also work to understand the
influence of events on historical shifts in discourse (DiMaggio, Nag, and Blei 2013)
and meaning (Hamilton, Leskovec, and Jurafsky 2016a). We further discuss NLP for
discourse and semantic change in §2.4 and §2.3.

2.2 Literature

Literary studies are closely tied to the analysis of themes (Jockers and Mimno 2013), set-
tings (Piper, So, and Bamman 2021), and narratives (Sap et al. 2022; Saldias and Roy 2020;
Boyd, Blackburn, and Pennebaker 2020). Settings can be identified using named entity
recognition (Brooke, Hammond, and Baldwin 2016) and toponym resolution (DeLozier
et al. 2016), which are already demonstrably solved by prompted models like GPT 3.5
Turbo (Qin et al. 2023). Themes are typically the subject of topic modeling, which is
outside the scope of LLMs. Instead we focus on NLP for narrative analysis. NLP systems
can be used to parse narratives into chains (Chambers and Jurafsky 2008) with agents
(Coll Ardanuy et al. 2020; Vala et al. 2015) their relationships (Labatut and Bost 2019; Iyyer
et al. 2016; Srivastava, Chaturvedi, and Mitchell 2016), and the events (Sims, Park, and
Bamman 2019) they participate in. We cover social role labeling and event extraction
methods in §3.3.4 and §3.3.2 respectively. Researchers can also study agents in terms
of their power dynamics (Sap et al. 2017) and emotions (Brahman and Chaturvedi 2020),
which we benchmark in §3.2.4 and §3.1.2. Figurative language (Kesarwani et al. 2017) and
humor classification (Davies 2017) are two other relevant tasks for the study of literary
devices, and we evaluate these tasks in §3.1.3 and §3.1.5.

2.3 Linguistics

Computational sociolinguists use computational tools to measure the interactions be-
tween society and language, including the stylistic and structural features that dis-
tinguish speakers (Nguyen et al. 2016). Language variation is closely related to social

4

Ziems, Held, Shaikh, Chen, Zhang, Yang

Can LLMs Transform CSS?

identity (Bucholtz and Hall 2005), from group membership (Del Tredici and Fernández
2017), geographical region (Purschke and Hovy 2019), and social class (Preo¸tiuc-Pietro,
Lampos, and Aletras 2015; Del Tredici and Fernández 2017) to personal attributes like
age and gender (Bamman, Eisenstein, and Schnoebelen 2014). In §3.1.1 and §3.1.10, we
use LLMs to identify the structural features of English dialects, which linguists can
use to classify and systematically study dialects, measure different feature densities
in different population strata, and study the onset and diffusion of language change
(Kershaw, Rowe, and Stacey 2016; Eisenstein et al. 2014; Ryskina et al. 2020; Kulkarni
et al. 2015; Hamilton, Leskovec, and Jurafsky 2016b; Carlo, Bianchi, and Palmonari 2019;
Zhu and Jurgens 2021b; Schlechtweg et al. 2020).

2.4 Political Science

Political scientists study how political actors move agendas (Grimmer 2010) by per-
suasively framing their discourse “to promote a particular problem definition, causal
interpretation, moral evaluation, and/or treatment recommendation” (Entman 1993).
These agendas cohere within ideologies. Computational social scientists have advanced
political science through the detection of political leaning, ideology, belief, and stance
(Ahmed and Xing 2010; Baly et al. 2020; Bamman and Smith 2015; Iyyer et al. 2014;
Johnson, Lee, and Goldwasser 2017; Preo¸tiuc-Pietro et al. 2017; Luo, Card, and Jurafsky
2020a; Stefanov et al. 2020), as well as issue (Iyengar 1990) and entity framing (van den
Berg et al. 2020). Applications for persuasion, framing, ideology, and stance detection
in the social sciences are numerous. Analysts can uncover fringe issue topics (Bail 2014)
and frames (Ziems and Yang 2021; Mendelsohn, Budak, and Jurgens 2021; Demszky
et al. 2019; Field et al. 2018), with applications to public opinion (Bhatia 2017; Garg
et al. 2018; Kozlowski, Taddy, and Evans 2019; Abul-Fottouh and Fetner 2018), voting
behavior (Black et al. 2011), policy change (Flores 2017), social movements (Nelson 2021;
Sech et al. 2020; Rogers, Kovaleva, and Rumshisky 2019; Tufekci and Wilson 2012),
and international relations (King and Lowe 2003). We benchmark ideology detection in
§3.1.6 and §3.3.3, stance detection in §3.1.9, and entity framing in §3.3.4. Furthermore,
understanding the discourse structure and persuasive elements of political speech can
help social scientists measure political impact (Altikriti 2016; Hashim and Safwat 2015).
We benchmark persuasion strategy and discourse acts classification in §3.1.8 and §3.2.1.

2.5 Psychology

As the science of mind and behavior, psychology intersects all other adjacent social
sciences in this section. For example, an individual’s personality, or their stable pat-
terns of thought and behavior across time, will correlate with their political leaning
(Gerber et al. 2010), social status (Anderson et al. 2001), and linguistic expression
(Pennebaker and King 1999). The most influential personality modeling benchmark,
MyPersonality (Kosinski, Stillwell, and Graepel 2013), is no longer available, but in
this work, we evaluate on a representative set of psychological factors down-stream
of personality. For example, differences in personality and cognitive processing can
impact what people find funny (Martin and Ford 2018) or persuasive (Hirsh, Kang,
and Bodenhausen 2012). These psychological factors then exert influence over a range
of social interactions. Humor and politeness (Brown and Levinson 1987) are correlated
with subjective impressions of psychological distance between speakers (Trope and
Liberman 2010), while persuasive techniques bind agents in social commitments, with
applications in the science of management and organizations. We evaluate on humor,

5

Computational Linguistics

Volume 50, Number 1

persuasion, and politeness classification in §3.1.5, §3.1.8, and §3.2.6 respectively. We
also consider LLMs as tools for counseling, mental health and positive psychology in
text-based interactions. Specifically, we evaluate on empathy detection in online mental
health platforms (Sharma et al. 2020) in §3.2.2, emotional aspect-based summarization in
§3.4.1 ,and a positive reframing style-transfer task (Ziems et al. 2022) based on cognitive
behavioral therapy in §3.4.5.

2.6 Sociology

Sociologists want to understand the structure of society and how people live collectively
in social groups (Wardhaugh and Fuller 2021; Keuschnigg, Lovsjö, and Hedström 2018).
By tracing the diffusion and recombination of linguistic, political, and psychological
content between actors in a community across time, sociologists can begin to under-
stand social processes at both the micro and macro scale. At the micro scale, there is
the computational sociology of power (Danescu-Niculescu-Mizil et al. 2012; Bramsen
et al. 2011; Prabhakaran, Reid, and Rambow 2014; Prabhakaran, Rambow, and Diab
2012) and social roles (Welser et al. 2011; Fazeen, Dantu, and Guturu 2011; Zhang, Tang,
and Li 2007; Yang, Wen, and Rosé 2015; Maki et al. 2017). LLMs can assist sociological
research by predicting power relations (§3.2.4) and unhealthy conversations (§3.2.5).
At the macro-scale, there are computational analyses of social norms and conventions
(Centola et al. 2018; Bicchieri 2005), information diffusion (Leskovec, Backstrom, and
Kleinberg 2009; Tan, Lee, and Pang 2014; Vosoughi, Roy, and Aral 2018; Cheng et al.
2016), emotional contagion (Bail 2016), collective behaviors (Barberá et al. 2015), and
social movements (Nelson 2021, 2015). Again, LLMs can detect constructs like emotion
(§3.1.2) and the speech of hateful social groups (§3.1.4). Furthermore, social movements
rely on the diffusion of norms and idiomatic slogans, which carry meaning through
figurative language that LLMs can decode (§3.1.3).

3. Representative CSS Task Selection

While not exhaustive, our task selection is designed to provide a representative survey
of the CSS needs in §2. This will allow us to answer Research Questions 1-4, which are
pertinent to social science researchers. Thus our work is distinct and complementary to
BIG-Bench (Srivastava et al. 2023) and other efforts to benchmark the logical, physical,
and social reasoning capabilities of LLMs. Our attention is more carefully focused on the
affordances of LLMs for social science.1Our tasks are field-specific and come with the
field-specific challenges of expert taxonomies, large label spaces, temporal grounding,
and domain-specific parsing schemes (see §7.6).

To help answer RQ3 and 4, we organize this section according to our division
of tasks into functional categories based on the unit of text analysis: 10 utterance-
level classification tasks (§3.1), 6 conversation-level tasks (§3.2), and 4 document-level
tasks for the analysis of media (§3.3). In addition to these 20 classification tasks, we
evaluate 5 generation tasks in §3.4 for explaining social science constructs and applying
psychological theories to restructure text.

1 To elaborate, BIG-Bench, among its 200 tasks, has some overlap in figurative language, humor, emotion,
empathy, and toxicity detection, but it does not cover dialect, discourse relations, character tropes, event
detection, ideology, misinformation, persuasion, politeness, power relations, semantic change, or stance.
BIG-Bench covers few document-level analyses and no conversation-level analysis. We are the first to run
extensive experiments to understand patterns of LLM performance on tasks critical to social scientists.

6

Ziems, Held, Shaikh, Chen, Zhang, Yang

Can LLMs Transform CSS?

3.1 Utterance-Level Classification

An utterance is a unit of communication produced by a single speaker to convey a single
subject, which may span multiple sentences (Bakhtin 2010). CSS researchers can use
utterance data to study linguistic phenomena like the syntax of dialect, the semantics of
figurative language, or the pragmatics of humor. Utterance-level analysis also reflects
human states like emotion and communicative intent, or stable traits like stance and
ideology (Evans and Aceves 2016). We evaluate LLMs on utterance classification tasks
for dialect, hate speech, figurative language, emotion, humor, misinformation, ideology,
persuasion, semantic change, and stance classification.

3.1.1 Dialect Features. Linguistic feature detection is critical to the study of dialects
(Eisenstein, Smith, and Xing 2011) and ideolects (Zhu and Jurgens 2021a), with numer-
ous applications in sociolinguistics, education, and the sociology of class and commu-
nity membership (see §2.3). These features can be used to study the sociolinguistics of
language change (Kulkarni et al. 2015; Hamilton, Leskovec, and Jurafsky 2016b) or the
linguistic biases in educational assessments (Craig and Washington 2002) and online
moderation (Sap et al. 2019). The utterance is an appropriate level of analysis here
because syntactic and morphological features are all defined on subtrees of the sentence
node (Ziems et al. 2023; Eisenstein et al. 2023).

We evaluate on the Indian English dialect feature detection task of Demszky et al.
(2021) because this is one of the only available datasets to be hand-labeled by a domain
expert. Additionally, Indian English is the most widely-spoken low-resource variety of
English, so the domain is representative. The task is to map utterances to a set of 22
grammatical features: i.e., a lack of inversion in wh-questions, the omission of copula
be, or features related to tense and aspect like the habitual progressive, found in Indian
varieties of English. For example, the sentence “Two years I stayed alone” exemplifies
Preposition Omission.

3.1.2 Emotions. Emotion detection, the cornerstone of affective computing (Picard 2000),
is highly relevant to psychology and political science, among other disciplines, since sta-
ble emotional patterns in-part define an individual’s personality, and targeted emotions
outline the political stances she has. Additional application domains for the task include
emotional contagion (Bail 2016) and human factors behind economic markets (Bollen,
Mao, and Zeng 2011; Nguyen and Shirai 2015).

Expert-labeled emotion detection datasets are not common. We evaluate emotion
detection with weakly labeled Twitter data from Saravia et al. (2018), which uses
Plutchik’s 8 emotional categories: anger, anticipation, disgust, fear, joy, sadness, surprise,
and trust. For example, the following sentence would express fear:

I started the steroids on Saturday and I had some really bad side effects, like my eyes
started feeling weird.

Plutchik’s model is one of the three most recognized discrete emotion models, and it is
also used in our later Emotion Summarization Task (§3.4.1).

3.1.3 Figurative Language. Figurative expressions are where the speaker meaning dif-
fers from the utterance’s literal meaning. Recognizing figurative language is a first
step in understanding literary content (Jacobs and Kinder 2018) and political texts

7

Computational Linguistics

Volume 50, Number 1

(Huguet Cabot et al. 2020), detecting hate speech (Lemmens, Markov, and Daelemans
2021) and identifying mental health self-disclosure (Iyer et al. 2019).

We use the FLUTE (Chakrabarty et al. 2022) benchmark because it is, at this time, the
most comprehensive, with examples from many prior datasets (Chakrabarty et al. 2021;
Srivastava et al. 2023; Stowe, Utama, and Gurevych 2022). FLUTE contains 9k premise
sentences, each paired to a hypothesis with figurative language:

premise: I said, work independently and come up with some plans.

hypothesis: I said, put your heads together and come up with some plans.

The classification task is to recognize whether the figurative sentence contains
(1) sarcasm (Joshi, Bhattacharyya, and Carman 2017), (2) simile (Niculae and Danescu-
Niculescu-Mizil 2014), (3) metaphor (Gao et al. 2018), or (4) an idiom (Jochim et al. 2018).
In the above example, the hypothesis contains the idiom “put your heads together.”

3.1.4 Hate Speech. Hate speech is language that disparages a person or group on the
basis of protected characteristics like race. Beyond the societal importance of detecting
and mitigating hate speech, this is a category of language that is salient to many social
scientists. By not only detecting, but also systematically understanding hate speech, po-
litical scientists can track the rise of hateful ideologies, and sociologists can understand
how these hateful ideas diffuse through a network and influence social movements.

Thus we evaluate on the more nuanced task of fine-grained hate speech taxonomy
classification from Latent Hatred (ElSherief et al. 2021). This task requires models to
infer a subtle social taxonomy from the coded or indirect speech of U.S. hate groups.
Utterances should be classified with one of six domain-specific categories: incitement to
violence, inferiority language, irony, stereotypes and misinformation, threatening and intimi-
dation language, and white grievance. For example, the following sentence contains white
grievance: “jewish harvard professor noel ignatiev wants to abolish the white race.”

3.1.5 Humor. Humor is a rhetorical (Markiewicz 1974) and literary device (Kuipers 2009)
that modulates social distance and trust (Sherman 1988; Graham 1995; Kim, Lee, and
Wong 2016). However, different audiences may perceive the same joke differently. In the
study of sociocultural variation, communication, and bonding, humor detection will be
of prime interest to sociologists and social psychologists, as well as to literary theorists
and historians. Computational social scientists have effectively detected punchlines
(Mihalcea and Strapparava 2005; Ofer and Shahaf 2022) and predicted audience laugh-
ter (Chen and Soo 2018), demonstrating the computational tractability of the domain.

Our evaluation uses a popular dataset from Weller and Seppi (2019) to focus on
binary humor detection across a wide range of joke sources, from Reddit’s r/Jokes, a
Pun of The Day website, and a set of short jokes from Kaggle, summing to ∼16K jokes.

3.1.6 Ideology. A speaker’s subtle decisions in word choice and diction can betray their
beliefs and the political environment to which they belong (Jelveh, Kogut, and Naidu
2014). While political scientists care most about identifying the underlying ideologies
and partisan organizations behind these actors (§2.4), sociolinguists can study the cor-
relation between language and social factors.

We evaluate ideology detection on the Ideological Books Corpus (Gross et al. 2013)
from Iyyer et al. (2014), which contains 2,025 liberal sentences, 1,701 conservative sen-
tences, and 600 neutral sentences. The corpus was designed to disentangle a speaker’s

8

Ziems, Held, Shaikh, Chen, Zhang, Yang

Can LLMs Transform CSS?

overall partisanship from the particular ideological beliefs that are reflected in an indi-
vidual utterance. Thus labels reflect perceived ideology according to annotators and not
the speaker’s ground truth partisan affiliation. For example, one sentence associated
with a strongly conservative ideology is: “the feminist movement, with its mockery of mar-
riage and demands for absolute sexual freedom... was a frontal assault on the meritocracy and
the traditional family.”

3.1.7 Misinformation. Misinformation is both a political and social concern as it can
jeopardize democratic elections, public health, and economic markets. The effort to
combat misinformation is multi-disciplinary (Lazer et al. 2018), and it depends on
reliable misinformation detection tools.

We evaluate on the Misinfo Reaction Frames corpus (Gabriel et al. 2022), a dataset of
25k news headlines with fact checked labels for the accuracy of the related news articles
about COVID-19, climate change, or cancer. Models perform binary misinformation
classification on news article headlines alone, which the authors found was a tractable
task for fine-tuned models. For example, an article with the headline “White House Ousts
Top Climate Change Official” is marked as likely to contain misinformation.

3.1.8 Persuasion. Persuasion is the art of changing or reinforcing the beliefs of others.
Understanding persuasive strategies is central to behavioral economics and the psychol-
ogy of advertising and propaganda (Martino et al. 2020). Utterances are a natural unit
for the analysis of individual persuasive strategies, which may be combined in dialogue
for an overall persuasive effect (c.f. §3.2.3).

While multi-modal persuasion detection tasks exist, we focus on the popular text-
based persuasion dataset, Random Acts of Pizza (RAOP; Althoff, Danescu-Niculescu-
Mizil, and Jurafsky 2014), where Reddit users attempt to convince community members
to give them free food. This dataset was labeled by Yang et al. (2019a) with a fine-grained
persuasive strategy taxonomy based on Cialdini (2003) that includes Evidence, Impact,
Politeness, Reciprocity, Scarcity, and Emotion. The task objective is to classify utterance-
level RAOP requests according to this 6-class taxonomy. An example of an Evidence
sentence is “There is a Pizza Hut and a Dominos near me," since it provides concrete facts
relevant to the request. An example of Scarcity is “I haven’t had a meal in two days.”

3.1.9 Stance. Although stance detection can be formalized in different ways, the most
common task design is for models to determine whether a text’s author is in favor
of a target view, against the target, or neither. With this formulation, sociologists can
understand consensus and disagreement in social groups, psychologists can measure
interpersonal attachments, network scientists can build signed social graphs, political
scientists can track the views of a voter base or the policies of candidates, historians
can plot shifting opinions, and digital humanities researchers can quickly summarize
narratives via character intentions and goals.

We evaluate stance detection on the earliest and most established SemEval-2016
Stance Dataset (Mohammad et al. 2016), which contains 1,250 tweets and their asso-
ciated stance towards six topics: atheism, climate change, the feminist movement, Hillary
Clinton, Donald Trump and the legalization of abortion. Stance is given as favor, against, or
none. For zero-shot experiments, we use the test set where the target is Donald Trump
for all evaluations. An example tweet against Donald Trump is as follows:

@realDonaldTrump needs to learn when to stop talking. You are making it worse
Donald... so much worse.

9

Computational Linguistics

Volume 50, Number 1

3.1.10 Semantic Change. In addition to its more stable features, researchers can plot
the change of language over time for a fixed community. Semantic change detection
can serve as a proxy measure for the spread and change of culture (Kirby, Dowman,
and Griffiths 2007), both on the internet (Eisenstein 2012; Eisenstein et al. 2014) and in
historical archives (Mihalcea and Nastase 2012; Kim et al. 2014; Kulkarni et al. 2015;
Rudolph and Blei 2018)2.

We evaluate LLMs as binary word-sense discriminators using the popular Temporal
Word-in-Context benchmark (TempoWiC; Pilehvar and Camacho-Collados 2019). Tem-
poWiC measures the core capability of drawing discrete boundaries between word-level
semantics. Given two sentences with the same lexeme, the task is binary classification
with positive indicating both sentences use the same sense of the word and negative
indicating different senses of the word. For example, consider the different senses of the
word ‘impostor’ in the following texts.

text1: Having a rough start to my doctorate program in both the student and teacher
roles and feel down and ashamed. I spoke to faculty and know how to move forward,
but while they believe in me I find it hard to believe in myself. How do you fight
impostor syndrome @AcademicChatter

text2: laughed so hard running from impostor friend around the lab table that I gave
myself an headache lmao what a good day

A perfect classifier for this task can be used to cluster all usage of a surface-form into
sense groups using pairwise comparison.

3.2 Conversation-Level Classification

Conversations are multi-party exchanges of utterances. They are critical units for analy-
sis in the social sciences (Hutchby and Wooffitt 2008; Silverman 1998; Sacks 1992), since
they richly reflect social relationships (Evans and Aceves 2016) — a key factor that was
missing in utterance-level analysis. Sociological frameworks like ethnomethodology
(Garfinkel 2016) focus particularly on conversations. The tasks in this section are drawn
largely from the ConvoKit toolkit of Chang et al. (2020).

3.2.1 Discourse Acts. Discourse acts are the building blocks of conversations and are
thus relevant to conversation analysis in sociology, genre analysis in literature, prag-
matics, and ethnographic studies of speech communities (see Paltridge and Burton for
example). Some popular discourse act taxonomies like DAMSL (Stolcke et al. 2000) and
DiAML (Bunt et al. 2010) can have as many as 40 categories, tailored to spoken commu-
nication. We use Zhang, Culbertson, and Paritosh (2017)’s simpler and more focused
9-class taxonomy since it was designed to cover online text conversations—the focus
of CSS research. The taxonomy includes questions, answers, elaborations, announcements,
appreciation, agreements, disagreements, negative reactions, and humor.

We evaluate on the Coarse Discourse Sequence Corpus (Zhang, Culbertson, and
Paritosh 2017). The model input is a comment from a Reddit thread, along with the
utterance to which the comment is responding. For example,

2 Additional works in this area can be found under the Workshop on Computational Approaches to

Historical Language Change

10

Ziems, Held, Shaikh, Chen, Zhang, Yang

Can LLMs Transform CSS?

[userABC]: So i went thinking to myself this fine day ¨hey lets check out Levetihanänd
then i found out that this DLC does not appear in my Origin store...

[userXYZ]: Did you go into ME3 game and access ¨downloadable content¨?

The expected output is the category from the above 9-class taxonomy which best de-
scribes the comment’s speech act: Question in the above example.. Since Announcements
and Negative reactions have fewer than 10 examples total in the dataset, they are omitted
from our evaluation along with the catch-all Other category.

3.2.2 Empathy. Since the early days of internet access, users have looked to internet com-
munities for support (Preece 1998). Thus web communities can provide CSS researchers
with empathetic communication data in naturalistic settings (Pfeil and Zaphiris 2007;
Sharma et al. 2020). By better understanding community-specific affordances (Zhou
and Jurgens 2020) and the most common triggers for empathetic responses (Buechel
et al. 2018; Omitaomu et al. 2022), CSS can reciprocally inform the design of empathetic
communities (Coulton et al. 2014; Taylor et al. 2019), as well as community-specific tools
like counseling dialogue systems (Sharma et al. 2021; Ma et al. 2020).

Understanding is the first step towards building more effective online mental
health resources, and this motivates our evaluation on the TalkLife dataset of Sharma
et al. (2020), a clinically-motivated empathy detection dataset. The paper’s EPITOME
measures empathy using a multi-stage labeling scheme. First, a listener communicates
an Emotional Reaction to describe how the seeker’s disclosure makes the listener feel.
Then the listener offers an Interpretation of the emotions the seeker is experiencing.
Finally, the listener moves into Exploration, or the pursuit of further information to
better understand the seeker’s situation. Clinical psychologists labeled the listener’s
effectiveness at each stage of a listener’s top-level reply. Here we focus on Exploration, as
prior work has shown open-questions to be especially effective for peer-support (Shah
et al. 2022). Given a seeker’s post and a top-level listener’s reply, we classify whether the
listener offered: Strong Exploration (specific questions about the seekers situation), Weak
Exploration (general questions), or No Exploration. Consider the example conversation:

Seeker: I spent today either staring blankly at a computer screen or my phone. Was too
hurt to do anything today, really.

Response: I wish I even had the will to play games. For me it’s excessive daydreaming.

The above response is an example of No exploration.

3.2.3 Persuasion. In §3.2.3, we considered utterance-level analysis of fine-grained per-
suasive strategies. However, social scientists are also interested in the overall persuasive
effect that one speaker has on another through sequences of rhetorical strategies in
dialogue (Shaikh et al. 2020). Persuasive outcomes are particularly important for the
political science of successful campaigns (Murphy and Shleifer 2004) and the sociology
of idea propagation and social movements (Stewart, Smith, and Denton Jr 2012).

We evaluate our persuasion prediction task on the Winning Arguments Corpus (Tan
et al. 2016), which contains 3,051 conversations from r/ChangeMyView in which the
persuader tries to convince the persuadee to change their mind. Models receive as input
the reply thread (starting from a top-level comment) and perform binary prediction on
whether the persuadee awarded the persuader a ‘delta’ for a successful argument: If

11

Computational Linguistics

Volume 50, Number 1

you were the original poster, would this reply convince you? Consider this example of
an unsuccessful argument by UserA below:

[UserA]: “Right on red”, when it’s allowed, is primarily because you’re going from the
innermost lane TO the intersecting innermost lane... this part of the state is infamous
for a**hat drivers blocking people from turning, changing lanes, etc... could you
imagine the chaos? :D

[UserB]: Er, the image I posted, I found on Google images. It may triple the number of
lanes to be concerned about, but one of them shouldn’t usually be a problem if people
stay in their lanes. And the other two, you still have to look in the same direction."

3.2.4 Power and Status. Sociologists, political scientists, and online communities re-
searchers are interested in understanding hierarchical organizations, social roles, and
power relationships. Power is related to control of the conversation (Prabhakaran, Reid,
and Rambow 2014) and power dynamics shape both behavior and communication.
Specifically, text analysis can uncover power relationships in the degree to which one
speaker accommodates to the linguistic style of another (Danescu-Niculescu-Mizil et al.
2012). We anticipate that this task is tractable for LLMs.

We evaluate on the Wikipedia Talk Pages dataset from Danescu-Niculescu-Mizil
et al. (2012). Conversations are drawn from the debate forums regarding Wikipedia edit
histories, and power is a binary label describing whether or not the Wikipedia editor is
an administrator. All models are given an editor’s entire comment history from the Talk
Pages, and the objective is binary classification. In the following example, EditorA uses
a high degree of politeness and hedging langauge, which indicates that he is not in a
position of power:

[EditorA]: That’s odd. Somehow, I came across one of that user’s edits, though I believe
it was on recent changes. As you can see, most of the older edits are vandalism, but I
guess due to the time that wouldn’t warrant much of a block. I don’t know how I
happened to come across that since it’s so old.

[EditorA]: That could be the case. I’ve seen a few of those tonight.

3.2.5 Toxicity Prediction. Toxicity is a major area of social research in online com-
munities, as online disinhibition (Suler 2005) makes antisocial behaviour especially
prevalent (Cheng, Danescu-Niculescu-Mizil, and Leskovec 2015). Predictive models can
be used to understand the early signs of later toxicity (Cheng et al. 2017) for downstream
causal analysis on the evolution of toxicity (Mathew et al. 2020) and the effectiveness of
intervention methods (Kwak, Blackburn, and Han 2015). Even without interpretable
features, a predictive system can serve causal methods as a propensity score.

Using the Conversations Gone Awry corpus (Zhang et al. 2018), we investigate
whether LLMs can predict future toxicity from early cues. As context, the model takes
the first two messages in a conversation between Wikipedia users. The model should
make a binary prediction whether or not the Wikipedia conversation will contain toxic
language at any later stage. For example:

[UserA]: I have removed recent edition of pappe to the lead though Pappe view might
notable currently without attribution and proper context of other views it WP:NPOV
violation.

[UserB]: In fact, Pappe is already mentioned twice in the proper place.

12

Ziems, Held, Shaikh, Chen, Zhang, Yang

Can LLMs Transform CSS?

The conversation above contains overt confrontation that will later devolve into toxicity.

3.2.6 Politeness. Before overt toxicity is evident in a community, researchers can mea-
sure its health and stability according to members’ adherence to politeness norms. Polite
members can help communities grow and retain other valuable members (Burke and
Kraut 2008), while rampant impoliteness in a community can foreshadow impending
toxicity (Andersson and Pearson 1999). Text-based politeness measures also reflect other
societal factors that we explore in this work, like gender bias (Herring 1994; Ortu
et al. 2016, §3.1.4), power inequality (Danescu-Niculescu-Mizil et al. 2013, §3.2.4), and
persuasion (Shaikh et al. 2020, §3.1.8).

We evaluate on the Stanford Politeness Corpus (Danescu-Niculescu-Mizil et al.
2013). The dataset is foundational in the computational study of politeness and its
relation to other social dynamics. The corpus contains requests made by one Wikipedia
contributor to another. For example,

I am looking for help improving the dermatology content on Wikipedia. Would you be
willing to help, or do you have any friends interested...

Each request is classified into one of three categories, Polite, Neutral, or Impolite, accord-
ing to Mechanical Turk annotators’ interpretation of workplace norms (the example
above is Polite). High zero-shot performance on this task will strongly indicate a model’s
broader ability to recognize conversational social norms.

3.3 Document-Level Classification

Documents provide a complementary view for social science. Like conversations, doc-
uments can encode sequences of ideas or temporal events, as well as interpersonal
relationships not present in isolated utterances. Unlike the dyadic communication of
a conversation, a document can be analyzed under a unified narrative (Piper, So, and
Bamman 2021). Thus for our purposes, a document is a collection of utterances that
form a single narrative. Our document-level classification tasks cluster around media,
which has been the subject of content analysis in the social sciences since the time of
Max Weber in 1910. In this section, we focus on computational tools for content analysis
(Berelson 1952) to code media documents for their underlying ideological content (§3.3.3),
the events they portray (§3.3.1, §3.3.2), as well as the agents involved and the specific roles
or character tropes they exhibit (§3.3.4).

3.3.1 Event Detection. Following a massive effort to digitize critical documents, social
scientists depend on event extraction to automatically code and organize these docu-
ments into smaller and more manageable units for analysis. Events are the “building
blocks” from which historians construct theories about the past (Sprugnoli and Tonelli
2019); they are the backbone of narrative structure (Chambers and Jurafsky 2008). Event
detection is the first step in the event extraction pipeline. Hippocorpus (Sap et al. 2020b)
is a resource of 6,854 stories that were collected from crowdworkers and tagged for
sentence-level events (Sap et al. 2022) . Events can be further classified into minor or
major events, as well as expected or unexpected. We evaluate on the simplest task:
binary event classification at the sentence level. For example:

A: Four months ago, I had a big family reunion.
B: We haven’t had one in over 20 years.

13

Computational Linguistics

Volume 50, Number 1

C: This was a very exciting event.
D: I saw my Grandma who said I liked great as ever.

The above lines A and D denote new events.

3.3.2 Event Argument Extraction. Where event detection was concerned with identify-
ing event triggers, event argument extraction is the task of filling out an event template
according to a predefined ontology, identifying all related concepts like participants in
the event, and parsing their roles. Historians, political scientists, and sociologists can use
such tools to extract arguments from sociopolitical events in the news and historical text
documents, and to understand social movements (Hürriyeto ˘glu et al. 2021). Economists
can use event argument extraction to measure socioeconomic indicators like the unem-
ployment rate, market volatility, and economic policy uncertainty (Min and Zhao 2019).
Event argument extraction is also a key feature of narrative analysis (Sims, Park, and
Bamman 2019), as well as in the wider domains of legal studies (Shen et al. 2020), public
health (Jenhani, Gouider, and Said 2016), and policy.

WikiEvents (Li, Ji, and Han 2021) is a document-level event extraction benchmark
for news articles that were linked from English Wikipedia articles. WikiEvents uses
DARPA’s KAIROS ontology with 67 event types in a three-level hierarchy. For example,
the Movement.Transportation event has the agentless Motion subcategory and an
agentive Bringing subcategory. Both include a Passenger, Vehicle, Origin, and
Destination argument, but only the agentive Bringing has a Transporter agent.
KAIROS’s event argument ontology is richer and more versatile than the commonly
used ACE ontology, which only has 33 types of events. An example of this task is to
take the following document

The Taliban <tgr>killed <tgr>more than 100 members of the Afghan security forces
inside a military compound in central Maidan Wardak province on Monda...

and produce the following structured output

{’Victim’: ’members’, ’Place’: ’undefined’, ’Killer’: ’The Taliban’,

(cid:44)→ ’MedicalIssue’: ’undefined’}

3.3.3 Ideology. CSS is extremely useful for understanding and quantifying real and
perceived political differences. For a variety of specific phenomena (Amber et al. 2013;
Baly et al. 2018; Roy and Goldwasser 2020; Luo, Card, and Jurafsky 2020b; Ziems and
Yang 2021), this takes the form of gathering articles from across the political spectrum,
processing each one further for a phenomenon of interest, and evaluating the relative
differences for the articles from different ideological groups. The first step in such stud-
ies is to separate articles according to the overarching political ideology they represent.
We evaluate ideology detection on the Article Bias Corpus from Baly et al. (2020),
which collects a set of articles from media sources covering the United States of America
and labels them according to Left, Right, and Centrist political bias. Unlike the task of
utterance-level ideology prediction (§3.1.6), this task provides an entire news article as
context. This tests the ability of the model to understand the relationship that a sequence
of stances taken across an entire article might have with political leaning. For example,
one Left-leaning article in this dataset contains the strongly-indicative phrase: “it was
hard not to think about the insularity and cossetting the super-wealthy enjoy,” and then goes
on to talk at length about former LA Clippers owner Donald Sterling. In other articles,

14

Ziems, Held, Shaikh, Chen, Zhang, Yang

Can LLMs Transform CSS?

political views are more diffuse and less starkly concentrated into particular phrases
or slogans. Still, each article must be classified into exactly one of the three ideological
categories above.

3.3.4 Roles and Tropes. Social roles are defined by expectations for behavior, based on
social interaction patterns (Yang et al. 2019b). Similarly, personas are simplified models
of personality (Grudin 2006), like a trope that a character identifies within a movie. The
ability to infer social roles and personas from text has immediate applications in the
psychology of personality, the sociology of group dynamics, and the study of agents
in literature and film. These insights can help us understand stereotypical biases and
representational harms in media (Blodgett et al. 2020). Downstream applications also
include narrative psychology (Murray et al. 2015), economics, political polarization, and
mental health (Piper, So, and Bamman 2021).

Others have considered character role labeling for narratives (Jahan, Mittal, and
Finlayson 2021) and news media (Gomez-Zara, Boon, and Birnbaum 2018). We evaluate
this task with the CMU Movie Corpus dataset from Bamman, O’Connor, and Smith
(2013) as it was extended and modified by Chu, Vijayaraghavan, and Roy (2018) to
include character trope labels and IMBD character quotes. The character trope classifica-
tion task involves identifying from a character’s quotes alone which of 72 movie tropes
that characters identity best fits; e.g., the coward or the casanova. The following example
quotations are from an absent-minded professor:

Now, THIS makes any fabric instantly impervious. Dirt proof, stain proof... Ouch! And
bullet proof! It’s still not perfected yet! It’s hell on the dry-cleaning bill.

This baby is the ultimate corrosive. I call it - DON’T TOUCH IT! - I call it
“hydrochloricdioxynucleocarbonium”. Well, the name needs work. But it’ll eat through
a Buick! OR -

3.4 Generation Tasks

Regarding RQ4 Functionality, we want to understand whether LLMs are best suited
to classify taxonomic social science constructs from text, or whether these models are
equally if not better suited for generative explanations and summaries. This section
describes our natural language generation tasks, where LLMs might be used to summa-
rize relevant aspects (§3.4.1), elucidate the hidden social meaning behind a text (§3.4.2
— §3.4.4) or implement social theory by stylistically restructuring an utterance (§3.4.5).

3.4.1 Emotion-Specific Summarization. Prior work has already demonstrated LLMs’
skill at generic summarization tasks (Goyal, Li, and Durrett 2022; Qin et al. 2023).
Here, we consider a more domain-specific task, aspect-based summarization. The key
idea of aspect-based summarization is that different elements of a document will be
relevant to different users. This is especially true for social scientists and other domain
specialists. For example, scientists who study population-level emotional responses to
crisis events will need to know not only which emotions are represented in text (i.e.,
emotion detection; §3.1.2), but also, in brief, what specific experiences triggered such
emotions. The scientist may not have highly focused queries like in QA tasks, but this
use still demands summaries about broad subtopics or themes (Ahuja et al. 2022).

15

Computational Linguistics

Volume 50, Number 1

We use the COVIDET dataset of Zhan et al. (2022), which contains 1,883 Reddit posts
from the COVID-19 pandemic. Given a post and one of Plutchik’s target emotions, the
task is to summarize from the post what triggered the author to feel the target emotion.

3.4.2 Figurative Language Explanation. Our interests in figurative language are covered
in §3.1.3, where we introduce the FLUTE dataset. FLUTE contains 9k (literal, figura-
tive) sentence pairs with either entailed or contradictory meanings. The goal of the
explanation task is to generate a sentence to explain the entailment or contradiction.
For example, the figurative sentence “she absorbed the knowledge” entails the literal
sentence “she mentally assimilated the knowledge” under the following explanation:
“to absorb something is to take it in and make it part of yourself.”

3.4.3 Implied Misinformation Explanation. Both scientific understanding and real-
world intervention strategies depend on more than black-box classification. This moti-
vates our implied statement generation task, which is specified in the Misinfo Reaction
Frames corpus (Gabriel et al. 2022) as covered in §3.1.7. Models take the headline of a
news article and generate the underlying meaning of the headline in plain English. This
is called the writer’s intent. Consider, for example, the misleading headline, “Wearing
a face mask to slow the spread of COVID-19 could cause Legionnaires’ disease.” Here, the
annotator wrote that the writer’s intent was to say “wearing masks is dangerous; people
shouldn’t wear masks.”

3.4.4 Social Bias Inference. While hate speech detection focuses on the overall harmful-
ness of an utterance, specific types of hate speech are targeted towards a demographic
subgroup. To this end, the Social Bias Inference Corpus (SBIC; Sap et al. 2020a) consists
of 34K inferences, where hate speech is annotated with free-text explanations. Impor-
tantly, explanations highlight why a specific subgroup is targeted. For example, the
sentence “We shouldn’t lower our standards just to hire more women.” implies that “women
are less qualified.” To model these explanations, Sap et al. (2020a) treat the task as a
standard conditional generation problem. We mirror this setup to evaluate LLMs.

3.4.5 Positive Reframing. NLP can help scale mental health and psychological counsel-
ing services by training volunteer listeners and teaching individuals the techniques of
cognitive behavioral therapy (CBT; Rothbaum et al., 2000), which is used to address
mental filters and biases that perpetuate anxiety and depression. Positive reframing
is a sequence-to-sequence task which translates a distorted negative utterance into
a complementary positive viewpoint using CBT strategies without contradicting the
original speaker meaning. Take the example source sentence:

Always stressing and thinking about loads of things at once need I take it one at a time
overload stressed need to rant.

Using the growth and neutralizing strategies, the author can reframe this thought more
positively as follows:

Loads of things on my mind, I need to make a list, prioritise and work through it all
calmly and I will feel much better.

16

Ziems, Held, Shaikh, Chen, Zhang, Yang

Can LLMs Transform CSS?

4. Evaluation Methods

4.1 Model Selection and Baselines

Our goal is to evaluate LLMs in zero-shot settings through prompt engineering
(§4.2) and to identify suitable model architectures, sizes, and pre-training/fine-tuning
paradigms for CSS research (RQ 1,2). We choose FLAN-T5 (Chung et al. 2022) as
an open-source model with strong zero-shot and few-shot performance. Although it
follows a standard T5 encoder-decoder architecture, FLAN’s zero-shot performance
is due to its instruction fine-tuning over a diverse mixture of sequence to sequence
tasks. The added benefit is that FLAN-T5 checkpoints exist at six different sizes ranging
from small (80M parameters) to XXL (11B) and UL2 (20B), allowing us to investigate
scaling laws. Next, we consider OpenAI’s GPT-3 (Brown et al. 2020; Zong and Kr-
ishnamachari 2022) including text-001, text-002 learning with instructions and
text-003, which is further learned from human preferences (RLHF) (Christiano et al.
2017) series, and gpt-3.5-turbo (Qin et al. 2023; Gilardi, Alizadeh, and Kubli 2023),
which is the conversation-based LLM trained through RLHF (Christiano et al. 2017).
Finally we include GPT-4 (OpenAI 2023), which is a multimodal model that, at 1.7
trillion parameters, scales up the GPT-3 architecture by 1000×.

Traditional supervised fine-tuned models can serve as baselines for each task.
These baselines are intended to provide a comparison point for the utility of LLMs for
CSS, rather than providing a fair methodological comparison between approaches. For
classification tasks, we use RoBERTa-large (Liu et al. 2019) as the backbone model and
tune hyperparameters based on F1 score on the validation set. For generation tasks,
we use T5-base (Raffel et al. 2020) as the backbone model and tune hyperparameters
based on average BLEU score on the validation set. We use a grid search to find
the most suitable hyperparameters including learning rate {5e-6, 1e-5, 2e-5,
5e-5}, batch size {4, 8, 16, 32} and the number of epochs {1, 2, 3, 4}. Other
hyperparameters are set to the defaults defined by the HuggingFace Trainer. We average
results across three different random seeds to reduce variance. These baselines will
prove competitive in Table 3, matching or exceeding the best reported performances
from the original publications in Event Surprisal, Event Argument Extraction, and the clas-
sification of Emotions, Empathy, Figurative Language, Implicit Hate, Persuasion, Persuasion
Strategies, Political Ideology, and Semantic Change. Still, it is important to note that greater
performances might be achievable by fine-tuning alternative architectures.

4.2 Prompt Engineering

One strength of current LLMs is their ability to be "programmed" through natural lan-
guage instructions (Brown et al. 2020). This capability has been further improved by
training models to explicitly follow these instructions (Sanh et al.; Wang et al. 2022;
Chung et al. 2022; Ouyang et al. 2022). CSS tools can then be developed directly by
subject-matter experts using natural language instructions rather than explicit program-
ming language interpretations. In order to evaluate LLMs, each task requires a prompt
designed to elicit the desired behavior from the model.

The author who is most familiar with the task writes an initial prompt for it
based on the task description and the design guidelines below. Then we generate four
semantically equivalent perturbations of that prompt using gpt-3.5-turbo as a zero-
shot paraphrase model. All results are averaged across prompt perturbations to remove
instruction-based variance (Perez, Kiela, and Cho 2021; Zhao et al. 2021).

17

Computational Linguistics

Volume 50, Number 1

Effective Prompt Guideline

Reference

Guideline Example

When the answer is categorical, enumerate op-
tions as alphabetical multiple-choice so that the
output is simply the highest-probability token
(‘A’, ‘B’).

Each option should be separated by a new line
( ←(cid:45) ) to resemble the natural format of online
multiple choice questions. More natural prompts
will elicit more regular behavior.

To promote instruction-following, give instruc-
tions after the context is provided; then explic-
itly state any constraints. Recent and repeated
text has a greater effect on LLM generations due
to common attention patterns.

Clarify the expected output in the case of uncer-
tainty. Uncertain models may use default phrases
like “I don’t know,” and clarifying constraints
force the model to answer.

When the answer should contain multiple
information, request responses
pieces of
in JSON format. This leverages LLM’s famil-
iarity with code to provide an output structure
that is more easily parsed.

Hendrycks et al. (2021)

{$CONTEXT}

Inverse Scaling Prize

Which of the following describes
the above news headline? ←(cid:45)
A: Misinformation ←(cid:45)
B: Trustworthy ←(cid:45)
{$CONSTRAINT}

Child et al. (2019)

{$CONTEXT}
{$QUESTION}

No Existing Reference

Constraint: Even if you are
uncertain, you must pick either
“True” or “False” without using
any other words.

MiniChain Library

{$CONTEXT}
{$QUESTION}

JSON Output:

Table 1
LLM Prompting Guidelines to generate consistent, machine-readable outputs for CSS tasks.
These techniques can help solve overgeneralization problems on a constrained codebook, and
they can force models to answer questions with inherent uncertainty or offensive language.

In order to receive consistent, reproducible results we utilize a temperature of zero
for all LLMs. For models which provide probabilities directly, we constrain decoding to
the valid output classes.3 For other models, such as gpt-3.5-turbo, we use logit bias
to encourage valid outputs during decoding.4 All other generation parameters are left
at the default settings for each model.

CSS Prompt Design Guidelines. CSS tasks often require models to make inferences about
subtext and offensive language. Additionally, CSS codebooks often project complex
phenomena into a reduced set of labels. This raises challenges for the use of LLMs
which have been refined for general use. When initially exploring LLM behavior, we
found that models would hedge in the case of uncertainty, refuse to engage with
offensive language, and attempt to generalize beyond provided labels. While desirable
in a general context, these behaviors make it difficult to use LLMs inside a CSS pipeline.
Therefore, we built a set of guidelines in Table 1, drawn from both the literature and
our own experience with non-CSS tasks as NLP researchers. We explicitly share these
guidelines to help CSS practitioners control LLMs for their purposes. There is no claim
that the resulting prompts are optimally-engineered for each task; they instead provide
reasonable approximations to the kinds of prompts a non-AI expert could design after
considering established guidelines. By averaging our results over five prompt pertuba-
tions, we reduce the variance in this approximation of standard CSS tool-use.

3 Probability outputs for HuggingFace and GPT-3
4 Logit Bias reference for gpt-3.5-turbo

18

Ziems, Held, Shaikh, Chen, Zhang, Yang

Can LLMs Transform CSS?

Dataset

Size Classes

Dataset

Size Classes

Generation Tasks

500

Utterance Level

Dialect
Persuasion
Impl. Hate
Emotion
Figurative
Ideology
Stance
Humor
Misinfo
Semantic Chng

266
399
498
498
500
498
435
500
500
344

-

23
7
6
6
4
3
3
2
2
2

Conversation Level

Discourse
Politeness
Empathy
Toxicity
Power
Persuasion

497
498
498
500
500
434

Document Level

Event Arg.
Evt. Surprisal
Tropes
Ideology

283
240
114
498

7
3
3
2
2
2

–
–
114
3

Table 2
Dataset size and classes count across all selected CSS benchmarks. Datasets are sorted by class
count for each task category.

4.3 Test Set Construction

For each task, we evaluate a class-stratified sample of at most 500 instances from the
dataset’s designated test set. If the designation is missing, we take the class-stratified
sample from the entire dataset. Our sampled test sizes and class counts are in Table 2. All
datasets, prompts, and model outputs are released for future comparison and analysis.5

4.4 Evaluation Metrics

Automatic Evaluation. Each dataset has a different structure with a different number of
labels (see Table 2), so the use of accuracy is not the most informative metric. Instead, we
use compute the macro F1 score for all classification and structured parsing tasks and
average over the 5 prompt perturbations. Since we mapped the label space for each task
to an alphabetical list of candidate options and set the logit bias to favor these options
(§4.2), evaluation scripts use straightforward string-matching.

For high-variation domains like our generation tasks, on the other hand, word-
overlap-based machine translation metrics like BLEU (Post 2018) are expected to
have low correlation with human quality judgments (Liu et al. 2016). Here, even
embedding-similarity metrics like BERTScore (Zhang et al. 2020) may be insufficient
(Novikova et al. 2017). Manual inspection revealed high-quality generation outputs,
but the BLEURT (Sellam, Das, and Parikh 2020) score reported zero semantic overlap,
and variation in BLEU and BERTScores failed to follow any discernible patters with
regards to model preference or scaling laws that we observed by manual inspection.
For generation tasks, human evaluation is strongly preferable (Santhanam and Shaikh
2019), and we describe human evaluation in the following paragraphs.

5 Data Directory of our Github Project

19

Computational Linguistics

Volume 50, Number 1

Human Scoring Evaluation. To get a sense of the generation quality for each task, we
recruit a domain expert to blindly evaluate 100-400 model outputs. Evaluations are on
1-5 Likert scales for 4 standard metrics from the NLG literature. Following Fabbri et al.
(2021), we define these metrics as follows:

• Faithfulness: The generation is consistent with the source document and with the defi-

nition of the task.

• Coherence: The generation is well-structured and well-organized. The generation is not
just a heap of unrelated information, but forms a coherent body of information about a
topic. (Dang 2005)

• Relevance: The generation includes only important information from the source docu-

ment; no redundancies or excess information.

• Fluency: The generation has no formatting problems, capitalization errors or obviously
ungrammatical sentences (e.g., fragments, missing components) that make the text diffi-
cult to read.

All experts are recruited and paid through the Upwork platform. Annotator back-
grounds and expertise are summarized in the bottom right pane of Table 6. For
COVIDET summarization, we recruit a former CDC health communication specialist
with a B.S. in Public Health and an M.S. in Health Education. For Misinformation, we
enlist a Public Policy Graduate Student with a B.A. in Political Science. For Figurative
Language, we hire a former writing expert at Grammarly with an M.F.A. For Social Bias,
we find a Graduate Student with a B.S. in Journalism. And for Positive Reframing, we
hire a Nurse in Clinical Behavioral Health with a B.A. in Psychology.

Human Ranking Evaluation. Instead of scoring or rating target generations on a standard
Likert scale, annotators can also rank the model explanations in terms of their faithfulness
at describing the target construct. The ranking-style evaluation can be less variable than
scoring for generation tasks (Harzing et al. 2009; Belz and Kow 2010). We will use Social
Bias Frames as an example to illustrate the general setup for Human Ranking Evalua-
tions. Here, the annotator reviews a hateful message and an associated hate target. Then
they review four Implied Statements generated by one of the OpenAI models or pulled
from the SBIC’s gold human annotations. They are asked to rank these statements from
best to worst according to how accurate the implied statement is at describing the hidden
message from the hateful message. In this forced-choice ranking scheme, ties are not
allowed, but we use a unanimous vote to determine when a given model outranks
human performance. Unanimous vote flattens the variance for explanations of similar
quality and reflects only significant differences in quality.

Pilot annotation proved that crowdworker evaluations can exhibit high variance
and instability due to cultural and individual differences, as well as different interpre-
tations of the task. Thus the authors served as blind annotators for this evaluation. Two
authors evaluated each task and unanimous voting determined the reported metrics.

5. Classification Results

Table 3 presents all zero-shot results for utterance, conversation, and document-level
tasks. We use these results to answer Research Questions 1-3. The results suggest that
LLMs are a viable tool for augmenting human CSS annotation. For classification tasks,
results show that larger, instruction-tuned open-source LLMs are preferable.

20

Ziems, Held, Shaikh, Chen, Zhang, Yang

Can LLMs Transform CSS?

Model

Data

Dialect
Emotion
Figurative
Humor
Ideology
Impl. Hate
Misinfo
Persuasion
Sem. Chng.
Stance

Discourse
Empathy
Persuasion
Politeness
Power
Toxicity

Event Arg.
Event Det.
Ideology
Tropes

Baselines

FLAN-T5

FLAN

text-001

text-002 text-003

Chat

Rand Finetune Small Base Large

XL XXL

UL2 Ada Babb. Curie Dav. Davinci Davinci GPT3.5 GPT4

3.0
71.6
99.2
73.1
64.8
62.5
81.6
52.0
62.3
36.1

49.6
71.6
33.3
75.8
72.7
64.6

65.1
75.8
85.1
-

0.2
19.8
16.6
51.8
18.6
7.4
33.3
3.6
33.5
25.2

4.2
16.7
9.2
22.4
46.6
43.8

–
9.8
24.0
1.7

4.5
63.8
23.2
37.1
23.7
14.4
53.2
10.4
41.0
36.6

21.5
16.7
11.0
42.4
48.0
40.4

–
7.0
19.2
8.4

Utterance Level Tasks

24.8
65.7
32.2
56.9
47.6
32.3
68.7
32.1
52.0
43.2

30.3
66.2
53.2
29.9
53.1
29.6
69.6
45.7
36.3
49.1

0.5
32.9
6.4
70.8
10.0
62.3
56.8 38.7
46.4 39.7
7.1
32.0
45.8
77.4
43.5
3.6
41.6 32.8
48.1 18.1

Conversation Level Tasks

37.8
21.2
8.4
57.2
55.6
43.4

50.6
35.9
41.8
51.9
52.6
34.0

39.6
6.6
34.7 24.5
6.9
43.1
53.4 16.7
56.9
43.1
48.2 41.4

Document Level Tasks

–
10.9
29.0
14.6

–
41.8
42.4
19.0

–

–
50.6 29.8
38.8 22.1
7.7
28.6

23.4
69.7
18.0
54.9
43.0
7.2
64.8
37.5
56.9
42.2

33.6
22.1
11.3
44.7
40.8
42.5

–
1.0
28.3
13.7

0.5
4.9
15.2
33.3
25.1
7.8
36.2
5.3
38.9
17.7

9.6
17.6
6.7
17.1
39.8
34.2

–
47.3
26.8
12.8

1.2
6.6
10.0
34.7
25.2
4.9
41.5
4.7
41.3
17.2

4.3
27.6
6.7
33.9
37.5
33.4

8.6
47.4
18.9
16.7

9.1
19.7
19.4
29.2
23.1
9.2
42.3
11.3
35.7
35.6

11.4
16.8
33.3
22.1
36.9
34.8

8.6
44.4
21.5
15.2

3.3
16.7
25.0
49.5
33.3
16.7
50.0
14.3
50.0
33.3

14.3
33.3
50.0
33.3
49.5
50.0

22.3
0.4
33.3
36.9

17.1
36.8
45.6
29.7
46.0
18.4
70.2
21.6
41.9
46.4

35.1
16.9
33.3
33.1
39.2
41.8

21.6
48.8
42.8
16.3

14.7
44.0
57.8
33.0
46.8
19.2
73.7
17.5
37.4
41.3

36.4
17.4
53.9
39.4
51.9
46.9

22.9
52.4
43.4
26.6

11.7
47.1
48.6
43.3
43.1
16.3
55.0
23.3
44.2
48.0

35.4
22.6
51.7
51.1
56.5
31.2

22.3
51.3
44.7
36.9

23.2
50.6
17.5
61.3
60.0
3.7
26.9
56.4
21.2
76.0

16.7
6.4
28.6
59.7
42.0
55.4

23.0
14.8
51.5
44.9

Table 3
Zero-shot Classification Results across our selected CSS benchmark tasks. All tasks are
evaluated with macro F-1, which is averaged across 5 prompt permutations for zero-shot
models. Supervised baseline results are averaged over 3 random seeds. Best zero-shot models
are in green . A dash indicates a model did not follow instructions.

5.1 Viability (RQ1)
5.1.1 Zero-Shot Viability. To understand the viability of LLMs as CSS tools, we ask
if zero-shot LLMs match or exceed the reliability of human annotation. If the overall
performance is high and the expected agreement between humans and prompted mod-
els is as high as that between humans alone, then we might expect LLMs to viably
augment the human annotation process. According to one paradigm, an LLM can serve
as just one of many human and AI labelers, and gold labels would be decided by ma-
jority vote across these independent annotations. According to another complementary
paradigm, LLM pseudo-labels can be used with a small set of gold-labels to compute
unbiased estimators in downstream regressions following methods like Design-based
Semi-supervised Learning (DSL; Egami et al. 2023) and other .

Table 3 shows the best zero-shot models achieve as high as 77.4 F1 on misin-
formation detection. On this task, the best-performing FLAN-UL2 model achieves an
agreement of κ = 0.55 with gold labels (see Table 4), which is higher than the κ = 0.51
inter-human agreement reported by Gabriel et al. (2022) in their original paper. In fact,
for 8/17 tasks in Table 4, or 47% of classification tasks, models achieve moderate to
good agreement scores ranging from κ = 0.40 to 0.65. These tasks also correspond
to the highest absolute performances on Stance (76.0 F1) Emotion (70.8 F1), Figurative
Language (62.3 F1) and utterance-level Ideology Classification (60.0 F1). In these cases of
high viability, we recommend that CSS researchers consider the DSL and augmented-
annotator paradigms. Such strong performances are on tasks that either have objective

21

Computational Linguistics

Volume 50, Number 1

Dataset

Best Model

F1

κ Agreement

Dataset

Best Model

F1

κ Agreement

Utterance-Level

Convo-Level

Dialect

Emotion

Figurative
Humor
Ideology
Impl. Hate
Misinfo
Persuasion
Semantic Chng.

flan-ul2

flan-ul2

flan-ul2
gpt-4
davinci-002
flan-ul2
flan-ul2
gpt-4
flan-t5-large

Stance

gpt-3.5-turbo

32.9

70.8

62.3
61.3
60.0
32.3
77.4
56.4
56.9

72.0

0.15

0.65

poor

good

0.52 moderate
0.23
fair
0.40 moderate
0.20
fair
0.55 moderate
0.51 moderate
poor
0.14

0.58 moderate

Discourse
Empathy
Persuasion

Politeness
Power
Toxicity

flan-t5-xxl
flan-t5-xxl
davinci-003

flan-t5-xl
gpt-4
gpt-4

50.6
35.9
53.9

59.2
59.7
55.4

0.45 moderate
poor
0.04
poor
0.14

0.38
0.26
0.11

fair
fair
poor

Document-Level

Ideology
Event Det.
Tropes

gpt-4
gpt-4
gpt-4

51.5
23.0
44.9

0.51 moderate
-
n/a
-
n/a

Table 4
(Acc.) Best model F1 scores. F1 scores above 70% are bolded. (κ) Agreement scores between
zero-shot model classification and human gold labels. Out of ten utterance-level tasks, six have
at least moderate M and only two have poor agreement P . Three (50%) of the conversation
tasks have at least fair agreement F .

ground truth (fact checking for misinformation) or have labels with explicit colloquial
definitions in the pretraining data (emotional categories like anger are part of everyday
vernacular; political stances are well-documented and explicit in online forums). Our
qualitative error analysis in §5.1.2 will show that here, models are less likely to default
to neutral categories, and errors are more likely to come from annotation mistakes in
the gold dataset according to the author’s own manual error analysis (see lower neutral
and higher gold error in Figure 2).

Are zero-shot models ready to label text out-of-the-box? Zero-shot results rarely
exceed the carefully-tuned supervised RoBERTa baselines in Table 3. However, the
best observed performances here match that of classifiers used in published studies
on stance detection (67.8 F1; Zarrella and Marsh 2016), COVID-19 vaccination opinions
(Cotfas et al. 2021), political opinions (Siddiqua, Chy, and Aono 2019), and debates (Lai
et al. 2020). In such scenarios, zero-shot models could offer a data-efficient alterna-
tive to fine-tuned models by removing the need for expensive training sets. Humans
could focus all of their efforts on validating LLM outputs and tuning prompts (§4.2)
rather than coding unstructured text. However, we encourage practitioners to proceed
cautiously, especially in sensitive domains, and we recommend human-in-the-loop
methods to mitigate bias and risk. See §7.7 and §7.8 for further discussion.

It is important to consider that LLM performance could be unusably poor for some
CSS tasks. For a non-negligible subset of tasks we considered, LLMs have poor agree-
ment (5/17 = 29.5%), and here social scientists might not consider zero-shot annotation
augmentation via LLMs. On these poor agreement tasks, LLM absolute performance
is not significantly better than random guessing: see 56.9 F1 vs 50 Random on Semantic
Change; 35.9 F1 vs 33.3 Random on Empathy; 53.9 F1 vs 50 Random on conversation-level
Persuasion; and 55.4 F1 vs 50 Random on Toxicity. Some of these low-performance tasks
like Event Argument Extraction are structurally complex and may require additional en-
gineering efforts. Others like Empathy and Tropes have challenging and subjective expert
taxonomies whose semantics differ from definitions learned in model pretraining. This
is confirmed by our error analysis in Figure 2 where GPT3.5 often defaults to the neutral,
more colloquially recognizable label stereotype (64% of errors) rather than use a more

22

Ziems, Held, Shaikh, Chen, Zhang, Yang

Can LLMs Transform CSS?

Figure 2
Breakdown of Shared Error Types. For a representative subset of classification tasks, we
conduct an analysis of up to 50 shared errors across evaluated models. We focus specifically on
the best performing model in a class (e.g. the best variant of FLAN models or the best OpenAI
model). Plausible/gold errors occur when gold labels are incorrect or the model identifies a valid
secondary label. Neutral errors occur when a model over-predicts a category in a respective task
(metaphor in Figurative; surprise in Emotion; neutral in Politeness, and stereotypical in Implicit).

taxonomy-specific label like white grievance. In §5.1.3, we test if few-shot prompting can
reduce misalignments between model and ground-truth definitions.

5.1.2 Zero-Shot Error Analysis. For a representative subset of classification tasks, we
conduct an analysis of shared errors across evaluated models. We focus specifically on
the best performing model in a class (e.g. the best variant of FLAN models or the best
OpenAI model). Finally, in Figure 2 we break down the error types for gpt-3.5-turbo.

Figurative Language. We sample all 29 cases in which every model was incorrect. In
just under half of these cases (14/29), all models agreed on an incorrect answer, which
we call a unanimous error. Out of fourteen unanimous errors, the models were at least
partially correct four times, which we call a plausible/gold error (see Figure 2). There was
one mistaken gold label and three cases of correctly-labeled similes nested inside the
predicted sarcasm. Of the remaining ten unanimous errors, three were idioms mistaken
as metaphors, and seven were similes classified with the more general metaphor label.
For humans, this is a common error, but for models, this is surprising, since similes
should have easy keyword signals “as” and “like.” The baseline method was likely able
to exploit these signals to achieve a higher accuracy.

In 5 errors, all models disagreed and missed the intended sarcasm label. In another
5 error cases, only UL2 and text-davinci-003 agreed on the correct label, but the
dataset was mislabeled, with four idioms marked wrongly as metaphors and one simile
marked as an idiom. In the remaining 5 errors, ChatGPT showed a preference for the
most generic label and predicted metaphor.

Emotion Recognition. We sample 50 cases where all models differed from the gold labels.
Unlike Figurative Language, a minority of examples had the same mismatch across
models (9/50). However, a closer analysis of individual errors yields a surprising re-
sult: at least 18/50 examples across all evaluated models were judged as gold mislabels.

23

FigurativeEmotionPolitenessImplicit0204060% Error TypeGold/Plausible ErrorNeutral ErrorComputational Linguistics

Volume 50, Number 1

Additionally, for FLAN-UL2 and ChatGPT, 17/50 and 15/50 predictions respectively
could be considered as valid—even if they differed from the gold label.6

Moving to true negatives, we observe that DV2 makes the most errors (28/50) that
cannot be categorized as a gold mislabel, while UL2 (17/20) and ChatGPT (19/20) make
significantly fewer. The distribution of errors differ across each model type: ChatGPT,
for example, over-labels with surprise: especially instances with a true gold label of Joy
(8) or Love (5). On the other hand, UL2 mislabels Love as Joy frequently (9); and fear as
Sadness (4) or Surprise (4). Finally, davinci mislabels Sadness most frequently as Joy (9)
or anger/love (3 each).

Politeness Prediction. We first visualize the per-category accuracy of the different best-
performing models (FLAN-T5-XL, Text-davinci-002, and ChatGPT). We observe
that: (1) The XL model tends to predict more polite labels. It is more accurate in terms of
the utterances that were polite and neutral with 70.4% and 62.0% accuracy. Most errors
come from impolite cases (with a 45.2% accuracy). (2) davinci-002 performs best in
judging neutral utterances. davinci-002 is the most accurate for neutral utterances
(82.9% accuracy) while making significantly more errors for polite and impolite utter-
ances (43.9% and 40.9% accuracy respectively). (3) ChatGPT performs worst in finding
impolite utterances while making more neutral predictions, with only 9.0% accuracy for
the impolite category, whereas it achieves 75.9% and 66.8% for neutral and polite cases.
We then consider the 81/498 cases where the three models are all making er-
rors. We find that the three models make the same errors in most cases (54/81) and
davinci-002 models make errors more similar to ChatGPT (17/81 cases). Among
these common error cases, we observe that 79/81 cases are related to the 1st and
2nd person mention strategy (Danescu-Niculescu-Mizil et al. 2013) and all of them
are direct or indirect questions, while 38/81 are related to counterfactual modal and
indicative modal (Danescu-Niculescu-Mizil et al. 2013). This indicates that all three
models struggle with direct or indirect questions with 1st and 2nd person mentions.

Implicit Hate Classification. We first consider the confusion matrix and find that OpenAI
models are particularly oversensitive to the “stereotypical” class (71% and and 65%
false-positive rates from davinci-003 and ChatGPT respectively). Our error analysis
of 50 samples shows that models fail to apply the definition: stereotypical text must
associate the target with particular characteristics. Instead, models are more likely to
mark as stereotype any text that contains an identity term (86% of false-positives contain
identity terms). All models also fail to recognize strong phrasal signals, like “rip” or
“kill white people” for the white grievance (all 3/50 cases are errors), or violent terms
associated with threats. More subtle false-negatives require sociopolitical knowledge
(2/50) or understanding of humor (6/50). Other errors are examples where the model
identified a valid secondary hate category (5/50).

5.1.3 Few-Shot Viability. Zero-shot models may not be naturally aligned with the
non-standard or technical meanings of certain key terms in the social sciences. To
address this issue, we consider the viability of open-source FLAN models for few-
shot classification. Specifically, we try 3-shot and 5-shot experiments with no further
prompt engineering. Table 5 shows that any improvements from these methods are

6 For example, “i feel that the sweet team really accomplished that” can be considered both love - gold or joy -

predicted

24

Ziems, Held, Shaikh, Chen, Zhang, Yang

Can LLMs Transform CSS?

Model

Shot

FLAN Small

FLAN Base

FLAN Large

FLAN XL

FLAN XXL

FLAN UL2

0

3

5

0

3

5

0

3

5

0

3

5

0

3

5

0

3

5

0.4

4.5

9.3

7.2

3.6

0.0

6.8

0.0

7.4

1.4 23.4

3.6 10.4 10.8

6.2 14.4 21.1

0.7 14.1 24.8

8.0 20.5 30.3

0.2 29.9 32.9 12.6 27.5
0.2
Dialect
19.8 10.6 10.1 63.8 42.7 42.0 69.7 67.6 67.4 65.7 62.1 62.5 66.2 61.8 57.4 70.8 70.0 69.8
Emotion
9.2 23.2 29.1 27.3 18.0 21.8 19.6 32.2 27.9 28.5 53.2 52.6 66.2 62.3 52.7 62.0
16.6 10.0
Figurative
51.8 52.8 53.1 37.1 35.1 34.7 54.9 54.0 53.8 56.9 57.0 56.7 29.9 34.8 35.3 56.8 55.5 54.1
Humor
18.6 16.7 24.0 23.7 22.6 38.3 43.0 47.3 45.5 47.6 48.8 50.4 53.1 52.9 57.7 46.4 36.9 51.5
Ideology
7.4
4.7 32.3 28.5 34.6 29.6 31.6 35.1 32.0 29.5 25.9
Impl. Hate
33.3 33.3 33.3 53.2 45.3 59.7 64.8 64.8 64.2 68.7 67.2 69.7 69.6 74.9 74.4 77.4 53.7 76.4
Misinfo
7.3 37.5 39.0 37.7 32.1 44.3 41.8 45.7 44.6 48.6 43.5 42.2 40.1
3.6
Persuasion
Sem. Chng. 33.5 33.3 34.0 41.0 35.7 41.7 56.9 48.8 60.4 52.0 40.8 35.6 36.3 34.0 33.3 41.6 62.5 34.6
25.2 16.7 29.6 36.6 18.1 36.6 42.2 41.8 39.8 43.2 52.1 46.2 49.1 46.0 48.7 48.1 55.6 54.7
Stance
4.2
Discourse
3.6 39.1
16.7 16.7 16.7 16.7 16.7 16.7 22.1 16.7 17.1 21.2 30.4 22.8 35.9 29.8 28.2 34.7 41.5 39.6
Empathy
8.4 42.8 43.8 41.8 38.8 35.2 43.1 44.9 46.1
9.2 55.9 45.0 11.0 55.0 48.7 11.3 54.6 51.7
Persuasion
22.4 16.7 20.1 42.4 23.9 35.4 44.7 44.5 51.9 57.2 27.7 50.4 51.9 44.2 50.3 53.4 43.6 53.9
Politeness
46.6 44.5 33.3 48.0 39.8 41.4 40.8 45.5 43.5 55.6 58.9 60.2 52.6 52.0 62.6 56.9 57.2 57.5
Power
43.8 46.7 33.3 40.4 34.7 54.4 42.5 34.7 36.7 43.4 38.7 49.2 34.0 33.3 35.1 48.2 44.7 52.5
Toxicity
24.0 16.7 19.2 19.2 16.6 21.3 28.3 17.0 17.9 29.0 31.7 27.0 42.4 48.5 47.9 38.8 38.9 39.7
Ideology
6.8 28.6 27.3 24.6
1.7
Tropes

3.4 13.7 10.0 11.6 14.6

7.5 21.5 18.1 20.7 33.6

3.6 38.0 50.6

3.6 34.6 37.8

3.6 43.4 39.6

8.4 10.0 19.0

4.0

3.4

8.4

5.1

8.4

5.1

Table 5
Few-shot Classification does not uniformly improve performance across our selected CSS
benchmark tasks. All tasks are evaluated with macro F-1.

spotty and inconsistent. For some challenging tasks like Empathy and Persuasion that
have subjective definitions or non-standard taxonomies, few-shot learning can improve
performance in 2 and 5 out of 6 model sizes respectively. However, these gains are
small and not widespread among other tasks. We conclude that additional engineering
efforts may be needed to achieve significant gains on CSS tasks via few-shot learning.

5.2 Model-Selection (RQ2)

CSS researchers should understand how their choice of model can decide the reliability
of zero-shot methods. Our results show that, for structured parsing tasks like event
extraction, it is best to use a code-instructed model like OpenAI’s gpt-3.5-turbo,
while for most classification tasks, open-source LLMs like FLAN-UL2 are best.

Model Size. LLMs generally follow scaling laws (Kaplan et al. 2020; Hoffmann et al.
2022) where performance increases with the size of the model and training data. We
investigate scaling laws in the two families of instruction-tuned LLMs: FLAN and
OpenAI. Results show larger open-sourced models are preferable.

FLAN’s CSS performance roughly matches Kaplan et al.’s predicted power-law
effects from pure model size. Figure 3 shows FLAN classification performances scaling
nearly logarithmically with the parameter count. With each order of magnitude size
increase, the median average task improvement in FLAN models is 5.0 absolute percent-
age points. All FLAN-T5 models use the same stable corpus, pretraining objective, and
architecture, which gives us a controlled environment to observe stable scaling laws.

25

Computational Linguistics

Volume 50, Number 1

Figure 3
Effects of Scaling on the mean zero-shot performance on our CSS benchmark tasks. FLAN
models and davinci-001/002 are instruction fine-tuned. davinci-003 and
gpt-3.5-turbo are instruction fine-tuned and refined with Reinforcement Learning from
Human Feedback. GPT Parameter counts reported based on approximates.

OpenAI’s GPT-3 001 models, on the other hand, do not monotonically benefit
from scaling.7 There is minimal performance improvement from ada to davinci-001,
despite the three orders of magnitude increase in size. Similarly, we observe little benefit
from the trillion-parameter GPT-4 over the hundred-billion-parameter GPT-3.5-turbo.
Instead, the greatest performance improvements come from variations in pretraining,
fine-tuning, and reinforcement learning.

Pretraining & Instruction Fine-tuning. Besides scale, two key factors play a major role
in model performance: pretraining data and instruction fine-tuning. Pretraining data is
the raw text upon which an LLM learns to model the general generative process of
language. Instruction fine-tuning refines the raw LLM to perform specific tasks based
on human-written instructions.

OpenAI’s davinci models significantly benefit from pretraining and instruc-
tion fine-tuning tricks. For classification tasks (Table 3), we see an outsized in-
crease in CSS performance (↑ absolute 11 pct. pts.) moving from davinci-001
to davinci-002,
larger than any performance increase from scale alone. Both
davinci-001 and davinci-002 use the same supervised instruction fine-tuning
strategy, but davinci-002 is based on OpenAI’s base-code model, which had access
to a larger set of instruction fine-tuning data. Most importantly, davinci-002 was pre-
trained on both text and code. This difference benefits structured, JSON-formatted tasks
like Event Argument Extraction. While davinci-001 often fails to generate JSON,
davinci-002 succeeds with markedly improved performance (+13.0 F1).

7 This analysis relies on estimates which combine community estimates, the OpenAI research

documentation, and the assumption that all models named or "improved" from davinci have the same
parameter counts. These estimates may be incorrect, as hypothesized by other community estimates. This
is a limitation of research on these models as exact model size and training data are a trade secret of
OpenAI.

26

Model ParametersMean CSS Task F1 Score010203040501.00E+81.00E+91.00E+101.00E+111.00E+12Ziems, Held, Shaikh, Chen, Zhang, Yang

Can LLMs Transform CSS?

Learning From Human Feedback. We see that RLHF can improve LLM performance on
CSS classification tasks. RLHF has been lauded as the major catalyst behind the
success of instruction-following models (Ouyang et al. 2022), and here we see
text-davinci-003 and gpt-3.5-turbo (with RLHF) improves the average F1 of
text-davinci-002 (without RLHF) by 3.5 absolute points.

5.3 Domain-Utility (RQ3)

The survey and taxonomy of social science need in §2 allows us to understand whether
the utility of LLMs is limited to certain domains or certain data types. To do so, we
partition all classification results from Table 3 into bins corresponding to the academic
field most impacted by the task.8 Although we recognize the multi-disciplinary utility
of all tasks, this type of 1:1 organization is appropriate for understanding the academic
scope of our results. We acknowledge that the partitioning and selection of the dataset
influence the performance distributions that we observe. We urge readers to interpret
the results with caution and focus on broader conclusions rather than the fine numerical
details of these distributions.

The box plot in Figure 4 shows that field-specific performances significantly over-
lap. Thus overall, we do not observe a strong bias against or proclivity for a particular
field of study. In political science, we see the highest overall performance on misin-
formation detection (F1=77.4) and much lower performance on implicit hate detection
(F1=32.3). For psychology, we observe high performance on emotion detection (F1=70.8)
and low performance on empathy detection (F1=35.9). Peformances span the full range
of disciplines. This suggests that performance is not tied to academic discipline.

In terms of data type, Figure 4 suggests that performance may be more closely
determined by the complexity of the input. In particular, documents encode complex
sequences of ideas or temporal events, and overall, the two lowest task performances
are on the document-level tasks: character trope classification and event argument ex-
traction. All other document-level accuracies are at or below 50%. The most challenging
utterance and conversation-level tasks are also a function of their label space complexity.
Implicit hate (F1=32.3), empathy (F1=35.9), and dialect feature (F1=32.9) annotations are
expert-labeled on a subtle theoretical taxonomy.

6. Generation Results

In this section, we answer RQ4: Are prompted LLMs useful for generatively implementing
theories and explaining social scientific constructs with text? Will generative models replace
or augment human analysis? To answer this question, we rely on the human evaluation
setup described in §4.4. Note that FLAN models are excluded from all evaluation tables
because FLAN models failed to follow instructions by manual inspection. Instead, we
evaluate across the OpenAI suite.

Human Scoring Evaluation. According to the domain experts in Table 6, leading gen-
erative models can produce text of a quality that matches or exceeds that of human
gold references. For Aspect-Based Emotion Summarization, Misinformation Explana-
tion, and Social Bias Inference, gpt-3.5-turbo produce, on average, more domain-

8 This partitioning follows Figure 1, with stance and ideology detection in the political science bin and

dialect feature classification under linguistics, for example.

27

Computational Linguistics

Volume 50, Number 1

Figure 4
(Left) Task Performance By Field of Study. Significant overlap in the distributions suggests that
neither high nor low performance is exclusive to any particular discipline. Caution: The
distributions depend on the particular choices of this study, which datasets to select and how to
partition them.
(Right) Task Performance By Level of Analysis. Document-level tasks are challenging for their
input length and complexity, and this is reflected in their F1 scores all near or below 50%.
Utterance and conversation-level task performance varies also with the complexity of the task.

faithful, coherent, and fluent text than both gold references and the fine-tuned baseline.
For Positive Reframing and Figurative Language explanation, text-davinci-003
match the gold-standard levels of faithfulness, relevance, coherence, and fluency, again
outperforming the fine-tuned baseline. For generation performance, scale matters, as
smaller models fail to produce explanations and summaries that are faithful to the
task specifications, especially in COVIDET, FLUTE, and SBIC, where text-ada-001
earns faithfulness scores of less than 2 out of 5 on average. With scale, however, LLMs
are capable of generating useful, relevant, coherent, and fluent explanations and
summaries of underlying social science constructs.

Human Ranking Evaluation. According to the authors’ ranking evaluations in Table 7,
prompted LLMs produce helpful and informative text in all five generation tasks.
Model generations outrank the dataset’s gold human reference at least 38% of the time.
The best models approach parity with humans—a near 50-50 coin toss to decide which
is preferred. Furthermore, we see significant performance benefits from both RLHF
models, gpt-3.5-turbo and text-davinci-003. Unlike classification (§5.2), our
selected generation tasks seem to systematically benefit from human feedback.

Despite strong performances, no model substantially outperforms human annota-
tion. This suggests that current LLMs cannot fully replace human analysis. Still, given
LLM’s performance parity with humans, the results suggest one avenue for human-
AI collaboration: instead of coding text with summary explanations from scratch,
researchers and annotators could apply minor edits to correct model generations. 9
The results in Table 7 suggest that, for every five model generations, 2 to 3 of these
outputs would demand no additional annotator effort. If implemented successfully, this
partnership could significantly increase the efficiency of the social scientist’s research
pipeline. However, we leave it to future work in HCI to determine the plausibility of

9 Note that machine generated explanations might be limited in terms of their diversity. Although human
validation can help refine these machine outputs, such process may not be able to introduce novel edits
or perspectives.

28

historylinguisticsliteraturepolitical sciencepsychologysociologyField of Study0.30.40.50.60.70.8Best Task F1 ScoresutteranceconversationdocumentLevel of Analysis0.30.40.50.60.70.8Best Task F1 Scores4.2
4.5
4.3
4.4
4.5
4.9+
4.5
4.9+
4.5
4.4

Fluent
1.9−
3.3+
3.8+
4.5+
3.9+
4.2+
4.4+
4.2+
4.6+
2.6

Ziems, Held, Shaikh, Chen, Zhang, Yang

Can LLMs Transform CSS?

Aspect-Based Summarization (COVIDET)

Implied Misinformation Explanation (MRF)

Model

Faithful Relevant Coherent

Fluent

Model

Faithful Relevant Coherent

Baseline
ada-001
babbage-001
curie-001
davinci-001
davinci-002
davinci-003
GPT 3.5
GPT 4
Human

2.1
1.8−
2.0−
2.3
2.3
2.4
2.9
3.9+
3.7+
2.8

2.3
1.8−
2.0
2.3
2.4
2.5
2.8
3.5+
3.3+
2.6

2.1−
2.4
2.3
2.6
2.5
3.2
3.0
3.8+
3.8+
2.8

Fluent
2.6−
3.6
3.7
3.8
3.9
4.0
4.1+
4.5+
4.4+
3.8

Baseline
ada-001
babbage-001
curie-001
davinci-001
davinci-002
davinci-003
GPT 3.5
GPT 4
Human

3.4
1.1−
1.6−
2.6−
1.7−
3.9+
3.1−
3.7+
3.7
3.5

3.5
1.1−
1.7−
2.7−
1.7−
4.1+
3.4
3.9
3.9
3.7

3.7
2.0−
2.5−
3.1−
2.5−
4.3+
3.9
4.2+
4.1
3.9

Figurative Language Explanation (FLUTE)

Social Bias Inference (SBIC)

Model

Baseline
ada-001
babbage-001
curie-001
davinci-001
davinci-002
davinci-003
GPT 3.5
GPT 4
Human

Faithful Relevant Coherent
1.7−
1.5−
1.9−
2.3−
1.9−
3.4
4.0
3.6
3.3
4.0

1.4−
1.4−
1.4−
1.5−
1.2−
2.5
3.0
2.1−
2.1−
2.8

1.4−
1.5−
1.5−
1.7−
1.5−
2.5
3.1
2.5
2.4
2.6

Fluent

Model

4.2
3.9
3.9−
4.1
4.1
4.1
4.1+
4.1
4.0
4.2

Baseline
ada-001
babbage-001
curie-001
davinci-001
davinci-002
davinci-003
GPT 3.5
GPT 4
Human

Faithful Relevant Coherent
2.1−
2.2−
3.1
3.3
3.4
3.5
3.4
3.7+
3.8+
3.0

1.9−
2.4
3.1
3.4
3.4
3.7+
3.5
4.0+
4.1+
2.9

2.1−
2.7
3.6+
3.9+
3.8+
4.1+
4.1+
4.2+
4.2+
3.1

Positive Reframing

Model

Faithful Relevant Coherent

Fluent

Baseline
ada-001
babbage-001
curie-001
davinci-001
davinci-002
davinci-003
GPT 3.5
GPT 4
Human

4.1
1.8−
3.8
4.1
3.5−
4.0
4.4
4.3
4.1
4.2

4.2
1.4−
2.5−
3.7−
4.0
3.9−
4.5+
4.3
4.3
4.2

3.9
1.8−
3.8
4.1
3.3−
4.0
4.2
4.2
4.1
4.1

4.4
1.6−
3.7
3.9
4.1
4.2
4.6+
4.4
4.2
4.2

Task

COVIDET

MRF

FLUTE

SBIC

Reframing

Annotator Backgrounds

Education

Profession

MS,
Health Ed.
BA,
Poli. Sci.
MFA,
Creat. Writing
BS,
Journalism
BA,
Psychology

CDC Health
Comm. Specialist
Grad Student,
Public Policy
Writing Expert,
Grammarly
Grad Student,
Epidemiology
Clinical Behavioral
Health, Nurse

Table 6
Expert Scoring Evaluations for Zero-shot Generation Tasks show that leading generative
models (davinci-003, GPT 3.5) can match or exceed the faithfulness, relevance, coherence,
and fluency of both fine-tuned models (Baseline) and gold references (Human). All scores are
average ratings on 1-5 Likert scales. Best models are in green followed by blue . Marks for + and −
show performance significantly better or worse than human (P < .05) by Paired Bootstrap.

this partnership and the degree to which it might reduce annotators’ cognitive load on
exploratory analysis and free-coding tasks.

As a tradeoff for LLM’s efficiency, researchers will face the burden of manually
validating generative outputs. It is well-known that automatic performance metrics
fail to capture human preferences (Goyal, Li, and Durrett 2022; Liang et al. 2022).
In fact, we found that BLEU, BERTScore, and BLEURT, which rely on comparisons
to human written ground truth, all produced uninterpretable scores for generation
tasks. This highlights a fundamental challenge for evaluation of generation systems in
CSS, especially if zero-shot performance continues to improve. As zero-shot models
approach or outperform the quality of the gold-reference generations, reference-based
scoring becomes an invalid construct for measuring models’ true utility (Raji et al. 2021),
even if we assume the semantic similarity metrics are ideal. This motivates our use of

29

Computational Linguistics

Volume 50, Number 1

Model

MRF

FLUTE

SBIC Reframing COVIDET

% Model Preferred Over Gold Annotations

Baseline
ada-001
babbage-001
curie-001
davinci-001
davinci-002
davinci-003
GPT 3.5
GPT 4

31.2%
17.6%
29.4%
29.4%
21.4%
21.4%
38.9%
27.8%
36.4%

16.5%
4.6%
11.8%
1.7%
29.4%
6.7%
32.4%
1.7%
39.0%
6.2%
29.3%
25.0%
50.0%
47.0%
37.9% 65.9%
60.6%
51.5%

45.0%
0.0%
0.0%
11.5%
30.4%
10.0%
48.5%
56.1%
39.4%

37.5%
23.5%
23.5%
41.2%
50.0%
37.5%
59.1%
68.2%
36.4%

Table 7
Ranking Evaluations for Zero-shot Generation Tasks give the proportion of all pairwise
rankings where authors unanimously ranked the model’s generation as more accurate or
preferable to a gold-standard explanation drawn from the dataset. Best models are in green and
runner-ups are in blue .

reference-free expert evaluation of generations, that is, asking expert annotators which
generation is more accurate with regard to the input. However, this alternative is limited
by both cost and reproducibility concerns (Karpinska, Akoury, and Iyyer 2021). There is
a clear need for new metrics and procedures to quantify model utility for CSS.

7. Discussion

This work presents a comprehensive evaluation of LLMs on a representative suite of
CSS tasks. We contribute a robust evaluation pipeline, which allows us to benchmark
performance alongside supervised baselines on a wide range of tasks. Our research
questions and empirical results are designed to help CSS researchers make decisions
about when LLMs are suitable and which models are best suited for different research
needs. In summary, we find that LLMs can augment but not entirely replace the
traditional CSS research pipeline.

More concretely, we make the following recommendations to CSS researchers:

1. Integrate LLMs-in-the-loop to transform large-scale data labeling.
2. Prioritize open-source LLMs for classification
3. Prioritize faithfulness, relevance, coherence, and fluency in your generations by
opting for larger instruction-tuned models that have learned human preferences.
4. Investigate how LLMs produce new CSS paradigms built on the multipurpose

capabilities of LLMs in the long term.

In the following subsections, we more specifically detail in how annotation fits into
the CSS pipeline (§7.1), how LLMs can augment annotation (§7.2), which LLMs we
recommend for this purpose (§7.3), and the opportunities LLMs expose for new research
paradigms (§7.4 and §7.5).

30

Ziems, Held, Shaikh, Chen, Zhang, Yang

Can LLMs Transform CSS?

Figure 5
Human-AI Collaboration can improve the efficiency and reliability of text analysis. In this
misinformation example, the LLM helps scale up annotation while reducing variance in the gold
labels. Human annotation serves as validation for model-provided annotations.

7.1 How Annotation Fits Into CSS

Social scientists are not often interested in classification labels or generative codes
merely for their own sake. Labeled text is almost always used to explain a wider
phenomenon using downstream inferential statistics such as regression. To ensure a
valid downstream inference, any estimators of the underlying construct need to be
asymptotically unbiased and allow for the computation of valid confidence intervals.
In a study that follows up our own, Egami et al. (2023) demonstrate that even the most
accurate of LLM annotations will produce biased estimates and invalid confidence in-
tervals when they are merely averaged. However, Egami et al. (2023) propose a method
called Design-based Semi-supervised Learning (DSL) which they use for computing
unbiased estimators for prevalence estimation on each of our 17 classification tasks.
Using FLAN-UL2 pseudo-labels and only a handful of gold-labeled instances, they find
that it is possible to compute unbiased regressions, even for tasks with low accuracy
from UL2. With only 25 gold annotations, DSL can compute confidence intervals that
have >86% correct coverage for all of our classification tasks including those with the
lowest performance from LLM pseudo-labels.

7.2 LLMs Can Augment Annotation

Our work shows that current LLMs perform well enough to augment the CSS annotation
pipeline and thus reduce the need for human labor on some tasks. §5.1 show that an LLM
annotator yields fair to strong agreement with humans on 12 out of 17 classification
tasks. However, LLMs are not a wholesale replacement for human annotators. Even the best
LLMs exhibit unusably low performance on some CSS tasks. Ensembling prediction
does not mitigate this label corruption as LLMs demonstrate high internal agreement,
even when inaccurate (Gilardi, Alizadeh, and Kubli 2023). Overconfident models, if left
unchecked, distort the conclusions of CSS research and subsequently mislead policy
and social actions taken in response. Human validation is key to avoiding a replication
crisis in CSS caused by LLM hallucinations and inaccuracies.

31

Persimmon kills coronavirus, according to the study by Japanese scientists.Misinformation Detection ExampleLLM Augmented✗✗✓✗✗?✓TraditionalComputational Linguistics

Volume 50, Number 1

Instead, we advocate that CSS researchers integrate LLMs with human annotation, as
illustrated in Figure 5. When a LLM matches human levels of agreement, it can be
used as one of multiple labelers. It is possible from such methods to produce unbiased
estimators. The estimation methods of Chaganty, Mussmann, and Liang (2018) are
provably optimal, and provide these unbiased estimators with 7-13% monetary savings
by leveraging LLM pseudo-labels.

Moving forward, LLMs can serve as a flywheel for dataset collection. Prompted
LLMs consistently perform significantly better than chance, providing imperfect labels
at low cost. Annotation schemes developed to iteratively improve imperfect data —such
as weak supervision (Ratner et al. 2017), targeted data cleaning (Chen, Yu, and Bowman
2022), and active learning (Yuan, Lin, and Boyd-Graber 2020; Li et al. 2022) — avoid
LLM pitfalls by allowing human validation to refine the original model. This creates a
virtuous cycle which exploits the strengths of LLMs to focus human expertise where it
is most needed (Kiela et al. 2021).

Our results show that LLMs are even stronger at generation tasks, being rated superior
to human gold annotations over 38% of the time in all 5 tasks we evaluate. LLMs can
already generate syntactically cohesive and stylistically consistent text, and as we have
shown, the best generations are also highly relevant and faithful to core CSS tasks.
Humans expertise can be used to further curate outputs according to domain-specific
accuracy and quality metrics. Dataset construction through human curation of LLM
generations has already emerged in recent NLP works on decision explanation (Wiegr-
effe et al. 2022), model error identification (Ribeiro and Lundberg 2022), and even to
build the figurative language benchmark used in this work (Chakrabarty et al. 2022).

We recommend that CSS researchers consider the use of LLMs as the foundation of
such annotation procedures, and that future studies measure the degree to which this
strategy improves annotation efficiency as we suspect. If the anticipated efficiency is
achieved, CSS researchers should reinvest savings to train expert annotators, reversing
the trends of replacing experts with crowdworkers due to cost (Snow et al. 2008). By
doing so, LLMs could enable data labeling procedures that more deeply benefit from
the non-computational expertise of the social scientists whose theories we build upon.

7.3 When To Use What LLM

We hope these results help CSS researchers to understand LLM alternatives for their use
cases. Our general prompt guidelines allow us to quickly design functional prompts for
many models. When looking to incorporate LLMs in their work, CSS researchers should
consider the advantages and disadvantages of open and closed-source models.

For CSS classification, our work shows that open-source models like FLAN are as capable as
state-of-the-art closed-source LLMs from OpenAI. We recommend researchers who already
have access to GPUs capable of running these models prefer open-source models. For
continuous monitoring and enormous-scale analysis, the low marginal cost of these
models could make them price-advantageous. For CSS researchers with expertise, open-
source LLMs have the added benefit of being able to be fine-tuned on labeled data
and constrained programatically for more predictable behavior. At this time, it is not
possible to further fine-tune all of OpenAI’s instruction-tuned models.

For those without existing hardware infrastructure, proprietary APIs appear to be
a cost-efficient option. Based on current cloud pricing,10 the hardware necessary to

10 Google Cloud FLAN hosting cost

32

Ziems, Held, Shaikh, Chen, Zhang, Yang

Can LLMs Transform CSS?

run FLAN-T5-XXL costs 170 dollars per day—the equivalent of processing ∼50 million
words with gpt-3.5-turbo.11 In most cases, gpt-3.5-turbo is more cost-efficient
and has a lower operational overhead for hardware-constrained research groups.

For generation tasks, the results are clear-cut. Even the largest open-source models
failed to generate meaningful responses for CSS tasks. Even when labeled data is avail-
able, the best proprietary models outperform fine-tuned baselines consistently and approach
parity with gold human annotations when evaluated by crowdworkers. For CSS experts
looking to generate interpretations or explanations of data, gpt-3.5-turbo is the clear
leading LLM by both price and performance. No matter which modeling decision is
made, practitioners should keep the limitations of natural language generation in mind,
understanding that explanations are not causal and recognizing the risks that come with
model errors and hallucinations (see §7.8).

Our work shows that all LLMs struggle most with conversational and full doc-
ument data. Also, LLMs currently lack clear cross-document reasoning capabilities,
limiting extremely common CSS applications like topic modeling. For CSS subfields
which often study these discourse types—sociology, literature, and psychology—LLMs
have major limitations and are unlikely to have major immediate impact. NLP re-
searchers who aim to improve existing LLMs to empower more CSS tasks should study
the unique technical challenges of conversations, long documents, and cross-document
reasoning (Beltagy, Peters, and Cohan 2020; Caciularu et al. 2021; Yu et al. 2021).

7.4 Blending CSS Paradigms

The few-shot (Brown et al. 2020) and zero-shot capabilities (Ouyang et al. 2022) of
LLMs blur the traditional line between supervised and unsupervised ML methods
for the social sciences. Historically, supervised methods invest in labeled data guided
by existing theory to develop a trained model. This model is then used to classify
text at scale to gather evidence for the causal effects surrounding the theory. By com-
parison, unsupervised methods like topic modeling often condense large amounts of
information to help researchers discover new relationships, which develop or refine
social theories (Evans and Aceves 2016).

The ability of LLMs to follow instructions and interpret complex tasks is rapidly
advancing, with major new models even within the course of this work (OpenAI
2023). Beyond annotation, LLMs have multi-purpose capabilities to retrieve, label, and
condense relevant information at scale. We believe that this can blend the boundaries be-
tween supervised and unsupervised paradigms. Rather than using separate paradigms
to develop and test theories, a single tool can be used to develop working hypotheses,
using generated and summarized data, and test hypotheses, labeling human samples
flexibly with low-cost classification capabilities. We believe CSS researchers should use
the multi-functionality of LLMs to create new paradigms of research for their fields.

Simulation. An emerging example of such innovation in CSS is the use of LLMs as
simulated sample populations. Game theorists have used rule-based utility functions
to develop hypotheses about the causes of social phenomena (Schelling 1971; Easley
and Kleinberg 2010) and to predict the effects of policy changes (Shubik 1982; Klein-
berg et al. 2018). However, simulations are limited by the expressiveness of utility
functions (Ellsberg 1961; Machina 1987). LLMs hold a great potential to provide more

11 OpenAI Pricing

33

Computational Linguistics

Volume 50, Number 1

powerful simulations for CSS (Bail 2023), as they replicate human biases without explicit
conditioning (Jones and Steinhardt 2022; Koralus and Wang-Ma´scianica 2023). Recent
work leverages this capacity to simulate social computing systems (Park et al. 2022),
community and their members’ interactions (Park et al. 2023), public opinion (Argyle
et al. 2022; Chu et al. 2023), and subjective experience description (Argyle et al. 2022).

However, there are dangers and uncertainties in this area as noted in these works.
Since social systems evolve unpredictably (Salganik, Dodds, and Watts 2006), simu-
lated samples inherently have limited predictive and explanatory power. While utility-
based simulations have similar limitations, their assumptions are explicit unlike the
opaque model of human behavior an LLM provides. Additionally, current models
exhibit higher homogeneity of opinions than humans (Argyle et al. 2022; Santurkar et al.
2023a). Combining LLMs with true human samples is essential to avoid an algorithmic
monoculture and could lead to fragile findings covering only the limited perspectives
represented (Kleinberg and Raghavan 2021; Bommasani et al. 2022).

7.5 The Need for A New Evaluation Paradigm

Evaluation will need to adapt if blended methods create a new CSS paradigm.
Accuracy-based metrics were ideal for fixed-taxonomy classification tasks in the era of
NLP benchmarking. Similarly, word-overlap metrics made sense for natural language
generation tasks in which the gold reference was well-defined (e.g., translation). How-
ever, open-ended coding and CSS explanation objectives follow neither a pre-defined
taxonomy nor a regular output template. For more open-ended data exploration tasks
like topic modeling, held-out likelihood helped automatically measure the predictive
power of the model (Wallach et al. 2009), but predictiveness does not always correlate
with explainability (Shmueli et al. 2010), and these automatic metrics proved to be at
odds with human quality evaluations (Chang et al. 2009). In CSS, human evaluations
can be unreliable (Karpinska, Akoury, and Iyyer 2021). We observe this directly in our
work, as crowd work seems to provide unreliable quality metrics for FLUTE, a nuanced
generative task. New metrics are needed to capture the semantic validity of free-form
coding with LLMs as explanation-generators.

7.6 CSS Challenges for LLMs

As shown by our §5 results, LLMs face notable challenges that pervade the computa-
tional social sciences. The first challenge comes from the subtle and non-conventional
language of expert taxonomies. Expert taxonomies contain technical terms like the
dialect feature copula omission (§3.1.1), plus specialized or nonstandard definitions of
colloquial terms, like the persuasive scarcity strategy (§3.1.8), or white grievance in im-
plicit hate (§3.1.4). LLMs may lack sufficient representations for such technical terms, as
they may be absent from the pretraining data (Yao et al. 2021). How to teach LLMs to un-
derstand these social constructs deserves further technical attention. This is especially
true for novel theoretical constructs that social scientists may wish to define and study in
collaboration with LLMs.

Unlike widely used NLP classification tasks, the challenge of expert taxonomies
in CSS is compounded by the size of the target label space, which, in CSS applica-
tions, may contain upwards of 72 classes (see character tropes, §3.3.4). This challenges
transformer-based LLMs, which have relatively limited memory, finite processing win-
dows, and quadratic space complexity.

34

Ziems, Held, Shaikh, Chen, Zhang, Yang

Can LLMs Transform CSS?

Large, complex, and nuanced annotation schemes may also introduce dependen-
cies among labels that are organized into multi-level hierarchies or richly constrained
schemas, as in many event argument extraction applications. Such complex structural
parsing tasks pose special challenges to the zero-shot prompting paradigm introduced
in this work since prompted models often struggle to generate consistent outputs
(Mishra, Tater, and Sankaranarayanan 2019). Our prompting best practices in Table 1
all help LLMs generate more consistent machine-readable outputs, but this challenge is
not fully solved for all CSS tasks.

Finally, Computational Social Scientists study language, norms, beliefs, and politi-
cal structures that all change across time. To account for these distribution shifts, LLMs
will need an extremely high level of temporal grounding—knowledge and signals by
which to orient a text analysis in a particular place and time (Bommasani et al. 2021).
This is especially challenging wherever researchers are interested in rapid, synchronous
analysis of breaking events. It may be prohibitively expensive to frequently update
LLM’s knowledge of current events via continually training (Bender et al. 2021), and
this challenge will only be exacerbated as models continue to scale up.

7.7 Issues in Bias and Fairness

Bias. Researchers should weigh the benefits of applying prompting methods to CSS,
along with the limitations and risks of doing so. Most notably, LLMs are known to
amplify social biases and stereotypes (Sheng et al. 2021; Abid, Farooqi, and Zou 2021;
Borchers et al. 2022; Lucy and Bamman 2021; Shaikh et al. 2022), as well as viewpoint
biases in subjective domains (Santurkar et al. 2023b). These biases can emerge in open-
ended generation tasks like the explanation and paraphrasing (Dhamala et al. 2021). The
performance of LLMs as tools for classification and parsing may vary systematically as
a function of demographic variation in the target population (Zhao et al. 2018). With
the datasets available, we were unable to perform a systematic analysis of biases and
performance discrepancies, but we urge researchers to carefully consider these risks in
downstream applications.

Risks Inherent to Proprietary LLMs. Researchers will often lack details on the selection,
filtering, and formatting of online corpora for training proprietary models like Ope-
nAI’s GPT-4. There are unique risks and privacy implications for those who employ
these models for research. One risk inherent in an obscured pre-training corpus is that
we can’t decompose the above issues of bias and social harm into their respective
sources for targeted mitigation. Especially with open-ended generative coding (§3.4),
unattributed biases could jeopardize the reliability and prosocial impact of downstream
scientific analyses. Such issues may also escape human review, as humans are prone to
falsely attribute factuality to texts that bear a more authoritative or expert style (Wu and
Aji 2023)—-a style that modern proprietary LLMs have largely mastered. Furthermore,
black-box industrial APIs may not allow for targeted mitigation via fine-tuning.

Researchers who operate with closed-source industrial APIs may also be more
prone to privacy issues and legal disputes over intellectual property. Proprietary models
are known to replicate copyrighted materials and sensitive personally identifiable infor-
mation (Carlini et al. 2021). Researchers who employ these models may be unknowingly
accountable for knowledge based on false or missing attributions as well as private
personal information.

35

Computational Linguistics

Volume 50, Number 1

7.8 Limitations

Task Selection and Data Leakage. Our tasks do not represent an exhaustive list of all appli-
cation domains. Some highly-sensitive domains like mental health (Nguyen et al. 2022),
which requires expert annotations, and cultural studies, which requires community-
specific knowledge, are rife with additional challenges and ethical concerns. These are
largely outside the scope of the current study. More broadly, LLMs should not be used to
give legal or medical advice, prescribe or diagnose illness, or interfere with democratic
processes (Solaiman and Dennison 2021). Finally, our task selection was limited by the
available data resources in the field, which is largely dominated by text in standard
dialects (Ziems et al. 2023) representing members of Western, Educated, Industrial, Rich,
and Democratic populations (WEIRD; Ignatow and Mihalcea 2016; Muthukrishna et al.
2020). Future studies should separately consider LLMs’ utility for cross-cultural CSS.

When evaluating LLMs, one notable concern is data leakage. Data from the test
set might have been seen by LLMs during the pre-training, and this would artificially
inflate test performances. This problem is especially concerning for closed-source or
proprietary models with undisclosed training sets. One mitigation strategy is to design
explicit prompts that force the model to forget the test set. Another strategy is to design
custom test sets from perturbations of existing data to more fairly evaluate models. We
leave this for future work.

Causality and Explanations. Explanations are important to social science (Shmueli et al.
2010; Hofman, Sharma, and Watts 2017; Yarkoni and Westfall 2017). In this work, we
explored the predictive power of LLMs rather than causal explanations. Predictions
serve to expose and elaborate on the underlying social phenomena latent in a text. These
explicit phenomena can then be used as structured features for further causal analysis.
However, this may not be sufficient: social scientists often seek causal theories
(DiMaggio 2015), or at least contrastive explanations, why P instead of Q (Miller 2019).
Because LLMs are not grounded in a causal model of the world (Bender et al. 2021),
they are not on their own reliable tools for mining causal relationships in text. We leave
it to future work to explore contrastive or causal explanations in LLMs.

Acknowledgments
We are thankful to Tony Wang, Rishi Bommasani, Albert Lu, Myra Cheng, Yanzhe Zhang,
Camille Harris, and Minzhi Li for their helpful feedback on our early drafts. We thank the
anonymous reviewers for their insightful suggestions as they significantly shaped the final form
of this work. Caleb Ziems is supported by the NSF Graduate Research Fellowship under Grant
No. DGE-2039655. This work was partially sponsored by NSF grant IIS-2247357 and IIS-2308994.

References
Abbott, Andrew. 1990. Conceptions of time
and events in social science methods:
Causal and narrative approaches.
Historical Methods: A Journal of Quantitative
and Interdisciplinary History, 23(4):140–150.
Abid, Abubakar, Maheen Farooqi, and James
Zou. 2021. Persistent anti-muslim bias in
large language models. In Proceedings of
the 2021 AAAI/ACM Conference on AI,
Ethics, and Society, pages 298–306.

Abul-Fottouh, Deena and Tina Fetner. 2018.

Solidarity or schism: ideological

congruence and the twitter networks of
egyptian activists. Mobilization: An
International Quarterly, 23(1):23–44.

Ahmed, Amr and Eric Xing. 2010. Staying

informed: Supervised and
semi-supervised multi-view topical
analysis of ideological perspective. In
Proceedings of the 2010 Conference on
Empirical Methods in Natural Language
Processing, pages 1140–1150, Association
for Computational Linguistics,
Cambridge, MA.

36

Ziems, Held, Shaikh, Chen, Zhang, Yang

Can LLMs Transform CSS?

Ahuja, Ojas, Jiacheng Xu, Akshay Gupta,

Kevin Horecka, and Greg Durrett. 2022.
Aspectnews: Aspect-oriented
summarization of news documents. In
Proceedings of the 60th Annual Meeting of the
Association for Computational Linguistics
(Volume 1: Long Papers), pages 6494–6506.

Althoff, Tim, Cristian

Danescu-Niculescu-Mizil, and Dan
Jurafsky. 2014. How to ask for a favor: A
case study on the success of altruistic
requests. In Proceedings of the International
AAAI Conference on Web and Social Media,
volume 8, pages 12–21.

Altikriti, Sahar. 2016. Persuasive speech acts
in barack obama’s inaugural speeches
(2009, 2013) and the last state of the union
address (2016). International Journal of
Linguistics, 8(2):47–66.

Amber, Boydstun, Gross Justin, Philip

Resnik, and Noah Smith. 2013. Identifying
media frames and frame dynamics within
and across policy issues. In New directions
in analyzing text as Data workshop.

Anderson, Cameron, Oliver P John, Dacher
Keltner, and Ann M Kring. 2001. Who
attains social status? effects of personality
and physical attractiveness in social
groups. Journal of personality and social
psychology, 81(1):116.

Andersson, Lynne M and Christine M

Pearson. 1999. Tit for tat? the spiraling
effect of incivility in the workplace.
Academy of management review,
24(3):452–471.

Argyle, Lisa P, Ethan C Busby, Nancy Fulda,
Joshua R Gubler, Christopher Rytting, and
David Wingate. 2022. Out of one, many:
Using language models to simulate
human samples. Political Analysis, pages
1–15.

Bail, Chris. 2014. Terrified: How anti-Muslim
fringe organizations became mainstream.
Princeton University Press.

Bail, Christopher A. 2016. Emotional

feedback and the viral spread of social
media messages about autism spectrum
disorders. American journal of public health,
106(7):1173–1180.

Natural Language Processing (EMNLP),
pages 4982–4991, Association for
Computational Linguistics, Online.
Baly, Ramy, Georgi Karadzhov, Dimitar
Alexandrov, James Glass, and Preslav
Nakov. 2018. Predicting factuality of
reporting and bias of news media sources.
In Proceedings of the 2018 Conference on
Empirical Methods in Natural Language
Processing, pages 3528–3539, Association
for Computational Linguistics, Brussels,
Belgium.

Bamman, David, Jacob Eisenstein, and Tyler
Schnoebelen. 2014. Gender identity and
lexical variation in social media. Journal of
Sociolinguistics, 18(2):135–160.

Bamman, David, Brendan O’Connor, and
Noah A. Smith. 2013. Learning latent
personas of film characters. In Proceedings
of the 51st Annual Meeting of the Association
for Computational Linguistics (Volume 1:
Long Papers), pages 352–361, Association
for Computational Linguistics, Sofia,
Bulgaria.

Bamman, David and Noah A. Smith. 2015.
Open extraction of fine-grained political
statements. In Proceedings of the 2015
Conference on Empirical Methods in Natural
Language Processing, pages 76–85,
Association for Computational
Linguistics, Lisbon, Portugal.

Bang, Yejin, Samuel Cahyawijaya, Nayeon
Lee, Wenliang Dai, Dan Su, Bryan Wilie,
Holy Lovenia, Ziwei Ji, Tiezheng Yu, Willy
Chung, et al. 2023. A multitask,
multilingual, multimodal evaluation of
chatgpt on reasoning, hallucination, and
interactivity. ArXiv preprint,
abs/2302.04023.

Barberá, Pablo, Ning Wang, Richard

Bonneau, John T Jost, Jonathan Nagler,
Joshua Tucker, and Sandra
González-Bailón. 2015. The critical
periphery in the growth of social protests.
PloS one, 10(11):e0143611.

Beltagy, Iz, Matthew E Peters, and Arman

Cohan. 2020. Longformer: The
long-document transformer. ArXiv
preprint, abs/2004.05150.

Bail, Christopher A. 2023. Can generative ai

Belz, Anja and Eric Kow. 2010. Comparing

improve social science?

Bakhtin, Mikhail Mikha˘ılovich. 2010. Speech
genres and other late essays. University of
Texas press.

Baly, Ramy, Giovanni Da San Martino, James
Glass, and Preslav Nakov. 2020. We can
detect your bias: Predicting the political
ideology of news articles. In Proceedings of
the 2020 Conference on Empirical Methods in

rating scales and preference judgements in
language evaluation. In Proceedings of the
6th International Natural Language
Generation Conference.

Bender, Emily M, Timnit Gebru, Angelina

McMillan-Major, and Shmargaret
Shmitchell. 2021. On the dangers of
stochastic parrots: Can language models
be too big? In Proceedings of the 2021 ACM

37

Computational Linguistics

Volume 50, Number 1

conference on fairness, accountability, and
transparency, pages 610–623.

Berelson, Bernard. 1952. Content analysis in

communication research.

Box-Steffensmeier, Janet M and Bradford S

Jones. 2004. Event history modeling: A guide
for social scientists. Cambridge University
Press.

van den Berg, Esther, Katharina Korfhage,

Boyd, Ryan L, Kate G Blackburn, and

Josef Ruppenhofer, Michael Wiegand, and
Katja Markert. 2020. Doctor who? framing
through names and titles in German. In
Proceedings of the 12th Language Resources
and Evaluation Conference, pages
4924–4932, European Language Resources
Association, Marseille, France.

Bhatia, Sudeep. 2017. Associative judgment
and vector space semantics. Psychological
review, 124(1):1.

Bicchieri, Cristina. 2005. The grammar of

society: The nature and dynamics of social
norms. Cambridge University Press.
Black, Ryan C, Sarah A Treul, Timothy R
Johnson, and Jerry Goldman. 2011.
Emotions, oral arguments, and supreme
court decision making. The Journal of
Politics, 73(2):572–581.

Blodgett, Su Lin, Solon Barocas, Hal

Daumé III, and Hanna Wallach. 2020.
Language (technology) is power: A critical
survey of “bias” in NLP. In Proceedings of
the 58th Annual Meeting of the Association
for Computational Linguistics, pages
5454–5476, Association for Computational
Linguistics, Online.

Bollen, Johan, Huina Mao, and Xiaojun Zeng.

2011. Twitter mood predicts the stock
market. Journal of computational science,
2(1):1–8.

Bommasani, Rishi, Kathleen A Creel,

Ananya Kumar, Dan Jurafsky, and Percy S
Liang. 2022. Picking on the same person:
Does algorithmic monoculture lead to
outcome homogenization? Advances in
Neural Information Processing Systems,
35:3663–3678.

Bommasani, Rishi, Drew A Hudson, Ehsan

Adeli, Russ Altman, Simran Arora,
Sydney von Arx, Michael S Bernstein,
Jeannette Bohg, Antoine Bosselut, Emma
Brunskill, et al. 2021. On the opportunities
and risks of foundation models. ArXiv
preprint, abs/2108.07258.

Borchers, Conrad, Dalia Gala, Benjamin

Gilburt, Eduard Oravkin, Wilfried Bounsi,
Yuki M Asano, and Hannah Kirk. 2022.
Looking for a handsome carpenter!
debiasing GPT-3 job advertisements. In
Proceedings of the 4th Workshop on Gender
Bias in Natural Language Processing
(GeBNLP), pages 212–224, Association for
Computational Linguistics, Seattle,
Washington.

38

James W Pennebaker. 2020. The narrative
arc: Revealing core narrative structures
through text analysis. Science advances,
6(32):eaba2196.

Brahman, Faeze and Snigdha Chaturvedi.

2020. Modeling protagonist emotions for
emotion-aware storytelling. In Proceedings
of the 2020 Conference on Empirical Methods
in Natural Language Processing (EMNLP),
pages 5277–5294, Association for
Computational Linguistics, Online.
Bramsen, Philip, Martha Escobar-Molano,
Ami Patel, and Rafael Alonso. 2011.
Extracting social power relationships from
natural language. In Proceedings of the 49th
Annual Meeting of the Association for
Computational Linguistics: Human Language
Technologies, pages 773–782, Association
for Computational Linguistics, Portland,
Oregon, USA.

Brooke, Julian, Adam Hammond, and

Timothy Baldwin. 2016. Bootstrapped
text-level named entity recognition for
literature. In Proceedings of the 54th Annual
Meeting of the Association for Computational
Linguistics (Volume 2: Short Papers), pages
344–350, Association for Computational
Linguistics, Berlin, Germany.

Brown, Penelope and Stephen C Levinson.

1987. Politeness: Some universals in language
usage, volume 4. Cambridge university
press.

Brown, Tom B., Benjamin Mann, Nick Ryder,
Melanie Subbiah, Jared Kaplan, Prafulla
Dhariwal, Arvind Neelakantan, Pranav
Shyam, Girish Sastry, Amanda Askell,
Sandhini Agarwal, Ariel Herbert-Voss,
Gretchen Krueger, Tom Henighan, Rewon
Child, Aditya Ramesh, Daniel M. Ziegler,
Jeffrey Wu, Clemens Winter, Christopher
Hesse, Mark Chen, Eric Sigler, Mateusz
Litwin, Scott Gray, Benjamin Chess, Jack
Clark, Christopher Berner, Sam
McCandlish, Alec Radford, Ilya Sutskever,
and Dario Amodei. 2020. Language
models are few-shot learners. In Advances
in Neural Information Processing Systems 33:
Annual Conference on Neural Information
Processing Systems 2020, NeurIPS 2020,
December 6-12, 2020, virtual.

Bucholtz, Mary and Kira Hall. 2005. Identity
and interaction: A sociocultural linguistic
approach. Discourse studies, 7(4-5):585–614.

Ziems, Held, Shaikh, Chen, Zhang, Yang

Can LLMs Transform CSS?

Buechel, Sven, Anneke Buffone, Barry Slaff,

Lyle Ungar, and João Sedoc. 2018.
Modeling empathy and distress in
reaction to news stories. In Proceedings of
the 2018 Conference on Empirical Methods in
Natural Language Processing, pages
4758–4765, Association for Computational
Linguistics, Brussels, Belgium.
Bunt, Harry, Jan Alexandersson, Jean

Carletta, Jae-Woong Choe, Alex Chengyu
Fang, Koiti Hasida, Kiyong Lee, Volha
Petukhova, Andrei Popescu-Belis, Laurent
Romary, Claudia Soria, and David Traum.
2010. Towards an ISO standard for
dialogue act annotation. In Proceedings of
the Seventh International Conference on
Language Resources and Evaluation
(LREC’10), European Language Resources
Association (ELRA), Valletta, Malta.

Burke, Moira and Robert Kraut. 2008. Mind
your ps and qs: the impact of politeness
and rudeness in online communities. In
Proceedings of the 2008 ACM conference on
Computer supported cooperative work, pages
281–284.

Caciularu, Avi, Arman Cohan, Iz Beltagy,
Matthew E Peters, Arie Cattan, and Ido
Dagan. 2021. Cdlm: Cross-document
language modeling. In Findings of the
Association for Computational Linguistics:
EMNLP 2021, pages 2648–2662.
Carlini, Nicholas, Florian Tramer, Eric
Wallace, Matthew Jagielski, Ariel
Herbert-Voss, Katherine Lee, Adam
Roberts, Tom Brown, Dawn Song, Ulfar
Erlingsson, et al. 2021. Extracting training
data from large language models. In 30th
USENIX Security Symposium (USENIX
Security 21), pages 2633–2650.

Carlo, Valerio Di, Federico Bianchi, and
Matteo Palmonari. 2019. Training
temporal word embeddings with a
compass. In The Thirty-Third AAAI
Conference on Artificial Intelligence, AAAI
2019, The Thirty-First Innovative
Applications of Artificial Intelligence
Conference, IAAI 2019, The Ninth AAAI
Symposium on Educational Advances in
Artificial Intelligence, EAAI 2019, Honolulu,
Hawaii, USA, January 27 - February 1, 2019,
pages 6326–6334, AAAI Press.

Centola, Damon, Joshua Becker, Devon

Brackbill, and Andrea Baronchelli. 2018.
Experimental evidence for tipping points
in social convention. Science,
360(6393):1116–1119.

Chaganty, Arun, Stephen Mussmann, and

Percy Liang. 2018. The price of debiasing
automatic metrics in natural language

evalaution. In Proceedings of the 56th
Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long
Papers), pages 643–653, Association for
Computational Linguistics, Melbourne,
Australia.

Chakrabarty, Tuhin, Debanjan Ghosh, Adam
Poliak, and Smaranda Muresan. 2021.
Figurative language in recognizing textual
entailment. In Findings of the Association for
Computational Linguistics: ACL-IJCNLP
2021, pages 3354–3361, Association for
Computational Linguistics, Online.
Chakrabarty, Tuhin, Arkadiy Saakyan,

Debanjan Ghosh, and Smaranda Muresan.
2022. Flute: Figurative language
understanding through textual
explanations. In Proceedings of the 2022
Conference on Empirical Methods in Natural
Language Processing, pages 7139–7159.
Chambers, Nathanael and Dan Jurafsky.

2008. Unsupervised learning of narrative
event chains. In Proceedings of ACL-08:
HLT, pages 789–797, Association for
Computational Linguistics, Columbus,
Ohio.

Chang, Jonathan, Jordan L. Boyd-Graber,

Sean Gerrish, Chong Wang, and David M.
Blei. 2009. Reading tea leaves: How
humans interpret topic models. In
Advances in Neural Information Processing
Systems 22: 23rd Annual Conference on
Neural Information Processing Systems 2009.
Proceedings of a meeting held 7-10 December
2009, Vancouver, British Columbia, Canada,
pages 288–296, Curran Associates, Inc.
Chang, Jonathan P., Caleb Chiam, Liye Fu,

Andrew Wang, Justine Zhang, and
Cristian Danescu-Niculescu-Mizil. 2020.
ConvoKit: A toolkit for the analysis of
conversations. In Proceedings of the 21th
Annual Meeting of the Special Interest Group
on Discourse and Dialogue, pages 57–60,
Association for Computational
Linguistics, 1st virtual meeting.

Chen, Derek, Zhou Yu, and Samuel Bowman.
2022. Clean or annotate: How to spend a
limited data collection budget. In
Proceedings of the Third Workshop on Deep
Learning for Low-Resource Natural Language
Processing, pages 152–168.

Chen, Peng-Yu and Von-Wun Soo. 2018.

Humor recognition using deep learning.
In Proceedings of the 2018 Conference of the
North American Chapter of the Association for
Computational Linguistics: Human Language
Technologies, Volume 2 (Short Papers), pages
113–117, Association for Computational
Linguistics, New Orleans, Louisiana.

39

Computational Linguistics

Volume 50, Number 1

Cheng, Justin, Lada A. Adamic, Jon M.

Kleinberg, and Jure Leskovec. 2016. Do
cascades recur? In Proceedings of the 25th
International Conference on World Wide Web,
WWW 2016, Montreal, Canada, April 11 - 15,
2016, pages 671–681, ACM.

Cheng, Justin, Michael Bernstein, Cristian
Danescu-Niculescu-Mizil, and Jure
Leskovec. 2017. Anyone can become a
troll: Causes of trolling behavior in online
discussions. In Proceedings of the 2017 ACM
conference on computer supported cooperative
work and social computing, pages 1217–1230.

Cheng, Justin, Cristian

Danescu-Niculescu-Mizil, and Jure
Leskovec. 2015. Antisocial behavior in
online discussion communities. In
Proceedings of the international aaai
conference on web and social media,
volume 9, pages 61–70.

Child, Rewon, Scott Gray, Alec Radford, and
Ilya Sutskever. 2019. Generating long
sequences with sparse transformers.
ArXiv preprint, abs/1904.10509.

Christiano, Paul F., Jan Leike, Tom B. Brown,
Miljan Martic, Shane Legg, and Dario
Amodei. 2017. Deep reinforcement
learning from human preferences. In
Advances in Neural Information Processing
Systems 30: Annual Conference on Neural
Information Processing Systems 2017,
December 4-9, 2017, Long Beach, CA, USA,
pages 4299–4307.

Chu, Eric, Jacob Andreas, Stephen

Ansolabehere, and Deb Roy. 2023.
Language models trained on media diets
can predict public opinion. ArXiv preprint,
abs/2303.16779.

Chu, Eric, Prashanth Vijayaraghavan, and
Deb Roy. 2018. Learning personas from
dialogue with attentive memory networks.
In Proceedings of the 2018 Conference on
Empirical Methods in Natural Language
Processing, pages 2638–2646, Association
for Computational Linguistics, Brussels,
Belgium.

Chung, Hyung Won, Le Hou, Shayne

Longpre, Barret Zoph, Yi Tay, William
Fedus, Eric Li, Xuezhi Wang, Mostafa
Dehghani, Siddhartha Brahma, et al. 2022.
Scaling instruction-finetuned language
models. ArXiv preprint, abs/2210.11416.
Cialdini, Robert B. 2003. Influence. Influence

At Work.

Coll Ardanuy, Mariona, Federico Nanni,
Kaspar Beelen, Kasra Hosseini, Ruth
Ahnert, Jon Lawrence, Katherine
McDonough, Giorgia Tolfo, Daniel CS
Wilson, and Barbara McGillivray. 2020.

40

Living machines: A study of atypical
animacy. In Proceedings of the 28th
International Conference on Computational
Linguistics, pages 4534–4545, International
Committee on Computational Linguistics,
Barcelona, Spain (Online).

Cotfas, Liviu-Adrian, Camelia Delcea, Ioan

Roxin, Corina Ioan˘a¸s, Dana Simona
Gherai, and Federico Tajariol. 2021. The
longest month: analyzing covid-19
vaccination opinions dynamics from
tweets in the month following the first
vaccine announcement. Ieee Access,
9:33203–33223.

Coulton, Paul, Jonny Huck, Andrew

Hudson-Smith, Ralph Barthel, Panagiotis
Mavros, Jennifer Roberts, and Philip
Powell. 2014. Designing interactive
systems to encourage empathy between
users. In Proceedings of the 2014 companion
publication on Designing interactive systems.
pages 13–16.

Craig, Holly K and Julie A Washington. 2002.
Oral language expectations for african
american preschoolers and kindergartners.

Danescu-Niculescu-Mizil, Cristian, Lillian

Lee, Bo Pang, and Jon M. Kleinberg. 2012.
Echoes of power: language effects and
power differences in social interaction. In
Proceedings of the 21st World Wide Web
Conference 2012, WWW 2012, Lyon, France,
April 16-20, 2012, pages 699–708, ACM.
Danescu-Niculescu-Mizil, Cristian, Moritz

Sudhof, Dan Jurafsky, Jure Leskovec, and
Christopher Potts. 2013. A computational
approach to politeness with application to
social factors. In Proceedings of the 51st
Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long
Papers), pages 250–259, Association for
Computational Linguistics, Sofia,
Bulgaria.

Dang, Hoa Trang. 2005. Overview of duc
2005. In Proceedings of the document
understanding conference, volume 2005,
pages 1–12, Citeseer.

Davies, Catherine E. 2017. Sociolinguistic
approaches to humor. In The Routledge
handbook of language and humor. Routledge,
pages 472–488.

Del Tredici, Marco and Raquel Fernández.

2017. Semantic variation in online
communities of practice. In IWCS 2017 -
12th International Conference on
Computational Semantics - Long papers.
DeLozier, Grant, Ben Wing, Jason Baldridge,
and Scott Nesbit. 2016. Creating a novel
geolocation corpus from historical texts. In
Proceedings of the 10th Linguistic Annotation

Ziems, Held, Shaikh, Chen, Zhang, Yang

Can LLMs Transform CSS?

Workshop held in conjunction with ACL 2016
(LAW-X 2016), pages 188–198, Association
for Computational Linguistics, Berlin,
Germany.

Demszky, Dorottya, Nikhil Garg, Rob Voigt,

James Zou, Jesse Shapiro, Matthew
Gentzkow, and Dan Jurafsky. 2019.
Analyzing polarization in social media:
Method and application to tweets on 21
mass shootings. In Proceedings of the 2019
Conference of the North American Chapter of
the Association for Computational Linguistics:
Human Language Technologies, Volume 1
(Long and Short Papers), pages 2970–3005,
Association for Computational
Linguistics, Minneapolis, Minnesota.

Demszky, Dorottya, Devyani Sharma,

Jonathan Clark, Vinodkumar
Prabhakaran, and Jacob Eisenstein. 2021.
Learning to recognize dialect features. In
Proceedings of the 2021 Conference of the
North American Chapter of the Association for
Computational Linguistics: Human Language
Technologies, pages 2315–2338, Association
for Computational Linguistics, Online.
Dhamala, Jwala, Tony Sun, Varun Kumar,

Satyapriya Krishna, Yada Pruksachatkun,
Kai-Wei Chang, and Rahul Gupta. 2021.
Bold: Dataset and metrics for measuring
biases in open-ended language generation.
In Proceedings of the 2021 ACM conference
on fairness, accountability, and transparency,
pages 862–872.

DiMaggio, Paul. 2015. Adapting

computational text analysis to social
science (and vice versa). Big Data &
Society, 2(2):2053951715602908.

DiMaggio, Paul, Manish Nag, and David
Blei. 2013. Exploiting affinities between
topic modeling and the sociological
perspective on culture: Application to
newspaper coverage of us government
arts funding. Poetics, 41(6):570–606.
Dobson, James E. 2019. Critical digital

humanities: the search for a methodology.
University of Illinois Press.

Easley, David and Jon Kleinberg. 2010.

Networks, crowds, and markets: Reasoning
about a highly connected world. Cambridge
university press.

Egami, Naoki, Musashi Jacobs-Harukawa,
Brandon M Stewart, and Hanying Wei.
2023. Using large language model
annotations for valid downstream
statistical inference in social science:
Design-based semi-supervised learning.
ArXiv preprint, abs/2306.04746.
Eisenstein, Jacob. 2012. Mapping the

geographical diffusion of new words.

ArXiv preprint, abs/1210.5268.
Eisenstein, Jacob, Brendan O’Connor,

Noah A Smith, and Eric P Xing. 2014.
Diffusion of lexical change in social media.
PloS one, 9(11):e113114.

Eisenstein, Jacob, Vinodkumar Prabhakaran,
Clara Rivera, Dorottya Demszky, and
Devyani Sharma. 2023. Md3: The
multi-dialect dataset of dialogues. ArXiv
preprint, abs/2305.11355.

Eisenstein, Jacob, Noah A. Smith, and Eric P.
Xing. 2011. Discovering sociolinguistic
associations with structured sparsity. In
Proceedings of the 49th Annual Meeting of the
Association for Computational Linguistics:
Human Language Technologies, pages
1365–1374, Association for Computational
Linguistics, Portland, Oregon, USA.

Ellsberg, Daniel. 1961. Risk, ambiguity, and
the savage axioms. The quarterly journal of
economics, 75(4):643–669.

ElSherief, Mai, Caleb Ziems, David

Muchlinski, Vaishnavi Anupindi, Jordyn
Seybolt, Munmun De Choudhury, and
Diyi Yang. 2021. Latent hatred: A
benchmark for understanding implicit
hate speech. ArXiv preprint,
abs/2109.05322.

Entman, Robert M. 1993. Framing: Toward
clarification of a fractured paradigm.
Journal of communication, 43(4):51–58.
Evans, James A and Pedro Aceves. 2016.

Machine translation: Mining text for social
theory. Annual review of sociology, 42:21–50.

Fabbri, Alexander R, Wojciech Kry´sci ´nski,
Bryan McCann, Caiming Xiong, Richard
Socher, and Dragomir Radev. 2021.
Summeval: Re-evaluating summarization
evaluation. Transactions of the Association
for Computational Linguistics, 9:391–409.

Fazeen, Mohamed, Ram Dantu, and

Parthasarathy Guturu. 2011. Identification
of leaders, lurkers, associates and
spammers in a social network:
context-dependent and
context-independent approaches. Social
Network Analysis and Mining, 1(3):241–254.
Field, Anjalie, Doron Kliger, Shuly Wintner,
Jennifer Pan, Dan Jurafsky, and Yulia
Tsvetkov. 2018. Framing and
agenda-setting in Russian news: a
computational analysis of intricate
political strategies. In Proceedings of the
2018 Conference on Empirical Methods in
Natural Language Processing, pages
3570–3580, Association for Computational
Linguistics, Brussels, Belgium.

Flores, René D. 2017. Do anti-immigrant

laws shape public sentiment? a study of

41

Computational Linguistics

Volume 50, Number 1

arizona’s sb 1070 using twitter data.
American Journal of Sociology,
123(2):333–384.

Gabriel, Saadia, Skyler Hallinan, Maarten
Sap, Pemi Nguyen, Franziska Roesner,
Eunsol Choi, and Yejin Choi. 2022. Misinfo
reaction frames: Reasoning about readers’
reactions to news headlines. In Proceedings
of the 60th Annual Meeting of the Association
for Computational Linguistics (Volume 1:
Long Papers), pages 3108–3127.

Gao, Ge, Eunsol Choi, Yejin Choi, and Luke
Zettlemoyer. 2018. Neural metaphor
detection in context. In Proceedings of the
2018 Conference on Empirical Methods in
Natural Language Processing, pages
607–613, Association for Computational
Linguistics, Brussels, Belgium.
Garfinkel, Harold. 2016. Studies in

ethnomethodology. In Social Theory
Re-Wired. Routledge, pages 85–95.
Garg, Nikhil, Londa Schiebinger, Dan

Jurafsky, and James Zou. 2018. Word
embeddings quantify 100 years of gender
and ethnic stereotypes. Proceedings of the
National Academy of Sciences,
115(16):E3635–E3644.

Gerber, Alan S, Gregory A Huber, David

Doherty, Conor M Dowling, and Shang E
Ha. 2010. Personality and political
attitudes: Relationships across issue
domains and political contexts. American
Political Science Review, 104(1):111–133.
Gilardi, Fabrizio, Meysam Alizadeh, and

Maël Kubli. 2023. Chatgpt outperforms
crowd-workers for text-annotation tasks.
ArXiv preprint, abs/2303.15056.

Golder, Scott A and Michael W Macy. 2014.
Digital footprints: Opportunities and
challenges for online social research.
Annual Review of Sociology, 40:129–152.
Gomez-Zara, Diego, Miriam Boon, and Larry

Birnbaum. 2018. Who is the hero, the
villain, and the victim? detection of roles
in news articles using natural language
techniques. In 23rd International Conference
on Intelligent User Interfaces, pages 311–315.

Goyal, Tanya, Junyi Jessy Li, and Greg

Durrett. 2022. News summarization and
evaluation in the era of gpt-3. ArXiv
preprint, abs/2209.12356.

Graham, Elizabeth E. 1995. The involvement
of sense of humor in the development of
social relationships. Communication
Reports, 8(2):158–169.

Grimmer, Justin. 2010. A bayesian

hierarchical topic model for political texts:
Measuring expressed agendas in senate
press releases. Political Analysis, 18(1):1–35.

42

Gross, Justin H, Brice Acree, Yanchuan Sim,
and Noah A Smith. 2013. Testing the
etch-a-sketch hypothesis: a computational
analysis of mitt romney’s ideological
makeover during the 2012 primary vs.
general elections. In APSA 2013 Annual
Meeting Paper, American Political Science
Association 2013 Annual Meeting.

Grudin, Jonathan. 2006. Why personas work:
The psychological evidence. The persona
lifecycle, 12:642–664.

Hamilton, William L., Jure Leskovec, and
Dan Jurafsky. 2016a. Cultural shift or
linguistic drift? comparing two
computational measures of semantic
change. In Proceedings of the 2016
Conference on Empirical Methods in Natural
Language Processing, pages 2116–2121,
Association for Computational
Linguistics, Austin, Texas.

Hamilton, William L., Jure Leskovec, and
Dan Jurafsky. 2016b. Diachronic word
embeddings reveal statistical laws of
semantic change. In Proceedings of the 54th
Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long
Papers), pages 1489–1501, Association for
Computational Linguistics, Berlin,
Germany.

Harzing, Anne-Wil, Joyce Baldueza, Wilhelm
Barner-Rasmussen, Cordula Barzantny,
Anne Canabal, Anabella Davila, Alvaro
Espejo, Rita Ferreira, Axele Giroud,
Kathrin Koester, et al. 2009. Rating versus
ranking: What is the best way to reduce
response and language bias in
cross-national research? International
business review, 18(4):417–432.

Hashim, Safair Safwat Mohammed and
Suhair Safwat. 2015. Speech acts in
political speeches. Journal of Modern
Education Review, 5(7):699–706.

Hendrycks, Dan, Collin Burns, Steven Basart,
Andy Zou, Mantas Mazeika, Dawn Song,
and Jacob Steinhardt. 2021. Measuring
massive multitask language
understanding. In International Conference
on Learning Representations.

Herring, Susan C. 1994. Politeness in

computer culture: Why women thank and
men flame. In Cultural performances:
Proceedings of the third Berkeley women and
language conference, pages 278–294.

Hirsh, Jacob B, Sonia K Kang, and Galen V

Bodenhausen. 2012. Personalized
persuasion: Tailoring persuasive appeals
to recipients’ personality traits.
Psychological science, 23(6):578–581.

Ziems, Held, Shaikh, Chen, Zhang, Yang

Can LLMs Transform CSS?

Hoffmann, Jordan, Sebastian Borgeaud,
Arthur Mensch, Elena Buchatskaya,
Trevor Cai, Eliza Rutherford, Diego de Las
Casas, Lisa Anne Hendricks, Johannes
Welbl, Aidan Clark, et al. 2022. Training
compute-optimal large language models.
ArXiv preprint, abs/2203.15556.
Hofman, Jake M, Amit Sharma, and

Duncan J Watts. 2017. Prediction and
explanation in social systems. Science,
355(6324):486–488.

Huguet Cabot, Pere-Lluís, Verna Dankers,

David Abadi, Agneta Fischer, and
Ekaterina Shutova. 2020. The Pragmatics
behind Politics: Modelling Metaphor,
Framing and Emotion in Political
Discourse. In Findings of the Association for
Computational Linguistics: EMNLP 2020,
pages 4479–4488, Association for
Computational Linguistics, Online.
Hürriyeto ˘glu, Ali, Hristo Tanev, Vanni
Zavarella, Jakub Piskorski, Reyyan
Yeniterzi, Deniz Yuret, and Aline
Villavicencio. 2021. Challenges and
applications of automated extraction of
socio-political events from text (CASE
2021): Workshop and shared task report.
In Proceedings of the 4th Workshop on
Challenges and Applications of Automated
Extraction of Socio-political Events from Text
(CASE 2021), pages 1–9, Association for
Computational Linguistics, Online.
Hutchby, Ian and Robin Wooffitt. 2008.

Conversation analysis. Polity.

Ignatow, Gabe and Rada Mihalcea. 2016. Text
mining: A guidebook for the social sciences.
Sage Publications.

Iyengar, Shanto. 1990. Framing responsibility
for political issues: The case of poverty.
Political behavior, 12(1):19–40.

Iyer, Adith, Aditya Joshi, Sarvnaz Karimi,
Ross Sparks, and Cecile Paris. 2019.
Figurative usage detection of symptom
words to improve personal health mention
detection. In Proceedings of the 57th Annual
Meeting of the Association for Computational
Linguistics, pages 1142–1147, Association
for Computational Linguistics, Florence,
Italy.

Iyyer, Mohit, Peter Enns, Jordan

Boyd-Graber, and Philip Resnik. 2014.
Political ideology detection using
recursive neural networks. In Proceedings
of the 52nd Annual Meeting of the Association
for Computational Linguistics (Volume 1:
Long Papers), pages 1113–1122, Association
for Computational Linguistics, Baltimore,
Maryland.

Iyyer, Mohit, Anupam Guha, Snigdha

Chaturvedi, Jordan Boyd-Graber, and Hal
Daumé III. 2016. Feuding families and
former Friends: Unsupervised learning for
dynamic fictional relationships. In
Proceedings of the 2016 Conference of the
North American Chapter of the Association for
Computational Linguistics: Human Language
Technologies, pages 1534–1544, Association
for Computational Linguistics, San Diego,
California.

Jacobs, Arthur M and Annette Kinder. 2018.
What makes a metaphor literary? answers
from two computational studies. Metaphor
and Symbol, 33(2):85–100.

Jahan, Labiba, Rahul Mittal, and Mark

Finlayson. 2021. Inducing stereotypical
character roles from plot structure. In
Proceedings of the 2021 Conference on
Empirical Methods in Natural Language
Processing, pages 492–497.

Jelveh, Zubin, Bruce Kogut, and Suresh

Naidu. 2014. Detecting latent ideology in
expert text: Evidence from academic
papers in economics. In Proceedings of the
2014 Conference on Empirical Methods in
Natural Language Processing (EMNLP),
pages 1804–1809, Association for
Computational Linguistics, Doha, Qatar.
Jenhani, Ferdaous, Mohamed Salah Gouider,

and Lamjed Ben Said. 2016. A hybrid
approach for drug abuse events extraction
from twitter. Procedia computer science,
96:1032–1040.

Jochim, Charles, Francesca Bonin, Roy

Bar-Haim, and Noam Slonim. 2018. SLIDE
- a sentiment lexicon of common idioms.
In Proceedings of the Eleventh International
Conference on Language Resources and
Evaluation (LREC 2018), European
Language Resources Association (ELRA),
Miyazaki, Japan.

Jockers, Matthew L and David Mimno. 2013.

Significant themes in 19th-century
literature. Poetics, 41(6):750–769.
Johnson, Kristen, I-Ta Lee, and Dan

Goldwasser. 2017. Ideological phrase
indicators for classification of political
discourse framing on Twitter. In
Proceedings of the Second Workshop on NLP
and Computational Social Science, pages
90–99, Association for Computational
Linguistics, Vancouver, Canada.
Jones, Erik and Jacob Steinhardt. 2022.
Capturing failures of large language
models via human cognitive biases. ArXiv
preprint, abs/2202.12299.

Joshi, Aditya, Pushpak Bhattacharyya, and

Mark J Carman. 2017. Automatic sarcasm

43

Computational Linguistics

Volume 50, Number 1

detection: A survey. ACM Computing
Surveys (CSUR), 50(5):1–22.

Kaplan, Jared, Sam McCandlish, Tom

Henighan, Tom B Brown, Benjamin Chess,
Rewon Child, Scott Gray, Alec Radford,
Jeffrey Wu, and Dario Amodei. 2020.
Scaling laws for neural language models.
ArXiv preprint, abs/2001.08361.

Karpinska, Marzena, Nader Akoury, and
Mohit Iyyer. 2021. The perils of using
Mechanical Turk to evaluate open-ended
text generation. In Proceedings of the 2021
Conference on Empirical Methods in Natural
Language Processing, pages 1265–1285,
Association for Computational
Linguistics, Online and Punta Cana,
Dominican Republic.

Kershaw, Daniel, Matthew Rowe, and

Patrick Stacey. 2016. Towards modelling
language innovation acceptance in online
social networks. In Proceedings of the Ninth
ACM International Conference on Web Search
and Data Mining, San Francisco, CA, USA,
February 22-25, 2016, pages 553–562, ACM.

Kesarwani, Vaibhav, Diana Inkpen, Stan

Szpakowicz, and Chris Tanasescu. 2017.
Metaphor detection in a poetry corpus. In
Proceedings of the Joint SIGHUM Workshop
on Computational Linguistics for Cultural
Heritage, Social Sciences, Humanities and
Literature, pages 1–9, Association for
Computational Linguistics, Vancouver,
Canada.

Keuschnigg, Marc, Niclas Lovsjö, and Peter
Hedström. 2018. Analytical sociology and
computational social science. Journal of
Computational Social Science, 1(1):3–14.

Kiela, Douwe, Max Bartolo, Yixin Nie,
Divyansh Kaushik, Atticus Geiger,
Zhengxuan Wu, Bertie Vidgen, Grusha
Prasad, Amanpreet Singh, Pratik Ringshia,
Zhiyi Ma, Tristan Thrush, Sebastian
Riedel, Zeerak Waseem, Pontus Stenetorp,
Robin Jia, Mohit Bansal, Christopher Potts,
and Adina Williams. 2021. Dynabench:
Rethinking benchmarking in NLP. In
Proceedings of the 2021 Conference of the
North American Chapter of the Association for
Computational Linguistics: Human Language
Technologies, pages 4110–4124, Association
for Computational Linguistics, Online.

Kim, Tae-Yeol, Deog-Ro Lee, and Noel

Yuen Shan Wong. 2016. Supervisor humor
and employee outcomes: The role of social
distance and affective trust in supervisor.
Journal of Business and Psychology,
31:125–139.

Kim, Yoon, Yi-I Chiu, Kentaro Hanaki,

Darshan Hegde, and Slav Petrov. 2014.

44

Temporal analysis of language through
neural language models. In Proceedings of
the ACL 2014 Workshop on Language
Technologies and Computational Social
Science, pages 61–65, Association for
Computational Linguistics, Baltimore,
MD, USA.

King, Gary and Will Lowe. 2003. An

automated information extraction tool for
international conflict data with
performance as good as human coders: A
rare events evaluation design. International
Organization, 57(3):617–642.

Kirby, Simon, Mike Dowman, and Thomas L
Griffiths. 2007. Innateness and culture in
the evolution of language. Proceedings of
the National Academy of Sciences,
104(12):5241–5245.

Kleinberg, Jon, Himabindu Lakkaraju, Jure
Leskovec, Jens Ludwig, and Sendhil
Mullainathan. 2018. Human decisions and
machine predictions. The quarterly journal
of economics, 133(1):237–293.

Kleinberg, Jon and Manish Raghavan. 2021.

Algorithmic monoculture and social
welfare. Proceedings of the National
Academy of Sciences, 118(22):e2018340118.

Koralus, Philipp and Vincent

Wang-Ma´scianica. 2023. Humans in
humans out: On gpt converging toward
common sense in both success and failure.
ArXiv preprint, abs/2303.17276.

Kosinski, Michal, David Stillwell, and Thore
Graepel. 2013. Private traits and attributes
are predictable from digital records of
human behavior. Proceedings of the national
academy of sciences, 110(15):5802–5805.

Kozlowski, Austin C, Matt Taddy, and

James A Evans. 2019. The geometry of
culture: Analyzing the meanings of class
through word embeddings. American
Sociological Review, 84(5):905–949.
Kuhn, Thomas S. 1962. The structure of

Scientific Revolutions. The University of
Chicago Press.

Kuipers, Giselinde. 2009. Humor styles and

symbolic boundaries.

Kulkarni, Vivek, Rami Al-Rfou, Bryan
Perozzi, and Steven Skiena. 2015.
Statistically significant detection of
linguistic change. In Proceedings of the 24th
International Conference on World Wide Web,
WWW 2015, Florence, Italy, May 18-22,
2015, pages 625–635, ACM.

Kwak, Haewoon, Jeremy Blackburn, and

Seungyeop Han. 2015. Exploring
cyberbullying and other toxic behavior in
team competition online games. In
Proceedings of the 33rd Annual ACM

Ziems, Held, Shaikh, Chen, Zhang, Yang

Can LLMs Transform CSS?

Conference on Human Factors in Computing
Systems, CHI 2015, Seoul, Republic of Korea,
April 18-23, 2015, pages 3739–3748, ACM.

Labatut, Vincent and Xavier Bost. 2019.
Extraction and analysis of fictional
character networks: A survey. ACM
Computing Surveys (CSUR), 52(5):1–40.
Lai, Mirko, Alessandra Teresa Cignarella,
Delia Irazú Hernández Farías, Cristina
Bosco, Viviana Patti, and Paolo Rosso.
2020. Multilingual stance detection in
social media political debates. Computer
Speech & Language, 63:101075.

Lai, Viet, Minh Van Nguyen, Heidi Kaufman,

and Thien Huu Nguyen. 2021. Event
extraction from historical texts: A new
dataset for black rebellions. In Findings of
the Association for Computational Linguistics:
ACL-IJCNLP 2021, pages 2390–2400,
Association for Computational
Linguistics, Online.

Lazer, David, Alex Pentland, Lada Adamic,

Sinan Aral, Albert-László Barabási, Devon
Brewer, Nicholas Christakis, Noshir
Contractor, James Fowler, Myron
Gutmann, et al. 2009. Computational
social science. Science, 323(5915):721–723.
Lazer, David MJ, Matthew A Baum, Yochai

Benkler, Adam J Berinsky, Kelly M
Greenhill, Filippo Menczer, Miriam J
Metzger, Brendan Nyhan, Gordon
Pennycook, David Rothschild, et al. 2018.
The science of fake news. Science,
359(6380):1094–1096.

Lazer, David MJ, Alex Pentland, Duncan J
Watts, Sinan Aral, Susan Athey, Noshir
Contractor, Deen Freelon, Sandra
Gonzalez-Bailon, Gary King, Helen
Margetts, et al. 2020. Computational social
science: Obstacles and opportunities.
Science, 369(6507):1060–1062.

Lemmens, Jens, Ilia Markov, and Walter

Daelemans. 2021. Improving hate speech
type and target detection with hateful
metaphor features. In Proceedings of the
Fourth Workshop on NLP for Internet
Freedom: Censorship, Disinformation, and
Propaganda, pages 7–16, Association for
Computational Linguistics, Online.
Leskovec, Jure, Lars Backstrom, and Jon

Kleinberg. 2009. Meme-tracking and the
dynamics of the news cycle. In Proceedings
of the 15th ACM SIGKDD international
conference on Knowledge discovery and data
mining, pages 497–506.

Li, Sha, Heng Ji, and Jiawei Han. 2021.
Document-level event argument
extraction by conditional generation. In
Proceedings of the 2021 Conference of the

North American Chapter of the Association for
Computational Linguistics: Human Language
Technologies, pages 894–908, Association
for Computational Linguistics, Online.
Li, Shuang, Xavier Puig, Chris Paxton, Yilun
Du, Clinton Wang, Linxi Fan, Tao Chen,
De-An Huang, Ekin Akyürek, Anima
Anandkumar, et al. 2022. Pre-trained
language models for interactive
decision-making. Advances in Neural
Information Processing Systems,
35:31199–31212.

Liang, Percy, Rishi Bommasani, Tony Lee,

Dimitris Tsipras, Dilara Soylu, Michihiro
Yasunaga, Yian Zhang, Deepak
Narayanan, Yuhuai Wu, Ananya Kumar,
et al. 2022. Holistic evaluation of language
models. ArXiv preprint, abs/2211.09110.
Liu, Chia-Wei, Ryan Lowe, Iulian Serban,

Mike Noseworthy, Laurent Charlin, and
Joelle Pineau. 2016. How NOT to evaluate
your dialogue system: An empirical study
of unsupervised evaluation metrics for
dialogue response generation. In
Proceedings of the 2016 Conference on
Empirical Methods in Natural Language
Processing, pages 2122–2132, Association
for Computational Linguistics, Austin,
Texas.

Liu, Yinhan, Myle Ott, Naman Goyal, Jingfei
Du, Mandar Joshi, Danqi Chen, Omer
Levy, Mike Lewis, Luke Zettlemoyer, and
Veselin Stoyanov. 2019. Roberta: A
robustly optimized bert pretraining
approach.

Lucy, Li and David Bamman. 2021. Gender

and representation bias in GPT-3
generated stories. In Proceedings of the
Third Workshop on Narrative Understanding,
pages 48–55, Association for
Computational Linguistics, Virtual.

Luo, Yiwei, Dallas Card, and Dan Jurafsky.

2020a. Desmog: Detecting stance in media
on global warming. In Proceedings of the
2020 Conference on Empirical Methods in
Natural Language Processing: Findings,
pages 3296–3315.

Luo, Yiwei, Dallas Card, and Dan Jurafsky.

2020b. Detecting stance in media on global
warming. In Findings of the Association for
Computational Linguistics: EMNLP 2020,
pages 3296–3315, Association for
Computational Linguistics, Online.
Ma, Yukun, Khanh Linh Nguyen, Frank Z
Xing, and Erik Cambria. 2020. A survey
on empathetic dialogue systems.
Information Fusion, 64:50–70.

Machina, Mark J. 1987. Choice under
uncertainty: Problems solved and

45

Computational Linguistics

Volume 50, Number 1

unsolved. Journal of Economic perspectives,
1(1):121–154.

Maki, Keith, Michael Yoder, Yohan Jo, and
Carolyn Rosé. 2017. Roles and success in
Wikipedia talk pages: Identifying latent
patterns of behavior. In Proceedings of the
Eighth International Joint Conference on
Natural Language Processing (Volume 1:
Long Papers), pages 1026–1035, Asian
Federation of Natural Language
Processing, Taipei, Taiwan.

Markiewicz, Dorothy. 1974. Effects of humor
on persuasion. Sociometry, pages 407–422.
Martin, Rod A and Thomas Ford. 2018. The

psychology of humor: An integrative approach.
Academic press.

Martino, Giovanni Da San, Stefano Cresci,
Alberto Barrón-Cedeño, Seunghak Yu,
Roberto Di Pietro, and Preslav Nakov.
2020. A survey on computational
propaganda detection. In Proceedings of the
Twenty-Ninth International Joint Conference
on Artificial Intelligence, IJCAI 2020, pages
4826–4832, ijcai.org.

Mathew, Binny, Anurag Illendula, Punyajoy
Saha, Soumya Sarkar, Pawan Goyal, and
Animesh Mukherjee. 2020. Hate begets
hate: A temporal study of hate speech.
Proceedings of the ACM on Human-Computer
Interaction, 4(CSCW2):1–24.

Mendelsohn, Julia, Ceren Budak, and David

Jurgens. 2021. Modeling framing in
immigration discourse on social media. In
Proceedings of the 2021 Conference of the
North American Chapter of the Association for
Computational Linguistics: Human Language
Technologies, pages 2219–2263, Association
for Computational Linguistics, Online.

Mihalcea, Rada and Vivi Nastase. 2012.

Word epoch disambiguation: Finding how
words change over time. In Proceedings of
the 50th Annual Meeting of the Association
for Computational Linguistics (Volume 2:
Short Papers), pages 259–263, Association
for Computational Linguistics, Jeju Island,
Korea.

Mihalcea, Rada and Carlo Strapparava. 2005.
Making computers laugh: Investigations
in automatic humor recognition. In
Proceedings of Human Language Technology
Conference and Conference on Empirical
Methods in Natural Language Processing,
pages 531–538, Association for
Computational Linguistics, Vancouver,
British Columbia, Canada.

Miller, Tim. 2019. Explanation in artificial
intelligence: Insights from the social
sciences. Artificial intelligence, 267:1–38.

46

Min, Bonan and Xiaoxi Zhao. 2019. Measure
country-level socio-economic indicators
with streaming news: An empirical study.
In Proceedings of the 2019 Conference on
Empirical Methods in Natural Language
Processing and the 9th International Joint
Conference on Natural Language Processing
(EMNLP-IJCNLP), pages 1249–1254,
Association for Computational
Linguistics, Hong Kong, China.

Mishra, Abhijit, Tarun Tater, and Karthik
Sankaranarayanan. 2019. A modular
architecture for unsupervised sarcasm
generation. In Proceedings of the 2019
Conference on Empirical Methods in Natural
Language Processing and the 9th International
Joint Conference on Natural Language
Processing (EMNLP-IJCNLP), pages
6144–6154, Association for Computational
Linguistics, Hong Kong, China.

Mohammad, Saif, Svetlana Kiritchenko,

Parinaz Sobhani, Xiaodan Zhu, and Colin
Cherry. 2016. SemEval-2016 task 6:
Detecting stance in tweets. In Proceedings
of the 10th International Workshop on
Semantic Evaluation (SemEval-2016), pages
31–41, Association for Computational
Linguistics, San Diego, California.

Murphy, Kevin M and Andrei Shleifer. 2004.
Persuasion in politics. American Economic
Review, 94(2):435–439.

Murray, Michael et al. 2015. Narrative
psychology. Qualitative psychology: A
practical guide to research methods, pages
85–107.

Muthukrishna, Michael, Adrian V Bell,
Joseph Henrich, Cameron M Curtin,
Alexander Gedranovich, Jason McInerney,
and Braden Thue. 2020. Beyond western,
educated, industrial, rich, and democratic
(weird) psychology: Measuring and
mapping scales of cultural and
psychological distance. Psychological
science, 31(6):678–701.

Nelson, Laura K. 2015. Political logics as
cultural memory: cognitive structures,
local continuities, and women’s
organizations in chicago and new york
city. Work. Pap. Kellogg School Manag.,
Northwestern Univ.

Nelson, Laura K. 2021. Cycles of conflict, a

century of continuity: the impact of
persistent place-based political logics on
social movement strategy. American
Journal of Sociology, 127(1):1–59.

Nguyen, Dong, A Seza Do ˘gruöz, Carolyn P

Rosé, and Franciska de Jong. 2016.
Computational sociolinguistics: A survey.
Computational linguistics, 42(3):537–593.

Ziems, Held, Shaikh, Chen, Zhang, Yang

Can LLMs Transform CSS?

Nguyen, Thien Hai and Kiyoaki Shirai. 2015.
Topic modeling based sentiment analysis
on social media for stock market
prediction. In Proceedings of the 53rd
Annual Meeting of the Association for
Computational Linguistics and the 7th
International Joint Conference on Natural
Language Processing (Volume 1: Long
Papers), pages 1354–1364, Association for
Computational Linguistics, Beijing, China.
Nguyen, Thong, Andrew Yates, Ayah Zirikly,
Bart Desmet, and Arman Cohan. 2022.
Improving the generalizability of
depression detection by leveraging clinical
questionnaires. In Proceedings of the 60th
Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long
Papers), pages 8446–8459.
Niculae, Vlad and Cristian

Danescu-Niculescu-Mizil. 2014. Brighter
than gold: Figurative language in user
generated comparisons. In Proceedings of
the 2014 Conference on Empirical Methods in
Natural Language Processing (EMNLP),
pages 2008–2018, Association for
Computational Linguistics, Doha, Qatar.

Novikova, Jekaterina, Ondˇrej Dušek,

Amanda Cercas Curry, and Verena Rieser.
2017. Why we need new evaluation
metrics for NLG. In Proceedings of the 2017
Conference on Empirical Methods in Natural
Language Processing, pages 2241–2252,
Association for Computational
Linguistics, Copenhagen, Denmark.
Ofer, Dan and Dafna Shahaf. 2022. Cards

against AI: Predicting humor in a
fill-in-the-blank party game. In Findings of
the Association for Computational Linguistics:
EMNLP 2022, pages 5397–5403,
Association for Computational
Linguistics, Abu Dhabi, United Arab
Emirates.

Omitaomu, Damilola, Shabnam Tafreshi,

Tingting Liu, Sven Buechel, Chris
Callison-Burch, Johannes Eichstaedt, Lyle
Ungar, and João Sedoc. 2022. Empathic
conversations: A multi-level dataset of
contextualized conversations. ArXiv
preprint, abs/2205.12698.

OpenAI. 2023. Gpt-4 technical report.
Ortu, Marco, Alessandro Murgia, Giuseppe
Destefanis, Parastou Tourani, Roberto
Tonelli, Michele Marchesi, and Bram
Adams. 2016. The emotional side of
software developers in jira. In Proceedings
of the 13th international conference on mining
software repositories, pages 480–483.

Ouyang, Long, Jeffrey Wu, Xu Jiang, Diogo
Almeida, Carroll Wainwright, Pamela

Mishkin, Chong Zhang, Sandhini
Agarwal, Katarina Slama, Alex Ray, et al.
2022. Training language models to follow
instructions with human feedback.
Advances in Neural Information Processing
Systems, 35:27730–27744.

Paltridge, Brian and Jill Burton. 2000. Making

sense of discourse analysis. Antipodean
Educational Enterprises Gold Coast,
Queensland.

Park, Joon Sung, Joseph C. O’Brien, Carrie J.
Cai, Meredith Ringel Morris, Percy Liang,
and Michael S. Bernstein. 2023. Generative
agents: Interactive simulacra of human
behavior.

Park, Joon Sung, Lindsay Popowski, Carrie
Cai, Meredith Ringel Morris, Percy Liang,
and Michael S Bernstein. 2022. Social
simulacra: Creating populated prototypes
for social computing systems. In
Proceedings of the 35th Annual ACM
Symposium on User Interface Software and
Technology, pages 1–18.

Pennebaker, James W and Laura A King.

1999. Linguistic styles: language use as an
individual difference. Journal of personality
and social psychology, 77(6):1296.

Perez, Ethan, Douwe Kiela, and Kyunghyun
Cho. 2021. True few-shot learning with
language models. Advances in neural
information processing systems,
34:11054–11070.

Pfeil, Ulrike and Panayiotis Zaphiris. 2007.

Patterns of empathy in online
communication. In Proceedings of the
SIGCHI conference on Human factors in
computing systems, pages 919–928.

Picard, Rosalind W. 2000. Affective computing.

MIT press.

Pilehvar, Mohammad Taher and Jose
Camacho-Collados. 2019. WiC: the
word-in-context dataset for evaluating
context-sensitive meaning representations.
In Proceedings of the 2019 Conference of the
North American Chapter of the Association for
Computational Linguistics: Human Language
Technologies, Volume 1 (Long and Short
Papers), pages 1267–1273, Association for
Computational Linguistics, Minneapolis,
Minnesota.

Piper, Andrew, Richard Jean So, and David
Bamman. 2021. Narrative theory for
computational narrative understanding.
In Proceedings of the 2021 Conference on
Empirical Methods in Natural Language
Processing, pages 298–311.
Plutchik, Robert. 1980. A general

psychoevolutionary theory of emotion. In
Theories of emotion. Elsevier, pages 3–33.

47

Computational Linguistics

Volume 50, Number 1

Post, Matt. 2018. A call for clarity in

reporting BLEU scores. In Proceedings of
the Third Conference on Machine Translation:
Research Papers, pages 186–191,
Association for Computational
Linguistics, Brussels, Belgium.

Prabhakaran, Vinodkumar, Owen Rambow,
and Mona Diab. 2012. Predicting overt
display of power in written dialogs. In
Proceedings of the 2012 Conference of the
North American Chapter of the Association for
Computational Linguistics: Human Language
Technologies, pages 518–522, Association
for Computational Linguistics, Montréal,
Canada.

Prabhakaran, Vinodkumar, Emily E. Reid,
and Owen Rambow. 2014. Gender and
power: How gender and gender
environment affect manifestations of
power. In Proceedings of the 2014 Conference
on Empirical Methods in Natural Language
Processing (EMNLP), pages 1965–1976,
Association for Computational
Linguistics, Doha, Qatar.

Preece, Jenny. 1998. Empathic communities:
Reaching out across the web. interactions,
5(2):32–43.

Preo¸tiuc-Pietro, Daniel, Vasileios Lampos,

and Nikolaos Aletras. 2015. An analysis of
the user occupational class through
Twitter content. In Proceedings of the 53rd
Annual Meeting of the Association for
Computational Linguistics and the 7th
International Joint Conference on Natural
Language Processing (Volume 1: Long
Papers), pages 1754–1764, Association for
Computational Linguistics, Beijing, China.

Preo¸tiuc-Pietro, Daniel, Ye Liu, Daniel

Hopkins, and Lyle Ungar. 2017. Beyond
binary labels: Political ideology prediction
of Twitter users. In Proceedings of the 55th
Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long
Papers), pages 729–740, Association for
Computational Linguistics, Vancouver,
Canada.

Purschke, Christoph and Dirk Hovy. 2019.

Lörres, möppes, and the swiss.(re)
discovering regional patterns in
anonymous social media data. Journal of
Linguistic Geography, 7(2):113–134.

Qin, Chengwei, Aston Zhang, Zhuosheng
Zhang, Jiaao Chen, Michihiro Yasunaga,
and Diyi Yang. 2023. Is chatgpt a
general-purpose natural language
processing task solver? ArXiv preprint,
abs/2302.06476.

Raffel, Colin, Noam Shazeer, Adam Roberts,
Katherine Lee, Sharan Narang, Michael

48

Matena, Yanqi Zhou, Wei Li, and Peter J
Liu. 2020. Exploring the limits of transfer
learning with a unified text-to-text
transformer. The Journal of Machine
Learning Research, 21(1):5485–5551.
Raji, Deborah, Emily Denton, Emily M.

Bender, Alex Hanna, and Amandalynne
Paullada. 2021. Ai and the everything in
the whole wide world benchmark. In
Proceedings of the Neural Information
Processing Systems Track on Datasets and
Benchmarks, volume 1, Curran.

Ratner, Alexander, Stephen H Bach, Henry
Ehrenberg, Jason Fries, Sen Wu, and
Christopher Ré. 2017. Snorkel: Rapid
training data creation with weak
supervision. In Proceedings of the VLDB
Endowment. International Conference on Very
Large Data Bases, volume 11, page 269,
NIH Public Access.

Ribeiro, Marco Tulio and Scott Lundberg.

2022. Adaptive testing and debugging of
nlp models. In Proceedings of the 60th
Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long
Papers), pages 3253–3267.

Rogers, Anna, Olga Kovaleva, and Anna

Rumshisky. 2019. Calls to action on social
media: Potential for censorship and social
impact. EMNLP-IJCNLP 2019, page 36.

Rothbaum, Barbara Olasov, Elizabeth A

Meadows, Patricia Resick, and David W
Foy. 2000. Cognitive-behavioral therapy.

Roy, Shamik and Dan Goldwasser. 2020.

Weakly supervised learning of nuanced
frames for analyzing polarization in news
media. In Proceedings of the 2020 Conference
on Empirical Methods in Natural Language
Processing (EMNLP), pages 7698–7716,
Association for Computational
Linguistics, Online.

Rudolph, Maja R. and David M. Blei. 2018.
Dynamic embeddings for language
evolution. In Proceedings of the 2018 World
Wide Web Conference on World Wide Web,
WWW 2018, Lyon, France, April 23-27, 2018,
pages 1003–1011, ACM.

Ryskina, Maria, Ella Rabinovich, Taylor

Berg-Kirkpatrick, David Mortensen, and
Yulia Tsvetkov. 2020. Where new words
are born: Distributional semantic analysis
of neologisms and their semantic
neighborhoods. In Proceedings of the Society
for Computation in Linguistics 2020, pages
367–376, Association for Computational
Linguistics, New York, New York.

Sacks, Harvey. 1992. Lectures on

conversation: Volume i. Malden,
Massachusetts: Blackwell.

Ziems, Held, Shaikh, Chen, Zhang, Yang

Can LLMs Transform CSS?

Saldias, Belen and Deb Roy. 2020. Exploring

aspects of similarity between spoken
personal narratives by disentangling them
into narrative clause types. In Proceedings
of the First Joint Workshop on Narrative
Understanding, Storylines, and Events, pages
78–86, Association for Computational
Linguistics, Online.

Salganik, Matthew J, Peter Sheridan Dodds,
and Duncan J Watts. 2006. Experimental
study of inequality and unpredictability in
an artificial cultural market. science,
311(5762):854–856.

Sanh, Victor, Albert Webson, Colin Raffel,
Stephen Bach, Lintang Sutawika, Zaid
Alyafeai, Antoine Chaffin, Arnaud
Stiegler, Arun Raja, Manan Dey, et al.
Multitask prompted training enables
zero-shot task generalization. In
International Conference on Learning
Representations.

Santhanam, Sashank and Samira Shaikh.

2019. Towards best experiment design for
evaluating dialogue system output. In
Proceedings of the 12th International
Conference on Natural Language Generation,
pages 88–94, Association for
Computational Linguistics, Tokyo, Japan.

Santurkar, Shibani, Esin Durmus, Faisal
Ladhak, Cinoo Lee, Percy Liang, and
Tatsunori Hashimoto. 2023a. Whose
opinions do language models reflect?
Santurkar, Shibani, Esin Durmus, Faisal
Ladhak, Cinoo Lee, Percy Liang, and
Tatsunori Hashimoto. 2023b. Whose
opinions do language models reflect?
ArXiv preprint, abs/2303.17548.

Sap, Maarten, Dallas Card, Saadia Gabriel,

Yejin Choi, and Noah A. Smith. 2019. The
risk of racial bias in hate speech detection.
In Proceedings of the 57th Annual Meeting of
the Association for Computational Linguistics,
pages 1668–1678, Association for
Computational Linguistics, Florence, Italy.

Sap, Maarten, Saadia Gabriel, Lianhui Qin,
Dan Jurafsky, Noah A. Smith, and Yejin
Choi. 2020a. Social bias frames: Reasoning
about social and power implications of
language. In Proceedings of the 58th Annual
Meeting of the Association for Computational
Linguistics, pages 5477–5490, Association
for Computational Linguistics, Online.

Sap, Maarten, Eric Horvitz, Yejin Choi,

Noah A. Smith, and James Pennebaker.
2020b. Recollection versus imagination:
Exploring human memory and cognition
via neural language models. In Proceedings
of the 58th Annual Meeting of the Association
for Computational Linguistics, pages

1970–1978, Association for Computational
Linguistics, Online.

Sap, Maarten, Anna Jafarpour, Yejin Choi,

Noah A Smith, James W Pennebaker, and
Eric Horvitz. 2022. Quantifying the
narrative flow of imagined versus
autobiographical stories. Proceedings of the
National Academy of Sciences,
119(45):e2211715119.

Sap, Maarten, Marcella Cindy Prasettio, Ari
Holtzman, Hannah Rashkin, and Yejin
Choi. 2017. Connotation frames of power
and agency in modern films. In Proceedings
of the 2017 Conference on Empirical Methods
in Natural Language Processing, pages
2329–2334, Association for Computational
Linguistics, Copenhagen, Denmark.

Saravia, Elvis, Hsien-Chi Toby Liu, Yen-Hao
Huang, Junlin Wu, and Yi-Shin Chen.
2018. CARER: Contextualized affect
representations for emotion recognition.
In Proceedings of the 2018 Conference on
Empirical Methods in Natural Language
Processing, pages 3687–3697, Association
for Computational Linguistics, Brussels,
Belgium.

Schelling, Thomas C. 1971. Dynamic models
of segregation. Journal of mathematical
sociology, 1(2):143–186.

Schlechtweg, Dominik, Barbara McGillivray,
Simon Hengchen, Haim Dubossarsky, and
Nina Tahmasebi. 2020. SemEval-2020 task
1: Unsupervised lexical semantic change
detection. In Proceedings of the Fourteenth
Workshop on Semantic Evaluation, pages
1–23, International Committee for
Computational Linguistics, Barcelona
(online).

Sech, Justin, Alexandra DeLucia, Anna L.
Buczak, and Mark Dredze. 2020. Civil
unrest on Twitter (CUT): A dataset of
tweets to support research on civil unrest.
In Proceedings of the Sixth Workshop on
Noisy User-generated Text (W-NUT 2020),
pages 215–221, Association for
Computational Linguistics, Online.

Sellam, Thibault, Dipanjan Das, and Ankur
Parikh. 2020. BLEURT: Learning robust
metrics for text generation. In Proceedings
of the 58th Annual Meeting of the Association
for Computational Linguistics, pages
7881–7892, Association for Computational
Linguistics, Online.

Shah, Raj Sanjay, Faye Holt, Shirley Anugrah
Hayati, Aastha Agarwal, Yi-Chia Wang,
Robert E Kraut, and Diyi Yang. 2022.
Modeling motivational interviewing
strategies on an online peer-to-peer
counseling platform. Proceedings of the

49

Computational Linguistics

Volume 50, Number 1

ACM on Human-Computer Interaction,
6(CSCW2):1–24.

Shaikh, Omar, Jiaao Chen, Jon Saad-Falcon,

Polo Chau, and Diyi Yang. 2020.
Examining the ordering of rhetorical
strategies in persuasive requests. In
Findings of the Association for Computational
Linguistics: EMNLP 2020, pages 1299–1306,
Association for Computational
Linguistics, Online.

Shaikh, Omar, Hongxin Zhang, William

Held, Michael Bernstein, and Diyi Yang.
2022. On second thought, let’s not think
step by step! bias and toxicity in zero-shot
reasoning. ArXiv preprint, abs/2212.08061.
Sharma, Ashish, Inna W Lin, Adam S Miner,
David C Atkins, and Tim Althoff. 2021.
Towards facilitating empathic
conversations in online mental health
support: A reinforcement learning
approach. In Proceedings of the Web
Conference 2021, pages 194–205.

Sharma, Ashish, Adam Miner, David Atkins,
and Tim Althoff. 2020. A computational
approach to understanding empathy
expressed in text-based mental health
support. In Proceedings of the 2020
Conference on Empirical Methods in Natural
Language Processing (EMNLP), pages
5263–5276, Association for Computational
Linguistics, Online.

Shen, Shirong, Guilin Qi, Zhen Li, Sheng Bi,
and Lusheng Wang. 2020. Hierarchical
Chinese legal event extraction via pedal
attention mechanism. In Proceedings of the
28th International Conference on
Computational Linguistics, pages 100–113,
International Committee on
Computational Linguistics, Barcelona,
Spain (Online).

Sheng, Emily, Kai-Wei Chang, Prem

Natarajan, and Nanyun Peng. 2021.
Societal biases in language generation:
Progress and challenges. In Proceedings of
the 59th Annual Meeting of the Association
for Computational Linguistics and the 11th
International Joint Conference on Natural
Language Processing (Volume 1: Long
Papers), pages 4275–4293, Association for
Computational Linguistics, Online.
Sherman, Lawrence W. 1988. Humor and
social distance in elementary school
children.

Shmueli, Galit et al. 2010. To explain or to
predict? Statistical science, 25(3):289–310.
Shubik, Martin. 1982. Game theory in the social

sciences: concepts and solutions.

Siddiqua, Umme Aymun, Abu Nowshed

Chy, and Masaki Aono. 2019. Tweet stance

50

detection using multi-kernel convolution
and attentive lstm variants. IEICE
TRANSACTIONS on Information and
Systems, 102(12):2493–2503.

Silverman, David. 1998. Harvey Sacks: Social
science and conversation analysis. Oxford
University Press on Demand.

Sims, Matthew, Jong Ho Park, and David

Bamman. 2019. Literary event detection.
In Proceedings of the 57th Annual Meeting of
the Association for Computational Linguistics,
pages 3623–3634, Association for
Computational Linguistics, Florence, Italy.

Snow, Rion, Brendan O’Connor, Daniel

Jurafsky, and Andrew Ng. 2008. Cheap
and fast – but is it good? evaluating
non-expert annotations for natural
language tasks. In Proceedings of the 2008
Conference on Empirical Methods in Natural
Language Processing, pages 254–263,
Association for Computational
Linguistics, Honolulu, Hawaii.

Solaiman, Irene and Christy Dennison. 2021.
Process for adapting language models to
society (palms) with values-targeted
datasets. Advances in Neural Information
Processing Systems, 34:5861–5873.

Sprugnoli, Rachele and Sara Tonelli. 2019.
Novel event detection and classification
for historical texts. Computational
Linguistics, 45(2):229–265.

Srivastava, Aarohi, Abhinav Rastogi,

Abhishek Rao, Abu Awal Md Shoeb,
Abubakar Abid, Adam Fisch, Adam R
Brown, Adam Santoro, Aditya Gupta,
Adrià Garriga-Alonso, et al. 2023. Beyond
the imitation game: Quantifying and
extrapolating the capabilities of language
models. Transactions on Machine Learning
Research.

Srivastava, Shashank, Snigdha Chaturvedi,
and Tom M. Mitchell. 2016. Inferring
interpersonal relations in narrative
summaries. In Proceedings of the Thirtieth
AAAI Conference on Artificial Intelligence,
February 12-17, 2016, Phoenix, Arizona,
USA, pages 2807–2813, AAAI Press.
Stefanov, Peter, Kareem Darwish, Atanas
Atanasov, and Preslav Nakov. 2020.
Predicting the topical stance and political
leaning of media using tweets. In
Proceedings of the 58th Annual Meeting of the
Association for Computational Linguistics,
pages 527–537, Association for
Computational Linguistics, Online.
Stewart, Charles J, Craig Allen Smith, and
Robert E Denton Jr. 2012. Persuasion and
social movements. Waveland Press.

Ziems, Held, Shaikh, Chen, Zhang, Yang

Can LLMs Transform CSS?

Stolcke, Andreas, Klaus Ries, Noah Coccaro,
Elizabeth Shriberg, Rebecca Bates, Daniel
Jurafsky, Paul Taylor, Rachel Martin, Carol
Van Ess-Dykema, and Marie Meteer. 2000.
Dialogue act modeling for automatic
tagging and recognition of conversational
speech. Computational Linguistics,
26(3):339–374.

Stone, Philip J, Dexter C Dunphy, and
Marshall S Smith. 1966. The general
inquirer: A computer approach to content
analysis.

Stowe, Kevin, Prasetya Utama, and Iryna

Gurevych. 2022. IMPLI: Investigating NLI
models’ performance on figurative
language. In Proceedings of the 60th Annual
Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), pages
5375–5388, Association for Computational
Linguistics, Dublin, Ireland.

Suler, John. 2005. Contemporary media
forum: The online disinhibition effect.
International Journal of Applied
Psychoanalytic Studies.

Tan, Chenhao, Lillian Lee, and Bo Pang.

2014. The effect of wording on message
propagation: Topic- and author-controlled
natural experiments on Twitter. In
Proceedings of the 52nd Annual Meeting of
the Association for Computational Linguistics
(Volume 1: Long Papers), pages 175–185,
Association for Computational
Linguistics, Baltimore, Maryland.
Tan, Chenhao, Vlad Niculae, Cristian

Danescu-Niculescu-Mizil, and Lillian Lee.
2016. Winning arguments: Interaction
dynamics and persuasion strategies in
good-faith online discussions. In
Proceedings of the 25th International
Conference on World Wide Web, WWW 2016,
Montreal, Canada, April 11 - 15, 2016, pages
613–624, ACM.

Taylor, Samuel Hardman, Dominic DiFranzo,
Yoon Hyung Choi, Shruti Sannon, and
Natalya N Bazarova. 2019. Accountability
and empathy by design: Encouraging
bystander intervention to cyberbullying
on social media. Proceedings of the ACM on
Human-Computer Interaction,
3(CSCW):1–26.

Trope, Yaacov and Nira Liberman. 2010.

Construal-level theory of psychological
distance. Psychological review, 117(2):440.

Tufekci, Zeynep and Christopher Wilson.
2012. Social media and the decision to
participate in political protest:
Observations from tahrir square. Journal of
communication, 62(2):363–379.

Vala, Hardik, David Jurgens, Andrew Piper,
and Derek Ruths. 2015. Mr. bennet, his
coachman, and the archbishop walk into a
bar but only one of them gets recognized:
On the difficulty of detecting characters in
literary texts. In Proceedings of the 2015
Conference on Empirical Methods in Natural
Language Processing, pages 769–774,
Association for Computational
Linguistics, Lisbon, Portugal.

Vosoughi, Soroush, Deb Roy, and Sinan Aral.
2018. The spread of true and false news
online. science, 359(6380):1146–1151.
Wallach, Hanna M., Iain Murray, Ruslan
Salakhutdinov, and David M. Mimno.
2009. Evaluation methods for topic
models. In Proceedings of the 26th Annual
International Conference on Machine
Learning, ICML 2009, Montreal, Quebec,
Canada, June 14-18, 2009, volume 382 of
ACM International Conference Proceeding
Series, pages 1105–1112, ACM.

Wang, Yizhong, Swaroop Mishra, Pegah
Alipoormolabashi, Yeganeh Kordi,
Amirreza Mirzaei, Atharva Naik, Arjun
Ashok, Arut Selvan Dhanasekaran, Anjana
Arunkumar, David Stap, et al. 2022.
Super-naturalinstructions: Generalization
via declarative instructions on 1600+ nlp
tasks. In Proceedings of the 2022 Conference
on Empirical Methods in Natural Language
Processing, pages 5085–5109.

Wardhaugh, Ronald and Janet M Fuller.
2021. An introduction to sociolinguistics.
John Wiley & Sons.

Weller, Orion and Kevin Seppi. 2019. Humor

detection: A transformer gets the last
laugh. In Proceedings of the 2019 Conference
on Empirical Methods in Natural Language
Processing and the 9th International Joint
Conference on Natural Language Processing
(EMNLP-IJCNLP), pages 3621–3625,
Association for Computational
Linguistics, Hong Kong, China.

Welser, Howard T., Dan Cosley, Gueorgi
Kossinets, Austin Lin, Fedor Dokshin,
Geri Gay, and Marc Smith. 2011. Finding
social roles in wikipedia. In Proceedings of
the 2011 iConference, iConference ’11, pages
122–129, ACM, New York, NY, USA.
Wiegreffe, Sarah, Jack Hessel, Swabha

Swayamdipta, Mark Riedl, and Yejin Choi.
2022. Reframing human-AI collaboration
for generating free-text explanations. In
Proceedings of the 2022 Conference of the
North American Chapter of the Association for
Computational Linguistics: Human Language
Technologies, pages 632–658, Association
for Computational Linguistics, Seattle,

51

Computational Linguistics

Volume 50, Number 1

United States.

Wu, Minghao and Alham Fikri Aji. 2023.

Style over substance: Evaluation biases for
large language models. ArXiv preprint,
abs/2307.03025.

Xiang, Wei and Bang Wang. 2019. A survey
of event extraction from text. IEEE Access,
7:173111–173137.

Yang, Diyi, Jiaao Chen, Zichao Yang, Dan

Jurafsky, and Eduard Hovy. 2019a. Let’s
make your request more persuasive:
Modeling persuasive strategies via
semi-supervised neural nets on
crowdfunding platforms. In Proceedings of
the 2019 Conference of the North American
Chapter of the Association for Computational
Linguistics: Human Language Technologies,
Volume 1 (Long and Short Papers), pages
3620–3630, Association for Computational
Linguistics, Minneapolis, Minnesota.
Yang, Diyi, Robert E. Kraut, Tenbroeck

Smith, Elijah Mayfield, and Dan Jurafsky.
2019b. Seekers, providers, welcomers, and
storytellers: Modeling social roles in
online health communities. In Proceedings
of the 2019 CHI Conference on Human
Factors in Computing Systems, CHI 2019,
Glasgow, Scotland, UK, May 04-09, 2019,
page 344, ACM.

Yang, Diyi, Miaomiao Wen, and Carolyn
Rosé. 2015. Weakly supervised role
identification in teamwork interactions. In
Proceedings of the 53rd Annual Meeting of the
Association for Computational Linguistics and
the 7th International Joint Conference on
Natural Language Processing (Volume 1: Long
Papers), pages 1671–1680, Association for
Computational Linguistics, Beijing, China.
Yao, Yunzhi, Shaohan Huang, Wenhui Wang,

Li Dong, and Furu Wei. 2021.
Adapt-and-distill: Developing small, fast
and effective pretrained language models
for domains. In Findings of the Association
for Computational Linguistics: ACL-IJCNLP
2021, pages 460–470, Association for
Computational Linguistics, Online.
Yarkoni, Tal and Jacob Westfall. 2017.

Choosing prediction over explanation in
psychology: Lessons from machine
learning. Perspectives on Psychological
Science, 12(6):1100–1122.

Yu, Tao, Rui Zhang, Alex Polozov,

Christopher Meek, and Ahmed Hassan
Awadallah. 2021. Score: Pre-training for
context representation in conversational
semantic parsing. In International
Conference on Learning Representations.
Yuan, Michelle, Hsuan-Tien Lin, and Jordan

Boyd-Graber. 2020. Cold-start active

52

learning through self-supervised language
modeling. In Proceedings of the 2020
Conference on Empirical Methods in Natural
Language Processing (EMNLP), pages
7935–7948, Association for Computational
Linguistics, Online.

Zarrella, Guido and Amy Marsh. 2016.

MITRE at SemEval-2016 task 6: Transfer
learning for stance detection. In
Proceedings of the 10th International
Workshop on Semantic Evaluation
(SemEval-2016), pages 458–463,
Association for Computational
Linguistics, San Diego, California.
Zhan, Hongli, Tiberiu Sosea, Cornelia

Caragea, and Junyi Jessy Li. 2022. Why do
you feel this way? summarizing triggers
of emotions in social media posts. In
Proceedings of the 2022 Conference on
Empirical Methods in Natural Language
Processing, pages 9436–9453.

Zhang, Amy, Bryan Culbertson, and Praveen

Paritosh. 2017. Characterizing online
discussion using coarse discourse
sequences. In Proceedings of the
International AAAI Conference on Web and
Social Media, volume 11, pages 357–366.
Zhang, Jing, Jie Tang, and Juanzi Li. 2007.
Expert finding in a social network. In
Advances in Databases: Concepts, Systems
and Applications. Springer, pages
1066–1069.

Zhang, Justine, Jonathan Chang, Cristian

Danescu-Niculescu-Mizil, Lucas Dixon,
Yiqing Hua, Dario Taraborelli, and
Nithum Thain. 2018. Conversations gone
awry: Detecting early signs of
conversational failure. In Proceedings of the
56th Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long
Papers), pages 1350–1361, Association for
Computational Linguistics, Melbourne,
Australia.

Zhang, Tianyi, Varsha Kishore, Felix Wu,
Kilian Q. Weinberger, and Yoav Artzi.
2020. Bertscore: Evaluating text generation
with BERT. In 8th International Conference
on Learning Representations, ICLR 2020,
Addis Ababa, Ethiopia, April 26-30, 2020,
OpenReview.net.

Zhao, Jieyu, Tianlu Wang, Mark Yatskar,
Vicente Ordonez, and Kai-Wei Chang.
2018. Gender bias in coreference
resolution: Evaluation and debiasing
methods. In Proceedings of the 2018
Conference of the North American Chapter of
the Association for Computational Linguistics:
Human Language Technologies, Volume 2
(Short Papers), pages 15–20, Association for

Ziems, Held, Shaikh, Chen, Zhang, Yang

Can LLMs Transform CSS?

Computational Linguistics, New Orleans,
Louisiana.

Zhao, Zihao, Eric Wallace, Shi Feng, Dan

Klein, and Sameer Singh. 2021. Calibrate
before use: Improving few-shot
performance of language models. In
International Conference on Machine
Learning, pages 12697–12706, PMLR.
Zhou, Naitian and David Jurgens. 2020.
Condolence and empathy in online
communities. In Proceedings of the 2020
Conference on Empirical Methods in Natural
Language Processing (EMNLP), pages
609–626, Association for Computational
Linguistics, Online.

Zhu, Jian and David Jurgens. 2021a.

Idiosyncratic but not arbitrary: Learning
idiolects in online registers reveals
distinctive yet consistent individual styles.
ArXiv preprint, abs/2109.03158.

Zhu, Jian and David Jurgens. 2021b. The
structure of online social networks
modulates the rate of lexical change. In
Proceedings of the 2021 Conference of the
North American Chapter of the Association for
Computational Linguistics: Human Language
Technologies, pages 2201–2218, Association
for Computational Linguistics, Online.
Zhuo, Terry Yue, Yujin Huang, Chunyang

Chen, and Zhenchang Xing. 2023.
Exploring ai ethics of chatgpt: A
diagnostic analysis. ArXiv preprint,
abs/2301.12867.

Ziems, Caleb, William Held, Jingfeng Yang,
Jwala Dhamala, Rahul Gupta, and Diyi
Yang. 2023. Multi-VALUE: A framework
for cross-dialectal English NLP. In
Proceedings of the 61st Annual Meeting of the
Association for Computational Linguistics
(Volume 1: Long Papers), pages 744–768,
Association for Computational
Linguistics, Toronto, Canada.

Ziems, Caleb, Minzhi Li, Anthony Zhang,
and Diyi Yang. 2022. Inducing positive
perspectives with text reframing. In
Proceedings of the 60th Annual Meeting of the
Association for Computational Linguistics
(Volume 1: Long Papers), pages 3682–3700.
Ziems, Caleb and Diyi Yang. 2021. To protect

and to serve? analyzing entity-centric
framing of police violence. In Findings of
the Association for Computational Linguistics:
EMNLP 2021, pages 957–976.

Zong, Mingyu and Bhaskar Krishnamachari.

2022. a survey on gpt-3.

53

54

