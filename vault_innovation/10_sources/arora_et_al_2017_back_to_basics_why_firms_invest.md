NBER WORKING PAPER SERIES

BACK TO BASICS: WHY DO FIRMS INVEST IN RESEARCH?

Ashish Arora
Sharon Belenzon
Lia Sheer

Working Paper 23187
http://www.nber.org/papers/w23187

NATIONAL BUREAU OF ECONOMIC RESEARCH
1050 Massachusetts Avenue
Cambridge, MA 02138
February 2017, Revised November 2017

We would like to thank Wes Cohen and Andrea Patacconi for helpful comments and suggestions.
We  thank  the  Fuqua  School  of  Business,  Duke  University,  for  research  support.  All  remaining
errors are ours. The views expressed herein are those of the authors and do not necessarily reflect
the views of the National Bureau of Economic Research.

NBER working papers are circulated for discussion and comment purposes. They have not been
peer-reviewed or been subject to the review by the NBER Board of Directors that accompanies
official NBER publications.

© 2017 by Ashish Arora, Sharon Belenzon, and Lia Sheer. All rights reserved. Short sections of
text, not to exceed two paragraphs, may be quoted without explicit permission provided that full
credit, including © notice, is given to the source.

Back to Basics: Why do Firms Invest in Research?
Ashish Arora, Sharon Belenzon, and Lia Sheer
NBER Working Paper No. 23187
February 2017, Revised November 2017
JEL No. O31,O32

ABSTRACT

If scientific knowledge is a public good, why do firms invest in research? This paper revisits this
classic question with new data on patent citations to scientific publications by corporations. Using
data on 4,736 firms for the period 1980-2006, we document that corporate investment in research
is closely related to its use in internal invention. Specifically, firms that build on their scientific
research in their inventive activity invest more in research than those that are less successful in
using their research internally. Consistent with this, research that is internally used is valued more
and is more productive. Our results are consistent with the view that to justify further investment
in research corporate scientists need to demonstrate that their recent scientific work is useful for
the core inventive activity of the sponsoring firm.

Lia Sheer
Fuqua School of Business
Duke University
100 Fuqua Drive
Durham NC 27708
lia.sheer@duke.edu

Ashish Arora
Fuqua School of Business
Duke University
Box 90120
Durham, NC 27708-0120
and NBER
ashish.arora@duke.edu

Sharon Belenzon
Fuqua School of Business
Duke University
100 Fuqua Drive
Durham, NC 27708
and NBER
sharon.belenzon@duke.edu

Back to Basics: Why do Firms Invest in Research?

Ashish Arora(cid:3)

Sharon Belenzony

Lia Sheerz

November 6, 2017

Abstract

If scienti(cid:133)c knowledge is a public good, why do (cid:133)rms invest in research? This paper revisits this
classic question with new data on patent citations to scienti(cid:133)c publications by corporations. Using
data on 4,736 (cid:133)rms for the period 1980-2006, we document that corporate investment in research is
closely related to its use in internal invention. Speci(cid:133)cally, (cid:133)rms that build on their scienti(cid:133)c research
in their inventive activity invest more in research than those that are less successful in using their
research internally. Consistent with this, research that is internally used is valued more and is more
productive. Our results are consistent with the view that to justify further investment in research
corporate scientists need to demonstrate that their recent scienti(cid:133)c work is useful for the core inventive
activity of the sponsoring (cid:133)rm.

Keywords: innovation, scienti(cid:133)c research, development, role of science in corporate R&D
JEL Classi(cid:133)cation: O31, O32, O16.

1 Introduction

Corporate investment in scienti(cid:133)c knowledge has always been a puzzle. It is substantial in magnitude and

the available evidence suggests it is privately pro(cid:133)table, and yet, we do not fully understand how (cid:133)rms

derive value from producing what is essentially a public good. In 2015, the business sector performed

nearly 26% of all basic research in the United States and funded a similar share (NSF 2017)1. In absolute

terms, the business sector invested over $22 billion in basic research, a substantial amount. While evidence

on the pro(cid:133)tability of such investments is scarce, studies based on data from the 1960s and 1970s suggest

that private returns are substantial. In particular, Zvi Griliches (1986), based on a sample of 883 large

(cid:3)Duke University, Fuqua School of Business and NBER (ashish.arora@duke.edu)
yDuke University, Fuqua School of Business and NBER (sharon.belenzon@duke.edu)
zDuke University, Fuqua School of Business (lia.sheer@duke.edu)
1 National Science Foundation, National Center for Science and Engineering Statistics. 2017. National Patterns of R&D
Resources: 2014(cid:150)15 Data Update. NSF 17-311. Arlington, VA. https://www.nsf.gov/statistics/2017/nsf17311. According
to the same source, business performed over 40% of basic and applied research in the United States, and funded a similar
share.

1

manufacturing (cid:133)rms in the United States, concluded that investment in basic research was associated

with higher productivity and pro(cid:133)ts, implying a signi(cid:133)cant private returns to basic research. Yet, the

mechanism by which these private returns accrue remains unclear once the knowledge produced is made

publicly available in the form of patents and scienti(cid:133)c publications.

Over the last quarter century, a variety of explanations have been put forward. These explanations

focused on absorptive capacity to use external knowledge (Cohen and Levinthal, 1989; Rosenberg, 1990;

Gambardella, 1992), enhancing reputation to attract investors and costumers (Hicks, 1995) and incentives

for high-skilled scientist-inventors (Audretsch and Stephan, 1996; Stern, 2004; Gambardella et al., 2015).

The various explanations are not mutually exclusive, but can have very di⁄erent normative and positive

implications (section 2 discusses these in more detail).

In this paper, we explore the empirical basis for a di⁄erent explanation, namely that ". . . most of

the actual research in industry is devoted to the development of new products or processes" (Griliches,

1986:145)2. We use newly developed data linking patents to scienti(cid:133)c publications matched to (cid:133)rms to

investigate the extent to which (cid:133)rms invest in research as an input into their own inventions. We measure

corporate research by scienti(cid:133)c papers authored by researchers employed by (cid:133)rms. We measure the use of

research as inputs into inventive activity by citations in the (cid:133)rm(cid:146)s patents to its own scienti(cid:133)c publications.

Spillovers are measured by citations in the patents of other (cid:133)rms to the focal (cid:133)rm(cid:146)s scienti(cid:133)c publications.

We (cid:133)nd that (cid:133)rms produce more scienti(cid:133)c knowledge when they are able to use it in their own inventions,

but spillovers to product market rivals are associated with lower scienti(cid:133)c production. Our estimates

indicate that the positive e⁄ect of one internal citation on the number of future publications produced

by the focal (cid:133)rm is equivalent to the combined negative e⁄ect of four external citations. Thus, while

spillovers might cause (cid:133)rms to underinvest in research, (cid:133)rms would still invest in research if they are able

to use it internally.

Our principal contribution is to document that corporate production of scienti(cid:133)c knowledge is closely

related to its use in internal invention. We examine both the determinant of progress of science and

2 The modern innovation literature has tended to con(cid:135)ate research and development. The older innovation literature was
much more careful in distinguishing between the two. Nelson (1959) was among the (cid:133)rst to examine incentives to invest
in research as opposed to development. Using publications data, Adams (1990) (cid:133)nds that scienti(cid:133)c knowledge absorbed by
(cid:133)rms is associated with higher productivity growth. Simon Kuznets, in his 1971 Nobel Prize Lecture concluded that "Mass
application of technological innovations, which constitutes much of the distinctive substance of modern economic growth, is
closely connected with the further progress of science, in its turn the basis for additional advance in technology ".

2

its application in development at the (cid:133)rm level. Our main methodological contribution is to match

publication records from Web of Science (WoS) to front-page non-patent literature (NPL) references on a

large scale. While previous research using patent citation data was mostly done for selected industries and

years (e.g., Narin and Noma, 1985; Narin et al., 1997; McMillan et al., 2000; Hicks et al., 2001; Breschi

and Catalini, 2010; Bikard, 2015; Popp, 2016), our research examines a broad range of companies across

many industries over a quarter of a century. Our primary (cid:133)rm sample consists of 4,736 U.S. headquartered

publicly listed, R&D-performing companies over the period 1980-2006. Collectively, these (cid:133)rms account

for approximately 300 thousand corporate scienti(cid:133)c publications over the sample period, of which 50,494

publications are cited at least once by patents granted up to 2014.

We present three main (cid:133)ndings. First, we validate that our measure of patent citation to science

corresponds to the use of science in invention. Using data from the Carnegie Mellon Survey of R&D

performing (cid:133)rms (Cohen et al., 2000), we show that (cid:133)rms whose patents cite science are also those

that report using scienti(cid:133)c output in their R&D projects. This relationship continues to hold at a (cid:133)ner

measurement scale such as relating citations to use in speci(cid:133)c technology areas.

Second, we demonstrate a strong positive relationship between corporate investment in research and

internal use of past research in invention. Firms invest more in research when the scienti(cid:133)c knowledge

they produce is cited in their patents. This relationship is stronger for new, basic, high quality cited

research and for citing patents in core technology areas of the inventing (cid:133)rm. We supplement these

(cid:133)ndings by showing that internal use is associated with a higher R&D productivity and a higher stock

market valuation of scienti(cid:133)c publications stock.

Third, consistent with the view that research is an input into internal inventive activity, we (cid:133)nd that

(cid:133)rms produce fewer publications when their research spills over to close product market rivals and that

these spillovers are negatively related to the private value of research. These patterns are inconsistent with

the view that (cid:133)rms invest in research principally to absorb external knowledge. This is also inconsistent

with (cid:133)rm(cid:146)s investing in research principally to attract talented workers or to signal to customers or

regulators.

The (cid:133)rm behavior we analyze, namely the production and use of scienti(cid:133)c knowledge by pro(cid:133)t seeking

companies, is complex. We are well aware that both the production and use of research are potentially

3

a⁄ected by common variables, some of which are unobserved and are likely to vary across (cid:133)rms and

industries. We probe the robustness of our results by using (cid:133)rm-(cid:133)xed e⁄ects and by directly measur-

ing organizational features that should help (cid:133)rms use internally the science they produce. We present

instrumental variable estimates that are based on variation across states over time in the application

of the Inevitable Disclosure Doctrine. This doctrine restricts scientists and inventors(cid:146)mobility between

companies, leading to a higher use of research in invention through a tighter link between research and

development personnel.

The rest of the paper is organized as following. Section 2 discusses related literature, Section 3 presents

the data and empirical methodology, Section 4 presents the estimation results and Section 5 concludes.

2 Related literature

American industrial research activity typically takes place inside corporate research labs. These labs were

initially established with only modest goals. In the late 19th century, (cid:133)rms in technology intensive sectors

such as railroads, steel, and telegraphy relied largely on external inventions. These (cid:133)rms established

industrial labs to evaluate the quality of inputs, such as the quality of steel for rails (Mowery, 1995;

Carlson, 2013). Thereafter, in the early 20th century, (cid:133)rms such as AT&T, GE and DuPont invested in

internal research to solve production problems and evaluate and adapt inventions acquired from other

(cid:133)rms (Reich, 1985; Hounshell and Smith, 1988). Corporate investment in research became more signi(cid:133)cant

during the inter-war years, as corporations grew larger and more anxious to manage innovation instead

of having to rely on external inventions (Maclaurin, 1953). Stronger anti-trust enforcement provided an

additional impetus as some farsighted managers saw in research a source of new products to fuel growth

without running afoul of the anti-trust authorities.

The importance of discoveries such as vacuum tubes, radar, radio, synthetic rubber, nuclear (cid:133)ssion,

and penicillin in the conduct of World War II led to a deeper appreciation of the potential economic

usefulness of research. The simplest view of the role of research in innovation was the so-called "linear

model" associated with Bush (1945), who asserted that technical progress rests upon scienti(cid:133)c advance;

that inventions grew out of research3. This view was modi(cid:133)ed and enriched in a variety of ways (Kline

3 In Vannevar Bush(cid:146)s own words: "Basic research leads to new knowledge. It provides scienti(cid:133)c capital. It creates the fund

4

and Rosenberg, 1986; David, Mowery and Steinmueller, 1992). However, the underlying notion that

"...most of the actual research in industry is devoted to the development of new products or processes..."

(Griliches, 1986: 145) remained in place. In a seminal study, Griliches estimated the private return to

research using the National Science Foundation (NSF) R&D-Census match, containing information on

R&D expenditures, sales and employment for approximately 1000 largest manufacturing (cid:133)rms from 1957

through 1977. He estimated a Cobb-Douglas production function, including basic research as a fraction

of total R&D in addition to R&D stock, labor and capital and found a very large return to basic research.

Firms that spent a larger share of R&D on basic research were substantially more productive.4

While Griliches(cid:146)s work demonstrated the presence of signi(cid:133)cant private returns to research, the mech-

anism by which these private returns accrue remained unclear. Since the results of basic research were

typically published and shared (e.g., Dasgupta and David, 1994), this raised the question of how (cid:133)rms

were bene(cid:133)ting from their investment in research and why should they invest themselves rather than

"free-ride" on the research of others (Arrow, 1962; Nelson 1959). Contributing to this puzzle was the

absence of a serious attempt to explore empirically the extent to which (cid:133)rms invest in science to spur their

own downstream inventions. This puzzle led to new explanations for why (cid:133)rms invest in research includ-

ing absorptive capacity (Cohen and Levinthal, 1989; Rosenberg, 1990; Gambardella, 1992), incentives for

high-skilled scientist-inventors (Audretsch and Stephan, 1996; Stern, 2004; Gambardella et al., 2015) and

enhancing reputation to attract investors and costumers (Hicks, 1995). The various explanations are not

mutually exclusive, but can have very di⁄erent normative and positive implications.

Cohen and Levinthal (1989) challenged the public good nature of research, arguing that accessing

outside knowledge is costly and requires absorptive capacity, which in turn requires that (cid:133)rms engage in

R&D. Rosenberg (1990) also challenged the idea that existing knowledge, though in the public domain,

was "on the shelf", available to all. Instead, he argued that (cid:133)nding, evaluating, and using publicly avail-

able knowledge itself presupposed some prior knowledge. He claimed therefore that (cid:133)rms invest in research

because, in part, basic research helps the company stay up-to-date and identify scienti(cid:133)c developments

from which the practical applications of knowledge must be drawn. New products and new processes do not appear full-grown.
They are founded on new principles and new conceptions, which in turn are painstakingly developed by research in the purest
realms of science." (p. 241).

4 Mans(cid:133)eld (1980) found that investment in basic research was related to productivity growth in U.S. manufacturing

industries in the period 1948-66, controlling for applied research and development.

5

in its (cid:133)eld as well as more easily absorb external knowledge while (cid:133)tting it to its own needs (Rosenberg

1990). A vast literature has found evidence consistent with absorptive capacity. Using survey data, Levin

et al. (1987) (cid:133)nd that independent R&D is most e⁄ective for learning about rivals(cid:146) technology. Gam-

bardella (1992) shows that pharmaceutical (cid:133)rms with better research capabilities, measured by number

of publications, are able to exploit internal as well as external science more e⁄ectively.

Using data from the pharmaceuticals industry, Cockburn and Henderson (1998) argue that to take ad-

vantage of public research (cid:133)rms must develop internal basic research programs as a platform of interacting

with public sector researchers. Several studies examined the role of corporate publications in attracting

talented scientist-inventors. Hicks (1995) argues that companies invest is research because publications

are an e⁄ective tool to recruit scientists5. Henderson and Cockburn (1994) emphasize the importance of

publications as a reward system. Examining research programs of major pharmaceutical (cid:133)rms they (cid:133)nd

that scientists that are promoted on the basis of their publications and reputation in the wider scienti(cid:133)c

community generate more important patents. Some researchers may have a "taste for science" i.e., may

be willing to accept industrial positions if allowed to spend some time on their own research and to publish

it. Stern (2004) (cid:133)nds that scientists may be willing to accept 20% lower wages in exchange for autonomy,

such as time for conducting and publishing independent research. Using survey data on PhD industrial

scientists, Sauermann and Cohen (2010) study the relationship between industrial scientists(cid:146)motives and

their innovation activities. They (cid:133)nd that intellectual challenge and independence have the strongest

(positive) relationship with innovation output, especially in upstream research activities. Gambardella et

al. (2015) argue that DuPont(cid:146)s invention of Nylon is the result of o⁄ering the young Harvard scientist

Wallace Carothers the opportunity to publish his independent research. Gans et al. (2013) develop a

theoretical model in which (cid:133)rms allow researchers to publish in return to lower wages as long as patents

can be used to prevent the disclosed knowledge from bene(cid:133)ting rivals.

It is worth noting that while

demonstrating that performing research and producing scienti(cid:133)c articles play an important motivating

role for attracting scientists, it remains unclear why (cid:133)rms wish to attract scientists in the (cid:133)rst place.

Moreover, if performing research is merely a reward instrument, whether research is used in invention

5 Cockburn and Henderson (1998) conclude that participation in research "acts as a powerful recruiting tool, since the
highest quality scientists in a (cid:133)eld are often reluctant to work for private (cid:133)rms if they will not be able to publish and thus
maintain their personal scienti(cid:133)c reputation".

6

should not in(cid:135)uence investment decisions.

Basic research can also bene(cid:133)t the sponsoring (cid:133)rm by allowing it to signal its scienti(cid:133)c and tech-

nical capabilities to regulators, prospective customers, employees, or (cid:133)nanciers (Hicks, 1995; Audretsch

and Stephan, 1996; Azoulay, 2002). Lichtenberg (1986) shows that through investment in research,

(cid:133)rms can signal their capabilities to attract government contracts. Based on Compustat (cid:133)rm data and

defense-related federal procurement data he (cid:133)nds that approximately half of the increase in private R&D

investment between 1979 and 1984 was stimulated by increase in government demand. Audretsch and

Stephan (1996) suggest that collaborative research with university scientists helps biotech (cid:133)rms signal

their quality to investors. Azoulay (2002) (cid:133)nds that prescriptions for anti-ulcer drugs are in(cid:135)uenced by

publications activity by drug manufacturers. Hicks (1995) suggests that scienti(cid:133)c publications serve as

a signal of the (cid:133)rm(cid:146)s tacit knowledge and capabilities and thus enhance the technical reputation of the

(cid:133)rm. She emphasizes that by publishing in open science (cid:133)rms establish a trustworthy reputation with the

academic and scienti(cid:133)c community, which helps them in turn trade information with these communities.

The various explanations for why (cid:133)rms invest in research predict that invention productivity would

be higher in (cid:133)rms that invest in research. For instance, insofar as the (cid:133)rm invests in research to attract

talented inventors, one would also expect that talented inventors publish scienti(cid:133)c articles, and for in-

vention productivity to be higher in such (cid:133)rms. The absorptive capacity view has similar predictions if

one makes the auxiliary assumption that inventors that are active in research are better able to absorb

external knowledge, and hence, are more productive. What is distinctive is whether the coupling between

research and invention is based on the use of internally generated knowledge in the sponsoring (cid:133)rm(cid:146)s own

inventions.

There are two related implications of this distinction that can be empirically tested.

If corporate

research is principally about building reputation capital with regulators, customers, or others, it should

be more e⁄ective in doing so when others build upon it and cite it. In other words, spillovers should

enhance the e¢ cacy of the signal and internal use would merely be a welcome bonus.

If, however,

corporate research is primarily about producing more and higher quality inventions internally, spillovers,

particularly to rivals, should lower private return and reduce the incentives to invest in research. In such

case, the (cid:133)rm(cid:146)s incentives to invest are directly tied to whether its own inventors build upon the internally

7

generated research. To test this, in our empirical analysis we examine how a company(cid:146)s publication activity

is related to the use of internally generated knowledge in its own inventions as well as to the use by others

including its rivals in the product market.

3 Data

We combine data from three main sources: (i) company and accounting information from U.S. Com-

pustat, (ii) scienti(cid:133)c publications from Web of Science and (iii) patent and non-patent literature (NPL)

citation from PatStat database. Building on Arora et al. (2015), we develop new data linking corporate

publications to NPL citations to learn about the use of corporate science in invention and its implications

for corporate investment in research, R&D productivity and stock market value.

We start with all publicly traded (cid:133)rms in the U.S. annual Compustat database and select companies

with active records and positive R&D expenses for at least one year during our sample period, 1980-2006.

We exclude companies without at least one patent based on the NBER 2006 patent dataset. We also

exclude (cid:133)rms that are not headquartered in the United States. Our (cid:133)nal estimation sample consists of

an unbalanced panel of 4,736 (cid:133)rms and 57,765 (cid:133)rm-year observations. Of those (cid:133)rms, 2,413 have at least

one scienti(cid:133)c publication during the sample period.

We use scienti(cid:133)c publications as our measure of production of new scienti(cid:133)c knowledge and patents as

our measure of inventive activity. We treat a citation by a patent to a corporate publication as an indicator

that the patented invention used or built upon the knowledge in the publication. Internal citation is a

citation by a patent to a scienti(cid:133)c publication produced by the same (cid:133)rm.

Corporate publications. Similar to the method discussed in Arora et al. (2015), to measure (cid:133)rms(cid:146)

participation in scienti(cid:133)c research we match our sample (cid:133)rms to the Web of Science (WoS) database, which

covers articles published in over 5000 journals. We include articles from journals covered in the "Science

Citation Index" and "Conference Proceedings Citation Index - Science", excluding social sciences, arts

and humanities articles. Using the a¢ liation (cid:133)eld, we identify approximately 300 thousand articles with

at least one author employed by our sample of Compustat (cid:133)rms, published from 1980 through 2006.

Appendix 6.2 provides details on the matching procedure.

Patent citation to corporate science. The main methodological contribution of this paper is

8

matching NPL citations to WoS publications. Using all patents granted in the period 1980-2014, we

perform a many-to-many match between NPL citations and WoS corporate publications (approximately 14

million citations matched to 300 thousand corporate publications), allowing for more than one publication

to be matched to each citation. To exclude mismatches, we develop a specialized matching algorithm

that is based on di⁄erent sources of publication information: standardized authors(cid:146) names, number of

authors listed, article title, journal name and year of publication. The matching algorithm accounts

for misspelling, unstructured text, incomplete references, and other issues that may cause mismatches.6

Finally, we perform extensive manual checks to con(cid:133)rm matches. Details on the matching algorithm are

provided in Appendix 6.4.

Following the above procedures, we obtain 266,361 patent citations to 50,494 corporate publications

(17% of corporate publications), by 151,412 citing patents. Of the cited publications, 79% receive only

external citations and the remaining receive at least one internal citation.

Ownership structure. Due to the complexity of measuring large (cid:133)rms(cid:146)innovative activities, which

typically take place inside numerous subsidiaries (Arora et al., 2014), we aggregate the data to the

ultimate-owner-parent-company level (UO). For example, if a (cid:133)rm(cid:146)s subsidiary publishes scienti(cid:133)c articles

while the parent company is the assignee registered on the (cid:133)rm(cid:146)s patents, we record both at the UO level

and a citation from a patent to a publication would be considered as an internal citation.

The construction of the (cid:133)rm dataset presents several challenges. For instance, a parent company

and a subsidiary may have di⁄erent identi(cid:133)cation numbers and records in Compustat. Furthermore, a

single company may correspond to multiple (cid:133)rm identi(cid:133)ers due to changes in ownership structure and

accounting changes over the sample period. We detail the challenges of constructing the dataset and the

procedures we take to deal with them in Appendix 6.1.

3.1 Descriptive statistics

Our main sample and variables are at the parent company-year level. Appendix Table A1 summarizes the

de(cid:133)nition and data source for each variable. Table 1 presents descriptive statistics for our main variables

over the sample period, 1980-2006. Our sample includes a wide distribution of (cid:133)rm sizes: market value

6 An example of a front-page patent reference to a non-patent literature is presented in Appendix Figure A5.

9

ranging from 5 million dollars (10th percentile) to 2.3 billion dollars (90th percentile) and sales ranging

from 2 million dollars (10th percentile) to 2 billion dollars (90th percentile).

Table 2 presents summary statistics for the main citation variables used in the econometric analysis

for publishing (cid:133)rms. A total of 2,413 (cid:133)rms (51 percent of our sample (cid:133)rms) publish at least one scienti(cid:133)c

article. 799 (cid:133)rms receive at least one citation to their publications (an average of 1 internal and 7 external

citations per year), 388 (cid:133)rms make at least one citation to their own scienti(cid:133)c publications (an average

of 1 unique (cid:133)rm publication cited per year) and 760 (cid:133)rms receive at least one external citation to their

publication (an average of 6 unique patents citing a (cid:133)rm(cid:146)s publications per year).

Table 3 presents mean comparison tests for di⁄erences in characteristics between (cid:133)rms with high and

low internal citations for the sample of publishing (cid:133)rms with at least one citation. Firms with above mean

value share of internal citation (de(cid:133)ned as the ratio of internal citations received and the sum of internal

and external citations received) have statistically signi(cid:133)cant higher (i) number of publications, (ii) R&D

intensity and (iii) inventor-author overlap, where higher overlap indicates a stronger tie between research

and development personnel, measured as the share of patents that list at least one scientist (publication

author) as an inventor.78

Insert Tables 1-3 here

3.2 Validating patent citations to scienti(cid:133)c articles as a measure of use of science in

invention

To validate our measure of use of science(cid:150)NPL citation to WoS articles(cid:150) we utilize the Carnegie Mellon

Survey (CMS) data on industrial R&D (Cohen et al., 2000).9 Our sample includes 772 patenting (cid:133)rms

that were included in the survey with patents granted between 1991 and 1999 (a total of 29,318 patents).

Figures 1A-1C present the relationship between patent citations to science and the survey answers per-

taining to the role of science in corporate R&D. There is a strong correlation between the average number

of patent citations to science made by the surveyed (cid:133)rms(cid:146)patents and the responses of the same (cid:133)rms to

7 This measure is further discussed in section 4.2.1 as part of our instrumental variable analysis.
8 Appendix Table A3 presents a mean comparison test between patents that cite internal science and patents that do not
cite internal science. We (cid:133)nd that patents that cite internal science are of statistically signi(cid:133)cant higher quality (based on
forward patent citation received) and are in the core technology of the (cid:133)rm (core de(cid:133)ned as the four-digit IPC that has the
majority of (cid:133)rm patents in a given year).

9 We thank Michael Roach and Wesley Cohen for providing the Carnegie Mellon survey data.

10

questions on the importance of scienti(cid:133)c research for their R&D projects.

Figures 1A and 1B present mean comparisons for the average number of patent citations to publications

for (cid:133)rms with high and low survey response for the use of public science in R&D projects.10 Classi(cid:133)cation

to high and low is based on median value survey response. The (cid:133)gures show that (cid:133)rms with high

self-reported use of science also cite more public science (publications by all universities and research

institutions, Figure 1A) and articles publications by top 200 American universities (Figure 1B).1112 Figure

1C shows that the relationship between self-reported use of science and citations to science holds also

within narrowly de(cid:133)ned technology areas.13 The (cid:133)gure shows that there is a tight correspondence between

the speci(cid:133)c scienti(cid:133)c areas the (cid:133)rm reports to have in(cid:135)uenced its R&D projects and the research areas

cited by its patents.

Table 4 con(cid:133)rms that the above correlations continue to hold in a regression analysis that controls for

(cid:133)rm size, number of backward patent citations to other patents (to ensure that the e⁄ect of NPL citations

is not driven by how many backward citations the patent makes), and complete sets of four-digit industry

and year dummies.

Insert Figure 1 and Table 4 here

4 Econometric analysis

4.1 Internal citation and publication output

We estimate the relationship between internal use of research, measured by patent citations to internally

produced science, and investment in research, measured by numbers of publications authored by at least

one corporate scientist. Our baseline speci(cid:133)cation is as follows:

1 0 Based on 1994 CMS data Q.18: "During the last three years, what percentage of your R&D unit(cid:146)s projects made use of
the following research outputs produced by universities or government research institutes and labs?: a. Research (cid:133)ndings".
1 1 Top university publications were identi(cid:133)ed by matching a list of top 200 U.S. university names based on Shanghai

Ranking to the a¢ liation (cid:133)eld of each publications record.

1 2 Appendix Figure A1 shows that the same pattern holds for main industries. Appendix Figures A2-A4 present additional
supporting evidence. Figure A2 shows that citations to science are positively related to share of Ph.Ds or M.D. scientists of
all R&D employees as reported in the survey.

1 3 Based on 1994 CMS data Q.22: "Referring to the (cid:133)elds listed above, indicate the (cid:133)eld whose research (cid:133)ndings in general
(not just university and government research) contributed the most to your R&D activities during the last three years. Then,
indicate the importance of that (cid:133)eld(cid:146)s (cid:133)ndings to your R&D activities". The sample is restricted to (cid:133)rms that indicated their
main (cid:133)eld in Q22 as A-J (excluding category K -(cid:145)others(cid:146)). Publications were classi(cid:133)ed to main (cid:133)elds based on key related
words under the WoS journal subject category (cid:133)eld. For example, (cid:147)Organometallics(cid:148) Journal related subject category is
(cid:147)Chemistry, Inorganic & Nuclear; Chemistry, Organic(cid:148) accordingly it is classi(cid:133)ed under main (cid:133)eld of chemistry.

11

ln(1 + P ublicationsit) = (cid:12)0 + (cid:12)1 ln(1 + Internal citationit

1) + Z0it

(cid:0)

(cid:0)

1(cid:13) + (cid:17)i + (cid:28)t + (cid:15)it

(1)

P ublicationsit is number of publications by (cid:133)rm i in year t. Internal_citationit

1 is lagged number of

(cid:0)

patent citations made by (cid:133)rm i(cid:146)s patents granted up to year t-1 (inclusive) to its own scienti(cid:133)c publications

published up to year t-1 (inclusive). Zit

1 is a vector of lagged (cid:133)rm-year controls, including patent stock,

(cid:0)

R&D stock, and sales14. (cid:17)i and (cid:28)t are complete sets of (cid:133)rm and year dummies, respectively. (cid:15)it is and

iid error term. Our coe¢ cient of interest is (cid:12)1 and we expect

(cid:12)1 > 0: All speci(cid:133)cations include a dummy

variable for (cid:133)rm-year observations with zero publications. Table 5 presents the estimation results.

b

One main concern is that (cid:133)rms with a higher number of publications are more likely to randomly cite

one of their publications, which would upward bias

(cid:12)1. To mitigate this concern, all of our speci(cid:133)cations

include (cid:133)rm (cid:133)xed e⁄ects as well as (cid:133)rm controls for scale such as patent stock, R&D stock and sales.
b

Furthermore, our choice of the temporal structure of internal citations aims at mitigating concerns that

number of publications and internal citation are a⁄ected by common shocks (e.g., shocks to research

opportunity that a⁄ect both number of publications and number of patents).15

Column 1 presents the estimation results from a pooled speci(cid:133)cation with four-digit industry (cid:133)xed

e⁄ects. There is a positive and statistically signi(cid:133)cant relationship between internal citation and number

of publications. Column 2 presents the same pattern of results for a between-(cid:133)rm speci(cid:133)cation, which

collapses the panel data into a cross-section by averaging variables at the (cid:133)rm level. Column 3 adds

(cid:133)rm (cid:133)xed-e⁄ects.

(cid:12)1 falls sharply from 0.68 (column 1) to 0.11, indicating that the relationship between

internal citation and publications is driven largely by heterogeneity across (cid:133)rms rather than within (cid:133)rms

b

over time. Yet,

(cid:12)1 remains statistically signi(cid:133)cant. Based on the estimates from column 3 ((cid:133)rm (cid:133)xed

e⁄ect), one additional internal citation is associated with an additional 0.5 publication per (cid:133)rm-year

b

(0:11

(cid:2)

6:216=1:274).

Columns 4-8 present several robustness checks. Column 4 restricts the sample to (cid:133)rms with at least

one publication during the sample period. There is no substantial change in

(cid:12)1. Column 5 controls

1 4 R&D stock is calculated using a perpetual inventory method with a 15 percent depreciation rate (Hall et al., 2005). R&D
1 where Rt is the R&D expenditure in year t and (cid:14) = 0:15. Patent

b

stock, GRD, in year t is GRDt = Rt + (1
stock in year t is P atent stockt = P att + (1

(cid:14))GRDt
(cid:0)
(cid:14))P atent stockt

1 where P att is the number of patents in year t.

1 5 The temporal structure of citations and publications are illustrated in Appendix Figure A6.

(cid:0)
(cid:0)

(cid:0)

12

for internal patent citations to own patents ("self-citations"). While

(cid:12)1 remains stable, the coe¢ cient

estimate on self citations is statistically zero. This result is reassuring because it mitigates a concern than

b

that

(cid:12)1 captures a "self-citation" e⁄ect that might be driven by cumulative innovation capabilities (Hall

et al., 2005; Belenzon, 2012).

b

Columns 6-8 present the estimation results using alternative measures of internal citation, all yielding

the expected positive relationship with publications.161718

Insert Table 5 here

4.1.1 Heterogeneous e⁄ects

Not all citations to science are of equal importance. We expect internal citations to a⁄ect future investment

in research when the cited publication (i) is of high scienti(cid:133)c impact, (ii) is based on recent work that

is less known by others and (iii) is related to the (cid:133)rm(cid:146)s core technologies and to its valuable inventions.

These predictions are con(cid:133)rmed in our data and are reported in Table 6.

Column 1 distinguishes between citations to old vs. new science. Internal citations to new science

include only citations to articles published no later than (cid:133)ve years from the grant year of the citing patent.

While the coe¢ cient estimate on internal citation to recent science is positive and statistically signi(cid:133)cant

(0.130), internal citations to old science have no e⁄ect.

Columns 2-3 distinguish between citations to basic and applied publications using journal CHI index19

(Column 2) and Journal Impact Factor (JIF) (Column 3). In Column 2, we de(cid:133)ne basic (applied) journals

as the top (bottom) two categories of the CHI index and classify publications accordingly. In Column 3,

we classify journals as basic and applied based on their JIF value. A publication is classi(cid:133)ed as basic if it

1 6 In unreported robustness checks, we ran the analysis excluding references to articles related to clinical trial phase
in the pharmaceutical and biotech industry, which are not considered as research. We examine all publications cited by
pharmaceutical and biotech patents and identify clinical trial publications by related phrases in the title and abstract of
each publication record (e.g., clinical trial, clinical study, preclinical trial, subjects). We locate less than 100 internally cited
clinical trial publications and exclude them from the analysis. Our results remain robust.

1 7 As additional unreported robustness checks, we performed the same analysis excluding citations added by patent ex-
aminers. We also excluded citations where patent inventors cite their own publications. The results are robust in both
cases.

1 8 Columns 1-3 in Appendix Table A4 present our main results with right-hand-side variables lagged by two and three

years. The coe¢ cient estimate on internal citation remains positive and statistically signi(cid:133)cant.

1 9 Narin et al. (1976) and CHI Research develop the CHI index to classify scienti(cid:133)c journals into four research categories

ranging from applied to basic.

13

is published in a journal with above median JIF value (using the JIF value distribution in the complete

WoS database), and as applied otherwise. About 70% of internal citations are to articles published in

basic science journals (this percentage is robust across both classi(cid:133)cations) and these citations matter

the most for the production of future publications. Based on Column 3 (JIF), the coe¢ cient estimate

on internal citation to basic science is positive and statistically signi(cid:133)cant (0.122), while the coe¢ cient

estimate on internal citation to applied science is statistically zero.

Column 4 distinguishes between high and low quality publications using number of citations an article

receives from other publications, divided by average number of citations received by all WoS publications

published in the same journal-year as the focal publication. Classi(cid:133)cation of articles into high and low

quality is based on median value of normalized citations received in the corporate publications sample.

Our results indicate that only citations to high quality publications matter. While the coe¢ cient estimate

on high quality internal citation is positive and signi(cid:133)cant (0.116), the coe¢ cient estimate on citations to

low quality publications is statistically zero.

Column 5 distinguishes between use of science by patents in core and non-core technology areas of

the focal (cid:133)rm. Core citations include only citations to publications made by patents in the (cid:133)rm(cid:146)s core

technology area. Core technology is de(cid:133)ned as the IPC with the majority of the (cid:133)rm(cid:146)s patents in a given

year.20 There is a strong relationship between citations by core technology patents and future publications.

Moving from core to non-core citing patents lowers the coe¢ cient estimate on internal citation from 0.12

to 0.04.

Column 6 distinguishes between citations by high and low quality patents. Patent quality is based

on number of citations a patent receives divided by average number of citations received by all patents

granted in the same year as the focal patent. Patents are classi(cid:133)ed into high and low quality using median

value from the corporate patents sample. The relationship between internal citation and publications is

stronger for high quality citing patents, but the coe¢ cient estimates on high and low quality patents are

not statistically di⁄erent from each other (0.091 vs. 0.054).

In summary, Table 6 shows that internal patent citations to science that matter for the production

of future science are citations to recent, high quality basic publications that are made by core and high

2 0 Average number of patents in core technology areas is 8.6. About 40% of internal citations are by core patents.

14

quality patents. These results are consistent with the view that to justify further investment in research

scientists are required to demonstrate that their recent scienti(cid:133)c work is useful for the core inventive

activity of the sponsoring (cid:133)rm.

Insert Table 6 here

4.2 Exploring the causal e⁄ect of internal citations

An important concern is that internal citations and investment in research can be driven by common

unobserved or mismeasured time-varying e⁄ects, such as technological opportunity shocks or technology

specialization that can be correlated with number of publications and internal citations. This section

proposes an instrumental variable estimation strategy to mitigate this concern.

4.2.1

Inventor-author overlap

Our instrumental variable estimation is motivated by a potential determinant of internal citation: inventor-

author overlap. Arguably, (cid:133)rms should be better positioned to use the science they produce in their down-

stream development if there is a tighter link between its research and development personnel (Kline and

Rosenberg, 1986; Rosenberg, 1990).21 This link should align research priorities with downstream needs

and facilitate "back and forth" between upstream research and downstream development. In particular,

a (cid:133)rm should be better positioned to capitalize on its research if some aspects of the research (cid:133)ndings are

tacit and more easily transmitted through face-to-face interactions between researchers and inventors.

Building on this logic, the next section explores legal constraints to labor mobility that potentially

a⁄ect the overlap between research and development personnel as an instrument for internal citation.

Stronger mobility barriers should raise the overlap between researcher and inventor teams and in turn

lead to a higher internal citation rate. Importantly, there is no clear reason why mobility barriers should

a⁄ect the number of publications a (cid:133)rm produces, conditional on how these publications are used in

downstream development.

2 1 According to Rosenberg (1990, p.170): "When basic research in industry is isolated from the rest of the (cid:133)rm, whether
organizationally or geographically, it is likely to become sterile and unproductive. The history of basic research in industry
suggests that it is likely to be most e⁄ ective when it is highly interactive with the work, or the concerns of applied scientists
and engineers."

15

We construct a measure of overlap between inventors and authors at the (cid:133)rm-year level. This measure

is the share of patents with inventors who are also authors of a publication by the same (cid:133)rm published

no later than three years from the focal patent(cid:146)s grant year. Inventor-author overlap is de(cid:133)ned only for

publishing (cid:133)rms. Appendix 6.6 provides additional details on the construction of this measure.22

Columns 1-2 in Table 7 present OLS estimation results of a linear probability model that examines the

relationship between inventor-author overlap and internal citation. The dependent variable is one for (cid:133)rm-

year observations with at least one internal citation and zero otherwise. Column 1 includes a complete set

of four-digit industry dummies and Column 2 includes (cid:133)rm (cid:133)xed e⁄ects. As expected, the probability of

internal citation increases with inventor-author overlap. Based on the within-(cid:133)rm estimates (Column 2),

a one-standard deviation increase in inventor-author overlap increases the probability of internal citation

by about 30%, relative to the sample mean.23

Column 3 examines external citations and (cid:133)nds that they are unrelated to inventor-author overlap.

This result mitigates a concern that the overlap-citation relationship is driven by a higher general propen-

sity to cite as overlap increases.

4.2.2

Inevitable Disclosure Doctrine

We proceed by introducing a source of variation that should a⁄ect inventor-author overlap, but not

publications. We exploit variation in the adoption of Inevitable Disclosure Doctrine (IDD) by U.S. state

courts as an instrument for internal citation. IDD is a legal doctrine that restricts workers mobility from

one organization to another in cases where they might (cid:147)inevitably disclose(cid:148)trade secrets. It is applicable

even if the employee did not sign a non-compete or non-disclosure agreement, if there is no evidence of

actual disclosure or if the rival is located in another state. IDD status at the focal (cid:133)rm(cid:146)s state in a given

year is taken from Klasa et al. (2015) (see also Marx et al., 2009). Our instrument multiplies IDD by a

(cid:133)rm-speci(cid:133)c employment mobility risk, measured as number of rival publishing (cid:133)rms in close geographical

proximity to the focal (cid:133)rm.

Our instrument, IDD mobility, is constructed as:

2 2 Average value of inventor-author overlap is 0.2 with a median of 0.
2 3 Under the assumption that overlap should a⁄ect citations to publications of current workers, as a robustness check we
compute internal citation only for recent publications (published no later than (cid:133)ve years from the grant year of the citing
patent). The coe¢ cient estimate on inventor-author overlap increases in size and remains statistically signi(cid:133)cant.

16

IDD mobilityit = IDDst

mobility riskit

(cid:2)

Where, IDDst, is a dummy variable equals one if IDD is in e⁄ect in the focal (cid:133)rm(cid:146)s (i) state (s) in year

t. Firm address is from the publication(cid:146)s (cid:147)a¢ liation(cid:148) (cid:133)eld.24 mobility riskit is the number of publishing

(cid:133)rms in the same industry (4-digits SIC) within 100 mile of the focal (cid:133)rm in a given year. We calculate

distance between (cid:133)rms using the NBER(cid:146)s ZIP Code Distance Database.

Our main identifying assumption is that mobility barriers do not directly a⁄ect incentives to invest

in research. Thus, one has to assume that IDD adoption is uncorrelated with unobserved state-speci(cid:133)c

variables such as technological opportunities. We test this assumption by examining whether changes in

IDD status are correlated with technological opportunities, measured by patents per R&D. As shown in

Appendix Table A7, there is no relationship between changes in IDD and patents per R&D (same pattern

holds for publications per R&D).

Column 4 in Table 7 presents OLS estimation results for the relationship between IDD mobility and

inventor-author overlap. As expected, higher mobility restrictions are associated with a higher inventor-

author overlap. The estimates indicate that a two standard deviation increase in IDD mobility is asso-

ciated with an increase of 22% in inventor-author overlap (relative to the sample mean).

Columns 5-7 present within-(cid:133)rm Two-Stage Least Squares estimation results for the e⁄ect of internal

citation on publications using lagged IDD_mobility as an instrument. To mitigate possible unobserved

time-varying state heterogeneity in economic conditions that might be correlated with IDD we also control

for state employment level.25 Column 5 presents the (cid:133)rst stage estimation results, where internal citation

is regressed on lagged IDD mobility controlling for patents stock, R&D stock, sales and state employment.

The results con(cid:133)rm that higher mobility restrictions are associated with higher internal citation and that

the instrument has strong explanatory power (Kleibergen-Paap F statistic=72).

Column 7 presents the second stage estimation results where internal citation is instrumented with

IDD mobility. The IV coe¢ cient estimate on internal citation is larger than the OLS estimate in

2 4 Our algorithm accounts for cases where several publishing institutions are listed under the a¢ liation (cid:133)eld and locates
the relevant state in the string that is related to the focal (cid:133)rm. For example, (cid:147)JOHNS HOPKINS UNIV DEPT CHEM
BALTIMORE MD 21218 USA, ARCO CHEM CO NEWTOWN SQ PA 19073 USA."

2 5 Annual state employment is from U.S. Bureau of Economic Analysis (BEA).

17

Column 6 (0.6 versus 0.1). One possible explanation for the smaller IV estimate is that the OLS estimate

is downward biased due to unobserved (cid:133)rm heterogeneity, which is corrected in the IV estimation. For

example, mismeasured or unobserved (cid:133)rm specialization might be positively correlated with internal

citations (because both patents and publications are in similar (cid:133)elds they are more likely to be linked by

a citation) and negatively correlated with number of publications (because they are more focused, (cid:133)rms

perform research in a more narrow research domain). Another possible explanation for the smaller OLS

estimate is noise. If the variation used in the IV estimation captures "true" use citations,

(cid:12)1 would be

larger.26

b

Finally, Appendix section 6.7 presents an analysis that exploits a di⁄erent source of variation in internal

citation(cid:150)pro(cid:133)t shocks due to foreign exchange rate (cid:135)uctuations that a⁄ect the dependence of inventions

on science (Cyert and March, 1963; Graham at al., 2004; Bruneel et al., 2016). We (cid:133)nd that at the

industry level, foreign currency devaluation is associated with drop in pro(cid:133)ts and fewer internal citations

to science. These results are consistent with (cid:133)rms performing less exploratory, science-based, innovation

in leaner times. Our instrumental variable estimation further shows a positive and statistically signi(cid:133)cant

e⁄ect of internal citation on publications. Lastly, we include both instruments, IDD and devaluation,

in a single two-stage least-squares speci(cid:133)cation. The same pattern of results remains in the (cid:133)rst and

second stage estimations and the Hansen test for overidentifying restrictions supports the validity of the

instruments (results are presented in Appendix Table A5).

Insert Table 7 here

4.3 Knowledge spillovers

If (cid:133)rms invest in research because it is an input into internal inventive activity, the use of this research

by rivals would lower the return to such investment (Nelson, 1959; Arrow, 1962).

In this section we

investigate how investment in research is related to external citations(cid:150)citations in patents (cid:133)led by others

to the research published by the focal (cid:133)rm.

Table 8 presents the estimation results. Column 1 includes the number of external citations made

2 6 Appendix Table A4 Columns 4-6 present results for the IV estimation with right-hand-side variables lagged by two and

three years. The coe¢ cient estimate on internal citation remains positive and statistically signi(cid:133)cant.

18

to the focal (cid:133)rm(cid:146)s publications (by corporate and non-corporate patents). While the coe¢ cient estimate

on internal citation remains robust and similar in size to previous estimates (Table 5, Column 3), the

coe¢ cient estimate on external citation is negative and statistically indistinguishable from zero. A similar

relationship is found when restricting external citation to citations received only from corporate patents

(Column 2).

Not all citations represent pro(cid:133)t-reducing spillovers. Pro(cid:133)t-reducing spillovers are more likely when

a rival uses the knowledge than when an unrelated (cid:133)rm uses it. Similarly, pro(cid:133)t-reducing spillovers are

more likely when recently generated knowledge is used by a rival, rather than when the knowledge is older

and already di⁄used.

We build on Bloom et al. (2013) and Ja⁄e (1988) to construct SEGMENT and TECH as our measures

of the proximity of citing and cited (cid:133)rms in product market space and technology space, respectively.

Firms are close in product space if the distribution of sales across di⁄erent product market segments

is similar. Firms are close in technology space if the distribution of patents across technology classes

is similar. Formally, the distance in technology space is the cosine of vectors representing the share of

patents in 4-digit IPC classes for each pair of (cid:133)rms. Product market distance is measured analogously

using industry segments (4-digit SIC codes level).27 More details on the construction of SEGMENT and

TECH are provided in Appendix 6.5.

We compute two external citation variables as SEGMENT-weighted and TECH-weighted number of

outsider citations to the focal (cid:133)rm(cid:146)s publications (using SEGMENT and TECH as weights). Naturally,

only citations by corporate patents are included in this analysis. Insofar as higher SEGMENT citations

represent pro(cid:133)t-reducing spillovers, we expect these to be negatively related to publications. We make no

clear prediction for TECH citations.

Columns 3-5 present the estimation results of breaking up external citations by SEGMENT and TECH.

The coe¢ cient estimate on SEGMENT citations is negative, however statistically insigni(cid:133)cant (Column

3).

2 7 SEGMENT proximity for each cited(cid:150)citing

(cid:133)rm pair is the absolute un-centered correlation between their sales segment share vectors, calculated as

is business segment sales shares vector for (cid:133)rm i taken from Compustat(cid:146)s operating segments database. The measure ranges
from zero (least correlated) to 1. Similarly, TECH proximity is computed based on (cid:133)rm(cid:146)s patent share distribution across
technology (cid:133)elds (4-(cid:133)git IPC).

: si

Sj

S0i(cid:2)
pSi(cid:2)pSj (cid:12)
(cid:12)
(cid:12)
(cid:12)

(cid:12)
(cid:12)
(cid:12)
(cid:12)

19

Columns 4-5 restrict citations to recent publications (published no later than (cid:133)ve years from the

citing patent(cid:146)s grant year). As expected, external citations from close product market rivals are nega-

tively related to publications. Conversly, citations from close technology rivals are positively related to

publications (Column 4). This may capture unobserved (cid:133)rm-speci(cid:133)c publications quality e⁄ect(cid:150)quality

is positively correlated with citations from technology rivals and with publications production. Finally,

the SEGMENT and TECH estimates become larger in absolute value when restricting the sample to

publishing (cid:133)rms (Column 5).28

Overall, our results are consistent with the view that a (cid:133)rm(cid:146)s investment in research depends, among

other things, on how its research is used internally and externally. A (cid:133)rm whose research is used in its

own inventive activity is likely to continue investing in research. However, a (cid:133)rm whose research spills

over to rivals is likely to reduce its investment. An important empirical contribution of the present paper

is quantifying this internal/external tradeo⁄. Based on the estimates from Column 4 in Table 8, one

additional internal citation mitigates the negative e⁄ect of four segment-weighted external citations.

4.4 R&D productivity

Insert Table 8 here

We next examine whether higher internal citation implies a greater productivity of R&D investment as

measured by number of citation-weighted patents produced per R&D dollar invested. Table 9 presents

the estimation results of the following speci(cid:133)cation:

ln(1 + Citation weighted patentsit) = (cid:11)0 + (cid:11)1Share of inter citationit

1

(cid:0)

(2)

+ (cid:11)2Share of inter citationit

1

(cid:0)

(cid:2)

ln (R&D stockit

1)

(cid:0)

(cid:11)3 ln (R&D stockit

(cid:0)

1) + (cid:11)4 ln (1 + P ub stockit

1) + (cid:17)i + (cid:28)t + (cid:15)it

(cid:0)

Citation-weighted patents is the annual (cid:135)ow of patents weighted by the ratio of the number of citations

each patent receives and average number of citations received by all other patents granted in the same

year as the focal patent. Share of Inter citation is the ratio of internal citations from own patents to

2 8 The observed pattern of result is not driven by any particular industry. See Tables A6 for variation across main industries.

Appendix A2 includes a list of four-digit SIC codes included in the industry breakdown in Table A6.

20

number of citations received from all corporate patents.29 The coe¢ cients of interest are (cid:11)1 and (cid:11)2: We

expect that (cid:133)rms with more scienti(cid:133)c R&D programs to be more productive. Thus, we expect

(cid:11)1 > 0

and

(cid:11)2 > 0. As in previous analysis, all speci(cid:133)cations control for (cid:133)rm (cid:133)xed e⁄ects.

b
Column 1 shows a strong positive relationship between internal citation and R&D productivity (
b

(cid:11)1 >

0): Columns 2-3 add the interaction term between R&D stock and share of internal citation. As expected,

b

(cid:11)2 > 0 and is statistically signi(cid:133)cant. Column 3 restricts the sample to publishing (cid:133)rms with no substantial

change in the estimates.
b

4.5 Stock market value

Insert Table 9 here

If internal citation increases private returns to research, whereas spillovers to rivals reduce private returns,

this should be re(cid:135)ected not only in the level of publication output, but also in its value. We examine next

the relationship between use of research and (cid:133)rm stock market value30. Following Griliches (1986) and

Hall et al. (2005), we estimate the following speci(cid:133)cation:

ln(M arket valueit) = (cid:11)0 + (cid:11)1 ln(1 + Internal pub stockit

1) + (cid:11)2 ln(1 + External pub stockit

(cid:0)

+ (cid:11)3 ln Assetsit

1 + Z0it

(cid:0)

(cid:0)

1(cid:13) + (cid:17)i + (cid:28)t + (cid:15)it

1)

(cid:0)

(3)

Internal pub stock and External pub stock are publications stock weighted by number of internal and

external citations each publication receives, respectively31. Assets is the book value of physical capital32

and Z is a vector of controls including lagged sales, R&D stock and patents stock. The coe¢ cient estimates

are amenable to di⁄erent interpretations. We interpret these coe¢ cients as re(cid:135)ecting the imputed value

attributable to the relevant asset, or the "shadow price" of the asset (Hall et al., 2005). Our interest is

at the coe¢ cients (cid:11)1 and (cid:11)2: We expect

(cid:11)1 > 0 and

(cid:11)2 < 0: Table 10 presents the estimation results.

2 9 Average value of Share of Inter citation is 0.013 with a standard deviation of 0.093.
3 0 Market value is the sum of common stock, preferred stock and total debt net of current assets.
b
3 1 Publications stock is computed as Internal pub stockt = Internal pubt+ Internal pub stockt

1, where Internal pubt is
the number of internal citations publications receive in year t: External pub stockt is computed in an equivalent way with
external citations received. For example, if a publication receives one internal citation and two external citation, it adds one
to Internal pub stockt and two to External pub stockt:

b

(cid:0)

3 2 Calculated as the sum of net plant, property and equipment, inventories, investments in unconsolidated subsidiaries, and

intangibles other than R&D.

21

Consistent with previous research, Column 1 shows a positive relationship between publications stock

and market value (Arora et al., 2015). Column 2 breaks up publications stock into internally- and

externally-cited publications. As expected,

(cid:11)1 > 0, but contrary to our expectation

(cid:11)2 > 0 (signi(cid:133)cant at

the 5% level).

b

b

Column 3 distinguishes between external citations received from rivals in product markets and those

from other (cid:133)rms in the same technical domains. Thus, External pub stock is broken up into two separate

measures, one where external citations are weighted by product market proximity (SEGMENT) and an-

other where external citations are weighted by technology market proximity (TECH). This decomposition

of external citations leads to a negative and statistically signi(cid:133)cant coe¢ cient estimate on SEGMENT, as

expecred. The coe¢ cient estimate on TECH is positive, similar to our (cid:133)ndings from Column 4, Table 8.

The estimates from Table 10, Column 3 indicate that one additional internal citation weighted publi-

cation mitigates the negative market value e⁄ect of approximately 3 external SEGMENT-weighted pub-

lications. Taken together, the evidence from Table 10 supports the view that private return to research

is positively related to its internal use in invention, but negatively related to its use in invention by close

product market rivals.

5 Conclusion

Insert Table 10 here

Using data on 4,736 publicly traded American (cid:133)rms over the period 1980-2006, this paper studies the

relationship between use of corporate research in invention and corporate production of science. We sys-

tematically match all NPL (non-patent literature) references to publication records from Web of Science

to learn about how corporate research is used in invention. Our primary contribution is providing sys-

tematic evidence of the private economic value of corporate research as an input into internal inventive

activity and demonstrating that investment in research is strongly tied to how research bene(cid:133)ts technology

development.

We make several empirical contributions. First, we show that patent citations to scienti(cid:133)c publications

are a good measure of use of science in invention. We utilize the Carnegie Mellon Survey to show that

(cid:133)rms whose patents cite science also report greater use of science in their R&D projects. Second, we show

22

that (cid:133)rms that are able to use their research in their inventions produce more of it. This relationship

is stronger for new, high quality basic research and for citing patents in the core technology area of the

inventing (cid:133)rm. We supplement these (cid:133)ndings by showing that internal use is associated with higher R&D

productivity and stock market valuation of scienti(cid:133)c publications stock. Third, spillovers reduce private

value and (cid:133)rms publish less when their research spills over to product market rivals.

Our (cid:133)ndings support the view that (cid:133)rms invest in research because its scienti(cid:133)c output feeds into

downstream technology development. Our paper contributes to the growing discussion of why American

(cid:133)rms are withdrawing from investment in science (Arora et al., 2015). To understand the causes and

implications of the decline in corporate research, we must (cid:133)rst develop a better understanding of why

(cid:133)rms invest in research in the (cid:133)rst instance. Over time, (cid:133)rms will invest less in research if the output

of their research becomes relatively less important for the technology they develop, and spills over to

product market rivals.

References

[1] Adams, J.D., 1990. Fundamental stocks of knowledge and productivity growth. Journal of Political

Economy, 98(4), pp.673-702.

[2] Arora, A., Belenzon, S. and Patacconi, A., 2015. Killing the golden goose? The decline of science in

corporate R&D (No. w20902). National Bureau of Economic Research.

[3] Arora, A., Belenzon, S. and Rios, L.A., 2014. Make, buy, organize: The interplay between research,

external knowledge, and (cid:133)rm structure. Strategic Management Journal, 35(3), pp.317-337.

[4] Arrow, K., 1962. Economic welfare and the allocation of resources for invention. In The rate and
direction of inventive activity: Economic and social factors (pp. 609-626). Princeton University Press.

[5] Audretsch, D.B. and Stephan, P.E., 1996. Company-scientist locational links: The case of biotech-

nology. The American Economic Review, 86(3), pp.641-652.

[6] Azoulay, P., 2002. Do pharmaceutical sales respond to scienti(cid:133)c evidence?. Journal of Economics &

Management Strategy, 11(4), pp.551-594.

[7] Belenzon, S., 2012. Cumulative innovation and market value: evidence from patent citations. The

Economic Journal, 122(559), pp.265-285.

[8] Bikard, M., 2015. Peer-Based Knowledge Validation: A Hurdle to the Flow of Academic Science to

Inventors. Available at SSRN 2333413.

23

[9] Bloom, N., Schankerman, M. and Van Reenen, J., 2013. Identifying technology spillovers and product

market rivalry. Econometrica, 81(4), pp.1347-1393.

[10] Breschi, S. and Catalini, C., 2010. Tracing the links between science and technology: An exploratory

analysis of scientists(cid:146)and inventors(cid:146)networks.Research Policy, 39(1), pp.14-26.

[11] Bruneel, J., D(cid:146)Este, P. and Salter, A., 2016. The impact of (cid:133)nancial slack on explorative and ex-
ploitative knowledge sourcing from universities: evidence from the UK. Industrial and Corporate
Change, 25(4), pp.689-706.

[12] Bush, V., 1945. Science: The endless frontier. Transactions of the Kansas Academy of Science (1903-),

48(3), pp.231-264.

[13] Carlson, W.B., 2013. Innovation and the Modern Corporation. Companion Encyclopedia of Science

in the Twentieth Century, p.203.

[14] Cockburn, I.M. and Henderson, R.M., 1998. Absorptive capacity, coauthoring behavior, and the
organization of research in drug discovery. The Journal of Industrial Economics, 46(2), pp.157-182.

[15] Cohen, W.M. and Levinthal, D.A., 1989. Innovation and learning: the two faces of R & D. The

economic journal, 99(397), pp.569-596.

[16] Cohen, W.M., Nelson, R.R. and Walsh, J.P., 2000. Protecting their intellectual assets: Appropri-
ability conditions and why US manufacturing (cid:133)rms patent (or not) (No. w7552). National Bureau of
Economic Research.

[17] Cyert, R.M. and March, J.G., 1963. A behavioral theory of the (cid:133)rm. Englewood Cli⁄s, NJ, 2

[18] Dasgupta, P. and David, P.A., 1994. Toward a new economics of science.Research policy, 23(5),

pp.487-521.

[19] David, P.A., Mowery, D. and Steinmueller, W.E., 1992. Analysing the economic payo⁄s from basic

research. Economics of innovation and New Technology, 2(1), pp.73-90.

[20] Gambardella, A., 1992. Competitive advantages from in-house scienti(cid:133)c research: The US pharma-

ceutical industry in the 1980s. Research Policy, 21(5), pp.391-407.

[21] Gambardella, A., Panico, C. and Valentini, G., 2015. Strategic incentives to human capital. Strategic

Management Journal, 36(1), pp.37-52.

[22] Gans, J.S., Murray, F.E. and Stern, S., 2013. Contracting over the disclosure of scienti(cid:133)c knowledge:
Intellectual property and academic publication (No. w19560). National Bureau of Economic Research.

[23] Graham, JR., CR Harvey and Rajgopal, S., 2005 The economic implications of corporate (cid:133)nancial

reporting. Journal of accounting and economics, 40 (1), 3-73.

24

[24] Griliches, Z., 1986. Productivity, R and D, and Basic Research at the Firm Level in the 1970(cid:146)s. The

American Economic Review, 76(1), pp.141-154.

[25] Griliches Z. 1981. Market value, R&D, and patents. Economics Letters 7(2): 183(cid:150)187.

[26] Hall, B.H., Ja⁄e, A. and Trajtenberg, M., 2005. Market value and patent citations. RAND Journal

of economics, pp.16-38.

[27] Henderson, R. and Cockburn, I., 1994. Measuring competence? Exploring (cid:133)rm e⁄ects in pharmaceu-

tical research. Strategic management journal,15(S1), pp.63-84.

[28] Hicks, D., 1995. Published papers, tacit competencies and corporate management of the pub-

lic/private character of knowledge. Industrial and corporate change, 4(2), pp.401-424.

[29] Hicks, D., Breitzman, T., Olivastro, D. and Hamilton, K., 2001. The changing composition of inno-

vative activity in the US(cid:151) a portrait based on patent analysis. Research policy, 30(4), pp.681-703.

[30] Hounshell, D.A. and Smith, J.K., 1988. Science and Corporate Strategy: Du Pont R and D, 1902-

1980. Cambridge University Press.

[31] Ja⁄e, A.B., 1988. Demand and supply in(cid:135)uences in R & D intensity and productivity growth. The

Review of Economics and Statistics, pp.431-437.

[32] Klasa, S., Ortiz-Molina, H., Ser(cid:135)ing, M. and Srinivasan, S., 2015. Protection of trade secrets and

capital structure decisions. Available at SSRN 2439216.

[33] Kline, S.J. and Rosenberg, N., 1986. An overview of innovation. The positive sum strategy: Harness-

ing technology for economic growth, 14, p.640.

[34] Kuznets, S., 1971. Prize Lecture: Modern Economic Growth: Findings and Re(cid:135)ections. Nobel-

prize.org.

[35] Levin, R.C., Klevorick, A.K., Nelson, R.R., Winter, S.G., Gilbert, R. and Griliches, Z., 1987. Ap-
propriating the returns from industrial research and development. Brookings papers on economic
activity, 1987(3), pp.783-831.

[36] Lichtenberg, F.R., 1986. Private Investment in R&D to Signal Ability to Perform Government Con-

tracts. NBER Working Paper, (w1974).

[37] Maclaurin, W.R., 1953. The sequence from invention to innovation and its relation to economic

growth. The Quarterly Journal of Economics, pp.97-111.

[38] Mans(cid:133)eld, E., 1980. Basic research and productivity increase in manufacturing. The American Eco-

nomic Review, 70(5), pp.863-873.

[39] Marx, M., Strumsky, D. and Fleming, L., 2009. Mobility, skills, and the Michigan non-compete

experiment. Management Science, 55(6), pp.875-889.

25

[40] McMillan, G.S., Narin, F. and Deeds, D.L., 2000. An analysis of the critical role of public science in

innovation: the case of biotechnology. Research policy, 29(1), pp.1-8.

[41] Mowery, D.C., 1995. International Computer Software Industry. Oxford University Press, Inc.

[42] Narin, F., Pinski, G., & Gee, H. H. (1976). Structure of the biomedical literature. Journal of the

American Society for Information Science, 27(1), 25-45.

[43] Narin, F. and Noma, E., 1985. Is technology becoming science? Scientometrics, 7(3-6), pp.369-381.

[44] Narin, F., Hamilton, K.S. and Olivastro, D., 1997. The increasing linkage between US technology

and public science. Research policy, 26(3), pp.317-330.

[45] Nelson, R.R., 1959. The simple economics of basic scienti(cid:133)c research. Journal of political economy,

67(3), pp.297-306.

[46] Popp, D., 2016. From Science to Technology: The Value of Knowledge From Di⁄erent Energy Re-

search Institutions (No. w22573). National Bureau of Economic Research.

[47] Reich, L. S., 1985. The Making of American Industrial Research. New York: Cambridge University

Press.

[48] Rosenberg, N., 1990. Why do (cid:133)rms do basic research (with their own money)?. Research policy,

19(2), pp.165-174.

[49] Sauermann, H. and Cohen, W.M., 2010. What makes them tick? Employee motives and (cid:133)rm inno-

vation. Management Science, 56(12), pp.2134-2153.

[50] Stern, S., 2004. Do scientists pay to be scientists? Management science,50(6), pp.835-853.

6 Appendix.

6.1 Sample construction

We implement various matching procedures to construct two main datasets, one at the (cid:133)rm-year level
and another at the citation-publication level, including (i) matching scienti(cid:133)c publications to Compustat
companies; (ii) mapping patent citations to publications; (iii) matching patent data to Compustat; and
(iv) dynamic matching of Compustat accounting information. We discuss these procedures below.

A parent company and a subsidiary may have di⁄erent identi(cid:133)cation numbers and records within
the Compustat data. Also, a single company may correspond to multiple (cid:133)rm identi(cid:133)ers (CUSIPs or
GVKEYs) within the Compustat database due to changes in ownership structure and accounting changes
over the sample period that can lead to a change in its identi(cid:133)cation number. Appendix Table B1
illustrates the challenges in assigning a unique id over time based on the (cid:133)rm id in Compustat. To deal
with these challenges, we implement several procedures.

First, we rely on the NBER 2006 patent data project, which corresponds to our subsample years,
to identify multiple Compustat records that are associated with a single company in our subsample.

26

Second, we further merge parent Compustat companies and independent Compustat subsidiaries and
related joint-ventures that appear in our initial subsample using the (cid:147)CGS Associated Issuers(cid:148)database,
which links related issuers in the Compustat database and other online sources. For example, we merge
ARMSTRONG WORLD INDUSTRIES under its holding company ARMSTRONG HOLDINGS INC
as well as merge the joint venture, DOW CORNING CORP, under both his parent companies, DOW
CHEMICAL and CORNING INC. We manually modify the NBER data according to these changes.
Third, we uniquely identify each parent company by a 9-digit CUSIP (our UO-COMPANY variable) and
up to (cid:133)ve associated CUSIPs in case of multiple related (cid:133)rm CUSIPs and subsidiary CUSIPs. In addition
to our UO-COMPANY identi(cid:133)er, we assign each company a unique NBER (cid:147)PDPCO(cid:148)code. This enables
us to dynamically match our dataset with Compustat accounting data and with NBER patent data. We
exclude from our sample non-patenting (cid:133)rms. Lastly, we exclude (cid:133)rms that are not headquartered in
the United States, based on Compustat current records. Appendix Table B2 presents an example of the
dynamic match.

The above procedures leave us with our (cid:133)nal estimation sample of an unbalanced panel including
4,736 publicly traded US headquartered companies and 57,765 (cid:133)rm-year observations over the period
1980-2006. These (cid:133)rms have at least one year of positive R&D expenditures and at least one patent from
1980 through 2006.

6.2 Matching scienti(cid:133)c publications to Compustat companies

After obtaining our initial subsample of (cid:133)rms we proceed to match our (cid:133)rm sample to publications data
to capture their investment in science. We obtain publications data from the Web of Science database
(previously known as ISI Web of Knowledge). We include articles from journals covered in the "Science
Citation Index" and "Conference Proceedings Citation Index - Science," excluding social sciences, arts
and humanities articles.

Each publication record contains detailed information including title of the publication, authors, jour-
nal info and our main variable of interest, an a¢ liation (cid:133)eld with name and address of the publishing
institute or company in case of a corporate publication. This (cid:133)eld can include more than one listing
in case of a collaborative publication, for example, (cid:147)DARLEY M (reprint author), TEXAS INSTRU-
MENTS INC, DEPT DATAPATH VLSI PROD SEMICOND GRP 8330 LBJ FREEWAY, POB 655303,
DALLAS, TX 75265 USA SUN MICROSYST INC, MT VIEW, CA USA(cid:148).

Companies appear in the Compustat (cid:133)le under their most current name with no records of previous
names. Since company names may change over the course of our sample years (e.g., due to mergers and
acquisitions), we manually search online sources (e.g., Bloomberg, Opencorporates, Crunchbase websites)
and check older Compustat datasets and the (cid:147)CGS Associated Issuers(cid:148) in order to identify previous
names relevant to our sample period. For example, EG&G, which changed its name to "PerkinElmer
Inc" in 1999 after buying the Analytical Instrument division from Perkin-Elmer will appear under both
names in our dataset. Similarly, (cid:147)APPLIED MOLECULAR GENETICS INC (cid:148), which changed its name
in 1983 to (cid:147)AMGEN INC (cid:148) will appear under both names in our dataset, as well as the pharmaceuti-
cal company (cid:147)WYETH (cid:148), which up to 2002 was known as (cid:147)AMERICAN HOME PRODUCTS (cid:148), (cid:147)3M
CO(cid:148), formerly known as the (cid:147)MINNESOTA MINING AND MANUFACTURING COMPANY (cid:148), and

27

(cid:147)SPECTRA DIODE LAB (cid:148), which changed its name to (cid:147)SDL, INC (cid:148). In addition to the parent company
name we also check related subsidiary names using SDC Platinum (M&A data) and other online sources.
Lastly, we allocate abbreviations that are commonly used by companies instead of their o¢ cial name.
For example, (cid:147)INTERNATIONAL BUSINESS MACHINES CORP (cid:148), will also appear under its common
abbreviation (cid:147)IBM (cid:148) and (cid:147)GENERAL ELECTRIC CO(cid:148) under (cid:147)GE.(cid:148)

Company name was (cid:133)rst standardized by cleaning all non- alphabetic characters as well as Compu-
stat related indicators and converting all strings to uppercase characters. Where possible, we omitted
legal entity endings and other common words (e.g.
INC, CORP, LTD, PLC, THE, LAB, PHARMA-
CEUTICAL) to maximize the matching rates (e.g., (cid:147)XEROX CORP (cid:148) was standardized to (cid:147)XEROX (cid:148),
(cid:147)ABBOTT LABORATORIES (cid:148) to (cid:147)ABBOTT (cid:148)). However, in cases where the company(cid:146)s name is too
short, generic or can match to other strings within the address (cid:133)eld, we preserved the original name to
avoid mismatches. For example, omitting the legal entity from (cid:147)QUANTUM CORP (cid:148)would mismatch it to
various research institutions such as (cid:147)TEXAS STATE UNIV CTR APPL QUANTUM ELECTR DEPT (cid:148).
Similarly, (cid:147)MALLINCKRODT INC (cid:148)can mismatch with (cid:147)EDWARD MALLINCKRODT INST (cid:148)or with
(cid:147)HARVARD UNIV MALLINCKRODT CHEM LAB (cid:148)and (cid:147)KELLOGG CO(cid:148)can mismatch with (cid:147)M.W.
KELLOGG(cid:148). For cases where we cannot omit the legal entity, we try adding additional relevant names
to improve the match, for example for (cid:147)MERCK & CO(cid:148) we also include (cid:147)MERCK RESEARCH LAB (cid:148)
and for (cid:147)GTE CORP (cid:148) we include (cid:147)GTE LAB (cid:148). To further improve the quality of match, we obtained
the list of most frequent company names of the (cid:133)rst publisher within the a¢ liation string and adjusted
our company name list accordingly.

One last step in standardizing the company names is to (cid:133)t it to the publication a¢ liation (cid:133)eld format
that contains many abbreviated words. For this process, we formed a list that includes over 80 abbreviated
words matched to their various origins as well as to other forms of abbreviations. For example, LABORA-
TORIES, LABORATORY, LABS, LABO, LABORATORIE, LABORATARI, LABORATARIO, LABO-
RATARIA, LABORATORIET and LABORATORIUM were all abbreviated to (cid:147)LAB(cid:148). The list was
compiled from the most frequent abbreviated words in the Address (cid:133)eld (accordingly, the list is targeted
to our sample). Appendix Table B3 presents a list of the most frequent abbreviated words.

Finally, we apply a many-to-many match between each standardized company name and the a¢ liation
(cid:133)eld for each publication (approximately 14mm publications and 5.5K names), while allowing for more
than one (cid:133)rm to be matched to each publication (to allow for collaborative publications). We use STATA(cid:146)s
(cid:147)regexm(cid:148) command33 to detect whether the a¢ liation (cid:133)eld contains each company name. In addition to
our automated algorithm, we perform extensive manual checks to detect cases that can cause mismatches
and verify matches by comparing the address listed within Compustat to the address in the publication
data. For example, to distinguish between (cid:147)THERATECH INC / UTAH (cid:148)and (cid:147)THERATECH INC (cid:148)we
verify that the address of the (cid:133)rm under the a¢ liation (cid:133)eld is in Salt Lake City.

We (cid:133)nd approximately 300 thousand articles from more than 5000 di⁄erent journals that were pub-
lished from 1980 through 2006, with at least one author employed by our sample of Compustat (cid:133)rms. At
the end of this procedure, we obtain a match between a unique publication id and a UO company id.

3 3 Stata(cid:146)s (cid:147)strdist(cid:148) command is based on the Levenshtein distance score, which measures the distance between two strings

by the minimum number of character edits required to gain an exact match.

28

6.3 Matching patent data

We apply the strategy used in the NBER 2006 patent data project (Hall et al., 2001) to perform a dynamic
match of patents to our subset of Compustat (cid:133)rms. The NBER dynamic reassignment of patents accounts
for changes in Compustat identi(cid:133)cation numbers and M&A reassignment of patents based on SDC data.
We make manual adjustments to the NBER data based on our aggregation of the data under a parent
(cid:147)UO(cid:148)company. For example, while BOEING CAPITAL CORP and BOEING CO are treated as separate
companies in the NBER database, we merge BOEING CAPITAL CORP under BOEING CO as it is a
wholly owned subsidiary of the company. We adjust the NBER data in such way that all of BOEING
CAPITAL CORP patents are assigned to BOEING CO. Using this process we identify the original UO
(cid:133)rm of each patent and also account for reassignment of patents over time. In case a patent has several
assignees, we match the patent to several (cid:133)rms and assign fractional patent ownership to each assignee
(i.e., 1/number of assignees).

6.4 Matching NPL citations to Web of Science

Patent citations to science are obtained from the Non-Patent Literature (NPL) citations section located
at the front page of patents taken from PatStat database. An example of a front-page patent citation
to non-patent literature is provided in Appendix Figure A5. Using all patents granted in the period
1980-2014 (including corporate and non-corporate patents), we match NPLs to corporate publications
from Web of Science (approximately 14mm citations and 300k corporate publications). This is a central
match and the most challenging one, due to di⁄erences in structure between NPLs and publications. We
begin with a many-to-many match, allowing more than one publication to be matched to each citation.
For each possible records pair, we construct a score that captures the degree of textual overlap between
the title, journal, authors and publication year. To exclude mismatches, we use a more detailed matching
algorithm that is based on di⁄erent sources of publication information: standardized authors(cid:146) names,
number of authors, article title, journal name and year of publication. The matching algorithms accounts
for misspelling, unstructured text, incomplete references, and other issues that may cause mismatches.34
The (cid:133)rst step is to match between the publication(cid:146)s (cid:147)Title(cid:148) (cid:133)eld and the title that is located within
the citation string. There are two main problems: (i) the position of the title within the citation is not
(cid:133)xed (ii) there may be small variation in the title (e.g., (cid:147)GIVE(cid:148) vs. (cid:147)GIVES(cid:148)) and thus an exact match
may not perform well. To overcome these problems we implement a fuzzy match algorithm. After we
standardize and clean the di⁄erent (cid:133)elds, we measure the length-di⁄erence between the citation string
and the publication title string. Then, using STATA(cid:146)s (cid:147)strdist(cid:148) command we calculated the distance
between the two strings. We use the di⁄erence between the length di⁄erence and distance as a measure
of proximity of the titles. We supplement this measure with an exact match of the (cid:133)rst part of the title.
In some cases the title is missing from the citation string. In such cases we rely more on other available

3 4 The following example (from the (cid:133)rst line in Appendix Table B4) illustrates the matching challenge. NPL citation:
LIN, KUN SHAN, ET AL., SOFTWARE RULES GIVES PERSONAL COMPUTER REAL WORD POWER , INTER-
NATIONAL ELECTRONICS, VOL. 53, NO. 3, FEB. 10, 1981, PP. 122 125. Matched Publication: Title: SOFTWARE
RULES GIVE PERSONAL-COMPUTER REAL WORD POWER, Authors: LIN KS, FRANTZ GA, GOUDIE K, Journal
information: ELECTRONICS 54 (3): 122-125 1981.

29

features to determine the (cid:133)nal match.

Second, we match between the publication(cid:146)s (cid:147)Authors(cid:148)(cid:133)eld and the authors listed within the citation
string. As with the title, we cannot identify the exact location where the authors are listed within
the citation string since the location varies from one citation to another. In addition, there are several
di⁄erences in how names are written: (i) Last name only vs. full names; (ii) names vs. initials (e.g., LIN
KS vs. LIN KUN SHAN); (iii) listing of all authors vs. one author followed (or not) by (cid:147)et al.(cid:148); (iv)
order of last and (cid:133)rst names within the string. To verify a match by authors we (cid:133)rst count the number
of authors listed in the publication record. We then check whether the citation string contains (cid:147)et al.(cid:148).
To mitigate the name variation problem, we implement an algorithm that matches di⁄erent variations of
the authors(cid:146)name to the citation (including transformation of last and/or (cid:133)rst and/or middle name to
initials and changes in order listed). In cases where several authors are listed under the publication and
(cid:147)et al.(cid:148) does not appear within the citation we perform a one-to-many match between the citation and
each author and assume that at least 80% of the authors must be matched to the citation to determine a
match. For cases where several authors are listed in the publication and only one is matched within the
citation while (cid:147)et al.(cid:148) is omitted, we rely more on match results in other features to determine the (cid:133)nal
match.

Next, we match journal information including standardized journal(cid:146)s name, year published, page
numbers and volume, while accounting for typos, abbreviations and di⁄erences in format between the
datasets (e.g., (cid:147)INTERNATIONAL ELECTRONICS(cid:148)vs. (cid:147)ELECTRONICS(cid:148); (cid:147)VOL. 53, NO. 3(cid:148)vs. (cid:147)54
(3)(cid:148)).

Finally, we combine the match results for the di⁄erent features (title, authors and journal information)
using di⁄erent weights according to their relative importance, in order to determine a (cid:133)nal match. We
perform extensive manual checks to con(cid:133)rm matches. At the end of this procedure, we obtain unique
identi(cid:133)cation numbers for the citation, the citing patent and the cited publication.

6.5 SEGMENT and TECH proximity measures

We build on Bloom et al. (2013) and Ja⁄e (1988) to construct the measures SEGMENT and TECH
as the correlations between (cid:133)rm pairs. SEGMENT proximity is computed based on the distribution of
line of business listed within the Compustat operating segments database. We use the dynamic match
as explained previously to match our UO (cid:133)rms to Compustat segment database and calculate their sales
share over the complete sample period (1980-2006) in each segment. There are a total of 60 segments (out
of 69 available) related to our citing and cited (cid:133)rms. We generate a vector for each UO (cid:133)rm based on the
distribution of sales share in each of these 60 segments. The SEGMENT proximity for each cited(cid:150)citing
where Si denotes the
(cid:133)rm pair is the absolute un-centered correlation between their vectors,
vector of the shares of (cid:133)rm i(cid:146)s sales in di⁄erent segments. In case of several assignee (cid:133)rms matched to
the cited patent, we compute the average distance between the di⁄erent (cid:133)rms. The measure ranges from
zero (least correlated) to one (fully correlated).

S0i(cid:2)
(cid:2)

Sj
pSj

pSi

Similarly, TECH is computed based on each (cid:133)rm(cid:146)s patent share distribution across di⁄erent technology
(cid:133)elds. We generate a vector for each UO (cid:133)rm based on its granted patents share in each 3-digit main IPC

30

over the complete sample period (1980-2006). The TECH proximity for each cited(cid:150)citing (cid:133)rm pair is the
where Ti denotes the
absolute un-centered correlation distance between their IPC-share vectors,

T 0i (cid:2)
(cid:2)

Tj
pTj

pTi

vector of the shares of (cid:133)rm i(cid:146)s patents in the di⁄erent technology (cid:133)elds.

6.6 Inventor-author overlap

Inventor-author overlap is measured as the share of patents per (cid:133)rm-year that include an inventor who
is also an author of a corporate publication by the same (cid:133)rm published no later than 3 years from the
patent(cid:146)s grant year.

We perform the following steps to construct the overlap measure. First, we standardize inventor and
author names for all non-collaborative patents and corporate publications related to our sample (cid:133)rms
during the sample period (1980-2006). For patent inventor names, we use the HBS Patent Inventor
Database that identi(cid:133)es individual inventors for each patent and conveniently lists their (cid:133)rst-name and
last-name in separate (cid:133)elds. For publication author names, we use the publication(cid:146)s author list, which
lists names by last name followed by initials (e.g., (cid:147)MALIK RJ , HAYES JR , CAPASSO F , ALAVI K
, CHO AY(cid:148)). The standardized name format we implement for the match is last name followed by (cid:133)rst
name initial, all in uppercase letters (e.g., MALIK R).

Next, for each (cid:133)rm-grant year we perform a many to many match between each patent(cid:146)s inventor-
standardized names and author-standardized names of publications published by the focal (cid:133)rm up to 3
years prior to the patent(cid:146)s grant year. For example, IBM patent US6013336 (granted in 2000) includes an
inventor, Peter Baumgart, who also published a paper in 1997: (cid:147)Wang, R.H., Raman, V., Baumgart, P.,
Spool, A.M. and Deline, V., 1997. Tribology of laser textured disks with thin overcoat. IEEE Transactions
on Magnetics, 33(5), pp.3184-3186.(cid:148)

Finally, we compute for each (cid:133)rm-grant year the share of non-collaborative patents that their inventor
list includes at least one author of a corporate publication published by the (cid:133)rm up to 3 years prior to the
patent(cid:146)s grant year. The average value of inventor-author overlap is 0.21 median is 0, standard deviation
is 0.33 and the 10th and 90th percentile values are 0 and 0.9, respectively. Figures B1-B2 show that there
is heterogeneity in inventor-author overlap across our sample (cid:133)rms.

6.7 Instrumental variable II: Pro(cid:133)t shocks due to exchange rate (cid:135)uctuations

A di⁄erent source of variation in internal use arises from changes in the mix of downstream innovation
activities. Whereas incremental innovation is less likely to use science, including internally generated
science, exploratory innovation is more likely to build on scienti(cid:133)c advances and be guided by them.
Exploration has more uncertain outcomes and is less likely during lean times. Put di⁄erently, exploratory
innovation requires (cid:133)nancial slack, because "slack provides a source of funds for innovations that would
not be approved in the case of scarcity" (Cyert and March, 1963, p. 279). The opposite relationship has
been argued between slack and exploitation. Exploitative innovation, also called (cid:145)problemistic search(cid:146),
is directed towards (cid:133)nding an immediate solution to a speci(cid:133)c problem (Levinthal and March, 1981;
March, 1991; Greve, 2003, 2007; Bruneel et al., 2016). For example, Bruneel et al. (2016), building on
survey data from 2002-2006, (cid:133)nd that high levels of (cid:133)nancial slack (measured by cash (cid:135)ow) are associated

31

with British (cid:133)rms(cid:146)engagement in explorative knowledge sourcing from universities, whereas low levels of
slack are associated with exploitative knowledge sourcing. Moreover, consistent with the (cid:146)slack search(cid:146)
view, Graham at al. (2004) report that 80% of the 401 executives they surveyed would decrease their
discretionary R&D spending and delay starting a new project in order to meet an earning target.

We exploit (cid:133)nancial shocks using foreign currency devaluations for export-oriented American (cid:133)rms.
When dollar-denominated pro(cid:133)ts drop due to a stronger US dollar (USD), (cid:133)rms would engage in more
exploitation and less exploration. Assuming that exploitation builds less on science, we expect less internal
use of research (that is, patent citations to own science) as (cid:133)rm patents become more exploitative and
less exploratory. The main idea is that exchange rates a⁄ect pro(cid:133)ts of (cid:133)rms with foreign subsidiaries, and
pro(cid:133)ts in turn a⁄ect the decision of (cid:133)rms to exploit science. Our identifying assumption is that short-term
pro(cid:133)t shocks a⁄ect the decision of (cid:133)rms to use science, but short-term pro(cid:133)t shock does not a⁄ect the
value of scienti(cid:133)c research independently from its e⁄ect on use. Speci(cid:133)cally, we assume that (i) the future
pro(cid:133)ts depend upon the realized level of exchange rates, so that conditioning on current exchange rates,
the long run value of research is una⁄ected for a given level of internal use, and (ii) shocks to exchange
rates lead to changes in internal use. We demonstrate that negative shocks to exchange rates lead to a
decrease in pro(cid:133)tability and that negative exchange rate shocks shift downstream innovation away from
exploration and towards exploitation, as re(cid:135)ected in reduced patent citations to science. We assume that
in turn this will also reduce internal use of the (cid:133)rm(cid:146)s own science.

Our instrument uses the yearly change in foreign exchange rates weighted by (cid:133)rm-speci(cid:133)c weights.
We use two sets of weights: (i) foreign subsidiaries by (cid:133)rm i in each country and (ii) the industry-level
export of goods between the US and each foreign country in the main industry of (cid:133)rm i. We include
only manufacturing (cid:133)rms (SIC 20-39). The data are for the years 1990-2006 (which allow us to include
subsidiaries in former USSR countries). The weighted change in exchange rates is computed as:

(cid:1)dit =

c
X

j
X

Sic

(cid:2)

Exportjct

(cid:1)dtc

(cid:2)

Where, (cid:1)dit is (cid:133)rm-year change in the weighted-average value of foreign currency relative to USD.
It includes only manufacturing industries and covers the years 1990 to 2006. Higher (cid:1)dit means USD
becomes stronger indicating a negative shock to USD-denominated pro(cid:133)ts. (cid:1)dtc is the change in the USD
denominated value of country(cid:146)s c currency between years t and t-1. Annual exchange rates are o¢ cial
exchange rates from the World Bank(cid:146)s World Development Indicators. We compute an annual average
based on monthly averages (local currency units relative to the U.S. dollar). For countries adopting the
Euro currency, we adjusted (cid:1)dtc to zero, for the year of the currency change. Changes in annual exchange
rate vary from a 10th percentile value of -0.09 to 90th percentile value of 0.24 (mean of 0.22 and standard
deviation of 1.4). Examples of extreme devaluation include the Brazilian Real that depreciated by more
than 1600% during 1993 and 1994, the Indian Rupee depreciated by 30% between 1990-1991, the Chinese
Renminbi that depreciated by 50% between 1993-1994 and the British Pound Sterling that depreciated
by 17% between 1992-1993.

Sic is the share of subsidiaries (cid:133)rm i has in country c of all subsidiaries owned by (cid:133)rm i. Subsidiaries
information for our sample (cid:133)rm are from the 2014 Orbis database, maintained by Bureau VanDyke. The

32

average (cid:133)rm has 54 foreign subsidiaries in 8 di⁄erent countries. Example of a¢ liates(cid:146)countries include:
Great Britain (9%), Germany (7%), France (6%), Netherlands (5%), Italy (4%), China (4%), Brazil (3%),
India (3%), Russia (1%). Exportjct is the share of export by industry j (where (cid:133)rm i operates) to country
c in year t. Annual industry export (cid:135)ows between US and foreign countries are based on Schott (2010)35.
(cid:1)dit varies from a 10th percentile value of -0.38 to 90th percentile value of 0.45 (mean of 0.02 and standard
deviation of 0.5) for our estimation sample.

Appendix Table A5 presents the estimation results. Our sample is conditioned on (cid:133)rm with at least
one publication stock. It includes 1901 publishing (cid:133)rms, out of which 981 (cid:133)rms have subsidiaries in 52
di⁄erent countries. We compute a dummy variable based on the measure, which receives the value of 1
for devaluation ((cid:1)dit>0). We lag (cid:1)d dummy by two periods as our instrument for one-period lagged
internal use and control for the level of exchange rate, dit.36

Columns 1-4 present the relationship between (cid:1)d dummy with pro(cid:133)ts (EBIDTA) and the use of
science(cid:150)the average number of patent citations to non-patent literature (NPL), per patent. Consistent
with our proposed mechanism, foreign currency devaluation is associated with drop in pro(cid:133)ts. Based on
the estimates from Column 1 and evaluated at the sample average, devaluation is associated with 8%
drop in EBIDTA. In other words, exchange rates shocks a⁄ect short-term pro(cid:133)tability.

Columns 2-4 further show foreign currency devaluation is associated with drop in use of science.
Column 2 shows that devaluation is associated with reduction of 0.5 citations per patent to the non-
patent literature (NPL) which is equivalent to a 9.7% decrease at the mean. Column 3 shows that results
hold when restricting the sample to (cid:133)rm-years with patents. Based on the estimates from Column 3,
devaluation is associated with 12.5% decrease in average NPL per patent. For Column 4 the dependent
variable is share of patents per year with at least one citation to NPL. Evaluated at the sample average,
devaluation is associated with 12% drop in share of patents citing NPL. These results are consistent with
(cid:133)rms conducting less exploratory inventive activity in leaner times. It is plausible that this would also
imply less use of internal science.

Columns 5-7 present the results using devaluation as an instrument for internal use. The (cid:133)rst stage
estimation instruments internal citation with a dummy variable for (cid:1)dit>0. As expected, devaluation
of foreign currencies is negatively associated with internal use. Based on the estimates from Column 5,
devaluation is associated with 8.1% decrease in average internal use (a decrease of 0.65 internal cites).
We reject the test for weak instruments with a Kleibergen-Paap F statistic=59 (Staiger and Stock, 1997).
Column 7 presents the second stage estimation results, regressing the log of number of publications
against the predicted lagged use of science due to pro(cid:133)tability shocks. The coe¢ cient estimate on internal
citation increases from 0.9 (OLS estimation, Column 6) to 1.4. Based on this estimate, a 10 percent
increase in internal citation is associated with approximately 14% increase in annual publications.

Lastly, Columns 8-10 include jointly our two instruments, IDD and devaluation, in a single two-
stage least-squares speci(cid:133)cation. The same pattern of results remains in the (cid:133)rst and second stage
estimations. The Hansen test for overidentifying restrictions is consistent with the instruments being

3 5 Data are available for download at: http://faculty.som.yale.edu/peterschott/sub_international.htm
3 6 dit =

dtc, where dtc is the exchange rate of country(cid:146)s c currency in USD at time t.

Exportjct

Sic

(cid:2)

(cid:2)

c
X

j
X

33

valid; we are unable to reject the null hypothesis that the instruments are uncorrelated with the error
term and correctly excluded from the estimated speci(cid:133)cation (p-value for overidentifying restrictions=0.44,
Hansen J statistic=0.59).

References

[1] Bruneel, J., D(cid:146)Este, P. and Salter, A., 2016. The impact of (cid:133)nancial slack on explorative and
exploitative knowledge sourcing from universities: evidence from the UK. Industrial and Corporate
Change, 25(4), pp.689-706.

[2] Cyert, R.M. and March, J.G., 1963. A behavioral theory of the (cid:133)rm. Englewood Cli⁄s, NJ, 2.

[3] Graham, JR., CR Harvey and Rajgopal, S., 2005 The economic implications of corporate (cid:133)nancial

reporting. Journal of accounting and economics, 40 (1), 3-73.

[4] Greve, H.R., 2003. A behavioral theory of R&D expenditures and innovations: Evidence from

shipbuilding. Academy of management journal, 46(6), pp.685-702.

[5] Greve, H.R., 2007. Exploration and exploitation in product innovation. Industrial and Corporate

Change, 16(5), pp.945-975.

[6] Hall, B. H., A. B. Ja⁄e, and M. Trajtenberg (2001). "The NBER Patent Citation Data File:

Lessons, Insights and Methodological Tools." NBER Working Paper 8498.

[7] Klasa, S., Ortiz-Molina, H., Ser(cid:135)ing, M. and Srinivasan, S., 2015. Protection of trade secrets and

capital structure decisions. Available at SSRN 2439216.

[8] Levinthal, D. and March, J.G., 1981. A model of adaptive organizational search. Journal of Eco-

nomic Behavior & Organization, 2(4), pp.307-333.

[9] March, J.G., 1991. Exploration and exploitation in organizational learning. Organization science,

2(1), pp.71-87.

[10] Schott, P., 2010. US manufacturing exports and imports by SIC or NAICS category and partner

country, 1972 to 2005. Notes.

[11] Staiger, D. and Stock, J.H., 1997. Instrumental Variables Regression with Weak Instruments.

Econometrica, 65(3), pp.557-586.

34

VARIABLE
Publications count
Publications stock
Patents stock

Patents count
R&D expenditures($mm)
R&D stock($mm)

Table 1. Summary Statistics for Main Variables

# Obs.
32,923

32,923

57,765

57,765

57,765

57,765

# Firms
2,413

2,413

4,736

4,736

4,736

4,736

Mean
9

104

65

12

55

231

Std. Dev.
51

762

379

74

319

1,467

10th
0

0

0

0

0.25

0.5

Distribution
50th
0

2

3

0

5

17

90th
9

75

75

14

67

260

Market value ($mm)
2,271
Sales ($mm)
1,997
Assets ($mm)
1,237
Inventor-author overlap
0.9
Notes: This table provides summary statistics for the main variables used in the econometric analysis. The sample is at the firm-year level and includes an unbalanced
panel of 4,736 US HQ publicly traded companies (out of which 2,413 are publishing companies) over the sample period, 1980-2006. These firms have at least one year
with positive R&D expenditures and at least one patent during the sample period. The sample for all publication variables is restricted to publishing firms. Inventor-
author overlap is the share of patents per year with inventors who include at least one author of a publication published by the same firm in the three-year window prior to
the patent's grant year. For Inventor-author overlap, the sample is conditional on at least one publication stock and on firm-years with granted patents.

15,280
8,063
6,281
0.3

57,765
57,765
57,765
16,538

4,736
4,736
4,736
2,081

2,105
1,394
954
0.2

87
66
30
0

5
2
1
0

Table 2. Summary Statistics for Citations Variables (only firms with cites to own publications)

VARIABLE
Total patent citations to own publications
Internal patent citations to own publications
External patent citations to own publications
Notes:  This table provides summary statistics for the main citation variables used in the econometric analysis. The sample is at the firm-year level
and is conditional on firms with positive patent citations to publications.

(1)
Number of firms
with positive
values
799
388
760

(2)

Average value
per firm-year
8
1
7

(3)
Number of citing
patents per firm-
year
7
1
6

(4)
Number of cited
publications per
firm-year
5
1
4

Table 3. High Internal Use vs.  Low Internal Use (only firms with cites to own publications)

(1)

Std. Dev.
VARIABLE
0.4
Publications flow/R&D expenditures
0.5
Patents stock/R&D expenditures
2.8
R&D expenditures/Sales
Inventor-author overlap
0.3
Notes:  This table presents mean comparison tests for firms with high share of internal citations vs.  firms with low share of internal citations. Share of internal citations is the ratio of
citations the firm's publications receive from its own patents to total citations received. The sample is conditional on firms with positive citations. The unit of analysis is a firm, yearly
values are averaged over the period 1980-2006. * and **  denote that the difference in means is significant at the 5% and 1% level, respectively.

(3) minus (6)
       0.1**
       0.06
       1.3**
       0.2**

Std. Dev.
0.5
0.4
5.2
0.3

(2)
(4)
(3)
High Share of internal citations (> median)
Mean
Obs.
0.3
388
0.43
388
2.3
388
0.4
388

(5)
(7)
(6)
Low Share of internal citations (≤ median)
Mean
Obs.
0.2
411
0.37
411
1.0
411
0.2
411

Table 4. Supporting Evidence from Carnegie Mellon Survey
Dependent variable: CMS questions

Response to CMS questions:
Citations to top 200 universities articles

Citations to public science articles

Citations to articles in main research field

Citations to corporate articles

Citations to patents

ln(Sales)

Industry dummies
Observations
R-squared

(1)

(2)

Importance of public research
findings (Q.18)

(3)
Importance of the
main research field's
findings (Q.22)

(4)
Importance other
firm's research
findings (Q.16)

(5)

Basic research
share (Q.45)

0.337
(0.146)

0.001
(0.006)
0.078
(0.032)

Yes
555
0.39

0.246
(0.120)

0.001
(0.006)
0.074
(0.034)

Yes
555
0.39

0.148
(0.065)

-0.002
(0.005)
0.040
(0.020)

Yes
495
0.46

0.453
(0.161)
-0.003
(0.007)
-0.016
(0.027)

Yes
555
0.41

1.821
(0.697)

-0.043
(0.037)
0.023
(0.174)

Yes
557
0.39

Notes:  This table presents OLS estimation results for the relationship between average patent citation to publications per patent and the 1994
Carnegie Mellon survey (CMS) questions response (Cohen et al., 2000) related to the importance of research findings as an input to the firm’s R&D
projects. The relevant CMS questions are mentioned in the main text. The sample includes only patenting firms. In Column 3, the sample is restricted
to firms that indicated their main research field in Q22 (excluding ‘Others’ category). For Citations to articles in main research field , publications
were classified to research fields based on WoS journal subject category. Citations to corporate articles include citation to publications by our main
sample of Compustat firms. Citations to patents include backward citations to patents. Robust standard errors in parentheses.

Table 5. Internal Use and Publication Output

Dependent variable: ln(1+number of publications)
(1)

(2)

(3)

(4)

Pooled
0.681

(0.042)

Between-
firms
1.692

Within-firms
0.110

Publishing
firms only
0.098

(0.113)

(0.026)

(0.025)

(7)
Share internal
citation of total
citation
received by
own pubs

(8)

Share internal
citation of total
citation made to
corp pubs

(5)

(6)

 Internal
citation,
average per
patent

Backward
patent
citation to
own patents
0.103

(0.026)
0.014
(0.007)

0.094
(0.007)

0.142
(0.012)

0.028
(0.005)

0.076
(0.007)

0.133
(0.009)

0.023
(0.005)

0.065
(0.009)

0.073
(0.011)

0.047
(0.006)

0.096
(0.014)

0.085
(0.014)

0.088
(0.010)

0.06
(0.009)

0.065
(0.012)

0.047
(0.006)

0.035
(0.018)

0.066
(0.004)

0.080
(0.005)

0.047
(0.003)

0.099
(0.035)

0.066
(0.004)

0.079
(0.005)

0.047
(0.003)

0.068
(0.032)

0.066
(0.004)

0.080
(0.005)

0.047
(0.003)

ln(1+Internal citation to publications)t-1

ln(1+Self-citation)t-1

Internal patent citation, average per patent

Internal citation/Total citations receivedt-1

Internal citation/Total citations madet-1

ln(R&D stock)t-1

ln(1+Patent stock)t-1

ln(Sales)t-1

No
Yes
Yes
5.2
3.6
4,634
53,029
0.64

Firm fixed-effects
Industry dummies (4 digit)
Year dummies
Sample average Publication
Std. Internal citation variable
Number of firms
Observations
R-squared
Notes:  This table presents OLS estimation results for the relationship between past internal patent citation to own publications and future annual publications, for the period 1980-
2006. Internal citation to publications include patent citations up to year t-1 to publications published up to the same year. Column 2 averages variables at the firm level and performs
a cross section analysis. In Column 5, Self-citation  is defined as average number of patent citations to own patents per firm-year. In Column 6, internal citations are measured as
average citations to own publications, per corporate patent. In Column 7, share of internal citations is defined as ratio of citations the firm's publications receive from own patents to
total citations received by the focal firm’s publications. In Column 8, share of internal citations is defined as ratio of citations the firm's publications received from own patents to
total citations to corporate science made by the focal firm’s patents. All specifications include a dummy variable that receives the value of one for firms that never published up to the
focal year. Standard errors (in brackets) are robust to arbitrary heteroscedasticity and allow for serial correlation through clustering by firms.

Yes
-
Yes
5.2
3.6
4,634
53,029
0.87

Yes
-
Yes
9.1
4.7
2,380
30,510
0.85

Yes
-
Yes
5.2
0.107
4,634
53,029
0.87

Yes
-
Yes
5.2
3.6
4,634
53,029
0.87

Yes
-
Yes
5.2
0.2
4,634
53,029
0.87

Yes
-
Yes
5.2
0.093
4,634
53,029
0.87

No
Yes
Yes
2.9
1.8
4,634
4,634
0.66

Table 6. Internal Use and Publication Output: Heterogeneous Effects

(1)

Dependent variable: ln(1+number of publications)
(3)
 Basic vs.
Applied
Publications
(JIF)

(2)
 Basic vs.
Applied
Publications
(CHI)

(4)

(5)

(6)

High vs. Low
quality
Publications

Core vs. Non-
Core Tech

High vs.
Low quality
Patens

New vs. Old
science
0.130
(0.017)
0.028
(0.015)

ln(1+Internal citation to publications, NEW)t-1

ln(1+Internal citation to publications, OLD)t-1

ln(1+Internal citation to publications, BASIC)t-1

ln(1+Internal citation to publications, APPLIED)t-1

ln(1+Internal citation to publications, High Quality)t-1

ln(1+Internal citation to publications, Low Quality)t-1

ln(1+Internal citation to publications, CORE)t-1

ln(1+Internal citation to publications, NON-CORE)t-1

ln(R&D stock)t-1

ln(1+Patent stock)t-1

ln(Sales)t-1

0.132
(0.015)
-0.003
(0.021)

0.122
(0.014)
-0.007
(0.022)

0.065
(0.004)

0.074
(0.005)

0.047
(0.003)

0.065
(0.004)

0.075
(0.005)

0.047
(0.003)

0.065
(0.004)

0.074
(0.005)

0.047
(0.003)

0.116
(0.014)
0.001
(0.024)

0.065
(0.004)

0.074
(0.005)

0.047
(0.003)

0.091
(0.016)
0.054
(0.018)

0.065
(0.004)

0.074
(0.005)

0.047
(0.003)

0.120
(0.017)
0.044
(0.016)

0.065
(0.004)

0.074
(0.005)

0.047
(0.003)

Difference of coefficients (significance level)
Firm fixed-effects
Year dummies
Dependent variable sample average
Number of firms
Observations
R-squared
Notes:  This table presents OLS estimation results for the relationship between past patent citations to own publications and future annual publications,
while distinguishing between different types of internal citations. All Internal citation variables include patent citations up to year t-1 to publications
published up to the same year. See main text for exact variable definition.  All specifications include a dummy variable that receives the value of one for
firms that never published up to the focal year. Standard errors (in brackets) are robust to arbitrary heteroscedasticity and allow for serial correlation
through clustering by firms.

0.005
Yes
Yes
5.2
4,634
53,029
0.87

0.000
Yes
Yes
5.2
4,634
53,029
0.87

0.000
Yes
Yes
5.2
4,634
53,029
0.87

0.001
Yes
Yes
5.2
4,634
53,029
0.87

0.000
Yes
Yes
5.2
4,634
53,029
0.87

0.212
Yes
Yes
5.2
4,634
53,029
0.87

Table 7. Instrumental Variable Estimation: Inventor-Author Overlap, Inevitable Disclosure Doctrine and Publication Output (Sample:
Publishing Firms)

(1)

(2)

(3)

(4)

(5)

(6)

(7)

Inventor-Author Overlap

IV: Inevitable Disclosure Doctrine

Dependent variable:

Dummy for internal citation

Dummy for
external citation

Inventor-author
overlap

Inventor-Author overlapt

IDD-Mobilityt-2

ln(Internal citation to own publications)t-1

ln(1+Publication stock)t-1

ln(1+Patent stock)t-1

ln(R&D stock)t-1

ln(Sales)t-1

ln(Total employment at state level)t-1

ln(1+Publication stock)t-2

ln(Patent stock)t-2

ln(R&D stock)t-2

ln(Sales)t-2

Firm fixed-effects
Industry dummies
Year dummies

Pooled
0.152
(0.012)

Firm FE
0.079
(0.011)

Firm FE
-0.009
(0.012)

0.061
(0.004)
0.023
(0.003)
0.005
(0.003)

-0.002
(0.002)

0.065
(0.006)
0.031
(0.005)
0.007
(0.005)

0.006
(0.004)

0.142
(0.007)
0.032
(0.006)
-0.001
(0.007)

-0.002
(0.005)

No
Yes
Yes

Yes
-
Yes

Yes
-
Yes

Firm FE

0.003
(0.001)

0.042
(0.004)

-0.014
(0.002)
0.004
(0.003)
-0.012
(0.003)

Yes
-
Yes

ln(1+Internal
citation)t-1
First  Stage

 ln(1+Number of publications)

OLS

2SLS

0.017
(0.002)

0.020
(0.004)
0.076
(0.005)

0.012
(0.004)
-0.001

(0.009)

0.111
(0.012)

0.130
(0.010)
0.055
(0.007)

0.127
(0.008)
0.021

(0.023)

0.670
(0.104)

0.116
(0.010)
0.011
(0.011)

0.120
(0.009)
0.030

(0.023)

Yes
-
Yes

Yes
-
Yes

Yes
-
Yes

0.08
2,259
23,466
0.54

0.08
2,259
23,466
0.36

Weak identification(Kleibergen-Paap)
0.19
Dependent variable sample average
2,259
Number of firms
23,466
Observations
R-squared
0.61
Notes: for this table the sample is conditional on at least one publication stock over the sample period, 1980-2006. Columns 1-3 present OLS estimation results for the relationship
between inventor-author overlap and citation to science. Dummy for internal (external) citation is equal to one if the firm receives at least one internal (external) citation at the focal
year to any of its publication published up to the focal year. Inventor-author overlap is measured by the share of patents per year with inventors who include at least one author of a
publication published by the same firm in the three-year window prior to the patent's grant year. IDD-Mobility is equal to the status of the Inevitable Disclosure Doctrine (IDD) per
the focal firm's state-year (i.e., for effective IDD equals to one) multiplied by a mobility risk measure that is based on the number of publishing firms within 100 miles in the same
industry. Specifications include a dummy variable that receives the value of one for firms with no patents at the focal year. Columns 5-7 present Two-Stage Least Squares estimation
results for the effect of patent citations to own publications on the number of future publications, using IDD-Mobility as an instrumental variable. Standard errors (in brackets) are
robust to arbitrary heteroscedasticity and allow for serial correlation through clustering by firms.

F=72
0.65
2,199
22,226
0.64

0.14
2,199
22,226
0.60

12
2,199
22,226
0.87

12
2,199
22,226
-0.01

Table 8. Knowledge Spillovers: External Citation and Publication Output

Dependent variable:  ln(1+Number of publications)

(1)

(2)
All cites

(3)

(4)

(5)

5 years citing lag

ln(1+Internal citation to publications)t-1

ln(1+External citation to own publications)t-1

ln(1+External citation to own publications,
SEGMENT)t-1

ln(1+External citation to own publications,
TECH)t-1

ln(R&D stock)t-1

ln(1+Patent stock)t-1

ln(Sales)t-1

Citation received,
by SEGMENT and
TECH
0.118

Citation received,
by SEGMENT and
TECH
0.111

Publishing firms
only
0.100

(0.014)

(0.016)

(0.015)

All patents
0.121

Corporate patents
0.117

(0.027)

-0.018
(0.027)

(0.026)

-0.013
(0.026)

-0.047

(0.030)

0.015

(0.022)

0.065
(0.004)

0.075
(0.005)

0.047
(0.003)

-0.080

(0.040)

0.135

(0.025)

0.064
(0.004)

0.073
(0.005)

0.047
(0.003)

-0.106

(0.038)

0.144

(0.024)

0.095
(0.006)

0.085
(0.007)

0.088
(0.005)

0.065
(0.009)

0.074
(0.011)

0.047
(0.006)

0.065
(0.009)

0.074
(0.011)

0.047
(0.006)

Difference of coefficients (significance level)
Firm fixed-effects
Year dummies
Dependent variable sample average
Number of firms
Observations
R-squared
Notes: This table presents OLS estimation results for the relationship between external and internal patent citation to own publication and future annual publications, for the
period 1980-2006. All the citation variables include patent citations up to year t-1 to publications published up to the same year. SEGMENT and TECH measure the product
market proximity and the technology market proximity, respectively. In Column 1, external citation include corporate and non-corporate patent citations. Columns 2-5 include
only external citation from corporate patents. Columns 4-5 include citations to publications published no earlier than five years prior to the citing patent. All specifications
include dummy variable that receives the value of one for firms that never published up to the focal year. Standard errors (in brackets) are robust to arbitrary
heteroscedasticity and allow for serial correlation through clustering by firms.

0.000
Yes
Yes
9.1
2,380
30,510
0.85

0.000
Yes
Yes
5.2
4,634
53,029
0.87

0.213
Yes
Yes
5.2
4,634
53,029
0.87

0.001
Yes
Yes
5.2
4,634
53,029
0.87

0.000
Yes
Yes
5.2
4,634
53,029
0.87

Table 9. Internal Use and Patent Production

(1)

(2)

(3)

  Dependent variable:  ln(1+Number of citation-weighted patents)
Interaction Within
firms

Within firms

Publishing firms
only

Share of internal citationt-1

ln(R&D stock)t-1 ×  Share of internal
citationt-1

ln(R&D stock)t-1

ln(1+Publication stock)t-1

0.198
(0.047)

0.166
(0.006)

0.137
(0.008)

-0.603
(0.168)

0.154
(0.031)

0.165
(0.006)

0.135
(0.008)

-0.509
(0.155)

0.131
(0.029)

0.256
(0.013)

0.135
(0.013)

Yes
Yes
0.093
4,634
53,029
0.86

Firm fixed-effects
Year dummies
Std. Share of internal citation
Number of firms
Observations
R-squared
Notes:  This table presents results OLS estimation results of a patent equation, for the period 1980-2006. Patents are
weighted by citations. Share of internal citations is defined as ratio of citations the firm's publications receive from
own patents to citations received from all patents. All specifications include a dummy variable that receives the
value of one for firm-years without patents and a dummy variable that receives the value of one for firm-years
without citations. Standard errors (in brackets) are robust to arbitrary heteroscedasticity and allow for serial
correlation through clustering by firms.

Yes
Yes
0.093
4,634
53,029
0.86

Yes
Yes
0.138
2,259
23,466
0.87

Table 10. Stock Market Value and Use

Dependent variable:  ln(Market value)

(1)

(2)

(3)

ln(1+Publication stock)t-1

ln(1+Publication stock weighted by internal citation)t-1

ln(1+Publication stock weighted by external citation)t-1

ln(1+Publication stock weighted by external citation,
SEGMENT)t-1

ln(1+Publication stock weighted by external citation, TECH)t-1

ln(1+Patent stock)t-1

ln(R&D stock)t-1

ln(Sales)t-1

ln(Assets)t-1

Pub stock
weighted by inter
& exter citation

Exter-cited pub
stock weighted
by SEGMENT
and TECH

0.053

(0.017)

0.031

(0.013)

0.001
(0.012)
0.070
(0.012)
0.009
(0.007)
0.201
(0.010)

0.075

(0.018)

-0.081

(0.035)

0.069

(0.029)
0.005
(0.012)
0.071
(0.012)
0.009
(0.007)
0.201
(0.010)

Pub stock

0.083

(0.014)

-0.004
(0.012)
0.066
(0.012)
0.008
(0.007)
0.201
(0.010)

Difference of coefficients (significance level)
Firm fixed-effects
Year dummies
Dependent variable sample average
Number of firms
Observations
R-squared
Notes: This table presents OLS estimation results for the relationship between citation-weighted publication stock and
stock market value, for the period 1980-2006. In Column 2, publication stock is weighted by its internal and external
citations from patents granted up to 2014. In Column 3, external cited publications are weighted by product market
proximity (SEGMENT) and the technology market proximity (TECH), between the citing patent and cited publication.
Publication stock includes WoS publications of our sample firms, published over the sample period (1980-2006).
Standard errors (in brackets) are robust to arbitrary heteroscedasticity and allow for serial correlation through clustering
by firms.

0.049
Yes
Yes
2,080
4,223
39,734
0.81

Yes
Yes
2,080
4,223
39,734
0.81

Yes
Yes
2,080
4,223
39,734
0.81

Variable

Description

Data Source

Table A1. Main Variables Definition

Publications count

Publication stock

Patent count

Patent Stock

Publication count for firm I in year t, including all publications with at least one author employed by the focal firm.
Publication stock in year t for firm I is calculated by: Publication_stockt=Pubt+Publications_stockt-1, where Pubt is the focal firm's
publication count in year t.
Patent count in year t for firm i
Patent stock in year t for firm i is calculated by: Patent_stockt=Patentt+Patent_stockt-1, where Patentt is the focal firm's patent count in
year t.

Internal citation to publications

Annual flow of internal patent citations to firm's i own publications

External citations to firm’s own publications

External citations to firm's own publications,
SEGMENT

Annual flow of external patent citations to firm's i publications. Includes citations by corporate and non-corporate patents.
Annual flow of external patent citations  to firm's i publications, weighted by product market proximity of the citing and cited firms.
Product market proximity is computed based on each firm's sales share distribution across line of business listed within the Compustat
operating segments database.

External citations to firm's own publications,
TECH

Annual flow of external patent citations to firm's i publications, weighted by technology market proximity of the citing and cited firms.
Technology market proximity is computed based on each firm’s patent share distribution across different technology fields.

Share of internal citations

Inventor-author overlap

Market value

R&D stock

Assets

Share of internal citations to science  is defined as ratio of internal-citations from own patents to internal and external citations received
by corporate and non-corporate patents, per year.

The share of patents per year with inventors who include at least one author of a publication published by the same firm in the three-year
window prior to the patent's grant year.
Following Griliches (1981), market value per firm-year is defined as the sum of the values of common stock, preferred stock, and total
debt net of current assets. Tobin’s-Q  is defined as the ratio of market value to assets.

R&D stock per firm-year is calculated using a perpetual inventory method with a 15 percent depreciation rate (Hall et al., 2005), such that
the R&D stock, GRD, in year t is GRDt=Rt+(1-δ)GRDt-1 where Rt is the focal firm's R&D expenditure in year t based on Compustat data
and δ=0.15.
The book value of capital includes net plant, property and equipment, inventories, investments in unconsolidated subsidiaries, and
intangibles other than R&D.

U.S. Compustat

U.S. Compustat

Web of Science articles, covered in "Science Citation Index" and
"Conference Proceedings Citation Index-Science", 1980-2006

Web of Science
NBER 2006 patent data project

NBER 2006 patent data project
PatStat database and citation match for patents granted at the
focal year and publications published from 1980 until the focal
year.
PatStat database and citation match for patents granted at the
focal year and publications published from 1980 until the focal
year.
Compustat operating segments database, PatStat database and
citation match for patents granted at the focal year and
publications published from 1980 until the focal year.
PatStat database and citation match for patents granted at the
focal year and publications published from 1980 until the focal
year.
PatStat database and citation match for patents granted at the
focal year and publications published from 1980 until the focal
year.
Web of Science, NBER 2006, HBS Patent Inventor Database.
Including all non-collaborative patents and  publications related
to our sample firms during the sample period (1980-2006),

U.S. Compustat

Table A2. SIC Classification by Main Industries

Category
Telecommunication
IT & Software

Description
Telecom, Communication- system, equipment, services
IT & Software - Development, Provider, Sale & Services

Machinery/equipment/system

Energy

Chemicals

Manufacture /sale/ rent - Machinery, Systems, Equipment, Instruments,
Components and Tools not elsewhere included (e.g., medical, lab, heating,
transportation,  construction,  measurement)
Electricity, Oil, Gas, Power station-  including: utility, exploration,
equipment, services, machinery, tools, etc.

Chemicals- Manufacture & Sale

Electronics & Semiconductor
Drugs, Pharmaceuticals and Biotechnology

Electronic products and equipments including components; semiconductor;
computers including system and components -Manufacture, Sale & Rent
Drugs, pharmaceuticals & biotech- Manufacture, Sale & Services

Related 4-digit sic codes in our sample of firms
3661 3663 3669 4812 4813 4822 4832 4833 4841 4899
5040 5045 5734 7370 7371 7372 7373 7374
3420 3430 3433 3510 3523 3524 3530 3531 3532 3533 3537 3540 3541
3550 3555 3559 3560 3561 3562 3564 3567 3569 3580 3585 3590 3711
3713 3714 3715 3716 3728 3743 3760 3790 3812 3821 3822 3823 3824
3825 3826 3827 3829 3841 3842 3843 3844 3845 3873 5047 5070 5080
5084 7359

1311 1381 1382 1389 1600 1623 1700 2911 2990 4922 4923 5172
1000 1040 1220 1221 2800 2810 2820 2821 2840 2842 2851 2860 2870
2890 2891 3320 3330 3334 3341 3350 3357 3360 3390 5160
3570 3571 3572 3575 3576 3577 3578 3579 3600 3612 3613 3620 3621
3630 3634 3640 3651 3670 3672 3674 3677 3678 3679 3690 3695 3861
5063 5064 5065
2833 2834 2835 2836 5122 5912 8731

Table A3. Corporate patents that cite science vs.  do  not cite  science, 1980-2006

(1)

(2)

(3)
(5)
(4)
Patents that cite science

(6)

(7)
Patents that cite internal science

(8)

(9)
(10)
Patents that do not cite science

(11)

(4) minus
(10)
       5.6**
       0.06**

(7) minus
(10)
       4.7**
       0.02**

Variable
Forward citations
Core patents
Notes:  This table presents mean comparison tests for corporate patents that cite  vs. do not cite (internal) science. The sample includes all patents related to our sample firms
granted over the period 1980-2006. Patent that cite internal science include patents with at least one citation to the firm's own publications.** denotes that the difference in
means is significant at the 1 percent level.

Std. Dev.
51
0.5

Std. Dev.
45
0.5

Obs.
656,164
656,164

Std. Dev.
33
0.5

Obs.
10,460
10,460

Obs.
32,310
32,310

Mean
24.3
0.43

Mean
25.1
0.46

Mean
19.6
0.40

Table A4. Internal Use and Publication Output- Different Lags

Dependent variable: ln(1+number of publications)

ln(1+Internal citation to publications)t-x

ln(R&D stock)t-x

ln(1+Patent stock)t-x

ln(Sales)t-x

ln(Total employment at state level)t-x

Weak identification(Kleibergen-Paap)

Firm fixed-effects
Year dummies

(1)

Lag 1
0.110

(0.026)
0.065
(0.009)

0.073
(0.011)

0.047
(0.006)

(2)
OLS
Lag 2
0.080

(0.013)
0.062
(0.004)

0.056
(0.005)

0.054
(0.003)

(3)

Lag 3
0.063

(0.013)
0.058
(0.004)

0.044
(0.006)

0.054
(0.003)

Yes
Yes

Yes
Yes

Yes
Yes

(4)

(5)
IV IDD (Sample: Publishing Firms)
Lag 1
Lag 3
Lag 2
0.480
0.521
0.670

(6)

(0.104)
0.011
(0.011)

0.116
(0.010)

0.120
(0.009)

0.030
(0.023)
F=72

Yes
Yes

(0.108)
0.095
(0.011)

0.001
(0.012)

0.130
(0.010)

0.033
(0.025)
F=70

Yes
Yes

(0.112)
0.071
(0.012)

-0.004
(0.013)

0.117
(0.010)

0.032
(0.028)
F=63

Yes
Yes

Dependent variable sample average
Number of firms
Observations
R-squared
Notes: The table presents OLS estimation result (Columns 1-3) and Two-Stage Least Squares estimation results (Columns 4-6) for the relationship
between past internal patent citations to own publications and future annual publications, for the period 1980-2006, for different lags of right hand
side variables. Internal citations to own publications include patent citations up to year t-1 to publications published up to the same year. For the
IV estimation, the sample is conditioned on at least one publication stock. The endogenous variable, internal citation to publications, is
instrumented by the IDD-Mobility measure. Standard errors (in brackets) are robust to arbitrary heteroscedasticity and allow for serial correlation
through clustering by firms.

5
4,634
53,029
0.87

6
4,430
48,395
0.87

12
2,199
22,226
-0.01

6
4,104
43,965
0.88

13
1,938
17,969
-0.01

14
1,717
15,124
-0.03

Table A5. Instrumental Variable Estimation II: Changes in Foreign Exchange Rates (Sample: Publishing Firms)

(1)

(2)

(3)

(4)

(5)

OLS

(6)
IV: Devaluation

(7)

(8)

(9)
IVs: IDD and Devaluation

(10)

Dependent variable:

ln(Internal citation to publications)t-1

Devaluation dummyt-2

Inevitable disclosure doctrine dummyt-2

ln(R&D stock)t-1

ln(1+Patent stock)t-1

ln(Assets)t-1

Exchange rate levelt

ln(Total employment)t-1

Firm fixed-effects
Industry dummies
Year dummies

Profits
(EBIDTA)

Publishing
firms

Avg. NPL citations per patent

Publishing
firms

Exc. zero
patents

Share of
patents with
NPL>0

Publishing
firms

ln(1+Internal
citation)t-1

First  Stage

-33.266

(11.577)

-0.097

(0.031)

-0.125

(0.043)

-0.044

(0.010)

88.434
(9.969)

-0.074
(0.007)

-0.100
(0.009)

-0.028
(0.002)

Yes
-
Yes

No
Yes
Yes

No
Yes
Yes

No
Yes
Yes

-0.081

(0.010)

0.068
(0.003)

0.093
(0.004)

-0.020
(0.002)
-0.001

(0.001)

No
Yes
Yes

 ln(1+Number of
publications)

OLS
0.886

(0.040)

0.244
(0.019)

0.066
(0.016)

-0.006
(0.010)
0.001

(0.001)

No
Yes
Yes

IV
1.408

(0.232)

0.209
(0.017)

0.019
(0.022)

0.006
(0.007)
0.001

(0.001)

No
Yes
Yes

ln(1+Internal
citation)t-1

First  Stage

-0.079

(0.011)
0.023

(0.008)

0.067
(0.003)

0.093
(0.004)

-0.019
(0.002)
-0.001

(0.001)
0.020

(0.004)

No
Yes
Yes

 ln(1+Number of publications)

OLS
0.885

(0.041)

0.241
(0.019)

0.067
(0.016)

-0.004
(0.010)
0.001

(0.001)
0.031

(0.021)

No
Yes
Yes

IV
1.434

(0.223)

0.205
(0.016)

0.017
(0.021)

0.007
(0.006)
0.001

(0.001)
0.021

(0.010)

No
Yes
Yes

Weak identification(Kleibergen-Paap)
Overidentification (Hansen test)
0.36
Dependent variable sample average:
1901
Number of firms
14,565
Observations
R-squared
0.39
Notes:  This table presents instrumental variable estimation results for the effect of patent citations to own science on firm's future publication, for the period 1990-2006. The sample is conditional on at least one
publication stock. The endogenous variable, internal citation in year t-1, is instrumented at the firm-year level by a devaluation dummy that is based on weighted-changes in exchange rates in countries where the
firm has subsidiaries. Profit is measured by EBIDTA. NPL citations are cites in year t by the focal firm's patents to any article. Standard errors (in brackets) are robust to arbitrary heteroscedasticity and allow for
serial correlation through clustering by firms.

F=29.168 > Stock-Yogo CV 5%= 13.46
t-statistic=0.59
0.83
1901
14,565
0.28

5
1901
14,565
0.32

0.83
1901
14,565
0.28

11
1901
14,565
0.54

7
1751
10,883
0.10

403
1901
14,565
0.91

11
1901
14,565
0.50

11
1901
14,565
0.54

11
1901
14,565
0.50

F= 59

Dependent variable:

 ln(1+No. of Publications)

Table A6. Publications and Citations to Science, by Industry

(1)

(2)

(3)

(4)

(5)

(6)

(7)

ln(1+Internal citation to  publications)t -1

ln(1+ External citation to own publications) t -1

ln(R&D stock)t-1

ln(1+Patent stock) t-1

ln(Sales)t-1

Electronics &
Semiconductor
0.096
(0.034)

Pharma&Biotech
0.073
(0.025)

Chemicals
0.123
(0.052)

-0.081
(0.026)

0.074
(0.010)

0.106
(0.011)

0.040
(0.006)

0.069
(0.020)

0.184
(0.014)

0.059
(0.017)

0.071
(0.010)

-0.077
(0.034)

0.153
(0.018)

0.047
(0.022)

0.064
(0.016)

Energy
0.054
(0.051)

-0.126
(0.044)

-0.026
(0.040)

0.147
(0.048)

0.027
(0.017)

IT & Software
0.186
(0.081)

Telecom
0.120
(0.055)

-0.132
(0.059)

0.036
(0.011)

0.085
(0.019)

0.047
(0.007)

-0.120
(0.038)

0.061
(0.012)

0.103
(0.017)

-0.003
(0.007)

Machinery /
equipment /
system
0.087
(0.042)

-0.134
(0.034)

0.038
(0.009)

0.095
(0.010)

0.051
(0.007)

Firm fixed-effects
Year dummies
Observations
R-squared
Notes:  This table presents OLS estimation results for the relationship between internal and external citations to firm's own publication and future annual publications, by industry, for the period 1980-2006.
Industry classification is based on four-digit main SIC code. Citation variables include patent citations up to year t-1 to publications published up to the same year. External cites to own publications include
corporate and non-corporate patent citations. All specifications include dummy variable that receives the value of one for firms that never published up to the focal year. Standard errors (in brackets) are
robust to arbitrary heteroscedasticity and allow for serial correlation through clustering by firms.

Yes
Yes
13,600
0.82

Yes
Yes
3,122
0.94

Yes
Yes
6,246
0.88

Yes
Yes
2,871
0.89

Yes
Yes
4,978
0.86

Yes
Yes
9,229
0.86

Yes
Yes
1,065
0.94

Table A7. IDD Effective vs.  Non-Effective: Patents to R&D, Per Firm-Year
(2)
(6)
Non-Effective IDD

(3)
Effective-IDD

(5)

(4)

(1)

(7)

Variable
MA (1994)

Patents to R&D
TX (1993)

Patents to R&D
NJ (1987)

Patents to R&D
IL (1989)

Patents to R&D
MN (1986)

(3) minus (6)

Obs.

Mean

Std. Dev.

Obs.

Mean

Std. Dev.

      -0.376

2,322

       0.037

1,422

      -0.947

2,278

      -0.484

1,477

0.5

0.8

0.8

0.9

7.2

4.6

10.8

12.0

1,596

1,408

717

780

0.9

0.7

1.7

1.3

5.5

3.6

13.6

9.8

Patents to R&D
Notes:  This table presents mean comparison tests for Patent-count to R&D for firm-years before and after the recognition of the
Inevitable Disclosure Doctrine (IDD) in main effective states, over the sample period (1980-2006). The table includes only
affected states with above 2000 firm-year sample observations. For this analysis, the firm’s state is based on the HQ of each
firm.

      -0.212

1,707

363

4.9

3.6

0.8

1.0

Figure 1. Patent citations to science are related to Carnegie Mellon survey response on the importance of research

Figure	A.	Patent	citations	to	Web	of	Science	articles,	all	publications

Figure	B.	Patent	citations	to	Web	of	Science	articles	by	top	200	U.S.	universities

e
c
n
e
i
c
s
o
t

s
n
o
i
t
a
t
i
c

t
n
e
t
a
p
e
g
a
r
e
v
A

0.80

0.70

0.60

0.50

0.40

0.30

0.20

0.10

0.00

Low

High

0.64

0.24

Percentage	of	the	R&D	unit's	projects	that	made	use	of		research
findings	produced	by	universities	or	government	research

e
c
n
e
i
c
s
o
t

s
n
o
i
t
a
t
i
c

t
n
e
t
a
p
e
g
a
r
e
v
A

0.60

0.50

0.40

0.30

0.20

0.10

0.00

Low

High

0.41

0.15

Percentage	of	the	R&D	unit's	projects	that	made	use	of		research	findings
produced	by	universities	or	government	research

Figure	C.	Patent	citations	to	Web	of	Science	articles	in	main	research	field

Low

High

0.40

0.35

0.30

0.25

0.20

0.15

0.10

0.05

0.00

e
c
n
e
i
c
s
o
t

s
n
o
i
t
a
t
i
c

t
n
e
t
a
p
e
g
a
r
e
v
A

0.30

0.14

Importance	of	the	main research field's	findings	to	R&D	activities

Note: figures A & B present mean comparisons for average patent citation to publications by low and
high percentage of the R&D unit's projects that made use of research findings produced by universities or
government. Based on 1994 Carnegie Mellon survey data (Cohen et al., 2000) Q.18: “During the last
three years, what percentage of your R&D unit's projects made use of the following research outputs
produced by universities or government research institutes and labs : a. Research findings”. High and
low are defined by the mid category rank in the survey- Low -636 firms; High-110 firms. Figure C
presents mean comparisons for average patent citation to publications by low and high importance of the
main research field's findings to the firm’s R&D activities. Based on CMS Q.22: “Referring to the fields
listed above, indicate the field whose research findings in general (not just university and government
research) contributed the most to your R&D activities during the last three years. Then, indicate the
importance of that field's findings to your R&D activities”. The sample is restricted to firms that indicated
their main field in Q22 as A-J (excluding category K -‘others’). Publications were classified to main
fields by their subject category. High is defined by the top rank and low by the lowest 3 ranks in the
survey. Low -354 firms; High-308 firms. The lines represent standard error bars. The sample includes
only patenting firms. Citations are restricted to publications published no earlier than five years prior to
the citing patent. Related patents were granted between 1991 to 1999.

Figure A1. Patent citations to science are related to Carnegie Mellon survey response on the importance of research, by main fields
Pharmaceuticals /	Biotech	/	Chemicals

Figure	A.	Patent	citations	to	Web	of	Science	articles	by	public	science

Figure	B.	Patent	citations	to	Web	of	Science	articles	by	top	200	U.S.	universities

e
c
n
e
i
c
s
o
t

s
n
o
i
t
a
t
i
c

t
n
e
t
a
p
e
g
a
r
e
v
A

1.40

1.20

1.00

0.80

0.60

0.40

0.20

0.00

Low

High

0.48

0.97

Percentage	of	the	R&D	unit's	projects	that	made	use	of		research	findings
produced	by	universities	or	government	research

e
c
n
e
i
c
s
o
t

s
n
o
i
t
a
t
i
c

t
n
e
t
a
p
e
g
a
r
e
v
A

0.80

0.70

0.60

0.50

0.40

0.30

0.20

0.10

0.00

Low

High

0.30

0.61

Percentage	of	the	R&D	unit's	projects	that	made	use	of		research	findings
produced	by	universities	or	government	research

Figure	C.	Patent	citations	to	Web	of	Science	articles	by	public	science

Figure	D.	Patent	citations	to	Web	of	Science	articles	by	top	200	U.S.	universities

Electronics	&	Semiconductor	/	IT	&	software	/	Telecom	/	Machinery

Low

High

Low

High

e
c
n
e
i
c
s
o
t

s
n
o
i
t
a
t
i
c

t
n
e
t
a
p
e
g
a
r
e
v
A

0.90
0.80
0.70
0.60
0.50
0.40
0.30
0.20
0.10
0.00

0.68

0.16

Percentage	of	the	R&D	unit's	projects	that	made	use	of		research	findings
produced	by	universities	or	government	research

e
c
n
e
i
c
s
o
t

s
n
o
i
t
a
t
i
c

t
n
e
t
a
p
e
g
a
r
e
v
A

0.70

0.60

0.50

0.40

0.30

0.20

0.10

0.00

0.46

0.10

Percentage	of	the	R&D	unit's	projects	that	made	use	of		research
findings	produced	by	universities	or	government	research

Note: the figures present mean comparisons for average patent citation to publications by low and high percentage of the R&D unit's projects that made use of research findings produced by universities or government. Based on
1994 Carnegie Mellon survey data (Cohen et al., 2000) Q.18: “During the last three years, what percentage of your R&D unit's projects made use of the following research outputs produced by universities or government research
institutes and labs : a. Research findings”. High and low are defined by the mid category rank in the survey. Figure A & B: Low -131 firms; High-31 firms. Figures C & D: Low -293 firms; High-41 firms. The lines represent
standard error bars. The sample includes only patenting firms. Citations are restricted to publications published no earlier than five years prior to the citing patent. Related patents were granted between 1991 to 1999.

Figure A2. Citations to science are positively related to share of scientists from CMS

Figure	A.	Patent	citations	to	Web	of	Science	articles

Figure	B.	Patent	citations	to	Web	of	Science	articles	by	top	200	U.S.	universities

Low

High

Low

High

0.60

0.50

0.40

0.30

0.20

0.10

0.00

e
c
n
e
i
c
s
o
t

s
n
o
i
t
a
t
i
c

t
n
e
t
a
p
e
g
a
r
e
v
A

0.52

0.21

Share	of	Ph.D.	or	M.D.	scientists	out	of	R&D	employees

e
c
n
e
i
c
s
o
t

s
n
o
i
t
a
t
i
c

t
n
e
t
a
p
e
g
a
r
e
v
A

0.35

0.30

0.25

0.20

0.15

0.10

0.05

0.00

Figure	C.	Patent	citations	to	Web	of	Science	articles	by	corporations	(Compustat)

Low

High

0.27

0.10

Share	of	Ph.D.	or	M.D.	scientists	out	of	R&D	employees

0.16

0.14

0.12

0.10

0.08

0.06

0.04

0.02

0.00

e
c
n
e
i
c
s
o
t

s
n
o
i
t
a
t
i
c

t
n
e
t
a
p
e
g
a
r
e
v
A

0.12

0.05

Share	of	Ph.D.	or	M.D.	scientists	out	of	R&D	employees

Note: The figures present mean comparisons for average patent citation to publications by low
and high share of Ph.D. or M.D. scientists out of R&D employees. Based on 1994 Carnegie
Mellon survey data (Cohen et al., 2000) Q.53-54: “Approximately how many professional and
technical R&D employees does your firm have working in your focus industry (include all
facilities working in that industry)? Of the above number, approximately how many are Ph.D. or
M.D. scientists?“. High and low are defined by above and below the median value Share of
Ph.D. or M.D. scientists, respectively Low -350 firms; High-358 firms. The sample includes only
patenting firms. Citations are restricted to publications published no earlier than five years prior
to the citing patent. The lines represent standard error bars.

Figure A3 : Cumulative distribution for the relationship between citations to science and CMS

Figure	A.	Patent	citations	to	Web	of	Science	articles	by	public	science

Figure	B.	Patent	citations	to	Web	of	Science	articles	by	top	200	U.S.	universities

y
t
i
l
i

b
a
b
o
r
p
e
v
i
t
a
u
m
u
C

l

y
t
i
l
i

b
a
b
o
r
p
e
v
i
t
a
u
m
u
C

l

Average	patent	citation	to	science

Average	patent	citation	to	science

Figure	C.	Patent	citations	to	Web	of	Science	articles	in	main	research	field

y
t
i
l
i

b
a
b
o
r
p
e
v
i
t
a
u
m
u
C

l

Average	patent	citation	to	science

Note: Figures A & B plot the cumulative distribution of patent citations to science by low and high
percentage of the R&D unit's projects that made use of research findings produced by universities or
government.. Based on 1994 Carnegie Mellon survey data (Cohen et al., 2000) Q.18: “During the last
three years, what percentage of your R&D unit's projects made use of the following research outputs
produced by universities or government research institutes and labs : a. Research findings”. High and
low are defined by the mid category rank in the survey: Low -636 firms; High-110 firms. Number of
patent citations per patent is presented with a proximity value in the 95th percentile of the sample. Figure
C plots the cumulative distribution of patent citations to science by low and high importance of the main
research field's findings to the firm’s R&D activities. Based on CMS Q.22: “Referring to the fields listed
above, indicate the field whose research findings in general (not just university and government research)
contributed the most to your R&D activities during the last three years. Then, indicate the importance of
that field's findings to your R&D activities”. The sample is restricted to firms that indicated their main
field in Q22 as A-J (excluding category K -‘others’). Pubs were classified to main fields by their subject
category. High is defined by the top rank and low by the lowest 3 ranks in the survey. Low -354 firms;
High-308 firms. Number of patent citations per patent is presented with a proximity value in the 99th
percentile of the sample. The sample includes only patenting firms. Citations are restricted to
publications published no earlier than five years prior to the citing patent.

Figure A3 : Cumulative distribution for the relationship between citations to science and CMS

Figure	A.	Patent	citations	to	Web	of	Science	articles

Figure	B.	Patent	citations	to	Web	of	Science	articles	by	top	200	U.S.	universities

y
t
i
l
i

b
a
b
o
r
p
e
v
i
t
a
u
m
u
C

l

y
t
i
l
i

b
a
b
o
r
p
e
v
i
t
a
u
m
u
C

l

Figure	C.	Patent	citations	to	Web	of	Science	articles	by	corporations	(Compustat)

Average	patent	citation	to	science

Average	patent	citation	to	science

y
t
i
l
i

b
a
b
o
r
p
e
v
i
t
a
u
m
u
C

l

Note: The figures plot the cumulative distribution of patent citations to science, by low
and high share of Ph.D. or M.D. scientists out of R&D employees. Based on 1994
Carnegie Mellon survey data (Cohen et al., 2000) Q.53-54: “Approximately how many
professional and technical R&D employees does your firm have working in your focus
industry (include all facilities working in that
industry)? Of the above number,
approximately how many are Ph.D. or M.D. scientists?“. High and low are defined by
above and below the median value Share of Ph.D. or M.D. scientists, respectively Low -
350 firms; High-358 firms. Number of patent citations per patent is presented with a
proximity value in the 95th percentile of the sample. The sample includes only patenting
firms. Citations are restricted to publications published no earlier than five years prior to
the citing patent.

Average	patent	citation	to	science

Figure A5. External and internal citation, matching process
(i) Example of an external citation to IBM’s publication : the
patent owner and cited corporate publication are different

(ii) Example of an internal citation to IBM’s publication : the
patent owner and cited corporate publication are the same

Figure A6. Timeline- Production and Use of Research

{T-3}

Focal	Firm:

Corporate
Publication

Upstream	investment
in	science:	“scientific
capital”

{T-2}

Downstream
invention	–use	of
science
{T-1}

Corporate
Publication

Corporate
Patent

Internal
citation	{T-1}

DV:	Future
production	of
scientific	knowledge

{T}

Corporate
Publication

Firm	B:

Firm	C:

{T-1}

External
citation		{T-1}

External
citation		{T-1}

Corporate
Patent

{T-1}

Corporate
Patent

At	time	{T-1}	the	focal	firm
has:
Internal	citations:1
External	citations:2

Appendix	B:	Supplement	Tables	and	figures

Table	B1.	Challenges	in	assigning	a	unique	company	id	over	time

Name

GENZYME	CORP-CONSOLIDATED
GENZYME	CORP
GENZYME	TISSUE	REPAIR
GENZYME	SURGICAL	PRODUCTS
GENZYME	MOLECULAR
ONCOLOGY
GENZYME	BIOSURGERY

GVKEY

119053
12233
118653
121742

CUSIP

begyr

endyr

comment

63799A936
372917104
372917401
372917609

1988
1996
1996
1997

2002
2006
1999
1999

Old	CUSIP
New	CUSIP
Related	subsidiary	CUSIP
Related	subsidiary	CUSIP

117298

372917500

1997

2002

143176

372917708

1999

2002

Related	subsidiary	CUSIP
Related	subsidiary	CUSIP

Table	B2.	Dynamic	match	example

UO	Company GVKEY1 Company1	 begyr1 endyr1 GVKEY2 Company2 begyr2 endyr2 GVKEY3 Company3 begyr3 endyr3 GVKEY4 Company4 begyr4 endyr4

LORAL	CORP

6807

LORAL	CORP 1960

1993

62640

CELANESE
CORP

CELANESE
CORP-OLD

2827

1950

1985

13934

LORAL
SPACE	&
COMMUN 1994
HOECHST
CELANESE
CORP

1987

2006

1996

125434

CELANESE
AG

1998

2002 162254

CELANESE
CORP

2003

2006

Table	B3.	Most	frequent	abbreviated	words

ADV
ASSOC
BIOTHERAPEUT
DYNAM
GRP
INSTR
MICROELECTR
PHARM
SFTWR

AEROSP
AUTOMAT
CHEM
EDUC
HLDG
INTERACT
MICROSYS
PHOTON
SOLUT

AGR
BIOL
CLIN
ELECTR
HLTHCR
INTL
MOLEC
PHYS
SURG

AMER
BIOMED
COMMUN
ENGN
HOSP
INVEST
NATL
PROD
SYS

ANAL
BIOPHARM
COMP
ENVIRONM
INC
LAB
NAVIGAT
RES
TECH

ANALYT
BIOSCI
CORP
FAVORS
IND
LTD
NEUROSCI
SCI
TEL

ANIM
BIOSURG
CTR
GEN
INFO
MAT
NUTR
SECUR
TELECOM

APPL
BIOSYS
DEV
GENET
INNOVAT
MED
ONCOL
SEMICOND
THERAPEUT

APPLICAT
BIOTECH
DIAGNOST
GRAPH
INST
MFG
ORTHOPAED
SERV
TRANSPORTAT

Table	B4.	Matching	Citations	to	Publications	-	Examples

Citation

Title

Publication	info
Authors

Journal	information

LIN,	KUN	SHAN,	ET	AL.,	SOFTWARE	RULES	GIVES
PERSONAL	COMPUTER	REAL	WORD	POWER	,
INTERNATIONAL	ELECTRONICS,	VOL.	53,	NO.	3,	FEB.	10,
1981,	PP.	122	125.
U.	WACHSMANN,	R.	F.	H.	FISCHER	AND	J.B.	HUBER,
MULTILEVEL	CODES:	THEORETICAL	CONCEPTS	AND
PRACTICAL	DESIGN	RULES,	IEEE	TRANS	INFORM.
THEORY,	VOL.	45,	NO.	5,	PP.	1361-1391,	JUL.	1999.

"SOFTWARE	RULES	GIVE 	PERSONAL-
COMPUTER	REAL	WORD	POWER"

"MULTILEVEL	CODES:	THEORETICAL
CONCEPTS	AND	PRACTICAL	DESIGN
RULES"

LIN	KS,	FRANTZ	GA,	GOUDIE	K

ELECTRONICS		54	(3):	122-125	1981

WACHSMANN	U,	FISCHER	RFH,
HUBER	JB

IEEE	TRANSACTIONS	ON	INFORMATION
THEORY		45	(5):	1361-1391	JUL	1999

DESIGN	CHARACTERISTICS	OF	GAS	JET	GENERATORS,
BORISOV,	1979,	PP.	21	25.

"DESIGN	CHARACTERISTICS	OF	GAS-JET
GENERATORS"

BORISOV	YY

SOVIET	PHYSICS	ACOUSTICS-USSR		26	(1):
21-25	1980

Comment

Typo	in	title	and
journal	Vol.;	initials
vs.	full	name

Several	names	listed;
variation	in	journal
name

Typo	in	year;	diff	in
location	of	title
within	the	citation

KERNS,	SHERRA	E.,	THE	DESIGN	OF	RADIATION
HARDENED	ICS	FOR	SPACE:	A	COMPENDIUM	OF
APPROACHES,	PROCEEDINGS	OF	THE	IEEE,	NOV.	1988,
PP.	1470	1509.

"THE	DESIGN	OF	RADIATION-HARDENED
ICS	FOR	SPACE	-	A	COMPENDIUM	OF
APPROACHES"

KERNS	SE,	SHAFER	BD,	ROCKETT
LR,	PRIDMORE	JS,	BERNDT	DF,
VANVONNO	N,	BARBER	FE

PROCEEDINGS	OF	THE	IEEE		76	(11):	1470-
1509	NOV	1988

Several	authors	w/o
"et	al."

GENESTIER	ET	AL	(BLOOD,	1997,	VOL.	90,	PP.	3629-3639).

STEPHEN	M.	BEBGE,	LYLE	D.	BIGHLEY	AND	DONALD	C.
MONKHOUSE	PHARMACEUTICAL	SALTS	JOURNAL	OF
PHARMACEUTICAL	SCIENCES,	1977,	66,	1-19.
L.	YOUNG	AND	D.	SHEENA,	METHODS	&	DESIGNS:
SURVEY	OF	EYE	MOVEMENT	RECORDING	METHODS,
BEHAV.	RES.	METHODS	INSTRUM.,	VOL.	5,	PP.	397-429,
1975.

"FAS-INDEPENDENT	APOPTOSIS	OF
ACTIVATED	T	CELLS	INDUCED	BY
ANTIBODIES	TO	THE	HLA	CLASS	I	ALPHA	1
DOMAIN"

GENESTIER	L,	PAILLOT	R,
BONNEFOYBERARD	N,	MEFFRE
G,	FLACHER	M,	FEVRE	D,		LIU	YJ,
LEBOUTEILLER	P,	WALDMANN
H,	ENGELHARD	VH,
BANCHEREAU	J,	REVILLARD	JP

BLOOD		90	(9):	3629-3639	NOV	1	1997

No	title	within
citation-	however,
perfect	match	in	all
other	features

"PHARMACEUTICAL	SALTS"

BERGE	SM,		BIGHLEY	LD,
MONKHOUSE	DC

JOURNAL	OF	PHARMACEUTICAL	SCIENCES
66	(1):	1-19	1977

Several	names	listed;
variation	of	names

"SURVEY	OF	EYE-MOVEMENT	RECORDING
METHODS"

YOUNG	LR,	SHEENA	D

BEHAVIOR	RESEARCH	METHODS
&INSTRUMENTATION		7	(5):	397-429	1975

diff	in	title

MICROWAVE	JOURNAL,	VOL.	22,	NO.	2,	FEB.	1979,
DEDAHAM	US	PP.	51	52,	H.	C.	CHAPPELL.

"DESIGNING	IMPEDANCE	MATCHED	IN-
PHASE	POWER	DIVIDERS"

CHAPPELL	HC

MICROWAVE	JOURNAL		22	(2):	51-52	1979

no	title	-	however,
perfect	match	in	all
other	features;	diff
position	of	author's
name	within	citation

Table	B5.	Inevitable	Disclosure	Doctrine	(IDD)-	Effective	Dates	by	State	for	IV	Estimation

Firm-year
obs. in
sample
248
122
629
13,037
1,391
1,646
70
167
1,783
1,071
53
282
109
2,585
918
241
163
199
4,246
1,099
102
1,424
2,292
745
87

Year IDD became
effective in state
-
1997
-
-
-
1996
-
1964
1960-2001
1998
-
1996
-
1989
1995
2006
-
-
1994
-
-
1966-2002
1986
2000
-

Firm-year
obs. in
sample
39
946
6
145
418
3,489
66
326
4,347
2,151
236
583
2,410
202
275
46
315
3,139
724
983
46
1,058
1,018
85
3

Year IDD became
effective in state
-
1976
-
-
-
1987
-
-
1919
2000
-
-
1982
-
-
-
-
1993-2003
1998
-
-
1997
-
-
-

State
MT
NC
ND
NE
NH
NJ
NM
NV
NY
OH
OK
OR
PA
RI
SC
SD
TN
TX
UT
VA
VT
WA
WI
WV
WY

State
AL
AR
AZ
CA
CO
CT
DC
DE
FL
GA
HI
IA
ID
IL
IN
KS
KY
LA
MA
MD
ME
MI
MN
MO
MS

Note:	The	firm’s	state	for	each	year	is	based	on	the	publication	address.

Figure B1-	Frequency distribution for inventor-author overlap

Figure B2-	Frequency distribution for inventor-author overlap, by industry

	Note:	Classification	to	industries	is	based	on	four-digit	main	SIC	code.

