Electronic copy available at: https://ssrn.com/abstract=4234381

© 2022 International Monetary Fund

WP/22/192

IMF Working Paper

European Department

Promoting Innovation: The Differential Impact of R&D Subsidies

Prepared by Reda Cherif, Fuad Hasanov, Christoph Grimpe, and Wolfgang Sofka1

Authorized for distribution by Ivanna Vladkova Hollar

September 2022

IMF Working Papers describe research in progress by the author(s) and are published to elicit
comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s)
and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

ABSTRACT: We investigate the effect of R&D subsidies on firms’ innovation by ownership, industry, and
firm size using German firm-level data. The impact of R&D subsidies is heterogeneous across industries for
multinational corporations (MNCs) and domestic firms while it does not differ substantially by firm size.
Domestic firms have a larger response in R&D spending in low-tech manufacturing, knowledge-intensive
services, and technological services while the response of domestic and foreign MNCs is broadly similar
and is greater in medium-tech and high-tech manufacturing. Foreign MNC subsidiaries’ response in terms of
patents is greater than that of domestic MNCs in most industries.

JEL Classification Numbers:

H25, H32, 030, 025

Keywords:

Innovation; patents; research and development; R&D; subsidies;
multinationals; investment; technology policy

Author’s E-Mail Address:

acherif@imf.org; fhasanov@imf.org; cg.si@cbs.dk; ws.si@cbs.dk

1

Cherif and Hasanov: IMF. Grimpe: Copenhagen Business School and ZEW Leibniz Centre for European Economic Research.
Sofka: Copenhagen Business School and University of Liverpool Management School. The authors thank Grazia Santangelo for
excellent feedback and David Amaglobeli, Rodrigo Cerda, Ruud de Mooij, Mauricio Soto, and Yue Zhou for helpful comments.
The work on this paper started when Wolfgang Sofka was a Visiting Scholar in the Institute for Capacity Development of the
International Monetary Fund. He thanks the IMF for its hospitality. We are grateful to Jocelyne Vanderhaegen for formatting the
paper. All errors are our own.

Electronic copy available at: https://ssrn.com/abstract=4234381

©International Monetary Fund. Not for Redistribution3

Contents

Abstract ...........................................................................................................................................................

 2

Introduction ........................................................................................................ Error! Bookmark not defined.

Data, Descriptive Statistics, and Empirical Methodology……...………………………………………………6

Results………………………

…………………………………………………………………………………………17

Conclusion ....................................................................................................................................................

 21

References ....................................................................................................................................................

 22

Appendixes……………………………………………………………………………………………………………2

7

TABLES
1. R&D Spending (in million euros): Descriptive Statistics by Ownership, Industry, and Size………………..
2. Patent Applications in the Next 5 Years: Descriptive Statistics by Ownership, Industry, and Size………..
3.
4. Patents: Weighted Regressions, Matched Sample…………………………………………………………….

10
11
 R&D Spending: Weighted Regressions, Matched Sample……………………………………………………. 18
19

 FIGURES
1. R&D Spending (log[1+R&D]) by Ownership…………………………………………………………………….
2. R&D Spending (log[1+R&D]) by Ownership and Subsidy (=1)…………………………………………….…..
3. R&D Spending (log[1+R&D]) by Size and Subsidy (=1)………………………………………………….........
4. R&D Spending (log[1+R&D] and 5-Year Ahead Patents(log[1+Patents]) by Ownership and Subsidy

12
12
13

(Red)……………………………………………………………….………………………………………...

.13 5. R&D Spending (log[1+R&D]) and 5-Year Ahead Patents (log[1+Patents]) by Industry and Subsidy

(Red

)……...………………..……………………………………………………………………………...…14

6. R&D Spending (log[1+R&D]) and 5-Year Ahead Patents (log[1+Patents]) by Size and Subsidy

(Red)……………..…………………………………………………………………….………………….….

14

Electronic copy available at: https://ssrn.com/abstract=4234381

©International Monetary Fund. Not for Redistribution4

Introduction

Innovation is key to economic growth, and governments are keen to promote innovation using various

tools at their disposal. Research and development (R&D) activities represent an important ingredient in the
innovation process, and a standard tool used by government to encourage it is R&D subsidies. In this context,
it is important for policymakers to know how effective R&D subsidies are beyond the average or aggregate
effect. Indeed, it would be beneficial to know if the subsidy impact is differential depending on the ownership
type (e.g., foreign owned vs. domestic), firm size, and industry (Blanes & Busom, 2004). This could help focus
scarce resources while increasing the overall impact.

In this paper, using German firm-level data, covering the 2000s, we study the effect of R&D subsidies

on innovation inputs such as R&D spending and outputs such as patents. We further study whether R&D
subsidies have a differential effect on the subsidiaries of foreign multinational companies (MNCs) vs. domestic
MNCs and domestic firms, whether the firm size matters, and whether the effect of subsidies differs by industry.
We use a treatment model to identify the effect of R&D subsidies. Identification requires modeling the
counterfactual, that is, how firms would have engaged in innovation activities had they not received any
subsidy. We employ a propensity score matching and regressions on a matched sample to estimate the
parameters of interest in a cross-section of firms.

The empirical evidence suggests that subsidies increase R&D spending compared to the comparable

firms that do not receive subsidies2, and moreover, result in higher future patenting activity. We find that the
effect of R&D subsidies on R&D spending is broadly similar for foreign MNC subsidiaries and domestic MNCs.
In contrast, there are significant differences in the effects on MNCs and domestic firms across industries, but
not by firm size. The impact on R&D spending is larger for MNCs in medium- and high-tech manufacturing than
for domestic firms but is lower in low-tech manufacturing and some service industries. The subsidy’s effect on
future patents is bigger for MNCs than domestic firms and interestingly, is bigger for foreign MNCs than
domestic MNCs in most industries except for medium-tech manufacturing.

There are several reasons as to why R&D subsidies would increase the innovation effort and

performance of firms. The alleviation of financial constraints would, for example, increase R&D and
consequently, patenting activity. The fact that MNCs increase R&D spending more in certain industries and
patenting activity in general than domestic firms, suggests that competing in international markets in medium-
and high-tech manufactures requires a lot of innovation. The higher patenting of foreign MNCs compared to
domestic MNCs could suggest more efficient use or allocation of resources toward patentable technologies or a
signaling toward headquarters to pursue more innovation in a foreign location. In fact, pursuing more innovation
at the technological frontier, resulting in better innovation outcomes like patenting, could be the result of
knowledge spillovers and technology transfers across the MNC global network (Niosi, 1999; Cantwell and
Mudambi, 2005; Un and Cuervo-Cazurra, 2008; Gelman and Imbens, 2013; Santangelo et al., 2016; Cantwell,
2017).

Economic theory provides a justification for the government’s support of firms’ innovation activities.

Firms tend to underinvest in R&D spending due to a variety of market failures (e.g., Arrow 1962; Klette et al.,
2000). Positive externalities such as knowledge spillovers, imperfect information about future returns, and
market frictions as well as resource constraints would produce less than socially optimal investment and

2 Given that the amount of the subsidy is not available in the dataset, we have evidence that the multiplier on R&D spending is

positive but not necessarily greater than one.

Electronic copy available at: https://ssrn.com/abstract=4234381

©International Monetary Fund. Not for Redistribution

5

innovation activities (Bozeman, 2000; David et al., 2000a; Feldman and Kelley, 2006; Ceh, 2009; Rigby and
Ramlogan, 2012; Lazzarini, 2015; Holmes et al., 2016). In addition, governments may also intervene to tackle
potential systemic problems in the innovation ecosystem (Salter and Martin, 2001). These include technological
transitions, lock-in problems due to an excessive focus on existing technologies, and innovation network
deficiencies (Chaminade and Edquist, 2008). The system of innovation approach emphasizes the importance
of innovation networks in which firms do not innovate in isolation but continuously interact with other innovation
agents such as other firms, universities, or public research organizations (Lundvall, 1992).

Although there is a debate about the effectiveness of R&D programs, a large literature in economics
and management has mostly found a positive effect of these programs on innovation such as R&D spending
and patents (Czarnitzki and Toole, 2007; Aerts & Schmidt, 2008; Gonzalez and Pazo, 2008; Zúñiga-Vicente et
al., 2014; Jaffe and Le, 2015; Howell, 2017). Subsidies could narrow the scope of firms’ innovation solutions
(Ely et al., 2014), increase the costs of R&D inputs such as wages of researchers (David et al., 2000b;
Clarysse et al., 2009), or prop up lagging firms in terms of innovation capacity rather than facilitate movement
of skilled labor to high-tech firms (Acemoglu et al., 2018).

More important, subsidies could potentially crowd out R&D spending, resulting in no increase in R&D

spending funded by firms, but the empirical evidence shows otherwise. Essentially, a zero multiplier implies
that the incentive effect of subsidies to engage in more R&D and eventually patenting activities is offset by the
reallocation of spending toward other activities that the freeing of firm resources allows after a subsidy receipt.
Prior literature, however, suggests that overall, there is no or only partial crowding out of R&D investments
(e.g., Jaffe and Le, 2015; Dimos and Pugh, 2016). Moreover, the elasticity of R&D to tax credits is equal to or
greater than one (e.g., Bloom, Griffith, and van Reenen, 2002; Rao, 2016), and benefits of tax incentives
exceed their costs (Lester and Warda, 2020). Targeted R&D subsidies could also encourage long-term
research such as cancer research (Budish, Roin, and Williams, 2015). R&D subsidies could also potentially
nudge subsidiaries of foreign MNCs to be more innovative (Birkinshaw and Hood, 1998; Cantwell and
Mudambi, 2005; Cantwell, 2017).

R&D support to firms has strong impact on innovation outcomes such as patents. R&D subsidies have

a statistically significant and economically large effect on patents and venture capital investment, enabling
proof-of-concept that would not have been financially possible otherwise (Howell, 2017). In the UK, there is
evidence that tax credits increase both patenting and citations (Dechezleprêtre, Einiö, Martin, Nguyen and van
Reenen, 2016) while R&D subsidies increase patenting in Italy (Bronzini and Piselli, 2016). Tax credits also
increase product and process innovation (Czarnitzki et al., 2011; Cappelen et al., 2012) while R&D support
induces innovation collaboration among firms in the innovation ecosystem (e.g., OECD, 2006; Un et al., 2010;
Gök and Edler, 2012) and increases labor productivity of firms (Minniti and Venturini, 2017).

In terms of the heterogeneity of the R&D subsidy impact, Sofka et al. (2021), using German firm-level

data, find that both foreign and domestic MNCs increase R&D by the same amount but spend more on R&D
than domestic firms. In addition, foreign MNCs patent more than domestic MNCs and domestic firms. In
contrast, this paper explores the heterogeneous impact of subsidies by industry and firm size and assesses the
subsidy impact on R&D spending and patents using matched-firm regressions.

Electronic copy available at: https://ssrn.com/abstract=4234381

©International Monetary Fund. Not for Redistribution

6

Data, Descriptive Statistics, and Empirical
Methodology

Government R&D policies in Germany

Germany is an interesting case study to analyze R&D policy’s impact on innovation as it is both R&D

intensive and open. The R&D intensity of the German economy is about 3 percent of GDP, and R&D
expenditures have increased in both the government and business sectors (Sofka et al., 2018). Germany is
also a major foreign direct investor in terms of outflows (FDI outflow positions of about 44 percent of GDP in
2017) as well as inflows (FDI inflow positions of about 26 percent of GDP in 2017) (OECD, 2019). In addition,
MNCs have operated subsidiaries in Germany for a long time—for instance, investments by the US car
manufacturers General Motors and Ford date back to the first half of the 20th century (de Faria & Sofka, 2010).

Using the German firm-level data allows us to better control for various institutional conditions, allowing
us to focus on innovation implications of R&D policy. Germany has a stable institutional environment such as a
strong intellectual property rights regime (Park, 2008; Papageorgiadis and Sofka, 2020) as well as continuous
political support for innovation (EFI, 2017), which could positively affect R&D decisions. Germany provides
information and administrative support for potential foreign investors (Germany Trade and Invest, GATI.de) but
does not provide tax incentives. The country also has low restrictions for FDI, which could be beneficial for
MNCs. Interestingly, there are no R&D tax credits (Sofka et al., 2018), and government R&D subsidies are
application-based grants.

Research and innovation policy in Germany is the shared responsibility of the Federal Government

and the 16 State (“Laender”) Governments. At the federal level, the Federal Ministry of Education and
Research (BMBF) drives most policy initiatives while the Federal Ministry of Economics and Energy (BMWi) is
involved in specific areas (Sofka et al., 2018). Support for research and innovation in private firms is an
important component of Germany’s High-Tech Strategy and National Reform Programs (NRP, 2017). German
firms can apply for government support, following a formal application process and the guidelines of the
European Union (BMBF, 2016a). The typical support instrument is a grant.

There is a broad variety of support schemes in place, which are often operated by specialized project

management organizations (“Projekttraeger”) or associations like the German Federation of Industrial
Research Associations (AiF) “Otto von Guericke” (Sofka and Sprutacz, 2017). Other policy initiatives target
particular areas, e.g. IT security (BMBF, 2016c) or groups of firms like startups (e.g. High-Tech Startup Fund)
or small and medium sized firms (“Mittelstand”) (RKW, 2017). State governments complement the support
schemes of the federal government with their own measures (BMBF, 2016b). Often these measures reflect the
priorities or structures of the state. For example, the state of Baden-Wuerttemberg identifies sustainable
mobility as one of its research priority topics (Sofka et al., 2018).

Electronic copy available at: https://ssrn.com/abstract=4234381

©International Monetary Fund. Not for Redistribution

7

Data

Our dataset merges data from a representative innovation survey of firms in Germany with patent
statistics from the European Patent Office (EPO). The innovation survey used is the “Mannheim Innovation
Panel” (MIP), which is the German component of the Community Innovation Survey (CIS) of the European
Union. In contrast to many other CIS surveys, the MIP is conducted annually and allows the construction of an
unbalanced firm panel dataset. MIP respondents are responsible for innovation topics in their firms such as
CEOs, heads of R&D, or innovation management. They are asked to answer a comprehensive set of questions
about innovation inputs as well as outputs and to assign importance ratings (Criscuolo et al., 2005). The MIP
provides a stratified random sample, which is representative of firms in Germany. Non-response analyses show
no systematic distortions between responding and non-responding firms (Rammer et al., 2005), and Eurostat
(2009) considers CIS data from Germany as high quality.

We obtain firm-level data from the MIP for the years 2000, 2002, 2003, 2004, and 2006. The survey
waves for the years 2001 and 2005 are not useful for our analysis since they do not include questions on the
receipt of R&D subsidies, which is the central variable in our study. The firm information obtained from the MIP
is merged with the patent statistics from the EPO using assignee names and addresses. Patent statistics are
available for longer time periods than the survey data. We use patent applications between 1997 and 2011 to
construct the stock of patent applications prior to our survey period and patent applications for up to five years
after the survey year.

As a dependent variable, we use both R&D expenditures reported as well as the number of a firm’s

EPO patent applications in the subsequent five years. Since there is a significant time delay between investing
in R&D and arriving at a patentable invention and lengthy patent filing procedures, we use a five-year time
window for the patent applications variable. Longer time windows for measuring patent numbers increase the
risk of confounding factors.

Our central independent variables of interest are related to R&D subsidy (recipient vs. non-recipient),
firm ownership (foreign MNC, domestic MNC, and domestic firm) and size (large vs. small), and industry (low-,
medium- and high-tech manufacturing and various services). We use dummy variables to identify these groups
as follows: The survey respondents indicate whether their firms have received R&D subsidy from the German
government (state and/or federal level).3 We classify firms into a domestic firm, a domestic MNC, or a
subsidiary of a foreign MNC. The latter group is based on whether a firm is part of a company group with
headquarters abroad, in line with previous research on the innovation activities of foreign MNC subsidiaries
(Sofka et al., 2014). The firm size is based on the number of employees, and we split firms into three
categories: small with 50 or less employees, medium with 51-500 employees, and large with more than 500
employees. Lastly, we create 6 industry dummies based on grouped two-digit NACE codes, which have been
used frequently in previous innovation studies (Grimpe et al., 2017). These are low-tech manufacturing (e.g.,
food and textiles), medium-tech manufacturing (e.g., motor vehicles), high-tech manufacturing (e.g., medical
devices), distributive services (e.g., logistics), knowledge-intensive services (e.g., consulting), and
technological services (e.g., ICT-related services). The description is provided in the Appendix Table 1.

3 The survey does not provide information on the subsidy amount. The related question in the survey introduces government

subsidies as support for R&D and/or innovation with a short description. Then, respondents choose the funding source. Within
our context, a government R&D subsidy can be obtained from the federal government or one of the 16 state governments in
Germany in which the firm operates. Firms might obtain multiple grants from one or multiple government sources, but this
information is not available in the survey.

Electronic copy available at: https://ssrn.com/abstract=4234381

©International Monetary Fund. Not for Redistribution

8

We include additional control variables to capture other factors, which could potentially affect firm’s
innovation performance. We control for the overall size (number of employees) and age of firms (number of
years since founded in Germany). We also attempt to account for differences in firms’ innovation capacities by
adding firm’s patent applications in the year of observation since these inventions are likely to predate R&D
potentially induced by a government subsidy. We also add the number of patent applications of firms in the
three years preceding our sample, that is, 1997, 1998 and 1999, following Blundell et al. (2002). We capture
differences in the skills of employees by controlling for the share of employees with college education. We add
a dummy variable for whether the firm engages in R&D continuously. This variable is frequently used to
indicate the presence of a dedicated R&D department (Czarnitzki and Licht, 2006; Koehler et al., 2012). We
control for the degree of internationalization through the share of exports in firm sales since internationalization
has been found to affect a firm’s innovation activities (Cassiman and Golovko, 2011). Additionally, we include a
dummy variable for whether a firm engages in process innovation from the same survey since such activities
may affect its ability to patent. Lastly, we add time dummies to control for macroeconomic conditions.

Our dataset contains 6,052 firm observations after excluding firms that have not engaged in either
product or process innovation and with less than 5 employees. After dropping outliers, the sample includes
5,717 observations, of which 5,623 can be matched with control firms.4 In the patent regressions, the sample
without outliers has 5,353 observations, while the matched sample contains 5,263 observations. We perform
regressions on the full sample of 6,052 observations and the matched samples.5

Descriptive statistics

In the full sample, firms spend on average €1.6 million on R&D and file about 2.3 patents in a 5-year
period. About a third of them has received an R&D subsidy from state or federal governments, irrespective of
ownership or size. Large firms that receive a subsidy comprise about 12 percent of subsidy-receiving firms.
Small firms account for one-half of subsidy-receiving firms. This distribution is similar to the firm distribution
observed. About half of firms is small with less than 50 employees and about 13 percent is large firms with
more than 500 employees. The subsidy receipt differs by industry with about half of firms in high-tech
manufacturing and technological services receiving a subsidy while 10-15 percent of firms receive a subsidy in
knowledge-intensive and distributive services (Appendix Tables 3-5). About half of the firms are engaged in
continuous R&D activities and about two-thirds of them are process innovators. Foreign MNC subsidiaries
comprise about 10 percent of firms, similar to that of domestic MNCs, i.e., headquartered in Germany. About a
third of firms is in low-tech manufacturing, about 18 percent each in medium-tech and technological services,
10 percent each in high-tech manufacturing and knowledge-intensive services while 14 percent of firms is in
distributive services.

A cursory look at R&D spending reveals a few interesting patterns (Table 1). MNCs, whether domestic

or foreign MNC subsidiaries, do more R&D and file more patent applications than their domestic counterparts
while domestic MNCs tend to outperform their foreign MNC subsidiaries (Figure 1). Yet interestingly, R&D
spending in low-tech manufacturing by domestic firms is at par with foreign MNCs, albeit with far smaller
dispersion in the latter (similarly, in distributive services). In contrast, domestic MNCs do much more R&D in
low-tech manufacturing and in fact, on average exceed R&D in all the service industries, including

4 The extreme values of the following variables—firms above 100 years of age as well as observations above the 99th percentile of

the distributions of the number of employees, patent stock, share of R&D in sales, and exports—are dropped.
5 The estimation results between the matched sample and the unmatched sample that excludes outliers are similar.

Electronic copy available at: https://ssrn.com/abstract=4234381

©International Monetary Fund. Not for Redistribution

9

sophisticated ones, whether by domestic firms or foreign MNCs. The largest R&D spending of domestic MNCs
is in medium-tech manufacturing, and although the second largest spending industry is high-tech
manufacturing (both exceeding other industries by far), domestic MNCs, on average, slightly fall behind foreign
MNC subsidiaries in high-tech manufacturing.

The patents statistics tell us a largely similar story (Table 2). One difference is that foreign subsidiaries

tend to file more patents in low-tech manufacturing than domestic firms, but this pattern is reversed in
knowledge-intensive service industry.

Large firms (with more than 500 employees), not surprisingly, also outperform their smaller
counterparts (Tables 1-2). Even domestic large firms tend to spend more on R&D and file more patents on
average than smaller domestic MNCs and foreign MNC subsidiaries. Interestingly, small domestic MNCs tend
to file more patents than other firms, including even all medium-sized firms (but the sample size of medium-
sized MNCs is relatively small).

In addition, whether by industry, size, or ownership, firms receiving a R&D subsidy tend to have larger
R&D spending than firms that do not receive a subsidy (Figures 2-6). It is not just the large median or average
with only a few firms skewing the impact; rather, many firms have higher spending with a large mass not far
above the median of the distribution. The impact is much more pronounced in large firms, domestic MNCs, and
foreign MNC subsidiaries. Both domestic MNCs and foreign MNC subsidiaries, receiving a subsidy, have
greater R&D spending and patenting (Figure 4). Furthermore, firms in manufacturing and technological
services tend to do more R&D and patenting with a subsidy receipt (Figure 5). while a subsidy seems to
increase innovation activities of small firms substantially (Figure 6).

Electronic copy available at: https://ssrn.com/abstract=4234381

©International Monetary Fund. Not for Redistribution

10

Table 1.  R&D Spending (in million euros): Descriptive Statistics by Ownership, Industry, and
Size

Electronic copy available at: https://ssrn.com/abstract=4234381

IndustryMean0.542.000.550.69St. Dev.12.4616.921.3612.47Obs.15622041721938Mean0.4018.995.414.40St. Dev.1.4493.1545.9743.30Obs.7371911591087Mean0.3211.8415.924.19St. Dev.1.3451.2159.4130.16Obs.4277592594Mean0.491.090.350.53St. Dev.7.915.141.427.43Obs.7027259833Mean0.211.420.930.38St. Dev.1.258.004.113.00Obs.4805941580Mean0.331.570.720.43St. Dev.1.683.442.101.89Obs.90167521020SizeMean0.060.150.120.07St. Dev.0.180.480.270.19Obs.267370852828Mean0.210.610.620.32St. Dev.0.511.361.390.85Obs.18083093342451Mean4.4317.2714.7411.31St. Dev.29.5681.2464.7560.91Obs.328289156773Mean0.427.774.381.60St. Dev.7.7954.0334.2522.08Obs.48096685756052Medium (Firms with 51-500 empl.)Large (Firms with 500+ empl.)AllDomesticDomestic MNCsForeign MNC SubsidiariesAllSmall (Firms with up to 50 empl.)Low-tech manufacturingMedium-tech manufacturingHigh-tech manufacturingDistributive servicesKnowledge-intensive servicesTechnological services©International Monetary Fund. Not for Redistribution

11

Table 2.  Patent Applications in the Next 5 Years: Descriptive Statistics by Ownership, Industry,
and Size

Electronic copy available at: https://ssrn.com/abstract=4234381

IndustryMean0.422.771.370.75St. Dev.3.218.344.124.20Obs.15622041721938Mean2.7429.723.907.65St. Dev.27.49111.8617.5753.39Obs.7371911591087Mean0.7812.3120.835.34St. Dev.6.0052.2283.3938.62Obs.4277592594Mean0.310.250.340.31St. Dev.6.282.011.765.81Obs.7027259833Mean0.040.050.000.03St. Dev.0.470.290.000.43Obs.4805941580Mean0.420.271.980.49St. Dev.2.090.939.542.93Obs.90167521020SizeMean0.535.351.461.27St. Dev.2.2761.664.8122.08Obs.18083093342451Mean0.120.200.990.15St. Dev.0.890.777.431.56Obs.267370852828Mean7.1019.1614.8813.18St. Dev.42.7371.9166.4560.16Obs.328289156773Mean0.7510.785.032.27St. Dev.11.3863.6035.3626.04Obs.48096685756052Technological servicesSmall (Firms with up to 50 empl.)Medium (Firms with 51-500 empl.)Large (Firms with 500+ empl.)AllAllLow-tech manufacturingMedium-tech manufacturingHigh-tech manufacturingDistributive servicesKnowledge-intensive servicesDomesticDomestic MNCsForeign MNC Subsidiaries©International Monetary Fund. Not for Redistribution

12

Figure 1.  R&D Spending (log[1+R&D]) by Ownership

Figure 2.  R&D Spending (log[1+R&D]) by Ownership and Subsidy (=1)

Electronic copy available at: https://ssrn.com/abstract=4234381

©International Monetary Fund. Not for Redistribution

13

Figure 3.  R&D Spending (log[1+R&D]) by Size and Subsidy (=1)

Figure 4.  R&D Spending (log[1+R&D]) and 5-Year Ahead Patents (log[1+Patents]) by
Ownership and Subsidy (Red)

Electronic copy available at: https://ssrn.com/abstract=4234381

©International Monetary Fund. Not for Redistribution

14

Figure 5.  R&D Spending (log[1+R&D]) and 5-Year Ahead Patents (log[1+Patents]) by Industry
and Subsidy (Red)

Figure 6.  R&D Spending (log[1+R&D]) and 5-Year Ahead Patents (log[1+Patents]) by Size and
Subsidy (Red)

Electronic copy available at: https://ssrn.com/abstract=4234381

©International Monetary Fund. Not for Redistribution

15

Estimation strategy

To assess the effect of an R&D subsidy on innovation—R&D spending and 5-year ahead patent

applications—by ownership, industry, and size, we estimate several models. We use both an unmatched full
sample and matched sample without outliers. We estimate OLS regressions with time dummies and various
firm controls. Since our dataset is repeated cross-sections over a few years (only a few hundred observations
are of a panel structure), we cannot use fixed effects and attempt to control for firm heterogeneity using various
firm characteristics (as discussed in the previous subsection). The matched sample is based on propensity
score matching and is used to estimate a treatment model conditioning on observables. We cluster robust
standard errors on the industry variable (which assumes correlation within the industry). We exclude dummies
on domestic firms, the distributive services industry, and medium-sized firms in the regressions.

The R&D spending equations with relevant industry-subsidy-ownership and size-subsidy-ownership

dummies and various controls are as follows:

       (1)

       (2)

The patent regressions follow equations (1)-(2) except that R&D spending and its interactions are also

added as control variables:

                               (3)

       (4)

In addition to standard OLS regressions, we apply a matching estimator to establish the effect of a

subsidy (i.e., the treatment) on R&D investment and future patent applications. Matching estimation takes into
account that the receipt of a subsidy is not random, i.e., some firms are more likely than others to apply for

Electronic copy available at: https://ssrn.com/abstract=4234381

12551151ln(1)ForeignDomititiitiitForeignjijitjijiitjjDomjijiitittitjRDspendingSubsidyMNCSubsidyMNCSubsidyIndustrySubsidyIndustryMNCSubsidyIndustryMNCSubsidyXT===+=+++++++++12221121ln(1)ForeignDomititiitiitForeignjijitjijiitjjDomjijiitittitjRDspendingSubsidyMNCSubsidyMNCSubsidySizeSubsidySizeMNCSubsidySizeMNCSubsidyXT===+=+++++++++5ln(1)ln(1)ln(1)itititititittitpatentsSubsidyRDspendingRDspendingSubsidyXT++=++++++++515521151ln(1)ln(1)ForeignitititiitDomForeigniitjijitjijiitjjDomjijiitjpatentsSubsidyRDspendingMNCSubsidyMNCSubsidyIndustrySubsidyIndustryMNCSubsidyIndustryMNCSubsidy+===+=+++++++++ittitXT++©International Monetary Fund. Not for Redistribution

16

subsidies and some applications are more likely to be granted. Matching estimators rely on observable
characteristics to match each treated firm, i.e., subsidy recipients, with a comparable control firm, thereby
creating a quasi-experimental setting. A comparison between such matched treated and control firms would not
suffer from selection biases (Heckman et al., 1998), and the difference in R&D investment between a
subsidized firm and its matched control can be interpreted as induced by the subsidy.

In line with most matching studies, we rely on propensity score matching to match treated and control

firms and compute average treatment effects. We first estimate the propensity for a firm to receive a subsidy
based on observable characteristics using a probit estimation (Rosenbaum & Rubin, 1983). Subsequently, we
match treated and control firms based on the propensity score and nearest neighbor matching.6 We then test
whether there are any remaining significant differences between the matched pairs, i.e., if the matched sample
is balanced. To achieve a balanced match, we impose common support by dropping the 5 percent of treated
observations for which the density of control observations is the lowest, i.e., it is increasingly unlikely to find
good matches (Appendix Table 6).7

We use the following variables in line with previous literature to predict the propensity of a firm to
receive an R&D subsidy: two dummy variables for whether the firm is part of a foreign or domestic MNC,
respectively, firm size (number of employees in logs), firm age in years since founding, patent stock in logs,
exports as a share of sales, five industry group dummies (described above) and four year dummies (2002,
2003, 2004, 2006). These variables are designed to make subsidized firms comparable to their counterparts,
for example, regarding their historical R&D performance measured by the patent stock.

In addition to the matching estimator, we use a matched sample to run both unweighted and weighted

regressions. The matched sample is obtained by dropping observations without common support (i.e., firms
that were not matched). There are about 100 dropped observations, and our final matched sample has 5,623
observations for R&D regressions and 5,263 observations for patent regressions (see the data subsection
above). We use the odds ratio based on the propensity score above to weigh observations to match the
distributions of the observables between the treated and control groups. This approach essentially applies a
matching estimator in the regression setting (Nichols 2007).

Since the dependent variables, whether R&D spending or patents, include many zeros and the

distribution is skewed, we transform the variables into a logarithmic form. To obtain a log form, we take a
natural logarithm after adding one to the value of the variable. Since many observations have small values (the
sample mean of R&D spending is about 0.34 while that of patents is 0.67), it may be an acceptable
transformation.8

6 We also test whether results are sensitive to the choice of the matching estimator by using the Gaussian kernel matching but find
that the results are similar. Matching estimations can be inefficient when they only use the nearest neighbor observation. We
repeat the matching procedure using a Gaussian kernel matching procedure. Kernel matching does not rely on individual control
observations for each treated firm but uses the weighted average of all control observations (Caliendo and Kopeinig 2008).
Differences in the propensity score between a treated firm and control observations serve as weights and the kernel distribution
determines how averages are calculated.

7 We use psmatch2 command in Stata (Leuven and Sianesi 2003).
8 We also attempted a zero-inflated negative binomial estimation as many firms do not do R&D or patent, but estimations did not
converge. Zero-inflated negative binomial regressions require the definition of a condition determining zeros. Firms’ R&D and
patent propensity is typically determined by the technological and institutional conditions of the industry (Arundel & Kabla, 1998;
Fontana et al., 2013). We capture these industry differences by calculating the share of firms in an industry (two-digit NACE)
that filed for EPO patent applications between 1995 and 1999, prior to our estimation sample.

Electronic copy available at: https://ssrn.com/abstract=4234381

©International Monetary Fund. Not for Redistribution

17

Results

Various estimation results show that a R&D subsidy has a positive impact on R&D spending. The

matching estimator indicates that the average treatment effect (ATE) is about 0.1 while the average treatment
effect on the treated (ATT) is about 0.2. These numbers suggest that R&D spending increases by about €0.2
million conditional on the receipt of the subsidy and by €0.1 million for a representative firm. The weighted
regression results on the matched sample show about the same ATE. In the regression without firm controls,
the coefficient on the subsidy dummy is about 0.1 and statistically significant.9 With firm controls, the estimate
of ATE falls to about 0.04 (Table 3, columns 1-4). The results from the unweighted regressions in the matched
sample are similar (Appendix Tables 7-8).

The impact of a subsidy on R&D investment by ownership and size is broadly the same. Interacting the
subsidy dummy with foreign and domestic MNC dummies, we get insignificant coefficients (Table 3, column 5),
suggesting that there is no difference between domestic firms and MNCs, whether foreign or domestic, in extra
R&D investment from a subsidy receipt. The firm size interactions do not produce significant estimates, either
(Table 3, column 7). One exception is that for small firms receiving a subsidy, R&D investment is about €0.1
million lower than for those that do not receive a subsidy. It seems small firms reorient their spending when
they receive a subsidy. Perhaps the subsidy alleviates financial constraints allowing firms to spend on other
items that allow them to commercialize newly developed technologies before investing into creating new ones
(Figure 3 and Figure 6).

Once we incorporate industry interactions, we do get heterogeneous effects of a subsidy (Table 3,

column 6). Domestic firms have a larger response (0.05) to a subsidy in low-tech manufacturing, knowledge-
intensive services, and technological services than MNCs. The response of domestic and foreign MNCs is
largely the same and is larger in medium-tech manufacturing (0.1) and especially in high-tech manufacturing
(about 0.4) than that of domestic firms. The only differential response between domestic and foreign MNCs is in
knowledge-intensive services, where domestic MNCs undertake on average €0.2 million less R&D than foreign
MNCs (and domestic firms).

9 Since the dependent variable is ln(1+R&D spending), the coefficient estimate on the R&D subsidy dummy implies that at low levels
of R&D spending (around the mean of 0.34), the impact is on the R&D spending level (by €0.1 million) while at high levels of
R&D spending, the impact is on the R&D growth rate (0.1 or 10 percent).

Electronic copy available at: https://ssrn.com/abstract=4234381

©International Monetary Fund. Not for Redistribution

18

Table 3.  R&D Spending: Weighted Regressions, Matched Sample

Electronic copy available at: https://ssrn.com/abstract=4234381

(1)(2)(3)(4)(5)(6)(7)Dependent variable: Log (1 + R&D spending)OLSOLSOLSOLSOLSOLSOLSNational government R&D subsidy (d)0.08***0.09***0.10***0.04***0.02-0.02*0.05(0.02)(0.01)(0.01)(0.01)(0.02)(0.01)(0.03)Domestic MNC * R&D subsidy0.06-0.12-0.02(0.07)(0.07)(0.08)Foreign MNC subsidiary * R&D subsidy0.14-0.010.04(0.08)(0.02)(0.08)Low-tech manuf. * R&D subsidy0.05***(0.01)Medium high-tech manuf. * R&D subsidy0.04**(0.01)High-tech manuf. * R&D subsidy-0.01(0.02)Knowledge-intens. services * R&D subsidy0.05*** (0.01)Technological services * R&D subsidy0.05***(0.01)Low-tech manuf. * R&D subsidy * Domestic MNC0.02(0.02)Medium high-tech manuf. * R&D subsidy * Domestic MNC0.10***(0.02)High-tech manuf. * R&D subsidy * Domestic MNC0.47***(0.02)Knowledge-intens. services * R&D subsidy * Domestic MNC-0.20***(0.02)Technological services * R&D subsidy * Domestic MNC0.05(0.04)Low-tech manuf. * R&D subsidy * Foreign MNC-0.03(0.03)Medium high-tech manuf. * R&D subsidy * Foreign MNC0.09**(0.03)High-tech manuf. * R&D subsidy * Foreign MNC0.41***(0.04)Knowledge-intens. services * R&D subsidy * Foreign MNC-0.07(0.04)Technological services * R&D subsidy * Foreign MNC0.04(0.03)Firm with up to 50 empl. * R&D subsidy-0.09***(0.02)Firm with 500+ empl. * R&D subsidy0.46(0.24)Firm with up to 50 empl. * R&D subsidy * Domestic MNC-0.14(0.13)Firm with 500+ empl. * R&D subsidy * Domestic MNC-0.18(0.33)Firm with up to 50 empl. * R&D subsidy * Foreign MNC-0.05(0.10)Firm with 500+ empl. * R&D subsidy * Foreign MNC0.12(0.23)Observations5,6235,6235,6235,6235,6235,6235,623Time dummiesYYYYYYYOwnership dummiesNYYYYYYIndustry dummiesNNYYYYYOther controlsNNNYYYYAdjusted R-squared0.010.140.370.440.450.460.50Robust standard errors in parentheses*** p<0.01, ** p<0.05, * p<0.1©International Monetary Fund. Not for Redistribution

19

Table 4.  Patents: Weighted Regressions, Matched Sample

Electronic copy available at: https://ssrn.com/abstract=4234381

(1)(2)(3)(4)(5)Dependent variable: Log (1 + 5-year ahead patents)OLSOLSOLSOLSOLSNational government R&D subsidy (d)0.01-0.020.000.03-0.01(0.02)(0.02)(0.03)(0.02)(0.03)R&D spending (log)0.15***0.13*0.17**0.130.13*(0.03)(0.06)(0.05)(0.06)(0.06)R&D spending * R&D subsidy-0.03-0.13(0.09)(0.12)Domestic MNC * R&D subsidy-0.010.08-0.06-0.07(0.08)(0.17)(0.09)(0.15)Foreign MNC subsidiary * R&D subsidy0.27**0.17**-0.020.31**(0.09)(0.05)(0.13)(0.08)R&D spending * R&D subsidy * Domestic MNC-0.06(0.18)R&D spending * R&D subsidy * Foreign MNC subsidiary0.26(0.17)Low-tech manuf. * R&D subsidy-0.05***(0.00)Medium high-tech manuf. * R&D subsidy-0.07***(0.01)High-tech manuf. * R&D subsidy-0.09***(0.02)Knowledge-intens. services * R&D subsidy0.01(0.03)Technological services * R&D subsidy-0.02**(0.01)Low-tech manuf. * R&D subsidy * Domestic MNC0.18*(0.08)Medium high-tech manuf. * R&D subsidy * Domestic MNC0.17*(0.08)High-tech manuf. * R&D subsidy * Domestic MNC-0.04(0.08)Knowledge-intens. services * R&D subsidy * Domestic MNC-0.05(0.05)Technological services * R&D subsidy * Domestic MNC-0.13(0.08)Low-tech manuf. * R&D subsidy * Foreign MNC0.43***(0.03)Medium high-tech manuf. * R&D subsidy * Foreign MNC0.04(0.06)High-tech manuf. * R&D subsidy * Foreign MNC0.59***(0.07)Knowledge-intens. services * R&D subsidy * Foreign MNC-0.05(0.07)Technological services * R&D subsidy * Foreign MNC0.39***(0.05)Firm with up to 50 empl. * R&D subsidy-0.00(0.04)Firm with 500+ empl. * R&D subsidy-0.25(0.15)Firm with up to 50 empl. * R&D subsidy * Domestic MNC0.35***(0.08)Firm with 500+ empl. * R&D subsidy * Domestic MNC0.36(0.25)Firm with up to 50 empl. * R&D subsidy * Foreign MNC-0.20(0.17)Firm with 500+ empl. * R&D subsidy * Foreign MNC0.19(0.34)Observations5,2635,2635,2635,2635,263Time, ownership, and industry dummies and other controlsYYYYYAdjusted R-squared0.550.550.550.550.55Robust standard errors in parentheses*** p<0.01, ** p<0.05, * p<0.1©International Monetary Fund. Not for Redistribution

20

Examining the impact of an R&D subsidy on the 5-year ahead patents, we find an additional and
differential effect of an R&D subsidy for domestic and foreign MNCs, even accounting for R&D spending.
Although the government R&D subsidy does not affect 5-year ahead patents separately (Table 4, column 1),
the impact of the subsidy is larger for foreign MNC subsidiaries than domestic MNCs or domestic firms, about
0.3 extra patents for subsidy recipients (Table 4, column 2). However, the impact of the subsidy does not
depend on the level of R&D spending (Table 4, column 3). Accounting for the differential effects by industry, we
find larger impact for foreign MNCs than other firms in low-tech manufacturing and especially in high-tech
manufacturing and technological services (Table 4, column 4).10 Only in medium-tech manufacturing, the
impact of the subsidy for domestic MNCs is larger than for foreign MNCs, about 0.2 extra patents. Ignoring
industry interactions, we find that it is only domestic MNCs with less than 50 employees that tend to increase
their patent applications upon receiving a subsidy. These results broadly suggest that foreign MNCs tend to
benefit more from R&D subsidies than domestic MNCs and domestic firms.

Overall, our estimations show that it is important to account for the differential impact of the subsidy by

industry and ownership and less so by firm size. The impact on R&D spending is largely similar between
foreign and domestic MNCs and is larger than that for domestic firms in medium-tech and high-tech
manufacturing. Domestic firms tend to benefit more in low-tech manufacturing and services than MNCs.
However, the impact on future patents is mostly larger for foreign MNCs than domestic MNCs and domestic
firms in low-tech and high-tech manufacturing and technological services. Only in medium-tech manufacturing,
domestic MNCs tend to benefit more than other firms. Interestingly, the impact of the subsidy on future patent
applications is slightly negative for domestic firm subsidy recipients than domestic firm non-recipients.

10 The detailed estimation results are in Appendix Tables 9-10.

Electronic copy available at: https://ssrn.com/abstract=4234381

©International Monetary Fund. Not for Redistribution

21

Conclusion

A government R&D subsidy has important impact on innovation, both R&D spending and patent

applications. Our study suggests that MNCs, domestic and foreign, are more responsive to an R&D subsidy
than domestic firms. Perhaps it is not surprising as MNCs compete internationally, and innovation is key to
staying competitive. More important, the effect of subsidies depends on the industry, and our results suggest
that a targeted subsidy could be more efficient. In medium- and high-tech industries, there should be a greater
focus on both foreign and domestic MNCs while domestic firms should be more favored in low-tech
manufacturing, knowledge-intensive services, and technological services.

A more surprising result is that foreign MNCs tend to file more patent applications in response to a
subsidy than even domestic MNCs across several industries (except medium-tech manufacturing). Perhaps
despite a similar effect of a subsidy on R&D spending, the impact on patent applications is higher for foreign
MNCs because they use a host country subsidy more effectively or apply it toward more patentable
technologies or products. It is also possible that foreign MNC subsidiaries use subsidies to signal their
headquarters for a new or extended innovation mandate, allowing them to pursue research and patenting more
vigorously (Birkinshaw and Hood, 1998; Cantwell and Mudambi, 2005; Alkemade et al, 2015; Sofka et al.,
2021). This result is also consistent with the international technology sourcing argument. Pursuing R&D in
technological frontier countries like Germany allows firms to source technology, benefit from knowledge
spillovers, and improve innovation outcomes (Alcacer and Chung, 2007; Song et al., 2011; Belderbos et al.,
2015; Chen and Dauchy, 2018; Belderbos & Grimpe, 2020).

In addition, the large impact of a subsidy on foreign MNC subsidiaries suggests that subsidy providers

should not necessarily exclude foreign affiliates. Increasing the R&D activities of foreign MNC subsidiaries
enlarges the knowledge pool within a host country, potentially spilling over to domestic firms. Our findings
regarding the advantages of foreign MNC subsidiaries in translating R&D subsidies into higher R&D spending
and more patents may provide policymakers with an additional rationale for the attraction of foreign direct
investment. However, to mitigate potential negative effects of giving subsidies to foreign MNC subsidiaries, the
government could facilitate collaboration between MNC subsidiaries and domestic firms to enable knowledge
and technology transfer.

Electronic copy available at: https://ssrn.com/abstract=4234381

©International Monetary Fund. Not for Redistribution

22

References

Acemoglu, D., U. Akcigit, H. Alp, N. Bloom, and W. Kerr. 2018. Innovation, Reallocation, and Growth. American

Economic Review, 108(11): 3450–3491.

Aerts, K., & Schmidt, T. 2008. Two for the Price of One?: Additionality Effects of R&D Subsidies: A Comparison

between Flanders and Germany. Research Policy, 37(5): 806-822.

Alcacer, J., & Chung, W. 2007. Location Strategies and Knowledge Spillovers. Management Science, 53(5):

760-776.

Alkemade, F., Heimeriks, G., Schoen, A., Villard, L., & Laurens, P. 2015. Tracking the Internationalization of

Multinational Corporate Inventive Activity: National and Sectoral Characteristics. Research Policy,
44(9): 1763-1772.

Arrow, K. J. 1962. Economic Welfare and the Allocation of Resources for Invention. In Nelson, R.R. (eds.), The

Rate and Direction of Inventive Activity: Economic and Social Factors: pp 609-625. Princeton, NJ.

Arundel, A., & Kabla, I. 1998. What Percentage of Innovations Are Patented? Empirical Estimates for European

Firms. Research Policy, 27: 127-141.

Belderbos, R., & Grimpe, C. 2020. Learning in Foreign and Domestic Value Chains: The Role of Opportunities

and Capabilities. Industrial and Corporate Change, forthcoming.

Belderbos, R., Lokshin, B., & Sadowski, B. 2015. The Returns to Foreign R&D. Journal of International

Business Studies, 46(4): 491-504.

Birkinshaw, J., & Hood, N. 1998. Multinational Subsidiary Evolution: Capability and Charter Change in Foreign-

Owned Subsidiary Companies. Academy of Management Review, 23(4): 773-795.

Blanes, J. V., & Busom, I. 2004. Who Participates in R&D Subsidy Programs? Research Policy, 33(10): 1459-

1476.

Bloom, Nicholas, Rachel Griffith, and John van Reenen. 2002. Do R&D Tax Credits Work? Evidence from a

Panel of Countries 1979-1997. Journal of Public Economics, 85(1): 1-31.

Blundell, R., Griffith, R., & Windmeijer, F. 2002. Individual Effects and Dynamics in Count Data Models. Journal

of Econometrics, 108(1): 113-131.

BMBF. 2016a. Bundesbericht Forschung Und Innovation 2016.

BMBF. 2016b. Forschungs- Und Innovationspolitik Der Länder  - Bundesbericht Forschung Und Innovation

2016 - Ergänzungsband 3.

BMBF. 2016c. Forschungsrahmenprogramm Der Bundesregierung Zur It-Sicherheit - Selbstbestimmt Und

Sicher  in Der Digitalen Welt 2015-2020.

Bozeman, B. 2000. Technology Transfer and Public Policy: A Review of Research and Theory. Research

Policy, 29: 627-655.

Bronzini, R. and P. Piselli. 2016. The Impact of R&D Subsidies on Firm Innovation. Research Policy, 45: 442–

457.

Budish, E., B. Roin, and H. Williams. 2015. Do Firms Underinvest in Long-Term Research? Evidence from

Cancer Clinical Trials. American Economic Review, 105(7): 2044–2085.

Electronic copy available at: https://ssrn.com/abstract=4234381

©International Monetary Fund. Not for Redistribution

23

Caliendo, M., & Kopeinig, S. 2008. Some Practical Guidance for the Implementation of Propensity Score

Matching. Journal of Economic Surveys, 22(1): 31-72.

Cantwell, J. 2017. Innovation and International Business. Industry and Innovation, 24(1): 41-60.

Cantwell, J., & Mudambi, R. 2005. Mne Competence-Creating Subsidiary Mandates. Strategic Management

Journal, 26(12): 1109-1128.

Cappelen, Å., A. Raknerud, and M. Rybalka. 2012. The Effects of R&D Tax Credits on Patenting and

Innovations. Research Policy, 41(2): 334–345.

Cassiman, B., & Golovko, E. 2011. Innovation and Internationalization through Exports. Journal of International

Business Studies, 42(1): 56-75.

Ceh, B. 2009. A Review of Knowledge Externalities, Innovation Clusters and Regional Development.

Professional Geographer, 61: 275-277.

Chaminade, C., & Edquist, C. 2008. Rationales for Public Policy Intervention in the Innovation Process:

Systems of Innovation Approach. In Smits, R., Kuhlmann, S., and Shapira, P. (eds.), The Theory and
Practice of Innovation Policy: pp 95-119. Cheltenham: Edward Elgar.

Chen, Sophia and Estelle Dauchy. 2018. International Technology Sourcing and Knowledge Spillovers:

Evidence from OECD Countries. IMF Working Paper 18/51.

Clarysse, B., Wright, M., & Mustar, P. 2009. Behavioural Additionality of R&D Subsidies: A Learning

Perspective. Research Policy, 38(10): 1517-1533.

Criscuolo, C., Haskel, J. E., & Slaughter, M. J. (2005) Global Engagement and the Innovation Activities of

Firms, NBER Working Paper, Cambridge, MA.

Czarnitzki, D., & Licht, G. 2006. Additionality of Public R&D Grants in a Transition Economy. Economics of

Transition, 14(1): 101-131.

Czarnitzki, D., & Toole, A. A. 2007. Business R&D and the Interplay of R&D Subsidies and Product Market

Uncertainty. Review of Industrial Organization, 31(3): 169-181.

Czarnitzki, D., P. Hanel, and J. M. Rosa. 2011. Evaluating the Impact of R&D Tax Credits on Innovation: A

Microeconometric Study on Canadian Firms. Research Policy, 40(2): 217–229.

David, P. A., & Hall, B. H. 2000a. Heart of Darkness: Modeling Public–Private Funding Interactions inside the

R&D Black Box. Research Policy, 29: 1165-1183.

David, P. A., Hall, B. H., & Toole, A. A. 2000b. Is Public R&D a Complement or a Substitute for Private R&D?

Research Policy, 29: 497-529.

Dechezleprêtre, A., E. Einiö, R. Martin, K.-T. Nguyen, and J. van Reenen. 2016. Do Tax Incentives for
Research Increase Firm Innovation? An RD Design for R&D, Technical report, NBER.

de Faria, P., & Sofka, W. 2010. Knowledge Protection Strategies of Multinational Firms - a Cross-Country

Comparison. Research Policy, 39(7): 956-968.

Dimos, C., & Pugh, G. 2016. The Effectiveness of R&D Subsidies: A Meta-Regression Analysis of the

Evaluation Literature. Research Policy, 45: 797-815.

EFI. 2017. Gutachten Zu Forschung, Innovation Und Technologischer Leistungsfaehigkeit Deutschlands 2017.

Electronic copy available at: https://ssrn.com/abstract=4234381

©International Monetary Fund. Not for Redistribution

24

Ely, A., Van Zwanenberg, P., & Stirling, A. 2014. Broadening out and Opening up Technology Assessment:
Approaches to Enhance International Development, Co-Ordination and Democratisation. Research
Policy, 43(3): 505-518.

Eurostat. 2009. Fifth Community Innovation Survey: Synthesis of Quality Reports. Luxembourg: Office for

Official Publications of the European Communities.

Feldman, M. P., & Kelley, M. R. 2006. The Ex Ante Assessment of Knowledge Spillovers: Government R&D

Policy, Economic Incentives and Private Firm Behavior. Research Policy, 35(10): 1509-1521.

Fontana, R., Nuvolari, A., Shimizu, H., & Vezzulli, A. 2013. Reassessing Patent Propensity: Evidence from a

Dataset of R&D Awards, 1977–2004. Research Policy, 42(10): 1780-1792.

Gelman, A., & Imbens, G. (2013) Why Ask Why? Forward Causal Inference and Reverse Causal Questions,

NBER Working Paper No. 19614, Cambridge, MA.

Gök, A., & Edler, J. 2012. The Use of Behavioural Additionality Evaluation in Innovation Policy Making.

Research Evaluation, 21(4): 306-318.

Gonzalez, X., & Pazo, C. 2008. Do Public Subsidies Stimulate Private R&D Spending? Research Policy, 37:

271-389.

Grimpe, C., Sofka, W., Bhargava, M., & Chatterjee, R. 2017. R&D, Marketing Innovation, and New Product

Performance: A Mixed Methods Study. Journal of Product Innovation Management, 34(3): 360-383.

Heckman, J. J., Ichimura, H., Smith, J. A., & Todd, P. 1998. Charaterizing Selection Bias Using Experimental

Data. Econometrica, 66(5): 1017-1098.

Holmes, R. M., Zahra, S. A., Hoskisson, R. E., DeGhetto, K., & Sutton, T. 2016. Two-Way Streets: The Role of

Institutions and Technology Policy in Firms' Corporate Entrepreneurship and Political Strategies.
Academy of Management Perspectives, 30(3): 247-272.

Howell, S. T. 2017. Financing Innovation: Evidence from R&D Grants. American Economic Review, 107(4):

1136-1164.

Jaffe, A. B., & Le, T. (2015) The Impact of R&D Subsidy on Innovation: A Study of New Zealand Firms, NBER

Working Paper No. No. 21479.

Klette, T. J., Møen, J., & Griliches, Z. 2000. Do Subsidies to Commercial R&D Reduce Market Failures?

Research Policy, 29(4): 471-495.

Koehler, C., Sofka, W., & Grimpe, C. 2012. Selective Search, Sectoral Patterns, and the Impact on Product

Innovation Performance. Research Policy, 41(8): 1344-1356.

Lazzarini, S. G. 2015. Strategizing by the Government: Can Industrial Policy Create Firm-Level Competitive

Advantage? Strategic Management Journal, 36(1): 97-112.

Lester, J. and J. Warda. 2020. Enhanced Tax Incentives for R&D Would Make Americans Richer. ITIF Working

Paper.

Leuven E. and B. Sianesi. 2003. PSMATCH2: Stata module to perform full Mahalanobis and propensity score

matching, common support graphing, and covariate imbalance testing.

Lundvall, B. A., editor. 1992. National Systems of Innovation. Towards a Theory of Innovation and Interactive

Learning. London: Pinter Publishers.

Minniti, A. and F. Venturini. 2017. The Long-run Growth Effects of R&D Policy. Research Policy, 46: 316–326.

Nichols, Austin. 2007. Causal Inference with Observational Data. The Stata Journal, 7(4): 507-541.

Electronic copy available at: https://ssrn.com/abstract=4234381

©International Monetary Fund. Not for Redistribution

25

Niosi, J. 1999. The Internationalization of Industrial R&D: From Technology Transfer to the Learning

Organization. Resarch Policy, 28: 107-117.

NRP. 2017. Nationales Reformprogramm 2017.

OECD. 2006. Government R&D Funding and Company Behavior: Measuring Behavioral Additionality. Paris:

OECD.

OECD. 2019. Fdi in Figures. Paris: OECD.

Papageorgiadis, N., & Sofka, W. 2020. Patent Enforcement across 51 Countries – Patent Enforcement Index

1998–2017. Journal of World Business, 55(4): 1-14.

Park, W. G. 2008. International Patent Protection: 1960-2005. Research Policy, 37(4): 761-766.

Rao, N. 2016. Do Tax Credits Stimulate R&D Spending? The Effect of the R&D Tax Credit in its First Decade.

Journal of Public Economics, 140: 1–12.

Rammer, C., Peters, B., Schmidt, T., Aschhoff, B., Doherr, T., & Niggemann, H. 2005. Innovationen in

Deutschland - Ergebnisse Der Innovationserhebung 2003 in Der Deutschen Wirtschaft. Baden-Baden:
Nomos.

Rigby, J., & Ramlogan, R. 2012. Access to Finance: Impacts of Publicly Supported Venture Capital and Loan

Guarantees. London: Nesta.

RKW. 2017. Wirksamkeit Der Geförderten Fue-Projekte Des Zentralen Innovationsprogramm Mittelstand (Zim)

Fokus: 2014 Abgeschlossene Zim-Projekte.

Rosenbaum, P. R., & Rubin, D. B. 1983. The Central Role of the Propensity Score in Observational Studies for

Causal Effects. Biometrika, 70(1): 41-55.

Salter, A., & Martin, B. 2001. The Economic Benefits of Publicly Funded Basic Research: A Critical Review.

Research Policy, 30(3): 509-532.

Santangelo, G. D., Meyer, K. E., & Jindra, B. 2016. MNE Subsidiaries’ Outsourcing and Insourcing of R&D: The

Role of Local Institutions. Global Strategy Journal, 6(4): 247-268.

Sofka, W., C. Grimpe, F. Hasanov, and R. Cherif. 2021. Additionality or Opportunism? Do Host-Country R&D
Subsidies Impact Innovation in Foreign MNC Subsidiaries? Journal of International Business Policy.

Sofka, W., Shehu, E., & de Faria, P. 2014. Multinational Subsidiary Knowledge Protection—Do Mandates and

Clusters Matter? Research Policy, 43(8): 1320-1333.

Sofka, W., Shehu, E., & Hristov, H. 2018. Research and Innovation (Rio) Country Report 2017: Germany.

Brussels: European Commission.

Sofka, W., & Sprutacz, M. 2017. Rio Country Report 2016: Germany.

Song, J., Asakawa, K., & Chu, Y. 2011. What Determines Knowledge Sourcing from Host Locations of

Overseas R&D Operations?: A Study of Global R&D Activities of Japanese Multinationals. Research
Policy, 40(3): 380-390.

Un, C. A., & Cuervo-Cazurra, A. 2008. Do Subsidiaries of Foreign Mnes Invest More in R&D Than Domestic

Firms? Research Policy, 37(10): 1812-1828.

Un, C. A., Cuervo-Cazurra, A., & Asakawa, K. 2010. R&D Collaborations and Product Innovation. The Journal

of Product Innovation Management, 27(5): 673–689.

Electronic copy available at: https://ssrn.com/abstract=4234381

©International Monetary Fund. Not for Redistribution

26

Zúñiga-Vicente, J. Á., Alonso-Borrego, C., Forcadell, F. J., & Galán, J. I. 2014. Assessing the Effect of Public
Subsidies on Firm R&D Investment: A Survey. Journal of Economic Surveys, 28(1): 36-67.

Electronic copy available at: https://ssrn.com/abstract=4234381

©International Monetary Fund. Not for Redistribution

27

Appendixes

Appendix Table 1.  Industry Classification

Industry
Mining and quarrying
Food and tobacco
Textiles and leather
Wood / paper / publishing
Chemicals / petroleum
Plastic / rubber
Glass / ceramics
Metal
Manufacture of machinery and equipment
Manufacture of electrical machinery
Medical, precision and optical instruments
Manufacture of motor vehicles
Manufacture of furniture, jewellery, sports
equipment and toys
Electricity, gas and water supply
Construction
Retail and motor trade
Wholesale trade
Transportation and communication
Financial intermediation
Real estate and renting
ICT services
Technical services
Consulting
Other business-oriented services

NACE Code
10 – 14
15 – 16
17 – 19
20 – 22
23 – 24
25
26
27 – 28
29
30 – 32
33
34 – 35
36 – 37

40 – 41
45
50, 52
51
60 – 63, 64.1
65 – 67
70 – 71
72, 64.2
73, 74.2, 74.3
74.1, 74.4
74.5 – 74.8, 90

Industry Group
Low-tech manufacturing
Low-tech manufacturing
Low-tech manufacturing
Low-tech manufacturing
Medium high-tech manufacturing
Low-tech manufacturing
Low-tech manufacturing
Low-tech manufacturing
Medium high-tech manufacturing
High-tech manufacturing
High-tech manufacturing
Medium high-tech manufacturing
Low-tech manufacturing

Low-tech manufacturing
Low-tech manufacturing
Distributive services
Distributive services
Distributive services
Knowledge-intensive services
Distributive services
Technological services
Technological services
Knowledge-intensive services
Distributive services

Electronic copy available at: https://ssrn.com/abstract=4234381

©International Monetary Fund. Not for Redistribution

28

Appendix Table 2. Variable Description

Source
CREFO company panel

EPO patent statistics

EPO patent statistics

EPO patent statistics

Variable
Company age (years)

Continuous R&D (d)

Domestic MNC (d)

Foreign MNC subsidiary (d)

No. of employees (log)

Patent appl. (t)

Patent appl. (t+1, t+5)

Patent appl. 1997-1999

Process innovator (d)

R&D investment (€ mil)

Receipt domestic R&D subs. (d)

Share of empl. w/ college educ.

Share of exports in sales (ratio)

Sales (log)
Total patent stock

Firm up to 50 empl. (d)

Firm with 500+ empl. (d)
Industry dummies (1-6)

Year dummies (2000, 2002-2004,
2006)

(d) indicates a dummy variable

MIP survey

MIP survey

MIP survey

MIP survey

MIP survey

Definition
No. of years since registration in
Germany
Firm performed R&D continuously
in the reporting period
Firm is part of a multinational group
with headquarters in Germany
Firm is part of a multinational group
with headquarters outside Germany
Number of employees in reporting
year (log transformed)
Number of EPO patent applications
in reporting year
Number of EPO patent applications
5 years after the reporting year
Number of EPO patent applications
in the pre-sample period 1997-1999
Firm has introduced a process
innovation during the reporting
period
Total R&D investment in € mil in
reporting year
Firm has received an R&D subsidy
from the Federal Government of
Germany or a State Government
during the reporting period
Share of employees with college
education in reporting year
Share of exports in total sales in
reporting year
Total sales
Number of EPO patent applications
until reporting year
Whether a firm has up to 50
employees
Whether a firm has 500+ employees  MIP survey
MIP survey
Industry classification according to
Error! Reference source not
found.
Reporting year

MIP survey

MIP survey

MIP survey

MIP survey

MIP survey

MIP survey

MIP survey
EPO patent statistics

Electronic copy available at: https://ssrn.com/abstract=4234381

©International Monetary Fund. Not for Redistribution

29

Electronic copy available at: https://ssrn.com/abstract=4234381

©International Monetary Fund. Not for Redistribution

30

Appendix Table 3.  Descriptive Statistics by Ownership

Electronic copy available at: https://ssrn.com/abstract=4234381

SampleMeanStd. Dev.MinMaxMeanStd. Dev.MinMaxMeanStd. Dev.MinMaxMeanStd. Dev.MinMaxNo. of patent applications in the next 5 years2.2726.04010690.7511.38071110.7863.60010695.0335.360574R&D expenditures (€ mil)1.6022.080714.790.427.790469.887.7754.030714.794.3834.250579.29Patent stock1.7914.680492.490.645.230252.497.3937.100492.494.8719.680206.06National government R&D subsidy (d)0.320.47010.320.47010.320.47010.310.4601Domestic MNC (d)0.110.31010.000.00001.000.00110.000.0000Foreign MNC subsidiary (d)0.100.29010.000.00000.000.00001.000.0011Firms with up to 50 empl. (d)0.470.50010.560.50010.100.31010.150.3601Firms with 500+ empl. (d)0.130.33010.070.25010.430.50010.270.4501No. patent appl. in t0.383.9301620.151.8201071.569.5101620.985.24088Sales (log)2.132.02-4.2710.521.651.79-4.2710.524.151.84-0.8010.113.721.71-1.7110.31No of employees489.774809.795240000275.384559.6052400001704.806150.62666393871.284850.186104000No of employees (log)4.251.641.6112.393.891.451.6112.395.911.621.7911.105.361.461.7911.55Company age (years)31.2933.33015029.3131.66015043.5639.30014933.6636.170148College educ. empl. (share)25.2226.09010025.5426.94010023.6122.26010024.4622.630100Contin. R&D activities (d)0.460.50010.410.49010.650.48010.600.4901Share of exports in sales0.350.4902.130.280.4302.000.580.5502.060.680.5802.13Process innovator (d)0.660.47010.650.48010.720.45010.670.4701Low-tech manuf. (d)0.320.47010.320.47010.310.46010.300.4601Medium high-tech manuf. (d)0.180.38010.150.36010.290.45010.280.4501High-tech manuf. (d)0.100.30010.090.28010.110.32010.160.3701Distributive services (d)0.140.34010.150.35010.110.31010.100.3001Knowledge-intens. services (d)0.100.29010.100.30010.090.28010.070.2601Technological services (d)0.170.37010.190.39010.100.30010.090.2901Year 2000 (d)0.240.43010.240.43010.250.43010.230.4201Year 2002 (d)0.190.39010.190.39010.210.41010.220.4101Year 2003 (d)0.110.32010.110.31010.140.35010.110.3201Year 2004 (d)0.290.46010.290.45010.280.45010.310.4601Year 2006 (d)0.160.37010.170.38010.120.33010.130.3401No of observations6,0524,809668575AllDomesticDomestic MNCsForeign MNC Subsidiaries©International Monetary Fund. Not for Redistribution

31

Appendix Table 4. Descriptive Statistics by Industry

Electronic copy available at: https://ssrn.com/abstract=4234381

SampleMeanStd. Dev.MinMaxMeanStd. Dev.MinMaxMeanStd. Dev.MinMaxNo. of patent applications in the next 5 years0.754.200687.6553.39010695.3438.620574R&D expenditures (€ mil)0.6912.470469.884.4043.300714.794.1930.160426.75Patent stock0.804.06061.625.3930.280492.494.0519.180206.06National government R&D subsidy (d)0.250.44010.420.49010.520.5001Domestic MNC (d)0.110.31010.180.38010.130.3301Foreign MNC subsidiary (d)0.090.28010.150.35010.150.3601Firms with up to 50 empl. (d)0.370.48010.340.47010.500.5001Firms with 500+ empl. (d)0.130.34010.180.38010.110.3201No. patent appl. in t0.130.930181.258.2401620.865.11088Sales (log)2.441.82-4.2010.522.762.00-2.9610.111.982.02-2.3010.31No of employees419.374664.015193000703.383926.42553144575.184716.155104000No of employees (log)4.501.501.6112.174.711.651.6110.884.151.651.6111.55Company age (years)38.7836.21015034.9935.06014925.0928.130148College educ. empl. (share)10.9712.24010021.8620.28010033.5323.790100Contin. R&D activities (d)0.370.48010.660.47010.740.4401Share of exports in sales0.360.4501.960.700.5502.060.570.5402.13Process innovator (d)0.710.46010.600.49010.540.5001Low-tech manuf. (d)1.000.00110.000.00000.000.0000Medium high-tech manuf. (d)0.000.00001.000.00110.000.0000High-tech manuf. (d)0.000.00000.000.00001.000.0011Distributive services (d)0.000.00000.000.00000.000.0000Knowledge-intens. services (d)0.000.00000.000.00000.000.0000Technological services (d)0.000.00000.000.00000.000.0000Year 2000 (d)0.220.41010.230.42010.170.3801Year 2002 (d)0.160.37010.200.40010.240.4301Year 2003 (d)0.110.31010.140.35010.130.3401Year 2004 (d)0.330.47010.290.45010.300.4601Year 2006 (d)0.180.38010.140.34010.160.3701No of observations1,9381,087594Low-tech manufacturingMedium-tech manufacturingHigh-tech manufacturing©International Monetary Fund. Not for Redistribution

32

Appendix Table 4. Descriptive Statistics by Industry, continued

Electronic copy available at: https://ssrn.com/abstract=4234381

SampleMeanStd. Dev.MinMaxMeanStd. Dev.MinMaxMeanStd. Dev.MinMaxNo. of patent applications in the next 5 years0.315.8101640.030.43090.492.93068R&D expenditures (€ mil)0.537.430196.060.383.00060.840.431.89029.17Patent stock0.172.22058.530.101.17023.360.775.470112.38National government R&D subsidy (d)0.150.36010.090.29010.510.5001Domestic MNC (d)0.090.28010.100.30010.070.2501Foreign MNC subsidiary (d)0.070.26010.070.26010.050.2201Firms with up to 50 empl. (d)0.530.50010.430.50010.740.4401Firms with 500+ empl. (d)0.120.33010.210.41010.030.1701No. patent appl. in t0.040.730200.010.25060.140.91023Sales (log)2.181.87-4.279.682.252.48-2.3010.390.821.59-3.008.99No of employees727.988895.515240000572.531637.82514201104.55506.4058600No of employees (log)4.111.651.6112.394.491.901.619.563.321.251.619.06Company age (years)29.9730.08013435.8438.76115015.2418.080138College educ. empl. (share)15.5417.7909027.5927.47010057.6027.090100Contin. R&D activities (d)0.190.39010.240.43010.580.4901Share of exports in sales0.130.3402.000.040.1601.540.190.3701.96Process innovator (d)0.690.46010.760.43010.600.4901Low-tech manuf. (d)0.000.00000.000.00000.000.0000Medium high-tech manuf. (d)0.000.00000.000.00000.000.0000High-tech manuf. (d)0.000.00000.000.00000.000.0000Distributive services (d)1.000.00110.000.00000.000.0000Knowledge-intens. services (d)0.000.00001.000.00110.000.0000Technological services (d)0.000.00000.000.00001.000.0011Year 2000 (d)0.330.47010.270.45010.230.4201Year 2002 (d)0.160.37010.180.39010.240.4301Year 2003 (d)0.090.28010.100.30010.110.3201Year 2004 (d)0.280.45010.280.45010.240.4301Year 2006 (d)0.150.35010.160.37010.170.3801No of observations8335801,020Distributive servicesKnoweldge-intensive servicesTechnological services©International Monetary Fund. Not for Redistribution

33

Appendix Table 5.  Descriptive Statistics by Size

Electronic copy available at: https://ssrn.com/abstract=4234381

SampleMeanStd. Dev.MinMaxMeanStd. Dev.MinMaxMeanStd. Dev.MinMaxNo. of patent applications in the next 5 years0.151.560681.2722.080106913.1860.160711R&D expenditures (€ mil)0.070.1903.430.320.85016.8711.3160.910714.79Patent stock0.161.00020.381.068.720399.9910.0036.960492.49National government R&D subsidy (d)0.350.48010.300.46010.290.4501Domestic MNC (d)0.020.16010.130.33010.370.4801Foreign MNC subsidiary (d)0.030.17010.140.34010.200.4001Firms with up to 50 empl. (d)1.000.00110.000.00000.000.0000Firms with 500+ empl. (d)0.000.00000.000.00001.000.0011No. patent appl. in t0.040.31080.222.140932.1510.120162Sales (log)0.531.08-4.274.872.951.07-1.207.145.371.390.5010.52No of employees21.2012.91550172.54113.56515003209.8813143.56501240000No of employees (log)2.850.661.613.914.950.643.936.217.170.946.2212.39Company age (years)20.3522.94014237.2935.75015052.3441.560150College educ. empl. (share)32.6629.79010019.1021.1509517.4116.75095Contin. R&D activities (d)0.400.49010.460.50010.630.4801Share of exports in sales0.240.4202.000.420.4902.060.550.5702.13Process innovator (d)0.600.49010.680.47010.770.4201Low-tech manuf. (d)0.250.44010.390.49010.330.4701Medium high-tech manuf. (d)0.130.34010.210.41010.250.4301High-tech manuf. (d)0.110.31010.090.29010.090.2801Distributive services (d)0.160.36010.120.32010.130.3401Knowledge-intens. services (d)0.090.28010.090.28010.160.3601Technological services (d)0.270.44010.100.30010.040.2001Year 2000 (d)0.220.41010.250.43010.260.4401Year 2002 (d)0.190.39010.180.39010.220.4201Year 2003 (d)0.110.31010.110.31010.140.3501Year 2004 (d)0.290.46010.300.46010.280.4501Year 2006 (d)0.190.39010.160.37010.090.2901No of observations2,8282,451773Small (up to 50 empl.)Medium (51-500 empl.)Large (500+ empl.)©International Monetary Fund. Not for Redistribution

34

Appendix Table 6.  Nearest Neighbor Matching: Mean Comparison

Electronic copy available at: https://ssrn.com/abstract=4234381

VariableMean, treatedMean, controlt-testP < tPropensity score0.420.411.240.21Foreign MNC subsidiary (d)0.100.1001.00Domestic MNC (d) 0.090.0901.00No of employees (log) 3.993.99-0.030.98Company age (years)18.9319.26-0.530.60Patent stock (ln) -3.17-3.2410.32Share of exports to sales (ratio)0.430.401.450.15Medium high-tech manuf. (d)0.240.2401.00High-tech manuf. (d) 0.160.1601.00Distributive services (d) 0.060.0601.00Knowledge-intensive services (d)0.020.0201.00Technological services (d)0.250.250.080.94Year 2002 (d) 0.200.2001.00Year 2003 (d) 0.110.1101.00Year 2004 (d) 0.220.22-0.040.97Year 2006 (d) 0.230.220.040.97©International Monetary Fund. Not for Redistribution

35

Appendix Table 7.  R&D Spending: Unweighted Regressions, Matched Sample

Electronic copy available at: https://ssrn.com/abstract=4234381

(1)(2)(3)(4)(5)(6)(7)Dependent variable: Log (1 + R&D spending)OLSOLSOLSOLSOLSOLSOLSNational government R&D subsidy (d)0.11***0.11***0.09***0.03**-0.00-0.010.03(0.01)(0.01)(0.01)(0.01)(0.01)(0.01)(0.02)Domestic MNC * R&D subsidy0.17**0.000.09(0.05)(0.05)(0.05)Foreign MNC subsidiary * R&D subsidy0.15*-0.030.07(0.06)(0.02)(0.04)Low-tech manuf. * R&D subsidy0.02*(0.01)Medium high-tech manuf. * R&D subsidy0.01(0.01)High-tech manuf. * R&D subsidy-0.06***(0.01)Knowledge-intens. services * R&D subsidy0.04* (0.02)Technological services * R&D subsidy0.03**(0.01)Low-tech manuf. * R&D subsidy * Domestic MNC0.06**(0.02)Medium high-tech manuf. * R&D subsidy * Domestic MNC0.20***(0.03)High-tech manuf. * R&D subsidy * Domestic MNC0.41***(0.03)Knowledge-intens. services * R&D subsidy * Domestic MNC-0.23***(0.03)Technological services * R&D subsidy * Domestic MNC0.07**(0.02)Low-tech manuf. * R&D subsidy * Foreign MNC0.03(0.02)Medium high-tech manuf. * R&D subsidy * Foreign MNC0.23***(0.02)High-tech manuf. * R&D subsidy * Foreign MNC0.39***(0.02)Knowledge-intens. services * R&D subsidy * Foreign MNC0.03(0.02)Technological services * R&D subsidy * Foreign MNC0.23***(0.02)Firm with up to 50 empl. * R&D subsidy-0.08**(0.02)Firm with 500+ empl. * R&D subsidy0.22*(0.10)Firm with up to 50 empl. * R&D subsidy * Domestic MNC-0.20*(0.09)Firm with 500+ empl. * R&D subsidy * Domestic MNC-0.01(0.22)Firm with up to 50 empl. * R&D subsidy * Foreign MNC-0.07(0.05)Firm with 500+ empl. * R&D subsidy * Foreign MNC0.21(0.23)Observations5,6235,6235,6235,6235,6235,6235,623Time dummiesYYYYYYYOwnership dummiesNYYYYYYIndustry dummiesNNYYYYYOther controlsNNNYYYYAdjusted R-squared0.020.130.310.390.390.400.44Robust standard errors in parentheses*** p<0.01, ** p<0.05, * p<0.1©International Monetary Fund. Not for Redistribution

36

Appendix Table 8.  Patents: Unweighted Regressions, Matched Sample

Electronic copy available at: https://ssrn.com/abstract=4234381

(1)(2)(3)(4)(5)(6)(7)Dependent variable: Log (1 + 5-year ahead patents)OLSOLSOLSOLSOLSOLSOLSNational government R&D subsidy (d)-0.01-0.01-0.010.00-0.00-0.00-0.02(0.01)(0.01)(0.02)(0.01)(0.01)(0.00)(0.02)R&D spending (log)0.09**0.11**0.09**0.11**0.09**0.11***0.09**(0.02)(0.03)(0.03)(0.03)(0.03)(0.03)(0.02)R&D spending * R&D subsidy0.060.050.050.07(0.06)(0.11)(0.11)(0.12)Domestic MNC * R&D subsidy-0.000.05-0.11***-0.09-0.08-0.01(0.04)(0.13)(0.03)(0.07)(0.08)(0.15)Foreign MNC subsidiary * R&D subsidy0.12*0.06-0.04-0.070.15**0.09(0.05)(0.05)(0.06)(0.07)(0.06)(0.06)R&D spending * R&D subsidy * Domestic MNC-0.11-0.09-0.18(0.24)(0.26)(0.21)R&D spending * R&D subsidy * Foreign MNC subsidiary0.080.100.13(0.19)(0.17)(0.22)Low-tech manuf. * R&D subsidy-0.02***-0.03***(0.00)(0.01)Medium high-tech manuf. * R&D subsidy0.00-0.01(0.00)(0.02)High-tech manuf. * R&D subsidy-0.04***-0.05***(0.01)(0.01)Knowledge-intens. services * R&D subsidy0.020.02(0.02)(0.02)Technological services * R&D subsidy-0.00-0.01(0.01)(0.01)Low-tech manuf. * R&D subsidy * Domestic MNC0.22***0.24**(0.04)(0.08)Medium high-tech manuf. * R&D subsidy * Domestic MNC0.16***0.19(0.04)(0.10)High-tech manuf. * R&D subsidy * Domestic MNC-0.07-0.03(0.04)(0.15)Knowledge-intens. services * R&D subsidy * Domestic MNC0.02*0.00(0.01)(0.06)Technological services * R&D subsidy * Domestic MNC0.020.04(0.02)(0.06)Low-tech manuf. * R&D subsidy * Foreign MNC0.27***0.26***(0.01)(0.01)Medium high-tech manuf. * R&D subsidy * Foreign MNC-0.04*-0.09**(0.02)(0.03)High-tech manuf. * R&D subsidy * Foreign MNC0.36***0.30***(0.02)(0.03)Knowledge-intens. services * R&D subsidy * Foreign MNC-0.06*-0.07**(0.03)(0.03)Technological services * R&D subsidy * Foreign MNC0.28***0.23***(0.02)(0.02)Firm with up to 50 empl. * R&D subsidy-0.010.00(0.01)(0.01)Firm with 500+ empl. * R&D subsidy-0.02-0.05(0.09)(0.08)Firm with up to 50 empl. * R&D subsidy * Domestic MNC0.26*0.21*(0.11)(0.10)Firm with 500+ empl. * R&D subsidy * Domestic MNC0.180.28(0.26)(0.15)Firm with up to 50 empl. * R&D subsidy * Foreign MNC-0.12-0.08(0.09)(0.09)Firm with 500+ empl. * R&D subsidy * Foreign MNC-0.09-0.20(0.15)(0.23)Observations5,2635,2635,2635,2635,2635,2635,263Time, ownership, and industry dummies and other controlsYYYYYYYAdjusted R-squared0.560.560.560.560.560.560.56Robust standard errors in parentheses*** p<0.01, ** p<0.05, * p<0.1©International Monetary Fund. Not for Redistribution

37

Appendix Table 9.  R&D Spending: Weighted Regressions, Matched Sample

Electronic copy available at: https://ssrn.com/abstract=4234381

(1)(2)(3)(4)(5)(6)(7)Dependent variable: Log (1 + R&D spending)OLSOLSOLSOLSOLSOLSOLSNational government R&D subsidy (d)0.08***0.09***0.10***0.04***0.02-0.02*0.05(0.02)(0.01)(0.01)(0.01)(0.02)(0.01)(0.03)Domestic MNC * R&D subsidy0.06-0.12-0.02(0.07)(0.07)(0.08)Foreign MNC subsidiary * R&D subsidy0.14-0.010.04(0.08)(0.02)(0.08)Low-tech manuf. * R&D subsidy0.05***(0.01)Medium high-tech manuf. * R&D subsidy0.04**(0.01)High-tech manuf. * R&D subsidy-0.01(0.02)Knowledge-intens. services * R&D subsidy0.05*** (0.01)Technological services * R&D subsidy0.05***(0.01)Low-tech manuf. * R&D subsidy * Domestic MNC0.02(0.02)Medium high-tech manuf. * R&D subsidy * Domestic MNC0.10***(0.02)High-tech manuf. * R&D subsidy * Domestic MNC0.47***(0.02)Knowledge-intens. services * R&D subsidy * Domestic MNC-0.20***(0.02)Technological services * R&D subsidy * Domestic MNC0.05(0.04)Low-tech manuf. * R&D subsidy * Foreign MNC-0.03(0.03)Medium high-tech manuf. * R&D subsidy * Foreign MNC0.09**(0.03)High-tech manuf. * R&D subsidy * Foreign MNC0.41***(0.04)Knowledge-intens. services * R&D subsidy * Foreign MNC-0.07(0.04)Technological services * R&D subsidy * Foreign MNC0.04(0.03)Firm with up to 50 empl. * R&D subsidy-0.09***(0.02)Firm with 500+ empl. * R&D subsidy0.46(0.24)Firm with up to 50 empl. * R&D subsidy * Domestic MNC-0.14(0.13)Firm with 500+ empl. * R&D subsidy * Domestic MNC-0.18(0.33)Firm with up to 50 empl. * R&D subsidy * Foreign MNC-0.05(0.10)Firm with 500+ empl. * R&D subsidy * Foreign MNC0.12(0.23)©International Monetary Fund. Not for Redistribution

38

Appendix Table 9.  R&D Spending: Weighted Regressions, Matched Sample, cont.

Electronic copy available at: https://ssrn.com/abstract=4234381

Domestic MNC (d)0.41***0.17*0.080.060.060.09(0.08)(0.08)(0.06)(0.04)(0.04)(0.06)Foreign MNC subsidiary (d)0.35***0.14**0.06-0.00-0.000.03(0.08)(0.04)(0.03)(0.02)(0.02)(0.02)Patent stock (log)0.010.010.010.01*(0.01)(0.01)(0.01)(0.01)Sales (log)0.05**0.05**0.06**0.05**(0.02)(0.02)(0.02)(0.02)No of employees (log)0.07***0.07***0.07***0.05*(0.02)(0.02)(0.02)(0.02)Company age (years)-0.00-0.00-0.00-0.00(0.00)(0.00)(0.00)(0.00)College educ. empl. (share)0.00**0.00*0.00*0.00**(0.00)(0.00)(0.00)(0.00)No of patent applications (log)0.17**0.17**0.16**0.12**(0.05)(0.05)(0.05)(0.05)Contin. R&D activities (d)0.13***0.13***0.13***0.13***(0.02)(0.02)(0.02)(0.02)Exports to sales (share)-0.01-0.01-0.01-0.01(0.01)(0.01)(0.01)(0.01)Process innovator (d)0.010.010.010.00(0.01)(0.01)(0.01)(0.01)Low-tech manuf. (d)-0.00-0.02*-0.02*-0.02**-0.01(0.02)(0.01)(0.01)(0.01)(0.01)Medium high-tech manuf. (d)0.14***0.020.030.020.04(0.02)(0.01)(0.01)(0.01)(0.02)High-tech manuf. (d)0.19***0.10***0.11***0.09***0.12***(0.01)(0.01)(0.01)(0.01)(0.01)Knowledge-intens. services (d)0.01**0.020.020.020.02(0.00)(0.01)(0.01)(0.01)(0.02)Technological services (d)0.14***0.07**0.07**0.05*0.07**(0.01)(0.02)(0.02)(0.02)(0.02)Firm with up to 50 empl. (d)-0.21***0.07*(0.04)(0.03)Firm with 500+ empl. (d)0.57***0.17**(0.07)(0.06)Year 2002 (d)0.040.030.04**0.030.030.03*0.03**(0.02)(0.03)(0.01)(0.02)(0.02)(0.02)(0.01)Year 2003 (d)0.040.040.040.030.030.030.03(0.04)(0.03)(0.03)(0.03)(0.03)(0.02)(0.02)Year 2004 (d)0.05**0.05**0.06**0.05***0.05**0.05***0.05**(0.02)(0.01)(0.02)(0.01)(0.01)(0.01)(0.01)Year 2006 (d)0.05***0.04**0.04**0.010.020.010.02(0.01)(0.01)(0.01)(0.02)(0.02)(0.02)(0.02)Constant0.16**0.09**0.07**-0.38**-0.37**-0.36**-0.33*(0.05)(0.03)(0.02)(0.11)(0.11)(0.11)(0.14)Observations5,6235,6235,6235,6235,6235,6235,623Time dummiesYYYYYYYOwnership dummiesNYYYYYYIndustry dummiesNNYYYYYOther controlsNNNYYYYAdjusted R-squared0.010.140.370.440.450.460.50Robust standard errors in parentheses*** p<0.01, ** p<0.05, * p<0.1©International Monetary Fund. Not for Redistribution

39

Appendix Table 10.  Patents: Weighted Regressions, Matched Sample

Electronic copy available at: https://ssrn.com/abstract=4234381

(1)(2)(3)(4)(5)Dependent variable: Log (1 + 5-year ahead patents)OLSOLSOLSOLSOLSNational government R&D subsidy (d)0.01-0.020.000.03-0.01(0.02)(0.02)(0.03)(0.02)(0.03)R&D spending (log)0.15***0.13*0.17**0.130.13*(0.03)(0.06)(0.05)(0.06)(0.06)R&D spending * R&D subsidy-0.03-0.13(0.09)(0.12)Domestic MNC * R&D subsidy-0.010.08-0.06-0.07(0.08)(0.17)(0.09)(0.15)Foreign MNC subsidiary * R&D subsidy0.27**0.17**-0.020.31**(0.09)(0.05)(0.13)(0.08)R&D spending * R&D subsidy * Domestic MNC-0.06(0.18)R&D spending * R&D subsidy * Foreign MNC subsidiary0.26(0.17)Low-tech manuf. * R&D subsidy-0.05***(0.00)Medium high-tech manuf. * R&D subsidy-0.07***(0.01)High-tech manuf. * R&D subsidy-0.09***(0.02)Knowledge-intens. services * R&D subsidy0.01(0.03)Technological services * R&D subsidy-0.02**(0.01)Low-tech manuf. * R&D subsidy * Domestic MNC0.18*(0.08)Medium high-tech manuf. * R&D subsidy * Domestic MNC0.17*(0.08)High-tech manuf. * R&D subsidy * Domestic MNC-0.04(0.08)Knowledge-intens. services * R&D subsidy * Domestic MNC-0.05(0.05)Technological services * R&D subsidy * Domestic MNC-0.13(0.08)Low-tech manuf. * R&D subsidy * Foreign MNC0.43***(0.03)Medium high-tech manuf. * R&D subsidy * Foreign MNC0.04(0.06)High-tech manuf. * R&D subsidy * Foreign MNC0.59***(0.07)Knowledge-intens. services * R&D subsidy * Foreign MNC-0.05(0.07)Technological services * R&D subsidy * Foreign MNC0.39***(0.05)Firm with up to 50 empl. * R&D subsidy-0.00(0.04)Firm with 500+ empl. * R&D subsidy-0.25(0.15)Firm with up to 50 empl. * R&D subsidy * Domestic MNC0.35***(0.08)Firm with 500+ empl. * R&D subsidy * Domestic MNC0.36(0.25)Firm with up to 50 empl. * R&D subsidy * Foreign MNC-0.20(0.17)Firm with 500+ empl. * R&D subsidy * Foreign MNC0.19(0.34)©International Monetary Fund. Not for Redistribution

40

Appendix Table 10.  Patents: Weighted Regressions, Matched Sample, cont.

Electronic copy available at: https://ssrn.com/abstract=4234381

Domestic MNC (d)0.030.030.020.030.02(0.06)(0.08)(0.09)(0.08)(0.09)Foreign MNC subsidiary (d)-0.09-0.21-0.22-0.21-0.22(0.14)(0.13)(0.13)(0.13)(0.14)Patent stock (log)0.08***0.08***0.08***0.08***0.08***(0.00)(0.00)(0.00)(0.00)(0.00)Sales (log)0.010.010.010.010.01(0.01)(0.01)(0.01)(0.01)(0.01)No of employees (log)0.020.020.020.020.02(0.02)(0.02)(0.02)(0.02)(0.02)Company age (years)0.000.000.00*0.000.00(0.00)(0.00)(0.00)(0.00)(0.00)College educ. empl. (share)-0.00-0.00-0.00-0.00-0.00(0.00)(0.00)(0.00)(0.00)(0.00)No of patent applications (log)0.89***0.89***0.89***0.88***0.88***(0.06)(0.06)(0.07)(0.06)(0.07)Contin. R&D activities (d)-0.02-0.01-0.02-0.01-0.02(0.03)(0.03)(0.02)(0.03)(0.03)Exports to sales (share)0.06**0.06**0.06**0.06**0.06**(0.02)(0.02)(0.02)(0.02)(0.02)Process innovator (d)-0.01-0.02-0.02-0.02-0.01(0.02)(0.02)(0.02)(0.02)(0.02)Low-tech manuf. (d)0.000.010.000.010.01(0.02)(0.02)(0.02)(0.02)(0.01)Medium high-tech manuf. (d)0.020.020.020.050.03(0.02)(0.03)(0.03)(0.03)(0.02)High-tech manuf. (d)0.020.020.020.040.02(0.02)(0.02)(0.02)(0.02)(0.02)Knowledge-intens. services (d)-0.01*-0.02**-0.02**-0.02*-0.02**(0.00)(0.00)(0.01)(0.01)(0.01)Technological services (d)0.030.030.020.020.02(0.02)(0.02)(0.02)(0.02)(0.02)Firm with up to 50 empl. (d)0.03(0.05)Firm with 500+ empl. (d)0.09(0.13)Year 2002 (d)-0.01-0.01-0.01-0.00-0.01(0.04)(0.03)(0.03)(0.03)(0.03)Year 2003 (d)-0.01-0.01-0.01-0.01-0.01(0.05)(0.04)(0.05)(0.04)(0.04)Year 2004 (d)-0.06-0.06-0.06-0.06-0.06(0.06)(0.06)(0.06)(0.06)(0.06)Year 2006 (d)-0.06-0.06-0.06-0.05-0.06(0.04)(0.04)(0.04)(0.04)(0.04)Constant0.31**0.31**0.31**0.30**0.27**(0.10)(0.10)(0.09)(0.10)(0.08)Observations5,2635,2635,2635,2635,263Time, ownership, and industry dummies and other controlsYYYYYAdjusted R-squared0.550.550.550.550.55Robust standard errors in parentheses*** p<0.01, ** p<0.05, * p<0.1©International Monetary Fund. Not for Redistribution

Electronic copy available at: https://ssrn.com/abstract=4234381

