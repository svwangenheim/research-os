4
2
0
2

v
o
N
7

]
L
C
.
s
c
[

1
v
0
5
0
5
0
.
1
1
4
2
:
v
i
X
r
a

Selecting Between BERT and GPT for Text Classification in

Political Science Research

Yu Wang∗, Wen Qu, Xin Ye
Fudan University

Abstract

Political scientists often grapple with data scarcity in text classification. Recently,
fine-tuned BERT models and their variants have gained traction as effective solutions
to address this issue. In this study, we investigate the potential of GPT-based models
combined with prompt engineering as a viable alternative. We conduct a series of
experiments across various classification tasks, differing in the number of classes and
complexity, to evaluate the effectiveness of BERT-based versus GPT-based models in
low-data scenarios. Our findings indicate that while zero-shot and few-shot learning
with GPT models provide reasonable performance and are well-suited for early-stage
research exploration, they generally fall short — or, at best, match — the performance
of BERT fine-tuning, particularly as the training set reaches a substantial size (e.g.,
1,000 samples). We conclude by comparing these approaches in terms of performance,
ease of use, and cost, providing practical guidance for researchers facing data limi-
tations. Our results are particularly relevant for those engaged in quantitative text
analysis in low-resource settings or with limited labeled data.

1 Introduction

Text classification is one of the most common tasks in quantitative text analysis. Re-

searchers often need to classify different texts into topics. Such texts encompass news

articles (Laurer et al., 2024; H¨affner et al., 2023; Barber´a et al., 2021; Y. Wang et al.,

2017, 2015), tweets (Widmann & Wich, 2023; Kim, 2022), public speeches (Widmann &

Wich, 2023; Y. Wang, 2023b), video descriptions (Lai et al., 2024), names (Kaufman &

Klevs, 2022; Chaturvedi & Chaturvedi, 2023), among others. Regardless of the specific

∗yuwang.aiml@gmail.com

1

text form, one of the key bottlenecks in performing text classification is data scarcity:

procuring labeled data is a slow and labor-intensive process and as a result the labeled set

is oftentimes fairly small.

To resolve the data scarcity issue, researchers have explored various approaches. For

example, some researchers have trained models using labeled cross-domain data, which is

abundant, and then applied the trained model to in-domain classification (Osnabr¨ugge et

al., 2021). Others have studied the plausibility of using ChatGPT as an automatic anno-

tator to replace human annotation and speed up the labeling process (Gilardi et al., 2023).

Still others have considered instead of random sampling how to select more informative

samples for labeling so as to reduce the number of labeled samples (Kaufman, 2024). Thus

far, however, the most effective approach has been finetuning BERT models (Devlin et

al., 2019). By coupling general knowledge in the pretrained language models and a few

hundred task-specific samples, finetuned BERT models have proven to offer superior per-

formance as compared with classical models such as logistic regression (Laurer et al., 2024;

Y. Wang, 2023a). Over the past few years, this pretrain-finetune paradigm (Y. Wang &

Qu, 2024) has quickly established itself as the go-to method for text classification (Laurer

et al., 2024; Lai et al., 2024).

In this article, we study zero-shot and few-shot prompting with GPT models as a

potential alternative solution to the data scarcity problem.1 Specifically, we analyze in

situations with 1,000 or fewer samples how prompting with GPT models compares with

finetuned BERT models in binary and multi-class classification. Through extensive ex-

periments, we demonstrate that zero-shot and few-shot learning with GPT-based large

language models can serve as an effective alternative to fine-tuning BERT models. The

advantages of GPT models for classification are particularly prominent when the number

of classes is small, e.g., 2, and when the task is easier.

1Besides

prompting,

models
(https://platform.openai.com/docs/guides/fine-tuning/). We do not explore this approach here be-
cause our early explorations in this direction did not yield promising results.

alternative

finetune

another

these

GPT

to

is

2

2 Text Classification in Political Science

Quantitative text analysis has gone through quite a few distinctive methodological stages

throughout its evolution: feature-based classical models, word embeddings, BERT models,

and more recently generative models.2 As in other social science disciplines (Nielbo et al.,

2024; O. N. Kjell et al., 2024; Y. Wang et al., 2022), text analysis in political science

research has followed a similar trajectory. Initially, researchers converted texts into counts

and trained classical models from scratch. Subsequently, word counts were replaced with

word embeddings, and recurrent neural networks were employed for classification. More

recently, there has been a growing body of literature focused on fine-tuning BERT models.

2.1 Classical Models

Classical models refer mostly to the simpler and smaller models that take word counts

as input. Naive Bayes, support vector machine and logistic regression models generally

fall into this category (Hastie et al., 2009; Y. Wang et al., 2022; Bestvater & Monroe,

2023).3 They are simpler in model architecture, smaller in model size, require training

from scratch, and take word frequencies as input. Given that the order of words is not

utilized, these models are considered as a “bag of words” approach. Other hallmarks of

classical models include preprocessing and feature engineering. Because of the significance

of word frequencies, careful preprocessing steps are usually required (Rodriguez & Spirling,

2022). Given the number of words (i.e., features) can be enormous, researchers need to

manually decide what features to include and what to exclude (Y. Wang et al., 2022).

Prominent examples that utilize classical models for text classification include D’Orazio

et al. (2014), which uses support vector machine to classify documents on the Militarized

Interstate Dispute 4 (MID4) data collection project, and Diermeier et al. (2011), which

uses support vector machine to classify U.S. senators into ‘(extreme) conservative’ and

2Some researchers have grouped the stages of word embeddings and BERT models into a unified repre-

sentation learning stage (Nielbo et al., 2024).

3In addition to their use as natural language processing tools, these models are also often trained on

tabular data. See for (Muchlinski et al., 2016) and (Y. Wang, 2019a) for recent examples.

3

‘(extreme) liberal’ using those senators’ speeches as text input.

2.2 Word Embeddings

Word embeddings are vector representations of words (Mikolov et al., 2013; Pennington et

al., 2014; Y. Wang, 2019b; Rodriguez & Spirling, 2022). By projecting words into a vector

space based on their co-occurrence patterns, word embeddings possess semantic meaning,

with semantically similar words located close to each other in the vector space. Researchers

have utilized word embeddings to study various topics, such as ideological placement in

parliamentary corpora (Rheault & Cochrane, 2019) and the evolving meaning of political

concepts (Rodman, 2019). Beyond serving as standalone entities, these embeddings can

also function as input to recurrent neural networks for text classification (Chang & Mas-

terson, 2020; Y. Wang et al., 2017). For notable applications of embeddings in other social

studies, readers can refer to Simchon et al. (2023), Peng et al. (2024), Rai et al. (2024)

and Y. Wang (2024).

2.3 BERT Models

BERT models, which are encoder-based language models, have emerged as one of the most

effective tools for text classification (Y. Wang & Qu, 2024). They are rooted in the trans-

former architecture first introduced by Vaswani et al. (2017). Since their introduction in

2018 (Devlin et al., 2019), BERT models have consistently achieved state-of-the-art perfor-

mance across various natural language processing tasks (Devlin et al., 2019). Building on

their initial success, numerous variations of BERT models have been developed, incorpo-

rating more extensive training data (Y. Liu et al., 2019), specialized data domains (Hu et

al., 2022; Lee et al., 2019), and novel pretraining tasks (Lan et al., 2020). In the last couple

of years, they have started to gain traction in political science research. Whether it is clas-

sifying news articles into different economic sentiments (Laurer et al., 2024), parliamentary

speeches into different topics (Y. Wang, 2023b), tweets for depression detection (Zhang et

al., 2021) or video descriptions into ideology categories (Lai et al., 2024). In addition to

4

their effectiveness as classifiers, BERT models have also been utilized by researchers for

embedding tasks (Peng et al., 2024; Rai et al., 2024; Kaufman, 2024; O. Kjell et al., 2023).

Researchers first transform texts into embeddings using BERT models and then apply

these embeddings in classical models such as logistic regression (Rodriguez & Spirling,

2022).

2.4 GPT Models

GPT models are decoder-based language models and represent another highly effective tool

for text analysis. Like BERT models, they also trace their roots back to the transformers

introduced in Vaswani et al. (2017). Unlike BERT models, GPT models are primarily

designed for text generation. They excel in tasks such as essay writing, text summariza-

tion, translation, question answering, idea generation, and medical report transformation,

among others (Radford et al., 2019; Korinek, 2023; Adams et al., 2023). Researchers in

various fields, such as economics (Mei et al., 2024) and psychology (Strachan et al., 2024),

have sought to leverage the generative capabilities of these models, exploring whether they

behave similarly to humans in classical games like the ultimatum bargaining game and the

prisoner’s dilemma game. Similarly, political scientists have explored using GPT models

to simulate human samples (Argyle, Busby, et al., 2023; Bisbee et al., 2024), investigat-

ing whether “silicon samples” respond to surveys in a manner akin to humans after the

models have been conditioned on thousands of socio-demographic backstories from real

participants. Others have explored leveraging these models’ generative capabilities for

chat interventions to improve online political conversations (Argyle, Bail, et al., 2023).

In addition to the original text generation capabilities, as GPT models grow in size,

they have started to demonstrate emergent abilities (Wei, Tay, et al., 2022) unseen in

smaller model versions.4 Among these emergent abilities are zero-shot prompting (Radford

et al., 2019) and few-shot prompting (Brown et al., 2020). For example, researchers have

explored the plausibility of using ChatGPT as an automatic annotator to replace human

4Per definition, “an ability is emergent if it is not present in smaller models but is present in larger

models.” (Wei, Tay, et al., 2022)

5

annotators (Gilardi et al., 2023). Others have studied whether ChatGPT can be used for

providing natural language explanations for implicit hateful speech detection (Huang et

al., 2023). Given the promise of zero-shot and few-shot prompting, a series of works (Zhong

et al., 2023; Ziems et al., 2024) in computer science have compared the performance of

prompting GPT models against that of finetuning BERT models and the general consensus

is that finetuned BERT models are still overall preferred for text classification despite their

much smaller size. In this article, our goal is to situate this question within the field of

political science, explore few-shot prompting as a potential solution to data scarcity, and

analyze the relative performance of BERT and GPT models in small-dataset settings.

3 Empirical Analyses

We primarily focus on five sets of experiments: (1) binary classification of news articles

based on economic sentiments, (2) 8-class classification of party manifestos,5 (3) 8-class

classification of New Zealand Parliamentary speeches, (4) 20-class classification of COVID-

19 policy measures, and (5) 22-class classification of the US State of the Union speeches.

For each experiment, we evaluate the performance of fine-tuning BERT models using

200, 500, and 1,000 samples. The particular BERT version that we use is RoBERTa-large

with 340 million parameters (Y. Liu et al., 2019).6 It is arguably the most performant

model in the BERT family (Ziems et al., 2024). In terms of hyperparameter tuning (Arnold

et al., 2024; Y. Wang & Qu, 2024; Goodfellow et al., 2016), we optimize the learning rate

(3e-5, 2e-5, 1e-5) using the validation set. Each experiment setting is run three times with

three different seeds and the mean, min, max are reported.

We further calculate the performance of GPT models with zero sample, 1 sample

per class and 2 samples per class, respectively. The particular GPT version we use is

GPT-4o.7 In terms of hyperparameter tuning (Gilardi et al., 2023), we use two different

5Data is collected from mostly democracies in OECD, Central and Eastern European countries and

South American countries.

6Please note that all our experiments utilize RoBERTa-large. For simplicity, we will use the terms

BERT and RoBERTa interchangeably in the following sections.

7Other GPT models include Gemini by Google, Claude by Anthropic, Llama by Meta, Mistral by

6

temperatures: a lower temperature at 0.2, which means less variation in the output, and

a higher temperature at 0.8, which means more variation. As in the BERT experiments,

each experimental setting is run three times. Each time a particular seed is used for repro-

ducibility. The mean of three runs is reported. For our prompting templates, interested

readers could refer to our replication package.

3.1 Economic Sentiment Classification (2-Class)

Sentiment analysis is one of the most common tasks that political scientists have to deal

with. Given a particular text snippet, our goal is classify it into either positive or negative.

It is often considered an easy task in that it has only two classes. In this experiment, we use

the Sentiment Economy News dataset by Barber´a et al. (2021) and Laurer et al. (2024).

The goal is to differentiate whether the economy is performing well or poorly according

to a given news headline and the corresponding first paragraph (Laurer et al., 2024). In

Table 1, we report the distribution of the two labels among the train, dev, and test sets.

It can be observed that approximately two-thirds of the samples are negative, a pattern

consistent across all three datasets. For finetuning the BERT model, we randomly sample

200, 500, and 1,000 samples from the training set. For procuring samples used in few-shot

prompting, we randomly select them from the training set as well.

Table 1: Summary statistics of the Sentiment Economy News dataset.

Dataset
Train
Dev
Test

Number of samples
2000
300
382

Positive
655 (32.75%)
102 (34.0%)
141 (36.91%)

Negative
1345 (67.25%)
198 (66.0%)
241 (63.09%)

In Figure 1, we report the experiment results. We observe that for finetuning BERT

models, as the number of training samples increases, the test accuracy increases from

71.1% (200 samples) to 73.4% (500 samples) and 73.9% (1,000 samples). In a similar vein,

Mistral AI. The latter two, in particular, offer open-source models. We opt for GPT-4o, which is closed-
source, because it arguably provides the best performance. Researchers interested in privacy or latency
could consider those smaller open-source alternatives.

7

we observe that one-shot prompting outperforms zero-shot prompting and that two-shot

prompting in turns supercedes one-shot prompting.

In terms of comparing finetuning

BERT models and prompting GPT models, we note that two-shot prompting with Chat-

GPT matches the performance of finetuning BERT models with 1,000 samples. Zero-shot

prompting (70.2%) is slightly lower than fine-tuning BERT with 200 samples (71.1%),

though the difference is minimal. Additionally, when adjusting the temperature settings

in prompting GPT, a temperature of 0.2 offers a slight performance advantage compared

to 0.8.

Figure 1: Increasing the number of samples enhances model accuracy, whether it’s through
fine-tuning BERT models or prompting GPT models.
‘RoBERTa # 200’ refers to fine-
tuning RoBERTa-large with 200 samples, while ‘Temp0.2 #0’ indicates zero-shot prompt-
ing with a temperature setting of 0.2. The black vertical error bar represents the range
from the minimum to the maximum values. Few-shot prompting with two samples per-
forms about the same as finetuning RoBERTa-large with 1,000 samples. Finetuning yields
a higher variance in test evaluations than prompting. A lower temperature setting of 0.2
yields slightly better performance than a higher temperature of 0.8 for prompting.

8

RoBERTa #200RoBERTa #500RoBERTa #1000Temp0.8 #0Temp0.2 #0Temp0.8 #1Temp0.2 #1Temp0.8 #2Temp0.2 #20.660.680.700.720.740.76Accuracy0.7110.7340.7390.6970.7020.7110.7200.7370.738Binary Sentiment Classification3.2 Manifesto Classification (8-Class)

Topic classification is another common task in political science research (Osnabr¨ugge et

al., 2021; Y. Wang, 2023b). In terms of the modeling process, it is essentially the same

as sentiment analysis, except that it often has more than two classes. In this subsection,

we compare the performance of finetuning BERT models with that of prompting GPT

models in an 8-class topic classification. The dataset comes from Laurer et al. (2024)

and is originally published by WZB Berlin Social Science Center. In this subsection, we

further study the problem of 8-class classification of party manifestos.8 In Table 2, we

report the data distribution. The 8 classes are Economy, External Relations, Fabric of

Society, Freedom and Democracy, No Other Category Applies, Political System, Social

Groups, and Welfare and Quality of Life. Economy and Welfare and Quality of Life are

the two largest classes, each accounting for between 27% and 30%. Other classes are more

or less evenly distributed, each accounting for about 9 percent. No Other Category Applies

is an exception in that it accounts for 0.65% of the training samples, 1.67% of the dev

samples and 0% of the test samples. Given how rare this class it, this task effectively boils

down to a 7-class classification problem.

Table 2: Distribution in Manifesto Datasets. Welfare and Quality of Life alone accounts
for nearly a third of the dataset, while Economy represents about one quarter of the
dataset. The smallest category, No Other Category Applies, comprises less than 2%.

Topic
Economy
External Relations
Fabric of Society
Freedom and Democracy
No Other Category Applies
Political System
Social Groups
Welfare and Quality of Life
Total

Train
553 (27.65%)
141 (7.05%)
231 (11.55%)
104 (5.2%)
13 (0.65%)
180 (9.0%)
194 (9.7%)
584 (29.2%)
2000

Dev
69 (23.0%)
24 (8.0%)
34 (11.33%)
23 (7.67%)
5 (1.67%)
22 (7.33%)
31 (10.33%)
92 (30.67%)
300

Test
85 (28.33%)
31 (10.33%)
28 (9.33%)
17 (5.67%)
- (-)
34 (11.33%)
22 (7.33%)
83 (27.67%)
300

8Note that data is from the Manifesto Project Dataset and is collected from mostly democracies in
OECD, Central and Eastern European countries and South American countries by the WZB Berlin Social
Science Center.

9

Figure 2: Prompting with or without samples lags behind fine-tuning RoBERTa-large
models by a sizeable margin in the 8-class manifesto classification.

In Figure 2, we report our experiment results. We observe that finetuning BERT

models yields substantially stronger results than prompting GPT models. As expected,

increasing the number of training samples improves the performance of finetuning BERT

models. At the same time, zero-shot prompting performs as well as few-shot prompting

in this 8-class classification task. When comparing between finetuning BERT models and

prompting GPT models, we observe that finetuning with 200 samples yields an accuracy

of 53.9% whereas zero-shot and few-shot prompting yield a maximum accuracy of 48.8%.

While adding extra samples helps further boost the performance of finetuned BERT mod-

els, we do not see the same performance gain when adding samples in few-shot prompting.

3.3 New Zealand Parliamentary Speech Classification (8-Class)

In this subsection, we study another example of 8-class classification. Specifically, we clas-

sify the speech transcripts from the New Zealand Parliament for the period from 1987 to

2002. The dataset originally comes from Osnabr¨ugge et al. (2021) and has 4,165 hand-

10

RoBERTa #200RoBERTa #500RoBERTa #1000Temp0.8 #0Temp0.2 #0Temp0.8 #1Temp0.2 #1Temp0.8 #2Temp0.2 #20.350.400.450.500.550.600.65Accuracy0.5390.5670.5820.4820.4780.4710.4880.4820.469Manifesto 8-Class Classificationcoded text snippets. In Osnabr¨ugge et al. (2021), the authors initially used the dataset

as a test set for cross-domain classification. Y. Wang (2023b) later split this dataset into

train, dev, and test to finetune a BERT model (RoBERT-base). From these 4,165 sam-

ples, we random sample 2,000 as the training set, 300 as the dev set, and another 300

as the test set.

In Table 3, we report the data distribution for our experiment. The

data is unbalanced among classes: Political System alone accounts for over a quarter of

the dataset, while Economy represents another 17%. The smallest category, External

Relations, comprises just 2-3%.

Table 3: Distribution in New Zealand Parliamentary Speech Datasets. Political System
alone accounts for over a quarter of the dataset, while Economy represents another 17%.
The smallest category, External Relations, comprises just 2-3%.

Topic
Economy
External Relations
Fabric Of Society
Freedom and Democracy
Other
Political System
Social Groups
Welfare and Quality Of Life
Total

Train
337 (16.85%)
45 (2.25%)
197 (9.85%)
255 (12.75%)
100 (5.0%)
541 (27.05%)
147 (7.35%)
378 (18.9%)
2,000

Dev
57 (19.0%)
7 (2.33%)
30 (10.0%)
34 (11.33%)
11 (3.67%)
75 (25.0%)
23 (7.67%)
63 (21.0%)
300

Test
51 (17.0%)
8 (2.67%)
32 (10.67%)
44 (14.67%)
14 (4.67%)
65 (21.67%)
26 (8.67%)
60 (20.0%)
300

In Figure 3, we report our experiment results. A few observations immediately stand

out. First, adding more training samples significantly enhances the performance of fine-

tuned BERT models. Second, few-shot prompting offers little to no improvement over

zero-shot prompting. Third, fine-tuning BERT models is considerably more effective than

prompting GPT models. For example, BERT models fine-tuned with 500 samples achieve

an accuracy of 57.6%, nearly 40% higher than all prompting methods. Furthermore, BERT

models fine-tuned with 1,000 samples are about 50% more accurate than prompting.

3.4 COVID-19 Policy Measure Classification (20-Class)

In this subsection, we evaluate the models’ performance on a 20-class classification task.

The dataset is in the domain of policy measures against COVID-19. It comes from Laurer

11

Figure 3: Finetuning BERT models substantially outperforms prompting GPT models in
the 8-class New Zealand Parliamentary Speech classification. While fine-tuning continues
to show significant improvement with the addition of more training samples, prompting
appears to gain no benefit from embedding extra samples into the prompts.

et al. (2024) and originally came from Cheng et al. (2020). The dataset consists of over

13,000 policy announcements across more than 195 countries and encompasses a total of

20 classes, including, for example, Curfew and External Border Restrictions. In Table 4,

we report the data distribution in our experiments. Some of the largest classes, such as

Health Resources and Restriction and Regulation of Businesses, each account for over 10%

of the dataset. In contrast, Anti-Disinformation Measures is the smallest class, comprising

less than 1% of the dataset.

We report our experiment results in Figure 4. When fine-tuning BERT models, we

consistently observe that increasing the number of labeled samples leads to improved per-

formance. When prompting GPT models, however, zero-shot prompting is doing as well

as if not better than few-shot prompting. If we compare finetuning and prompting, we ob-

serve that prompting GPT models performs at a similar level (65.8%) as finetuning BERT

models with 500 samples (65.7%). Prompting (65.8%) is substantially more accurate than

12

RoBERTa #200RoBERTa #500RoBERTa #1000Temp0.8 #0Temp0.2 #0Temp0.8 #1Temp0.2 #1Temp0.8 #2Temp0.2 #20.30.40.50.60.7Accuracy0.4900.5760.6170.4100.4060.4130.4100.4100.406New Zealand Parliament 8-Class ClassificationTable 4: 20-class distribution of the COVID-19 Policy Measure dataset. Some of the larger
classes include Health Resources and Restriction and Regulation of Businesses, each ac-
counting for over 10% of the dataset. In contrast, Anti-Disinformation Measures and Dec-
laration of Emergency each account for less than 2% of the dataset.

Topic
Anti-Disinformation Measures
COVID-19 Vaccines
Closure and Regulation of Schools
Curfew
Declaration of Emergency
External Border Restrictions
Health Monitoring
Health Resources
Health Testing
Hygiene
Internal Border Restrictions
Lockdown
New Task Force, Bureau or Admin. Configuration 48 (2.4%)
Other Policy Not Listed Above
Public Awareness Measures
Quarantine
Restriction and Regulation of Businesses
Restriction and Regulation of Govt. Services
Restrictions of Mass Gatherings
Social Distancing
Total

Test
3 (1.0%)
9 (3.0%)

Dev
Train
0 (0.0%)
15 (0.75%)
6 (2.0%)
66 (3.3%)
16 (5.33%) 13 (4.33%)
114 (5.7%)
8 (2.67%)
6 (2.0%)
44 (2.2%)
4 (1.33%)
33 (1.65%)
6 (2.0%)
21 (7.0%)
119 (5.95%) 21 (7.0%)
65 (3.25%)
10 (3.33%)
12 (4.0%)
283 (14.15%) 38 (12.67%) 29 (9.67%)
9 (3.0%)
12 (4.0%)
56 (2.8%)
10 (3.33%)
4 (1.33%)
48 (2.4%)
12 (4.0%)
9 (3.0%)
61 (3.05%)
10 (3.33%) 12 (4.0%)
83 (4.15%)
10 (3.33%) 9 (3.0%)

101 (5.05%) 13 (4.33%) 21 (7.0%)
23 (7.67%) 21 (7.0%)
150 (7.5%)
111 (5.55%) 21 (7.0%)
14 (4.67%)
227 (11.35%) 34 (11.33%) 40 (13.33%)
17 (5.67%) 20 (6.67%)
138 (6.9%)
139 (6.95%) 25 (8.33%) 19 (6.33%)
17 (5.67%) 16 (5.33%)
99 (4.95%)
300
2000

300

finetuning with 200 samples (55.3%) but is not nearly as good as finetuning with 1,000

samples (71.3%).

3.5 Speech Classification (22-Class)

Following the 20-class classification task on COVID-19 policy measures, this subsection

compares the performance of fine-tuning BERT models with prompting GPT models in a

22-class classification task focused on State of the Union speeches. This task could pose

a greater challenge for both approaches, particularly for fine-tuning, for two key reasons.

First, with a fixed number of training samples, a larger number of classes means that each

13

Figure 4: Fine-tuning BERT models with 500 samples performs comparably to prompting
GPT models in the 20-class COVID-19 policy measure classification task. With fine-tuning
continuing to show significant improvement with the addition of more training samples,
fine-tuning with 1,000 samples clearly has an edge over prompting, which apparently is
not benefiting from the extra added samples.

class would have fewer samples on average. Second, the fine-tuned BERT model now has

significantly more classes to choose from, increasing the likelihood of errors. This second

challenge also applies to prompting GPT models.

We use the dataset from Laurer et al. (2024). The data consists of 22 classes: Agri-

culture, Civil Rights, Culture, Defense, Domestic Commerce, Education, Energy, Environ-

ment, Foreign Trade, Government Operations, Health, Housing, Immigration, International

Affairs, Labor, Law and Crime, Macroeconomics, Other, Public Lands, Social Welfare,

Technology, Transportation. Some of the larger classes are Defense (14%), International

Affairs (14%), and Macroeconomics (15%). Some minor classes, such as Immigration and

Technology, account for 1% or less of the data (Table 5). As a result, when we sample

200 samples for finetuning BERT models, there are only a couple of samples for these

minor classes (Laurer et al., 2024). Quantitatively, that is not dissimilar to the number of

samples we use for few-shot prompting.

14

RoBERTa #200RoBERTa #500RoBERTa #1000Temp0.8 #0Temp0.2 #0Temp0.8 #1Temp0.2 #1Temp0.8 #2Temp0.2 #20.40.50.60.70.8Accuracy0.5530.6570.7130.6530.6580.6430.6420.6460.646COVID-19 Policy Measure 20-Class ClassificationTable 5: 22-class distribution of the State of the Union Speech Dataset. Some of the larger
classes are Defense, International Affairs, and Macroeconomics. Several topics account for
1% or less of the dataset, highlighting the uneven distribution of the data.

Topic
Agriculture
Civil Rights
Culture
Defense
Domestic Commerce
Education
Energy
Environment
Foreign Trade
Government Operations
Health
Housing
Immigration
International Affairs
Labor
Law and Crime
Macroeconomics
Other
Public Lands
Social Welfare
Technology
Transportation
Total

Train
36 (2%)
47 (2%)
0 (0%)
281 (14%)
33 (2%)
94 (5%)
28 (1%)
31 (2%)
53 (3%)
104 (5%)
79 (4%)
30 (1%)
20 (1%)
282 (14%)
52 (3%)
67 (3%)
306 (15%)
318 (16%)
24 (1%)
60 (3%)
27 (1%)
28 (1%)
2000

Dev
9 (3%)
6 (2%)
0 (0%)
38 (13%)
3 (1%)
13 (4%)
3 (1%)
7 (2%)
8 (3%)
7 (2%)
11 (4%)
2 (1%)
2 (1%)
52 (17%)
8 (3%)
13 (4%)
54 (18%)
42 (14%)
5 (2%)
10 (3%)
3 (1%)
4 (1%)
300

Test
6 (2%)
7 (2%)
1 (0%)
34 (11%)
8 (3%)
9 (3%)
6 (2%)
1 (0%)
8 (3%)
18 (6%)
11 (4%)
7 (2%)
2 (1%)
37 (12%)
23 (8%)
11 (4%)
48 (16%)
51 (17%)
2 (1%)
8 (3%)
2 (1%)
0 (0%)
300

We report our experiment results in Figure 5. Regarding finetuning BERT models,

our typical observation holds true: increasing the number of training samples from 200 to

500 and then to 1,000 consistently results in performance improvements. When prompt-

ing GPT models, we observe that while the difference in performance between 1-shot and

2-shot prompting is minimal, the improvement from zero-shot to few-shot prompting is

significant, with accuracy increasing from 0.509 to 0.590. Between finetuning BERT and

prompting GPT, we note that zero-shot prompting outperforms finetuning with 200 sam-

ples and that few-shot prompting is equal to or slightly better than finetuning BERT

models with 500 or 1,000 samples.

15

Figure 5: In the 22-class classification of the US State of the Union speeches, zero-shot
prompting outperforms finetuning BERT with 200 samples. 1-shot and 2-shot prompting
perform similarly to finetuning with 500 and 1,000 samples, respectively.

4 Discussions and Future Research

The empirical results consistently demonstrate that fine-tuning BERT models is the pre-

ferred approach for maximizing model accuracy when researchers have access to around

1,000 data points. However, while prompting may not achieve the same level of perfor-

mance, it offers competitive results, particularly when the training set includes only a few

hundred samples. In this section, we delve deeper into these findings, discussing them in

terms of performance, ease of use, cost considerations, and potential future directions.

4.1 Performance

After comparing the performance of fine-tuning BERT models and prompting GPT models

across binary, 8-class, and 20+ class classifications, several key observations immediately

stand out. First and foremost, in general both finetuning and prompting represent viable

solutions to the data scarcity issue and both offer strong performance with limited labeled

16

RoBERTa #200RoBERTa #500RoBERTa #1000Temp0.8 #0Temp0.2 #0Temp0.8 #1Temp0.2 #1Temp0.8 #2Temp0.2 #20.400.450.500.550.60Accuracy0.4780.5630.5780.5090.5090.5770.5900.5770.58622-Class Speech Classificationdata. Second, when comparing the performance of these two approaches, we note that

for certain tasks, binary classifications in particular, zero-shot and few-shot prompting

can already do as well as BERT finetuning. Third, if the goal is model accuracy, then

researchers will have better success with finetuning. In Table 6, we summarize the com-

parisons between finetuning BERT and prompting GPT in terms of the required amount

of data and optimal task difficulty. From a practical standpoint, since political scientists

often use classification results as input for regression analysis (Torres, 2023; Fong & Tyler,

2021), both approaches enable researchers to quickly start experimenting with new ideas,

even with minimal or no labeled data (Laurer et al., 2024; Y. Wang, 2023b; Longpre et al.,

2020). This is especially true for zero-shot and few-shot prompting, which we will explore

next.

Table 6: Selection of BERT and GPT Models Based on Data Availability and Task Diffi-
culty.

Fine-tuning BERT
Prompting GPT

Required Data Amount
Small
Minimal to None

Optimal Task Difficulty
High
Low

4.2 Ease of Use

In terms of ease to use, finetuning BERT models is more complicated than zero-shot or

few-shot prompting GPT models. In terms of data preparation, both approaches represent

an advancement over classical methods, since there is no more need for data preprocessing,

such as stop word removal and stemming (Y. Wang et al., 2022). For finetuning BERT

models, we need to split the dataset into train, dev, and test. For prompting, we only

need the test set (and an optional dev set). When it comes to training, fine-tuning has

been greatly simplified by frameworks like Huggingface (Laurer et al., 2024). However,

researchers still need to write some boilerplate code. Additionally, there is the need to

adjust quite a few parameters, with the learning rate being particularly important (Arnold

et al., 2024; Goodfellow et al., 2016). By contrast, prompting with GPT models is done

17

via API calls and requires little code. Temperature is arguably the only hyperparameter

that researchers need to deal with (Gilardi et al., 2023).

Table 7: Comparing Finetuning BERT Models and Prompting GPT Models in Terms of
Ease of Use

Finetuning BERT
Prompting GPT

Data Processing
Medium
Easy

Training
Medium
None

Evaluation
Easy
Easy

4.3 Cost

In addition to performance and ease of use, a third dimension to consider is the financial

cost of using these models.9 The cost of fine-tuning BERT models primarily lies in GPU

time: the time spent using GPUs for fine-tuning and evaluation/inference. As we increase

the number of training samples from 200 to 500 and then to 1,000, we will linearly increase

the training time and thus the cost. As an example, in the 20-class classification of COVID-

19 policy measures, training a BERT model with 200 samples takes three and a half minute.

For 500 samples, it takes five and a half minute. For 1000 samples, it takes eight and a

half minute. During evaluation (inference), each sample takes about 10 milliseconds. As

we increase the number of test samples, we linearly increase the cost. Since fine-tuning is

performed only once, the associated costs can be considered sunk. In contrast, prompting

does not involve fine-tuning, so there are no sunk costs. However, each individual API call

for prompting is typically more expensive than the cost of BERT inferencing, at least for

now. Additionally, the cost of prompting GPT models is tied to the number of tokens in

the prompt—the more tokens per request, the higher the cost.

In Figure 6, we compare the cost of finetuning BERT models with that of prompting

GPT models. Our comparison is based on the following assumptions: (1) the cost of

running an A100 GPU is $1.20 per hour, and (2) the cost of prompting GPT-4o is $5

per million tokens.10 The black dashed line represents the cost of using fine-tuned BERT

9Researchers may also need to consider the cost of annotation, which is often not trivial (Gilardi et al.,

2023).

10For more details on fine-tuning and GPU costs, please visit https://colab.research.google.com/signup.

18

Figure 6: When fine-tuning BERT models, there is a sunk cost associated with the initial
fine-tuning process. However, this approach proves to be more economical during inference.
In contrast, prompting incurs no such sunk cost but has a steeper cost curve for inference.
In this experiment, the cost of zero-shot prompting catches up with fine-tuning after
processing 150-200 samples, while the cost of 2-shot prompting quickly surpasses that of
fine-tuning after just a few API calls.

models. While there is an initial sunk cost associated with fine-tuning on 1,000 samples,

the resulting model demonstrates a relatively flat cost slope. During inference, the fine-

tuned model incurs additional computational costs at a rate of 100 samples per second. For

zero-shot prompting (green solid line), there is no initial cost, but it has a steeper slope,

intersecting with the fine-tuning cost curve at 150-200 test samples. Two-shot prompting

is the most expensive approach. In this policy measure classification task with 20 classes,

each prompt includes 40 additional examples (two for each class). Consequently, the slope

is significantly steeper compared to zero-shot prompting. For a more detailed comparison,

interested readers may consider exploring other GPUs, such as the H100, and alternative

generative AI models such as Gemini Pro and GPT-4 mini.

For prompting and ChatGPT pricing, please see https://openai.com/api/pricing/.

19

050100150200250300Number of Test Samples01234Estimated Dollar Amount (USD)Cost Analysis of Finetuning and PromptingFinetuning with 1,000 SamplesZero-shot PromptingTwo-shot Prompting4.4 Future Directions

Natural language processing (NLP) and large language models are advancing rapidly. In

this section, we outline several emerging directions in NLP that hold significant promise

for enhancing political science research. Of the two approaches, fine-tuning BERT models

is more mature, while prompting is still relatively new. For fine-tuning BERT models,

researchers could further explore mixed precision training to reduce the sunk cost, par-

ticularly when working with large datasets. To enhance the performance of GPT models,

researchers might investigate newer foundation models, advanced prompting techniques

such as chain-of-thought and self-consistency (Wei, Wang, et al., 2022; X. Wang et al.,

2023), and more effective sample selection methods based on criteria like semantic simi-

larity (J. Liu et al., 2022; An et al., 2023). These strategies could not only improve the

effectiveness of prompting GPT models but also make them more economically compelling.

5 Conclusion

Quantitative text analysis plays a prominent role in political science research. Recent

advancements, particularly in large language models, have provided researchers with pow-

erful new tools to address both existing and emerging challenges. In this article, we have

explored the potential of using GPT-based models as an alternative solution to the data

scarcity issue, comparing their performance to that of fine-tuning BERT models, which

remains the state of the art. Through extensive experiments, we have demonstrated that

zero-shot and few-shot learning with GPT-based models can sometimes serve as an ef-

fective alternative to fine-tuning BERT models, especially when the number of classes is

small, but fine-tuning BERT models remains the overall go-to method for classification.

In addition to performance, we have also compared these approaches in terms of ease of

use and cost. While prompting GPT models is significantly easier to use than fine-tuning

BERT models, it also proves to be more expensive. We believe our findings will be valuable

to researchers involved in quantitative text analysis.

20

Data Availability

All our data and code will be made publicly available and posted on Harvard Dataverse

upon the paper’s acceptance.

Competing interests

The author(s) declare no competing interests.

Ethical approval

This article does not contain any studies with human participants performed by any of

the authors.

Informed consent

This article does not contain any studies with human participants performed by any of

the authors.

References

Adams, L. C., Truhn, D., Busch, F., Kader, A., Niehues, S. M., Makowski, M. R., &

Bressem, K. K.

(2023). Leveraging gpt-4 for post hoc transformation of free-text

radiology reports into structured reporting: A multilingual feasibility study. Radiology.

doi: https://doi.org/10.1148/radiol.230725

An, S., Zhou, B., Lin, Z., Fu, Q., Chen, B., Zheng, N., . . . Lou, J.-G. (2023). Skill-

based few-shot selection for in-context learning. In Proceedings of the 2023 conference

on empirical methods in natural language processing (emnlp).

21

Argyle, L. P., Bail, C. A., Busby, E. C., Gubler, J. R., Howe, T., Rytting, C., . . . Wingate,

D. (2023). Leveraging ai for democratic discourse: Chat interventions can improve online

political conversations at scale. Proceedings of the National Academy of Sciences.

Argyle, L. P., Busby, E. C., Fulda, N., Gubler, J. R., Rytting, C., & Wingate, D. (2023).

Out of one, many: Using language models to simulate human samples. Political Analysis,

1–15. doi: 10.1017/pan.2023.2

Arnold, C., Biedebach, L., K¨upfer, A., & Neunhoeffer, M. (2024). The role of hyperpa-

rameters in machine learning models and how to tune them. Political Science Research

and Methods.

Barber´a, P., Boydstun, A. E., Linn, S., McMahon, R., & Nagler, J. (2021). Automated

text classification of news articles: A practical guide. Political Anslysis.

Bestvater, S. E., & Monroe, B. L. (2023). Sentiment is not stance: Target-aware opinion

classification for political text analysis. Political Analysis, 31 (2), 235–256. doi: 10.1017/

pan.2022.10

Bisbee, J., Clinton, J. D., Dorff, C., Kenkel, B., & Larson, J. M.

(2024). Synthetic

replacements for human survey data? the perils of large language models. Political

Analysis.

Brown, T., Mann, B., Ryder, N., Subbiah, M., Kaplan, J. D., Dhariwal, P., . . . Amodei, D.

(2020). Language models are few-shot learners. 34th Conference on Neural Information

Processing Systems (NeurIPS 2020).

Chang, C., & Masterson, M. (2020). Using word order in political text classification with

long short-term memory models. Political Analysis.

Chaturvedi, R., & Chaturvedi, S. (2023). It’s all in the name: A character-based approach

to infer religion. Political Analysis.

22

Cheng, C., Barcel´o, J., Hartnett, A. S., Kubinec, R., & Messerschmidt, L. (2020). COVID-

19 Government Response Event Dataset (CoronaNet v.1.0). Nature Human Behaviour ,

4 , 756–768. doi: 10.1038/s41562-020-0909-7

Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2019). Bert: Pre-training of deep

bidirectional transformers for language understanding. Proceedings of NAACL-HLT ,

4171-4186.

Diermeier, D., Godbout, J.-F., Yu, B., & Kaufmann, S. (2011). Language and ideology in

congress. British Journal of Political Science.

D’Orazio, V., Landis, S. T., Palmer, G., & Schrodt, P. (2014). Separating the wheat

from the chaff: Applications of automated document classification using support vector

machines. Political Anslysis.

Fong, C., & Tyler, M. (2021, October). Machine learning predictions as regression covari-

ates. Political Analysis, 29 (4), 467–484.

Gilardi, F., Alizadeh, M., & Kubli, M. (2023). Chatgpt outperforms crowd-workers for

text-annotation tasks. Proceedings of the National Academy of Sciences.

Goodfellow, I., Bengio, Y., & Courville, A. (2016). Deep learning. The MIT Press.

Hastie, T., Tibshirani, R., & Friedman, J. (2009). The elements of statistical learning:

Data mining, inference, and prediction. Springer.

Hu, Y., Hosseini, M., Parolin, E. S., Osorio, J., Khan, L., Brandt, P. T., & D’Orazio, V. J.

(2022). Conflibert: A pre-trained language model for political conflict and violence.

Proceedings of the 2022 Conference of the North American Chapter of the Association

for Computational Linguistics.

Huang, F., Kwak, H., & An, J. (2023). Is chatgpt better than human annotators? potential

and limitations of chatgpt in explaining implicit hate speech. WWW ’23 Companion:

Companion Proceedings of the ACM Web Conference 2023 .

23

H¨affner, S., Hofer, M., Nagl, M., & Walterskirchen, J. (2023). Introducing an interpretable

deep learning approach to domain-specific dictionary creation: A use case for conflict

prediction. Political Analysis, 1–19. doi: 10.1017/pan.2023.7

Kaufman, A. R. (2024). Selecting more informative training sets with fewer observations.

Political Analysis.

Kaufman, A. R., & Klevs, A. (2022). Adaptive fuzzy string matching: How to merge

datasets with only one (messy) identifying field. Political Analysis.

Kim, T.

(2022). Violent political rhetoric on twitter. Political Science Research and

Methods.

Kjell, O., Giorgi, S., & Schwartz, H. A. (2023). The text-package: An r-package for analyz-

ing and visualizing human language using normal language processing and transformers.

Psychological Methods.

Kjell, O. N., Kjell, K., & Schwartz, H. A. (2024). Beyond rating scales: With targeted

evaluation, large language models are poised for psychological assessment. Psychiatry

Research.

Korinek, A. (2023). Generative ai for economic research: Use cases and implications for

economists. Journal of Economic Literature.

Lai, A., Brown, M. A., Bisbee, J., Tucker, J. A., Nagler, J., & Bonneau, R.

(2024).

Estimating the ideology of political youtube videos. Political Analysis.

Lan, Z., Chen, M., Goodman, S., Gimpel, K., Sharma, P., & Soricut, R. (2020). ALBERT:

A Lite BERT for Self-supervised Learning of Language Representations. ICLR.

Laurer, M., van Atteveldt, W., Casas, A., & Welbers, K. (2024). Less annotating, more

classifying: Addressing the data scarcity issue of supervised machine learning with deep

transfer learning and bert-nli. Political Analysis.

24

Lee, J., Yoon, W., Kim, S., Kim, D., Kim, S., So, C. H., & Kang, J. (2019). Biobert:

A pre-trained biomedical language representation model for biomedical text mining.

Bioinformatics, 36 .

Liu, J., Shen, D., Zhang, Y., Dolan, B., Carin, L., & Chen, W. (2022, January). What

makes good in-context examples for gpt-3? In Deelio 2022 - deep learning inside out:

3rd workshop on knowledge extraction and integration for deep learning architectures,

proceedings of the workshop.

Liu, Y., Ott, M., Goyal, N., Du, J., Joshi, M., Chen, D., . . . Stoyanov, V.

(2019).

RoBERTa: A Robustly Optimized BERT Pretraining Approach. arXiv:1907.11692 .

Longpre, S., Wang, Y., & DuBois, C. (2020). How Effective is Task-Agnostic Data Aug-

mentation for Pretrained Transformers? Findings of the Association for Computational

Linguistics: EMNLP 2020 .

Mei, Q., Xie, Y., Yuan, W., & Jackson, M. O. (2024). A turing test of whether ai chatbots

are behaviorally similar to humans. Proceedings of the National Academy of Sciences.

Mikolov, T., Sutskever, I., Chen, K., Corrado, G., & Dean, J. (2013). Distributed rep-

resentations of words and phrases and their compositionality. NIPS’13: Proceedings of

the 26th International Conference on Neural Information Processing Systems.

Muchlinski, D., Siroky, D., He, J., & Kocher, M. (2016). Comparing Random Forest with

Logistic Regression for Predicting Class-Imbalanced Civil War Onset Data. Political

Analysis, 24 (1), 87-103.

Nielbo, K. L., Karsdorp, F., Wevers, M., Lassche, A., Baglini, R. B., Kestemont, M.,

& Tahmasebi, N. (2024, April). Quantitative text analysis. Nature Reviews Methods

Primers, 4 , Article 25.

Osnabr¨ugge, M., Ash, E., & Morelli, M. (2021). Cross-domain topic classification for

political texts. Political Analysis.

25

Peng, H., Qiu, H. S., Fosse, H. B., & Uzzi, B. (2024). Promotional language and the

adoption of innovative ideas in science. Proceedings of the National Academy of Sciences

of the United States of America.

Pennington, J., Socher, R., & Manning, C.

(2014). Glove: Global vectors for word

representation. Proceedings of the 2014 Conference on Empirical Methods in Natural

Language Processing (EMNLP).

Radford, A., Wu,

J., Child, R., Luan, D., Amodei, D., & Sutskever,

I.

(2019).

Language models are unsupervised multitask learners.

Ope-

nAI .

Retrieved from https://www.openai.com/research/language-models-are

-unsupervised-multitask-learners

Rai, S., Stade, E. C., Giorgi, S., Francisco, A., Ungar, L. H., Curtis, B., & Guntuku, S. C.

(2024). Key language markers of depression on social media depend on race. Proceedings

of the National Academy of Sciences, 121 (14), e2319837121. Retrieved from https://

www.pnas.org/doi/abs/10.1073/pnas.2319837121 doi: 10.1073/pnas.2319837121

Rheault, L., & Cochrane, C. (2019). Word embeddings for the analysis of ideological

placement in parliamentary corpora. Political Analysis.

Rodman, E. (2019). A timely intervention: Tracking the changing meanings of political

concepts with word vectors. Political Analysis.

Rodriguez, P. L., & Spirling, A. (2022). Word embeddings what works, what doesn’t, and

how to tell the difference for applied research. Journal of Politics.

Simchon, A., Hadar, B., & Gilead, M. (2023). A computational text analysis investigation

of the relation between personal and linguistic agency. Communications Psychology.

Strachan, J. W. A., Albergo, D., Borghini, G., Pansardi, O., Scaliti, E., Gupta, S., . . .

Becchio, C.

(2024). Testing theory of mind in large language models and humans.

Nature Human Behaviour .

26

Torres, M. (2023). A framework for the unsupervised and semi-supervised analysis of

visual frames. Political Analysis.

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., . . . Polo-

sukhin, I. (2017). Attention Is All You Need. 31st Conference on Neural Information

Processing Systems.

Wang, X., Wei, J., Schuurmans, D., Le, Q., Chi, E. H., Narang, S., . . . Zhou, D. (2023).

Self-consistency improves chain of thought reasoning in language models. In Proceedings

of the International Conference on Learning Representations (ICLR 2023).

Wang, Y. (2019a). Comparing Random Forest with Logistic Regression for Predicting

Class-Imbalanced Civil War Onset Data: A Comment. Political Analysis, 21 (1), 107-

110.

Wang, Y. (2019b). Single training dimension selection for word embedding with pca. Pro-

ceedings of the 2019 Conference on Empirical Methods in Natural Language Processing

and the 9th International Joint Conference on Natural Language Processing (EMNLP-

IJCNLP).

Wang, Y. (2023a). On finetuning large language models. Political Analysis.

Wang, Y. (2023b). Topic classification for political texts with pretrained language models.

Political Analysis.

Wang, Y. (2024). Large language models for depression prediction. Proceedings of the

National Academy of Sciences.

Wang, Y., Feng, Y., Hong, Z., Berger, R., & Luo, J. (2017). How polarized have we

become? a multimodal classification of trump followers and clinton followers. Social

Informatics.

Wang, Y., & Qu, W. (2024). A tutorial on the pretrain-finetune paradigm for natural

language processing. arXiv:2403.02504 .

27

Wang, Y., Tian, J., Yazar, Y., Ones, D. S., & Landers, R. N. (2022). Using natural lan-

guage processing and machine learning to replace human content coders. Psychological

Methods.

Wang, Y., Yuan, J., & Luo, J. (2015). America tweets china: A fine-grained analysis

of the state and individual characteristics regarding attitudes towards china.

IEEE

International Conference on Big Data.

Wei, J., Tay, Y., Bommasani, R., Raffel, C., Zoph, B., Borgeaud, S., . . . Fedus, W.

(2022). Emergent abilities of large language models. Transactions on Machine Learning

Research.

Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., . . . Zhou, D. (2022).

Chain-of-thought prompting elicits reasoning in large language models. In Advances in

neural information processing systems 35 (neurips 2022) main conference track.

Widmann, T., & Wich, M. (2023). Creating and comparing dictionary, word embedding,

and transformer-based models to measure discrete emotions in german political text.

Political Analysis.

Zhang, Y., Lyu, H., Liu, Y., Zhang, X., Wang, Y., & Luo, J. (2021). Monitoring de-

pression trends on twitter during the covid-19 pandemic: Observational study. JMIR

Infodemiology.

Zhong, Q., Ding, L., Liu, J., Du, B., & Tao, D. (2023). Can chatgpt understand too? a

comparative study on chatgpt and fine-tuned bert. arXiv:2302.10198 .

Ziems, C., Held, W., Shaikh, O., Chen, J., Zhang, Z., & Yang, D. (2024, March). Can large

language models transform computational social science? Computational Linguistics,

50 (1).

28

