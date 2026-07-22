NBER WORKING PAPER SERIES

INNOVATION AND TOP INCOME INEQUALITY

Philippe Aghion
Ufuk Akcigit
Antonin Bergeaud
Richard Blundell
David Hémous

Working Paper 21247
http://www.nber.org/papers/w21247

NATIONAL BUREAU OF ECONOMIC RESEARCH
1050 Massachusetts Avenue
Cambridge, MA 02138
June 2015

We thank Daron Acemoglu, Pierre Azoulay, Gilbert Cette, Raj Chetty, Mathias Dewatripont, Thibault
Fally, Maria Guadalupe, John Hassler, Elhanan Helpman, Chad Jones, Pete Klenow, Torsten Persson,
Thomas Piketty, Andres Rodriguez-Clare, Emmanuel Saez, Stefanie Stantcheva, Francesco Trebbi,
Fabrizio Zilibotti and seminar participants at MIT Sloan, INSEAD, the University of Zurich, Harvard
University, The Paris School of Economics, Berkeley, the IIES at Stockholm University, and the IOG
group at the Canadian Institute for Advanced Research for very helpful comments and suggestions.
The views expressed herein are those of the authors and do not necessarily reflect the views of the
National Bureau of Economic Research.

NBER working papers are circulated for discussion and comment purposes. They have not been peer-
reviewed or been subject to the review by the NBER Board of Directors that accompanies official
NBER publications.

© 2015 by Philippe Aghion, Ufuk Akcigit, Antonin Bergeaud, Richard Blundell, and David Hémous.
All rights reserved. Short sections of text, not to exceed two paragraphs, may be quoted without explicit
permission provided that full credit, including © notice, is given to the source.

Innovation and Top Income Inequality
Philippe Aghion, Ufuk Akcigit, Antonin Bergeaud, Richard Blundell, and David Hémous
NBER Working Paper No. 21247
June 2015
JEL No. D63,J14,J15,O30,O31,O33,O34,O40,O43,O47

ABSTRACT

In this paper we use cross-state panel data to show a positive and significant correlation between various
measures of innovativeness and top income inequality in the United States over the past decades. Two
distinct instrumentation strategies suggest that this correlation (partly) reflects a causality from innovativeness
to top income inequality, and the effect is significant: for example, when measured by the number
of patent per capita, innovativeness accounts on average across US states for around 17% of the total
increase in the top 1% income share between 1975 and 2010. Yet, innovation does not appear to increase
other measures of inequality which do not focus on top incomes. Next, we show that the positive effects
of innovation on the top 1% income share are dampened in states with higher lobbying intensity. Finally,
from cross-section regressions performed at the commuting zone (CZ) level, we find that: (i) innovativeness
is positively correlated with upward social mobility; (ii) the positive correlation between innovativeness
and social mobility, is driven mainly by entrant innovators and less so by incumbent innovators, and
it is dampened in states with higher lobbying intensity. Overall, our findings vindicate the Schumpeterian
view whereby the rise in top income shares is partly related to innovation-led growth, where innovation
itself fosters social mobility at the top through creative destruction.

Richard Blundell
University College London
Department of Economics
Gower Street
London, ENGLAND
r.blundell@ucl.ac.uk

David Hémous
INSEAD
Boulevard de Constance
77305 Fontainebleau, France
david.hemous@insead.edu

Philippe Aghion
Department of Economics
Harvard University
1805 Cambridge St
Cambridge, MA 02138
and NBER
paghion@fas.harvard.edu

Ufuk Akcigit
Department of Economics
University of Pennsylvania
3718 Locust Walk, #445
Philadelphia, PA 19104
and NBER
uakcigit@econ.upenn.edu

Antonin Bergeaud
Banque de France/DGEI-DEMS-SEPS
1, rue de la Vrillière
75001 Paris
antonin.bergeaud@gmail.com

1

Introduction

That the past decades have witnessed a sharp increase in top income inequality worldwide
and particularly in developed countries, is by now a widely acknowledged fact.1 However no
consensus has been reached as to the main underlying factors behind this surge in top income
inequality. In this paper we argue that, in a developed country like the US, innovation is
certainly one such factor. For example, looking at the list of the wealthiest individuals across
US states in 2015 compiled by Forbes (Brown, 2015), 11 out of 50 are listed as inventors
in a US patent and many more manage or own ﬁrms that patent. More importantly, if we
look at patenting and top income inequality in the US and other developed countries over
the past decades, we see that these two variables tend to follow parallel evolutions. Thus
Figure 1 below looks at patenting per 1000 inhabitants and the top 1% income share in the
US since the 1960: up to the early 1980s, both variables show essentially no trend but then
since the early 1980s and starting at about the same time these two variables experience
sharp upward trends.

Figure 1: Evolution of the top 1% income share and of the total patent per capita in the US. 1963-2013.

In this paper, we use cross-state panel data over the period 1975-2010 to look at the
eﬀect of innovativeness on top income inequality, where innovativeness is measured by the
ﬂow and/or quality of patented innovations in the corresponding US state, and top income
inequality is measured by the share of income held by the top 1%.

In the ﬁrst part of the paper, we develop a Schumpeterian growth model where growth
results from quality-improving innovations that can be made in each sector either from the
incumbent in the sector or from potential entrants. Facilitating innovation or entry increases
the entrepreneurial share of income and spurs social mobility through creative destruction

1The worldwide interest for income and wealth inequality, has been spurred by popular books such as

Goldin and Katz (2009), Deaton (2014) and Piketty (2014).

2

as employees’ children more easily become business owners and vice versa. In particular,
this model predicts that: (i) innovation by entrants and incumbents increases top income
inequality; (ii) innovation by entrants increases social mobility; (iii) entry barriers lower the
positive eﬀects of entrants’ innovations on top income inequality and social mobility.

These predictions are not unreasonable at ﬁrst sight: for example California is the most
technologically advanced and the most innovative state in the US; but it is also a state where
the richest 1% receives more than 20% of total income in 2010 and it lies among the US
states with the highest levels of social mobility (see Chetty et al, 2015); whereas Southern
states like Alabama are less innovative, with also lower top 1% income shares (for instance
15.8% in 2010 in Alabama) and lower levels of social mobility. Similarly, in Scandinavian
countries, innovation-led growth has accelerated and top income shares have increased in the
decade after the mid 1990s relative to the previous decade, while in the meantime, social
mobility has not decreased. In this paper we go one step further and confront the above
predictions to more systematic cross state panel evidence and also to cross-commuting zone
(CZ) and cross-Metropolitan Statistical Areas (MSA) evidence.

Our main ﬁndings can be summarized as follows. First, the top 1% income share in
a given US state in a given year, is positively and signiﬁcantly correlated with the state’s
degree of innovativeness, i.e. with the quality-adjusted amount of innovation in this state in
that year—computed using citations data. Further, we show a causal eﬀect of innovation-
led growth on top incomes. We establish this result by instrumenting for innovativeness
following two diﬀerent strategies, ﬁrst by using data on the appropriation committees of the
Senate (following Aghion et al., 2009), and second by relying on knowledge spillovers from
the other states. Both instruments deliver similar coeﬃcients and the eﬀects are signiﬁcant:
for example, when measured by the number of patents per capita, innovativeness accounts
on average for around 17% of the total increase in the top 1% income share between 1975
and 2010. We also ﬁnd that in cross-state panel regressions, innovativeness is less positively
or even negatively correlated with measures of inequality which do not emphasize the very
top incomes, in particular the top 2 to 10% income share (i.e. excluding the top 1%), or
broader measures of inequality like the Gini coeﬃcient or the Atkinson index. Next, we show
that the positive eﬀects of innovation on the top 1% income share are dampened in states
with higher lobbying intensity. Finally, from cross-section regressions performed at the CZ
level, we ﬁnd that: (i) innovativeness is positively correlated with upward social mobility;
(ii) the positive correlation between innovativeness and social mobility, is driven mainly by
entrant innovators and less so by incumbent innovators, and it is dampened in states with
higher lobbying intensity.

Our results pass a number of robustness tests: in particular the positive and signiﬁcant
correlations between innovativeness and top income shares in cross state panel regressions,
is robust to controlling for the share of the ﬁnancial sector in state GDP and to including
top marginal tax rates as control variables (whether on capital, labor or interest income).
Moreover, the impact of innovation on top income inequality is the strongest when consid-
ering three-year lagged innovation, but it fades when considering innovation with more than
a six-year lag, which in turn indicates that a given innovation increases top inequality only
temporarily.

Overall, our ﬁndings are in line with the Schumpeterian view whereby more innovation-

3

led growth should both, increase top income shares (which reﬂect innovation rents) and social
mobility (which results from creative destruction and associated ﬁrm and job turnover).

The analysis in this paper relates to several strands of literature. First, to endogenous
growth models: thus Rebelo (1991) developed an AK model to argue that (over)taxing
capital can be detrimental to growth as capital accumulation amounts to knowledge accu-
mulation in AK models. Similarly, a straightforward implication of innovation-based growth
models (Romer, 1990; Aghion and Howitt, 1992) is that, everything else equal, taxing inno-
vation rents is detrimental to growth as it discourages individuals from investing in R&D and
thus from innovating. On the other hand, Banerjee and Newman (1993), Galor and Zeira
(1993), Benabou (1996) and Aghion and Bolton (1997) argue that once credit constraints
are present, reducing wealth inequality can actually have a stimulating eﬀect on growth, as
it allows credit-constrained individuals otherwise subject to credit-rationing to ﬁnance inno-
vative projects. We contribute to this literature, ﬁrst by introducing social mobility into the
picture and linking it to creative destruction, and second by looking explicitly at the eﬀects
of innovativeness on top income shares. Hassler and Rodriguez-Mora (2000) analyze the
relationship between growth and intergenerational mobility in a model which may feature
multiple equilibria, some with high growth and high social mobility and others with low
growth and low social mobility. Multiple equilibria arise because in a high growth environ-
ment, inherited knowledge depreciates faster, which reduces the advantage of incumbents. In
that paper however, growth is driven by externalities instead of resulting from innovations.
More recently, Jones and Kim (2014) model an economy where incumbents exert eﬀorts to
increase their market share while entrants can innovate to replace the incumbents. The
interplay between these two forces ensure a Pareto distribution of income, where top income
inequality is negatively correlated with innovation and with social mobility, a prediction at
odds with our empirical results.2

Second, our paper relates to an empirical literature on inequality and growth. Thus,
Banerjee and Duﬂo (2003) ﬁnd no robust relationship between income inequality and growth
when measuring inequality by the Gini coeﬃcient, whereas Forbes (2000) ﬁnds a positive
relationship between these two variables. However, these papers do not look at top incomes
nor at social mobility, and they do not contrast innovation-led growth with non-frontier
growth. More closely related to our analysis, Frank (2009) ﬁnds a positive relationship
between both the top 10% and top 1% income shares and growth across US states; however,
Franck does not establish any causal link from growth to top income inequality, nor does he
consider innovation or social mobility.3

Third, a large literature on skill-biased technical change aims at explaining the increase
in labor income inequality since the 1970’s.
In particular, Katz and Murphy (1992) and
Goldin and Katz (2008) have shown that technical change has been skill-biased in the 20th
century. Acemoglu (1998, 2002 and 2007) sees the skill distribution as determining the
direction of technological change, while H´emous and Olsen (2014) argue that the incentive to
automate low-skill tasks naturally increases as an economy develops. Several papers (Aghion

2To be more speciﬁc, the negative correlation between top income inequality and innovation hinges on

the fact that Jones and Kim deﬁne “innovation” as the result of the innovative eﬀorts by entrants only.

3Parallel work by Acemoglu and Robinson (2015) also reports a positive correlation between top income
inequality and growth in panel data at the country level (or at least no evidence of a negative correlation).

4

and Howitt, 1997; Caselli, 1999; Galor and Moav, 2000) see General Purpose Technologies
(GPT) as lying behind the increase in inequality, as the arrival of a GPT favors workers who
adapt faster to the detriment of the rest of the population. Krusell, Ohanian, R´ıos-Rull and
Violante (2000) show how with capital-skill complementarity, the increase in the equipment
stock can account for the increase in the skill premium. While this literature focuses on
the direction of innovation and on broad measure of labor income inequality (such as the
skill-premium), our paper is more directly concerned with the rise of the top 1% and how it
relates with the rate and quality of innovation (in fact our results suggest that innovativeness
does not have a strong impact on broad measures of inequality compared to their impact on
top income shares).

Finally, our focus on top incomes links our paper to a large literature documenting a
sharp increase in top income inequality over the past decades (in particular, see Piketty
and Saez, 2003). We contribute to this line of research by arguing that increases in top 1%
income shares, are at least in part caused by increases in innovation-led growth.4

The remaining part of the paper is organized as follows. Section 2 outlays a simple
Schumpeterian model to guide our analysis of the relationship between innovation-led growth,
top incomes, and social mobility. Section 3 presents our cross-state panel data and our
measures of inequality and innovativeness. Section 4 presents our core regression results.
Section 5 discussed three extensions of our analysis: ﬁrst, it looks at the relationship between
innovativeness and social mobility; second, it distinguishes between entrant and incumbent
innovation when looking at the eﬀects on top incomes and on social mobility; third, it looks
at how local lobbying impacts on the eﬀects of innovativeness on top income and on social
mobility. Section 6 concludes.

2 Theory

In this section we develop a simple Schumpeterian growth model to explain why increased
R&D productivity or increased openness to entry increases both, the top income share and
social mobility.

2.1 Baseline model

Consider the following discrete time model. The economy is populated by a continuum
of individuals. At any point in time, there is a measure 2 of individuals in the economy,
half of them are capital owners who own the ﬁrms and the rest of the population works
as production workers.5 Each individual lives only for one period. Every period, a new

4Rosen (1981) emphasizes the link between the rise of superstars and market integration: namely, as
markets become more integrated, more productive ﬁrms can capture a larger income share, which translates
into higher income for its owners and managers. Similarly, Gabaix and Landier (2008) show that the increase
in the size of some ﬁrms can account for the increase in their CEO’s pay. Our analysis is consistent with this
line of work, to the extent that successful innovation is a main factor driving diﬀerences in productivities
across ﬁrms, and therefore in ﬁrms’ size.

5One can extend the analysis to the more general case where workers’ population diﬀers from business
owners’ population. All our results go through except that we then have to carry around the mass of workers

5

generation of individuals is born and individuals that are born to current ﬁrm owners inherit
the ﬁrm from their parents. The rest of the population works in production unless they
successfully innovate and replace incumbents’ children.

2.1.1 Production

A ﬁnal good is produced according to the following Cobb-Douglas technology:

(cid:90) 1

ln Yt =

ln yitdi,

(1)

0
where yit is the amount of intermediate input i used for ﬁnal production at date t. Each
intermediate is produced with a linear production function

where lit is the amount of labor used to produce intermediate input i at date t and qit is the
labor productivity. Each intermediate i is produced by a monopolist who faces a competitive
fringe from the previous technology in that sector.

yit = qitlit,

(2)

2.1.2

Innovation

Whenever there is a new innovation in any sector i in period t, quality in that sector improves
by a multiplicative term ηH so that:

qi,t = ηHqi,t−1.

In the meantime, the previous technological vintage qi,t−1 becomes publicly available, so that
the innovator in sector i obtains a technological lead of ηH over potential competitors.

At the end of period t, other ﬁrms can partly imitate the (incumbent) innovator’s tech-
nology so that, in the absence of a new innovation in period t + 1, the technological lead
enjoyed by the incumbent ﬁrm in sector i shrinks to ηL with ηL < ηH.

Assuming away any further imitation before a new innovation occurs, the technological
lead enjoyed by the incumbent producer in any sector i takes two values: ηH in periods with
innovation and ηL < ηH in periods without innovation.6

Finally, we assume that an incumbent producer that has not recently innovated, can still
resort to lobbying in order to prevent entry by an outside innovator. Lobbying is successful
with exogenous probability z, in which case, the innovation is not implemented, and the
incumbent remains the technological leader in the sector (with a lead equal to ηL).

Both potential entrants and incumbents have access to the following innovation technol-

ogy. By spending

CK,t (x) = θK

x2
2

Yt

an incumbent (K = I) or entrant (K = E) can innovate with probability x. A reduction in
θK captures an increase in R&D productivity or R&D support, and we allow for it to diﬀer
between entrants and incumbents.

through all the equilibrium equations of the model.

6The details of the imitation-innovation sequence do not matter for our results, what matters is that

innovation increases the technological lead of the incumbent producer over its competitive fringe.

6

2.1.3 Timing of events

Each period unfolds as follows:

1. In each line i, a potential entrant spends CE,t (xi) and the oﬀspring of the incumbent

in sector i spends CI,t (˜xi) .

2. With probability (1 − z) xi the entrant succeeds, replaces the incumbent and obtains
a technological lead ηH, with probability ˜xi the incumbent succeeds and improves its
technological lead from ηL to ηH, with probability 1 − (1 − z) xi − ˜xi, there is no
successful innovation and the incumbent stays the leader with a technological lead of
ηL.7

3. Production and consumption take place and the period ends.

2.2 Solving the model

We solve the model in two steps: ﬁrst, we compute the income shares of entrepreneurs
and workers and the rate of upward social mobility (from being a worker to becoming an
entrepreneur) for given innovation rates by entrants and incumbents; second, we endogeneize
the entrants’ and incumbents’ innovation rates.

2.2.1

Income shares and social mobility for given innovation rates

In this subsection we take as given the fact that in all sectors potential entrants innovate at
some rate xt and incumbents innovate at some rate ˜xt at date t.

Using (2), the marginal cost of production of (the leading) intermediate producer i at

time t is

M Cit =

wt
qi,t

.

Since the leader and the fringe enter Bertrand competition, the price charged at time t by
intermediate producer i is simply a mark-up over the marginal cost equal to the size of the
technological lead, i.e.

pi,t =

wtηit
qi,t

,

(3)

where ηi,t ∈ {ηH, ηL}. Therefore innovating allows the technological leader to charge tem-
porarily a higher mark-up.

Using the fact that the ﬁnal good sector spends the same amount Yt on all intermediate
goods (a consequence of the Cobb-Douglas technology assumption), we have in equilibrium:

Yt = pi,tyit for all i.

(4)

7For simplicity, we rule out the possibility that both agents innovate in the same period, so that innova-
tions by the incumbent and the entrant in any sector, are not independent events. This can be microfounded
in the following way. Assume that every period there is a mass 1 of ideas, and only one idea is succesful.
Research eﬀorts x and (cid:101)x represent the mass of ideas that a ﬁrm investigates. Firms can observe each other
actions, therefore in equilibrium they will never choose to look for the same idea provided that x∗ + ˜x∗ < 1,
which is satisﬁed for θK suﬃciently large.

7

This, together with (3) and (2), allows us to immediately express the labor demand and
the equilibrium proﬁt in any sector i at date t. Labor demand by producer i at time t is
given by:

lit =

Yt
wtηit

.

And equilibrium proﬁts in sector i at time t are equal to:

πit = (pit − M Cit)yit =

ηit − 1
ηit

Yt.

Hence proﬁts are higher if the incumbent has recently innovated, namely:

πH,t =

ηH − 1
ηH
(cid:124) (cid:123)(cid:122) (cid:125)
≡πH

Yt > πL,t =

Yt.

ηL − 1
ηL
(cid:124) (cid:123)(cid:122) (cid:125)
≡πL

Now we have everything we need to derive the expressions for the income shares of workers
and entrepreneurs and for the rate of upward social mobility. Let µt denote the fraction of
high-mark-up sectors (i.e. with ηit = ηH) at date t.
Labor market clearing at date t implies that:

(cid:90)

1 =

litdi =

(cid:90)

Yt
wtηit

di =

Yt
wt

(cid:20) µt
ηH

+

1 − µt
ηL

(cid:21)

We restrict attention to the case where the ηit’s are suﬃciently large that

wt < πL,t < πH,t,

so that top incomes are earned by entrepreneurs.

Hence the share of income earned by workers (wage share) at time t is equal to:

wages sharet =

wt
Yt

=

µt
ηH

+

1 − µt
ηL

.

(5)

whereas the share of income earned by entrepreneurs (entrepreneurs share) at time t is equal
to:

entrepreneur sharet =

µtπH,t + (1 − µt) πL,t
Yt
Since mark-ups are larger in sectors with new technologies, aggregate income shifts from
workers to entrepreneurs in relative terms whenever the equilibrium fraction of product lines
with new technologies µt increases. But by the law of large numbers this fraction is equal
to the probability of an innovation by either the incumbent or a potential entrant in any
intermediate good sector.

1 − µt
ηL

µt
ηH

= 1 −

(6)

−

.

More formally, we have:

which increases with the innovation intensities of both incumbents and entrants, but to a
lesser extent with respect to entrants’ innovations the higher the entry barriers z are.

µt = ˜xt + (1 − z) xt,

(7)

8

Finally, we measure upward social mobility by the probability Ψt that the oﬀspring of a
worker becomes a business owner. This in turn happens only if this individual manages to
ﬁrst innovate and then avoids the entry barrier; therefore

Ψt = xt (1 − z) ,

(8)

which is increasing in entrant’s innovation intensity xt but less so the higher the entry barriers
z are. This yields:

Proposition 1 (i) A higher rate of innovation by a potential entrant, xt, is associated with
a higher entrepreneur share of income and a higher rate of social mobility, but less so the
higher the entry barriers z are; (ii) A higher rate of innovation by an incumbent, (cid:101)xt, is
associated with a higher entrepreneur share of income but has no impact on social mobility.

Remark 1: That the equilibrium share of wage income in total income decreases with
the fraction of high mark-up sectors µt, and therefore with the innovation intensities of
entrants and incumbents, does not imply that the equilibrium level of wages also declines.
In fact the opposite occurs, and to see this more formally, we can compute the equilibrium
level of wages by plugging (4) and (3) in (1), which yields:

wt =

Qt
H η1−µt
ηµt

L

,

(9)

where Qt is the quality index deﬁned as Qt = exp (cid:82) 1
quality index is computed as
(cid:90) 1

0 ln qitdi. The law of motion for the

Qt = exp

[µt ln ηHqit−1 + (1 − µt) ln qit−1] di = Qt−1ηµt
H .

(10)

0

Therefore, for given technology level at time t − 1, the equilibrium wage is given by
wt = ηµt−1

L Qt−1.

This last equation clearly shows that the overall eﬀect of a current increase in innovation
intensities is to increase the equilibrium wage for given technology level at time t − 1, even
though it also shifts some income share towards entrepreneurs.8

Remark 2: Equation (9) shows that if the equilibrium innovation intensities x∗ and (cid:101)x∗
of the entrant and incumbent are constant over time (which we show below) the growth rate
of aggregate variables such as aggregate output and the wage rate is equal to the growth rate
of the quality index Qt. Using the law of motion for Qt (10), we get that the equilibrium
growth rate is a constant given by

g∗ = η(1−z)x∗+˜x∗

H

− 1,

which is increasing in the entrant innovation rate x∗ (but less so the higher entry barriers z
are) and in the incumbent innovation rate ˜x∗.9

8In addition, note that the entrepreneurial share is independent of innovation intensities in previous
periods. Therefore, a temporary increase in current innovation only leads to a temporary increase in the
entrepreneurial share: once imitation occurs, the gains from the current burst in innovation will be equally
shared by workers and entrepreneurs.

9We looked at an extension of the model where only some high-ability incumbents can potentially innovate

9

2.2.2 Endogenous innovation

We now turn to the endogenous determination of the innovation rates of entrants and incum-
bents. The oﬀspring of the previous period’s incumbent solves the following maximization
problem:

(cid:26)

˜xπHYt + (1 − ˜x − (1 − z) x∗) πLYt + (1 − z) x∗wt − θI

max
˜x

(cid:27)

Yt

.

˜x2
2

This expression states that the oﬀspring of an incumbent can already collect the proﬁts of
the ﬁrm that she inherited (πL), but also has the chance of making higher proﬁt (πH) by
innovating with probability ˜x.

Clearly the optimal innovation decision is simply

t = ˜x∗ =
˜x∗

πH − πL
θI

=

(cid:18) 1
ηL

−

1
ηH

(cid:19) 1
θI

,

(11)

which decreases with incumbent R&D cost parameter θI.

A potential entrant in sector i solves the following maximization problem:

(cid:26)

max
x

(1 − z) xπHYt + (1 − x (1 − z)) wt − θE

(cid:27)

Yt

,

x2
2

since an entrant chooses its innovation rate with the outside option being a production worker
who receives wage wt.

Using the fact (see above) that

wt
Yt

=

µt
ηH

+

1 − µt
ηL

,

taking ﬁrst order conditions, and using our assumption that wt < πL,t, we can express the
entrant innovation rate as

t ≡ x∗ =
x∗

(cid:18)

πH −

(cid:20) µt
ηH

+

1 − µt
ηL

(cid:21)(cid:19) (1 − z)

θE

.

(12)

Then, using the fact that in equilibrium

µ∗ = (1 − z) x∗ + ˜x∗,

the equilibrium innovation rate for entrants is simply given by

(cid:16)

x∗ =

πH − 1
ηL

+

(cid:16) 1
− 1
ηL
ηH
θE − (1 − z)2 (cid:16) 1

(cid:17)

˜x∗(cid:17)

− 1
ηH

ηL

(1 − z)
(cid:17)

.

(13)

while the other, low-ability, incumbents cannot. In this extension, a high rate of entrant’s innovation and low
entry barriers further increase growth by ensuring a higher share of high-ability incumbents in steady-state.

10

Therefore lower barriers to entry (i.e. a lower z) and less costly R&D for entrants (lower
θE) both increase the entrants’ innovation rate (as 1/ηL − 1/ηH > 0). Less costly incumbent
R&D also increases the entrant innovation rate since (cid:101)x∗ is decreasing in θI.10

Intuitively, high mark-up sectors are those where an innovation just occurred and was
not blocked, so a reduction in either entrants’ or incumbents’ R&D costs increases the share
of high mark-up sectors in the economy and thereby the entrepreneurs’ share of income.
And to the extent that higher entry barriers dampen the positive correlation between the
entrants’ innovation rate and the entrepreneurial share of income, they will also dampen the
positive eﬀects of a reduction in entrants’ or incumbents’ R&D costs on the entrepreneurial
share of income.11

Finally, equation (8) immediately implies that a reduction in entrants’ or incumbents’

R&D costs increases social mobility but less so the higher the barriers to entry are.

We have thus established:

Proposition 2 An increase in R&D productivity (whether it is associated with a reduction
in θI or in θE), leads to an increase in the innovation rates x∗ and ˜x∗ but less so the higher
the entry barriers z are; consequently, it leads to higher growth, higher entrepreneur share
and higher social mobility but less so the higher the entry barriers are.

∂2
∂θK ∂z (1 − z) x∗ > 0
Proof. The only claim we have not formally proved in the text is that
(which immediately implies that the positive impact of a increase in R&D productivity on
growth, entrepreneurial share and social mobility is attenuated when barriers to entry are
high). Diﬀerentiating ﬁrst with respect to θE, we get:

∂ (1 − z) x∗
∂θE

= −

(1 − z) x∗
θE − (1 − z)2 (cid:16) 1

ηL

(cid:17),

− 1
ηH

which is increasing in z since x∗ and (1 − z) both decrease in z and the denominator θ +
(1 − z)2 (cid:104) 1
> 0). Similarly, diﬀerentiating with
ηH
respect to θI gives:

increases in z (recall that 1
ηL

− 1
ηH

− 1
ηL

(cid:105)

∂ (1 − z) x∗
∂θI

=

(cid:17)

(cid:16) 1
ηL

− 1
ηH
θE − (1 − z)2 (cid:16) 1

(1 − z)

− 1
ηH

ηL

∂ ˜x∗
∂θI

,

(cid:17)

which is increasing in z since ∂ ˜x∗
∂θI
This establishes the proposition.

< 0, and 1 − z and the denominator both decrease in z.

2.2.3

Impact of mark-ups on innovation and inequality

Our discussion so far pointed to a causality from innovation to top income inequality and
social mobility. However the model also speaks to the reverse causality from top inequality to

10That x∗ increases with (cid:101)x∗ results from the fact that more innovation by incumbents lowers the equilibrium
wage which decreases the opportunity cost of innovation for an entrant. This general equilibrium eﬀect rests
on the assumption that incumbents and entrants cannot both innovate in the same period.

11See the proof of Proposition 2 below.

11

innovation. First, a higher innovation size ηH leads to a higher mark-up for ﬁrms which have
successfully innovated. As a result, it increases the entrepreneur share for given innovation
rate (see (6)). Second, a higher ηH increases incumbents’ (11) and (13) entrants’ innovation
rates, which further increases the entrepreneur share of income.

More interestingly perhaps, a higher ηL increases the mark-up of a non-innovator and
thereby also the entrepreneur share, while discouraging incumbent’s innovation.12 This in
turn may dampen the positive correlation between innovation and the entrepreneur share of
income.

2.3 Predictions

We can summarize the main predictions from the above theoretical discussion as follows.

• Innovation by both entrants and incumbents, increases top income inequality;

• Innovation by entrants increases social mobility;

• Entry barriers lower the positive eﬀect of entrants’ innovation on top income inequality

and on social mobility.

We now confront these predictions to the data.

3 Data and measurement

Our core empirical analysis is carried out at US state level. Our dataset covers the period
1975-2010, a time range imposed upon us by the availability of patent data.

3.1 Inequality

The data on the share of income owned by the top 1% of the income distribution for our
cross-US-state panel analysis, are drawn from the US State-Level Income Inequality Database
(Frank, 2009). From the same data source, we also gather information on alternative mea-
sures of inequality: namely, the top 10% income share, the Atkinson Index (with a coeﬃcient
of 0.5), the Theil Index and the Gini Index. We thus end up with a balanced panel of 51
states (we include Alaska and Hawaii and count the District of Columbia as a “state”) and a
total of 1836 observations (51 states over 36 years). In 2010, the three states with the highest
share of total income held by the richest 1% are Connecticut, New York and Wyoming with
respectively 21.7%, 21.1% and 20.1% whereas West Virginia, Iowa and Maine are the states
with the lowest share held by the top 1% (respectively 11.8%, 12% and 12%). In every US
state, the top 1% income share has increased between 1975 and 2010, the unweighted mean
value was around 8% in 1975 and reached 21% in 2007 before slowly decreasing to 16.3% in

12In the Appendix, we show that an increase in ηL also decreases total innovation when θI = θE, but yet
its impact on the entrepreneur share remains positive for a suﬃciently high R&D cost (i.e. for θ suﬃciently
high).

12

2010. In addition, the heterogeneity in top income shares across states is larger in the recent
period than it was during the 1970s, with a cross-state variance multiplied by 2.7 between
1975 and 2010. Figure 2 shows the evolution of the top 1% share for the states of California
and Louisiana, and in the US as a whole.

Figure 2: Evolution of top 1% income share in California, in Louisiana and in the US.

Note that the US State-Level Income Inequality Database provides information on the
adjusted gross income from the IRS. This is a broad measure of pre-tax (and pre-transfer)
income which includes wages, entrepreneurial income and capital income (including realized
capital gains). Unfortunately it is not possible to decompose total income in the various
sources of income (wage, entrepreneurial or capital incomes) with this dataset. In contrast,
the World Top Income Database (Alvaredo et al., 2014), allows us to assess the composition
of the top 1% income share. On average between 1975 and 2010, wage income represented
50.7% and entrepreneurial income 19.1% of the total income earned by the top 1% (with
entrepreneurial income having a lower share in later years), while for the top 10%, wage
income represented 71.1% and entrepreneurial income 11.7% of total income. In our model,
entrepreneurs are those directly beneﬁtting from innovation. In practice, innovation bene-
ﬁts are shared between ﬁrm owners, top managers and inventors, thus innovation aﬀects all
sources of income within the top 1%. Yet, the fact that entrepreneurial income is overrepre-
sented in the top 1% income relative to wage income, suggests that our model captures an
important aspect in the evolution of top income inequality.

3.2 Innovation

When looking at cross state or more local levels, the US patent oﬃce (USPTO) and the
HBS patent database from Lai et al. (2013) provide complete statistics for patents granted

13

between the years 1975 and 2010. For each patent, it provides information on the state of
residence of the patent inventor, the date of application of the patent and a link to every
citing patents granted before 2010. This citation network between patents enables us to
construct several estimates for the quality of innovation as described below. Since a patent
can be associated with more than one inventor and since coauthors of a given patent do
not necessarily live in the same state, we assume that patents are split evenly between
inventors and thus we attribute only a fraction of the patent to each inventor. A patent is
also associated with an “assignee” that owns the right to the patent. Usually, the assignee is
the ﬁrm employing the inventor, and for independent inventors the assignee and the inventor
are the same person. We chose to locate each patent according to the US state where its
inventor lives and works. Although the inventor’s location might occasionally diﬀer from
the assignee’s location, most of the time the two locations coincide (the correlation between
the two is above 92%).13 Moreover, we checked that all our results are robust to locating
patents according to the assignee’s address instead of the inventor’s address. And we also
checked the robustness of our results to removing independent inventors from the patent
count. Finally, in line with the patenting literature, we focus on “utility patents” which
cover 90% of all patents at the USPTO.14

3.2.1 Truncation bias

The so-called truncation bias in patent count stems from the fact that the process of granting
a patent takes about two years on average following patent application. As the individual
USPTO database contains only patents that have been granted before 2010, simply grouping
by state for each year will lead to underestimate the intensity of innovation as we approach the
end period of the sample (as many patents with application dates close to 2010 are unlikely to
be granted by 2010, and therefore to appear in the database). Since we restrict attention to
patents with application dates between 1975 and 2010, the truncation bias is not an issue at
the beginning of the time period (correcting for patents that were granted after 1975 but with
application dates before 1975). To account for truncation, we use aggregate data on patent
granted by application date at the state level from the USPTO website. These data have
been updated in 2014 and therefore in principle they should not suﬀer too much from the
truncation bias problem over the period 1975-2010. However, even before 2010, we observe
a decrease in the number of granted patents as distributed by their application date.15 Two
main factors seem to account for the decreasing trend in the number of granted patents.
First, the information technology bubble has led many inventors to create a company in
the high tech sector during the 90s and to innovate faster than their competitors. This

13For example, Delaware and DC are states for which the inventor’s address is more likely to diﬀer from

the assignee’s address.

14The USPTO classiﬁcation considers three types of patents according to the oﬃcial documentation: utility
patents that are used to protect a new and useful invention, for example a new machine, or an improvement
to an existing process; design patents that are used to protect a new design of a manufactured object; and
plant patents that protect some new varieties of plants. Among those three types of patents, the ﬁrst is
presumably the best proxy for innovation, and it is the only type of patents for which we have complete
data.

15This is not the case when looking at the number of patents distributed by their granting year.

14

generated a patent race that stopped after the crisis in 2000. Second, the USPTO has faced
a large surge in the number of patent applications since the past decade as evidenced by
the oﬃcial statistics on the number of applications (regardless of whether these patents will
ultimately be granted or not). Consequently, a growing share in the number of applications
ﬁled are still pending because they have not yet been examined (for more information about
this “backlog”, see De Rassenfosse et al. (2013)). To address this problem, we completed
the series after 200616 with the adjusted number of patent applications by the various states
(regardless of whether the patents were to be granted or rejected) from the Strumsky Granted
Patent and Patent Application Database17 assuming a constant and homogeneous rate of
acceptance for the years 2007, 2008, 2009 and 2010. This assumption is not unreasonable
when looking at past data. This method has its shortcomings though: the measure is noisy
for the last three years as it may involve including many insigniﬁcant patents. An alternative
would be to assume that the backlog accounts for the same share of patents across all states,
which in turn is consistent with the shape of the lag distribution being very similar across
states. Then, the backlog would be captured by our ﬁxed eﬀects. Fortunately, these two
approaches yield very similar results and therefore we shall only present results using the
ﬁrst approach.18

Similarly, we correct for truncated citation bias using the quasi-structural approach pro-
posed by Hall, Jaﬀe and Trajtenberg (2001) and extend their HJT corrector until 2010. This
method allows us to generate corrected citation data that can be compared over time and
technologies. Here again, because of the inaccuracy of the correction variable for the last
three years, corrected citation counts can mainly be used before 2008.

There is a substantial amount of variation in innovativeness both across states and over
time. Between 1975 and 1990, Delaware, Connecticut, New Jersey and Massachusetts were
the most innovating states (with 0.55, 0.4, 0.39 and 0.29 patents per 1000 inhabitants re-
spectively), while Arkansas, Mississippi and Hawaii were the least innovative states with
less than 0.05 patents per thousands inhabitants. Between 1990 and 2009, however, the
most innovative states were Idaho (0.99 patents per 1000 inhabitants), Vermont (0.86), Mas-
sachusetts (0.63), Minnesota (0.61) and California (0.61), whereas Arkansas, West Virginia
and Mississippi all had less than 0.06 patents per 1000 inhabitants.19

16According to the USPTO website: “As of 12/31/2012, utility patent data, as distributed by year of
application, are approximately 95% complete for utility patent applications ﬁled in 2004, 89% complete for
applications ﬁled in 2005, 80% complete for applications ﬁled in 2006, 67% complete for applications ﬁled
in 2007, 49% complete for applications ﬁled in 2008, 36% complete for applications ﬁled in 2009, and 19%
complete for applications ﬁled in 2010; data are essentially complete for applications ﬁled prior to 2004.” By
the same logic, in 2014 nearly all patents from 2006 should be included.

17https://clas-pages.uncc.edu/innovation/
18Yet another approach is to delete the time component by considering only the share of total patents

application in each state. We checked the robustness of our results to using this alternative approach.

19Idaho’s place at the top of this list may look surprising, but it is home to several tech companies

(particularly in semiconductors). Our results carry through if one excludes Idaho.

15

3.2.2 Quality measures

Simply counting the number of patent granted by their application date is a crude measure
of innovation as it does not diﬀerentiate between a patent that made a signiﬁcant contri-
bution to science and a more incremental one. The USPTO database, provides suﬃciently
exhaustive information on patent citation to compute indicators which better measure the
quality of innovation. We consider four measures of innovation quality:

• 3, 4 and 5 year windows citations counter : this variable measures the number of
citations received within no more than 3, 4 or 5 years after the application date. This
measure has the advantage of being immune from the citation truncation bias problem
described above as long as we correct for the number of patents and provided we stop
our data sample at patents applied in 2006, 2005 and 2004 respectively.

• Is the patent among the 5% most cited in the year by 2010? This is a dummy variable
equal to one if the patent applied for in a given year belong to the top 5% most cited
patents. Because most of the patents are not yet cited, or at most once, in 2008, 2009
and 2010, we stop computing this measure after the year 2007.

• Total corrected citation counter: This measures the number of times a patent has been
cited, once this number has been corrected for the truncation citation bias as explained
above.

• Has the patent been renewed? This is a dummy variable equal to one if the patent
has been renewed (at least one) before 2014.
Indeed, USPTO require inventors to
pay maintenance fees three times during the lifetime of the patent, the ﬁrst payment
being made three years after the date of issue. Hence this measure is immune from
truncation bias issues. Unfortunatly, these data are only available from 1982.

These measures have been aggregated at the state level by taking the sum of the quality
measures over the total number of patents granted for a given state and a given application
date and then divided by the number of inhabitants. Most of our quality measures can thus
be considered as citation weighted patents counts. These diﬀerent measures of innovativeness
display consistent trends: hence the four states with the highest ﬂows of patents between
1975 and 1990 are also the four states with the highest total citation counts, and similarly
for the ﬁve most innovative states between 1990 and 2009.

3.3 Control variables

When regressing top income shares on innovativeness, a few concerns may be raised. First,
the business cycle is likely to have direct eﬀects on innovation and top income share. Second,
top income share groups are likely to involve to a signiﬁcant extent individuals employed by
the ﬁnancial sector (see for example Philippon and Reshef, 2012). To evidence this strong
correlation, Figure 3 shows the evolution of the share of the ﬁnancial sector and of the size
of the top 1% income share group in the state of New York. In turn, the ﬁnancial sector
is sensitive to business cycles and it may also aﬀect innovation directly. To address these

16

two concerns, we control for the output gap and for the share of GDP accounted for by the
ﬁnancial sector per inhabitant. In addition, we control for the size of the government sector
which may also aﬀect both top income inequality and innovation. To these we add usual
controls, namely GDP per capita and the growth of total population.

Figure 3: Evolution of the share of ﬁnancial sector and on the top 1% share in the state of New York.
1970-2012.

Data on GDP, total population and the share of the ﬁnancial and public sectors can be
found in the Bureau of Economic Analysis (BEA) regional accounts. Finally, we compute
the output gap deﬁned as the relative distance of real GDP per capita to its ﬁltered value
computed with a HP ﬁlter of parameter λ equal to 6.25. To deal with the issue of extreme
values at the beginning and the end of the period, we calculated this ﬁlter over the period
1970-2013.

4 Main empirical analysis: the eﬀect of innovativeness

on top incomes

4.1 Estimation strategy

We seek to look at the eﬀect of innovativeness measured by the ﬂow of patents granted by
the USPTO per thousand of inhabitants and by the quality of innovation on top income
shares. We thus regress the top 1% income share on our measures of innovativeness. Our
estimated equation is:

log(yit) = A + Bi + Bt + β1 log(innovi(t−1)) + β2Xit + εit,

(14)

17

where yit is the measure of inequality, Bi is a state ﬁxed eﬀect, Bt is a year ﬁxed eﬀect,
innovi(t−1) is innovativeness in year t − 1,20 and X is a vector of control variables.21 By
including state and time ﬁxed eﬀects we are eliminating permanent cross state diﬀerences
in inequality and also aggregate changes in inequality. We are essentially studying the
relationship between the diﬀerential growth in innovation across states with the diﬀerential
growth in inequality.

4.2 Results from OLS regressions

Table 2 presents the results from regressing top income shares and other inequality measures
on the ﬂow of patents. The relevant variables are deﬁned in Table 1. As explained in the
previous section, the number of patents granted by the USPTO for a given application date
has been corrected for the truncation bias.

From Table 2 we see that the eﬀect of the ﬂow of patents per capita on the top 1% income
share is always positive and signiﬁcant at the cross state level. The eﬀect is robust to adding
the control variables even when we control for the size of the ﬁnancial sector and for the size
of the government.

Table 3 shows the eﬀect of our various measures of innovation quality on the top 1%
income share. The ﬁrst three columns present our results when using the 3, 4 and 5 year
window citation number as our innovation quality measure. As argued above, this measure
has the advantage of being immune to the citation truncation bias problem as long as we
restrict our observations to before 2007, 2006 and 2005 respectively for these three measures.
The results from Table 3 show that these measures of innovation quality are positively
correlated with the top 1% income share. Columns 4, 5 and 6 from the same table consider
the other three measures of innovation quality. Column 4 regresses top income share on the
corrected number of citations per capita, column 5 regresses top income share on the number
of patents among the 5% most cited in the same application year, and column 6 regresses
the top income share on the number of patents per capita but counting only those that have
been renewed at least once. In all instances, we ﬁnd a positive and signiﬁcant coeﬃcient for
innovation on the top 1% income share. Moreover, the coeﬃcients are quite similar across
the diﬀerent measures of innovation.

4.3 Results from IV regressions

To deal with endogeneity issues in the regression of top income inequality on innovativeness,
we construct two instruments: the ﬁrst instrument relies on states’ representation in the
Appropriation Committees of the Senate and the House of Representatives. The second
instrument exploits knowledge spillovers across states.

20We discuss the choice of lagged innovation variable(s) below.
21When y is equal to 0, computing log(y) would result in removing the observation from the panel. In such
cases, we proceed as in Blundell et al. (1995) and set the left hand variable to 0 and add a dummy equal to
one if y is equal to 0. All the results of this paper are consistent with simply removing the observation and
the magnitudes are only very slightly altered. This dummy is not reported.

18

4.3.1

Instrumentation using the state composition of appropriation committees

Following Aghion et al (2009), we consider the time-varying State composition of the ap-
propriation committees of the Senate and the House of Representatives. To construct this
instrument, we gather data on membership of these committees over the period 1969-2010
(corresponding to Congress numbers 91 to 111).22 The rationale for using this instrument
is analyzed at length in Aghion et al. (2009): in a nutshell, the appropriation committees
allocate federal funds to research education across US states.23 A member of Congress who
sits in such a Committee often pushes towards subsidizing research education in the state in
which she has been elected, in order to increase her chances of reelection in that state. Con-
sequently, a state with one of its congressmen seating on the committee is likely to receive
more funding and to develop its research education, which should subsequently increase its
innovativeness in the following years.

For the years 1969-2010, the number of seats in this committee has slowly increased
from around 50 to 65 for the House and from around 25 to 30 for the Senate. The State
composition of the Appropriation Committees is potentially a good instrument for research
education subsidies and thus for innovativeness, because changes in the composition of the
appropriation committees have little to do with growth or innovation performance in those
states. Instead, they are determined by random events such as the death or retirement of
current heads or other members of these committees, followed by a complicated political
process to ﬁnd suitable candidates (although the committees are renewed every two years,
in practice committee members stay for several terms in a row, particularly in the Senate).
This process in turn gives large weight to seniority considerations with also a concern for
maintaining a fair political and geographical distribution of seats (as described with more
In addition, legislators are unable to fully evaluate the
details in Aghion et al., 2009).
potential of a research project and are more likely to allocate grants on the basis of political
interests. Both explain why it is reasonable to see the arrival of a congressman in the
appropriation committee in the Senate or the House of Representatives, as an exogenous
shock on innovativeness (a decrease in θE and θI in the context of our model).

Based on these Appropriation Committee data, diﬀerent instruments for innovativeness
can be constructed. We follow the simplest approach which is to take the number of senators
(0, 1 or 2) or representatives who seat on the committee for each state and at each date.24

the

been

have
by

22Data
documents
namely:
published
and
http://democrats.appropriations.house.gov/uploads/House Approps Concise% History.pdf.
http://www.gpo.gov/fdsys/pkg/CDOC-110sdoc14/pdf/CDOC-110sdoc14.pdf.
The name of each con-
gressman has been compared with oﬃcial biographical informations to determine the appointment date and
the termination date.

and
Representative

collected
of

compared

Senate,

various

House

from

and

the

23Even though these appropriations committees are not explicitly dedicated to research education, de
facto an important fraction of their budget goes to research education. As explained in Aghion et al (2009),
“research universities are important channels for pay back because they are geographically speciﬁc to a
legislator’s constituency. (...) Other potential channels include funding for a particular highway, bridge,
or similar infrastructure project located in the constituency”. We control for highway, infrastructure and
military expenditures in our regressions, as explained below.

24We checked that our results are consistent with two other measures: one which focuses on the subcom-
mittees which are the most active in allocating federal spending: Agriculture, Defense and Energy (following

19

Next, we need to ﬁnd the appropriate time-lag between a congressman’s accession into the
appropriation committee and the eﬀect this may have on innovativeness. According to
Aghion et al. (2009), many politicians in the United States are on a two year cycle. When
appointed to the committee, they must do everything in order to show their electors that they
are capable of doing something for them, and will thus allocate funds to universities located
in his/her states of constituency. For this reason, we decided to set the lag to two years, but
one and three year lags are also considered because of the time before the allocation of new
funds and the ﬁlling of a patent application.

Although changes in the composition of the Appropriation Committees can be seen as
exogenous shocks on innovativeness there is still a concern about potential eﬀects of such
changes on the top 1% income share that do not relate to innovation. There is not much
data on appropriation committee earmarks; yet, for the years 2008 to 2010, the Taxpayers
for Common Sense, a nonpartisan budget watchdog, reports data on earmarks in which we
can see that infrastructure, research education and military are the three main recipients for
appropriation committees’ funds. In addition, when looking more closely at top recipients,
we see that most are either universities or defense related companies.25

One can of course imagine a situation in which the (rich) owner of a construction or
military company will capture part of these funds.
In that case, the number of senators
seating in the committee of appropriation would be correlated with the top 1% income
share, but for reasons having little to do with innovation. To deal with such possibility,
we use data on federal allocation to states by identifying the sources of state revenues (see
Aghion et al., 2009). Such data can be found at the Census Bureau on a yearly basis. Using
this source, we identify a particular type of infrastructure spending, namely highways, for
which we have consistent data from 1975 onward. We thus control for highways and also for
the share of the federal military funding allocated to the various states.

Our results for the eﬀect of innovativeness on the top 1% income share in the correspond-
ing IV regressions are shown in Table 4.26 We chose to present the results only for the top
1% and for the instrument using the number of seats at the Senate. Adding the number
of seats occupied at the House of Representative shows consistent results but decreases the
ﬁrst stage F stat.27

Columns 1 to 3 show the eﬀect of the number of patents per capita (variable patent pc)
on top 1% income share while columns 4 to 6 use the number of citations in a 3 year windows
per capita (variable 3YWindow ).28 The eﬀect is positive and signiﬁcant whether we consider
1, 2 or 3 year lags. First stage regression F-statistics are reported at the bottom of Table
4.29

Aghion et al., 2009), and another one which only considers the number of members whose seniority is less
than 8 years (as these members are more likely to direct funds to their states for political reasons).

25Such data can be found on the Opensecrets website : https://www.opensecrets.org/earmarks/index.php
26As we have a long time series for each state, we are not concerned about ’short T ’ bias in panel data

IV. We apply instrumental variables estimator directly to equation (14).

27Looking at earmarks data, we can see that the Senate Appropriation Committee (although smaller than
the House of Representative’s Committee) send more earmarks. This might be one reason for why using the
Senate Appropriation Committee variable yields better ﬁrst stage results.

28Results for other measures of innovativeness are consistent and available upon request.
29It may seem surprising that an appointment on the appropriation committee should already have an

20

In addition, the share of the ﬁnancial sector is, as expected, positively correlated with
the top 1% income share (but signiﬁcantly only in the last three columns) while the share
of the public sector aﬀects top income inequality negatively.

As already stressed above, changes in the appropriation committee are hard to predict,
as they often result from the death of current committee members. Yet, one might raise the
possibility that some talented and rich inventors learn about a representative from another
state having just been elected on the appropriation committee, and subsequently decide to
move to that state so as to beneﬁt from future earmarks. This would enhance the positive
correlation between top income inequality and innovation although not for the reason to
be captured by our IV strategy.30 However, building on Lai et al. (2013), we were able to
identify the location of successive patents by a same inventor. This in turn allowed us to
delete patent observations pertaining to inventors whose previous patent was not registered
in the same state. Our results still hold when we look at the eﬀect of patents per capita on
the top 1%, with a regression coeﬃcient which is essentially the same as before (equal to
0.154).31

4.3.2

Instrumentation using the knowledge spillovers

To add further evidence of a causal link from innovativeness to top income shares, we exploit
a second instrument based on knowledge spillovers. The idea is to instrument innovation in
a state by the sum of innovation intensities in other states weighted by the propensity to cite
patents from these other states. Citations reﬂect past knowledge spillovers, hence a citation
network reﬂects channels whereby future knowledge spillovers occur. Knowledge spillovers
in turn lower the costs of innovation (in the model this corresponds to a decrease in θI or
θE). For example, patents applied from Massachusetts in 2001 have made 56109 citations
to patents outside Massachusetts. Among those citations, 1622 (3%) are made to patents
applied from Florida before 2001. Thus, the relative inﬂuence of Florida on Massachusetts
in 2001 in terms of innovation spillover can be set at 3%.

We then compute the matrix of weights by averaging bilateral innovation spillovers be-
tween each pair of states over the period from 1970 to 1978.32 With such matrix, we compute
if m(i, j, t) is the number of citations from a patent in state i,
our instrument as follows:
with an application date t, to a patent of state j, and if innov(j, t) denotes our measure of

impact on innovation after only one year. Note that separating between universities patent and non-university
patents, we did ﬁnd that the impact after one year was stronger on the former type. In addition, this is
consistent with Toole (2007) who shows that in the pharmaceutical industry, the positive impact of public
R&D on private R&D is the strongest after 1 year.

30Moretti and Wilson (2014) indeed showed that in the biotech industry, the decline in the user cost of
capital in some US states induced by federal subsidies to those states, generated a migration of star scientists
into these states.

31The Bayh-Dole Patent and Trademark Amendments Act of 1980 allowed universities to obtain patents
on research funded by the federal governments. This could have aﬀected the (ﬁrst-stage) relationship between
the composition of the Appropriation Committees and a state’s innovativeness. However, removing the ﬁrst
few years from the estimation does not change our baseline results.

32Indeed we observe patents whose application date is before 1975 as long as they were granted after 1975.

21

innovation in state j at time t, then we posit:

wi,j =

m(i, j, T )

m(i, k, T )

(cid:88)

k(cid:54)=i

and KSi,t =

1
P op−i,t

(cid:88)

j(cid:54)=i

wi,j × innov(j, t − 1),

where T is the length of the period (1970-1978) used to compute the weights wi,j, P op−i,t is
the population of all states except state i and KS is the instrument.33,34

Table 5 presents the results when the logarithm of KS is used to instrument for the
logarithm of our various measures of innovativeness: the number of patents in column 1,
the number of citations received within a 3, 4 or 5 year windows in columns 2, 3 and 4
respectively, the total number of citations in column 5, and the number of patent within the
5% most cited in the year in column 6. The coeﬃcients are always positive and signiﬁcant.35
Reverse causality from top income inequality to this knowledge spillover IV seems unlikely
(the top 1% income share in one state is unlikely to cause innovations in other states).36
One may also worry that this instrument captures regional or industry trends that are not
directly the result of innovation and yet aﬀect both top income inequality and innovation
in that state. However, we do control for state-level per capita GDP and for the output
gap, which both capture such trends.37 In addition, using the same weights as before, we
calculate and then control for a weighted average of other states’ per capita GDP (variable
Spill Gdppc). Finally, the weights wi,j are only weakly correlated with the distance between
states (the coeﬃcient is a little less than 0.2). Overall, our two instrumentation strategies,
based respectively on the appropriation committee composition and on cross-state innovation
spillovers, suggest a causal link between innovativeness and the top 1% income share.38

33We normalize our spillover measures for each state by the total population across the other US states.
Without this correction, our measure of spillovers would mecanically put at a relative disadvantage a state
which is growing relatively faster than other states. Nevertheless, our results still hold without it.

34Our results are also robust to adding the 2 year lag innovation as a control, in order to make sure that
our instrument does not only capture lagged innovation, and to removing California from the sample, which
is the most important state in our weighting.

35The negative and signiﬁcant coeﬃcient on per capita GDP may reﬂect the eﬀect of some omitted variable
like education which would aﬀect per capita GDP postively and top income inequality negatively. In fact,
when we control for the number of students per capita, this negative coeﬃcient is largely reduced and is no
longer signiﬁcant while all our results remain consistent. In any case, the coeﬃcient of innovation remains
unchanged when we remove per capita GDP from the set of control variables. This in turn suggests that
whatever causes the coeﬃcient on per capita GDP to be negative, does not interfere in any major way with
the eﬀect of innovativeness on top income inequality.

36Yet, reverse causality might arise from the same ﬁrm citing itself across diﬀerent states. We check that
this has, if anything, a very marginal eﬀect by removing citations from a ﬁrm to itself in two diﬀerent states
when constructing the weights: these results are essentially unaﬀected by this change.

37Moreover, we show in Section 4.5 that controlling for the size of additional sectors like computer manu-

facturing or chemistry does not aﬀect our results.

38When the two instruments are used together, the eﬀect of innovativeness on the top 1% income share
remains positive and signiﬁcant. The ﬁrst stage F stat is a little lower than with the Senate Committee of
Appropriation instrument but still acceptable. Finally, there is no evidence of overidentiﬁcation when the
Sargan-Hansen test is used. See column (1) of Table 6 to see the regression of innovation on top income
when the two instruments are combined.

22

One might question the fact that some of our control variables are endogenous and
that, conditional upon them, our instruments may be correlated with the unobservables in
our model. To check that this is not the case, we re-run our IV regressions, both with each
instrument separately and with both instruments jointly, with state and year ﬁxed eﬀects but
removing the control variables. And in each case we ﬁnd that the coeﬃcient of innovation
is only slightly altered compared to when run the corresponding IV regressions with all
the control variables. For example, when using our two instruments jointly the regression
coeﬃcient varies from 0.158 when we include the control variables to 0.155 when we exclude
them. The same is true when we run our IV regressions with all the control variables but
instrumenting each control variable by its 1 year lag value: the coeﬃcients on innovation are
almost identical to those in the baseline IV regressions.39

It is also remarkable that our two instruments yield very similar estimates for the impact
of innovation on top income inequality (e.g. the coeﬃcient is 0.166 in Table 4 versus 0.162
in Table 5), all the more since the two estimations rely on very diﬀerent sources of variation:
controlling for year and state ﬁxed eﬀects, the correlation between the two instruments is
very low (-5.8%). Note also that the magnitudes of the coeﬃcients are larger than in the OLS
case. This latter ﬁnding suggests that the OLS coeﬃcients are biased downward, possibly as
the result of some omitted variables that increase top income inequality but adversely aﬀect
innovation.40

More details on the IV regressions (including the ﬁrst stage and reduced form results)

are available in the Appendix.

4.3.3 Magnitude of the eﬀects

The above results suggest a causal eﬀect of innovativeness on top income shares at the cross
state panel level. At this stage it is worth setting back and looking at the magnitude of
this eﬀect. From our IV regressions in Tables 4 and 5, we see that an increase in 1% in
the number of patents per capita increases the top 1% income share by 0.17% and that
the eﬀects of a 1% increase in the citation-based measures are of comparable magnitude.
This means for example that in California where the ﬂow of patents per capita has been
multiplied by 3 and the top 1% income share has been multiplied by 2.3 from 1975 to 2009,
the increase in innovativeness can explain 22% of the increase in the top 1% income share
over that period. On average across US states, innovativeness as measured by the number of

39The key assumption is that the unobservables in the model are mean independent of the instruments

conditional on the included controls.

40Such variables may typically include entry barriers (e.g. associated with lobbying or corruption) that
aﬀect innovation by entrants negatively and yet contribute to increasing top income inequality by enhancing
incumbents’ rents. As shown below, lobbying is indeed positively correlated with the top 1% income share
and negatively correlated with the ﬂow of patents. Accordingly, our theoretical model in section 2.2.3 predicts
that higher mark-ups by non-innovator incumbents can have a positive impact on inequality but a negative
one on innovation.
Inequality by itself may cause lower innovation, for instance if concentrated wealth
negatively impacts innovation by poor credit-constrained individuals (as argued by Banerjee and Newman,
1993, Galor and Zeira, 1993, Benabou, 1996, and Aghion and Bolton, 1997). Finally, measurement errors
provide an additional explanation for a downward bias of the OLS coeﬃcients, especially to the extent that
the relationship between our measure of innovation quality and the revenues generated by an innovation may
be quite noisy.

23

patents per capita explains about 17% of the total increase in the top 1% income share over
the period between 1975 and 2010. Looking now at cross state diﬀerences in a given year,
we can compare the eﬀect of innovativeness with that of other signiﬁcant variables such as
the importance of the ﬁnancial sector and the government size. Our IV regressions suggest
that if a state were to move from the ﬁrst quartile in terms of the number of patents per
capita in 200041 to the fourth quartile, its top 1% income share would increase on average
by 1.5 percentage points. Similarly, moving from the ﬁrst to the fourth quartile in terms of
the number of citations, increases the top 1% income share by 1.6 percentage points. By
comparison, moving from the ﬁrst quartile in terms of the size of the ﬁnancial sector the
fourth quartile, would lead to a 1.0 percentage point increase in the top 1% income share.

Our results are likely to understate the true impact of innovation on top income inequality
at the national level for at least two reasons. First, if successful, an innovator from a relatively
poor state, is likely to move to a richer state, and therefore not contribute to the top 1%
share of her own state. Second, an innovating ﬁrm may have some of its owners and top
employees located in a state diﬀerent from that of inventors, in which case the eﬀect of
innovativeness on top income inequality will not be fully internalized by the state where the
patent is registered.42 Nevertheless, overall we ﬁnd a sizeable eﬀect of innovativeness on top
income inequality.

4.4 Other measures of inequality

In this section, we perform the same regressions as before but using broader measures of
inequality: the top 10% income share, the Gini coeﬃcient, the Atkinson index, the Theil
index and the Relative Mean Deviation of the distribution of income, which are drawn from
Frank (2009). Moreover, with data on the top 1% income share, we derive an estimate for
the Gini coeﬃcient of the remaining 99% of the income distribution, which we denote by
G99 where:

G99 =

G − top1
1 − top1

,

where G is the global Gini and top1 is the top 1% income share. In order to check if the eﬀect
of innovativeness on inequality is indeed concentrated on the top 1% income, we compute
the average share of income received by each percentile of the income distribution from top
10% to top 2% and compare the coeﬃcient on the regression of innovation on this variable
with the one obtained with the top 1% income share as left hand side variable. This average

41We chose 2000 as a reference year because it is the last year for which we have non corrected patents

data. Results remain consistent when the reference year changes.

42Not all innovations are patented. Yet, as long as the share of patented innovation does not vary across
states in a given year, this does not bias our estimation results. However, if this share is not constant
overtime (for instance, because of regulatory changes), it does aﬀect our measure of the increase in innovation.
In particular, if the share of innovations that get patented has increased over time, then the increase in
innovation is less than the measured increase in patents and innovation can only explain a smaller share of
the rise of top income inequality. Kortum and Lerner (1999), however, do argue that the sharp increase in
the number of patents in the 90’s reﬂected a genuine increase in innovation and a shift towards more applied
research instead of regulatory changes that would have made patenting easier.

24

size is equal to:

Avgtop =

top10 − top1
9

where top10 represents the size of the top 10% income share. Table 6 shows the results
obtained when regressing these other measures of inequalities on innovation quality.43
In
this table we instrument innovativeness using our two types of instruments, namely the
two year lag in the appropriation committee composition in the Senate and the knowledge
spillover instrument, jointly. Column 1 reproduces the results for the top 1% income share.
Column 2 uses the Avgtop measure, column 3 uses the top 10% income share, column 4 uses
the overall Gini coeﬃcient and column 5 uses the Gini coeﬃcient for the bottom 99% of
the income distribution to measure income inequality on the left-hand side of the regression
equation. Columns 6 and 7 use two broader measures of inequality, namely the Atkinson
Index with parameter 0.5 and the Theil index. The eﬀect of innovativeness is non signiﬁcant
for the Theil Index neither is it for the Atkinson index.

Looking at column 2 of Table 6, we see that the eﬀect of innovativeness on the share of
income received by the top 10 to top 2% of the income distribution is signiﬁcant but the
coeﬃcient is negative. Gini indexes (columns 4 and 5) show negative although not signiﬁcant
coeﬃcients.

Together, these results strongly suggest that the link between innovativeness and top in-
come inequality is mainly driven by what happens at the very top of the income distribution,
and speciﬁcally at the top 1% income share.44

4.5 Robustness checks

In this subsection we discuss the robustness of our regression results.

4.5.1 Choice of lags

One may question the interpretation of our positive and signiﬁcant coeﬃcients on the one
year lagged innovation variable in our regressions. In particular, some may legitimately argue
that one year after the application date is too short to have an impact on the inventor’s
income, especially since it takes on average two years between the application date and the
date at which the patent is granted by the patent oﬃce.45 Nevertheless we stick to the
view that our positive and signiﬁcant coeﬃcients on the one year lagged innovation variable,

43We chose to present results for the 3 year window citation variable but results are similar when using

other measures of innovation quality.

44We also explored the data on the share of income held by the top 0.1% at the state level, directly
provided to us by Mark Frank. These data are not as reliable as other measures of inequality and this is
why we chose to concentrate on the top 1% in our analysis of the relationship between innovation and top
income inequality. Yet, when running the same regression with the log of the top 0.1% income share as the
left-hand side variable, the coeﬃcient of innovation remains positive and signiﬁcant, only slightly smaller
than the coeﬃcient of innovation on the log of the top 1% income share.

45For example, using Finnish individual data on patenting and wage income, Toivanen and Vaananen
(2012) ﬁnd an average lag of two years between patent application and patent grant, and they ﬁnd an
immediate jump in inventors’ wages after patent grant.

25

already captures the eﬀect of innovativeness on top income inequality. In particular, patent
applications are often organized and supervised by ﬁrms who start paying for the ﬁnancing
and management of the innovation right after (or even before) the application date as they
anticipate the future proﬁts from the patent. Also, ﬁrms may sell a product embedding an
innovation before the patent has been granted, thereby already appropriating some of the
proﬁts from the innovation.

Yet as a robustness check, we investigate what happens when longer innovation lags are
included in the regression. More speciﬁcally, in our regression of the log of the top 1% in-
come share on the log of the number of patents per capita (jointly instrumented by our two
IVs) we allow the lag in innovativeness to vary from 1 to 5 years, and we lagged the instru-
ments correspondingly. As seen in Table 7, the coeﬃcient on innovation is always strongly
signiﬁcant and positive, regardless of which lag we are using. Moreover, the magnitude of
the coeﬃcient increases as we move from 1 to 3 year lag and then decreases before losing
signiﬁcance when the lag goes beyond 5 years—suggesting that, in line with the theory, the
impact of a given innovation on top income inequality is temporary. We also checked the
robustness of our results to using the granting date instead of the application date.46

Finally, we run an OLS regression to look at the eﬀect on top 1% income share at date
t when innovation is averaged over non-overlapping three year windows (that is, we count
patents with application dates between t − 1 and t − 3). As seen in column 6 of Table 7,
the coeﬃcient on innovation is still highly signiﬁcant and its magnitude is higher than when
only patents ﬁled at t − 1 are included.47

4.5.2 The role of two speciﬁc sectors: ﬁnance and natural resources

When considering top income shares and other inequality measures on the one hand and
innovativeness on the other hand, we abstracted from industry composition in the various
states. However, two particular sectors deserve to be considered more closely: Finance and
Natural resources.

The ﬁnancial sector is overrepresented in the top 1% income share (even though most
individuals in the top 1% do not work in the ﬁnancial sector). More speciﬁcally, Guvenen,
Kaplan and Song (2014) ﬁnd that 18.2% of individuals in the top 1% work in the Finance,
Insurance and Real Estate sector (versus 5.3% for the rest of the population), and that these
individuals’ income is particularly volatile. To make sure that our eﬀects are not mainly
driven by the ﬁnancial sector, in the above regressions we already controlled for the share of
the ﬁnancial sector in state GDP.

Here, we perform additional tests. First, we add the average employee compensation in
the ﬁnancial sector as a control to capture any direct eﬀect an increase in ﬁnancial sector’s
employee compensation might have on the top 1% income share. Second, we exclude states

46 We ﬁnd a regression coeﬃcient which is a little higher than before, and closer to the 3 and 4 year lag
coeﬃcients in the regressions on patent application. This is in turn consistent with the time lag between
patent application and patent grant being of about two years (not shown here).

47Here, we just show the OLS results, but we performed the IV estimation and found a signiﬁcant coeﬃcient
which is also larger than in the 1 year window case (0.228). Note however, that given the short time period
(T=10) the IV results are biased in this case.

26

in which ﬁnancial activities account for a large fraction of GDP. We selected four such states:
New York, Connecticut, Delaware and South Dakota, which are the four states where the
ﬁnancial sector’ share in GDP is the highest.

Third, ﬁnancial innovations themselves might directly increase rents and therefore the
top 1% income share. To account for this latter channel, we subtract patents belonging to
the class 705: “Financial, Business Practice” related to ﬁnancial activities in order to exclude
innovations in the ﬁnancial sector.

The IV regressions of the top 1% income share on innovativeness (measured by the
number of citations per capita) corresponding to these three robustness tests are presented
in Table 8, respectively in columns 1, 2 and 3.48 In each case, the eﬀect of innovativeness on
the top 1% income share is signiﬁcant and positive, showing very stable values when moving
from one speciﬁcation to another.

Another potential issue related to ﬁnance is that ﬁnancial development should impact
both innovation (by providing easier access to credit to potential innovators) and income
inequality at the top (by boosting high wages). Our IV strategy should in principle ad-
dress omitted variable issues including this one, yet here we construct a variable speciﬁcally
designed to directly capture this channel. For each US state, we divide patent application
in that state into 16 NAICS categories and use the external ﬁnancial dependence index
computed by Kneer (2013) and averaged over the period 1980-1989. External ﬁnancial de-
pendence is deﬁned as the ratio of capital expenditure minus cash ﬂow divided by capital
expenditure (see Rajan and Zingales, 1998). We multiply the number of patents in each
NAICS sector in that state by that index and then divide by the total number of patents
to compute a variable representing the level of ﬁnancial dependence of innovation. This
variable (denoted EFD in Table 8) should capture a variation in innovativeness at state-level
driven by a sector that is highly dependent on external ﬁnance. Results for regressing the
top 1% income share on the number of citations per capita when controlling for EFD are
presented in column 4. We see that the eﬀect of innovativeness remains signiﬁcant, even if
the coeﬃcient is slightly lower than the corresponding coeﬃcient when we do not control for
EFD in Tables 5 and 6.

Natural resources and oil extraction represent a large share of GDP in certain states
(Wyoming, West Virginia and particularly Alaska oil extraction activities account for almost
30% of total GDP in 2009), so that in these states the top 1% income share is likely to be
aﬀected by these sectors which are quite volatile (oil extraction is highly sensitive to energy
prices ﬂuctuation). To deal with this concern, we control for the share of natural resources
in GDP. In addition, we ﬁrst add the share of oil extraction related activities in state GDP
as a control variable; and second, we remove patents from class 208 (Mineral oils: process
and production) and 196 (Mineral oils: Apparatus). Results are presented in columns 5 and
6 of Table 8. Here again, our results remain signiﬁcant.49

48In this table we jointly instrument by the appropriation committee and knowledge spillover variables.
49We obtain similar results when using other measures of innovativeness.

27

4.5.3 Looking at industry composition

In this subsection, we check that our results are robust to controlling for sectors’ size. First,
we use the previous decomposition into 16 NAICS categories to remove patents related to
the NAICS numbered 334: “Computer and Electronic Products”, to deal with the concern
that the eﬀect of innovativeness on top income inequality might be concentrated in the fast-
growing computer industry. Similarly, we remove patents from the pharmaceutical sector
(NAICS 3254) and from the electrical equipment sector (NAICS 335).
In each case, we
conduct an IV panel regression combining our two instruments.

The baseline results are presented in columns 1 to 3 of Table 9. Then, in our regressions
we add controls for the logarithm of the value-added of these three NAICS. As seen in column
4 of Table 9, the coeﬃcient on innovation remains positive and signiﬁcant throughout.

In addition, we used the COMTRADE database to look at the extent to which our eﬀect
of innovation on top income inequality is driven more by more exporting sectors. Over the
period from 1975 to 2010, we identiﬁed three sectors that are particularly export-intensive:
Transportation, Machinery and Electrical Machinery. When we regress the top 1% income
share on patenting from those three sectors versus on patenting from other sectors, and using
our two instruments jointly, we obtain a higher coeﬃcient when restricting attention to the
three most exporting sectors (column 5 of Table 9): 0.251 versus 0.168 for the other sectors
(column 6 of Table 9). This result is in line with the notion that larger markets increase the
reward from innovation, thereby increasing the eﬀect of innovation on top income inequality.

4.5.4 Accounting for changes in top tax rates

Taxation is likely to aﬀect both innovation incentives and the 1% income share. In particular,
high top marginal income tax rates may reduce eﬀorts by top earners, divert their pay from
wages to perks, and reduce their incentives to bargain for higher wages (see, in particular,
In this subsection, we address this concern more
Piketty, Saez and Stantcheva, 2014).
directly, even though our IV strategy is meant to address omitted variable bias issues like
this one.

More speciﬁcally, we use data from the NBER TAXSIM website.50 This database provides
information on marginal tax rates for various levels of incomes ($10000, $25000, $50000,
$75000 and $100000 yearly incomes) and for labor, capital and interest incomes from 1977
onward. We use the state marginal labor income tax rate for individuals earning $100000
per year as an additional control when regressing the top 1% income share on innovativeness.
The results are displayed in Column (7) of Table 8: the eﬀect of innovativeness on the top
1% income share remains positive and signiﬁcant.51

4.6 Star inventors and top income shares

Some innovators are more highly talented than others and therefore more likely to move
up to the top 1% income bracket themselves or help the top management in their ﬁrms

50http://users.nber.org/ taxsim/state-tax-tables/
51Results are similar when other marginal top tax rates are used as controls.

28

enter the top 1% (in terms of our model such innovators would generate innovations with
size greater than ηH, thereby further increasing the share of entrepreneurial income). To
assess the inﬂuence of the most talented innovators more directly, we calculate the number
of “star inventors” in each state each year. Following Acemoglu et al. (2014), we deﬁne a
star inventor by looking at the adjusted number of citations to her patents in a given year52.
We then rank inventors according to two criteria: the maximum and the average number of
citations they received.53 Each inventor is then associated with a score for each year, and a
star inventor is deﬁned as one that made it to the top 5% according to that score.

The USPTO database, combined with the work of Lai et al. (2013), allows us to look
at inventors for each patents granted from 1975 to 2010. We aggregate this measure at the
state level by computing the number of star inventors per capita in each state and each
year. If a star inventor has diﬀerent patents in diﬀerent states, each state is attributed its
corresponding fraction of the inventor’s citations. Then we use our instruments to conduct
a 2SLS IV regression. Results are presented in Table 10. Columns 1 to 3 use the maximum
number of citations as a criterium to detect star inventors while columns 4 to 6 use the mean
number of citations. In every case, the results show that an increase in the number of star
inventors in a given state has a positive and signiﬁcant eﬀect on the top 1% income share.

5 Discussion and extensions

In this section we extend our core analysis in four directions: ﬁrst, we show the robustness
of our core results to moving from cross-state to cross-CZ analysis; second, having moved to
CZ-level analysis we consider the relationship between innovativeness and social mobility;
third, when analyzing the relationship between innovativeness and top incomes or social
mobility, we distinguish between entrant and incumbent innovation; then, we focus on a
particular source of entry barriers, namely lobbying activities across US states, and we look
at how lobbying intensity aﬀects the impact of innovativeness on top incomes and on social
mobility.

5.1 From cross-state to CZ-level analysis

Panel data on social mobility in the United States are not (yet) available. Therefore, to study
the impact of innovativeness on social mobility without reducing the number of observations
too much, we move from cross-state to cross-commuting zones (CZ) analysis and use the
measures of social mobility from Chetty et al (2014). A commuting zone (CZ) is a group
of neighboring counties that share the same commuting pattern. There are 741 commuting
zones which cover the whole territory of the United States. Some CZs are in rural areas
whereas others are in urban areas (large cities and their surroundings). At the CZ level,
we do not have data on top income shares for the whole population. However, Chetty et al

52Similar deﬁnitions of superstars are also used in Akcigit, Baslandze and Stantcheva (2015) who study

the international mobility of superstar inventors in response to top tax rate changes

53The number of citations has been corrected so as to compare between inventors across various techno-

logical ﬁelds.

29

(2015) use the 2000 census to provide estimates for the top 1% share as well as for the Gini
index for a sample of adults both at the CZ and the MSA levels. Using that information,
we compute cross-sectional measures of inequality as an average between 1996 and 2000. If
we look at urban CZs, the three largest top 1% income shares are in New York (23.6%), San
Jose (26.4%) and San Francisco (29.1%), all of which are highly innovative areas.

To associate a patent to a CZ location, we rely on Lai et al. (2013) to complete the
USPTO database as we did when looking at star scientists. This enables us to associate
each inventor with her address and her zipcode which can be linked up to a county, and
ultimately to a commuting zone. Finally, we aggregate county level data on GDP and
population from the BEA to compute GDP per capita and population growth. All other
data are taken from Chetty et al. (2014).

Using all these data, we can ﬁrst check whether the eﬀects of innovation on the top 1%
income share and on the Gini index are consistent with our cross-states ﬁndings (we compute
the innovativeness measure over the 1992-1996 period). Table 11 displays the results from
the regression when the logarithm of the number of patents per capita is used as a measure
of innovation. We add controls for GDP per capita, for the growth of total population and
for the size of local government proxied by the logarithm of the local government’s total
expenditure per capita. In addition, we also add a control for the labor force participation
rate in 1996-2000, for school expenditures in the same period, for the college graduation rate
and for the share of the manufacturing sector. Finally, standard errors are clustered at the
state level to account for potential correlation across neighboring CZs.54

As seen from the ﬁrst two columns of Table 11, the eﬀect of innovativeness on the top
1% income share is positive and signiﬁcant (column 1) and robust to adding many controls
(column 2). When regressing innovativeness on other measures of inequalities, the coeﬃ-
cients are negative for the bottom 99% Gini and positive for the overall Gini although not
signiﬁcant. Interestingly, the labor force participation rate and education related variables
have a negative impact on all our measures of inequality. The positive eﬀect on the top
1% is consistent with our core results and once again, we observe that the positive eﬀect of
innovation on inequality is focused on the top of the distribution.

5.2 The eﬀect of innovation on social mobility

Having moved from cross-state to cross-CZ analysis allows us to look at how innovativeness
aﬀects social mobility, using the various measures of social mobility in Chetty et al. (2014)
combined with our local measures of innovation and with the various controls mentioned
above. There, absolute upward mobility is deﬁned as the expected percentile or “rank”
(from 0 to 100) for a child whose parents belonged to some P percentile of the income
distribution. Percentiles are computed from the national income distribution. The ranks are
computed over the period 2011-2012 when the child is aged around 30 whereas the percentile
P of parents income is calculated over the period between 1996 and 2000 when the child was
aged around 15. In addition, Chetty et al. (2014) provide transition matrices by CZ and
in other words, one can estimate the probability for a child to reach quintile
by quintile:

54Here again, when no patent has been granted in a CZ, we set the innovativeness variable to 0 and add

a dummy equal to one in that case.

30

i of the national income distribution when the parents belonged to quintile j for all (i, j).
Once again, the intensity of innovativeness in each CZ is measured by the average number
of patents per capita, but this time, we take the averages over the period 2006-2010.

If we focus on the 50 largest commuting zones in our sample and sort them by the
probability for a child to reach the highest quintile when the child’s parents belonged to
the lowest quintile, we ﬁnd that the top 10 CZs in term of upward mobility at the top
include: San Jose, San Diego, San Francisco, Seattle, New York, Boston, Sacramento and
Los Angeles. These cities, most of them located in California, are among the most innovative
in the US. At the other end of the spectrum, we ﬁnd CZs like Charlotte, Memphis or Atlanta
with a very small amount of patents per capita. As argued in Chetty et al. (2014), social
mobility in the US exhibits a high degree of geographic heterogeneity, and if mobility is lower
on average than in other developed countries, in the regions where mobility is the highest it
is comparable to the levels observed in Canada or Sweden.

One potential concern with these data for our purpose, is that social mobility is based
on the location of the parents not the children, and therefore the data do not account for
children who move to and then innovate in a diﬀerent location from that of their parents.
if many individuals migrate
However, if anything this should bias our results downwards:
out of a speciﬁc CZ to innovate in San Francisco or New York, this CZ will exhibit high
social mobility but low innovativeness.

We thus conduct the following regression:

log(M obi) = A + β1log(innovi) + β2Xi + εi,

where M ob is our measure of upward social mobility, and innov is our Measure of innovation
(the number of patents per capita at the CZ level). We cluster standard errors by state.
Table 12 presents our results for this cross-section OLS regression. We add our regular set of
controls including the share of the manufacturing sector, the labor force participation rate
taken in 1996-2000, the college graduation rate and the local expenditures in public school
per student during the same period. Columns 1 and 4 look at the eﬀect of innovativeness on
upward mobility when parent income belongs to the 25th percentile. The eﬀect of innova-
tiveness is positive and signiﬁcant. Columns 2, 3, 5 and 6 show the eﬀects of innovativeness
on the probability for a child to belong to the highest quintile in income distribution at age
30 when her parent belonged to a lower quintile. The lower the quintile to which parents
belonged, the more positive and signiﬁcant is the correlation between innovativeness and
upward mobility.55 Not surprisingly, school expenditures, the college graduation rate and
labor force participation rate also play a positive role in explaining upward social mobility,
while the size of the manufacturing sector is negatively correlated. Finally, column 7 shows
the overall eﬀect of innovativeness on upward mobility measured by the probability to reach
the highest quintile when parent belonged to any lower quintile. Here again, the correlation
is positive and signiﬁcant.

One concern is worth mentioning here: in some CZs, the size of the top quintile is very
small, reﬂecting the fact that it is almost impossible to reach this quintile while staying in

55If we continue with quintiles 3 and 4, the eﬀect of innovativeness on social mobility is still signiﬁcant for
quintile 3 (but only when college per capita and manufacturing share are not include) and negative and not
signiﬁcant for quintile 4.

31

this CZ. This case often occurs in rural areas: for example, in Greenville, a CZ in Mississippi,
only 7.5% of children in 2011-2012 (when they are 30) belong to the highest quintile in the
national income distribution. To address this concern, we conduct the same regressions as
above but we remove CZs where the top quintile has a size below 10% and below 15% (this
excludes respectively 7 and 100 CZs). All our results remain consistent with columns 1 to
6 of the previous regressions.56 In fact, the results are even stronger, with the coeﬃcient of
innovation being now always signiﬁcant at the 5% level.

All the results presented in this section are consistent with the prediction of our model
that innovativeness increases mobility at the top. Yet, we should bear in mind that these are
just cross-sectional OLS correlations, and this remark holds for all other CZ level regressions
in this section.

5.3 Entrant versus incumbent innovation

Our empirical results have highlighted the positive eﬀects of innovativeness on top income
inequality and also on social mobility. Now, our model suggests that the eﬀect of innova-
tiveness on social mobility should operate mainly through entrant innovation, meanwhile
the eﬀect on top income inequality operates through both types of innovation.
In order
to distinguish between incumbent and entrant innovation in our data, we declare a patent
to be an “entrant patent” if the time lag between its application date and the ﬁrst patent
application date of the same assignee amounts to less than 3 years.57 We then aggregate the
number of “entrant patents” as well as the number of “incumbent patents” at the state level
from 1979 to 201058 and at the CZ level by averaging between 2006 and 2010.

We ﬁrst focus on the eﬀect of entrant innovation on social mobility. We thus conduct
the same regression as in the previous section at the cross CZ level but considering sepa-
rately entrant innovation and incumbent innovation on the right hand side of the regression
equation. Table 13 presents our results. Columns 1 to 3 regress our three measures of social
mobility on the number of “entrant patents” per capita, whereas columns 4 to 6 regress the
three measures of social mobility on the number of “incumbent patents”. The positive and
signiﬁcant coeﬃcients in the ﬁrst three columns, as compared to columns 4 to 6, suggest that
the positive eﬀect of innovativeness on social mobility is mainly driven by entrants. This
conjecture is conﬁrmed by the horse race regression in column 7 in which both entrant inno-
vation and incumbent innovation are included as right-hand side variables. There, we clearly
see that all the eﬀect of innovation on social mobility is associated with entrant innovation.

56This result is conﬁrmed by performing the same regression on the whole sample of CZs but adding an
interaction term between the number of patents per capita and a dummy equal to one if the CZ has a top
quintile of size higher than 15% of total CZ population. The coeﬃcient for this interaction term is positive
and signiﬁcant.

57We checked the robustness of our results to using a 5-year lag instead of a 3-year lag threshold to deﬁne
entrant versus incumbent innovation. Here we only focus on patents issued by ﬁrms and we have removed
patents from public research institute or independent inventors.

58We start in 1979 to reduce the risk of wrongly considering a patent to be an “entrant patent” just
because of the truncation issue at the beginning of the time period. In addition, we consider every patent
from the USPTO database, including those with application year before 1975 (but which were granted after
1975).

32

Next, we look at the eﬀect of entrants’ innovation on top income inequality, making full
use of our panel data at the cross state level. Following our deﬁnition of entrant innovation,
17% of patent applications from 1979 to 2010 can be considered “entrant” (this number
increases up to 23.7% when we use the 5-year lag threshold to deﬁne entrant versus incum-
bent innovation). These “entrant” patents have more citations than incumbent patents, for
example in 1980, entrant patents have 11.4 citations on average while incumbent only have
9.5 citations, conﬁrming the intuitive idea that entrant patents correspond to more radical
innovations (see Akcigit and Kerr, 2010).

Table 14 presents the results from the OLS panel regression of the top 1% income share
over two measures of innovativeness (number of patents per capita and number of citations
per capita), restricting attention respectively to entrant patents (columns 1 and 4) and to
incumbent patents (columns 2 and 5).59 The coeﬃcients on innovativeness are always posi-
tive and signiﬁcant when innovativeness refers to either entrant innovation or to incumbent
innovation, yet with a smaller coeﬃcient for the latter. In addition, columns 3 and 6 regress
the top 1% income share on both incumbent and entrant innovation, conﬁrming that both
types of innovations show signiﬁcant coeﬃcients,60 in line with what the theory predicts.

5.4 Lobbying as a dampening factor

To the extent that lobbying activities help incumbents prevent or delay new entry, our conjec-
ture is that places with higher lobbying intensity should also be places where innovativeness
has lower eﬀects on the top income share and on social mobility.

Measuring lobbying expenditures at state or at CZ level is not straightforward. In partic-
ular, the OpenSecrets project61 provides sector speciﬁc lobbying expenditure only at national
level, not at the state and CZ levels. In order to measure lobbying intensity at the state
level, we construct for each state a Bartik variable, as the weighted average of lobbying
expenditure in the diﬀerent sectors (2 digits NAICS sectors), with weights corresponding to
sector shares in the state’s total employment from the US Census Bureau.

More precisely, we want to compute Lob(i, .) the lobbying expenditure in state i, knowing
only the national lobbying expenditure Lob(., k) by sector k. We then deﬁne the lobbying
intensity by sector k in state i as:

Lob(i, k) =

Lob(., k),

emp(i, k)
I
(cid:88)

emp(j, k)

j=1

where emp(i, k) denotes industry k’s share of employment in state i (where 1 ≤ k ≤ K and
1 ≤ i ≤ I).

59We do not show the IV regressions. What we obtain is that: (i) the IV regression using both instruments
works for incumbent innovation; (ii) the IV regression using the senate appropriation committee IV works
for entrant innovation if we add one year lag to the instrument; (iii) the knowledge spillovers instrument
does not work for entrant innovation. Overall, this is not too surprising: knowledge spillovers and federal
subsidies take time to be eﬀective and thus are more likely to aﬀect established ﬁrms than entrants.

60The diﬀerence between the two coeﬃcients is not statistically signiﬁcant.
61https://www.opensecrets.org/lobby/list indus.php

33

From this we compute the aggregate lobbying intensity in state i as:

K
(cid:88)

k=1

Lob(i, .) =

emp(i, k)Lob(i, k)

K
(cid:88)

k=1

emp(i, k)

At the CZ level, there is no sectoral employment composition, however, such data exist
at the cross MSA level for the manufacturing sector (we use a 3 digits NAICS level) from
the Longitudinal Employer Household Dynamics dataset. We therefore move the analysis
from CZ to MSA at this point and compute similar Bartik measures of lobbying intensity at
that level (in particular the number of patents has been aggregated at the zipcode level).

Our resulting measure of lobbying at state level places Mississippi, Arkansas and Wis-
consin as the three states with the highest intensity of lobbying activities, deﬁned as total
lobbying expenditures over GDP. This intensity is negatively correlated with the ratio of
new ﬁrms (deﬁned as ﬁrm of age 0 from the Census Bureau) and with the number of patent
application from entrants while it is positively correlated with the top 1% income share.
Thus, in states where lobbying intensity is stronger, entrants seem to have more diﬃculties
to innovate. Looking over time at states with lobbying intensity above the median, we ﬁnd
that this group remains quite stable. In fact, 23 states are in this group every year from
1998 to 2010 (and this is also true in 2011, 2012 and 2013). We deﬁne these states as high
lobbying intensity states and create a dummy equal to one whenever a state belongs to that
group.62 We then interact this dummy with the logarithm of the number of patents per
capita. Columns 1 and 3 of Table 15 shows the results respectively for the OLS (column 1)
and for the IV (column 3) regressions with both instruments of the top 1% income share on
the total number of citations per capita (in log and lagged) and the interaction term between
the dummy variable for high lobbying intensity and the log of the number of citations per
capita. The results shows that if the overall eﬀect of innovativeness on the top 1% income
share is always signiﬁcant and positive, the eﬀect is less strong in states with higher lobbying
intensity. In addition, in a horse-race regression (column 2) where we split the innovativeness
variable between entrant and incumbent innovation, we see that lobbying dampens the im-
pact of entrant innovations on the top 1% income share while it has no eﬀect on the impact
of incumbent innovation on the top 1% income share, as predicted by the model.

We now look at how lobbying intensity impacts on the eﬀect of innovativeness on social
mobility, using cross-MSA data. As explained above, we aggregated patent applications
by zipcode and then by MSA and used mobility data from Chetty et al. (2014) who only
provide absolute mobility data and no transition matrix for MSAs. Our regular control
variables (GDP per capita, population growth, share of ﬁnancial sector and government
size) have been found in the BEA and averaged over the period 2006-2010. Overall, we are
left with 352 MSAs which can be separated in two groups of equal size, respectively with high
and low lobbying activities. Columns 4 and 5 of Table 15 show the eﬀect of innovation as

62These 23 states are: AL, AR, IA, ID, IN, KS, KY, ME, MI, MO, MS, NC, NE, NH, OH, OK, RI, SC,

SD, TN, VT, WI and WV.

34

measured by the number of entrant patents per capita (in log) on the logarithm of absolute
upward mobility. Column 4 focuses on MSAs above median in terms of lobbying activities
and column 5 on other MSAs. Similarly, columns 6 and 7 look at the eﬀect of the number of
incumbent patents per capita on absolute upward mobility. We see that the eﬀect of entrant
innovativeness on social mobility is positive and signiﬁcant only for MSAs that are below
median in terms of lobbying intensity. In addition, incumbent innovation has no eﬀect on
social mobility, whether we look at MSAs above or below the median in terms of lobbying
intensity. These results conﬁrm the idea that lobbying dampens the impact of innovativeness
on social mobility by reducing the eﬀect of entrant innovation. To sum up, in line with our
model, lobbying reduces the impact of innovativeness on social mobility and its impact on
the top 1% income share.63

6 Conclusion

In this paper we have analyzed the eﬀect of innovation-led growth on top incomes and on
social mobility. Our results show positive and signiﬁcant correlations between innovativeness
or frontier growth on the one hand, and top income shares or social mobility on the other
hand. Our instrumentation at cross-state level suggests that these correlations at least
partly reﬂect a causality from innovativeness to top income shares. Moreover, the eﬀect
of innovativeness on top income inequality is of signiﬁcant magnitude: for example, when
measured by the number of patents per capita, innovativeness accounts on average across
US states for around 17% of the total increase in the top 1% income share between 1975 and
2010.

These ﬁndings suggest interesting avenues for further research on (innovation-led) growth,
inequality and social mobility. First, in our IV regressions we are only directly investigating
the causal impact of innovation on top income inequality, not the reverse. However, the
comparison between our OLS and our IV results suggests that there are key components
of top 1% inequality that should have a negative impact on innovation. Identifying these
components is certainly an important avenue for future research.

Another related extension would be to explore policy implications. In particular, how
do we factor in innovation in tax policy design, and how should we combine tax policy with
other policy instruments (competition and entry policy, patent policy, R&D subsidies,...) to
achieve more inclusive growth, i.e. reconcile the goals of enhancing innovation-based growth,
enhancing social mobility, and avoiding excessive income inequality?

Another extension would be to look at the eﬀect of innovation on top income inequality
in cross-country panel data. Preliminary OLS regressions show a positive and signiﬁcant
correlation between our innovativeness measures and top 1% income share in cross-country
panel.

63In line with these ﬁndings, in another regression which we are not showing here we ﬁnd that venture
capital -which presumably fosters entrant innovation- enhances the eﬀect of innovativeness on top income
inequality: using data on the total number of deals by states from the National Venture Capital Yearbook
2014, we ﬁnd that in states where venture capital intensity is higher, innovation has a more positive eﬀect
on top income, but only for entrants.

35

A fourth extension is to explore the relationship between innovation, top income inequal-
ity and social mobility using individual data on revenues and patenting.64 In particular we
are interested in questions such as: (i) are individuals coming from lower income brackets
more likely to make it to top income brackets when they are inventors rather than non-
inventors? (ii) how do factors such as innate ability, family situation, gender, education,
parental education or parental income aﬀect the probability for an inventor to make it to
top income brackets? In parallel work we are conducting such a study using Finnish indi-
vidual data over the period 1990-2000 (Aghion, Akcigit and Toivanen, 2015)). Note however
that while such studies based on the matching between individual patenting data and in-
dividual ﬁscal data, allows us to more directly identify the eﬀect of innovation on upward
income mobility for inventors, unlike our analysis in this paper they do not account for the
aggregate eﬀect of innovation on top income inequality: this eﬀect goes well beyond the
inventor as it involves all those who beneﬁt from the inventor’s innovation, starting with the
ﬁrm that employs the inventor.

A ﬁfth extension would be to look at innovation beyond patenting. As a ﬁrst step in
that direction, we looked at the relationship between top income inequality and frontier
versus non-frontier growth, where frontier growth is deﬁned as growth in states where labor
productivity is closer than the median to the productivity in the most productive US state
that year. Preliminary cross-state panel OLS regressions show a positive and signiﬁcant
correlation between top income inequality and frontier growth, but a negative correlation
between top income inequality and non-frontier growth. Overall, these two ﬁndings are
consistent with the view that the positive correlation between top inequality and growth, if
any, is driven by innovation-led growth.

Finally, our results on the impact of lobbying suggests that the relationship between
innovativeness and income inequality depends upon institutional factors which vary across
countries. Further research should thus look deeper into how institutions aﬀect the rela-
tionship between top income inequality and innovation. These and other extensions of the
analysis in this paper are left for future research.

References

[1] Acemoglu, D (1998), “Why Do New Technologies Complement Skills: Directed Techni-
cal Change and Wage Inequality”, Quarterly Journal of Economics, 113, 1055-1089

[2] Acemoglu, D (2002), “Technical Change, Inequality, and the Labor Market”, Journal

of Economic Literature, 40, 7-72

[3] Acemoglu, D (2007), “Equilibrium Bias of Technology”, Econometrica, 75(5),1371-1409.

[4] Acemoglu, D., Akcigit, U., and Alp Celik, M (2014), “Young, Restless and Creative:
Openness to Disruption and Creative Innovations”, NBER Working Papers 19894, Na-
tional Bureau of Economic Research, Inc.

64Following work by Toivanen and Vaananen (2012) and Bell et al (2015).

36

[5] Acemoglu, D., and Robinson, J (2015), “The Rise and Decline of General Laws of

Capitalism”, Journal of Economic Perspectives, 29 (1), 3-28.

[6] Aghion, P., Akcigit, U., and Howitt, P (2014), “What Do We Learn from Schumpeterian
Growth Theory?”, in Handbook of Economic Growth, ed. by P. Aghion and S. Durlauf,
Vol 2B: 515-563.

[7] Aghion, P., Akcigit, U., and Toivanen, O (2015), “Living the American Dream in Fin-

land: The Social Mobility of Innovators”, mimeo Harvard.

[8] Aghion, P., Boustan, L., Hoxby, C., and Vandenbussche, J (2009), “The Causal Impact

of Education on Economic Growth: Evidence from US”, mimeo Harvard.

[9] Aghion, P., and Bolton, P (1997), ”A Theory of Trickle-Down Growth and Develop-

ment”, Review of Economic Studies, 64, 151-172

[10] Aghion, P., Caroli, E., and Garcia-Penalosa, C (1999), “Inequality and Economic
Growth: The Perspective of the New Growth Theories”, Journal of Economic Lit-
erature, 37, 1615-1660

[11] Aghion, P., and Howitt, P (1992), “A Model of Growth Through Creative Destruction”,

Econometrica, 60, 323-351

[12] Aghion, P., and Howitt, P (1997), Endogenous Growth Theory, MIT Press.

[13] Akcigit, U., Baslandze, S., and Stantcheva, S (2015) “Taxation and the International

Mobility of Inventors,” NBER Working Paper #21024.

[14] Akcigit, U., and Kerr, W. (2010), “Growth Through Heterogeneous Innovations”, NBER

Working Paper #16443

[15] Alvaredo, F., Atkinson, A., Piketty, T. and Saez, E (2014), The World Top Incomes

Database, http://topincomes.g-mond.parisschoolofeconomics.eu/.

[16] Autor, D., Katz, L., and Krueger, A (1998), “Computing Inequality: Have Computers

Changed the Labor Market?”, Quarterly Journal of Economics, 113, 1169-1213

[17] Banerjee, A., and Newman, A (1993), “Occupational Choice and the Process of Devel-

opment”, Journal of Political Economy, 101, 274-298

[18] Banerjee, A., and Duﬂo, E (2003), “Inequality and Growth: What Can the Data Say?”,

Journal of Economic Growth, 8, 267-299.

[19] Bell, A., Chetty, R., Jaravel, X., Petkova, N., and Van Reenen, J (2015), “The Lifecycle

of Inventors” , mimeo Harvard.

[20] Benabou, R (1996), “Inequality and Growth”, NBER Macroeconomics Annual, 11, 11-

92

37

[21] Berman, E., Bound, J., and Griliches, Z (1994), “Changes in Demand for Skilled La-
bor Within US Manufacturing: Evidence from the Annual Survey of Manufactures”,
Quarterly Journal of Economics, 109, 367-397

[22] Blundell, R., Griﬃth, R., and Van Reenen, J (1995), “Dynamic Count Data Models of
Technological Innovation,” Economic Journal, Royal Economic Society, vol. 105(429),
pages 333-44, March.

[23] Brown,

A (2015),

“The Richest

person

in

every

state”,

Forbes,

http://www.forbes.com/richest-in-each-state/list/#tab:overall.

[24] Caselli, F (1999). “Technological Revolutions”, American Economic Review, 89, 78-102.

[25] Chetty, R., Hendren, N., Kline, P., and Saez, E (2014), “Where Is the Land of Oppor-
tunity? The Geography of Intergenerational Mobility in the United States”, Quarterly
Journal of Economics, 129, 1553-1623.

[26] Deaton, A (2013), The Great Escape: Health, Wealth, and the Origins of Inequality,

Princeton University Press

[27] Forbes, K (2000), “A Reassessment of the Relationship between Inequality and Growth”,

American Economic Review, 90, 869-887

[28] Frank, M (2009), “Inequality and Growth in the United States: Evidence From A New
State-Level Panel of Income Inequality Measures”, Economic Inquiry, 47, 55-68.

[29] Gabaix, X., and Landier, A (2008), “Why Has CEO Pay Increased So Much”, Quarterly

Journal of Economics, 123, 49-100

[30] Galor, O., and Moav, O (2000), “Ability-Biased Technological Transition, Wage In-
equality, and Economic Growth”, Quarterly Journal of Economics, 115, 469-497.

[31] Galor, O., and Zeira, J (1993), “Income Distribution and Macroeconomics”, Review of

Economic Studies, 60, 35-52

[32] Goldin, C., and Katz, L (2008), The Race Between Education and Technology, Harvard

University Press

[33] Guvenen, S, Kaplan and Song, J (2014), “How Risky Are Recessions for Top Earners?”

The American Economic Review, Papers & Proceedings, 104(5), 148-153.

[34] Hall, B., Jaﬀe, A., and Trajtenberg, M (2001), “The NBER Patent Citations Data File:
Lessons, Insights and Methodological Tools,” CEPR Discussion Papers 3094, C.E.P.R.
Discussion Papers.

[35] Hassler, J., and Rodriguez Mora, J (2000), “Intelligence, Social Mobility, and Growth”,

American Economic Review, 90, 888-908.

38

[36] H´emous, D., and Olsen, M (2014), “The Rise of the Machines: Automation, Horizontal
Innovation and Income Inequality”, CEPR Discussion Paper 10244, C.E.P.R. Discus-
sion Papers.

[37] Jones, C., and Kim, J (2014), “A Schumpeterian Model of Top Income Inequality”,

mimeo Stanford.

[38] Katz, L., and Murphy, K (1992), “Change in Relative Wages: Supply and Demand

Factors”, Quarterly Journal of Economics, 107, 35-78

[39] Kneer, C (2013), “The Absorption of Talent into Finance: Evidence from U.S. Banking
Deregulation,” DNB Working Papers 391, Netherlands Central Bank, Research Depart-
ment.

[40] Kortum, S., and Lerner, J. (1999), “What is behind the recent surge in patenting?”,

Research Policy, 28, 1-22.

[41] Krusell, P., Ohanian, L., Rios Rull, V., and Violante, G (2000), “Capital-Skill Comple-

mentarity and Inequality: A Macroeconomic Analysis”, Econometrica, 68, 1029-1053.

[42] Lai, R., D’Amour, A., Yu, A., Sun, Y., and Fleming, L (2013), “Disambiguation and

Co-authorship Networks of the U.S. Patent Inventor Database (1975 - 2010)”

[43] Moretti, E., and Wilson, D (2014), “State incentives for innovation, star scientists and
jobs: Evidence from biotech,” Journal of Urban Economics, vol. 79(C), pages 20-38.

[44] Philippon, T., and Reshef, A (2012), “Wages and Human Capital in the U.S. Finance
Industry: 1909-2006”, The Quarterly Journal of Economics, 127 (4): 1551-1609.

[45] Piketty, T (2003), “Income Inequality in France: 1901-1998”, Journal of Political

Economy, 111, 1004-1042

[46] Piketty, T (2014) Capital in the 21 st century, Harvard University Press.

[47] Piketty, T., and Saez, E (2003), “Income Inequality in the United States: 1913-1998”,

Quarterly Journal of Economics, 1, 1-39

[48] Piketty, T., Saez, E. and Stantcheva, S (2014), “Optimal Taxation of Top Labor In-
comes: A Tale of Three Elasticities”, American Economic Journal: Economic Policy,
6, 230-271.

[49] Rajan, R., and Zingales, L (1998), “Financial Dependence and Growth,” American
Economic Review, American Economic Association, vol. 88(3), pages 559-86, June.

[50] de Rassenfosse, G., Dernis, H., Guellec, D., Picci, L., and van Pottelsberghe de la
Potterie, B (2013), “The Worldwide Count of Priority Patents: A New Indicator of
Inventive Activity”, Research Policy, Elsevier, 38, 779-792.

39

[51] Rebelo, S (1991), “Long-Run Policy Analysis and Long-Run Growth,” Journal of Po-

litical Economy, 99 (3), 500-521.

[52] Romer, P (1990), “Endogenous Technical Change”, Journal of Political Economy, 98,

71-102.

[53] Rosen, S (1981), “The Economics of Superstars”, American Economic Review, 71, 845-

858.

[54] Toivanen, O., and Vaananen, L (2012), “Returns to Inventors”, Review of Economics

and Statistics, 94, 1173-1190.

[55] Toole, A (2007), “Does Public Scientiﬁc Research Complement Private Investment in
Research and Development in the Pharmaceutical Industry?”, Journal of Law and Eco-
nomics, 50, 81-104.

40

7 Tables

Variable Names

Description

top1
top10
Gini
G99
Theil
Atkin

Measure of inequality

Share of income own by the richest 1% (on a scale of 0 to 100).
Share of income own by the richest 10% (on a scale of 0 to 100).
Gini index of inequality.
Gini index restricted to the bottom 99% of income distribution.
Theil index of inequality.
Atkinson index of inequality.

Measure of innovation

patent pc
3 (resp 4 and 5) YWindow Total number of citation received no longer than 3 (resp 4 and 5)years after

Number of patents granted by the USPTO per thousand of people.

Share5

Citations
Renew

AM25

AM50

P5-i

P5

Gdppc
Popgrowth
Shareﬁnance
Outputgap
Gvtsize
Highways
Military
Spill Gdppc

Participation Rate
College per capita
School Expenditure
Employment Manuf

per thousand of inhabitant. application.
Total number of patent among the 5% most cited in a given application per
thousand of inhabitant. year.
Total number of citations made to patents per thousand of inhabitants.
Number of patents that have been renewed at least once per thousand of in-
habitants.

Measure of social mobility

Expected percentile of a child at 30 whose parents belonged to the 25th per-
centile of income distribution in 2000.
Expected percentile of a child at 30 whose parents belonged to the 50th per-
centile of income distribution in 2000.
Probability for a child at 30 to belong to the 5th quintile of income distribution
if parent belonged to the ith quintile, i ∈ {1, 2}.
Probability for a child at 30 to belong to the 5th quintile of income distribution
if parent belonged to lower quintiles.

Control variables

Real GDP per capita in US $ (in log).
Growth of total population.
GDP of ﬁnancial sector divided by total population (in log).
Output gap.
GDP of government sector divided by total population (in log).
Federal expenditure on highways divided by total population (in log).
GDP of public military sector divided by total population (in log).
Weighted value of other states GDP per capita at t-1 (in log).
Additional control variables at the CZ level
Labor Share participation rate.
College graduation rate.
Average expenditures per student in public schools (in log).
Share of employed persons 16 and older working in manufacturing.

Table 1: Description of relevant variables used in regressions. Additional variables may be used in speciﬁc
analysis, in this case they will be explained in the corresponding table description.

41

Measure of

Inequality
Innovation

Innovation

(1)
Top 1%
patent pc
0.021*
(2.00)

(2)
Top 1%
patent pc
0.026**
(2.06)

(3)
Top 1%
patent pc
0.028**
(2.03)

(4)
Top 1%
patent pc
0.027*
(1.89)

Gdppc

Popgrowth

Shareﬁnance

Outputgap

Gvtsize

R2
N

-0.101
(-1.29)

-0.060
(-0.52)

-0.071
(-1.16)

0.011
(0.01)

0.333
(0.43)

0.016
(0.72)

-1.986
(-1.35)

0.280
(0.37)

0.013
(0.57)

-1.954
(-1.37)

-0.070
(-0.76)

0.920
1785

0.919
1785

0.919
1785

0.920
1785

Table 2: Eﬀect of the number of patents per capita (in log and lagged) on the logarithm of the top 1%
income share. Time span: 1975-2010. Panel data OLS regressions. State-ﬁxed eﬀect and time dummies are
added but not reported. Variable description is given in Table 1. ∗ ∗ ∗pvalue < 0.01. ∗ ∗ pvalue < 0.05.
∗pvalue < 0.10 ; t/z statistics in brackets, computed with robust standard errors.

42

Measure of

Inequality
Innovation

Innovation

Gdppc

Popgrowth

Shareﬁnance

Outputgap

Gvtsize

R2
N

(2)
Top 1%

(1)
Top 1%

(4)
Top 1%
3YWindow 4YWindow 5YWindow Citations
0.048***
(5.78)

0.041***
(4.24)

0.032***
(3.72)

0.042***
(4.58)

(3)
Top 1 %

(5)

(6)

Top 1% Top 1%
Renew
Share5
0.025***
0.022***
(2.71)
(4.23)

-0.089
(-1.55)

0.138
(0.22)

0.022*
(1.67)

-1.826
(-1.27)

-0.068
(-1.21)

0.024
(0.04)

0.024*
(1.74)

-2.302
(-1.64)

-0.055
(-0.94)

-0.174
(-0.24)

0.026*
(1.76)

-2.143
(-1.46)

-0.091*
(-1.66)

-0.061
(-1.13)

-0.130*
(-1.90)

0.068
(0.10)

0.024*
(1.87)

-2.115
(-1.53)

0.028
(0.04)

0.021
(1.58)

0.984
(1.30)

0.015
(1.13)

-2.128
(-1.53)

-3.265*
(-1.95)

-0.085**
(-2.00)

-0.109**
(-2.51)

-0.139***
(-3.09)

-0.090**
(-2.16)

-0.099**
(-2.34)

-0.065
(-1.28)

0.921
1632

0.916
1581

0.908
1530

0.921
1632

0.921
1632

0.885
1435

Table 3: Eﬀect of diﬀerent measures of the quality of innovation (in log and lagged) on the logarithm of
the top 1% income share. Time span: 1975-2007 for column (1), 1975-2006 for column (2), 1975-2005 for
column (3), 1976-2007 for column (3), 1976-2007 for column (5) and 1982-2007 for column (6). Panel data
OLS regressions. State-ﬁxed eﬀect and time dummies are added but not reported. Variable description is
given in Table 1. ∗ ∗ ∗pvalue < 0.01. ∗ ∗ pvalue < 0.05. ∗pvalue < 0.10 ; t/z statistics in brackets, computed
with robust standard errors.

43

Measure of

Inequality
Innovation

Innovation

Gdppc

Popgrowth

Shareﬁnance

Outputgap

Gvtsize

Highways

Military

(1)
Top 1%
patent pc
0.166**
(2.12)

(2)
Top 1%
patent pc
0.183**
(2.04)

(3)
Top 1 %
patent pc
0.177**
(1.99)

-0.122
(-1.52)

-0.135
(-1.61)

-0.130
(-1.59)

0.728
(1.07)

0.022
(1.52)

0.778
(1.15)

0.024
(1.57)

0.758
(1.10)

0.023
(1.59)

-2.408*
(-1.70)

-2.451*
(-1.74)

-2.434*
(-1.68)

-0.100**
(-2.20)

-0.098**
(-2.12)

-0.099**
(-2.20)

(4)
Top 1%

(5)
Top 1%
3YWindow 3YWindow 3YWindow
0.139**
(2.32)

(6)
Top 1%

0.145**
(2.23)

0.160**
(2.01)

-0.153
(-1.63)

0.735
(0.99)

0.041**
(2.08)

-1.947
(-1.23)

-0.084
(-1.44)

-0.147*
(-1.76)

0.703
(0.97)

0.039**
(2.15)

-1.942
(-1.24)

-0.087
(-1.58)

-0.168*
(-1.67)

0.813
(1.03)

0.044**
(2.12)

-1.961
(-1.21)

-0.076
(-1.27)

0.028***
(3.15)

0.029***
(3.11)

0.029***
(2.98)

0.027***
(3.02)

0.026***
(3.09)

0.028***
(2.80)

0.008**
(2.03)

0.008**
(2.06)

Lag of instrument
R2
1st stage F-stat
N

2 years
0.913
27.10
1748

1 year
0.910
21.98
1748

0.008*
(1.95)

3 years
0.912
21.54
1748

0.011**
(2.43)

2 years
0.913
18.84
1598

0.010**
(2.44)

1 year
0.914
21.78
1598

0.011**
(2.28)

3 years
0.911
13.92
1598

Table 4: Eﬀect of two measures of the quality of innovation (in log and lagged) on the logarithm of the
top 1% income share. Time span: 1975-2010 for columns (1) to (3) and 1975-2007 for others. Panel data
IV (2 SLS) regressions with the number of seats occupied at the appropriation committee in the Senate as
an instrument for inovativeness. State-ﬁxed eﬀect and time dummies are added but not reported. Variable
description is given in Table 1. ∗ ∗ ∗pvalue < 0.01. ∗ ∗ pvalue < 0.05. ∗pvalue < 0.10 ; t/z statistics in
brackets, computed with robust standard errors.

44

Measure of

Inequality
Innovation

Innovation

(1)
Top 1%
patent pc
0.162**
(2.24)

(2)
Top 1%

(3)
Top 1 %

(4)
Top 1%

3YWindow 4YWindow 5YWindow Citations
0.201***
(2.81)

0.136***
(2.59)

0.147***
(2.69)

0.124**
(2.53)

(5)

(6)

Top 1% Top 1%
Share5
0.297**
(2.14)

Gdppc

Popgrowth

Shareﬁnance

Outputgap

Gvtsize

Spill Gdppc

R2
1st stage F-stat
N

-0.169*
(-1.80)

-0.206**
(-2.00)

0.773
(1.12)

0.026*
(1.82)

-2.427*
(-1.68)

-0.038
(-0.79)

0.050
(0.11)

0.909
20.93
1785

0.653
(0.92)

0.043**
(2.46)

-2.000
(-1.27)

-0.015
(-0.24)

0.307
(0.61)

0.911
25.49
1632

-0.176*
(-1.79)

0.480
(0.67)

0.043**
(2.39)

-2.738*
(-1.78)

-0.035
(-0.54)

0.436
(0.86)

0.907
23.78
1581

-0.184*
(-1.74)

-0.245**
(-2.23)

-0.280*
(-1.80)

0.365
(0.46)

0.285
(0.42)

0.812
(0.74)

0.050**
(2.49)

0.054***
(2.74)

0.092**
(2.21)

-2.265
(-1.44)

-0.058
(-0.84)

0.413
(0.83)

0.897
22.63
1530

-2.105
(-1.47)

-0.032
(-0.55)

0.092
(0.20)

0.903
18.11
1632

-2.772
(-1.31)

0.007
(0.08)

0.356
(0.45)

0.740
4.93
1559

Table 5: Eﬀect of diﬀerent measures of the quality of innovation (in log and lagged) on the logarithm of the
top 1% income share. Time span: 1976-2010 for column (1), 1976-2007 for column (2), 1976-2006 for column
(6), 1976-2005 for column (4), 1976-2007 for column (5) and 1976-2007 for column (6). Panel data IV (2
SLS) regressions with the the spillover at time t-1 used as an instrument for inovativeness. States-ﬁxed eﬀect
and time dummies are added but not reported. Variable description is given in Table 1. ∗ ∗ ∗pvalue < 0.01.
∗ ∗ pvalue < 0.05. ∗pvalue < 0.10 ; t/z statistics in brackets, computed with robust standard errors.

45

Measure of

Inequality
Innovation

Innovation

Gdppc

Popgrowth

Shareﬁnance

Outputgap

Gvtsize

Highways

Military

Spill Gdppc

R2
1st stage F-stat
N

-0.148*
(-1.74)

0.121
(0.18)

0.039**
(2.50)

-2.065
(-1.46)

-0.124**
(-2.49)

0.028***
(3.14)

0.011***
(2.75)

0.153
(0.35)

0.914
25.58
1598

(3)

(1)
Top 1%

(2)
Avgtop
3YWindow 3YWindow 3YWindow
-0.037*
(-1.81)

Top 10 % Overall Gini
3YWindow
-0.003
(-0.21)

0.168***
(3.65)

0.014
(1.12)

(4)

(5)
G99

(6)
Atkin
3YWindow 3YWindow 3YWindow
0.025
(1.39)

-0.021
(-1.43)

0.012
(0.34)

(7)
Theil

0.086***
(2.70)

0.054**
(2.33)

-0.041*
(-1.81)

-0.055**
(-2.14)

0.125***
(3.66)

0.400***
(5.80)

-0.454**
(-1.97)

-0.008
(-1.05)

-0.616
(-1.35)

-0.034
(-1.42)

-0.006
(-1.56)

-0.002
(-1.24)

-0.037
(-0.23)

0.006
(1.17)

-0.482
(-1.46)

-0.439***
(-2.77)

-0.641***
(-3.59)

0.220
(0.87)

2.136***
(3.91)

-0.000
(-0.01)

-0.012
(-0.03)

-0.008
(-1.28)

0.003
(0.01)

0.018**
(2.07)

0.102
(0.18)

-0.000
(-0.02)

0.130
(0.12)

-0.077***
(-4.59)

0.035**
(2.03)

0.073***
(3.53)

-0.119***
(-4.65)

-0.289***
(-5.83)

0.004
(1.45)

0.002
(1.44)

0.009***
(3.18)

0.010***
(3.06)

-0.001
(-0.88)

-0.002
(-1.53)

0.810***
(4.37)

0.388***
(2.75)

0.704***
(4.98)

0.881***
(5.59)

0.544
25.58
1598

0.950
25.58
1598

0.884
25.58
1598

0.758
25.58
1598

0.003
(0.61)

0.000
(0.23)

0.268
(1.33)

0.930
25.58
1598

-0.002
(-0.23)

0.003
(0.95)

-0.250
(-0.62)

0.927
25.58
1598

Table 6: Eﬀect of the 3 year window citation number (in log and lagged) on the logarithm of diﬀerent
measures of inequality. Column (1) uses the top 1% income share, column (2) uses the average percentile
between 2 and 10, column (3) uses the top 10% income share, column (4) uses the overall Gini coeﬃcient
and column (5) the bottom 99% Gini coeﬃcient. Time span: 1975-2007. Panel data IV regressions with
both instruments (spillover and appropriation committee composition). State-ﬁxed eﬀect and time dummies
are added but not reported. Variable description is given in Table 1. ∗ ∗ ∗pvalue < 0.01. ∗ ∗ pvalue < 0.05.
∗pvalue < 0.10 ; t/z statistics in brackets, computed with robust standard errors.

46

Measure of

Inequality
Innovation

Lag of innovativeness

Innovation

(1)
top 1%
patent pc
1 year
0.184***
(3.37)

(2)
top1%
patent pc
2 years
0.194***
(3.00)

(3)
top 1%
patent pc
3 years
0.216***
(3.10)

(4)
top1%
patent pc
4 years
0.207***
(2.97)

(5)
top 1%
patent pc
5 years
0.199***
(2.91)

(6)
top1%
patent pc
Average 3 year
0.032***
(2.05)

Gdppc

Popgrowth

Shareﬁnance

Outputgap

Gvtsize

Highways

Military

Spill Gdppc

R2
1st stage F-stat
N

-0.143*
(-1.81)

-0.160*
(-1.92)

-0.202**
(-2.44)

-0.226***
(-2.60)

-0.245***
(-2.67)

-0.189*
(-1.93)

0.792
(1.16)

0.024*
(1.70)

0.908
(1.18)

0.027*
(1.86)

1.121
(1.39)

0.030*
(1.94)

1.396
(1.64)

0.028*
(1.78)

1.839**
(2.09)

0.024
(1.53)

-2.520*
(-1.76)

-2.740*
(-1.78)

-3.025**
(-2.03)

-3.708**
(-2.32)

-4.507***
(-2.70)

-0.094**
(-2.00)

-0.064
(-1.30)

-0.029
(-0.53)

0.029***
(3.33)

0.025***
(2.67)

0.023**
(2.44)

-0.009
(-0.16)

0.017*
(1.75)

0.009**
(2.08)

0.009**
(2.20)

0.010**
(2.28)

0.009**
(2.06)

0.220
(0.48)

0.910
25.48
1748

-0.039
(-0.09)

-0.018
(-0.04)

0.902
20.59
1698

0.891
18.12
1648

0.057
(0.11)

0.883
17.59
1598

-0.011
(-0.19)

0.015
(1.63)

0.007
(1.50)

0.199
(0.38)

0.872
20.10
1548

0.060
(0.07)

0.027
(1.38)

-0.791
(-0.27)

0.011
(0.16)

0.918
-
561

Table 7: Eﬀect of innovation (in log) at diﬀerent lags on the logarithm of the top 1% income share. Panel
data IV (2 SLS) regressions with both instrument (appropriation and spillover) for column 1 to 6 and OLS
for column 7. State ﬁxed eﬀects and time dummies are added but not reported. Variable description is given
in Table 1. ∗ ∗ ∗pvalue < 0.01. ∗ ∗ pvalue < 0.05. ∗pvalue < 0.10 ; t/z statistics in brackets, computed with
robust standard errors.

47

Measure of

Inequality
Innovation

Innovation

Gdppc

Popgrowth

Shareﬁnance

Outputgap

Gvtsize

Highways

Military

Spill Gdppc

RemunFinance

EFD

Oil

NaturalRessource

MarginalTax

(2)
(1)
Top 1%
Top 1%
Citations Citations
0.175***
0.187***
(3.46)
(3.84)

(5)
(4)
(3)
Top 1%
Top 1%
Top 1 %
patent pc Citations Citations
0.158***
0.202***
0.185***
(3.70)
(3.33)
(3.36)

(7)
(6)
Top 1%
Top 1%
patent pc Citations
0.202***
0.184***
(3.94)
(3.37)

-0.143
(-1.57)
0.310
(0.42)
0.028*
(1.79)
-2.177
(-1.48)
-0.138***
(-2.72)

0.023***
(2.65)
0.009**
(2.33)
-0.105
(-0.23)

-0.143*
(-1.81)
0.789
(1.15)
0.024*
(1.72)
-2.513*
(-1.75)
-0.095**
(-2.03)

0.029***
(3.32)
0.009**
(2.09)
0.224
(0.49)

-0.172*
(-1.93)
0.091
(0.13)
0.039**
(2.54)
-2.102
(-1.47)
-0.119**
(-2.35)

0.029***
(3.20)
0.012***
(2.89)
0.072
(0.17)

0.042
(1.05)

-0.146*
(-1.79)
0.031
(0.05)
0.043***
(2.58)
-1.870
(-1.33)
-0.143***
(-2.84)

0.029***
(3.08)
0.013***
(2.97)
0.181
(0.41)

-0.430
(-1.50)

-0.113
(-1.59)
0.345
(0.53)
0.034**
(2.29)
-2.961**
(-2.01)
-0.098**
(-1.97)

0.022***
(2.65)
0.011***
(2.82)
0.184
(0.41)

-0.130*
(-1.68)
0.809
(1.18)
0.022
(1.60)
-2.623*
(-1.79)
-0.105**
(-2.12)

0.029***
(3.34)
0.009**
(2.13)
0.284
(0.60)

-0.185**
(-2.09)
0.191
(0.27)
0.038**
(2.40)
-2.650*
(-1.76)
-0.112**
(-2.12)

0.027***
(2.94)
0.013***
(3.02)
0.507
(1.02)

1.768***
(3.81)
-0.029***
(-4.05)

-0.100
(-0.36)

0.009***
(2.70)

R2
1st stage F-stat
N

0.911
23.15
1598

0.916
19.32
1470

0.886
25.11
1748

0.908
17.00
1598

0.919
23.87
1598

0.910
26.34
1748

0.904
21.57
1548

Table 8: Eﬀect of various measures of innovation (in log and lagged) on the logarithm of the top 1% income
share. In column (2), NY, CT, DE and SD are dropped from the dataset, in column (3), ﬁnance-related
patents have been removed and in column (6), oil-related patent have been removed. Time Span: 1975-2010
for columns (3) and (6), 1975-2007 for others. Panel data IV (2 SLS) regressions with both instrument
(appropriation and spillover). State-ﬁxed eﬀect and time dummies are added but not reported. Variable
Oil and NaturalRessource measures the share of oil related and natural ressource extractions activities in
GDP, variable RemunFinance measures the average compensation per employee in the ﬁnancial sector,
variable EFD measures the ﬁnancial dependence of innovation and variable MarginalTax measures the
highest marginal tax rate of labor. Other variables are described in Table 1. ∗ ∗ ∗pvalue < 0.01. ∗ ∗ pvalue <
0.05. ∗pvalue < 0.10 ; t/z statistics in brackets, computed with robust standard errors.

48

Measure of

Inequality
Innovation

Innovation

Gdppc

Popgrowth

Shareﬁnance

Outputgap

Gvtsize

Highways

Military

Spill Gdppc

Size of sector

(1)
Top 1%
patent pc
0.308***
(3.02)

(2)
Top 1%
patent pc
0.181***
(3.36)

(3)
Top 1%
patent pc
0.186***
(3.36)

(4)
Top 1 %
patent pc
0.196***
(3.25)

-0.094
(-1.28)
0.409
(0.63)
-0.003
(-0.21)
-2.250
(-1.58)
-0.082
(-1.56)

0.026***
(2.81)
0.015***
(2.66)
0.600
(1.06)

-0.139*
(-1.78)
0.780
(1.14)
0.024*
(1.74)
-2.501*
(-1.74)
-0.096**
(-2.04)

0.029***
(3.35)
0.009**
(2.06)
0.216
(0.47)

-0.145*
(-1.82)
0.798
(1.16)
0.024*
(1.72)
-2.468*
(-1.72)
-0.097**
(-2.08)

0.029***
(3.35)
0.009**
(2.11)
0.181
(0.40)

(5)
Top 1%
patent pc
0.251***
(3.07)

-0.048
(-0.73)
-0.033
(-0.05)
0.020
(1.36)
-1.698
(-1.25)
-0.163***
(-3.04)

0.026***
(2.84)
0.013**
(2.54)
0.123
(0.25)

(6)
Top 1%
patent pc
0.168***
(3.35)

-0.158*
(-1.88)
0.873
(1.26)
0.025*
(1.75)
-2.719*
(-1.83)
-0.082*
(-1.72)

0.029***
(3.35)
0.008**
(1.97)
0.386
(0.78)

0.898
15.30
1748

0.908
24.25
1748

-0.167**
(-2.07)
0.657
(0.94)
0.012
(0.84)
-2.210
(-1.52)
-0.092*
(-1.94)

0.029***
(3.35)
0.010**
(2.34)
-0.369
(-0.77)

0.016
(0.84)
0.052***
(2.63)
-0.020*
(-1.66)

0.910
21.47
1748

Computer and Electronic Products

Chemistry

Electrical equipment

R2
1st stage F-stat
N

0.895
14.55
1748

0.910
25.84
1748

0.910
24.88
1748

Table 9: Eﬀect of the number of patents per capita in some speciﬁc sectors (in log and lagged) on the
logarithm of the top 1% income share. Column (1) excludes patents from the computer sectors (NAICS:
334), column (2) excludes patents from the pharmacetical sectors (NAICS: 3254) and column (3) excludes
patents from the electrical equipment sectors (NAICS: 335). Columns (5) focus on patents from three highly
exporting sectors: Transportation, Machinery and Electrical Machinery while column (6) excludes these
sectors. The size of a sector (see column (4)) is deﬁned as the gdp per capita from the corresponding sector.
Panel data IV (2 SLS) regressions with both instrument (appropriation and spillover). Time span: 1975-
2010. Variable description is given in Table 1. ∗ ∗ ∗pvalue < 0.01. ∗ ∗ pvalue < 0.05. ∗pvalue < 0.10 ; t/z
statistics in brackets, computed with robust standard errors.

49

Measure of

Inequality

Number of star inventors

Gdppc

Popgrowth

Shareﬁnance

Outputgap

Gvtsize

Highways

Military

Spill Gdppc

R2
1st stage F-stat
N

(1)

(2)

(3)

(4)

(5)

(6)

Top 1% Top 1% Top 1% Top 1% Top 1% Top 1%
0.174***
0.101**
(3.17)
(2.04)

0.129***
(3.22)

0.188**
(2.14)

0.132**
(2.06)

0.129**
(2.18)

-0.093
(-1.14)

-0.187*
(-1.67)

-0.137
(-1.53)

-0.091
(-1.11)

-0.215*
(-1.71)

-0.145
(-1.54)

-0.111
(-0.16)

-0.026
(-0.04)

-0.141
(-0.20)

-0.203
(-0.28)

-0.057
(-0.08)

-0.254
(-0.35)

0.037**
(2.03)

0.052**
(2.48)

0.045***
(2.67)

0.047**
(2.12)

0.070**
(2.44)

0.059***
(2.88)

-2.103
(-1.49)

-2.245
(-1.55)

-2.197
(-1.51)

-2.237
(-1.58)

-2.554*
(-1.68)

-2.430
(-1.64)

-0.127**
(-2.46)

-0.035
(-0.53)

-0.107*
(-1.95)

-0.123**
(-2.27)

-0.003
(-0.03)

-0.097*
(-1.65)

0.030***
(3.15)

0.008**
(2.08)

0.917
24.39
1648

0.033***
(3.40)

0.031***
(3.08)

0.009**
(2.19)

0.009**
(2.12)

0.218
(0.44)

0.905
17.22
1683

0.314
(0.65)

0.909
19.96
1648

0.404
(0.71)

0.893
13.76
1683

0.914
18.79
1648

0.034***
(3.31)

0.011**
(2.28)

0.487
(0.93)

0.902
15.69
1648

Table 10: Eﬀect of the number of top scientists per capita (in log and lagged) on the logarithm of the
top 1% income shares. Time span: 1975-2007. Panel data IV (2 SLS) regressions with the number of
senators on the Appropriation Committee used as an instrument in columns (1) and (4), the spillover on
the number of patent per capita in columns (2) and (5) and the two instruments jointly in columns (3) and
(6). States-ﬁxed eﬀect and time dummies are added but not reported. Variable description is given in Table
1. ∗ ∗ ∗pvalue < 0.01. ∗ ∗ pvalue < 0.05. ∗pvalue < 0.10 ; t/z statistics in brackets, computed with robust
standard errors.

50

Measure of

Inequality
Innovation

Innovation

Gdppc

Popgrowth

Gvtsize

Participation Rate

School Expenditure

College per capita

Employment Manuf

(1)
Top 1%
patent pc
0.047**
(2.13)

(2)
Top 1%
patent pc
0.053**
(2.46)

(3)
Gini
patent pc
-0.002
(-0.17)

(4)
Gini
patent pc
0.022*
(1.69)

(5)
G99
patent pc
-0.018
(-1.22)

(6)
G99
patent pc
0.009
(0.68)

0.475**
(2.68)

0.716***
(4.11)

-0.041
(-0.35)

0.280***
(3.16)

-0.279**
(-2.25)

-1.139*
(-1.99)

-0.002**
(-2.13)

-0.490
(-1.22)

-0.001
(-0.63)

-0.648**
(-2.01)

-0.001*
(-1.87)

-0.221
(-0.60)

-0.000
(-0.11)

0.107
(0.21)

-0.001
(-1.44)

-1.508***
(-6.82)

-0.232**
(-2.57)

-0.108*
(-1.82)

-0.350**
(-2.03)

-0.912***
(-2.79)

-0.239*
(-1.92)

-0.187*
(-1.69)

-0.262
(-1.07)

0.189
560

0.115
(1.40)

-0.096
(-0.25)

0.000
(0.09)

-1.735***
(-7.16)

-0.247***
(-2.77)

-0.055
(-1.05)

-0.365**
(-2.10)

R2
N

0.173
660

0.034
670

0.228
560

0.101
660

0.335
560

Table 11: Eﬀect of innovativeness on various measures of inequality at the commuting zone level. The
measure of innovation is the log of the average number of granted patents per capita whose ﬁled between
1992 and 1996. Columns (1) and (2) use the size of the top 1% income share group as a measure of inequality,
columns (3) and (4) use the Gini index and columns (5) and (6) use the Gini index for the bottom 99%.
Columns (2), (4) and (6) add additional controls. All inequalities measure are computed over the period
1996-2000. Cross sectional OLS regressions. Variable description is given in Table 1. ∗ ∗ ∗pvalue < 0.01.
∗ ∗ pvalue < 0.05. ∗pvalue < 0.10 ; t/z statistics in brackets, computed with robust standard errors.

51

Measure of
Mobility
Innovation

Innovation

Gdppc

Popgrowth

Gvtsize

(1)
AM25
patent pc
0.024***
(3.07)

(2)
P1-5
patent pc
0.108***
(3.13)

(3)
P2-5
patent pc
0.063***
(2.70)

(4)
AM25
patent pc
0.019**
(2.40)

(5)
P1-5
patent pc
0.073**
(2.10)

(6)
P2-5
patent pc
0.046*
(1.76)

(7)
P5
patent pc
0.022
(1.17)

-0.094*
(-1.81)

-0.225
(-1.09)

-0.204
(-1.48)

-0.139***
(-3.33)

-0.384*
(-1.84)

-0.356**
(-2.39)

-0.271**
(-2.31)

0.177
(0.61)

0.000
(1.43)

0.603
(0.55)

0.002
(1.30)

0.711
(0.87)

0.001
(0.84)

0.236
(0.76)

0.000
(0.06)

0.588
(0.48)

-0.000
(-0.19)

0.731
(0.84)

-0.001
(-0.77)

0.611
(0.89)

-0.000
(-0.37)

Participation Rate

0.600***
(3.76)

1.356**
(2.19)

1.274**
(2.45)

0.726***
(4.50)

2.067***
(3.22)

1.692***
(3.14)

1.087**
(2.55)

School Expenditure

0.116**
(2.07)

0.550**
(2.65)

0.349**
(2.20)

College per capita

Employment Manuf

0.096*
(1.81)

0.081
(1.52)

0.417**
(2.05)

0.075
(0.35)

0.298*
(1.91)

0.081
(0.49)

0.153
(1.36)

0.119
(0.98)

-0.333***
(-3.43)

-1.566***
(-4.27)

-1.273***
(-4.18)

-0.677***
(-2.86)

R2
N

0.201
637

0.182
645

0.163
645

0.243
546

0.215
546

0.211
546

0.160
546

Table 12: Eﬀect of innovativeness on social mobility at the commuting zone level. Columns (1) and (4) test
the eﬀect of the number of patents per capita on absolute upward mobility when the parent percentile is set
to 25. Columns (2), (3), (5) and (6) test the eﬀect of the number of patents per capita on the probability
for a child at 30 to reach the 5th quintile in global income distribution if parents belonged to quintile 1 for
columns (2) and (5) and 2 for columns (4) and (6), 3 for column (5) and 4 for column (6). Column (7)
tests the eﬀect of the log number of patents per capita on the overall probability to reach the 5th quintile in
global income distribution if parents belonged to any lower quintile. Cross-Section OLS regressions. Variable
description is given in Table 1. ∗ ∗ ∗pvalue < 0.01. ∗ ∗ pvalue < 0.05. ∗pvalue < 0.10 ; t/z statistics in
brackets, computed with robust standard errors.

52

Measure of
Mobility
Innovation

Innovation from Entrants

(1)
AM25
patent pc
0.016**
(2.61)

(2)
P1-5
patent pc
0.058**
(2.39)

(3)
P2-5
patent pc
0.038**
(2.11)

(4)
AM25
patent pc

(5)
P1-5
patent pc

(6)
P2-5
patent pc

(7)
AM25
patent pc
0.018**
(2.61)

Innovation from Incumbent

0.007
(0.87)

0.032
(0.97)

0.020
(0.75)

-0.006
(-0.64)

Gdppc

Popgrowth

Gvtsize

-0.136***
(-3.08)

-0.381*
(-1.78)

-0.330**
(-2.11)

-0.136***
(-2.96)

-0.405*
(-1.87)

-0.340**
(-2.14)

-0.128***
(-2.83)

0.287
(1.00)

0.000
(0.04)

0.757
(0.66)

-0.000
(-0.22)

0.827
(0.98)

-0.001
(-0.80)

0.272
(0.92)

0.000
(0.08)

0.708
(0.61)

-0.000
(-0.21)

0.792
(0.93)

-0.001
(-0.76)

0.290
(1.02)

0.000
(0.07)

Participation Rate

0.785***
(4.61)

2.291***
(3.44)

1.815***
(3.25)

0.758***
(4.48)

2.180***
(3.30)

1.743***
(3.14)

0.799***
(4.71)

School Expenditure

College per capita

0.109**
(2.09)

0.467**
(2.38)

0.322**
(2.04)

0.081*
(1.70)

0.068
(0.36)

0.090
(0.57)

0.102*
(1.95)

0.075
(1.57)

0.442**
(2.24)

0.036
(0.19)

0.306*
(1.95)

0.071
(0.44)

0.111**
(2.10)

0.084*
(1.81)

Employment Manuf

-0.312***
(-3.16)

-1.508***
(-4.12)

-1.212***
(-3.95)

-0.366***
(-3.70)

-1.705***
(-4.54)

-1.341***
(-4.34)

-0.307***
(-3.04)

R2
N

0.260
541

0.233
541

0.221
541

0.243
541

0.217
541

0.209
541

0.261
541

Table 13: Eﬀect of innovativeness on social mobility at the commuting zone level. Columns (1) and (4)
test the eﬀect of the number of patents per capita on absolute upward mobility when the parent percentile
is set to 25. Columns (2) and (5) (resp (4) and (6)) test the eﬀect of the number of patents per capita on
the probability for a child at 30 to reach the 5th quintile in global income distribution if parents belonged
to quintile 1 (resp 2). Columns (1) to (3) focus on “entrant patents” while columns (4) to (6) focus on
“incumbent patents” and column (7) add the two kinds of innovation in a horse race regression. Cross-
Section OLS regressions. Variable description is given in Table 1. ∗ ∗ ∗pvalue < 0.01. ∗ ∗ pvalue < 0.05.
∗pvalue < 0.10 ; t/z statistics in brackets, computed with robust standard errors.

53

Measure of

Inequality
Innovation

Innovation from Entrants

(2)
top 1%
patent pc

(1)
top 1%
patent pc
0.032***
(2.97)

(3)
top 1%

(4)
top 1%

(6)
top 1%
patent pc Citations Citations Citations
0.017**
0.030***
(2.44)
(2.69)

0.018***
(2.74)

(5)
top 1%

Innovation from Incumbents

0.017**
(2.32)

0.014*
(1.83)

0.014**
(2.33)

0.012*
(1.94)

Gdppc

Popgrowth

Shareﬁnance

Outputgap

Gvtsize

R2
N

-0.140**
(-2.35)

-0.134**
(-2.32)

-0.158**
(-2.57)

-0.115*
(-1.85)

-0.119**
(-1.97)

-0.128**
(-2.03)

0.797
(1.18)

0.006
(0.49)

0.817
(1.21)

0.015
(1.14)

0.945
(1.41)

0.007
(0.53)

0.394
(0.54)

0.017
(1.25)

0.437
(0.59)

0.017
(1.24)

0.386
(0.53)

0.018
(1.34)

-3.732**
(-2.36)

-3.802**
(-2.49)

-3.863**
(-2.46)

-3.829**
(-2.45)

-3.827**
(-2.40)

-3.772**
(-2.38)

-0.012
(-0.26)

0.907
1581

-0.013
(-0.29)

0.907
1581

0.008
(0.18)

0.908
1581

-0.059
(-1.20)

-0.071
(-1.49)

-0.062
(-1.32)

0.903
1377

0.903
1377

0.904
1377

Table 14: Eﬀect of innovativeness (in log and lagged) on inequality measured by the logarithm of the share
of income held by the richest 1%. Columns (1) and (4) restrict the sample on entrant patents, columns (2)
and (5) focus on incumbent patents and columns (3) and (6) use both innovation in a horse race. Time Span:
1979-2009 for columns (1), (2) and (3), 1981-2006 for others. Panel data OLS regressions. States ﬁxed eﬀect
and time dummmies are added but not reported. Variable descriptions are given in table 1.∗∗∗pvalue < 0.01.
∗ ∗ pvalue < 0.05. ∗pvalue < 0.10 ; t/z statistics in brackets, computed with robust standard errors.

54

Measure of

Inequality
Mobility
Innovation

Innovation

from Entrants

from Incumbents

Lobbying*Innovation

-0.060***
(-9.48)

from Entrants

from Incumbents

-0.093*
(-1.65)
0.445
(0.71)
0.016
(1.21)
-1.930
(-1.36)
0.008
(0.19)

Gdppc

Popgrowth

Shareﬁnance

Outputgap

Gvtsize

Highways

Military

Spill Gdppc

(1)
top 1%
-

(2)
top1%
-

(3)
top 1%
-

(4)
-
AM25

3YWindow 3YWindow 3YWindow patent pc

(5)
-
AM25
patent pc

(6)
-
AM25
patent pc

(7)
-
AM25
patent pc

0.059***
(6.06)

0.153***
(3.81)

0.020***
(3.71)
0.012*
(1.87)

-0.034***
(-6.79)
-0.004
(-0.65)

-0.071
(-1.33)
0.097
(0.15)
0.009
(0.64)
-2.201
(-1.61)
-0.044
(-1.04)

0.012
(1.28)

0.028***
(2.72)

0.005
(0.73)

0.014
(1.46)

0.044
(1.66)
0.002
(1.47)
0.000
(0.15)

0.030
(0.94)
0.000
(0.16)
-0.003***
(-2.82)

0.046
(1.68)
0.003
(1.64)
0.000
(0.40)

0.028
(0.81)
0.000
(0.16)
-0.003**
(-2.19)

-0.001
(-0.41)

0.001
(0.78)

-0.001
(-0.47)

0.001
(0.86)

0.107
-
176

0.079
-
176

0.100
-
176

0.049
-
176

-0.074***
(-10.01)

-0.200**
(-2.20)
1.229*
(1.72)
0.024
(1.58)
-2.550
(-1.57)
0.064
(1.12)
0.032***
(3.80)
0.005
(0.99)
0.983**
(2.01)

0.922
11.79
1598

R2
1st stage F-stat
N

0.925
-
1632

0.925
-
1632

Table 15: Eﬀect of innovativeness (in log and lagged) on inequality and social mobility, breakdown using
lobbying intensity and origin of innovation. Column (1) presents results from an OLS regression at the cross
state level for every patent citations while Column (2) uses entrant patents and incumbent separately (in
a OLS horse-race regression). Column (3) uses the measure of spillover as an instrument variable. Panel
regressions with a time span of 1975-2006, 1979-2006 and 1979-2006. Time dummies and states ﬁxed eﬀect
are added but not reported. Columns (4) to (7) present results from an OLS regression at the cross-MSA
level with robust standard errors clustered at the state level. Columns (4) and (6) restrict the sample to MSA
that are above median in terms of lobbying activity, columns (5) and (7) focus on MSA below this median.
Lobbying*Innovation stands for the interacting terms between innovativeness and a dummy for being above
median in terms of lobbying activities, other Variable description is given in Table 1. ∗ ∗ ∗pvalue < 0.01.
∗ ∗ pvalue < 0.05. ∗pvalue < 0.10 ; t/z statistics in brackets, computed with robust standard errors.

55

8 Appendix

8.1 Proofs for Section 2.2.3

From (11), we have:

whereas:

∂ ˜x∗
∂ηL

= −

1
η2
L

1
θI

< 0,

(cid:16)

−

∂x∗
∂ηL

= (1 − z)

[(1 − 2˜x∗)

(cid:16)

θE − (1 − z)2 (cid:16) 1
˜x∗(cid:17)
(1 − ˜x∗) − 1
ηH
θE − (1 − z)2 (cid:16) 1

ηL

− 1
ηH

ηL

πH − 1
ηL
(cid:16)

η2
L

(cid:17)(cid:17)

− 1
ηH
(1 − z)2]
(cid:17)(cid:17)2

,

the sign of which is ambiguous—intuitively a higher ηL decreases incumbent’s rate which
increases wages but also has a direct negative impact on wages and higher wages in turn
lower entrant innovation.

However, when θE = θI, the overall eﬀect of a higher ηL on the aggregate innovation rate

is negative; more formally:

∂ ˜x∗
∂ηL
1
η2
L

= −

+

1
θ

∂x∗
∂ηL

+

− (1 − z)

(1 − z) (1 − ˜x∗)

(cid:16)

η2
L
˜x∗ (cid:16)

θ − (1 − z)2 (cid:16) 1
θ − (1 − z)2 (cid:16) 1

ηL

ηL

(cid:17)(cid:17)

− 1
ηH

(cid:17)(cid:17)

(cid:16)

− 1
ηH
(cid:16)

πH − 1
+
ηL
θ − (1 − z)2 (cid:16) 1

η2
L

(cid:17)(cid:17)2

− 1
ηH

ηL

(1 − ˜x∗) − 1
ηH

˜x∗(cid:17)

(1 − z)2

1

= −

(cid:16)

η2
L

θ − (1 − z)2 (cid:16) 1
(cid:16)

ηL

(cid:17)(cid:17)

− 1
ηH

z
θ

θ + (1 − z)
(cid:17)(cid:17)

˜x∗(cid:16)

θ−(1−z)2(cid:16) 1
ηL

(cid:17)(cid:17)

(cid:16) 1
− 1
ηL
ηH
(cid:16)
πH − 1
ηL
− 1
ηH

− 1
+
ηH
θ−(1−z)2(cid:16) 1
(cid:16)
ηL

(1−˜x∗)− 1
ηH

(cid:17)(cid:17)






˜x∗(cid:17)

(1−z)2

+ (1 − z)






< 0.

Overall, we therefore have:

∂entrepreneur sharet
∂ηL

=

1
η2
L

(1 − (1 − z) x∗ − ˜x∗) +

(cid:18) 1
ηL

−

1
ηH

(cid:19) ∂
∂ηL

((1 − z) x∗ + ˜x∗) ,

where the second term is dominated by the ﬁrst term for θ large enough.

56

8.2 First stage and reduced form from the IV regressions

In Table 16, we present outputs from the reduced form (when direclty regressing our instru-
ments on the logarithm of the top 1% income share) and the ﬁrst stage regressions. Columns
1 and 2 use our two instruments jointly, columns 3 and 4 use only the spillover instrument
and columns 5 and 6 use the senate appropriation committee based instrument.

Measure of

Inequality
Innovation

Appropriation Committee

(1)
top 1%

0.012**
(2.17)

(2)
-
patent pc
0.077***
(5.33)

(3)
top 1%

(4)
-
patent pc

(5)
top 1%

0.011**
(2.13)

(6)
-
patent pc
0.076***
(5.27)

Spillover

Gdppc

Popgrowth

Shareﬁnance

Outputgap

Gvtsize

Highways

Military

Spill Gdppc

0.209***
(2.84)

1.089***
(4.77)

0.174**
(2.44)

1.098***
(4.63)

-0.016
(-0.27)

0.653***
(4.97)

-0.050
(-0.86)

0.647***
(5.35)

0.021
(0.41)

0.281
(0.43)

0.003
(0.22)

0.789***
(6.33)

-2.952**
(-2.09)

-0.124***
(-3.24)

-1.952
(-1.45)

2.691
(1.18)

-2.759**
(-2.11)

-0.048
(-1.36)

2.845
(1.29)

-0.028
(-0.20)

-0.137***
(-3.18)

-0.116
(-0.87)

0.019***
(2.70)

-0.059***
(-3.23)

0.005
(1.48)

-0.013**
(-2.22)

0.400
(0.67)

0.019
(1.55)

-2.007
(-1.49)

-0.060
(-1.37)

0.495
(0.75)

0.013
(0.99)

-2.136
(-1.56)

-0.094**
(-2.01)

-1.978
(-1.41)

-0.071**
(-1.97)

2.182
(0.96)

0.082
(0.58)

0.022***
(3.05)

-0.039**
(-2.12)

0.005
(1.35)

0.129
(0.31)

-0.018***
(-3.02)

-0.785
(-0.73)

0.029
(0.07)

-0.303
(-0.29)

N

1798

1748

1836

1785

1798

1748

Table 16: Results from the reduced form equation (columns 1, 3 and 5) and the ﬁrst stage regressions
(columns 2, 4 and 6) when the number of patent per capita (in log and lagged) is used as a Measure of
innovation. Panel OLS regressions. Variable description is given in table 1.∗ ∗ ∗pvalue < 0.01. ∗ ∗ pvalue <
0.05. ∗pvalue < 0.10 ; t/z statistics in brackets, computed with robust standard errors.

57

