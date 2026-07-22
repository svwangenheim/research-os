Using Large Language Model Annotations for the Social Sciences:
A General Framework of Using Predicted Variables
∗
in Downstream Analyses
† ‡ § ¶
Naoki Egami Musashi Hinck Brandon M. Stewart Hanying Wei
First Version: May 13, 2024
This Version: November 17, 2024
Abstract
Socialscientistsuseautomatedannotationmethods,suchassupervisedmachinelearn-
ing and, more recently, large language models (LLMs), that can predict labels and gen-
erate text-based variables. While such predicted text-based variables are often analyzed
as if they were observed without errors, we show that ignoring prediction errors in the
automated annotation step leads to substantial bias and invalid confidence intervals in
downstream analyses, even if the accuracy of the automated annotations is high, e.g.,
above 90%. We propose a framework of design-based supervised learning (DSL) that can
providevalidstatisticalestimates, evenwhenpredictedvariablescontainnon-randompre-
diction errors. DSL employs a doubly robust procedure to combine predicted labels and
a smaller number of expert annotations. DSL allows scholars to apply advances in LLMs
to social science research while maintaining statistical validity. We illustrate its general
applicability using two applications where the outcome and independent variables are
text-based.
∗TheproposedmethodologyisimplementedviaourRpackage,dsl(http://dsl.software). Thispaperextends
andgeneralizesthemethodsweproposedinEgamietal.(2023). Weappreciatetheexcellentresearchassistance
by Songpo Yang, TaeJun Seo, and Benedikt Str¨obl. We would like to thank Mitchell Bosley, Christian Fong,
Fabrizio Gilardi, Max Goplerud, Katie Keith, John Marshall, Molly Offer-Westort, Joe Ornstein, Nicholas
Pangakis, Tom Robinson, Arthur Spirling, and Hannah Waight for their thoughtful comments on an early
draft. We also appreciate comments from participants at the Political Methodology Summer meeting, the 2023
TADA conference, the 2023 Neurips meeting, and the Conference on Generative AI in Social Science at Yale.
†Corresponding Author. Assistant Professor, Department of Political Science, Columbia University.
Email: naoki.egami@columbia.edu. URL: https://naokiegami.com
‡Postdoctoral Research Associate, Data-Driven Social Science Initiative, Princeton University.
Email: mj2976@princeton.edu. URL: https://muhark.github.io/about
§CorrespondingAuthor. AssociateProfessor,DepartmentofSociologyandtheOfficeofPopulationResearch,
Princeton University. Email: bms4@princeton.edu. URL: https://brandonstewart.org
¶Ph.D. student, Department of Political Science, Columbia University.
Email: hw2893@columbia.edu. URL: https://polisci.columbia.edu/content/hanying-wei

1 Introduction
Over the last decade, social scientists have developed and applied a variety of text analysis
and natural language processing methods to study a large collection of documents. In text-
as-data applications, one of the most common tasks is text annotation (or text classification)
to generate text-based variables for subsequent statistical analyses. For example, Pan and
Chen (2018) annotate whether each online post accuses local Chinese officials of corruption so
that they can later study whether and how much such online complaints are censored. Fowler
et al. (2021) annotate the tone of political ads and then analyze how politicians strategically
change the tone of political advertising online and offline.
In an ideal world without any budget and time constraints, researchers, as domain experts,
might want to carefully annotate all the documents they use in their main statistical analyses.
However, this is often infeasible for the scale of corpora today. To facilitate large-scale anno-
tations, social scientists have used a variety of supervised machine learning (ML) methods to
automate this text annotation step by training machines to mimic expert coding (e.g., Grimmer
and Stewart 2013; Barber´a et al. 2021). More recently, a growing number of papers propose
using large language models (LLMs), such as ChatGPT, to automate text annotations by pre-
dicting text labels (e.g., Bommasani et al. 2021; Ornstein, Blasingame, and Truscott 2022;
Gilardi, Alizadeh, and Kubli 2023; Linegar, Kocielnik, and Alvarez 2023; Ollion et al. 2023;
Pangakis, Wolken, and Fasching 2023; Ziems et al. 2024). Given that researchers can adapt
LLMstoperformawiderangeoftextannotationtasksbysimplychangingprompts, automated
LLM annotations present exciting opportunities for the social sciences.
Whiletextannotationisessential,itisonlythefirststep. Socialscientistsareoftenprimarily
1

interested in using text labels predicted by automated methods as key variables in subsequent
statistical analyses (Hopkins and King 2010; Egami et al. 2022; Grimmer, Roberts, and Stewart
2022). In the vast majority of current applications, researchers treat predicted text-based
variables as if they were observed without errors; that is, they ignore prediction errors created
by automated text annotation. The natural intuition behind this common practice is that
when the prediction accuracy is high enough, the underlying automated text annotation model,
whether it is an LLM or a supervised ML model, “learned” how to label texts, and prediction
errors are small enough that analysts can ignore them. This problem has been previously raised
(Benoit, Laver, and Mikhaylov 2009; Wang, McCormick, and Leek 2020; Fong and Tyler 2021;
Knox, Lucas, and Cho 2022) but is seldom addressed in practice.
We clarify that ignoring such prediction errors in the first step of text annotation, even if the
errors are small, leads to substantial bias, invalid confidence intervals, and inaccurate p-values
in downstream statistical analyses of text-based variables. Biases from prediction errors exist
even when the prediction accuracy in the text classification step is extremely high, e.g., above
90% or even at 95%. This is because prediction errors are not necessarily random—they can
be correlated with observed and unobserved variables in downstream analyses. In practice, this
means that substantive and statistical conclusions can easily flip if researchers choose slightly
different automated text annotation methods, as we empirically show in Section 5.
In this paper, we make two contributions. First, we develop a general framework for us-
ing predicted variables in downstream statistical analyses without suffering from bias due to
prediction errors. Unlike the existing approaches, the proposed approach, which we call design-
based supervised learning (DSL), allows researchers to obtain statistically valid estimates and
standard errors, even when automated text annotation methods have arbitrary non-random
2

Design-based
Automated Annotations 🤖 Expert Annotations 🧐 Supervised Learning
🤖 + 🧐
Use automated annotation methods   Expert-annotate randomly
(e.g., LLMs) to predict labels in all documents sampled documents
Use annotated text labels as variables
in statistical analyses via DSL
Expert-coded data
|     |     | In 47 years, Mike Madigan hasn’t been …  | 1 1 | • DSL combines automated  |
| --- | --- | ---------------------------------------- | --- | ------------------------- |
|     |     | Donald Trump wants to roll back ….       | 0 1 |                           |
annotations and expert-labels
|     |     | …….. | …….. …….. |     |
| --- | --- | ---- | --------- | --- |
In 47 years, Mike Madigan hasn’t been …  1 via a doubly robust procedure
0
On Tuesday, Nevada voters will choose …
| Donald Trump wants to roll back …. | 0   |     |     |     |
| ---------------------------------- | --- | --- | --- | --- |
Lt Governor Dan Patrick cut public … 1 My commitment is to always be on the …. 0 0 • DSL enables valid statistical analyses
| …….. | …….. |     | Experts       | of text-based variables,         |
| ---- | ---- | --- | ------------- | -------------------------------- |
|      |      |     | assign labels | even when automated annotations  |
have non-random prediction errors
Data without Expert-Coding
0
My commitment is to always be on the ….
| Nobody thought a Democrat could win …. | 1   |                                         |      |                                |
| -------------------------------------- | --- | --------------------------------------- | ---- | ------------------------------ |
|                                        |     | On Tuesday, Nevada voters will choose … | 0    |                                |
|                                        |     | Lt Governor Dan Patrick cut public …    | 1    |                                |
|                                        |     | ……..                                    | …….. | ⚠ Ignoring prediction errors   |
Collect   Automated           bias and invalid confidence intervals
Documents of   methods   Nobody thought a Democrat could win …. 1 even when the predictive performance of
Interest assign labels
the automated annotation step is high
(e.g., above 90 ~ 95% accuracy)
Figure 1: Overview of the Design-based Supervised Learning (DSL).
prediction errors. Second, we show how this general framework allows researchers to unlock
the recent advances in LLMs without suffering from bias in downstream statistical analysis.
Preview of DSL
DSL combines large-scale (potentially biased) automated annotations and a smaller number
of expert annotations using a bias-correction step built on doubly robust estimation (Robins,
Rotnitzky, and Zhao 1994; Chernozhukov et al. 2018). Figure 1 provides an overview of the
method. While DSL provides statistically valid estimates regardless of the prediction accuracy
of the underlying automated annotation method, DSL can reduce standard errors when the
automated annotation method becomes more accurate. This pairs nicely with LLMs, which are
rapidly improving over time: as LLMs improve, estimation with DSL becomes more efficient.
Importantly, DSL only requires one transparent assumption—that researchers control the
process through which documents are sampled for expert annotations. One of the most com-
3

mon ways to guarantee the assumption is to randomly sample documents for expert coding.
This assumption is straightforward to guarantee by research design in many social science
applications, which gives the name, design-based supervised learning. We do not make any
assumptions about prediction errors in the underlying automated annotation method, and as
a result, the proposed method is applicable to any automated labeling procedure (including
LLMs that have not yet been released).
When we use the term “expert annotations,” we define it to be a procedure that estab-
lishes the benchmark against which the quality of the automated text annotation is evaluated,
as done in the supervised machine learning literature for decades (Hopkins and King 2010;
Grimmer and Stewart 2013). We call these labels “expert annotations” because we believe
that the target procedure that the modal social scientist is trying to approximate is domain
experts (e.g., the principal investigators) carefully labeling all documents by hand. However,
our method does not require “human” experts to provide this target procedure. More generally,
our procedure is applicable whenever researchers have an annotation procedure that they wish
to implement for the entire sample (but cannot, e.g., due to costs) and a cheaper automated
annotation procedure approximating this target.1 For example, if users want to correct anno-
tations by lower-quality smaller LLMs with more expensive annotations by larger LLMs as the
benchmark, the same proposed methodology can be applied. Similarly, if the ideal procedure is
to have a panel of experts vote on each classification, the panel can be the source of the expert
annotation. We do not assume that expert annotations are perfect. In Section 6, we provide
1. Formally, the statistical properties of DSL are defined with respect to what we would have
observed if all documents had been labeled using a given target procedure.
4

concrete, practical recommendations for how to incorporate errors or disagreements that re-
main in “expert annotations.” Researchers can apply a quasi-Bayesian approach to account for
uncertainties in expert annotations in addition to prediction errors and sampling errors.
Our proposed approach is a general-purpose method that works in a wide range of text-
as-data applications. DSL can incorporate any automated text annotation method (including
dictionaries, supervised ML methods, and any LLMs) and works for a variety of common down-
streamanalysesscholarsconductwithtext-basedvariables: linear,logistic,multinomial-logistic,
Poisson, andlinearfixed-effectsregression, aswellastheestimationofcategoryproportionsand
causal inference with texts.2 While we focus on the use of LLMs in text-as-data applications
because of the rapid rate of improvement and interest in the field, our proposed framework can
also be used in any application where predictive methods are used to scale up measurements,
e.g., analyses of images, videos, and audio, which we discuss in Section 6. We offer an easy-to-
use R package, dsl, which can implement all the methods described in this paper with simple
functions.
Related Literature
Our paper contributes to the growing literature on the use of predicted variables in statistical
analyses. A number of papers develop methods for specific scenarios by making assumptions
about the underlying data-generating process and prediction errors (e.g., Wang, McCormick,
and Leek 2020; Fong and Tyler 2021; Zhang 2021; Knox, Lucas, and Cho 2022). In contrast
to these papers, we only assume that researchers control the sampling process for expert an-
2. In general, the proposed DSL framework can be applied to any statistical method that
can be written as a convex optimization problem or a moment estimator.
5

notations, and we do not make any assumption about the nature of prediction errors, which is
particularly difficult to justify in applications of LLMs. Our paper is most closely related to
recent methods that build on the doubly robust estimation (Robins, Rotnitzky, and Zhao 1994;
Chernozhukov et al. 2018) to deal with predicted variables, such as the original proposal of DSL
(Egami et al. 2023), prediction-powered inference (e.g., Angelopoulos et al. 2023), and model-
assisted impact analysis (Mozer and Miratrix 2023). Methodologically, our paper extends these
previous results in four ways. First, while these papers only cover cases of text-based out-
come variables, we cover cases where any subset of the outcome and independent variables are
text-based. This methodological generalization is fundamental because about 45% of appli-
cations use text-based variables as independent variables. Second, we develop a data-driven
power analysis to help users determine the required number of expert annotations. Third, we
derive DSL estimators for a much wider range of downstream analyses popular in the social
sciences, including linear fixed effects regression and the instrumental variable method. Fourth,
we propose a quasi-Bayesian approach to explicitly take into account uncertainties in expert
annotations within the DSL framework. Finally, we provide a new R software package, dsl,
that implements all the methods proposed in this paper.
Roadmap
In the next section, we provide an introduction to annotation using LLMs. In Section 3, we
review how social scientists use text annotations in downstream analysis and clarify that the
current practice of directly using predicted variables in downstream analyses leads to substan-
tial bias and invalid confidence intervals. Section 4 outlines our solution, DSL, and provides
intuition for how it works. Section 5 demonstrates our approach with two empirical applica-
6

tions, Fowler et al. (2021) and Pan and Chen (2018). Before concluding, we offer practical
guidance in Section 6 to help researchers apply these techniques to their own work—answering
questions such as how to determine the required number of expert annotations.
2 Automated Text Annotation
One of the most fundamental steps in many text-as-data research projects is to annotate doc-
uments. Over the last decade, scholars have used automated annotation methods to facilitate
this time-consuming step by training machines to mimic expert annotation. In this section, we
discuss how researchers can use the recent advances in LLMs for a wide range of text annotation
tasks. We then clarify the potential risks of using LLM annotations, which motivates our main
methodological contributions in Section 3 and Section 4.
2.1 Large Language Models as Text Classifier
An increasing number of social scientists use LLMs as automated text classifiers: researchers
simply describe the annotation task in natural language instructions, and the LLM generates
text labels by predicting the most appropriate text to follow such a request. For example,
scholars have used LLMs to annotate sentiments, ideology, topics, hate speech, attitudes toward
immigrants, and support for a war, among others. See a wide range of examples in Appendix F.
2.1.1 How to Use LLMs as Text Classifiers
To illustrate this exciting potential, we use Fowler et al. (2021) as an example. The text
annotation task here is to code the tones of ads into three categories (“Attack,” “Contrast,”
and “Promote”). In the codebook developed in the well-known Wesleyan Media Project and
used by Fowler et al. (2021), the tone of ads is defined as an answer to the following question.
7

“In your judgment, is the primary purpose of the ad text to promote a specific candidate,
attack a candidate, or contrast the candidates?” Instead of providing the codebook to trained
expert coders, we can supply the same codebook to LLMs (see Figure 2-(a)) by first describing
the codebook, then supplying Text to be classified, and finally prompting the LLM to Answer.
In this example, when we use GPT 4, it understands the codebook and annotates a given
document correctly as “Attack” (a response from the LLM is in a gray box). Researchers can
also provide some examples (several pairs of texts and labels), also known as few-shot learning
or in-context learning, to improve the prediction accuracy (see Figure 2-(b)).
2.1.2 Empirical Illustration of LLM Annotation
While the idea of using LLMs for text classification sounds promising, does it work in practice?
In thissection, weuse two empiricalapplications ofours and the literature review to empirically
illustratetheperformanceinawiderangeofsettings, whichclarifiesthepromiseandchallenges.
Our first application is based on Fowler et al. (2021). In particular, we use the 13040 ads
that are expert-coded by the original authors and examine the prediction accuracy of LLMs
classifying the tone of ads. The second application is based on Pan and Chen (2018). We use
their expert-coded 1412 citizen complaints to evaluate how well LLMs can classify whether each
complaint accuses of wrongdoing by prefecture-level officials in China.
Panels (a) and (b) in Figure 3 report F1 scores3 for six versions of LLMs: GPT 4, GPT
3.5, and Llama 2 with zero-shot and few-shot learning. We provide the exact implementation
3. F1 score is a harmonic mean of the recall and precision, and it is the most standard
measure of prediction performance when categories are imbalanced. We also report the figures
based on accuracy in Appendix G and H, finding qualitatively similar results.
8

|        |           | (a)          | Zero-shot learning   | (no exemplar) |       |
| ------ | --------- | ------------ | -------------------- | ------------- | ----- |
|        |           | (b) Few-shot | learning (exemplars  | in non-bold   | face) |
| Figure | 2: How to | Use LLMs     | as Text Classifiers. |               |       |
Note: In (a) zero-shot learning, the basic prompt consists of a codebook (the first two lines), a
text to be classified (the next two lines), and an answer box (the last line). A response from an
LLM is represented in a gray box. In (b) few-shot learning, while keeping the basic components
(parts in a bold face), users can add examples (parts in a non-bold face) in the middle.
9

| Tone of Political Ads |       |         |         |      | Prefecture Wrongdoing |         |           |
| --------------------- | ----- | ------- | ------- | ---- | --------------------- | ------- | --------- |
|                       | GPT 4 | GPT 3.5 | Llama 2 |      | GPT 4                 | GPT 3.5 | Llama 2   |
| 1.00                  |       |         |         | 1.00 |                       |         |           |
|                       |       |         |         |      | 0.95 0.94             | 0.91    | 0.91 0.91 |
0.88
|          | 0.8  |           |     | 0.78     |     |     |     |
| -------- | ---- | --------- | --- | -------- | --- | --- | --- |
|          | 0.74 | 0.76 0.76 |     |          |     |     |     |
| 0.75     |      |           |     | 0.75     |     |     |     |
| erocs 1F |      |           |     | erocs 1F |     |     |     |
0.48
| 0.50 |     |     |     | 0.50 |     |     |     |
| ---- | --- | --- | --- | ---- | --- | --- | --- |
| 0.25 |     |     |     | 0.25 |     |     |     |
| 0.00 |     |     |     | 0.00 |     |     |     |
Zero−shot Few−shot Zero−shot Few−shot Zero−shot Few−shot Zero−shot Few−shot Zero−shot Few−shot Zero−shot Few−shot
|     | (a) Fowler | et al. | (2021) |     | (b) Pan | and Chen (2018) |     |
| --- | ---------- | ------ | ------ | --- | ------- | --------------- | --- |
LLM Performance in Other Applications
10
ycneuqerF
5
0
|     |     | 0.00 | 0.25 | 0.50 | 0.75 | 1.00 |     |
| --- | --- | ---- | ---- | ---- | ---- | ---- | --- |
F1 score
|     |     | (c) | 113 annotation | tasks | in 8 papers |     |     |
| --- | --- | --- | -------------- | ----- | ----------- | --- | --- |
Figure 3: Prediction Performance of LLMs as Text Classifiers.
details in Appendix G and H. Several points are worth noting. First, most of the LLMs can
achieve F1 scores of about 75 ∼ 90%. This is promising and surprising given that these LLMs
were not trained for these text annotation tasks, and LLMs were only given the codebook and
| a couple | of examples | (in the case | of few-shot | learning). |     |     |     |
| -------- | ----------- | ------------ | ----------- | ---------- | --- | --- | --- |
Second, the prediction performance varies across models and applications. In these two
10

applications, F1 scores range from 48% to 95%. To further illustrate this wide variation in
prediction performance, we also analyze a diverse set of empirical validation studies. In par-
ticular, based on a review paper by Ollion et al. (2023), we collected eight recent papers that
examine the performance of LLM annotations in the social sciences, and we analyzed 113 text
annotations tasks in total (see more details in Appendix F.1.2). We find that F-1 scores range
from as low as 20% to more than 95%, and many tasks show about 70 ∼ 80% (see Panel (c) in
Figure 3). This huge variation in prediction accuracy is a common feature of LLM annotations
in the social sciences, and it is one of the key potential challenges of using LLMs, which we
turn to next.
2.2 Potential Risks of LLM Annotation
As with any new technology, we have to carefully understand the potential risks as well as its
promises. Even though LLMs have huge potential in many different text annotation tasks, they
are, of course, not perfect and make prediction errors. While prediction errors can arise in any
prediction method, including the classical supervised ML method, prediction errors in LLM
classification are particularly difficult to understand for several reasons.
First, as we saw in Section 2.1.2, the amount and direction of prediction errors in LLM
classification can substantially vary depending on tasks, prompts, LLM models, and other
unknown parameters in models. Most importantly, these variations in prediction errors are
unknown and unpredictable to users. Second, many recent LLMs lack the basic scientific
requirement of transparency and replicability. In particular, many recent successful LLMs,
e.g., GPTs, are proprietary methods, and as a result, users and research communities, in
general, do not know the training data or exact training procedures that LLMs use (Spirling
11

2023). Finally, a large number of papers have shown that LLMs also inherit unknown social,
political, and racial biases contained in the unknown large-scale training data (see, e.g., Bender
et al. 2021). Prediction errors in LLMs can come not only from technical reasons but also from
deeper reasons related to ethics and fairness, which further complicates the understanding of
| prediction | errors. |     |     |     |     |
| ---------- | ------- | --- | --- | --- | --- |
In sum, it is nearly impossible to fully understand how prediction errors occur in LLM
classification. In the next section, we clarify the problem of ignoring such prediction errors in
LLM annotation.
| 3 Predicted |     | Text | Labels | as Variables | in Downstream |
| ----------- | --- | ---- | ------ | ------------ | ------------- |
Analyses
While document-level text classification is essential, text annotation is rarely the end goal of
social science research. Social scientists are often interested in using predicted text labels as
variables in subsequent statistical analyses. Even though researchers usually analyze predicted
text-based variables as if they were observed without any error, this section clarifies that ignor-
ing such prediction errors in the first step of text annotation, even if the errors are small, leads
to substantial bias, invalid confidence intervals, and wrong p-values in downstream statistical
| analyses  | of text-based | variables. |             |     |     |
| --------- | ------------- | ---------- | ----------- | --- | --- |
| 3.1 Setup | and           | Quantity   | of Interest |     |     |
We begin by defining statistical analyses we conduct after text annotation. Here, we focus on
the most common regression analyses, and we discuss other common analyses, such as causal
| inference | with texts, | in Section | 6.  |     |     |
| --------- | ----------- | ---------- | --- | --- | --- |
12

Suppose researchers are interested in analyzing N documents. For each document i, we
define Y as the outcome of interest and X as independent variables. Using general notation,
i i
we can define the quantity of interest as coefficients β of a generalized linear model.
E(Y | X ) = f(X⊤β) (1)
i i i
where f(·) is an inverse of a canonical link function for the generalized linear model. This
general setup incorporates a wide range of common statistical analyses, such as linear, logistic,
multinomial logistic, Poisson, and linear fixed-effects regression, as well as the estimation of
category proportions over time or across groups.4 Importantly, we only view coefficients β as a
low-dimensionalsummary, andthus, thispaperdoesnotassumetheunderlyingdata-generating
process follows a specified parametric model (Lundberg, Johnson, and Stewart 2021). Our
proposed method can also be used to estimate the first differences or other quantities that are
functions of coefficients rather than coefficients themselves (see an example in Section 5.2).
3.2 Current Practice: Directly Using Predicted Labels as Variables
In text analyses, a subset of the outcome Y and independent variables X are based on some
forms of text labels, and creating such text-based variables requires text annotation. When
using automated text annotation methods to predict text labels, regardless of the exact choice,
statistical analyses take the following steps in general. First, researchers check the accuracy
4. Our literature review of the ten political science journals finds that our setup covers
commonstatisticalmodelsusedinmorethan91%ofapplicationsusingtextannotations: Linear
regression (49% of applications), Logistic regression (21%), Category proportions over time or
across groups (Subgroup means) (19%), and Poisson regression (2%).
13

of prediction against expert-coded data, e.g., using cross-validation. If the accuracy is “low,”5
researchers retrain the model until it gets better (e.g., using different LLMs or ML models
and adding more informative predictors). Then, once the accuracy becomes “high enough,”
they now use predicted text labels directly in downstream analyses as if those variables were
directly observed and not predicted. The idea is that when the prediction accuracy is high,
the prediction model sufficiently mimics expert coding, and thus, prediction errors are small
| enough that | they | do not | affect | downstream |     | analyses | significantly. |
| ----------- | ---- | ------ | ------ | ---------- | --- | -------- | -------------- |
More concretely, most researchers use one of the following two ways. To predict text labels,
the first approach uses LLMs and the second uses the supervised machine learning model (e.g.,
random forest, and lasso), but both directly use predicted labels in downstream analyses after
| checking | the prediction |            | accuracy. |              |      |            |           |
| -------- | -------------- | ---------- | --------- | ------------ | ---- | ---------- | --------- |
| LLM-Only |                | Estimation |           |              |      |            |           |
| Step     | 1: Predict     | text       | labels    | using        | LLMs | for each   | document. |
| Step     | 2: Sample      | a          | subset    | of documents |      | for expert | coding.   |
Step 3: Check the prediction accuracy using the expert-coded data. Repeat Step 1 until
|     | the prediction |     | accuracy |     | is high. |     |     |
| --- | -------------- | --- | -------- | --- | -------- | --- | --- |
Step 4: Use LLM-predicted variables in downstream text analyses.
5. Scholars use different criteria for deciding how much is “low” and “high enough,” but
| many scholars | use | 80  | ∼ 90% | as rough | thresholds. |     |     |
| ------------- | --- | --- | ----- | -------- | ----------- | --- | --- |
14

| Classical | Supervised |     |        | Learning     | Estimation |     |        |         |     |     |     |
| --------- | ---------- | --- | ------ | ------------ | ---------- | --- | ------ | ------- | --- | --- | --- |
| Step      | 1: Sample  | a   | subset | of documents |            | for | expert | coding. |     |     |     |
Step 2: Train a supervised machine learning model with the expert-coded data.
Step 3: Check the prediction accuracy using the expert-coded data via cross-validation.
|     | Repeat | Step | 2 until |     | the prediction |     | accuracy |     | is high. |     |     |
| --- | ------ | ---- | ------- | --- | -------------- | --- | -------- | --- | -------- | --- | --- |
Step 4: Use ML-predicted variables in downstream text analyses.
| 3.3 The | Methodological |     |     |     | Challenges |     |     | of  | the Current | Practice |     |
| ------- | -------------- | --- | --- | --- | ---------- | --- | --- | --- | ----------- | -------- | --- |
Ignoring prediction errors in the text annotation step, even if the errors are small, leads to
bias, invalid confidence intervals, and wrong p-values in the subsequent statistical analyses of
text-based variables. Biases from prediction errors exist even when the prediction accuracy in
the text classification step is extremely high, e.g., above 90% or even at 95%. This is because
prediction errors are not completely random—prediction errors are correlated with observed
and unobserved variables we include in downstream analyses. Even small prediction errors can
bias downstream analyses in any direction by any amount. Because exactly the same problem
applies to the LLM-only estimation and the classical supervised learning estimation, we do not
| distinguish | them, | and | we discuss |     | prediction | errors |     | in general. |     |     |     |
| ----------- | ----- | --- | ---------- | --- | ---------- | ------ | --- | ----------- | --- | --- | --- |
To concretely illustrate the problem, we focus on a simple case where the outcome variable
Y requires text annotation, and researchers want to regress Y on independent variables X to
| estimate | coefficients | β   | defined | as, |     |     |     |      |     |     |     |
| -------- | ------------ | --- | ------- | --- | --- | --- | --- | ---- | --- | --- | --- |
|          |              |     |         |     | E(Y | | X | ) = | X⊤β. |     |     | (2) |
|          |              |     |         |     |     | i   | i   | i    |     |     |     |
Researchers can easily obtain the ordinary squares estimates of β when the outcome variable
15

of interest Y is observed for every document. However, when Y requires text annotation and
Y itself is not observed for each document, researchers instead regress the predicted outcome
variable Y(cid:98) on independent variables X. This linear regression with the predicted outcome
variable will lead to unbiased coefficient estimation when prediction error, e = Y(cid:98) −Y , is zero
i i i
| on average | across | all different combinations |     | of X.      |     |
| ---------- | ------ | -------------------------- | --- | ---------- | --- |
|            |        |                            | E(e | | X ) = 0. | (3) |
|            |        |                            | i   | i          |     |
Even though this expression might seem similar to the standard exogeneity assumption, it
turns out that this condition implies much stronger assumptions. Formally, researchers can
ignore prediction errors only when prediction errors are completely random, i.e., prediction
errors are not affected by the independent variable, the outcome variable, or any unobserved
confounder. Unfortunately, this condition is untenable in almost all social science applica-
tions. Similar stringent conditions are required when other types of variables (e.g., indepen-
dent variables) are text-based. We offer additional discussions and the general bias formula in
| Appendix | B.         |       |     |     |     |
| -------- | ---------- | ----- | --- | --- | --- |
| 3.4      | Simulation | Study |     |     |     |
We now use a simulation study to illustrate the severity of the problem. We vary the prediction
accuracy of the underlying automated annotation methods—from as low as 50% to as high as
95%—and evaluate how ignoring prediction errors affects downstream regression analyses. We
| detail the | data generation | process | in Appendix | E.  |     |
| ---------- | --------------- | ------- | ----------- | --- | --- |
The first column in Figure 4 shows the average bias across coefficients standardized by
the true coefficients. When prediction errors are ignored (the first row), bias decreases as the
accuracy of the underlying prediction method goes up. However, bias can be as large as 30%
16

|                    |                   | Bias |                  | Coverage |      | RMSE |
| ------------------ | ----------------- | ---- | ---------------- | -------- | ---- | ---- |
|                    | 1.00              |      | 1.00             |          | 0.5  |      |
| srorrE noitciderP  | saiB dezidradnatS |      | tnecreP egarevoC |          |      |      |
|                    | 0.75              |      | 0.75             |          | 0.4  |      |
|  gnirongI          |                   |      |                  |          | ESMR |      |
|                    | 0.50              |      | 0.50             |          | 0.3  |      |
|                    | 0.25              |      | 0.25             |          | 0.2  |      |
|                    | 0.00              |      | 0.00             |          | 0.1  |      |
0.5 0.6 0.7 0.8 0.9 0.95 0.5 0.6 0.7 0.8 0.9 0.95 0.5 0.6 0.7 0.8 0.9 0.95
|     | 1.00 |     | 1.00 |     | 0.200 |     |
| --- | ---- | --- | ---- | --- | ----- | --- |
saiB dezidradnatS
|     | 0.75 |     | tnecreP egarevoC 0.75 |     | 0.175 |     |
| --- | ---- | --- | --------------------- | --- | ----- | --- |
| LSD |      |     |                       |     | ESMR  |     |
|     | 0.50 |     | 0.50                  |     | 0.150 |     |
|     | 0.25 |     | 0.25                  |     | 0.125 |     |
|     | 0.00 |     | 0.00                  |     | 0.100 |     |
0.5 0.6 0.7 0.8 0.9 0.95 0.5 0.6 0.7 0.8 0.9 0.95 0.5 0.6 0.7 0.8 0.9 0.95
|     | Prediction Accuracy |     |     | Prediction Accuracy |     | Prediction Accuracy |
| --- | ------------------- | --- | --- | ------------------- | --- | ------------------- |
Figure 4: Ignoring Prediction Errors Lead to Bias and Invalid Confidence Intervals.
and 18% of the true coefficients even when the underlying prediction accuracy is 90% and 95%.
The second column in Figure 4 shows the coverage rate of the 95% confidence intervals (the
probability of reported confidence intervals covering the true coefficients), and the coverage
rates should be at least 95% if a given estimation method is statistically valid. Unfortunately,
when prediction errors are ignored, the coverage rate of 95% confidence intervals is as low as
32% and 58%, even when the underlying prediction accuracy is 90% and 95%, respectively.
Bias and coverage rates are, of course, much worse when the accuracy of the prediction method
| is about | 80 ∼ 90% | or lower, as | we see in most | applications. |     |     |
| -------- | -------- | ------------ | -------------- | ------------- | --- | --- |
The second row of Figure 4 previews the results of the proposed DSL. As we show in the
next section, DSL is theoretically guaranteed to have asymptotically unbiased estimates and
valid confidence intervals, regardless of the accuracy of the underlying prediction method (see
17

the first and second columns in the second row). When the underlying prediction method
becomes more accurate, DSL also gets more accurate and has smaller standard errors, which is
shown by the reduction in root mean squared error (RMSE) (see the third column in Figure 4).
| 4 Design-based |     | Supervised | Learning |     |
| -------------- | --- | ---------- | -------- | --- |
We propose a general method, which we call design-based supervised learning (DSL), to use
predicted variables in downstream analyses without introducing bias from prediction errors.
This general framework allows researchers to use LLM annotations or text labels predicted by
ML methods in downstream text analyses while maintaining statistical validity.
4.1 Overview
| We first provide | an overview | of the proposed | DSL        | method.   |
| ---------------- | ----------- | --------------- | ---------- | --------- |
| Design-based     | Supervised  | Learning        | Estimator  | (DSL)     |
| Step 1: Predict  | text labels | using LLMs      | for each   | document. |
| Step 2: Sample   | a subset    | of documents    | for expert | coding.   |
Step 3: Train an ML model to improve LLM prediction with the expert-coded data.
Step 4: Combine expert-coded labels and predicted variables in the DSL regression.
Importantly, most steps (Steps 1–3) are similar to existing approaches and thus are already
familiar to applied researchers. In the first step, like the LLM-only estimation, we predict
text labels using LLMs. In the second step, like the existing approaches, we sample a subset
of documents for expert-based coding. In the third step, researchers can use expert-coded
documentsas thetraining dataand traina supervisedmachinelearning modelwhere wepredict
the expert-coded labels with predictors that include LLM annotations generated in Step 1 and
18

any other variables that are predictive (e.g., term-document matrices).6 This step is useful for
incorporating multiple LLMs as predictors for the expert-coded labels. The fourth step is an
essential defining feature of DSL, which we describe in detail in the next sections.
4.2 Assumption: Design-based Sampling
Before we describe the details of the DSL regression, we clarify the central assumption. In par-
ticular, we require that researchers know the process through which documents are sampled for
expert coding. Formally, we make the following assumption by defining π to be the probability
i
of sampling document i for expert coding.
Assumption 1 (Design-based Sampling for Expert Coding)
The probability of sampling documents for expert coding π is known to researchers, and π is
i i
larger than zero for every document.
Assumption 1 holds when the researchers can choose which documents to be coded by
experts. For example, if the researchers have 10000 documents and sample 100 of them to
expert-annotate at random, π = 100 = .01 for all documents. Here, the sampling probability
i 10000
for each document is decided by the researchers and is greater than zero. We also allow more
complex stratified or block sampling schemes (i.e., change the sampling probability of docu-
ments based on document-level observed covariates) and can cover any case where the sampling
probability π depends on the LLM annotation, document-level covariates, independent vari-
i
ables, or the outcome variable, as long as π is known. This generality is important because
i
6. Researchers can also skip this third step, and doing so is equivalent to using the identity
function to predict expert-coded labels with LLM labels.
19

researchers might want to over-sample documents that are difficult to annotate.
Importantly, Assumption 1 does rule out some applications, and two are worth noting: (1)
Researchers use external coding (rather than their own expert coding) to measure text-based
variablesofinterest, anditisunknownwhyonlyasubsetofdocumentswerecoded. (2)Another
scenario occurs when researchers need to analyze documents in real-time as soon as they obtain
text data, e.g., making polling predictions based on social media posts on election day. In
Appendix B.5, we discuss them in detail with examples and explain how researchers can adjust
DSL to these scenarios.
While we do not cover all text-as-data scenarios, our approach covers the vast majority of
social science research applications where researchers need to annotate a corpus of documents
that are available in total before analyzing data. Even more importantly, Assumption 1 can be
guaranteed by research design alone. Our assumption is transparent and easy to justify. This
is the reason why our method is named design-based supervised learning.
There are other important practical considerations about expert annotations. In Sec-
tion 5.1.3, we discuss how to determine the required number of expert annotations using a
power analysis. In Section 6.1, we introduce an approach to explicitly incorporate errors and
uncertainties in expert annotations.
4.2.1 Assumptions We Do Not Make
We make no assumptions about prediction errors and allow for arbitrary prediction errors.
Researchers do not need to assume how prediction errors arise in LLMs or ML prediction.
They do not need to assume LLM annotations are unbiased or accurate, either. In practice,
this means that researchers can use predictions from LLMs or supervised ML without making
assumptions about their prediction errors or inherent biases.
20

This is in sharp contrast to existing alternatives. Both the LLM-only estimation and the
classical supervised learning approach have to assume prediction errors are completely random.
This assumption is often severely violated in practice, and importantly, researchers cannot
| guarantee | this assumption |     | by research | design. |     |     |     |     |     |
| --------- | --------------- | --- | ----------- | ------- | --- | --- | --- | --- | --- |
| 4.3       | DSL Regression  |     |             |         |     |     |     |     |     |
We now examine how the proposed DSL estimator can incorporate predicted variables without
introducing bias under Assumption 1. To provide intuition, we start with a simple case and
| generalize | it step | by step. |     |     |     |     |     |     |     |
| ---------- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- |
4.3.1 Building Intuition with Estimation of Category Proportion
Suppose researchers are interested in estimating the proportion of documents belonging to a
particular category, e.g., the proportion of political ads attacking opponents. Define Y ∈ {0,1}
i
to denote whether a given political ad attacks opponents. When using the LLM-only estimation
or the classical supervised ML methods, users would first predict whether each ad attacks
opponents Y(cid:98) and then average it over ads to estimate the proportion of attacking ads.
i
| In contrast, | DSL | uses | the following | design-adjusted |     | outcome. |     |     |     |
| ------------ | --- | ---- | ------------- | --------------- | --- | -------- | --- | --- | --- |
R
i
|     |     |     | Y(cid:101) | = Y(cid:98)                          | −                   | (Y(cid:98) −Y      | ),        |     | (4) |
| --- | --- | --- | ---------- | ------------------------------------ | ------------------- | ------------------ | --------- | --- | --- |
|     |     |     | i          | i                                    | π                   | i                  | i         |     |     |
|     |     |     |            | (cid:124)(cid:123)(cid:122)(cid:125) |                     | i                  |           |     |     |
|     |     |     |            | Predicted                            | (cid:124)           | (cid:123)(cid:122) | (cid:125) |     |     |
|     |     |     |            | Outcome                              | Bias-CorrectionTerm |                    |           |     |     |
where Y is the outcome of interest coded by experts, R is a binary variable taking 1 if doc-
|     | i   |     |     |     |     | i   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ument i is expert-coded and 0 otherwise, and π (defined in Section 4.2) is the probability of
i
sampling document i for expert coding.7 This estimator has deep theoretical connections to
7. The design-adjusted outcome is equal to Y(cid:98) when R = 0 and is equal to Y(cid:98) −(Y(cid:98) −Y )/π
|     |     |     |     |     | i   | i   |     | i i | i i |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
when R = 1. It might be counter-intuitive to change the outcome for documents R = 1, but
|     | i   |     |     |     |     |     |     | i   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
21

doubly robust estimation in the causal inference literature (Robins, Rotnitzky, and Zhao 1994;
Chernozhukov et al. 2018), and the bias-correction term is similar to the one in the augmented
| inverse probability |     | weighting |     | estimator. |     |     |     |     |     |
| ------------------- | --- | --------- | --- | ---------- | --- | --- | --- | --- | --- |
In the simplest case of random sampling with equal probabilities (π = n/N where n is
the number of expert-coded documents and N is the total number of documents), the DSL
| estimator | becomes | simple.    |     |                                        |          |                                        |            |                              |     |
| --------- | ------- | ---------- | --- | -------------------------------------- | -------- | -------------------------------------- | ---------- | ---------------------------- | --- |
|           |         | N          |     | N                                      | (cid:18) |                                        |            | (cid:19)                     |     |
|           | 1       | (cid:88)   |     | 1 (cid:88)                             |          | 1 (cid:88)                             | 1 (cid:88) |                              |     |
|           |         | Y(cid:101) | =   | Y(cid:98) −                            |          | Y(cid:98)                              | −          | Y                            | (5) |
|           | N       | i          |     | N i                                    |          | n i                                    | n          | i                            |     |
|           |         | i=1        |     | i=1                                    |          | i:Ri=1                                 | i:Ri=1     |                              |     |
|           |         |            |     | (cid:124) (cid:123)(cid:122) (cid:125) |          | (cid:124) (cid:123)(cid:122) (cid:125) | (cid:124)  | (cid:123)(cid:122) (cid:125) |     |
Meanof
|     |     |     |                   |     |                   | Meanof        | Meanof           |     |     |
| --- | --- | --- | ----------------- | --- | ----------------- | ------------- | ---------------- | --- | --- |
|     |     |     | PredictedOutcomes |     | PredictedOutcomes |               | ObservedOutcomes |     |     |
|     |     |     |                   |     |                   | inLabeledData | inLabeledData    |     |     |
The main idea is to use the expert-coded data to estimate bias from prediction errors (the
difference between the second and third terms on the right-hand side), which we subtract from
the conventional estimator that relies only on predicted labels (the first term on the right-
hand side). For example, suppose users have N = 10000 ads and randomly sampled n = 100
ads for expert annotation. The first term on the right-hand side estimates the proportion of
attacking ads by averaging the predicted labels in all N = 10000 documents (suppose it is
20%). The second and third terms on the right-hand side estimate the bias to be subtracted.
In particular, the second term estimates the proportion of attacking ads by averaging the
predicted labels in n = 100 expert-coded documents (suppose it is 18%), and the third term
estimates the proportion of attacking ads by averaging the expert-coded labels in n = 100
expert-coded documents (suppose it is 10%). Because the expert-coded data are randomly
importantly, the goal is not to correct the prediction error at each document level but at the
level of quantities of interest. In fact, we estimate the prediction error from documents with
R = 1, which is used to correct outcomes for documents with R = 0 on average.
| i   |     |     |     |     |     |     | i   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
22

sampled, we can estimate the bias by taking the difference between the second and third terms,
18−10 = 8%, which we subtract from the first term. In this simple example, the DSL estimate
| is 20−(18−10) | = 12%.     |            |     |     |     |     |
| ------------- | ---------- | ---------- | --- | --- | --- | --- |
| 4.3.2         | DSL Linear | Regression |     |     |     |     |
The DSL framework can be applied to linear regression as well (under any user-specified sam-
pling strategy). Specifically, the DSL linear regression simply needs to regress the design-
adjusted outcome Y(cid:101) (equation (4)) on independent variables X . Formally, the DSL regression
|           | i              |     |                                 |     | i   |     |
| --------- | -------------- | --- | ------------------------------- | --- | --- | --- |
| estimator | can be written | as  |                                 |     |     |     |
|           |                |     | β(cid:98) = (X⊤X)−1X⊤Y(cid:101) |     |     | (6) |
DSL
whereY(cid:101) = (Y(cid:101) ,...,Y(cid:101) )andithrowofmatrixXisX . UnderAssumption1, theDSLestimator
|     | 1 N |     |     | i   |     |     |
| --- | --- | --- | --- | --- | --- | --- |
is consistent and asymptotically normal when we use cross-fitting (Chernozhukov et al. 2018)
to generate predictions. The corresponding confidence intervals can be constructed with the
usual standard error formula. Valid statistical inference is possible because the design-adjusted
outcomes correct the prediction error on average across all different combinations of X.
E(Y(cid:101)
|            |                |             | −Y         | | X ) = 0.  |     | (7) |
| ---------- | -------------- | ----------- | ---------- | ----------- | --- | --- |
|            |                |             | i          | i i         |     |     |
| We provide | proof of these | theoretical | properties | in Appendix | B.  |     |
Importantly, the DSL estimator corrects bias only under Assumption 1 without making any
assumption about prediction errors in Y(cid:98). In practice, this means that researchers can use any
i
LLMs and supervised ML methods to construct the predicted outcomes, even if LLMs and ML
methodscontainarbitrarypredictionerrors. WhiletheDSLregressionallowsforanyprediction
error, it becomes more accurate (i.e., standard errors are smaller, and confidence intervals are
narrower) when the prediction errors are smaller. Therefore, researchers can exploit the recent
23

advances in LLMs and supervised ML methods without sacrificing valid statistical inference,
while reducing standard errors as the prediction step becomes more accurate. We illustrated
these desirable properties in simulation studies (Section 3.4) and will show more results in
| empirical | applications   | (Section 5). |     |     |     |
| --------- | -------------- | ------------ | --- | --- | --- |
| 4.3.3     | Generalization | of DSL       |     |     |     |
Finally, we emphasize that the same general idea applies to a large class of generalized linear
models (e.g., logistic, multinomial-logistic, Poisson, and linear fixed-effects regression) and to
general cases where any subset of the outcome variable and independent variables are text-
based. The only but crucial difference is that we have to bias-correct not the outcome variable
itself (as we did in equation (4)) but the underlying moment function. In general, define
m(Y ,X ;β) to be the subgradient of the convex optimization problem defining a generalized
i i
linear model. Then, the moment function for the DSL estimator can be written as
|     |     | R (cid:16) |     | (cid:17) |     |
| --- | --- | ---------- | --- | -------- | --- |
i
m(Y(cid:98),X(cid:98) ;β)− m(Y(cid:98),X(cid:98) ;β)−m(Y ,X ;β) (8)
|     |     | i i | i i | i i |     |
| --- | --- | --- | --- | --- | --- |
π
i
where Y(cid:98) and X(cid:98) are predictions for the outcome Y and independent variables X . We provide
|             | i i        |              | i   |     | i   |
| ----------- | ---------- | ------------ | --- | --- | --- |
| technical   | details in | Appendix B.  |     |     |     |
| 5 Empirical |            | Applications |     |     |     |
We now use empirical applications to illustrate how to apply DSL in a wide range of settings.
The first application, based on Fowler et al. (2021), considers settings where the outcome
variable is text-based, while the second, based on Pan and Chen (2018), examines cases where
| the independent | variables | are text-based. |     |     |     |
| --------------- | --------- | --------------- | --- | --- | --- |
24

5.1 Text as Outcome: Fowler et al. (2021)
Fowler et al. (2021) examine how the tone of political ads varies across Facebook and television.
To test this question, after annotating the tone of ads, the original authors run a linear fixed
effectsmodelthatregressesthetoneofadsonthemainindependentvariableindicatingwhether
a given ad is from Facebook or television, while including candidate-fixed-effects.
Weconductempiricalvalidationusingtheexpert-codedpoliticaladsfromFowleretal.(2021).
In particular, we use 13040 expert-coded political ads as the target population of documents
(N = 13040). But we pretend that we can only sample n = 1000 documents for expert coding
(less than 8% of the original number of expert coding) and use automated text annotation
methods to predict the tone of ads for all the documents. We then assess how well DSL and
other methods, which are based on 1000 expert annotations with 13040 predicted labels, can
recover the benchmark estimates, which use the entire 13040 expert annotations. By doing
so, we can illustrate the use of DSL step by step, while testing how DSL and other methods
perform when the automated text annotation methods have non-random prediction errors.
5.1.1 Setup
DSL requires four steps. First, we generate LLM annotations for the entire population of
documents. We here consider six versions: GPT 4, GPT 3.5, and Llama 2 with zero-shot
and few-shot learning. In the second step, we randomly sample 1000 documents for expert
coding.8 In the third step, we further improve LLM predictions by cross-fitting the generalized
8. In this empirical validation, we rely on expert coding from the original authors, so we
simply reveal expert coding for sampled documents.
25

random forest (Athey, Tibshirani, and Wager 2019) to predict the expert-coded labels with
LLM annotations produced in the first step. Finally, we combine expert-coded labels and
predicted labels in the DSL linear fixed-effects regression, where we regress the design-adjusted
outcome on the same independent variables used in the original paper. The main quantity of
interest in the original paper is the coefficient of the Facebook dummy variable. Our companion
R package dsl can implement the third and fourth steps with one function, while taking LLM
annotations (Step 1) and expert coding (Step 2) as inputs from users.
We compare DSL against the classical supervised learning approach and the LLM-only esti-
mation. For the classical supervised learning approach, we examine five widely used supervised
ML methods: drop-out regularized logistic regression (used in the original paper), lasso, ridge,
random forest, and XGBoost. We use a set of predictors used in the original paper (more than
7000 variables). For the LLM-only estimation, we consider the same six versions of LLM an-
notations. We expect that these existing approaches can provide unbiased estimates with valid
confidence intervals only when prediction errors are completely random, while DSL provides
valid statistical guarantees even with arbitrary prediction errors.
5.1.2 Results
Due to the space constraints, we focus on two outcomes, “Contrast” and “Promote,” in the
main text, while reporting the results on “Attack” in Appendix G.2. In Figure 5-(a), the
leftmost column reports the benchmark estimates based on the entire sample of 13040 expert-
coded documents. The remaining columnsshowpoint estimatesandstandard errorsof different
methods, and the X-axis shows the underlying automated text annotation method. Figure 5-
26

(b) reports coverage rates of the 95% confidence intervals.9 If a method can produce valid
confidence intervals, coverage rates of its 95% confidence interval should be at least 95%.
First, we look at the LLM-only estimation. Figure 5-(a) shows that point estimates have
largevariationsdependingontheunderlyingLLMmethodusedforautomatedtextannotations.
This is because the LLM-only estimation ignores differential prediction errors that each LLM
method makes, and as a result, estimates of the quantity of interest are biased. Some meth-
ods have small biases for one outcome, but no method has small biases across both outcomes.
Crucially, in the real-world application where researchers cannot observe the “Benchmark” es-
timate (unless they expert-code every single document), it is impossible for users to decide
which estimates to report and trust. Indeed, depending on which LLMs users choose, they
could reach statistically and substantively different results. For example, when researchers use
GPT 4 with Few-shot learning, they might conclude the effect on “Contrast” is substantively
and statistically indistinguishable from zero, whereas they would find a statistically significant,
negative effect when they use Llama 2 with Few-shot learning. Figure 5-(b) shows that con-
fidence intervals based on the LLM-only estimation are, in general, invalid (i.e., cannot cover
the benchmark estimates with 95%) due to large biases. In sum, the fundamental problem of
ignoring prediction errors is that researchers can get statistically and substantively different
estimates depending on the choice of LLMs, and there is no way to decide which estimate is
the most credible because the LLM-only estimation has no statistical guarantees.
Next,welookattheclassicalsupervisedMLmethod,whichhasthesameproblemofignoring
9. Wecomputethisastheprobabilityofconfidenceintervalscoveringthebenchmarkestimate
over 500 repeated sampling of the population of documents and expert coding.
27

Benchmark Classical Supervised ML LLM−only Estimation DSL
Outcome
=
Contrast
Outcome
=
Promote
0.0
−0.1
−0.2
0.2
0.1
0.0
Dropout Logit Lasso Ra Ri n d d g o e m Forest G X P G T B − o 4 o : s G t Z P e T r − G o 4 − P : T S − F h e 3 o . t w G 5 − : P S T Z h − e o r 3 t . L o l 5 − a : S m F h a e o − t w L 2 l − : a S Z m h e a o r t − o 2 − : S F h G e o P t w T − − S 4 h : G ot Z P e T r − G o 4 − P : T S − F h e 3 o . t w G 5 − : P S T Z h − e o r 3 t . L o l 5 − a : S m F h a e o − t w L 2 l − : a S Z m h e a o r t − o 2 − : S F h e ot w− Shot
Underlying Automated−Text−Annotation Methods
eziS
tceffE
Estimates and Standard Errors
(a)
Classical Supervised ML LLM−only Estimation DSL
Outcome
=
Contrast
Outcome
=
Promote
1.00
0.75
0.50
0.25
0.00
1.00
0.75
0.50
0.25
0.00
Dropout Logit Lasso R R i a d n g d e o m Forest X G G P B T o − os 4 t : G Ze P r T o − − 4 G S : P h T F ot − e 3 w . − 5 G : S h P Z o T t er − o 3. − 5 Ll S : a h F o m t e a w − − 2 L : S l h a Z ot e m r a o − − 2 S : h F ot e G w P − T S − h 4 o : t G Ze P r T o − − 4 G S : P h T F ot − e 3 w . − 5 G : S h P Z o T t er − o 3. − 5 Ll S : a h F o m t e a w − − 2 L : S l h a Z ot e m r a o − − 2 S : h F ot e w− Shot
Underlying Automated−Text−Annotation Methods
tnecreP
egarevoC
Coverage of 95% Confidence Intervals
(b)
Figure 5: Comparisons of DSL and Existing Approaches using Fowler et al. (2021).
Note: In Panel (a), red dotted lines represent point estimates of the “Benchmark” estimates,
andgraydottedlinesrepresenttheir95%confidenceintervals. Toshowtheaverageperformance
across random sampling of expert coding, we report the average point estimates and standard
errors across 500 repeated sampling. In Panel (b), blue dotted lines represent 95%.
28

prediction errors. Just like the LLM-only estimation, point estimates have large variations
depending on the underlying ML method used for automated text annotation.10 Importantly,
this variation exists even though each supervised ML method has roughly the same prediction
performance. Interestingly, estimates from XGBoost have small biases for both outcomes.
However, getting a good point estimate is not sufficient in social science analyses, and it is
crucial to report a valid uncertainty measure. Unfortunately, the classical supervised ML
method underestimates standard errors, and as a result, it has invalid confidence intervals.
Figure 5-(b) shows that, even for “XGBoost,” the 95% confidence intervals only cover the
true effect for about 50%, which in practice means that reported standard errors are severely
underestimated and reported p-values are wrong. These problems cannot be solved by simply
adding bootstrap because prediction errors are non-random.
Finally, we discuss how the proposed DSL overcomes the shortcomings of the existing meth-
ods. Several points are worth emphasizing. First, unlike the existing methods, point estimates
ofDSLarestableregardlessoftheunderlyingautomatedtextannotationmethodsuserschoose,
and they all have small biases. This property is fundamental in empirical research because re-
searchers do not need to worry that statistical and substantive conclusions might change if they
happen to use different LLMs. The DSL regression can also be used to correct biases when
the automated text annotation is done with the classical supervised ML method. Second, as
we see in Figure 5-(b), DSL gives valid standard errors and confidence intervals (i.e., reported
10. Researchers might wonder about extremely small confidence intervals for the supervised
ML method. This is due to both regularization bias and the failure to incorporate prediction
uncertainty, which both lead to smaller invalid standard errors.
29

confidence intervals have a coverage rate of 95%), unlike the existing methods that significantly
underestimate the true uncertainty. Taken together, DSL provides stable, unbiased point es-
timates and valid confidence intervals regardless of which LLMs researchers use to automate
annotations. This is because DSL explicitly takes into account prediction errors through the
design-based sampling of expert coding.
Researchers might wonder about the wider confidence intervals of DSL relative to other
methods. First, DSL estimators rightly have larger standard errors because they properly
take into account prediction errors. In contrast, by ignoring prediction errors, the confidence
intervals of the existing methods are invalid and underestimate the true uncertainties. Indeed,
falsely narrow confidence intervals around biased estimates are exactly what we should avoid.
Second, in practice, researchers can conduct a power analysis to decide the number of expert-
coded documents, which we discuss next.
5.1.3 Power Analysis
The number of documents experts need to annotate depends on applications. To help re-
searchers in each application, we develop a data-driven power analysis: After annotating a
small number of documents, we can predict how many more documents researchers need to
annotate in order to achieve a user-specified size of standard error.11 Figure 6 predicts how
standard errors reduce as the number of expert annotations increases. For example, as in
traditional power analysis, suppose researchers expected a coefficient of the Facebook dummy
variable to be −0.08 when the outcome is “Contrast.” To detect this effect size with suffi-
cient statistical power, scholars ordinarily need standard errors smaller than 0.04. From this
11. Our R package dsl implements this power analysis with one function.
30

Outcome = Contrast Outcome = Promote
0.045
0.040
0.035
0.030
0.025
1000 1500 2000 2500 3000 1000 1500 2000 2500 3000
Number of Expert Annotations
srorrE
dradnatS
Current Std. Error
Predicted Std. Error
Figure 6: Power Analysis to Determine the Required Number of Expert Annota-
tions. Note: Each panel reports the current standard errors (1000 expert annotated samples)
and predicted standard errors for different numbers of expert annotations. The left and right
panels consider DSL analyses when the outcome is “Contrast” and “Promote,” respectively.
figure, researchers can predict that randomly sampling 500 additional documents for expert
annotations will reduce the current standard errors from 0.044 to about 0.036.
5.2 Text as Independent Variables: Pan and Chen (2018)
We now use Pan and Chen (2018) to consider settings where the independent variables are text-
based. This application illustrates the general applicability of our proposed approach: Unlike
the previous application, documents of interest are written in Chinese, and the original authors
use logistic regression as the downstream statistical model.
The key research question in this study asks whether Chinese officials systematically conceal
complaints of corruption from upper-level authorities. To test this question, after annotating
whether each citizen complaint accuses of prefecture-level or county-level wrongdoing (Prefec-
ture Wrongdoing and County Wrongdoing), the original authors run a logistic regression that
regressestheupwardreporting(i.e., whetheragivencomplaintisreportedupwardtoprovincial-
31

level officials) on the aforementioned two independent variables (Prefecture Wrongdoing and
County Wrongdoing) and other control variables.
We again check the performance of DSL and existing methods against the benchmark esti-
mate based on the entire 1412 expert-coded complaints. We pretend that we can only sample
n = 500 documents for expert coding and use automated text annotation methods to predict
Prefecture Wrongdoing and County Wrongdoing for all the documents. While the implemen-
tation of each method is similar to the previous application, we provide all the details in
Appendix H.2.
Figure 7 shows estimated coefficients of Prefecture Wrongdoing and County Wrongdoing, as
well as the coverage rates of their 95% confidence intervals.12 As in the previous application,
estimatesfromtheLLM-onlyestimationarebiased, andimportantly, substantiveandstatistical
conclusions can flip depending on which LLM users choose for automated text annotation.
These variations exist even though the prediction accuracy of different LLMs is roughly similar
(see Appendix H). We emphasize that some methods (e.g., Llama 2) happened to have small
biases and reasonable coverages in this application, but this is simply a statistical coincidence
without any theoretical guarantee. In the real-world application where researchers cannot see
the “Benchmark” estimate, it is impossible for users to decide which estimate is the most
credible. As in the previous application, estimates from the classical supervised ML approach
are heavily biased and have invalid confidence intervals.
In contrast to these existing approaches, DSL is theoretically guaranteed to be asymptoti-
cally unbiased and have valid confidence intervals, as we can clearly see in Figure 7. In practice,
12. Appendix H.2 reports results based on the first differences, which reveal the same findings.
32

Benchmark Classical Supervised ML LLM−only Estimation DSL
Wrongdoing
Wrongdoing
Prefecture
County
2
1
0
−1
−2
−3
1.0
0.5
0.0
−0.5
−1.0
−1.5
Lasso R R i a d n g d e o m Forest X G G P B T o − o 4 s t : G P Ze T r − G o 4 P − : T S − F h 3 e o . t G w 5 − : P S T Z h − e o 3 r t L . l o 5 a − : S m F h a e o − t L w 2 l − : a S Z m h e a o r t − o 2 − : S F G h e o P t w T − −4 S : h G ot P Ze T r − G o 4 P − : T S − F h 3 e o . t G w 5 − : P S T Z h − e o 3 r t L . l o 5 a − : S m F h a e o − t L w 2 l − : a S Z m h e a o r t − o 2 − : S F h e ot w− Shot
Underlying Automated−Text−Annotation Methods
eziS
tceffE
Estimates and Standard Errors
(a)
Classical Supervised ML LLM−only Estimation DSL
Wrongdoing
Wrongdoing
Prefecture
County
1.00
0.75
0.50
0.25
0.00
1.00
0.75
0.50
0.25
0.00
Lasso Rid
R
g
a
e ndo m Forest X G
G
B
P
o
T
o
−
st
4 : G
Z
P
er
T
o
−
−
4 G
S
: P
h
T
F ot
−
e
3
w
.
−
5 G :
S
P
h Z
T
o e t
−
r
3
o
.
−
L 5 l
S
: a
h F o
m
t e
a
w
−
−
2 L : l
S
a
h Z o
m
e t r
a
o
−
−
2
S
:
h F ot e
G
w
P
−
T
S
−
h
4
o
:
t
G
Z
P
er
T
o
−
−
4 G
S
: P
h
T
F ot
−
e
3
w
.
−
5 G :
S
P
h Z
T
o e t
−
r
3
o
.
−
L 5 l
S
: a
h F o
m
t e
a
w
−
−
2 L : l
S
a
h Z o
m
e t r
a
o
−
−
2
S
:
h F ot e w− Shot
Underlying Automated−Text−Annotation Methods
tnecreP
egarevoC
Coverage of 95% Confidence Intervals
(b)
Figure 7: Comparisons of DSL and Existing Approaches using Pan and Chen (2018).
Note: In Panel (a), red dotted lines represent point estimates of the “Benchmark” estimates,
andgraydottedlinesrepresenttheir95%confidenceintervals. Toshowtheaverageperformance
across random sampling of expert coding, we report the average point estimates and standard
errors across 500 repeated sampling. In Panel (b), blue dotted lines represent 95%.
33

this means that researchers can get valid statistical estimates regardless of the choice of the
| underlying  | automated | text annotation | methods. |     |     |
| ----------- | --------- | --------------- | -------- | --- | --- |
| 6 Practical |           | Guide           |          |     |     |
We provide practical recommendations regarding the most frequently asked questions. We offer
additional practical guides in Appendix C, including reporting standards, how to choose LLMs,
how to use more complex sampling strategies (e.g., active learning), and what to do if the
| performance | of LLM | annotations   | is excellent | or poor.  |             |
| ----------- | ------ | ------------- | ------------ | --------- | ----------- |
| 6.1 Errors  | and    | Uncertainties |              | in Expert | Annotations |
In this paper, expert annotation is defined as a procedure that acts as the benchmark against
which the quality of the automated text annotation is evaluated. Therefore, as emphasized in
Section 1, DSL does not require “human” experts to provide this benchmark. We use the term
“expert annotations” to refer to the ideal (but costly) procedure we want to emulate.
In practice, expert annotations can also contain errors and uncertainties. Completely ran-
dom errors in expert annotations do not affect the validity of downstream analyses with DSL.
However, in some applications, users might worry that more fundamental uncertainties re-
main in expert annotations (e.g., Benoit, Laver, and Mikhaylov 2009; Hopkins and King 2010;
| Mikhaylov, | Laver, and | Benoit | 2012). |     |     |
| ---------- | ---------- | ------ | ------ | --- | --- |
We recommend having multiple expert coders and explicitly incorporating disagreements
between coders as additional uncertainties in the estimates, if the disagreements cannot be
reconciled. We take a quasi-Bayesian approach, similar to a multiple imputation algorithm for
missing data (King et al. 2001; Little and Rubin 2019). Suppose there are K expert coders
for each document. Then, we take the following three steps. (1) Randomly sample one expert
34

annotation among K annotations within each document. (2) Estimate DSL with a sampled
set of expert annotations. Draw quantities of interest Q times from the estimated asymptotic
normal distribution. (3) Repeat Step-(1) and Step-(2) B times and obtain Q × B draws of
quantities of interest. Researchers can then use its average as the point estimate and its 2.5
and 97.5 percentiles to form the confidence interval.
By combining bootstrap-style re-sampling in Step-(1) with DSL in Step-(2), this simple
procedure enables users to take into account uncertainties in expert annotations in addition
to uncertainties that DSL already handles, i.e., non-random prediction errors and sampling
errors. When the intercoder reliability is low, there are more uncertainties about labels, and
this is naturally reflected in Step-(1) of the procedure. Importantly, the procedure described
above assumes a uniform prior over the quality of the expert annotators. If users have prior
knowledge about which annotator is more credible than others, they can incorporate this prior
into the quasi-Baysian procedure by increasing the probability of sampling a label from more
credible coders in Step-(1). In Appendix D, we illustrate how this method works in practice.
6.2 Limitations
Automated text annotation, in particular, the use of LLM annotations, is a rapidly advanc-
ing technology. While we propose a generic method that can incorporate any automated text
annotation methods with any prediction error, it might sometimes be possible to derive an
application-specific automated text annotation method that can statistically guarantee com-
pletely random prediction errors or can model prediction errors. If so, they can potentially
get smaller standard errors than DSL. DSL is a general-purpose method that is most useful
when researchers want to avoid stringent assumptions about prediction errors in automated
35

text annotation methods.
6.3 Wide Applicability
While we so far focused on regression analyses in text-as-data applications, which are the most
commondownstreamanalyses, theDSLframeworkcanbeusedforabroaderrangeofstatistical
analyses in the social sciences. Our general framework is applicable to any application where
researchers use predictive methods to scale up measurements. In Appendix C.3, we discuss how
researchers can also apply DSL to (a) estimation of category proportions over time or across
groups (e.g., Hopkins and King 2010), (b) causal inference with texts (e.g., Egami et al. 2022),
and (c) analyses of a range of unstructured data, e.g., images, audios, videos (e.g., Knox and
Lucas 2021; Torres and Cantu´ 2022).
7 Concluding Remarks
In this paper, we propose a general framework for using recent advances in automated text
annotation methods (e.g., LLMs) and, more generally, generative artificial intelligence (AI)
in the social sciences. The proposed framework guarantees statistical validity of downstream
analyses, without suffering from bias due to unknown non-random prediction errors in AI
models.
Due to the recent rapid advances in AI, we can happily expect that new AI models will be
developed every month or even faster. This also means that we will continue to have a suite of
models that have high predictive performance but lack scientific and theoretical understanding
about their prediction errors and various biases (political, racial, gender, social, and so on).
However, the existing approaches (i.e., ignoring prediction errors) exactly need to justify how
prediction errors arise. Therefore, currently, researchers have to pretend that new AI models
36

have completely random prediction errors, or they have to miss those recent advances. DSL
overcomes this tradeoff by incorporating a small number of high-quality, expensive expert an-
notations. With DSL, researchers can always apply state-of-the-art AI models to their social
science studies, without worrying that prediction errors and biases in such AI models might
invalidate their scientific and statistical conclusions. We hope that this paper provides a foun-
dation for future work considering this exciting intersection of the social sciences, machine
learning, and AI.
37

References
Angelopoulos, Anastasios N., Stephen Bates, Clara Fannjiang, Michael I. Jordan, and Tijana
Zrnic. 2023. “Prediction-powered inference.” Science 382 (6671): 669–674. https://doi.
org/10.1126/science.adi6000. https://www.science.org/doi/abs/10.1126/science.adi6000.
Athey, Susan, Julie Tibshirani, and Stefan Wager. 2019. “Generalized Random Forests.” The
Annals of Statistics 47 (2): 1148–1178. https://doi.org/10.1214/18-AOS1709. https:
//doi.org/10.1214/18-AOS1709.
Barbera´, Pablo, Amber E Boydstun, Suzanna Linn, Ryan McMahon, and Jonathan Nagler.
2021. “Automated Text Classification of News Articles: A Practical Guide.” Political Anal-
ysis 29 (1): 19–42.
Bender, Emily M, Timnit Gebru, Angelina McMillan-Major, and Shmargaret Shmitchell. 2021.
“On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?” In Proceedings
of the 2021 ACM conference on fairness, accountability, and transparency, 610–623.
Benoit, Kenneth, Michael Laver, and Slava Mikhaylov. 2009. “Treating Words as Data with
Rrror: Uncertainty in Text Statements of Policy Positions.” American Journal of Political
Science 53 (2): 495–513.
Bommasani,Rishi,DrewAHudson,EhsanAdeli,RussAltman,SimranArora,SydneyvonArx,
Michael S Bernstein, Jeannette Bohg, Antoine Bosselut, Emma Brunskill, et al. 2021. “On
the Opportunities and Risks of Foundation Models.” arXiv preprint arXiv:2108.07258.
38

Chernozhukov, Victor, Denis Chetverikov, Mert Demirer, Esther Duflo, Christian Hansen,
Whitney Newey, and James Robins. 2018. “Double/Debiased Machine Learning for Treat-
ment and Structural Parameters.” Econometrics Journal 21:C1–C68.
Egami, Naoki, Christian J. Fong, Justin Grimmer, Margaret E. Roberts, and Brandon M.
Stewart. 2022. “How to Make Causal Inferences Using Texts.” Science Advances 8 (42):
| eabg2652. https://doi.org/10.1126/sciadv.abg2652. |     |     |
| ------------------------------------------------- | --- | --- |
Egami, Naoki, Musashi Hinck, Brandon Stewart, and Hanying Wei. 2023. “Using Imperfect
Surrogates for Downstream Inference: Design-based Supervised Learning for Social Sci-
ence Applications of Large Language Models.” Advances in Neural Information Processing
| Systems 36. |     |     |
| ----------- | --- | --- |
Fong, Christian, and Matthew Tyler. 2021. “Machine learning predictions as regression covari-
| ates.” Political | Analysis | 29 (4): 467–484. |
| ---------------- | -------- | ---------------- |
Fowler, Erika Franklin, Michael M Franz, Gregory J Martin, Zachary Peskowitz, and Travis
N Ridout. 2021. “Political Advertising Online and Offline.” American Political Science
| Review 115 | (1): 130–149. |     |
| ---------- | ------------- | --- |
Gilardi, Fabrizio, Meysam Alizadeh, and Ma¨el Kubli. 2023. “ChatGPT Outperforms Crowd-
Workers for Text-Annotation Tasks.” arXiv preprint arXiv:2303.15056.
Grimmer, Justin, Margaret E Roberts, and Brandon M Stewart. 2022. Text as data: A new
framework for machine learning and the social sciences. Princeton University Press.
39

Grimmer, Justin, and Brandon M Stewart. 2013. “Text as Data: The Promise and Pitfalls of
Automatic Content Analysis Methods for Political Texts.” Political analysis 21 (3): 267–
297.
Hopkins, Daniel J, and Gary King. 2010. “A Method of Automated Nonparametric Content
Analysis for Social Science.” American Journal of Political Science 54 (1): 229–247.
King, Gary, James Honaker, Anne Joseph, and Kenneth Scheve. 2001. “Analyzing Incomplete
Political Science Data: An Alternative Algorithm for Multiple Imputation.” American po-
| litical science | review | 95 (1): 49–69. |     |     |
| --------------- | ------ | -------------- | --- | --- |
Knox, Dean, and Christopher Lucas. 2021. “A Dynamic Model of Speech for the Social Sci-
| ences.” American | Political | Science | Review 115 | (2): 649–666. |
| ---------------- | --------- | ------- | ---------- | ------------- |
Knox, Dean, Christopher Lucas, and Wendy K Tam Cho. 2022. “Testing Causal Theories with
Learned Proxies.” Annual Review of Political Science 25:419–441.
Linegar, Mitchell, Rafal Kocielnik, and R Michael Alvarez. 2023. “Large Language Models and
| Political Science.” | Frontiers | in Political | Science | 5:1257092. |
| ------------------- | --------- | ------------ | ------- | ---------- |
Little, Roderick JA, and Donald B Rubin. 2019. Statistical Analysis With Missing Data. Vol. 3.
| John Wiley | & Sons. |     |     |     |
| ---------- | ------- | --- | --- | --- |
Lundberg, Ian, Rebecca Johnson, and Brandon M Stewart. 2021. “What is Your Estimand?
Defining the Target Quantity Connects Statistical Evidence to Theory.” American Socio-
| logical Review | 86 (3): | 532–565. |     |     |
| -------------- | ------- | -------- | --- | --- |
40

Mikhaylov, Slava, Michael Laver, and Kenneth R Benoit. 2012. “Coder Reliability and Mis-
classification in the Human Coding of Party Manifestos.” Political Analysis 20 (1): 78–
91.
Mozer, Reagan, and Luke Miratrix. 2023. “Decreasing the Human Coding Burden in Random-
izedTrialswithText-basedOutcomesviaModel-AssistedImpactAnalysis.”arXiv preprint
arXiv:2309.13666.
Ollion, Etienne, Rubing Shen, Ana Macanovic, and Arnault Chatelain. 2023. “Chatgpt for Text
Annotation? Mind the Hype!” SocArXiv. October 4.
Ornstein,JosephT,EliseNBlasingame,andJakeSTruscott.2022.How to Train Your Stochas-
tic Parrot: Large Language Models for Political Texts. Technical report. Working Paper.
Pan, Jennifer, and Kaiping Chen. 2018. “Concealing Corruption: How Chinese Officials Distort
Upward Reporting of Online Grievances.” American Political Science Review 112 (3): 602–
620.
Pangakis, Nicholas, Samuel Wolken, and Neil Fasching. 2023. “Automated Annotation with
Generative AI Requires Validation.” arXiv preprint arXiv:2306.00176.
Robins, James M, Andrea Rotnitzky, and Lue Ping Zhao. 1994. “Estimation of Regression
Coefficients When Some Regressors Are Not Always Observed.” Journal of the American
Statistical Association 89 (427): 846–866.
Spirling, Arthur. 2023. “Why Open-Source Generative AI Models Are An Ethical Way Forward
For Science.” Nature 616 (7957): 413–413.
41

Torres, Michelle, and Francisco Cantu´. 2022. “Learning to See: Convolutional Neural Networks
for the Analysis of Social Science Data.” Political Analysis 30 (1): 113–131.
Wang, Siruo, Tyler H McCormick, and Jeffrey T Leek. 2020. “Methods for Correcting Inference
based on Outcomes Predicted by Machine Learning.” Proceedings of the National Academy
of Sciences 117 (48): 30266–30275.
Zhang, Han. 2021. “How Using Machine Learning Classification as a Variable in Regression
Leads to Attenuation Bias and What to Do About It.” SocArXiv.
Ziems, Caleb, William Held, Omar Shaikh, Jiaao Chen, Zhehao Zhang, and Diyi Yang. 2024.
“Can large language models transform computational social science?” Computational Lin-
guistics 50 (1): 237–291.
42

|     |     |     | Online | Supplementary |     | Appendix |     |     |
| --- | --- | --- | ------ | ------------- | --- | -------- | --- | --- |
:
Using Large Language Model Annotations for the Social Sciences:
|     |     | A General |     | Framework     | of Using | Predicted | Variables |     |
| --- | --- | --------- | --- | ------------- | -------- | --------- | --------- | --- |
|     |     |           |     | in Downstream |          | Analyses  |           |     |
Contents
| A Connection   | to                | Literature |           |               |        |     |     | 1   |
| -------------- | ----------------- | ---------- | --------- | ------------- | ------ | --- | --- | --- |
| B Theories     | of DSL            |            |           |               |        |     |     | 2   |
| C Practical    | Guide             |            |           |               |        |     |     | 10  |
| D Errors       | and Uncertainties |            | in Expert | Annotations   |        |     |     | 12  |
| E Simulation   | Studies           |            |           |               |        |     |     | 14  |
| F Introduction | to                | LLMs       |           |               |        |     |     | 15  |
| G Empirical    | Application       |            | based on  | Fowler et al. | (2021) |     |     | 16  |
| H Empirical    | Application       |            | based on  | Pan and Chen  | (2018) |     |     | 18  |
| I Literature   | Review            |            |           |               |        |     |     | 22  |

A Connection to Literature
This paper builds on several lines of work. First, this paper is motivated by the rapid and fundamental development of
LLMs and, more generally, generative artificial intelligence. Over the last couple of years, many papers have shown the
incredible potential of LLMs for social science research in a wide range of problems (e.g., Argyle et al. 2023; Linegar,
Kocielnik, and Alvarez 2023; Palmer and Spirling 2023; Wu et al. 2023). Among them, one of the most promising and
popular use cases is text annotations by LLMs: to name a few papers, Bommasani et al. (2021), Ornstein, Blasingame,
andTruscott(2022),Gilardi,Alizadeh,andKubli(2023),Ollionetal.(2023),Pangakis,Wolken,andFasching(2023),and
Ziemsetal.(2024),andthislistisgrowingrapidly. EachpaperdiscussesandevaluatesthepromiseandrisksofusingLLM
annotationsindifferenttypesofsocialscienceapplications. Allofthesepaperscurrentlyonlyfocusonassessingpredictive
performance,andnopaperdiscusseshowsuchpredictedtextlabelscanbeproperlyusedindownstreamstatisticalanalyses,
which is the central focus of our paper.
This paper draws upon the large literature on double/debiased machine learning and doubly-robust estimation for
missing data and causal inference (Robins, Rotnitzky, and Zhao 1994; Chernozhukov et al. 2018; Kennedy 2022). In
particular, our doubly robust procedure builds on foundational results on semiparametric inference with missing data
(Robins and Rotnitzky 1995; Tsiatis 2006; Rotnitzky and Vansteelandt 2014; Davidian 2022) and the growing literature
on doubly robust estimators for surrogate outcomes (Kallus and Mao 2020) and semi-supervised learning (Chakrabortty
and Cai 2018; Chakrabortty, Dai, and Tchetgen Tchetgen 2022). Like these papers, we exploit the influence function to
derive debiased estimators.
Our paper contributes to the growing literature on the use of predicted variables in statistical analyses. A number
of papers develop methods for specific scenarios by making assumptions about the underlying data generating process.
For example, Wang, McCormick, and Leek (2020) take into account the predicted outcome by modeling prediction errors,
Fong and Tyler (2021) address the predicted independent variables under exclusion restriction, Zhang (2021) relies on a
conditionalindependenceassumptionaboutpredictionerrors,andKnox,Lucas,andCho(2022)usesignedcausaldiagrams
to compute bounds. In contrast to these papers, we only assume that researchers control the sampling process for expert
annotations, and we do not make any assumption about the nature of prediction errors, which is particularly difficult to
justify in applications of LLMs.
Our paper is most closely related to recent methods that build on the doubly robust estimation to deal with predicted
variables. Inparticular,ourpaperextendsandgeneralizesmethodsproposedinEgamietal.(2023). Inparticular,theyonly
cover cases where the outcome variable requires text annotation and only discuss several models for downstream analyses.
Byderivingamoregeneralresult,wecovercaseswhereanysubsetoftheoutcomeandindependentvariablesaretext-based
andaccommodateamuchwiderrangeofdownstreamanalyses. Thismethodologicalgeneralizationisfundamentalbecause
about 45% of applications use text-based variables as independent variables, which is not covered in Egami et al. (2023).
In addition, we make practical contributions by providing detailed guides on LLM annotations (e.g., how to use LLM
annotations in DSL) and expert annotations (e.g., how to determine the required number of expert annotations, and how
to handle errors in expert annotations) using two empirical applications.
Theoretically,ourpaperisalsocloselyrelatedtotworecentpapersthatsimilarlybuildontheliteratureondoublyrobust
methods. Prediction-powered inference (Angelopoulos et al. 2023) provides a similar framework to ours, but they have
primarilyfocusedonsettingswheretheoutcomevariableispredictedwhileprovidingbothasymptoticandnon-asymptotic
confidence intervals. Mozer and Miratrix (2023) focus on settings where the predicted outcome variable is used within
randomized experiments. Methodologically, our paper extends these previous results in three ways. First, while these
papers only cover cases of text-based outcome variables, we cover cases where any subset of the outcome and independent
1

variables are text-based. This methodological generalization is fundamental because about 45% of applications use text-
based variables as independent variables. Second, we develop a data-driven power analysis to help users determine the
required number of expert annotations. Third, we derive DSL estimators for a much wider range of downstream analyses
popular in the social sciences, including linear fixed effects regression and the instrumental variable method. In addition,
we make practical contributions by providing new statistical software and clarifying detailed guides using two empirical
applications. Katsumata and Yamauchi (2023) also develop a framework for using predicted variables while building on a
| different framework | of control | variates   | (Chen | and Chen | 2000). |     |     |     |
| ------------------- | ---------- | ---------- | ----- | -------- | ------ | --- | --- | --- |
| B Theories          | of         | DSL        |       |          |        |     |     |     |
| B.1 Notation        | and        | Assumption |       |          |        |     |     |     |
SupposeresearchersareinterestedinanalyzingN documents. Foreachdocumenti, wedefineD tobeavectorofrelevant
i
variablesweincludeinthedownstreamanalyses. Forregressionproblems,D =(Y,X)whereY istheoutcomevariableand
X is a vector of the independent variables. For the mean estimation problem, D = Y. For observational causal inference
under conditional ignorability, D = (Y,T,X) where Y is the outcome variable, T is the treatment, and X is a vector of
observed covariates. For the instrumental variable method, D = (Y,T,Z,X) where Y is the outcome of interest, T is the
| treatment, | Z is the instrument, | and | X is a vector | of observed | covariates. |     |     |     |
| ---------- | -------------------- | --- | ------------- | ----------- | ----------- | --- | --- | --- |
Intext-as-dataapplications,weoftencannotobserveallrelevantvariablesDfortheentirepopulationofdocuments. We
decompose D into two parts D =(Dobs,Dmis) where Dobs represents variables that are observed for the entire population
of documents and Dmis represents variables that are observed only for a subset of documents that are expert-coded. For
example, when the outcome variable Y requires text annotation but X = (X ,...,X ) are observed for every document,
|     |     |     |     |     |     |     | 1 4 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
Dmis = Y and Dobs = (X ,X ,X ,X ). When Y and X are text-based but the remaining independent variables are
|     |     | 1 2 | 3 4 |     | 1   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
observed for every document, Dmis = (Y,X ) and Dobs = (X ,X ,X ). This general setup allows for settings where any
|           |                    |                | 1   |     | 2 3 | 4   |     |     |
| --------- | ------------------ | -------------- | --- | --- | --- | --- | --- | --- |
| subset of | relevant variables | is text-based. |     |     |     |     |     |     |
We use Q to denote a vector of optional document-level variables that help predict Dmis. When researchers use LLM
|     | i   |     |     |     |     |     | i   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
annotations as the automated text annotation for Dmis, those LLM annotations are included in Q . When researchers
i i
use the classical supervised machine learning method to predict Dmis, a vector of word frequencies or word embedding is
i
| included | in Q i . |     |     |     |     |     |     |     |
| -------- | -------- | --- | --- | --- | --- | --- | --- | --- |
Finally, we use R ∈ {0,1} to denote whether document i is sampled for expert annotations. For documents with
i
R =1, we observe values for Dmis, but for documents with R =0, values for Dmis are missing.
| i   |     | i   |     |     | i   |     | i   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
The key assumption behind DSL (Assumption 1) is that the probability of sampling documents for expert-coding
π is decided by researchers, and π is larger than zero for every document. Without loss of generality, we can write
| i   |     |     | i   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
π = π(Dobs,Q ). This notation only assumes that R depends on a subset of (Dobs,Q ), so it also accommodates more
| i   | i i |     |     | i   |     |     | i i |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
common settings like random sampling where π i does not depend on any variable or stratified sampling where π i only
depends on a small number of observed variables. Under this design-based sampling, the sampling probability π is known
from the research design (i.e., not need to estimate the sampling probability), and we have
|             |         |     |     |        | Dmis |Dobs,Q |     |     |        |
| ----------- | ------- | --- | --- | ------ | ------------ | --- | --- | ------ |
|             |         |     |     | R i ⊥⊥ |              | i . |     | (OA.1) |
|             |         |     |     |        | i i          |     |     |        |
| B.2 General | Results |     |     |        |              |     |     |        |
We first provide proof for a general DSL estimator based on convex objective functions.
Suppose researchers are interested in estimands that can be characterized as the solution to the following convex
2

| optimization |     | problem. |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------ | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
argminE{ℓ(D;β)}
|     |     |     |     |     |     |     | β∗  | :=  |     |     |     |     |     | (OA.2) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |
β∈Rd
whereℓ(D;β)istheconvexlossfunctionandD representsalltherelevantvariablesinthedownstreamstatisticalanalyses.
This general setup incorporates a wide range of common regression models (see Appendix B.3), such as linear regression
with a continuous outcome, logistic regression with a binary outcome, multinomial logistic regression with a categorical
outcome, andPoissonregressionwithacountoutcome,aswellaslinearfixed-effectsregressionpopularincausalinference.
Undermildregularityconditions,convexityallowsustoexpressβ∗ asthesolutiontothefollowingestimationequation.
E{m(D;β)}
|     |     |     |     |     |     |     |     |     | =   | 0   |     |     |     | (OA.3) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |
where m(D;β)∈Rd is a subgradient of the loss function ℓ(D;β) with respect to β.
IfresearcherscanobserveallrelevantvariablesD,theycandirectlysolvetheestimationequationtoobtainaconsistent
| and | asymptotically |     | normal | estimator. |     |                 |                  |     |                     |                 |           |     |     |        |
| --- | -------------- | --- | ------ | ---------- | --- | --------------- | ---------------- | --- | ------------------- | --------------- | --------- | --- | --- | ------ |
|     |                |     |        |            |     |                 |                  |     | (cid:13) N          |                 | (cid:13)2 |     |     |        |
|     |                |     |        |            |     |                 |                  |     | (cid:13) 1 (cid:88) |                 | (cid:13)  |     |     |        |
|     |                |     |        |            |     | β(cid:98)oracle | :=argmin(cid:13) |     |                     | m(D ;β)(cid:13) | .         |     |     | (OA.4) |
|     |                |     |        |            |     |                 |                  |     | (cid:13)N           | i               | (cid:13)  |     |     |        |
β∈Rd
|     |     |     |     |     |     |     |     |     | (cid:13) i=1 |     | (cid:13) |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | -------- | --- | --- | --- |
2
However, when some relevant variables are not observed for the entire population of interest, this estimator is infeasible.
DSL can estimate β even when some variables Dmis are observed only for a subset of expert-coded documents. In
i
| general, | the | moment | function | for | DSL | is defined | as  |     |     |          |     |     |          |     |
| -------- | --- | ------ | -------- | --- | --- | ---------- | --- | --- | --- | -------- | --- | --- | -------- | --- |
|          |     |        |          |     |     |            |     |     |     | (cid:16) |     |     | (cid:17) |     |
R i
m (D ,Q ,R ;β,π,g ):=m(D obs,D(cid:98) mis;β)− m(D obs,D(cid:98) mis;β)−m(D obs,D mis;β) (OA.5)
|     | DSL | i   | i i | (cid:98) |     | i   | i   | π(Dobs | ,Q ) | i   | i   | i   | i   |     |
| --- | --- | --- | --- | -------- | --- | --- | --- | ------ | ---- | --- | --- | --- | --- | --- |
|     |     |     |     |          |     |     |     |        | i i  |     |     |     |     |     |
where D(cid:98) mis = g (D obs,Q ) and g (·) is a estimated supervised machine learning model to predict D mis with covariates
|     | i   | (cid:98) | i   | i   | (cid:98) |     |     |     |     |     |     |     | i   |     |
| --- | --- | -------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(Dobs,Q ). Using this moment function, the proposed DSL estimator is defined as,
i i
|     |     |     |     |     |     |     | (cid:13) |     |     |     | (cid:13)2 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --------- | --- | --- | --- |
K
|     |     |     |     |     |     |     | (cid:13) 1 | (cid:88) (cid:88) |     |     | (cid:13) |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----------------- | --- | --- | -------- | --- | --- | --- |
β(cid:98)DSL :=argmin(cid:13) m (D ,Q ,R ;β,π,g )(cid:13) , (OA.6)
|     |     |     |     |     |     |      | (cid:13)N |         | DSL | i i | i (cid:98)k (cid:13) |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --------- | ------- | --- | --- | -------------------- | --- | --- | --- |
|     |     |     |     |     |     | β∈Rd | (cid:13)  |         |     |     | (cid:13)             |     |     |     |
|     |     |     |     |     |     |      |           | k=1i∈Lk |     |     | 2                    |     |     |     |
where we employ a K-fold cross-fitting procedure (Chernozhukov et al. 2018). We first partition the observation indices
i=1,...,n into K groups L where k =1,...,K. We then learn the supervised machine learning model g by predicting
|      |       |         |         | k            |     |           |     |     |        |     |     |     | (cid:98)k |     |
| ---- | ----- | ------- | ------- | ------------ | --- | --------- | --- | --- | ------ | --- | --- | --- | --------- | --- |
| Dmis | using | (Dobs,Q | ) using | expert-coded |     | documents |     | not | in L . |     |     |     |           |     |
| i    |       | i       | i       |              |     |           |     |     | k      |     |     |     |           |     |
Proposition 1 Under Assumption 1 and the standard regularity conditions stated below, the cross-fitted DSL estimator
(equation (OA.6)) β(cid:98)DSL is consistent and asymptotically normal as sample size N goes to infinity.
√
|     |     |     |     |     |     |     | N(β(cid:98)DSL | −β∗)−→ | d   | N(0,V). |     |     |     | (OA.7) |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ------ | --- | ------- | --- | --- | --- | ------ |
where
|     |     |     |     | V = | S E(m |     | (D ,Q | ,R ;β∗,π,g)m |     | (D ,Q | ,R ;β∗,π,g)⊤)S | ,   |     |     |
| --- | --- | --- | --- | --- | ----- | --- | ----- | ------------ | --- | ----- | -------------- | --- | --- | --- |
|     |     |     |     |     | V     | DSL | i     | i i          |     | DSL i | i i            | V   |     |     |
|     |     |     |     |     |      |     |       |              | −1 |       |                |     |     |     |
|     |     |     |     |     |       | ∂m  | (D ,Q | ,R ;β∗,π,g)  |     |       |                |     |     |     |
|     |     |     |     |     | E     | DSL | i     | i i          |     |       |                |     |     |     |
|     |     |     |     | S = |      |     |       |              |    |       |                |     |     |     |
|     |     |     |     | V   |       |     | ∂β    |              |     |       |                |     |     |     |
Here we define g to be the probability limit of the estimated supervised machine learning function g (cid:98)k in the sense that for
E
each k, ||g −g|| =o (1) and (||m(L;β∗,g )−m(L;β∗,g)||2)=o (1). This probability limit does not need to be equal to
|     | (cid:98)k | 2   | p   |     | k   |     | (cid:98)k |     | 2   | p   |     |     |     |     |
| --- | --------- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
the true conditional expectation g∗. Thus, we do not assume the correct specification of the estimated supervised machine
learning function.
3

Proof. In this proof, for the notational simplicity, we use L =(D ,Q ,R ) and omit π from the notation of the moment
i i i i
function. That is, we use m
DSL
(L
i
;β,g) to denote the DSL moment function. We also use β(cid:98)to denote β(cid:98)DSL .
Using the mean value theorem, we can first expand the moment equation around β∗.
1 (cid:88) K (cid:88) 1 (cid:88) K (cid:88) 1 (cid:88) K (cid:88) ∂m DSL (L i ;β(cid:101),g (cid:98)k )
N
m
DSL
(L
i
;β(cid:98),g
(cid:98)k
) =
N
m
DSL
(L
i
;β∗,g
(cid:98)k
)+(β(cid:98)−β∗)
N ∂β
k=1i∈Lk k=1i∈Lk k=1i∈Lk
where β(cid:101) is a mean value, located between β(cid:98) and β∗. For the convex objective function, the first order condition implies
that we also have
K
1 (cid:88) (cid:88)
N
m
DSL
(L
i
;β(cid:98),g
(cid:98)k
) = 0.
k=1i∈Lk
Therefore, combining two equations, we have
 −1
√ 1 (cid:88) K (cid:88) ∂m DSL (L i ;β(cid:101),g (cid:98)k ) 1 (cid:88) K (cid:88)
N(β(cid:98)−β∗) = − N ∂β  ×√ N m DSL (L i ;β∗,g (cid:98)k )
k=1i∈Lk k=1i∈Lk
(cid:124) (cid:123)(cid:122) (cid:125) (cid:124) (cid:123)(cid:122) (cid:125)
(a) (b)
We will consider terms (a) and (b) in order.
Term (b). We begin with the main term (b), which can be decomposed into three terms.
K
1 (cid:88) (cid:88)
√ m (L ;β∗,g ) = H +H +H
DSL i (cid:98)k 1 2 3
N
k=1i∈Lk
where
K
1 (cid:88) (cid:88)
H := √ (m (L ;β∗,g )−E (m (L ;β∗,g )))−(m (L ;β∗,g)−E (m (L ;β∗,g)))
1 DSL i (cid:98)k k DSL i (cid:98)k DSL i k DSL i
N
k=1i∈Lk
K
1 (cid:88) (cid:88)
H := √ (m (L ;β∗,g)−E (m (L ;β∗,g)))
2 DSL i k DSL i
N
k=1i∈Lk
K
1 (cid:88)
H := √ N ×E (m (L ;β∗,g )).
3 k k DSL i (cid:98)k
N
k=1
Here we use E to denote the expectation over L conditional on L .
k k −k
H isknownastheempiricalprocessterm. Giventhatweusecross-fittingandE (||m (L ;β∗,g )−m (L ;β∗,g)||2)=
1 k DSL i (cid:98)k DSL i 2
o (1), we obtain H =o (1) by Lemma 2 of Kennedy, Balakrishnan, and G’Sell (2020).
p 1 p
Next, to examine H , we first show that E(m (L ;β∗,g))=0 for any arbitrary fixed function g.
2 DSL i (cid:101) (cid:101)
E(m (L ;β∗,g))
DSL i (cid:101)
(cid:18) (cid:19)
= E m(Dobs,g(Dobs,Q );β∗)− R i (cid:0) m(Dobs,g(Dobs,Q );β∗)−m(Dobs,Dmis;β∗) (cid:1)
i (cid:101) i i π(Dobs,Q ) i (cid:101) i i i i
i i
(cid:18)(cid:18) (cid:12) (cid:19)(cid:19)
= E π(Do R bs i ,Q ) m(D i obs,D i mis;β∗) (cid:12) (cid:12) (cid:12) D i obs,Q i
i i
(cid:18)(cid:18)(cid:18) (cid:19) (cid:12) (cid:19)(cid:19)
+ E 1− π(Do R bs i ,Q ) m(D i obs,g (cid:101) (D i obs,Q i );β∗) (cid:12) (cid:12) (cid:12) D i obs,Q i
i i
= E (cid:18)E(R i |D i obs,Q i ) E(cid:0) m(Dobs,Dmis;β∗)|Dobs,Q (cid:1) (cid:19)
π(Dobs,Q ) i i i i
i i
(cid:18)(cid:18) E(R |Dobs,Q ) (cid:19) (cid:19)
+ E 1− i i i m(Dobs,g(Dobs,Q );β∗)
π(Dobs,Q ) i (cid:101) i i
i i
4

|     |     | E(cid:0) m(Dobs,Dmis;β∗) |     |     | (cid:1) |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ------------------------ | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | =   |                          | i   | i   |         |     |     |     |     |     |     |     |     |     |     |
= 0.
where the first equality comes from the definition of the DSL moment function, and the second equality comes from
the rearrangement of the terms and the law of total expectation. The third equality comes from Assumption 1, i.e.,
R ⊥⊥Dmis |Dobs,Q ,whichimpliesE(R m(Dobs,Dmis;β∗)|Dobs,Q )=E(R |Dobs,Q )E(m(Dobs,Dmis;β∗)|Dobs,Q ).
| i   | i i | i   |     |     | i   | i   | i   |     | i   | i   | i   | i i | i   | i   | i i |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
E(R
The fourth equality comes from the equality that | Dobs,Q ) = Pr(R = 1 | Dobs,Q ) = π(Dobs,Q ) because R is a
|     |     |     |     |     |     |     | i   | i   | i   | i   |     | i i | i   | i   | i   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
binary variable. Finally, due to convexity of the objective function, E(m(D ,β∗))=0.
i
| We also | have |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
K
|     |     |     |     |      | 1   | (cid:88) | (cid:88) |             |     |     |     |          |     |     |     |
| --- | --- | --- | --- | ---- | --- | -------- | -------- | ----------- | --- | --- | --- | -------- | --- | --- | --- |
|     |     |     |     | H := | √   |          | (m       | (L ;β∗,g)−E |     | (m  | (L  | ;β∗,g))) |     |     |     |
|     |     |     |     | 2    |     |          |          | DSL i       |     | k   | DSL | i        |     |     |     |
N
k=1i∈Lk
|     |     |     |     |     | 1   | K        |          |            |     |     |      |          |     |     |     |
| --- | --- | --- | --- | --- | --- | -------- | -------- | ---------- | --- | --- | ---- | -------- | --- | --- | --- |
|     |     |     |     |     |     | (cid:88) | (cid:88) | ;β∗,g)−E(m |     |     |      | ;β∗,g))) |     |     |     |
|     |     |     |     | =   | √   |          | (m       | DSL (L i   |     | DSL | (L i |          |     |     |     |
N
k=1i∈Lk
|     |     |     |     |     | 1   | N        |     |            |     |     |          |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------- | --- | ---------- | --- | --- | -------- | --- | --- | --- | --- |
|     |     |     |     |     |     | (cid:88) |     | ;β∗,g)−E(m |     |     | ;β∗,g))) |     |     |     |     |
|     |     |     |     | =   | √   | (m       | (L  |            |     | (L  |          |     |     |     |     |
|     |     |     |     |     | N   |          | DSL | i          |     | DSL | i        |     |     |     |     |
i=1
because E (m (L ;β∗,g))=E(m (L ;β∗,g)). Finally, we can use the central limit theorem to show that
|             | k DSL | i           |     | DSL | i          |         |     |            |     |              |               |     |     |     |        |
| ----------- | ----- | ----------- | --- | --- | ---------- | ------- | --- | ---------- | --- | ------------ | ------------- | --- | --- | --- | ------ |
|             |       |             |     |     | H −→ d     | N(0,E(m |     | (L ;β∗,g)m |     | (L ;β∗,g)⊤)) |               |     |     |     | (OA.8) |
|             |       |             |     |     | 2          |         | DSL | i          |     | DSL i        |               |     |     |     |        |
|             |       | ;β∗,g))=E(m |     |     |            |         |     |            |     | E(m          |               |     |     |     |        |
| where Var(m |       | (L          |     |     | (L ;β∗,g)m |         | (L  | ;β∗,g)⊤)   | as  |              | (L ;β∗,g))=0. |     |     |     |        |
|             | DSL   | i           |     | DSL | i          |         | DSL | i          |     | DSL          | i             |     |     |     |        |
As for H , using the similar proof for E(m (L ;β∗,g)) = 0, we have E (m (L ;β∗,g )) = 0 because g is a fixed
|          | 3           |     |          |            |      | DSL       | i   | (cid:101) |     |     | k DSL | i (cid:98)k |     |     | (cid:98)k |
| -------- | ----------- | --- | -------- | ---------- | ---- | --------- | --- | --------- | --- | --- | ----- | ----------- | --- | --- | --------- |
| function | conditional | on  | L .      | Therefore, | H    | =0.       |     |           |     |     |       |             |     |     |           |
|          |             |     | −k       |            |      | 3         |     |           |     |     |       |             |     |     |           |
| Taken    | together,   | for | the main | term       | (b), | we obtain |     |           |     |     |       |             |     |     |           |
K
|     |     |     | 1 (cid:88) | (cid:88) |     |             | d    |         |     |            |     |               |     |     |     |
| --- | --- | --- | ---------- | -------- | --- | ----------- | ---- | ------- | --- | ---------- | --- | ------------- | --- | --- | --- |
|     |     | √   |            | m        | (L  | ;β∗,g       | ) −→ | N(0,E(m |     | (L ;β∗,g)m |     | (L ;β∗,g)⊤)). |     |     |     |
|     |     |     |            |          | DSL | i (cid:98)k |      |         | DSL | i          |     | DSL i         |     |     |     |
N
k=1i∈Lk
| Term (a). | We  | now consider |     | the term | (a),     | and | we need          | to show   | that |     |           |     |     |     |        |
| --------- | --- | ------------ | --- | -------- | -------- | --- | ---------------- | --------- | ---- | --- | --------- | --- | --- | --- | ------ |
|           |     |              |     |         |          |     |                  | −1       |      |    |           | −1 |     |     |        |
|           |     |              |     | 1 K      |          | ∂m  | (L ;β(cid:101),g | )         |      | ∂m  | (L ;β∗,g) |     |     |     |        |
|           |     |              |     | (cid:88) | (cid:88) | DSL | i                | (cid:98)k | p E  | DSL | i         |     |     |     |        |
|           |     |              |     |         |          |     |                  |          | −→   |    |           |    |     |     | (OA.9) |
|           |     |              |     | N        |          |     | ∂β               |           |      |     | ∂β        |     |     |     |        |
k=1i∈Lk
We require the standard regularity conditions that assume the smoothness of the derivative of the moment, which holds
| true for | the most | common | method | of  | moment | estimators |     | we consider |     | here. |     |     |     |     |     |
| -------- | -------- | ------ | ------ | --- | ------ | ---------- | --- | ----------- | --- | ----- | --- | --- | --- | --- | --- |
Assumption 5 from Chernozhukov et al. (2022). E(∂m (L ;β∗,g)/∂β) exists and there is a neighborhood N of
|     |     |     |     |     |     |     |     |     | DSL | i   |     |     |     |     | β   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
β∗ such that: (i) for each k, ||g −g|| =o (1); (ii) for all ||g−g|| small enough, m (L;β,g) is differentiable in β on
|     |     |     |     | (cid:98)k | 2   | p   |     |     | 2   |     |     | DSL |     |     |     |
| --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
N with probability approaching one, and there are C >0 and δ(D;g) such that, for β ∈N and ||g−g|| small enough,
| β   |     |                    |     |         |     |                          |     |                  |     |     |     | β   |     | 2   |     |
| --- | --- | ------------------ | --- | ------- | --- | ------------------------ | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     | (cid:12)(cid:12)   |     |         |     |                          |     | (cid:12)(cid:12) |     |     |     |     |     |     |     |
|     |     | (cid:12)(cid:12)∂m |     | (L;β,g) | ∂m  | (L;β∗,g)(cid:12)(cid:12) |     |                  |     |     |     |     |     |     |     |
(cid:12) (cid:12) DSL DSL (cid:12) (cid:12) ≤δ(L,g)||β−β∗||1/C; E(δ(L,g))<C.
|     |     | (cid:12) (cid:12) |     |     | −   |     |     | (cid:12) (cid:12) |     |     |     |     |     |     |     |
| --- | --- | ----------------- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     | (cid:12)(cid:12)  |     | ∂β  |     | ∂β  |     | (cid:12)(cid:12)  |     |     | 2   |     |     |     |     |
|     |     | (cid:12)(cid:12)  |     |     |     |     |     | (cid:12)(cid:12)  |     |     |     |     |     |     |     |
2
(iii) For each k and p and q, E(∂m (L;β∗,g ) /∂β −∂m (L;β∗,g) /∂β )=o (1).
|     |     |     |     | DSL |     | (cid:98)k | p q | DSL |     | p   | q   | p   |     |     |     |
| --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
These regularity conditions are standard (Newey and McFadden 1994). Among this regularity condition, the main
requirement is that, for each k, ||g −g|| = o (1). However, we define g to be the probability limit of g , and thus, this
|     |     |     |     | (cid:98)k | 2   | p   |     |     |     |     |     |     |     | (cid:98)k |     |
| --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- |
β(cid:98)−β∗
automatically holds. Therefore, under this assumption and =o p (1), we obtain equation (OA.9).
5

|     | Finally, | we combining |     | terms | (a) and | (b), | we have |     |     |     |     |     |     |     |
| --- | -------- | ------------ | --- | ----- | ------- | ---- | ------- | --- | --- | --- | --- | --- | --- | --- |
√
d
|     |     |     |     |     |     |     | N(β(cid:98)DSL | −β∗)−→ |     | N(0,V). |     |     |     | (OA.10) |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ------ | --- | ------- | --- | --- | --- | ------- |
where
|     |     |     |     |     |        | −1 |     |            |     |              |     |             | −1 |     |
| --- | --- | --- | ---- | --- | ------ | --- | --- | ---------- | --- | ------------ | --- | ------------ | --- | --- |
|     |     |     | ∂m   | (L  | ;β∗,g) |     |     |            |     |              |     | ∂m (L ;β∗,g) |     |     |
|     |     |     |      | DSL | i      |     |     |            |     |              |     | DSL i        |     |     |
|     |     | V   | =E  |     |        |    | E(m | (L ;β∗,g)m |     | (L ;β∗,g)⊤)E |     |             |  , |     |
|     |     |     |      | ∂β  |        |     | DSL | i          |     | DSL i        |     | ∂β           |     |     |
(cid:50)
| which | completes |     | the proof. |     |     |     |     |     |     |     |     |     |     |     |
| ----- | --------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
B.3 Examples
The general theoretical results developed in Appendix B.2 accommodate a wide range of regression problems. To derive a
new DSL estimator, researchers just need to derive a corresponding moment function (i.e., a subgradient of a given convex
| objective | function)       |             | for each    | estimator.  |       |            |            |          |          |               |             |     |     |     |
| --------- | --------------- | ----------- | ----------- | ----------- | ----- | ---------- | ---------- | -------- | -------- | ------------- | ----------- | --- | --- | --- |
|           | For linear      | regression, |             | the moment  |       | function   | is defined | as,      |          |               |             |     |     |     |
|           |                 |             |             |             |       | N          |            |          | N        |               |             |     |     |     |
|           |                 |             |             |             |       | 1 (cid:88) |            | 1        | (cid:88) |               |             |     |     |     |
|           |                 |             |             |             |       |            | m(D        | ;β):=    | (Y       | −X⊤β)X        | .           |     |     |     |
|           |                 |             |             |             |       | N          | i          | N        |          | i i           | i           |     |     |     |
|           |                 |             |             |             |       | i=1        |            |          | i=1      |               |             |     |     |     |
|           | For logistic    | regression, |             | the moment  |       | function   | is         |          |          |               |             |     |     |     |
|           |                 |             |             |             |       | N          |            |          | N        |               |             |     |     |     |
|           |                 |             |             |             |       | 1 (cid:88) |            | 1        | (cid:88) |               |             |     |     |     |
|           |                 |             |             |             |       |            | m(D ;β):=  |          | (Y       | −expit(X⊤β))X |             |     |     |     |
|           |                 |             |             |             |       |            | i          |          |          | i             | i           | i   |     |     |
|           |                 |             |             |             |       | N          |            | N        |          |               |             |     |     |     |
|           |                 |             |             |             |       | i=1        |            |          | i=1      |               |             |     |     |     |
| where     | expit(·)        | is          | the inverse | of the      | logit | function.  |            |          |          |               |             |     |     |     |
|           | For multinomial |             | logistic    | regression, |       | the moment |            | function | is       |               |             |     |     |     |
|           |                 |             |             |             |       |            |            |          | (cid:40) |               | (cid:41)J−1 |     |     |     |
|           |                 |             |             |             | 1     | N          |            |          | 1        | N             |             |     |     |     |
|           |                 |             |             |             |       | (cid:88)   | ;{β}J      |          | (cid:88) |               |             |     |     |     |
|           |                 |             |             |             |       | m(D        | i          | ):=      |          | (Y ik −ρ      | ik )X i     |     |     |     |
|           |                 |             |             |             | N     |            |            | k=1      | N        |               |             |     |     |     |
|           |                 |             |             |             |       | i=1        |            |          |          | i=1           |             |     |     |     |
k=1
| where | Y   | :=1{Y | =k}, |     |     |     |     |         |     |     |     |     |     |     |
| ----- | --- | ----- | ---- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
|       | ik  |       | i    |     |     |     |     |         |     |     |     |     |     |     |
|       |     |       |      |     |     |     |     | exp(X⊤β |     | )   |     |     |     |     |
i k
|     |     |     |     |     |     |     | ρ := |                    |     |     | ,   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | ------------------ | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     | ik   | (cid:80)J−1exp(X⊤β |     |     |     |     |     |     |
|     |     |     |     |     |     |     |      | 1+                 |     | k   | )   |     |     |     |
|     |     |     |     |     |     |     |      |                    | k=1 | i   |     |     |     |     |
and β =0.
J
|     | For Poisson | regression, |     | the moment |     | function   | is  |       |          |             |     |     |     |     |
| --- | ----------- | ----------- | --- | ---------- | --- | ---------- | --- | ----- | -------- | ----------- | --- | --- | --- | --- |
|     |             |             |     |            |     | N          |     |       | N        |             |     |     |     |     |
|     |             |             |     |            |     | 1 (cid:88) |     | 1     | (cid:88) |             |     |     |     |     |
|     |             |             |     |            |     |            | m(D | ;β):= | (Y       | −exp(X⊤β))X |     | .   |     |     |
|     |             |             |     |            |     |            | i   |       |          | i           | i   | i   |     |     |
|     |             |             |     |            |     | N          |     | N     |          |             |     |     |     |     |
|     |             |             |     |            |     | i=1        |     |       | i=1      |             |     |     |     |     |
TheDSLframeworkcanalsoaccommodateavarietyofobservationalcausalinferencemethods. Forthetwo-stageleast
squares estimator used in the instrumental variable design, the moment function is
|     |     |     |     |     | N        |       |     | N        |     |        |       |       |     |         |
| --- | --- | --- | --- | --- | -------- | ----- | --- | -------- | --- | ------ | ----- | ----- | --- | ------- |
|     |     |     |     | 1   | (cid:88) |       | 1   | (cid:88) |     |        |       |       |     |         |
|     |     |     |     |     | m(D      | ;β):= |     | (Y −β    | −β  | T −X⊤β | )(1,Z | ,X ), |     | (OA.11) |
|     |     |     |     |     |          | i     |     | i        | 0   | 1 i    | i 2:K | i i   |     |         |
|     |     |     |     | N   |          |       | N   |          |     |        |       |       |     |         |
|     |     |     |     |     | i=1      |       |     | i=1      |     |        |       |       |     |         |
where T is the treatment, Z is the instrument, and X is (K−1)-dimensional pre-treatment covariates.
|     | i   |     |     | i   |     |     |     | i   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Forthelocallinearregressionestimatorusedintheregressiondiscontinuitydesign,themomentfunctionforanestimator
| based | on observations |     | above | the | cutpoint | is  |     |     |     |     |     |     |     |     |
| ----- | --------------- | --- | ----- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
N
|     |     |     |     | 1 (cid:88) |     |       |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ---------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |            | m   | (D ;β | )   |     |     |     |     |     |     |     |
|     |     |     |     |            | 1   | i 1   |     |     |     |     |     |     |     |     |
N
i=1
6

N (cid:18) (cid:19)
:= 1 (cid:88) 1{c<X <c+h}K X i −c (Y −β −β (X −c))(1,X −c),
N i h i 10 11 i i
i=1
whereX istheforcing(running)variable,cisthecutpoint,histhebandwidth,andK(·)isauser-specifiedkernelfunction.
i
Similarly, the moment function for an estimator based on observations below the cutpoint is
N
1 (cid:88)
m (D ;β )
N 0 i 0
i=1
N (cid:18) (cid:19)
:= 1 (cid:88) 1{c−h<X <c}K X i −c (Y −β −β (X −c))(1,X −c).
N i h i 00 01 i i
i=1
The regression discontinuity design estimator is β(cid:98)10 −β(cid:98)00 .
For linear two-way fixed-effects regression used in the difference-in-differences design, the moment function is
 1 (cid:80)N (cid:80)T (Y −α −γ −X⊤β)X 
NT i=1 t=1 it i t it it
 
N 1 T (cid:88) N (cid:88) T m(D it ;β,α,γ):=     (cid:110) N 1 T (cid:80)T t=1 (Y it −α i −γ t −X i ⊤ t β)X it (cid:111)N i=1     ,
i=1 t=1  
(cid:110) (cid:111)T 
1 (cid:80)N (Y −α −γ −X⊤β)X
NT i=1 it i t it it
t=1
where {α }N is the individual-fixed-effect and {γ }T is the time-fixed-effect.
i i=1 t t=1
B.4 Power Analysis
Increasing the number of expert annotations is equivalent to increasing the sampling probability π for each document.
From the general results we derived in Appendix B.2, we know the asymptotic variance of the DSL estimator takes the
following form.
V = S E(m (D ,Q ,R ;β∗,π,g)m (D ,Q ,R ;β∗,π,g)⊤)S ,
V DSL i i i DSL i i i V
 −1
∂m (D ,Q ,R ;β∗,π,g)
DSL i i i
S V = E  ∂β 
Based on the definition of the DSL moment, we also have
 −1  −1
∂m (D ,Q ,R ;β∗,π,g) ∂m(D ;β∗)
DSL i i i i
E   = E   . (OA.12)
∂β ∂β
Therefore, the asymptotic variance of the DSL estimator can be re-written as follows.
 −1  −1
∂m(D;β∗) ∂m(D;β∗)
V =E  ∂β  E(m DSL (D i ,Q i ,R i ;β∗,π,g)m DSL (D i ,Q i ,R i ;β∗,π,g)⊤)E  ∂β  .
 −1
∂m(D;β∗)
Importantly, the “sandwich” part of the variance E   only depends on the original moment function and is
∂β
not dependent on the sampling probability π.
Therefore, increasing the number of expert annotations contributes only to the “meat” part of the variance. We can
further decompose the “meat” part of the variance as follows.
E(m (D ,Q ,R ;β∗,π,g)m (D ,Q ,R ;β∗,π,g)⊤)
DSL i i i DSL i i i
7

|     | (cid:18) |     |          |     |     |     |                  |     |     | (cid:19)  |
| --- | -------- | --- | -------- | --- | --- | --- | ---------------- | --- | --- | --------- |
|     |          | 1   | (cid:16) |     |     |     | (cid:17)(cid:16) |     |     | (cid:17)⊤ |
= E m(D ;β∗)−m(D obs,D(cid:98) mis;β∗) m(D ;β∗)−m(D obs,D(cid:98) mis;β∗)
|     |          |                  |                         | i        | i            | i   |                       | i         | i i |     |
| --- | -------- | ---------------- | ----------------------- | -------- | ------------ | --- | --------------------- | --------- | --- | --- |
|     | π(Dobs,Q |                  | )                       |          |              |     |                       |           |     |     |
|     |          | i                | i                       |          |              |     |                       |           |     |     |
|     |          | (cid:16)         |                         |          |              |     | (cid:17)              |           |     |     |
|     | + E      | m(Dobs,D(cid:98) | mis;β∗)m(Dobs,D(cid:98) |          | mis;β∗)⊤     |     |                       |           |     |     |
|     |          |                  | i i                     |          | i i          |     |                       |           |     |     |
|     |          | (cid:18)         |                         |          |              |     |                       | (cid:19)  |     |     |
|     |          |                  |                         | (cid:16) |              |     |                       | (cid:17)⊤ |     |     |
|     | + E      | m(D              | obs,D(cid:98) mis;β∗)   |          | m(D ;β∗)−m(D |     | obs,D(cid:98) mis;β∗) |           |     |     |
|     |          |                  | i i                     |          | i            |     | i i                   |           |     |     |
|     |          | (cid:18)(cid:16) |                         |          |              |     |                       | (cid:19)  |     |     |
(cid:17)
|     | + E | m(D | ;β∗)−m(D | obs,D(cid:98) | mis;β∗) | m(D | obs,D(cid:98) mis;β∗)⊤ |     |     |     |
| --- | --- | --- | -------- | ------------- | ------- | --- | ---------------------- | --- | --- | --- |
|     |     |     | i        | i             | i       |     | i i                    |     |     |     |
Fromthisdecomposition, wecanpredictthestandarderrorsunderdifferentsamplingprobabilitiesbyplugging-indifferent
samplingprobabilitiesintothefirstterm. Wecanconsistentlyestimatethisvarianceunderdifferentsamplingprobabilities.
| B.5 Examples | of  | Violations |     | of Assumptions |     |     |     |     |     |     |
| ------------ | --- | ---------- | --- | -------------- | --- | --- | --- | --- | --- | --- |
DSL covers the vast majority of social science research applications where researchers need to annotate a corpus of doc-
uments that are available in total before analyzing data. However, it is also important to understand specific examples
| where Assumption | 1 is violated. |     |     |     |     |     |     |     |     |     |
| ---------------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Importantly, Assumption 1 does rule out some applications, and two are worth noting: (1) Researchers use external
coding (rather than their own expert-coding) to measure text-based variables of interest, and it is unknown why only
a subset of documents were coded. For example, Hager and Hilbig (2020) analyze speech documents published by the
German government. For 47% of all documents, the topic of the speech is assigned by the German government, but the
rest of the documents are published without an explicit topic assignment. In this case, researchers do not decide which
document to be sampled for the expert-labeling, and thus, the assumption is violated. However, if researchers can create a
codebook,randomlysampledocumentswithoutanexplicittopicassignment,andthenlabelsuchdocuments,Assumption1
holds. With this additional sampling of expert coding, researchers can use DSL by redefining the sampling probability as
follows. For documents that were coded by the government, their sampling probability is 1, and for documents that were
not originally coded by the government, their sampling probability is n/N 0 where n is the number of expert-coding and
N is the number of documents that were not originally coded by the government.
0
(2) Another scenario occurs when researchers need to analyze documents in real-time as soon as they obtain text data,
e.g., making polling predictions based on social media posts on election day. In such cases, it might be inevitable to use
expert-coded documents from the past, but in this example, social media posts on election day have the probability of
being sampled for expert-coding is zero, and thus, the assumption is violated. However, if researchers have time to sample
a subset of social media posts on election day for expert-coding, Assumption 1 holds because now every document they
analyze has the probability of being labeled greater than zero. Therefore, when researchers need to collect documents
over time, researchers can guarantee Assumption 1 by making sure to sample documents for expert-coding from each time
| period they analyze. |             |         |            |     |        |     |     |     |     |     |
| -------------------- | ----------- | ------- | ---------- | --- | ------ | --- | --- | --- | --- | --- |
| B.6 Problem          | of Ignoring |         | Prediction |     | Errors |     |     |     |     |     |
| B.6.1 Example        | from        | Section | 3.3        |     |        |     |     |     |     |     |
We now further investigate the following expression introduced in Section 3.3.
E(e
|     |     |     |     |     | i   | |X i ) = | 0.  |     |     | (OA.13) |
| --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | ------- |
Eventhoughthisexpressionmightseemsimilartothestandardexogeneityassumption, itturnsoutthatthiscondition
implies much stronger assumptions (see a diagram in Figure OA-1). First, prediction errors cannot be affected by any
independent variable X included in downstream analyses. For example, in Fowler et al. (2021) where the original authors
included candidate-fixed effects and a platform on which a given political ad is run as X, this condition requires that
8

e
|     |     |     | (1) | (2) |     |     |
| --- | --- | --- | --- | --- | --- | --- |
X
X
|     |     |     | X   |     | Y   |     |
| --- | --- | --- | --- | --- | --- | --- |
X (3)
U
| Figure OA-1: | Conditions | Required | to Ignore | Prediction Errors. |     |     |
| ------------ | ---------- | -------- | --------- | ------------------ | --- | --- |
Note: Prediction errors e can be ignored only when e is uncorrelated with independent variables X. This implies that (1)
prediction errors e are not affected by independent variables X, (2) prediction errors e are not affected by the outcome
variable Y (to block the path X →Y →e), and (3) prediction errors e are not affected by unobserved confounders U (to
| block the | path X ←U | →e). |     |     |     |     |
| --------- | --------- | ---- | --- | --- | --- | --- |
prediction errors be the same across all candidates and platforms. This requirement might be the most natural one—
differential error rates across X lead to biased estimates of effects of X. Second, prediction errors cannot be affected
by the outcome of interest Y, either. For example, in Fowler et al. (2021) where Y is the tone of ads that has three
categories (Attack, Contrast, Promote), this condition requires that prediction errors be the same across all categories.
This condition is particularly unlikely to hold in most applications of text analyses in the social sciences because most
predictionapproaches(LLMsorsupervisedMLmethods)tendtohavehigherpredictionerrorsforrarecategories.1 Finally,
prediction errors cannot be affected by unobserved confounders U, either. This is the case even when researchers only
estimate coefficients β for descriptive analyses and do not make explicit causal claims. Unfortunately, it is not sufficient
to check relationships between prediction errors and the main variables in the downstream analyses (the outcome and the
independent variables). To ignore prediction errors, researchers also have to justify that prediction errors are unrelated
to any unmeasured confounder, which is extremely difficult in most applications given that researchers often have limited
| information | about unmeasured | confounders. |     |     |     |     |
| ----------- | ---------------- | ------------ | --- | --- | --- | --- |
Therefore, researchers can ignore prediction errors only when prediction errors are completely random, i.e., prediction
errors are not affected by the independent variable, the outcome variable, or any unobserved confounder. Unfortunately,
thisconditionisuntenableinalmostallsocialscienceapplications. WhilewefocusedononesettingwhereY istext-based,
similar stringent conditions are required when other types of variables (e.g., independent variables) are text-based.
| B.6.2 | General Bias | Formula |     |     |     |     |
| ----- | ------------ | ------- | --- | --- | --- | --- |
While we derived a condition required to ignore prediction errors above, we primarily focused on cases when Y is text-
i
based. Here, using the general framework developed in Appendix B, we consider general conditions that apply to any
convex optimization problem and cases where any subset of outcome and independent variables are text-based.
| In general, | to ignore | prediction errors, | researchers | need to assume |          |     |
| ----------- | --------- | ------------------ | ----------- | -------------- | -------- | --- |
|             |           |                    | (cid:16)    |                | (cid:17) |     |
E
|     |     |     | m(Dobs,D(cid:98) | mis;β)−m(Dobs,Dmis;β) | =0, | (OA.14) |
| --- | --- | --- | ---------------- | --------------------- | --- | ------- |
|     |     |     | i                | i i i                 |     |         |
which means that the moment function that plugs in predicted variables is unbiased. In a special case when outcome Y is
i
1.WefinddifferentialpredictionerrorsacrosscategoriesinLLMannotationsforFowleretal.(2021),whichwereportinAppendixG.
9

| text based, | this reduces | to the | bias | condition | derived | in  | the main paper. |     |
| ----------- | ------------ | ------ | ---- | --------- | ------- | --- | --------------- | --- |
(cid:16) (cid:17)
E
|             |               |       |                 |     | m(Dobs,D(cid:98) |                  | mis;β)−m(Dobs,Dmis;β) |          |
| ----------- | ------------- | ----- | --------------- | --- | ---------------- | ---------------- | --------------------- | -------- |
|             |               |       |                 |     |                  | i                | i                     | i i      |
|             |               |       |                 |     | (cid:16)         |                  |                       | (cid:17) |
|             |               |       |                 | =   | E m(Y(cid:98)i   | ,X ;β)−m(Y       | ,X                    | ;β)      |
|             |               |       |                 |     |                  | i                | i i                   |          |
|             |               |       |                 |     | (cid:16)         |                  |                       | (cid:17) |
|             |               |       |                 |     | E                |                  | ⊤β)−X                 | ⊤β)      |
|             |               |       |                 | =   | X                | i (Y(cid:98)i −X | i (Y i                | −X       |
|             |               |       |                 |     |                  |                  | i                     | i        |
|             |               |       |                 |     | (cid:16)         |                  | (cid:17)              |          |
|             |               |       |                 | =   | E X              | (Y(cid:98)i −Y   | )                     |          |
|             |               |       |                 |     |                  | i                | i                     |          |
| which is    | equal to zero | when  | E(Y(cid:98)i −Y | |X  | )=0.             |                  |                       |          |
|             |               |       |                 | i   | i                |                  |                       |          |
| C Practical |               | Guide |                 |     |                  |                  |                       |          |
In this section, we summarize our practical recommendations in each step of DSL.
| C.1 | Step 1: Predict |     | Text | Labels | with | LLMs |     |     |
| --- | --------------- | --- | ---- | ------ | ---- | ---- | --- | --- |
In the first step, researchers use LLMs to predict text labels for the entire population of documents. See our examples of
| prompts | in Section | 2 and Appendix |     | F.1. |     |     |     |     |
| ------- | ---------- | -------------- | --- | ---- | --- | --- | --- | --- |
| C.1.1   | Which LLMs | should         | we  | use? |     |     |     |     |
Researchers can often start with zero-shot learning (i.e., no exemplar) using the state-of-the-art LLM. We also recommend
implementing at least one open-source LLM like Llama-2. Researchers can also consider few-shot learning (i.e., adding
exemplars). Note that specifics of LLM implementations are likely to evolve quickly over time given the speed of the LLM
development.
More importantly, researchers do not need to choose one specific LLM in the proposed DSL framework. If researchers
havemultiplehigh-performingLLMannotations, theycanincorporatealloftheminDSLestimators. ThisisbecauseDSL
only uses LLM annotations as predictors for expert-coded labels, and we do not make any assumptions about errors in
LLM annotations.
| C.1.2 | What if LLM | annotations |     | are | Very | Good? |     |     |
| ----- | ----------- | ----------- | --- | --- | ---- | ----- | --- | --- |
If LLM annotations have extremely high predictive performance, DSL is going to have small standard errors because
bias-correction terms are small (the second part of equation (4) is close to zero), while maintaining statistical validity.
However, as long as LLM annotations are not perfect, even if they have excellent performance, the LLM-only estimation is
not statistically valid (as seen in our applications and simulations). So, DSL is preferred to the LLM-only estimation even
| when LLM | annotations | have        | high | predictive | performance.2 |      |     |     |
| -------- | ----------- | ----------- | ---- | ---------- | ------------- | ---- | --- | --- |
| C.1.3    | What if LLM | annotations |      | are        | Very          | Bad? |     |     |
If LLM annotations have extremely low predictive performance, DSL is going to have large standard errors because bias-
correctiontermsarelarge,eventhoughitwillstillmaintainstatisticalvalidity. Inthiscase,itisrecommendedtoretrainthe
automated text annotation step (e.g., using different LLMs or training the classical supervised machine learning method),
which is the same advice as in the classical supervised learning literature. Using low-quality LLM annotations will not
invalidate the statistical properties of DSL, but having higher performing automated text annotation will reduce standard
| errors and | the required | number | of  | expert | annotations. |     |     |     |
| ---------- | ------------ | ------ | --- | ------ | ------------ | --- | --- | --- |
2.InahypotheticalscenariowhenLLMannotationshavenoerroratall,DSLisgoingtobethesameastheLLM-onlyestimation.
10

C.1.4 Should we spend time on improving LLMs or increasing the number of expert annotations if we
want to reduce standard errors?
In general, we recommend researchers should spend time on increasing the number of expert annotations as long as the
predictive performance of the underlying automated text annotation method is reasonably high (around 80 ∼ 90%, as in
our examples in Section 2). When the predictive performance becomes moderately high, it is often difficult to further
improve the predictive accuracy or F1 scores by more than 5 percentage points. Standard errors of DSL do not often
reduce much even if the predictive accuracy of the underlying text annotation methods improves by 1 or 2 percentage
points. In contrast, increasing the number of expert annotations is theoretically guaranteed to reduce standard errors of
the downstream analyses. Researchers can also use a power analysis to explicitly predict how much standard errors will
decrease by adding a certain number of expert annotations (see Section 5.1.3).
C.2 Step 2: Sample Documents for Expert Annotation
In the second step, we sample a subset of documents for expert annotations. See Section 6 of the main texts for recom-
mendations about how to handle errors and uncertainties in expert annotations.
C.2.1 Construct Validity and Prediction Errors
Inthispaper,wedevelopedamethodtoaccountforpredictionerrors,whichisthediscrepancybetweenexpertannotations
and automated text annotations. An equally important problem is the construct validity, which is a question about a
mapping between a theoretical concept of interest and expert annotations. The proposed method can only account for
prediction errors, and this does not replace careful, theoretical considerations about how operationalization in a user-
specified codebook relates to the main theoretical concept. Rather, our method augments theoretical thinking about the
construct validity by allowing researchers to focus on expert annotations and removing any additional error from the use
of automated text annotation.
C.2.2 How to Sample Documents for Expert Annotations
DSLcanallowforanysamplingmethodforexpertannotationsaslongasitiscontrolledbyresearchers,includingthemost
common random sampling and any sampling method that depends on document-level observed covariates. In practice,
researchers can often start with random sampling with equal probabilities. If researchers wish to over-sample documents
that are difficult to annotate, one possible approach is to increase the sampling probability for documents that LLMs are
more uncertain about (e.g., Li et al. 2023). Active learning is also a promising area of research to improve text sampling
in the classical supervised learning settings (Bosley et al. 2022).
C.2.3 Active Learning
Active learning is a technique to adaptively choose documents for expert-coding. This technique is important when
researchers use the classical supervised learning method (Bosley et al. 2022). However, the use of active learning for
valid statistical inference is known to be challenging. The existing approaches assume away any prediction errors and
uncertaintiesinthefirststepofthesupervisedlearningstepandalsoignorethefactthatexpert-codeddataareadaptively
collected, which also makes the standard statistical inference invalid. Fortunately, when researchers use pre-trained LLMs
(e.g., GPTs) as the automated text annotation methods, researchers can easily apply the idea of active learning within
the DSL framework. We follow the idea developed in Li et al. (2023). In particular, researchers can first use multiple pre-
trainedLLMs—theycancomefromdifferentLLMsmodelsordifferentpromptswiththesamemodel—andthenobtainthe
inter-LLM agreement for each document. This agreement score captures the difficulty of labeling a particular document.
Researcherscanusethisagreementscoretochangethesamplingprobabilityforexpertcoding. Fordocumentswhoselabel
multiple LLMs disagree on, we can increase its probability, and for documents whose label multiple LLMs agree on, we
11

can decrease its probability. The key is that many of the current successful LLMs are pre-trained and we do not need to
fit them to the data. Therefore, this LLM agreement score can be analyzed simply as one of the observed document-level
variable. Therefore, without any additional complex statistical theory, researchers can systematically change the sampling
probability for expert coding based the LLM agreement score.
C.3 Wide Applicability
While we so far focused on regression analyses in text-as-data applications, which are the most common downstream
analyses, the DSL framework can be used for a broader range of statistical analyses in the social sciences. Our general
framework is applicable to any application where researchers use predictive methods to scale up measurements.
C.3.1 Estimation of Category Proportions over Time or across Groups
Manyscholarsareinterestedinestimatingtheproportionofalldocumentsineachuser-specifiedcategory(e.g.,Hopkinsand
King 2010; Keith and O’Connor 2018). For example, we might study how the proportion of censored documents changes
over time or how the proportion of social media posts containing hate speech differs across groups, such as Democrats and
Republicans.
ThesequestionscanbeanalyzedwithintheDSLframework,too. Specifically,researcherscanregressatextcategoryon
timeorgroups. Forexample,usingwhetheradocumentiscensoredastheoutcomeandtimeindicatorsastheindependent
variable in the DSL linear regression, researchers can estimate how the proportion of censored documents changes over
time. When users include time-fixed effects, this estimation method is non-parametric and is equivalent to estimating the
proportion of censored documents in each time period separately.
C.3.2 Causal Inference with Texts
Anincreasingnumberofscholarsmakecausalinferencewithtextualdata(FongandGrimmer2021;Egamietal.2022;Mozer
andMiratrix2023). DSLcanbeusedincausalinferenceapplicationswheretheoutcome,treatment,orconfoundersaretext-
based. Inrandomizedexperiments,researcherscanusetheDSLregressiontoperformthedifference-in-meansorcovariate-
adjustedlinearregressionforestimatingtheaveragetreatmenteffect.3 Inobservationalstudies,undercorrespondingcausal
identification assumptions, researchers can apply the DSL two-stage-least squares for the instrumental variable design, the
DSL local linear regression for the regression discontinuity design, and the DSL two-way fixed effects estimator for the
difference-in-differences design.
C.3.3 Statistical Analyses of Unstructured Data, e.g., Images, Audios, Videos
Social scientists have begun to utilize a wider range of new data sources, such as image, audio, and video (e.g., Knox and
Lucas 2021; Torres and Cantu´ 2022). Like the text-as-data literature, researchers often use medium-specific automated
annotation methods (e.g., convolutional neural networks, and recent foundation models) before analyzing such annotated
data in the main downstream statistical analyses. However, as in the automated text annotation, they inevitably contain
non-random prediction errors. DSL can be used directly to handle such prediction errors in image, audio, and video
annotation tasks as well.
D Errors and Uncertainties in Expert Annotations
As we emphasized in the main paper, concerns of errors in expert annotations are far from new, and they equally apply
to almost all existing text-as-data methods, including any supervised machine learning methods and any unsupervised
3.Previousstudies(e.g.,FongandGrimmer2021;Egamietal.2022)haveclarifiedthechallengesofinferringacodebookandcausalestimates
fromthesamedata,especiallywhenusingunsupervisedlearningapproaches. Incontrast,thispaperreliesonasupervisedlearningframework
whereacodebookisgivenbyresearchersratherthanestimatedbyamodel.
12

|     |     |     | Bias | Coverage of 95% Confidence Intervals |     |     |     |
| --- | --- | --- | ---- | ------------------------------------ | --- | --- | --- |
1.00
0.2 Quasi−Bayes
|     |     | Naive |     | 0.75 |     |     |     |
| --- | --- | ----- | --- | ---- | --- | --- | --- |
egarevoC
saiB
|     |     | 0.0 |     | 0.50 |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- |
0.25
−0.2
0.00
|     |     | 500 600                      | 700 800 900 1000 | 500 | 600 700                      | 800 900 1000 |     |
| --- | --- | ---------------------------- | ---------------- | --- | ---------------------------- | ------------ | --- |
|     |     | Number of Expert Annotations |                  |     | Number of Expert Annotations |              |     |
Figure OA-2: Bias and Coverage of the DSL estimator with and without the quasi-Bayesian approach.
learning methods that are validated by expert reading of documents (Grimmer and Stewart 2013). The DSL estimator
is not more sensitive to errors in expert annotations than other methods. Importantly, the problem of prediction errors,
which we focus on in this paper, is independent of the problem of errors in expert annotations. Thus, researchers can
combine any method to deal with errors in expert annotations with the DSL estimator.
In this paper, we take a quasi-Bayesian approach, similar to a multiple imputation algorithm for missing data. To
concretely introduce the method, suppose outcome Y requires text annotation, but the same approach works for any
text-based variable. There are K expert coders for each document, and we use {Y1,Y2,...,YK} to denote the expert
|     |     |     |     |     |     | i i i |     |
| --- | --- | --- | --- | --- | --- | ----- | --- |
annotation for document i from each expert coder. The quasi-Bayesian approach takes the following steps.
•
| Step | 1: We repeat | Step 2 and Step | 3 for B times. |     |     |     |     |
| ---- | ------------ | --------------- | -------------- | --- | --- | --- | --- |
• Step 2: For iteration b ∈ {1,...,B}, randomly sample one expert annotation among K annotations within each
labeled document. For each document i, randomly sample one from {Y1,Y2,...,YK} and deonte it by Y .
|     |     |     |     |     | i i | i   | ib  |
| --- | --- | --- | --- | --- | --- | --- | --- |
•
Step 3: Estimate DSL with a sampled set of expert annotations Y for all i with R =1. Draw quantities of interest
|     |     |     |     | ib  |     | i   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
Q times from the estimated asymptotic normal distribution and denote them as {β(cid:98)bq }Q .
q=1
• Step 4: Combine draws of quantities of interest and obtain {{β(cid:98)bq }Q }B . Researchers can then use its average as
|     |     |     |     |     | q=1 b=1 |     |     |
| --- | --- | --- | --- | --- | ------- | --- | --- |
the point estimate and its 2.5 and 97.5 percentiles to form the confidence interval.
Importantly,theproceduredescribedaboveassumesauniformprioraboutcoders’qualitiesandincorporatesinformation
from every expert coder with equal weights. If users have prior knowledge about which coder is more credible than others,
they can incorporate this prior into the quasi-Baysian procedure by increasing the probability of sampling a label from
more credible coders in Step 2. Formally, this procedure provides consistency and valid confidence intervals around the
target parameters that we would obtain if all the documents were coded by the same set of multiple expert coders and we
| estimated | the target parameters | using | the same quasi-Bayesian | approach. |     |     |     |
| --------- | --------------------- | ----- | ----------------------- | --------- | --- | --- | --- |
To illustrate how the method works in practice, we apply the proposed method to our empirical application based
on Pan and Chen (2018). The original authors had already disambiguated disagreements between expert coders, so we
simulated three expert coders based on their original expert annotations. We started with annotations from one coder and
then generated two other coders that agreed with the first coder with 80% and disagreed with 20%. We then explicitly
take into account the disagreement between the three coders. The target parameters are defined as the coefficients of the
13

logisticregressioninPanandChen(2018)thatwewouldobtainifallthedocumentswerecodedbythethreeexpertcoders
| and | we averaged | over | estimates | using | the quasi-Bayesian |     |     | approach. |     |     |     |     |     |
| --- | ----------- | ---- | --------- | ----- | ------------------ | --- | --- | --------- | --- | --- | --- | --- | --- |
Figure OA-2 shows the bias and the coverage of 95% confidence intervals for the DSL estimators that account for
the disagreement with the quasi-Bayesian approach (“Quasi-Bayes”; blue squares) and the estimators that ignore the
disagreementandjustuseannotationsfromthefirstcoder(“Naive”; redcircles). First,itisclearthatestimatesarebiased
and confidence intervals are invalid when uncertainties in expert annotations are ignored. Second, the figure also shows
that the proposed quasi-Bayesian approach is consistent and provides valid confidence intervals for the target parameters.
| E   | Simulation |     | Studies |     |     |     |     |     |     |     |     |     |     |
| --- | ---------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Here we offer the details of the simulation study we reported in Section 3.4. The main purpose of this simulation is to
clearly show that ignoring prediction errors can bias downstream estimates and standard errors. We also use empirical
applications in Section 5 to show the problem of ignoring prediction errors and how DSL solves the issue under realistic
| real-world | social | science | data | settings. |     |     |     |     |     |     |     |     |     |
| ---------- | ------ | ------- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
As the entire population, we generate n=5000 i.i.d. observations (i∈{1,...,5000}) as follows.
|     |     |     |     | →−  |     |     |     |     | →−  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
• Covariates: X ∼N(0,ΣX) where X =(X ,...,X ), and 0 is a vector of 0 with length 10. For ℓ∈{1,...,10},
|     |     |     | i   |     |     | i   | i1  | i10 |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ΣX =1 and for ℓ̸=ℓ′, ΣX =0.3. For the second covariate, we update it by binarizing X =1{X >qnorm(0.8)}.
|     | ℓℓ       |          |     | ℓℓ′                |     |     |       |     |     |     | i2 i2 |     |     |
| --- | -------- | -------- | --- | ------------------ | --- | --- | ----- | --- | --- | --- | ----- | --- | --- |
|     | • Binary | Outcome: | Y   | ∼Bernoulli(expit(W |     | ))  | where |     |     |     |       |     |     |
|     |          |          | i   |                    |     | i   |       |     |     |     |       |     |     |
|     |          |          |     |                    | 0.1 |     | 1.3X  |     |     |     |       |     |     |
i4
|     |     | W   | i =        |     |       | +   |             |     | +1.5X | i4 X i6 +0.5X i1 | X i2 +1.3X i1 | +X i2 |     |
| --- | --- | --- | ---------- | --- | ----- | --- | ----------- | --- | ----- | ---------------- | ------------- | ----- | --- |
|     |     |     | 1+exp(0.5X |     | −0.5X | )   | 1+exp(−0.1X |     | )     |                  |               |       |     |
|     |     |     |            |     | i3    | i2  |             |     | i2    |                  |               |       |     |
This data-generating process is similar to the one in Vansteelandt and Dukes (2022). It contains various nonlinear
transformation of X and it is difficult to correctly model the outcome function.
• Prediction by the automated text annotation method: Y(cid:98)i =P Y +(1−P )(1−Y ) where P ∼Bernoulli(P ) and P
|     |     |     |     |     |     |     |     |     | i i | i i | i   | q   | q   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
controls the accuracy of the prediction. When P =0.9, Y(cid:98)i =Y with 90% and Y(cid:98)i =1−Y with 10%. We vary P in
|     |                 |     |     |     |     |     | q   |     | i   |     | i   |     | q   |
| --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | our simulation. |     |     |     |     |     |     |     |     |     |     |     |     |
Toevaluatethegeneralstatisticalbehavior,herewedonotuseaspecificautomatedtextannotationmethod. Rather,
by directly controlling the amount of prediction errors, we can understand how prediction errors, in general, affect
downstream analyses. We used a very simple flipping error as used in Clayton et al. (2023). The realistic prediction
errors, as we examine in our empirical applications in Section 5, are more likely to be complex. The main idea here
is to show that bias from prediction errors is substantial even for these simple prediction errors.
• ExpertAnnotation: Weusesimplerandomsamplingof500documentsforexpertannotation. Thus,Pr(R =1)=0.1
i
|     | for every | observation. |     |     |     |     |     |     |     |     |     |     |     |
| --- | --------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
,X2,X
Our estimand of interest is the coefficients of the oracle logistic regression where we regress Y on (X ,X ). We
|     |     |     |     |     |     |     |     |     |     |     | i i1 | i1 i2 | i4  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ----- | --- |
evaluated bias, coverage, RMSE of the estimator ignoring prediction errors and DSL in Figure 1.
We found that estimators ignoring prediction errors have large biases and invalid confidence intervals, which makes it
unsuitable for social science downstream analyses. DSL has low bias and proper coverage of confidence intervals regardless
| of the | accuracy | of  | the underlying |     | automated | text | annotation | method. |     |     |     |     |     |
| ------ | -------- | --- | -------------- | --- | --------- | ---- | ---------- | ------- | --- | --- | --- | --- | --- |
14

| F   | Introduction |      | to  | LLMs   |         |              |     |     |
| --- | ------------ | ---- | --- | ------ | ------- | ------------ | --- | --- |
| F.1 | Prompts      | Used | in  | Social | Science | Applications |     |     |
F.1.1 Examples
In this section, to show the wide applicability of LLM annotations, we provide examples of prompts used in a range of
social science applications. As we see below, there are huge variations in how scholars provide prompts just like there are
variations in how we write codebooks and train human-coders. Given the space constraints, we provide three examples
| here, | and researchers | can            | see           | other      | examples  | in Ziems    | et al. (2024). |       |
| ----- | --------------- | -------------- | ------------- | ---------- | --------- | ----------- | -------------- | ----- |
|       | • Sentiment     | Classification |               | (Ornstein, |           | Blasingame, | and Truscott   | 2022) |
|       | ⋆ Goal:         | Classify       | the sentiment |            | of social | media posts |                |       |
⋆ Prompt:
|     | Decide whether | a Tweet’s | sentiment | is  | positive, | neutral, or | negative. |     |
| --- | -------------- | --------- | --------- | --- | --------- | ----------- | --------- | --- |
Tweet: Congratulations to the SCOTUS. American confidence in the Supreme Court is now lower than at any time in history. Well done!
Sentiment:
|     | • Ideological | Scaling  | Task         | (Ornstein, |                | Blasingame, | and Truscott | 2022) |
| --- | ------------- | -------- | ------------ | ---------- | -------------- | ----------- | ------------ | ----- |
|     | ⋆ Goal:       | Classify | the ideology |            | of a political | manifesto   |              |       |
⋆ Prompt:
Decide whether this sentence from a British political manifesto is Liberal, Conservative, or Neither.
Sentence: We will implement a comprehensive strategy for ending low pay, notably by the introduction of a statutory national minimum wage.
Classification:
|     | • Attitudes | toward   | Immigrants |        | (Mets      | et al. 2023) |     |     |
| --- | ----------- | -------- | ---------- | ------ | ---------- | ------------ | --- | --- |
|     | ⋆ Goal:     | Classify | attitudes  | toward | immigrants |              |     |     |
⋆ Prompt:
Tag the following numbered sentences as being either "supportive", "against" or "neutral" towards the topic of immigration. "Supportive"
means: "supports immigration, friendly to foreigners, wants to help refugees and asylum seekers". "Against" means: "against immigration,
dislikes foreigners, dislikes refugees and asylum seekers, dislikes people who help immigrants". "Neutral" means: "neutral stance, neutral
facts about immigration, neutral reporting about foreigners, refugees, asylum seekers". Don’t explain, output only sentence number and stance
tag.
1. Unfortunately, by now the violence has seeped from immigrant communities to all of the society.
|     | 2. [truncated] |            |             |     |     |                     |     |          |
| --- | -------------- | ---------- | ----------- | --- | --- | ------------------- | --- | -------- |
|     | 3. [truncated] |            |             |     |     |                     |     |          |
|     | F.1.2          | Prediction | Performance |     | in  | Other Applications: |     | Figure 3 |
Tofurtherillustratethewidevariationinpredictionperformance,wealsoanalyzeadiversesetofempiricalvalidation
studies. In particular, based on a review paper by Ollion et al. (2023), we collected eight recent papers that examine
theperformanceofLLMannotationsinthesocialsciencesandreporttheF-1scores(orpubliclysharedatasothatwe
could compute the F-1 scores). Eight papers are as follows: Heseltine and Clemm Von Hohenberg (2023), Kuzman,
Ljubeˇsi´c, andMozetiˇc(2023), Mellonetal.(2022), Metsetal.(2023), Mølleretal.(2023), Rathjeetal.(2023), Yang
15

and Menczer (2023), and Ziems et al. (2024). In each paper, they evaluate multiple different tasks, so we have 113
tasks in total. We want to emphasize that this set of tasks is not representative of text annotation tasks that social
scientists might perform. The results are probably the over-estimation of the current LLM performance given that
these papers are trying to show the promise of LLM annotations. At the same time, the LLM performance is also
likely to go up quickly as we have better and larger LLMs over time. This descriptive analysis is only meant to show
| the promise | but also        | the risk    | of using LLMs. |       |           |               |
| ----------- | --------------- | ----------- | -------------- | ----- | --------- | ------------- |
| G Empirical |                 | Application |                | based | on Fowler | et al. (2021) |
| G.1         | LLM Annotations |             |                |       |           |               |
| G.1.1       | Specification   | of LLM      | Annotations    |       |           |               |
Models. WeusethreeLLMsforourempiricalapplicationbasedonFowleretal.(2021): GPT-3.5(gpt-3.5-turbo-0613),
GPT-4 (gpt-4-preview-1106) and Llama-2-70B-chat. This choice is informed primarily by leaderboard performance
and popularity in the scientific community. In general, we recommend using a state-of-the-art LLM (currently,
| GPT-4) | and one state-of-the-art |     | open-source | LLM (currently, | Llama-2). |     |
| ------ | ------------------------ | --- | ----------- | --------------- | --------- | --- |
Prompt. LLMscanbeusedtoobtainpredictedlabelsfortextsbyincludingthetexttobelabeledinthecondition
and then autoregressively generating the predicted label. In general, users should include (a) a codebook, (b) texts
| to be labeld, | and (c) | an answer | box as | prompts. |     |     |
| ------------- | ------- | --------- | ------ | -------- | --- | --- |
In our empirical application based on Fowler et al. (2021), we follow the wording in the WMP codebook instructions
| used in | the original | paper. |     |     |     |     |
| ------- | ------------ | ------ | --- | --- | --- | --- |
In your judgment, is the primary purpose of the ad text to promote a specific candidate, attack a candidate, or contrast the candidates? Answer either
| "contrast", | "promote", | or "attack". |     |     |     |     |
| ----------- | ---------- | ------------ | --- | --- | --- | --- |
text: """
{text}
”””
Answer:
Here, {text} denotes a text to be labeled (i.e., a text of a political advertisement). The combined prompt-plus-text
is then given as an input to a LLM, which generates text using the autoregressive process.
| G.1.2 | Additional | LLM | Results |     |     |     |
| ----- | ---------- | --- | ------- | --- | --- | --- |
In Section 2.1.2, we reported the F1 scores for the overall performance of LLM annotations. Here, we provide
| additional | details. |     |     |     |     |     |
| ---------- | -------- | --- | --- | --- | --- | --- |
The left panel of Figure OA-3 shows the overall and disaggregated performance. Several points are worth noting.
First, the performance can vary across models and prompts. Second, the prediction accuracy is not uniform across
three categories. For all models, it is easiest to predict “Promote” and hardest to predict “Contrast”. This directly
means that prediction errors are affected by the outcome of interest (i.e., the tone of ads) itself, which implies that
| researchers | cannot | ignore prediction | errors | (see Section | 3.3). |     |
| ----------- | ------ | ----------------- | ------ | ------------ | ----- | --- |
In the main paper, we reported F1 score, which is the most common measure of prediction performance in the
computer science and machine learning literature, instead of the classification accuracy. It is important to remember
thattheclassificationaccuracycanbehighjustbecausethecategoryisrare. Forexample,whenthecategorytakes1
16

only with 5%, by predicting 0 for every observation, we can get 95% accuracy automatically. This is the main reason
whyF1scoresaregenerallyrecommendedasameasureofpredictionperformancewhenclassesareimbalanced. Given
thiscaveat,forsomeresearcherswhomightbemorefamiliarwithaccuracy,wealsoreporttheclassificationaccuracy
| for | LLM | predictions | in  | the right panel | of Figure | OA-3. |     |     |     |     |     |     |     |
| --- | --- | ----------- | --- | --------------- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- |
Tone of Political Ads: F1 score Tone of Political Ads: Accuracy
|      |      | GPT 4 | GPT 3.5 |      | Llama 2 |         |      | GPT 3.5   | GPT 4 |      | Llama 2 |      |         |
| ---- | ---- | ----- | ------- | ---- | ------- | ------- | ---- | --------- | ----- | ---- | ------- | ---- | ------- |
| 1.00 |      |       |         |      |         |         | 1.00 |           |       |      |         |      |         |
|      |      |       |         |      |         |         |      | 0.86 0.86 |       | 0.89 |         |      |         |
|      |      | 0.8   |         |      |         |         |      |           | 0.84  |      |         | 0.82 |         |
|      | 0.74 |       | 0.76    | 0.76 | 0.78    |         |      |           |       |      |         |      |         |
| 0.75 |      |       |         |      |         |         | 0.75 |           |       |      |         |      |         |
|      |      |       |         |      |         | Average |      |           |       |      | 0.55    |      | Average |
0.48
| 0.50 |     |     |     |     |     |     | 0.50 |     |      |      |      |      |     |
| ---- | --- | --- | --- | --- | --- | --- | ---- | --- | ---- | ---- | ---- | ---- | --- |
| 0.25 |     |     |     |     |     |     | 0.25 |     |      |      |      |      |     |
| 0.00 |     |     |     |     |     |     | 0.00 |     |      |      |      |      |     |
| 1.00 |     |     |     |     |     |     | 1.00 |     |      |      |      |      |     |
|      |     |     |     |     |     |     |      |     | 0.88 | 0.89 | 0.89 | 0.91 |     |
0.85 0.86
| 0.75 |      |      |      |      |      |             | 0.75 |     |     |     |     |     |             |
| ---- | ---- | ---- | ---- | ---- | ---- | ----------- | ---- | --- | --- | --- | --- | --- | ----------- |
|      |      |      |      |      |      | Attack (7%) |      |     |     |     |     |     | Attack (7%) |
|      |      | 0.55 |      |      | 0.56 |             |      |     |     |     |     |     |             |
|      | 0.53 |      |      | 0.49 |      |             |      |     |     |     |     |     |             |
| 0.50 |      |      | 0.47 |      |      |             | 0.50 |     |     |     |     |     |             |
0.41
| 0.25     |     |     |     |     |     |                | 0.25     |           |      |      |     |      |                |
| -------- | --- | --- | --- | --- | --- | -------------- | -------- | --------- | ---- | ---- | --- | ---- | -------------- |
| erocs 1F |     |     |     |     |     |                | ycaruccA |           |      |      |     |      |                |
| 0.00     |     |     |     |     |     |                | 0.00     |           |      |      |     |      |                |
| 1.00     |     |     |     |     |     |                | 1.00     |           |      |      |     |      |                |
|          |     |     |     |     |     |                |          | 0.83 0.84 | 0.83 | 0.85 |     | 0.86 |                |
| 0.75     |     |     |     |     |     | Contrast (17%) | 0.75     |           |      |      |     |      | Contrast (17%) |
0.65
0.51
| 0.50 |     |      |      |      |      |     | 0.50 |     |     |     |     |     |     |
| ---- | --- | ---- | ---- | ---- | ---- | --- | ---- | --- | --- | --- | --- | --- | --- |
|      |     | 0.34 |      |      | 0.33 |     |      |     |     |     |     |     |     |
| 0.25 |     |      | 0.23 | 0.22 |      |     | 0.25 |     |     |     |     |     |     |
0.16
| 0.00 |      |      |      |      |      |               | 0.00 |           |      |     |     |      |               |
| ---- | ---- | ---- | ---- | ---- | ---- | ------------- | ---- | --------- | ---- | --- | --- | ---- | ------------- |
| 1.00 |      | 0.93 | 0.91 | 0.91 |      |               | 1.00 |           |      |     |     |      |               |
|      | 0.89 |      |      |      | 0.86 |               |      | 0.87 0.87 |      | 0.9 |     |      |               |
|      |      |      |      |      |      |               |      |           | 0.84 |     |     | 0.81 |               |
|      |      |      |      |      |      | Promote (76%) |      |           |      |     |     |      | Promote (76%) |
| 0.75 |      |      |      |      |      |               | 0.75 |           |      |     |     |      |               |
0.52
0.5
| 0.50 |     |     |     |     |     |     | 0.50 |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
| 0.25 |     |     |     |     |     |     | 0.25 |     |     |     |     |     |     |
| 0.00 |     |     |     |     |     |     | 0.00 |     |     |     |     |     |     |
Zero−shotFew−shot Zero−shotFew−shot Zero−shotFew−shot Zero−shotFew−shot Zero−shotFew−shot Zero−shotFew−shot
Figure OA-3: F1 scores and Accuracy of LLM annotations: Fowler et al. (2021).
Note: “Average” shows the overall performance which is the weighted average for three categories: “Attack”, “Contrast”,
| and “Promote” |     | constitute | 7%, | 17%, and | 76% of political |        | ads.   |        |     |     |     |     |     |
| ------------- | --- | ---------- | --- | -------- | ---------------- | ------ | ------ | ------ | --- | --- | --- | --- | --- |
| G.2           |     | Additional | DSL | Results  | for              | Fowler | et al. | (2021) |     |     |     |     |     |
In the main paper, we reported the results for two outcomes, “Contrast” and “Promote”. In this appendix, we
also report the results for the third outcome “Attack.” The main findings are similar. First, estimates from the
LLM-only estimation are biased, and substantive and statistical conclusions can flip depending on which LLMs users
choose. Confidence intervals are also, in general, invalid. For this outcome, the LLM-only estimation with Llama-2
has reasonable coverages, but this is a statistical coincidence without any theoretical guarantee. Indeed, if we look
back at two other outcomes, the same estimator has poor coverage. Second, estimates from the classical supervised
learningmethodaresimilarlybiasedbecausetheyignorepredictionerrors,andtheyhaveinvalidconfidenceintervals.
In contrast to these existing approaches, DSL has unbiased estimates and valid confidence intervals.
17

Estimates and Standard Errors (Outcome = Attack)
|     |     | Benchmark | Classical Supervised ML |     |     |     | LLM−only Estimation |     |     |     |     | DSL |
| --- | --- | --------- | ----------------------- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- |
0.00
−0.05
eziS tceffE
−0.10
−0.15
−0.20
−0.25
|     |     |     | Dropout Logit | Lasso | g e Forest | s t      | o t o t  | o t o t     | o t     | ot o t   | o t         | o t o t o t Shot |
| --- | --- | --- | ------------- | ----- | ---------- | -------- | -------- | ----------- | ------- | -------- | ----------- | ---------------- |
|     |     |     |               |       | d          | o o      | S h S h  | S h S h     | S h S   | h S h    | S h S h     | S h S h          |
|     |     |     |               | R i   |            | B −      | −        | − −         | − −     | −        | − −         | − − w−           |
|     |     |     |               |       | m  X       | G r o    | e w r o  | e w r       | o e w   | r o e w  | r o         | e w r o e        |
|     |     |     |               |       | d o        | Z e      |   F Z e  |   F Z e     |   F     | Z e   F  | Z e   F     | Z e   F          |
|     |     |     |               |       | n          |  :   4   | :   :    | 5   :   :   | 2  : 4  | :  4   : |   :   5   : |   :   2  :       |
|     |     |     |               | R a   |            | − 4 T −  | 3 . 5 3. | − 2 a       | − −     | T − 3 .  | 5 3.        | − 2 a −          |
|     |     |     |               |       |            | P T P    | − T −    | m a m       | P T     | P −      | T − m a     | m                |
|     |     |     |               |       | G          | G P      | T P      | a Ll a      | G       | G P T    | P a         | Ll a             |
|     |     |     |               |       |            | G        | G Ll     |             |         | G        | G Ll        |                  |
Underlying Automated−Text−Annotation Methods
Coverage of 95% Confidence Intervals (Outcome = Attack)
|     |     | Classical Supervised ML |     |     |     | LLM−only Estimation |     |     |     |     | DSL |     |
| --- | --- | ----------------------- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- |
1.00
tnecreP egarevoC 0.75
0.50
0.25
0.00
Dropout Logit Lasso g e Forest s t o t ot o t ot o t o t o t ot o t ot o t Shot
|     |     |     | d   | o   | o S h    | S h      | S h S h      | S h     | S h     | S h S h     | S h      | S h S h     |
| --- | --- | --- | --- | --- | -------- | -------- | ------------ | ------- | ------- | ----------- | -------- | ----------- |
|     |     |     | R i | B   | −        | −        | − −          | −       | − −     | −           | − −      | − w−        |
|     |     |     | m   | X G | r o      | e w er o | e w          | r o e w | r o     | e w         | er o e w | r o e       |
|     |     |     | d o |     | Z e      | F Z      |   F Z        | e   F   | Z e     |   F Z       |   F      | Z e   F     |
|     |     |     | n   |     |  :  4  : | 5  :     | 5   : 2  :   | 2  :    |   :     | 4  : 5  :   | 5   :    | 2  :   2  : |
|     |     |     | R a |     | − 4 T −  | −3 . 3.  | −            | a −     | − 4 T − | −3 .        | 3. −     | a −         |
|     |     |     |     | P T | P        | T −      | m a          | m P     | T P     |             | T − m a  | m           |
|     |     |     |     | G   | G        | P T P    | a l a        | G       | G       | P T P       | a        | l a         |
|     |     |     |     |     | G        | G        | L l L        |         |         | G G         | L l      | L           |
Underlying Automated−Text−Annotation Methods
Figure OA-4: Results for Outcome = “Attack” in Fowler et al. (2021). Note: In the top panel, red dotted lines
represent point estimates of the “Benchmark” estimates and gray dotted lines represent their 95% confidence intervals.
To show the average performance across random sampling of expert-coding, we report the average point estimates and
standard errors across 500 repeated sampling. In the bottom panel, blue dotted lines represent 95%.
| H Empirical         |     |             | Application        |     | based | on   | Pan    | and |     | Chen | (2018) |     |
| ------------------- | --- | ----------- | ------------------ | --- | ----- | ---- | ------ | --- | --- | ---- | ------ | --- |
| H.1 LLM             |     | Annotations | for                | Pan | and   | Chen | (2018) |     |     |      |        |     |
| H.1.1 Specification |     |             | of LLM Annotations |     |       |      |        |     |     |      |        |     |
Models. As we did for the first application, we use three LLMs for our empirical application based on Pan and
| Chen (2018): | GPT-3.5, |     | GPT-4 and | Llama-2-70B-chat. |     |     |     |     |     |     |     |     |
| ------------ | -------- | --- | --------- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Prompt. In this empirical application, we annotate two different variables: Prefecture Wrongdoing (whether each
citizen complaint accuses of prefecture-level wrongdoing) and County Wrongdoing (whether each citizen complaint
accusesofcounty-levelwrongdoing). ForPrefectureWrongdoing,weusedthefollowingpromptforGPTs. ForLlama-
18

2, we found that the performance based on Chinese prompts is so poor that we decided to use the English version of
the same prompt.
下面的中文文本是发生在中国江西省九江市的一起投诉，判断帖子是否指控了九江市地级层面的政府官员或政府机构有不当行为，包括指控腐败和暴力，以及违反法律和法
规。请注意，评估仅考虑针对九江市地级的指控，不包括针对下辖地区及其子地区的任何指控（这些下辖地区包括’濂溪区’、’浔阳区’、’柴桑区’、’瑞昌市’、’共青城市’、’庐
山市’、’武宁县’、’修水县’、’永修县’、’德安县’、’都昌县’、’湖口县’、’彭泽县’）。
如果帖子包含对九江市地级官员或机构的上述性质的指控，请返回’1’。否则，请返回’0’。
文本：”””
{text}
”””
回答：
where {text} denotes that a text to be labeled (i.e., each online complaint). The combined prompt-plus-text is then
given as an input to a LLM.
ForCounty Wrongdoing,weusedthefollowingpromptforGPTs. Again,forLlama-2,wefoundthattheperformance
based on Chinese prompts is so poor that we decided to use the English version of the same prompt.
下面的文本是发生在中国江西省九江市的一起投诉。判断帖子是否指控了九江市下辖地区及其子地区的政府官员或政府机构有不当行为，这些不当行为包括指
控腐败和暴力，以及违反法律和法规。请注意，评估仅考虑针对九江市地级下辖地区或其子地区的指控（下辖地区包括濂溪区、浔阳区、柴桑区、瑞昌市、共
青城市、庐山市、武宁县、修水县、永修县、德安县、都昌县、湖口县、彭泽县），不包括任何针对九江市地级的指控。
如果帖子包含针对九江市地级市下辖地区或其子地区官员或机构的上述性质的指控，请返回’1’。否则，请返回’0’。
文本：”””
{text}
”””
回答：
H.1.2 Additional LLM Results
In Section 2.1.2, we reported the F1 scores for the overall performance of LLM annotations. Here, we provide
additional details.
Figure OA-3 shows F1scoresand the classification accuracyfor both “Prefecture Wrongdoing” and “CountyWrong-
doing”. Several points are worth noting. First, the performance varies across two tasks. It is easier to predict
“Prefecture Wrongdoing” than to predict “County Wrongdoing” across models and prompts. Second, in this appli-
cation, the prediction performance is relatively stable across models and prompts. However, as we see in Section 5,
eventhoughtheaveragepredictionperformanceisrelativelysimilar,becausepredictionerrorsarenon-random,LLM-
only estimation using different LLM annotations produces very different results. This highlights the methodological
problem of ignoring prediction errors.
H.2 Additional DSL Results for Pan and Chen (2018)
Setup
DSL requires simple four steps. First, we generate LLM annotations for the entire population of documents. As we
discussed in Section 2, we here consider six versions: GPT 4, GPT 3.5, and Llama 2 with zero-shot and few-shot
learning. In the second step, we randomly sample 500 documents for expert-coding. In the third step, using the
expert-coded data, we further improve LLM predictions by cross-fitting the generalized random forest to predict the
expert-coded labels with LLM annotations produced in the first step. Finally, we combine expert-coded labels and
19

| Wrongdoing: F1 score |           |         |      |         |      | Wrongdoing: Accuracy  |           |         |      |         |                       |
| -------------------- | --------- | ------- | ---- | ------- | ---- | --------------------- | --------- | ------- | ---- | ------- | --------------------- |
|                      | GPT 4     | GPT 3.5 |      | Llama 2 |      |                       | GPT 4     | GPT 3.5 |      | Llama 2 |                       |
| 1.00                 | 0.95 0.94 |         |      |         |      | 1.00                  | 0.95 0.94 |         |      |         |                       |
|                      |           | 0.88    | 0.91 | 0.91    | 0.91 |                       |           |         | 0.9  | 0.9     | 0.91                  |
|                      |           |         |      |         |      | Prefecture Wrongdoing |           | 0.85    |      |         | Prefecture Wrongdoing |
| 0.75                 |           |         |      |         |      | 0.75                  |           |         |      |         |                       |
| 0.50                 |           |         |      |         |      | 0.50                  |           |         |      |         |                       |
| 0.25                 |           |         |      |         |      | 0.25                  |           |         |      |         |                       |
| erocs 1F             |           |         |      |         |      | ycaruccA              |           |         |      |         |                       |
| 0.00                 |           |         |      |         |      | 0.00                  |           |         |      |         |                       |
| 1.00                 |           |         |      |         |      | 1.00                  |           |         |      |         |                       |
|                      |           |         | 0.82 | 0.83    | 0.84 |                       |           | 0.81    | 0.82 | 0.83    | 0.85                  |
0.78 0.79 0.81 Country Wrongdoing 0.77 0.79 Country Wrongdoing
| 0.75 |     |     |     |     |     | 0.75 |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
| 0.50 |     |     |     |     |     | 0.50 |     |     |     |     |     |
| 0.25 |     |     |     |     |     | 0.25 |     |     |     |     |     |
| 0.00 |     |     |     |     |     | 0.00 |     |     |     |     |     |
Zero−shotFew−shot Zero−shotFew−shot Zero−shotFew−shot Zero−shotFew−shot Zero−shotFew−shot Zero−shotFew−shot
Figure OA-5: Prediction Performance of LLM annotations: Pan and Chen (2018).
Note: The left panel shows F1 scores and the right panel shows the classification accuracy.
predictedlabelsintheDSLlogisticregressionwithexactlythesamespecificationintheoriginalpaper. Inparticular,
we regress the upward reporting (i.e., whether a given complaint is reported upward to provincial-level officials) on
the aforementioned two independent variables (Prefecture Wrongdoing and County Wrongdoing) and other control
variables with interactions where “Other Controls” include prevalence, group issue, sentiment, personal experience,
collectiveaction, petitions, andprovincialjurisdiction. SeeColumn(3)inTable3oftheoriginalpaper. Importantly,
| “Prefecture | Wrongdoing” |     | and “County | Wrongdoing” |     | are text-based. |     |     |     |     |     |
| ----------- | ----------- | --- | ----------- | ----------- | --- | --------------- | --- | --- | --- | --- | --- |
We compare DSL against the classical supervised learning approach and the LLM-only estimation. For the classical
supervised learning approach, we examine five widely used supervised ML methods: lasso, ridge, random forest,
and XGBoost. We use a term-document matrix used in the original paper, which has more than 5000 variables, as
predictors. For the LLM-only estimation, we consider the same six versions of LLM annotations.
Results
In the main paper, we reported the results for two main coefficients, “Prefecture Wrongdoing” and “County Wrong-
doing”. In this appendix, we also report the results based on the first differences because coefficients of logistic
regression tend to be difficult to interpret and it is often recommended to report results based on the differences in
predicted probabilities. As we emphasized in the paper, researchers can apply DSL and then use estimated coeffi-
cients to compute the first differences or any other function of estimated coefficients. Here we specifically focus on
the two effects that the original authors focused on most: the effect of “Prefecture Wrongdoing” and the effect of
“Connection” for posts accusing of “Country Wrongdoing”. We report the results in Figure OA-6.
The main findings are similar. First, estimates from the LLM-only estimation are biased, and substantive and
statistical conclusions can flip depending on which LLMs users choose. Confidence intervals are also, in general,
invalid. Some LLM-only estimators have reasonable coverages for at least one outcome, but no LLM-only estimator
has 95% coverages for both effects because they do not have any theoretical guarantees. Second, estimates from the
20

classical supervised learning method are similarly biased because they ignore prediction errors, and they have invalid
confidence intervals. In contrast to these existing approaches, DSL has unbiased estimates and valid confidence
| intervals, regardless | of  | the underlying |     | automated |     | text | annotation | method. |     |     |
| --------------------- | --- | -------------- | --- | --------- | --- | ---- | ---------- | ------- | --- | --- |
Estimates and Standard Errors (First Differences)
|     |     | Benchmark |     | Classical Supervised ML |     |     | LLM−only Estimation |     |     | DSL |
| --- | --- | --------- | --- | ----------------------- | --- | --- | ------------------- | --- | --- | --- |
0.50
Prefecture Wrongdoing
0.25
0.00
−0.25
eziS tceffE
−0.50
0.50
County Wrongdoing
 x Connections
0.25
0.00
−0.25
−0.50
|     |     |     |     | Lasso | d g e m Forest | o s t      | h o t h o t h   | o t h o t h o t | h o t h o t    | h o t h o t h o t h ot w−Shot |
| --- | --- | --- | --- | ----- | -------------- | ---------- | --------------- | --------------- | -------------- | ----------------------------- |
|     |     |     |     | R i   |                | B o − S    | − S − S         | − S − S −       | S − S          | − S − S − S − S               |
|     |     |     |     |       | X              | G er o     | e w e r o       | e w er o e w    | er o e w       | e r o e w er o e              |
|     |     |     |     |       | d o            |   Z :      | F   Z :  F      |   Z :  F        |   Z :   F      |   Z :  F   Z :  F             |
|     |     |     |     |       | a n            | 4  : − 4   | 5  : . 5        | 2  : − 2        | −4  : − 4   5  | : . 5   2  : − 2              |
|     |     |     |     | R     |                | P T − P T  | − 3 . T − 3 m a | − m a P T       | P T − 3 .      | T − 3 m a − m a               |
|     |     |     |     |       |                | G G P T    | P a             | l a G           | G P T          | P a l a                       |
|     |     |     |     |       |                | G          | G L l           | L               | G G            | L l L                         |
Underlying Automated−Text−Annotation Methods
(a)
Coverage of 95% Confidence Intervals (First Differences)
|     |     | Classical Supervised ML |     |     |     | LLM−only Estimation |     |     |     | DSL |
| --- | --- | ----------------------- | --- | --- | --- | ------------------- | --- | --- | --- | --- |
1.00
Prefecture Wrongdoing
0.75
0.50
tnecreP egarevoC 0.25
0.00
1.00
County Wrongdoing
 x Connections
0.75
0.50
0.25
0.00
|     |     | Lasso | Rid g e | m Forest | o st      | h ot h o t  | h o t h o t | h ot h o t | h ot h o t | h o t h o t h ot ew−Shot |
| --- | --- | ----- | ------- | -------- | --------- | ----------- | ----------- | ---------- | ---------- | ------------------------ |
|     |     |       |         |          | B o −     | S − S −     | S − S −     | S − S      | − S − S    | − S − S − S              |
|     |     |       |         | X        | G er o    | e w e r o   | e w e r o   | e w er     | o e w e r  | o e w e r o              |
|     |     |       | ndo     |          | 4 :  Z    | :   F   Z   | :   F   Z   | :  F   Z   | :   F   Z  | :   F   Z :  F           |
|     |     |       | a       |          | − 4       | 5  : . 5    | 2  : −      | 2  4  :    | − 4   5  : | . 5   2  : − 2           |
|     |     |       | R       |          | P T − P T | − 3 . T − 3 | m a − m a   | P T − P T  | − 3 . T −  | 3 m a − m a              |
|     |     |       |         |          | G G       | P T P       | a l a       | G G        | P T P      | a l a                    |
|     |     |       |         |          | G         | G L l       | L           |            | G G        | L l L                    |
Underlying Automated−Text−Annotation Methods
(b)
FigureOA-6: ComparisonsofDSLandExistingApproachesintermsofFirstDifferencesusingPanandChen
(2018). Note: In Panel (a), red dotted lines represent point estimates of the “Benchmark” estimates and gray dotted
lines represent their 95% confidence intervals. To show the average performance across random sampling of expert-coding,
we report the average point estimates and standard errors across 500 repeated sampling. In Panel (b), blue dotted lines
represent 95%.
21

I Literature Review
To evaluate the current practice of text annotations in text-as-data applications in political science, we conducted
a review of academic articles published in the top 10 political science journals: American Political Science Review
(APSR),AmericanJournalofPoliticalScience(AJPS),JournalofPolitics(JOP),PoliticalBehavior(PB),Quarterly
JournalofPoliticalScience(QJPS),BritishJournalofPoliticalScience(BJPS),ComparativePoliticalStudies(CPS),
World Politics (WP), International Organization (IO), and Journal of Experimental Political Science (JEPS).
We first searched for all articles published in the years 2015 through 2022 (inclusive) using a keyword “text as data”
and “text analysis” in Web of Science. We also included the articles published in the above-mentioned top journals
thatciteGrimmerandStewart(2013). Intotal,wereviewed88papers. Wenotethatthisnumberisthelowerbound
of the actual number of papers using text-as-data methods because some papers do not explicitly use terminologies,
such as “text as data” and “text analysis”.
We then manually coded the following information for each paper. (1) Whether a paper uses some forms of text
annotations (if so, we continue to code for the remaining items): (2) A type of downstream analyses that use text-
based variables: (3) Whether text-based variables are used as the outcome and/or independent variables in the
downstream analyses: (4) Whether a paper explicitly acknowledges the potential biases due to prediction errors: (5)
Whether a paper statistically addresses the potential biases due to prediction errors: (6) If a paper uses the classical
supervised learning approach, what is the F-1 score and the classification accuracy of the text classification step?
References
Angelopoulos,AnastasiosN.,StephenBates,ClaraFannjiang,MichaelI.Jordan,andTijanaZrnic.2023.“Prediction-
poweredinference.”Science 382(6671):669–674.https://doi.org/10.1126/science.adi6000.https://www.science.
org/doi/abs/10.1126/science.adi6000.
Argyle, Lisa P, Ethan C Busby, Nancy Fulda, Joshua R Gubler, Christopher Rytting, and David Wingate. 2023.
“Out of One, Many: Using Language Models to Simulate Human Samples.” Political Analysis 31 (3): 337–351.
Bommasani,Rishi,DrewAHudson,EhsanAdeli,RussAltman,SimranArora,SydneyvonArx,MichaelSBernstein,
JeannetteBohg,AntoineBosselut,EmmaBrunskill,etal.2021.“OntheOpportunitiesandRisksofFoundation
Models.” arXiv preprint arXiv:2108.07258.
Bosley,Mitchell,SakiKuzushima,TedEnamorado,andYukiShiraito.2022.“ImprovingProbabilisticModelsinText
Classification via Active Learning.” arXiv preprint arXiv:2202.02629.
Chakrabortty,Abhishek,andTianxiCai.2018.“Efficientandadaptivelinearregressioninsemi-supervisedsettings.”
Annals of Statistics.
Chakrabortty, Abhishek, Guorong Dai, and Eric Tchetgen Tchetgen. 2022. “A General Framework for Treatment
Effect Estimation in Semi-Supervised and High Dimensional Settings.” arXiv preprint arXiv:2201.00468.
Chen,Yi-Hau,andHungChen.2000.“AUnifiedApproachtoRegressionAnalysisunderDouble-SamplingDesigns.”
Journal of the Royal Statistical Society Series B: Statistical Methodology 62 (3): 449–460.
Chernozhukov,Victor,DenisChetverikov,MertDemirer,EstherDuflo,ChristianHansen,WhitneyNewey,andJames
Robins. 2018. “Double/Debiased Machine Learning for Treatment and Structural Parameters.” Econometrics
Journal 21:C1–C68.
Chernozhukov, Victor, Juan Carlos Escanciano, Hidehiko Ichimura, Whitney K Newey, and James M Robins. 2022.
“Locally robust semiparametric estimation.” Econometrica 90 (4): 1501–1535.
Clayton, Katherine, Yusaku Horiuchi, Aaron R Kaufman, Gary King, and Mayya Komisarchik. 2023. Correcting
Measurement Error Bias in Conjoint Survey Experiments. Technical report. Working Paper.
22

Davidian, Marie. 2022. “Methods based on semiparametric theory for analysis in the presence of missing data.”
| Annual | Review | of Statistics |     | and Its | Application | 9:167–196. |     |
| ------ | ------ | ------------- | --- | ------- | ----------- | ---------- | --- |
Egami,Naoki,ChristianJ.Fong,JustinGrimmer,MargaretE.Roberts,andBrandonM.Stewart.2022.“HowtoMake
Causal Inferences Using Texts.” Science Advances 8 (42): eabg2652. https://doi.org/10.1126/sciadv.abg2652.
Egami, Naoki, Musashi Hinck, Brandon Stewart, and Hanying Wei. 2023. “Using Imperfect Surrogates for Down-
streamInference:Design-basedSupervisedLearningforSocialScienceApplicationsofLargeLanguageModels.”
| Advances | in Neural | Information |     | Processing |     | Systems | 36. |
| -------- | --------- | ----------- | --- | ---------- | --- | ------- | --- |
Fong,Christian,andJustinGrimmer.2021.“CausalInferencewithLatentTreatments.”AmericanJournalofPolitical
Science.
Fong,Christian,andMatthewTyler.2021.“Machinelearningpredictionsasregressioncovariates.”Political Analysis
29 (4): 467–484.
Fowler,ErikaFranklin,MichaelMFranz,GregoryJMartin,ZacharyPeskowitz,andTravisNRidout.2021.“Political
Advertising Online and Offline.” American Political Science Review 115 (1): 130–149.
Gilardi, Fabrizio, Meysam Alizadeh, and Ma¨el Kubli. 2023. “ChatGPT Outperforms Crowd-Workers for Text-
| Annotation | Tasks.” | arXiv | preprint | arXiv:2303.15056. |     |     |     |
| ---------- | ------- | ----- | -------- | ----------------- | --- | --- | --- |
Grimmer, Justin, and Brandon M Stewart. 2013. “Text as Data: The Promise and Pitfalls of Automatic Content
| Analysis | Methods | for Political |     | Texts.” | Political | analysis | 21 (3): 267–297. |
| -------- | ------- | ------------- | --- | ------- | --------- | -------- | ---------------- |
Hager,Anselm,andHannoHilbig.2020.“DoesPublicOpinionAffectPoliticalSpeech?”AmericanJournalofPolitical
| Science | 64 (4): | 921–937. |     |     |     |     |     |
| ------- | ------- | -------- | --- | --- | --- | --- | --- |
Heseltine,Michael,andBClemmVonHohenberg.2023.“LargeLanguageModelsasASubstituteforHumanExperts
| in Annotating |     | Political | Text.” | preprint | SocArxiv: | cx752. |     |
| ------------- | --- | --------- | ------ | -------- | --------- | ------ | --- |
Hopkins, Daniel J, and Gary King. 2010. “A Method of Automated Nonparametric Content Analysis for Social
| Science.” | American | Journal |     | of Political | Science | 54  | (1): 229–247. |
| --------- | -------- | ------- | --- | ------------ | ------- | --- | ------------- |
Kallus, Nathan, and Xiaojie Mao. 2020. “On the role of surrogates in the efficient estimation of treatment effects
| with limited | outcome |     | data.” | arXiv preprint |     | arXiv:2003.12408. |     |
| ------------ | ------- | --- | ------ | -------------- | --- | ----------------- | --- |
Katsumata, Hiroto, and Soichiro Yamauchi. 2023. Statistical Analysis with Machine Learning Predicted Variables.
| Technical | report. | Working | Paper. |     |     |     |     |
| --------- | ------- | ------- | ------ | --- | --- | --- | --- |
Keith, Katherine, and Brendan O’Connor. 2018. “Uncertainty-aware generative models for inferring document class
prevalence.”InProceedings of the 2018 Conference on Empirical Methods in Natural Language Processing,4575–
4585. Brussels, Belgium: Association for Computational Linguistics. https://doi.org/10.18653/v1/D18-1487.
https://aclanthology.org/D18-1487.
Kennedy, Edward H. 2022. “Semiparametric doubly robust targeted double machine learning: a review.” arXiv
preprint arXiv:2203.06469.
Kennedy, Edward H, Sivaraman Balakrishnan, and Max G’Sell. 2020. “Sharp instruments for classifying compliers
| and generalizing |     | causal | effects.” | Annals | of Statistics. |     |     |
| ---------------- | --- | ------ | --------- | ------ | -------------- | --- | --- |
Knox,Dean,andChristopherLucas.2021.“ADynamicModelofSpeechfortheSocialSciences.”American Political
| Science | Review | 115 (2): | 649–666. |     |     |     |     |
| ------- | ------ | -------- | -------- | --- | --- | --- | --- |
Knox, Dean, Christopher Lucas, and Wendy K Tam Cho. 2022. “Testing Causal Theories with Learned Proxies.”
| Annual | Review | of Political | Science |     | 25:419–441. |     |     |
| ------ | ------ | ------------ | ------- | --- | ----------- | --- | --- |
Kuzman, Taja, Nikola Ljubeˇsi´c, and Igor Mozetiˇc. 2023. “ChatGpt: Beginning of An End of Manual Annotation?
Use Case of Automatic Genre Identification.” arXiv preprint arXiv:2303.03953.
Li, Minzhi, Taiwei Shi, Caleb Ziems, Min-Yen Kan, Nancy F Chen, Zhengyuan Liu, and Diyi Yang. 2023. “CoAnno-
tating:Uncertainty-guidedWorkAllocationbetweenHumanandLargeLanguageModelsforDataAnnotation.”
| arXiv preprint |     | arXiv:2310.15638. |     |     |     |     |     |
| -------------- | --- | ----------------- | --- | --- | --- | --- | --- |
Linegar, Mitchell, Rafal Kocielnik, and R Michael Alvarez. 2023. “Large Language Models and Political Science.”
| Frontiers | in Political | Science |     | 5:1257092. |     |     |     |
| --------- | ------------ | ------- | --- | ---------- | --- | --- | --- |
23

Mellon, Jonathan, Jack Bailey, Ralph Scott, James Breckwoldt, and Marta Miori. 2022. “Does GPT-3 Know What
the Most Important Issue Is? Using Large Language Models to Code Open-Text Social Survey Responses At
| Scale.” | SSRN preprint: |     | 4310154. |     |     |     |     |
| ------- | -------------- | --- | -------- | --- | --- | --- | --- |
Mets, Mark, Andres Karjus, Indrek Ibrus, and Maximilian Schich. 2023. “Automated Stance Detection in Complex
Topics and Small Languages: The Challenging Case of Immigration in Polarizing News Media.” arXiv preprint
arXiv:2305.13047.
Møller, Anders Giovanni, Jacob Aarup Dalsgaard, Arianna Pera, and Luca Maria Aiello. 2023. “Is A Prompt and A
Few Samples All You Need? Using GPT-4 for Data Augmentation in Low-Resource Classification Tasks.” arXiv
preprint arXiv:2304.13861.
Mozer, Reagan, and Luke Miratrix. 2023. “Decreasing the Human Coding Burden in Randomized Trials with Text-
based Outcomes via Model-Assisted Impact Analysis.” arXiv preprint arXiv:2309.13666.
Newey, Whitney K, and Daniel McFadden. 1994. “Large Sample Estimation and Hypothesis Testing.” Handbook of
| econometrics | 4:2111–2245. |     |     |     |     |     |     |
| ------------ | ------------ | --- | --- | --- | --- | --- | --- |
Ollion, Etienne, Rubing Shen, Ana Macanovic, and Arnault Chatelain. 2023. “Chatgpt for Text Annotation? Mind
| the Hype!” | SocArXiv. | October | 4.  |     |     |     |     |
| ---------- | --------- | ------- | --- | --- | --- | --- | --- |
Ornstein, Joseph T, Elise N Blasingame, and Jake S Truscott. 2022. How to Train Your Stochastic Parrot: Large
| Language | Models | for Political | Texts. | Technical | report. | Working | Paper. |
| -------- | ------ | ------------- | ------ | --------- | ------- | ------- | ------ |
Palmer, Alexis, and Arthur Spirling. 2023. Large Language Models Can Argue in Convincing and Novel Ways About
Politics: Evidence from Experiments and Human Judgement. Technical report. Working paper.
Pan,Jennifer,andKaipingChen.2018.“ConcealingCorruption:HowChineseOfficialsDistortUpwardReportingof
| Online | Grievances.” | American | Political | Science | Review | 112 | (3): 602–620. |
| ------ | ------------ | -------- | --------- | ------- | ------ | --- | ------------- |
Pangakis, Nicholas, Samuel Wolken, and Neil Fasching. 2023. “Automated Annotation with Generative AI Requires
| Validation.” | arXiv | preprint | arXiv:2306.00176. |     |     |     |     |
| ------------ | ----- | -------- | ----------------- | --- | --- | --- | --- |
Rathje, Steve, Dan-Mircea Mirea, Ilia Sucholutsky, Raja Marjieh, Claire Robertson, and Jay J Van Bavel. 2023.
| “GPT is | An Effective | Tool | for Multilingual |     | Psychological | Text | Analysis.” |
| ------- | ------------ | ---- | ---------------- | --- | ------------- | ---- | ---------- |
Robins, James M, and Andrea Rotnitzky. 1995. “Semiparametric efficiency in multivariate regression models with
missing data.” Journal of the American Statistical Association 90 (429): 122–129.
Robins, James M, Andrea Rotnitzky, and Lue Ping Zhao. 1994. “Estimation of Regression Coefficients When Some
Regressors Are Not Always Observed.” Journal of the American Statistical Association 89 (427): 846–866.
Rotnitzky, Andrea, and Stijn Vansteelandt. 2014. “Double-robust methods.” In Handbook of missing data methodol-
| ogy, 185–212. | CRC | Press. |     |     |     |     |     |
| ------------- | --- | ------ | --- | --- | --- | --- | --- |
Torres, Michelle, and Francisco Cantu´. 2022. “Learning to See: Convolutional Neural Networks for the Analysis of
| Social Science | Data.” | Political | Analysis | 30  | (1): 113–131. |     |     |
| -------------- | ------ | --------- | -------- | --- | ------------- | --- | --- |
Tsiatis, Anastasios A. 2006. Semiparametric theory and missing data. Springer.
Vansteelandt, Stijn, and Oliver Dukes. 2022. “Assumption-lean Inference for Generalised Linear Model Parameters.”
Journal of the Royal Statistical Society Series B: Statistical Methodology 84, no. 3 (July): 657–685. issn: 1369-
7412. https://doi.org/10.1111/rssb.12504. eprint: https://academic.oup.com/jrsssb/article-pdf/84/3/657/
49322532/rssb12504-sup-0001-supinfo.pdf. https://doi.org/10.1111/rssb.12504.
Wang, Siruo, Tyler H McCormick, and Jeffrey T Leek. 2020. “Methods for Correcting Inference based on Outcomes
Predicted by Machine Learning.” Proceedings of the National Academy of Sciences 117 (48): 30266–30275.
Wu,PatrickY,JoshuaATucker,JonathanNagler,andSolomonMessing.2023.“LargeLanguageModelsCanbeUsed
to Estimate the Ideologies of Politicians in A Zero-Shot Learning Setting.” arXiv preprint arXiv:2303.12057.
Yang, Kai-Cheng, and Filippo Menczer. 2023. “Large Language Models Can Rate News Outlet Credibility.” arXiv
preprint arXiv:2304.00228.
Zhang, Han. 2021. “How Using Machine Learning Classification as a Variable in Regression Leads to Attenuation
| Bias and | What to | Do About | It.” SocArXiv. |     |     |     |     |
| -------- | ------- | -------- | -------------- | --- | --- | --- | --- |
Ziems, Caleb, William Held, Omar Shaikh, Jiaao Chen, Zhehao Zhang, and Diyi Yang. 2024. “Can large language
models transform computational social science?” Computational Linguistics 50 (1): 237–291.
24