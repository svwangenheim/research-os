Growth through Heterogeneous Innovations

Source PDF: Akcigit_Kerr_2018_Growth through heteregeneous innovations.pdf

Converted from the local PDF after source-fidelity spot-check on 2026-05-04.




<!-- page 1 -->


Growth through Heterogeneous Innovations 
Ufuk Akcigit
University of Chicago, NBER, and CEPRWilliam R. Kerr
Harvard University and NBER
First Draft: October 27, 2010
This Draft: April 4, 2017
Abstract
We build a tractable growth model where multi-product incumbents invest in internal inno-
vations to improve their existing products, while new entrants and incumbents invest in external
innovations to acquire new product lines. External and internal innovations generate heteroge-
neous innovation qualities, and  rm size a ects innovation incentives. This framework allows
us to analyze how di erent types of innovation contribute to economic growth and how the
 rm size distribution can have important consequences for the types of innovations realized.
Our model aligns with many observed empirical regularities, and we quantify our framework
by matching Census Bureau operating data with patent data for U.S.  rms. We observe that
internal innovation scales moderately faster with  rm size than external innovation.
JEL Classi cation: O31, O33, O41, L16.
Keywords: Endogenous Growth, Innovation, External, Internal, Research and Develop-
ment, Patents, Citations, Scientists, Entrepreneurs.
 Comments are appreciated and can be sent to uakcigit@uchicago.edu and wkerr@hbs.edu. We thank Daron
Acemoglu, John Haltiwanger, Dirk Krueger, Rasmus Lentz, Matt Mitchell, anonymous referees, and many seminar
participants for their insights. We especially thank Sam Kortum for his comments and guidance on the work. Kerr
is a research associate of the Bank of Finland and thanks the Bank for hosting him during a portion of this research.
Selman Erol, Kaushik Ghosh, and especially Harun Alp provided excellent research assistance on this project. The
research in this paper was conducted while the authors were Special Sworn Status researchers of the US Census
Bureau at the Boston Census Research Data Center (BRDC). We gratefully acknowledge  nancial support from
the Alfred P. Sloan Foundation, the Ewing Marion Kau man Foundation, Harvard Business School, the Innovation
Policy and the Economy forum, and the National Science Foundation. Research results and conclusions expressed
are the authors' and do not necessarily re
ect the views of the Census Bureau or NSF. This paper has been screened
to ensure that no con dential data are revealed.Manuscript
 Click here to download Manuscript ms.tex 
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 2 -->


Growth through Heterogeneous Innovations
1 Introduction
Innovations di er substantially in their qualities, from major breakthroughs to small incremental
re nements. Innovations also di er in their types: Many innovations help  rms improve their ex-
isting portfolio of products or technologies, while others expand the portfolios of  rms and enable
them to enter into new markets. How do innovation qualities and types relate to  rm characteris-
tics? Some accounts emphasize the many great breakthroughs of independent entrepreneurs, while
others describe the  nancial might and longer investment horizons that large companies can take
towards innovation. Either way, a Silicon Valley start-up will behave very di erently from the R&D
laboratory of General Electric. These observations lead to important questions: Are there inno-
vation di erences between large and small  rms and, if so, how substantial are the gaps? How do
 rms change their innovation strategies over their life cycles? What are the aggregate implications
of di erent-sized  rms producing heterogeneous innovations and spillovers?
This paper is a major attempt to answer these questions empirically, theoretically, and quanti-
tatively using a fully-speci ed endogenous growth model. Despite many advances, growth theory
mostly provides frameworks that include a single type of innovation, perhaps drawn from a distri-
bution, but not the variation in types that empirical work has uncovered. Similarly, the  rm size
distribution is rarely important for how these growth models function. Our framework allows for
heterogeneity along both dimensions and links them together. We describe an economy with  rms
of multiple sizes that pursue di erent types of innovations and impact growth in di erent ways.
As a result, the model allows for di erent-sized  rms to generate multiple forms of innovation that
have di erent spillovers.
The model of Klette and Kortum (2004) provides a  rst step in this e ort. Their framework
allows  rms to own multiple product lines that are added or lost on the basis of innovation and
creative destruction forces. Klette and Kortum (2004) and Lentz and Mortensen (2008) show that
this set-up exhibits many behaviors consistent with the applied micro literature (e.g., skewness of
the  rm size distribution, greater growth volatility of small  rms). Following Lentz and Mortensen
(2008), many researchers use this powerful platform for applied growth theory, and we use it
ourselves in Acemoglu et al. (2013) andAcemoglu et al. (2016). This framework does not, however,
incorporate heterogeneous types of innovation, and innovation decisions are uniform across the  rm
1
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 3 -->


Akcigit and Kerr
size distribution (indeed, the model's perfect scaling of innovation choices with  rm size underlies
the framework's analytical beauty).
We introduce into this framework new heterogeneity in the types of innovations undertaken by
 rms, which in turn shapes how the  rm size distribution can matter for the economy. We distin-
guish two types of innovation that  rms undertake: external andinternal. Firms undertake external
innovations to create new products and capture markets from others, while internal innovations
improve product lines that  rms currently own. This heterogeneity in the forms of innovation and
the step sizes of associated advances is central in accounts of the di erences in innovation for large
and small  rms and yet not included in prior growth models.1
Our paper makes three key advances. The  rst is to build a growth model that incorporates
multiple forms of innovation, a direct connection from  rm size to choices over types of innova-
tions, and multiple step sizes in the impact of innovations that are endogenously determined. Our
baseline model analyzes a setting where internal innovations scale up with  rm size, while external
innovations do not. The tractable model yields analytical solutions and stark predictions about how
the innovations of new entrants and small  rms will di er from large  rms. The model provides
micro-founded explanations for small  rms experiencing faster average growth and contributing
disproportionately to major innovations.
The second contribution is to incorporate patents and patent citations into our endogenous
growth framework, which allows us to connect endogenous growth theory to the empirical innovation
literature (e.g., Griliches (1990)). Using  ndings from this empirical literature, we characterize
how patent citations would look in our economy and show how citation patterns hold information
relevant to the model. While these additions do not impact the model's economy directly (e.g.,
 rms don't block rivals with patents), citations provide greater depth to the results that we can
characterize. For example, we derive tests that employ patent citations to compare the growth
spillover e ects from external and internal innovations. Moreover, distributions of patent citations
contain much of the information that we need to quantify the model.
Our third contribution is a generalized framework that allows an arbitrary amount of scaling
1We mostly use the terms R&D and innovation interchangeably, favoring the latter. Strictly speaking,  rms
make R&D investments and realize innovation outcomes, and these are not perfectly correlated due to randomness
in achieving results. Nevertheless, our model makes similar predictions for both objects given their tightly coupled
nature.
2
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 4 -->


Growth through Heterogeneous Innovations
for external innovation with  rm size (internal innovation always scales fully). At the extremes of
this generalized framework are the extended Klette and Kortum (2004) framework (perfect scaling)
and our baseline model (no scaling). We quantify the model using indirect inference with Census
Bureau data on all patenting  rms during the 1982-1997 period. We observe moderate departures
from the Klette and Kortum (2004) world for the United States. However, we also  nd that this
departure could generate some sizable cost increases for large  rms. In particular, according to
our estimates, it costs 25% more for a  rm that is at the 90th percentile of the size distribution to
produce a major innovation than the median innovative  rm in the economy.
Our analysis helps inform long-standing debates about the role of small vs. large  rms for
innovation. For instance, we show that the relative rate of major inventions is higher in small
 rms. We demonstrate that these distributional di erences are not due to di erences in research
capabilities or technologies, but are instead an outcome of innovation investment choices by  rms.
We also decompose the aggregate growth due to innovation and  nd 19.8% is due to internal e orts
of incumbents, 54.5% to external e orts of incumbents, and 25.7% is due to new entrants.
In terms of the literature, we most clearly build on the e orts of Klette and Kortum (2004),
Lentz and Mortensen (2008), and Akcigit (2010) to incorporate more insights from the empirical
literature on innovation into workhorse theoretical models.2These papers in turn depend upon the
long endogenous growth literature.3Our work on spillover bene ts builds upon contributions like
Spence (1984) and Griliches (1992), with Caballero and Ja e (1993) and Eeckhout and Jovanovic
(2002) being rare examples that connect patent citations to a growth model. We are the  rst to
do so at a  rm level and with a focus on identifying varieties of innovation. Finally, we are deeply
connected to the empirical literature on  rm size and innovation that we review in the next section
as a prelude to our model.4
2More recent contributions are Lentz and Mortensen (2014), Garcia-Macia et al. (2016), and Akcigit et al. (2013).
3Classics include Aghion and Howitt (1992), Aghion et al. (1997), Aghion et al. (2001), Grossman and Helpman
(1991), Howitt (1999), Jones (1995), Kortum (1997), and Romer (1986, 1990). Acemoglu (2008), Aghion et al. (2014),
andBarro and Sala-i Martin (1995) provide full reviews.
4Our work likewise relates to the economics literatures on innovation and industry structure and evolution. Exam-
ples include Acemoglu and Akcigit (2012), Acemoglu and Cao (2015), Arkolakis (2011), Bloom et al. (2013), Cabral
and Mata (2003), Cai(2010), Cohen (1995), Dunne et al. (1988), Duranton (2007), Gans et al. (2002), Gilbert and
Newbery (1982), Hausman et al. (1984), Hopenhayn (1992), Hopenhayn et al. (2006), Jovanovic (1982), Jovanovic
and MacDonald (1994), Kerr (2010), Klepper and Graddy (1990), Lamoreaux et al. (2011), Lerner (1997), Luttmer
(2007, 2011), Nicholas (2014), Reinganum (1983), and Rosen (1991).
3
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 5 -->


Akcigit and Kerr
2 Empirics of Innovation
This section reviews prior work on the di erences in innovation across the  rm size distribution.
We then document three empirical regularities that motivate our model and are used to discipline
its quantitative analysis. In later sections, we provide additional results when comparing the
quanti ed model and empirical data on untargeted dimensions. Our appendix and NBER working
paper, Akcigit and Kerr (2010), contain many empirical extensions.
2.1 Innovation Across the Firm Size Distribution
A large empirical literature debates whether small or large  rms contribute disproportionately as
the source of radical innovations or achieve a greater innovation return per R&D dollar invested.5
Our model attempts to address these questions using a novel approach. Our framework would
be extremely uninteresting if we endowed  rms of various sizes with capabilities not available to
others (e.g., assuming that small  rms could achieve new breakthrough improvements not possible
for larger  rms). Instead, we trace out why large and small  rms might invest at di erent rates
in the same set of potential innovation approaches, with the heterogeneous innovations being an
outcome rather than an assumption.
We focus on internal vs. external innovation as it aligns with many important empirical insights
and it is the type of heterogeneity that we can measure most directly with data. At an extreme,
external vs. internal di erences must exist. Entering entrepreneurs do not have products to improve
upon, and so by de nition are di erent from incumbents. The literature further suggests this
di erence is pervasive, rather than con ned to the entry margin, and usually emphasizes a greater
internal focus for large  rms.
Large  rms might invest more in internal improvements since they can derive a better return
from these investments than small  rms. In situations where innovations are useful for enhancing
a company's operations but are otherwise hard to protect/sell, large companies achieve a greater
return for the same investment due to their larger base of operations. These incentive di erences are
5For example, Acemoglu et al. (2016), Acs and Audretsch (1987, 1988, 1991), Baumol (2002), Kerr et al. (2014),
Kueng et al. (2014), Nelson and Winter (1982), Peretto (1998), Rausch (2010), Rosen (1991), Samila and Sorenson
(2011), Thomke (2003), and Zucker et al. (1998). Of the e orts to quantify these claims, the best known is the
Kortum and Lerner (2000)  nding that venture capital dollars invested in small start-ups are three times more
potent for generating patented innovations than corporate R&D expenditures.
4
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 6 -->


Growth through Heterogeneous Innovations
frequently discussed for process innovations (e.g., Klepper, 1996), and Cohen and Klepper (1996)
show process R&D is more tightly linked to  rm size than product R&D. While these patterns
are consistent with internal innovation scaling more directly with  rm size, at least one counter
example exists. Basic R&D is also more likely to be conducted by large  rms due to the  xed
costs of basic R&D laboratories and the ability to realize resulting discoveries across a range of
products. To the extent that basic R&D also provides serendipitous advances that aid entry into
new industries outside of the  rm's current span, larger companies garner more external innovation.
An additional class of explanations for why large companies may pursue proportionately less
external innovation relates to organizational frictions and managerial capabilities. Under the Lu-
cas(1978) span-of-control model, there are limits to the number of operations that the world's
best managers can e ectively guide, and thus large companies might endogenously invest more in
improving their existing products vs. further expansion. These limits to optimal  rm size would
e ectively give a comparative advantage to small  rms for pursuing the acquisition of new lines.6
Related, models Hellmann and Perotti (2011) and Gromb and Scharfstein (2002) emphasize situa-
tions where the internal resources of large companies can be necessary for completing innovations.
On the other hand, the management literature frequently stresses organizational rigidities that in-
e ciently inhibit the external innovation e orts of large companies (e.g., Christensen, 1997, Clark
and Henderson, 1993, Henderson, 1990, March, 1991).7
External environments also shape innovation incentives for large companies, with  nancial mar-
kets being a well-studied example. Bernstein (2015)  nds that being a publicly listed  rm reduces
the novelty of a  rm's innovations by 40% and shifts work towards more conventional and internal
projects, while perhaps o ering additional funds for acquisitions. Lerner et al. (2011) reach similar
conclusions when examining the impact of private equity  rms on the innovation rates of the  rms
that they remove from public markets. Other studies  nd conglomerate  rms frequently trade at a
discount, and that managers often reduce R&D budgets to meet short-term return targets. Thus,
6Akcigit et al. (2015) introduces a span-of-control limitation for  rms into the Klette and Kortum (2004) framework
to study the  rm dynamics in the Indian manufacturing sector. Their model emphasizes how these managerial
conditions create limits to the scaling of  rms and their pursuit of new product lines, connecting to the empirical
work of Hsieh and Klenow (2014).
7Galasso and Simcoe (2011) identify how CEO personality traits shape innovation investments, and Lerner (2012)
further reviews the recent literature on the advantages and liabilities of large companies for pursuing new innovation
areas compared to start-ups (e.g., compensation constraints).
5
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 7 -->


Akcigit and Kerr
while deep capital markets may provide valuable resources to public companies, they appear to
create environments less attractive for external innovation.8
This brief literature discussion highlights why the internal vs. external distinction is likely to
be important. Several data sources are consistent with this observation:9
 Using the 2008 Business R&D and Innovation Survey, we observe a -0.16 correlation between
 rm size and the share of R&D that the  rm reports is directed towards business areas and
products where the company does not have existing revenues. Similar negative correlations
are found for questions about the share of  rm R&D being directed to technologies new to
markets.
 Using the 1979-1989 NSF R&D Surveys that recorded product vs. process R&D expenditures,
we observe a 0.22 correlation between  rm size and the share of R&D that the  rm reports
is process oriented. This accords with Cohen and Klepper (1996), and we  nd similar results
for indicator variables about the  rm conducting any process-focused R&D.
 Using the citations that  rms make on the patents they  le, we observe a 0.11 correlation
between  rm size and the share of citations given that are to a  rm's own prior patents.
Firms with larger past patent portfolios are mechanically more likely to self cite, and the
appendix C.1reports Monte Carlo simulations that measure the expected likelihood of self
citations given the technology and years that a  rm cites in their patents. Larger  rms are
more likely to show abnormal rates of self citations compared to these counterfactuals, with
the correlation to  rm size of being out of the simulated 95th percentile bound being 0.23.
These correlations point towards a consistent picture of heterogeneity in innovation behavior by
 rm size. An advantage of our model is its capacity to place these data pieces into context and use
indirect inference for more general statements.
8Di erences beyond  nancial markets also exist. Agrawal et al. (2010) consider how large companies may be
located in more isolated cities that limit the diversity of external ideas that they receive and can build upon. Some
industries are also characterized by a market for ideas (e.g., Gans et al. (2002)) that shifts the organization of innova-
tion for external work. Finally, policies with  rm-size-dependent components like labor regulations may make external
innovation less attractive for large companies to the extent that policies make the labor adjustments associated with
risky activities more costly for larger employers.
9All reported correlations measure  rm size through log employment and are statistically signi cant at a 5% level.
The correlations are taken over reported data in each survey, and some of these sources have incomplete coverage
for small R&D producers, as described in our working paper. These sample constraints likely weaken the observed
correlations to  rm size.
6
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 8 -->


Growth through Heterogeneous Innovations
2.2 Data Development
Our project employs the Longitudinal Business Database (LBD) and the NBER Patent Database.
The LBD is a business registry for the United States that contains annual observations for every
private-sector establishment with payroll from 1976 onward (Jarmin and Miranda, 2002). The
Census Bureau data are an unparalleled laboratory for studying the  rm size distribution, entry/exit
rates, and life cycles of U.S.  rms. Sourced from U.S. tax records and Census Bureau surveys, the
micro-records document the universe of establishments and  rms rather than a strati ed random
sample or published aggregate tabulations. We aggregate establishment-level records into  rm-year
observations using parent  rm identi ers.
We next match into the LBD the individual records of all patents granted by the United States
Patent and Trademark O ce (USPTO) from January 1975 to May 2008. Each patent record
provides information about the invention and the inventors submitting the application. Hall et al.
(2001) provide extensive details about these data, and Griliches (1990) surveys the use of patents
as economic indicators of technology advancement. We only employ patents 1)  led by inventors
living in the United States at the time of the patent application, and 2) assigned to industrial  rms.
In 1997, this group comprised about 77 thousand patents (40% of the total USPTO patent count
in 1997, with most of the residual being patents to foreign inventors). We match these patent data
to the LBD using  rm name and location matching algorithms that build upon Balasubramanian
and Sivadasan (2011) and Kerr and Fu (2008).10
Our  nal sample is the universe of patenting U.S.  rms with employees, comprised of 23,927
 rms that have been granted at least one patent by the USPTO over the 1982-1997 period. We
use earlier and later time periods for calculating some of our metrics on these  rms. This dataset
is the foundation for our empirical estimates in this section and also our quantitative analysis in
later sections. There are several important features about this dataset to highlight.
First, our sample only includes innovative  rms, which have a di erent  rm size distribution
than the economy as a whole. In our sample, for example, 14% of  rms have more than 500
10Our NBER working paper describes this matching procedure and the data employed more extensively. The
working paper also provides complementary evidence from the National Science Foundation's R&D Survey that
supports the patent-based results provided here. The NSF Survey sub-samples R&D performers that conduct less
than $1 million in R&D annually, and thus our focus on patenting allows us greater con dence for capturing the
complete  rm size distribution for innovative  rms.
7
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 9 -->


Akcigit and Kerr
employees at some point in their life span (12% for all observations of the  rm), while this share is
about 0.3% for the whole economy. This tilt towards larger  rms is not surprising, as the majority
of small  rms do not seek new innovations or to grow from their current size (Hurst and Pugsley
(2011)). This is often connected to non-pecuniary motivations for starting a business (e.g., to be
one's own boss). We thus exclude large numbers of non-innovative  rms from our sample (e.g.,
restaurants, beauty salons, grocery stores) to be in keeping with the model of innovative  rms.11
Second, only a few innovative  rms patent in every year, and the same is true in our model
with respect to realizing an innovation. These considerations lead us to use our data in two ways.
In some cases (e.g., Gibrat's law estimations), we conduct an annual analysis as the necessary
data elements are continually observed in both the data and the model. In other cases (e.g.,
quality distributions of realized innovations), we focus on  ve-year periods and the  rms achieving
innovations as depicted below. Our quantitative model exactly mirrors each data development step
undertaken to ensure that we precisely align the model with the data. This mirroring technique
has the powerful advantage of allowing us to select the approach that best suits each prediction,
accounting for the nuances of the data assembled.
Sample selection is very important, and we align the data and model as much as possible and
subject to the same treatment. Many parts of this e ort are quite straightforward. First, we de ne
metrics the same in both datasets (e.g., how exit is coded). Second, we ensure in both datasets that
we measure moments in comparable groups. For example, most innovation-related moments are
measured across continuously innovative  rms in both datasets to ensure comparability. Third, our
model is one in which every  rm invests in R&D and attempts to grow, and thus we earlier noted
the boundary condition that we are not attempting to model  rms that do not seek to develop new
ideas or expand [e.g., Hurst and Pugsley (2011), Akcigit, Alp, and Peters (2015)]. This too is true
in both the empirical work and model estimation.
There is one selection margin, however, that is more challenging and worth additional comment
and checking. While the model is built upon  rms always investing in R&D, success in these
e orts is stochastic and thus some R&D  rms do not realize innovations. In the empirical data,
11Approximate 25th, 50th, and 75th percentile levels of employment in our sample are 17, 70, and 370 employees.
These are \fuzzy" averages around these points in order to satisfy Census Bureau disclosure requirements. The mean
employment level is about 1805 workers.
8
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 10 -->


Growth through Heterogeneous Innovations
by contrast, the best and most comprehensive approach to identifying innovative  rms is through
patenting, as this does not encounter truncation biases common to R&D surveys that subsample
 rms below a threshold of R&D expenditure. However, our selection process does mean that every
 rm in our sample has achieved at least one patent in our sample period, which is not strictly true
in the model (e.g., a  rm might have achieved an innovation in the distant past that allowed it to
enter the market but it has not been successful in further e orts).
Several auxiliary tests suggest that this is not a  rst-order concern. First, when we impose the
equivalent of a patent-like selection criteria in our simulation period, we retain almost 99% of our
sample and hence our simulated moments are essentially unchanged. Second, as most moments are
aggregated or calculated over our continuously innovative samples, the greatest potential sensitivity
to this feature is the upcoming estimation of Gibrat's Law in Section 2.3. An additional form of
assurance comes in that we observe a very similar growth-size relationship when expanding our
sample to the broader manufacturing sector without imposing any selection criteria{speci cally, our
samples coe cient of 0:0351 (0:0013) becomes 0:0495 (0:0004) in the full sector-wide estimation{
suggesting broad stability on this particular margin.
2.3 Firm Growth by Firm Size
We  rst document the empirical regularity that small  rms grow faster than large  rms.12We test
this prediction using annual employment growth patterns for U.S. innovative  rms. Following Lentz
and Mortensen (2008), we de ne for  rm fthe employment growth of EmpGrf;t= [Empf;t+1
Empf;t]=Empf;t:We model employment growth without conditioning on survival and thus retain
EmpGrf;t=1 for businesses that close between tandt+ 1 (the LBD measures employment in
March of each year). This metric is unbounded upwardly, and we impose a 1000% growth cap.
With this winsorization, the mean of EmpGrf;tis 0.0745.
Dividing our sample into 20 roughly equal-sized bins in terms of numbers of  rms by current
employment levels, Figure 1displays the average forward growth rate across  rms in each size bin.
12The empirical deviation from Gibrat's Law of proportionate growth is extensively documented in surveys such
as Sutton (1997), Caves (1998), and Geroski (1998) and is among the stylized facts in Klette and Kortum (2004).
The Klette and Kortum (2004) model yields Gibrat's law. Lentz and Mortensen (2008) show that the addition of
 rm heterogeneity into the Klette and Kortum (2004) model is consistent with deviations from proportionate growth
observed in Danish  rm-level data.
9
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 11 -->


Akcigit and Kerr
The horizontal axis provides the average employment level for  rms in the bin. The declines in
average forward growth are substantial until about 50 employees, and they are again strong at the
largest  rm sizes. Appendix C.4shows a negative relationship when using the establishment counts
of  rms to generate  rm size bins. Size bins based upon establishment counts are substantially
coarser than employment but provide a complementary approach.
[Figure 1 Here]
To provide a single estimate and also control for industry-year  xed e ects  i;t, we estimate,
EmpGrf;t= i;t0:0351
(s.e. 0.0013) ln(Empf;t) + f;t:
This coe cient  nds a 10% increase in  rm employment is associated with a 0.35% reduction in
forward employment growth, or about 5% of the sample mean. The growth impact of the in-
terquartile range of  rm size (approximately 17 to 370 employees) is 10.8%, somewhat larger than
the mean.13This relationship is robust to alternative measures of  rm size, weighting observations,
or considering panel variation, re
ecting the many settings where it has been observed in prior
research. Conditional growth estimations that exclude exiting  rms yield a steeper negative rela-
tionship, as does raising the maximum growth rate (discussed further below in model robustness
checks). When using the Davis et al. (1996) formula that compares growth to the average of the
two periods, conditional estimations also yield a consistent negative relationship across the many
speci cation variants discussed, while unconditional estimations do not exhibit a clear pattern.
2.4 Innovation Intensity by Firm Size
We next consider the innovation intensity to  rm size relationship. Our model will consider this
intensity in terms of  rm-level inputs (e.g., R&D-to-sales ratios) and realized outputs (e.g., rate
of realized innovations per product line). We can discipline the model through either relationship,
and for several data quality reasons we pursue the realized rate of innovation outputs.14
13The regression sample includes 146,678 observations. We assign industries to  rms at the two-digit level of the
Standard Industrial Classi cation system using industries in which  rms employ the most workers. Regressions are
unweighted and cluster standard errors at the  rm level.
14Our NBER working paper provides complementary tabulations of R&D expenditures per sales or per employee
across the  rm size distribution using the NSF R&D Survey.
10
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 12 -->


Growth through Heterogeneous Innovations
We study this prediction through patents per employment Patent=Empl f;t, where the timing
of patents is by their application year. The largest innovative  rms like Microsoft or Boeing apply
for many patents each year, but most innovative  rms are irregular and lumpy in their patent
 lings. We thus analyze this prediction with  ve-year periods that extend 1982-1986, 1987-1992,
and 1992-1996. (With some abuse of notation, we continue to use tto represent time periods.) We
focus this exercise on \continually innovative  rms" in the sense that included  rms  le at least
one patent in each  ve-year period that they are observed to be in operation. This dataset includes
16,818  rm-period observations. The continuous sample approach keeps a consistent de nition with
respect to non-zeros and facilitates a sharper match with the model, where we also impose this
requirement for included  rms to be continually innovative over  ve-year periods.
Figure 2 shows the empirical relationship where we again divide our sample into 20 size bins.
There is a substantial decline in innovation intensity with  rm size among the continuously inno-
vative  rms. Appendix C.4 again shows a similar relationship when using establishment counts to
develop size bins.15
[Figure 2 Here]
To prepare for the future matching of our data moment to the model, we transform Patent=Empl f;t
to be of mean zero and unit standard deviation during each period. We use the transformed series
because the exact level of U.S. patenting per employee does not have a direct meaning or coun-
terpart to the levels of a theoretical model. By placing both data and model outcomes into unit
standard deviations, we are able to match and compare them. Our key estimation is
Patent=Empl f;t= i;t0:1816
(s.e. 0.0058) ln(Empf;t) + f;t:
This coe cient  nds a 10% increase in  rm employment is associated with a reduction of 0.018
standard deviations in patents per employee among innovative  rms. Across the interquartile range
of  rm sizes, the impact is 0.561 standard deviations. If we relax the continuous innovator sample
15The restriction to continuously innovative  rms will in
uence this relationship. For example, the sample excludes
 rms that attempt to innovate but fail to achieve a patent, be they small  rms and or larger ones that are only
marginally innovative. Our quantitative analysis handles this feature by treating the simulated data in an identical
way for this relationship and selecting  rms that achieve innovations in each time interval we use for equivalent
estimations.
11
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 13 -->


Akcigit and Kerr
restriction, the coe cient is very similar at -0.164. We also  nd robust results with the many
regression variants discussed above with the employment growth speci cations.
2.5 Fraction of Major Innovations by Firm Size
Our model's structure allows for internal and external innovations to have di erent average impacts
in terms of realized improvements upon existing technologies, and the model does not require
one form of innovation to be larger than the other. Nevertheless, if external innovations have a
larger average impact than internal innovations, then our baseline model makes some important
predictions regarding small innovative  rms and new entrants having a comparative advantage for
achieving major advances. If internal innovations have the larger average impact, then larger  rms
will hold this advantage for achieving major advances.
To investigate, Figure 3provides some empirical evidence regarding the relative impact of
external vs. internal innovations using patent citations. The sample is restricted to patents of U.S.
industrial  rms that have all inventors located in the United States. Similar to academic papers,
patents give citations to prior patents upon which the current invention builds. Going forward, the
impact of a patent is often measured in terms of the citations it subsequently receives. Examining
the citations given to prior patents at the time of the patent  ling, we classify patents into external
vs. internal innovations. Internal patents are those where 50% or more of the given citations are
to the prior inventions of the  rm  ling the patent (termed self citations). External patents are
where self-citations represent less than 50% of the citations given at  ling.
We measure forward impact through external citations received by the patent in the future
(i.e., excluding future self citations made by the  rm). The lighter dashed line in Figure 3provides
the distribution of future citations received for internal patents  led between 1975-1984. The
darker solid line provides the distribution for external patents that make no citations to prior
patents of the  rm. There is no mechanical reason for these two series to be di erent from each
other as the citations given and received are distinct from each other. Both series display a large
number of patents with no external citations and a skewed distribution, which are predictions of
our framework. More important, the comparison of the external and internal distributions shows
12
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 14 -->


Growth through Heterogeneous Innovations
that the former exceeds the latter in a form akin to  rst-order stochastic dominance.16
[Figure 3 Here]
With this background, we next verify that small innovative  rms and new entrants have a
comparative advantage for achieving major advances. We  rst identify the quality of each patent in
terms of its external citations compared to its peers from the same technology class and application
year. Constructing an indicator variable for the patent being in top decile in terms of these external
citations, we calculate TopPatentShare f;tas the average of these patent-level indicators across a
time period for a  rm. Not surprisingly, the average of this variable is about 0.10. We then estimate
this  rm-level measure as a function of  rm size as
TopPatentShare f;t= i;t0:0034
(s.e. 0.0008) ln(Empf;t) + f;t: (1)
This estimation  nds that a 10% increase in  rm employment is associated with a reduction of
0.034% in the fraction of a  rm's patents among the top decile of the patent quality distribution.
Relative to the sample mean, this e ect is 0.34%. Across the interquartile range of  rm sizes, the
impact is 0.011, or a tenth of the sample mean.
Table 1 broadens the lens and repeats speci cation (1) for each quartile of the patent quality
distribution using our continuous innovation sample. The  rst column documents the lowest quality
quartile, while the last column is the highest one; coe cients across the four speci cations naturally
sum to zero. Estimations again control for industry-period  xed e ects. Larger  rms are associated
with a systematic shift in the quality of their patents out of the top quartile and into the bottom
half of the distribution.17
[Table 1 Here]
16The di erences are statistically signi cant and hold in regressions that control for a variety of traits about the
patents (e.g., technology-year  xed e ects) or  rm  xed e ects. The omitted, middle group (i.e., patents where
backwards self citations are present but not a majority) behaves similarly to the no self citation group and are
excluded for visual clarity; later, we will group them with external patents for our model quanti cation.
17Our working paper further uses this framework to con rm our model's hypothesis that  rm size di erentials
weaken with more-stringent citation quality thresholds due to the increasing relative importance of the stochastic
nature of realized inventions.
13
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 15 -->


Akcigit and Kerr
3 Baseline Theoretical Framework
We begin with a baseline model that incorporates the empirical regularity that external R&D
does not scale as fast as internal R&D with  rm size. Our goal is to study the implications of
this heterogeneity on the R&D, innovation and growth dynamics of  rms. To allow for analytical
solutions and to build intuition, we  rst consider a stark environment where external R&D does not
scale at all with  rm size. We then generalize the theoretical framework in Section 4 to allow scaling
of external R&D, with this baseline model and Klette and Kortum (2004) being extremes of the
general framework. On top of this general framework, we also overlay patent citation behavior in
Section 5. Within this framework we can interpret data on patent citations, allowing us in Section
6to estimate parameters of R&D scaling within  rms.
3.1 Preferences and Final Good Technology
Consider the following continuous time economy. The world admits a representative household
with a logarithmic utility function
U=Z1
0exp ( t) lnC(t)dt: (2)
C(t) is consumption at time t;and  >0 is the discount rate. The household is populated by a
continuum of individuals with measure one. Each member is endowed with one unit of labor that
is supplied inelastically.
Individuals consume a  nal good Y(t), which is also used for R&D as discussed below. The  nal
good is produced by labor and a continuum of intermediate goods j2[0;1] with the production
technology
Y(t) =L (t)
1 Z1
0q 
j(t)k1 
j(t)dj: (3)
In this speci cation, kj(t) is the quantity of intermediate good j, andqj(t) is its quality. We
normalize the price of the  nal good Yto be one in every period without loss of generality. The
 nal good is produced competitively with input prices taken as given. Henceforth, the time index
twill be suppressed when it causes no confusion.
There is a set of  rms that are producing intermediate goods and their measure, F2(0;1);
14
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 16 -->


Growth through Heterogeneous Innovations
will be determined in equilibrium. Each intermediate good jis owned by a  rm f. A  rm is
characterized by the collection of its product lines Jf=fj:jis owned by  rm fg. Similarly we
denote the product (quality) portfolio of  rm fby a multiset qf=fqj:j2Jfgand denote the
cardinality by nf:18Figure 4 illustrates two  rms. Firm f= 1 has 5 product lines and f= 2 has
3 product lines (i.e., n1= 5 andn2= 3).
[Figure 4 & 5 Here]
Each intermediate good j2[0;1] is produced with a linear technology
kj=  qlj; (4)
whereljis the labor input and   q R1
0qjdjis the average quality in the economy.
In addition to the variable cost, production requires also a  xed cost of operation    qat the  rm
level in terms of the  nal good. As we will discuss later, this  xed cost avoids any non-linearities
in the  rm's value function.19
Individuals work in two capacities:  nal good production (L) and intermediate good production
(~L). In each period, the labor market has to satisfy the constraint
L+~L 1: (5)
Ris the total R&D spending, Kis the total  xed cost paid by  rms, and therefore the resource
constraint of the economy is Y=C+R+K.
3.2 Research and Development
The last innovator in each product line owns the leading patent and has monopolist pricing power
until being replaced by another  rm. Intermediate producers have pro t incentives to improve the
technologies for their existing products, thereby increasing associated quality. In addition, both
incumbents and potential entrants have incentives to add new products to their portfolios through
R&D competition. We now describe the innovation types which are also illustrated in Figure 5.
18A multiset is a generalization of a set which can contain more than one instances of the same member.
19See Proposition 1and the text above it for details.
15
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 17 -->


Akcigit and Kerr
Internal R&D Incumbent  rms undertake internal R&D (or innovation) to improve their exist-
ing products. To improve an existing product j2Jf,  rmfspends
Rz(zj;qj) = ^ z^ 
jqj (6)
units of the  nal good, where ^   > 0 and ^ > 1. Internal innovations are realized with the
instantaneous Poisson 
ow rate of zj 0. Cost (6) is proportional to the quality of the good that
the  rm is improving. First, this implies that a more-advanced technology has higher R&D costs.
Second, as will be shown in the next section, equilibrium returns to internal innovations are linear
inqj:Therefore, the linear e ects in return and cost cancel out and yield an internal innovation
e ort that is independent of the quality of the product line. When internal R&D is successful, the
current quality improves by a multiplicative factor  >0 such that qj(t+  t) = (1 +  )qj(t).
External R&D External R&D (or innovation) is undertaken by incumbents and potential new
entrants to obtain technology leadership over products that they do not currently own. A  rm with
n > 0 produces a 
ow rate xby payingRxin terms of the  nal good according to the following
cost function:20
Rx(x; q) = ~ x~  q; (7)
where ~  > 0 and ~ > 1:Cost (7) is proportional to the average quality level   qin the economy,
which again removes the dependence of innovation e orts on average quality since the returns to
external innovations will be proportional to   qand ensures that the R&D spending is a constant
fraction of the total output Y.
External R&D e orts are undirected in the sense that resulting innovations are realized in any
product line j2[0;1] with equal probability. This model structure has two main implications.
First,  rms do not innovate over their own product lines through external R&D since this event
has zero probability. Second, there is no strategic interaction among  rms. In addition to stochastic
20Note that the cost function in (7) corresponds to the following production function: x=h
Rx
~  qi1
~ 1n>0where
1n>0is an indicator function. This speci cation implies that past innovation, i.e. n>0;a ords  rms capacities to
innovate in the future. This structure is in the same spirit as the Klette and Kortum (2004) model that assumes a
Cobb-Douglas functional form: x=R1
~ n11
~ :For now, we shut down the dependence on nat the intensive margin
to prevent any scaling and just keep the dependence on the extensive margin via the indicator function.
16
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 18 -->


Growth through Heterogeneous Innovations
arrival rates, the sizes of realized quality improvements are randomly determined (see Figure 6):
[Figure 6 Here]
(i) With probability  2(0;1), the innovation is a major advance that substantially shifts forward
the latest quality level by a size   qsuch thatqj(t+  t) =qj(t)+  q(t). This generates a new
technology cluster with an associated wave of subsequent follow-on innovations. Prominent
examples include the transistor and mapping the human genome, but the step functions need
not be so profound. The conceptual construct is that these major advances de ne a wave of
innovation and product development until another major advance starts a new wave.
(ii) With probability 1  , the innovation is a follow-up improvement to the current technology
level of the product line that does not generate a new technology cluster. The size of the
follow-up improvement declines with the number of follow-up inventions since the last major
advancement. If the last major innovation in product line joccurredkjinnovations ago, the
new step size is sj q, wheresj=  kjwith 2(0;1).
Technology Clusters and Evolution The economy-wide arrival rate of new products, denoted
by , is endogenously determined by external R&D e orts of incumbents and potential entrants
and is characterized in detail below. With  determined, the probabilistic evolution of the quality
levelqjafter a short interval   tis
qj(t+  t) =qj(t) +8
>>>>>>><
>>>>>>>:  q(t)
  kj q(t)
 qj(t)
0with probability
with probability
with probability
with probability   t
(1 )  t
zj t
1zj t  t(8)
The  rst line represents a major advance that results from external R&D with probability  . The
second line represents a follow-up innovation that results from external R&D with probability
1 . The third line shows an internal improvement of size  by the current owner of product line j
through internal R&D. The  nal line represents the case where no quality improvement is realized
during  t, which results in stagnant technology quality.
17
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 19 -->


Akcigit and Kerr
The following example illustrates a possible evolution of innovations in a random product line,
with the top row of numbers representing the step size of each innovation:
Example 1
j
j
j  q
P1;f1   q
P2;f2  2 q
P3;f3 qj
P4;f3 qj
P5;f3  3 q
P6;f4| {z }
Tech Cluster 1j
j
j  q
P7;f5 qj
P8;f5   q
P9;f6|{z}
Tech Cluster 2j
j
j  q
P10;f7   q
P11;f8  2 q
P12;f9:::
|{z}
Tech Cluster 3
An example of a sequence of innovations in a product line
Here,Pm;fdenotes that the mth patent is obtained by  rm f. The example starts with a major
innovation that opens a new technology cluster by  rm f1. Firmsf2andf3then produce follow-up
external innovations. Firm f3further improves its own product twice. Firm f4then produces a
further follow-up external innovation. Next, this technology cluster is replaced by a new leading
innovation by  rm f5which is patented as P7. The second cluster is then replaced by another
leading innovation by  rm f7. This new cluster is further improved by patents 11 and 12, and so
on.
We later analytically solve for an expected step size   sfrom external innovations. For now, it is
important to note that this theoretical structure does not depend upon   sbeing greater or smaller
than , and in fact this comparison may di er substantially depending upon the country and time
period studied. The baseline model framework is very general with respect to the relative sizes of
internal versus external improvements.
3.3 Entry and Exit
As in Klette and Kortum (2004), a mass of entrants invest in R&D in order to become intermediate
producers upon a successful innovation. Entrants choose an innovation 
ow rate xe>0 with an
R&D costCe(xe; q) =xe  qin terms of the  nal good, where   >0 is a constant scale parameter.
The valueV0of being an outside entrepreneur is the expected value from innovating successfully
and entering the market. This value is determined according to
rV0_V0= max
xefxe[EjV(fqj+sj qg)V0] xe qg; (9)
18
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 20 -->


Growth through Heterogeneous Innovations
whereV(fqjg) denotes the value of a  rm that owns a single product line with quality qjand _V0 
@V0=@tdenotes the partial derivative of the outside value with respect to time. The expected value
EjV(fqj+sj qg) of a new innovation is an expectation over both quality level qjand innovation
sizesj. When there is positive entry, the equilibrium is such that
EjV(fqj+sj qg) =  q: (10)
Incumbent  rms produce intermediate inputs and invest in R&D. As a result,  rms simultane-
ously expand into new product lines and lose some of their current product lines to other  rms in
the economy through competition. Each product line faces the same aggregate endogenous creative
destruction rate  :A  rm that loses all product lines to competitors exits the economy.
3.4 Equilibrium
We now characterize the Markov Perfect Equilibria of the economy that make strategies a function
of payo  relevant states only. We focus on the steady state in which aggregate variables ( Y; C; R;
K; w;  q) grow at the constant rate g.
3.4.1 Production
The standard maximization problem of the representative household yields the Euler equation
_Y
Y=_C
C=r : (11)
The maximization problem of the  nal goods producer generates the inverse demand pj=L q 
jk 
j;
8j2[0;1]. The constant marginal cost of producing each intermediate variety is w= q:
The pro t maximization problem of the monopolist jis thus,
 (qj) = max
kj 0 
L q 
jk1 
jw
 qkj 
8j2[0;1]: (12)
19
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 21 -->


Akcigit and Kerr
The  rst order condition for (12) yields an optimal quantity and price for intermediate good j
kj= (1 )  q
w 1
 
Lqjandpj=w
(1 )  q: (13)
The realized price is a constant markup over the marginal cost and is independent of the in-
dividual product quality. Thus, the pro t for each active good is  (qj) = qj, where  
L( q=w)1 
 (1 )1 
  . In order to avoid the case of limit pricing and maintain a simple model,
we adopt the following stage-game assumption.
Assumption 1 (Monopoly pricing) In a given product line j, the current incumbent and any
former incumbents in the same line (with lower quality than the current incumbent) enter a two-
stage price-bidding game. In the  rst stage, each  rm pays a fee of  which is arbitrarily close to
0:In the second stage, all  rms that paid the fee announce their prices.
Under Assumption 1, only the leader pays the fee and enters the second stage since other  rms can
never recover their fee in the second stage. Since the leader is the only  rm bidding a price, the
leader will always operate with monopoly pricing, as in Aghion and Howitt (1992).
The maximization in the  nal goods sector, together with (13), implies a wage rate
w=~  q; (14)
where ~    [1 ]12 . Incorporating the equilibrium wage rate, the constant part of the equi-
librium pro t simpli es to
 =L(1 )~ : (15)
Note that, using the equilibrium quantity (13) and the wage rate (14) ;aggregate output can now
be expressed as as a linear function of production workers Land the average quality   qsuch that
Y=[1 ]12 
 1  qL: (16)
Equations (4), (5) ;(13), and (14) determine the  nal good workers as a fraction of the aggregate
20
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 22 -->


Growth through Heterogeneous Innovations
unit measure of workers,
L= 
(1 )2+ : (17)
3.4.2 Invariant Step-size Distribution and Expected External Step Size
We next compute the invariant step-size distribution 	 ( s) that determines the expected innovation
size from external innovations   s. Let 	kdenote the equilibrium share of product lines with k2N0
subsequent follow-up innovations such that sj=  kj. A steady state equilibrium requires a stable
innovation size distribution. Thus, while the stochastic nature of innovation moves individual
products up and down the kdistribution, the overall share of products at each level kis stable.
This stability requires equal in
ows and out
ows of products from each size level, resulting in the

ow equations:
State :
k= 0 :
k 1 :Inflow
(1	0)  =
	k1 (1 ) =Outflow
	0 (1 )
	k (18)
The  rst line governs in
ows and out
ows among product lines where major innovations have just
occurred. Out
ows happen due to follow-up innovations at the rate  (1 ), while in
ows happen
due to new leading innovations being realized at rate   throughout the innovation size distribution.
Internal R&D within  rms does not in
uence these kdistributions. A similar reasoning governs
the share of product lines with k 1 consecutive follow-up innovations. As a result, 
ow equations
(18) generate the invariant distribution
	k= (1 )kfork 0; (19)
which yields the expected innovation size from external R&D:
 s=E(sj) =1X
k=0	k  k=  
1(1 ) : (20)
This expected size is naturally increasing in the probability of a major innovation  , the realized
size of major innovations  , and for lower decay rates in innovation quality within a technology
cluster (i.e., higher  ).
21
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 23 -->


Akcigit and Kerr
3.4.3 Research and Development by Incumbents
The value functions of  rms determine R&D choices. For simplicity we drop the  rm subscript f
from the  rm variables when it causes no confusion. Consider a  rm with a product portfolio q
which serves as the state variable in the  rm's problem. The  rm takes the values of (r; ;g ) as
given and chooses the optimal R&D e orts xandzjfor everyj2J to maximize the following
value function:21
rV(q)_V(q) = max
x2[0;  x];
fzj2[0; z]gJ8
>>>>>>>>>><
>>>>>>>>>>:X
qj2q2
66664 qj^ z^ 
jqj
+zj[V(qn -fqjg[+fqj(1 + )g)V(q)]
+ [V(qn -fqjg)V(q)]3
77775
+x[EjV(q[+fqj+  qsjg)V(q)]
~ x~  q  q9
>>>>>>>>>>=
>>>>>>>>>>;: (21)
The  rst line on the right hand side represents operating pro ts over currently held product lines
minus internal R&D costs. The second line is the change in  rm value after internal improvements
to currently held products. V(qn -fqjg[+fqj(1 + )g) denotes the  rm value after improving one
of the  rm's existing products by size  . These terms are multiplied by the Poisson arrival rate zj
as the success of internal R&D is stochastic. Firms choose innovation e ort for each product line
separately. The third line shows the change in  rm value due to losing its product lines through
creative destruction  .V(qn -fqjg) denotes  rm value after losing a product that had quality qj.
The fourth line is the change in  rm value after a successful external innovation that garners
a new product line. V(q[+fqj+  qsjg) denotes equilibrium  rm value after a successful external
innovation of size sjthat adds a new product into the  rm's portfolio. This addition is multiplied by
the Poisson arrival rate xas the success of external R&D is stochastic too. The  nal line represents
external R&D costs and  xed costs. The _V(q) term on the left hand side of equation (21)
represents change in  rm value without any material events for the focal  rm due to economy-wide
growth (i.e.,   qchanges).
The aggregate creative destruction rate is the sum of average external innovation e ort by each
21We do not index the portfolio or R&D e orts by fasqf; xfandzj;fto simplify notation. [+indicates the
multiset union operator such that fa;bg[+fbg=fa;b;bg:Similarlyn-indicates the multiset di erence operator such
thatfa;b;bgn -fbg=fa;bg:
22
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 24 -->


Growth through Heterogeneous Innovations
incumbent, Fx, and the realized entry rate xe;
 =Fx+xe: (22)
The aggregate growth rate is determined by the frequency of innovations coming from creative
destruction  , consisting of new entry and external innovations by incumbents; the frequency of
internal innovations z; and their relevant innovation sizes as described in the following lemma.
Lemma 1 Let the equilibrium R&D e orts be given by ( ;z):The steady state growth rate of the
aggregate variables in the economy is
g=  s+z : (23)
Now we are ready to solve for the equilibrium value function. One technical detail needs par-
ticular attention. Our goal in this benchmark model is to generate new intuitions while preserving
tractability. The Klette and Kortum (2004) model is very tractable since everything scales per-
fectly in the number of product lines of the  rms; this includes the pro ts collected by the  rm and
thefranchise value, which is an option value for external innovation arising due to the fact that
more product lines make the  rm more innovative via the Cobb-Douglas R&D technology. In our
baseline model, pro ts also scale perfectly, yet the franchise value is constant across all  rms since
the R&D technology depends on having positive product lines only at the extensive margin but not
on the intensive margin. This introduces a non-linearity to the  rm value function. To generate a
value function that scales perfectly with the number of product lines as in the Klette and Kortum
(2004) model, we assume that the  xed cost of operation is equal to the franchise value as follows.22
Assumption 2 (Perfectly-scaling value function) The value of  xed cost of operation satis es
  =  
~ ~  ~ 
~ 1~  
~ 1 
:
The next proposition shows that the value function (21) and its components can be expressed in
a very tractable form. We assume for now that there is positive entry and later impose a parameter
22The equality simpli es the math for the rest of the baseline model. These technical conditions related to  xed
costs are not important for our general framework, and thus  xed costs are set equal to zero in later sections.
23
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 25 -->


Akcigit and Kerr
restriction that is su cient to verify this condition.
Proposition 1 Under assumptions 1 and 2and when there is positive entry xe>0, the value
function (21) of a  rm with a set of product lines qcan be expressed as V(q) =AX
qj2qqjwhereA
(the value of holding a product line) is
A= 
1 +  s: (24)
Moreover, the optimal R&D decisions are given by
z="
  
(1 +  s)^ ^ #1
^ 1
andx=  
~ ~  1
~ 1; (25)
and the aggregate creative destruction rate is
 =1
(1 +  s)2
4 
A  
^ ^  ^ 
^ 1A1
^ 1^  3
5: (26)
This proposition shows that the innovation e orts of incumbents, both internal and external,
are positively related to the entry cost. Higher entry costs lower entry rates and thus provide longer
expected durations and pro ts from owning product lines. Moreover, both internal and external
R&D e orts decline in their own cost scale parameters.
Importantly, internal innovation is increasing in its own step size  due to higher marginal
return to successful internal improvements, but internal investments are decreasing in the average
step size of external innovation   s, since larger   sencourages more creative destruction that lowers
the expected duration of monopoly power the  rm has on the product line. By contrast, step sizes
do not show up in the equilibrium external innovation rate since a bigger step size   sboth encourages
e ort (due to higher return) and discourages it (due to higher entry); these two opposing e ects
cancel out.
To pin down the entry rate, we solve for the equilibrium measure of  rms F:To achieve this,
we  rst characterize the invariant distribution of the number of products. This distribution is
the main proxy for the  rm size distribution in Klette and Kortum (2004). Let  ndenote the
equilibrium share of the incumbent  rms that own nproduct lines such that  1
n=1 n= 1. The
24
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 26 -->


Growth through Heterogeneous Innovations
invariant distribution again depends upon the following 
ow equations:
State :
n= 0 :
n= 1 :
n 2 :Inflow
F 1 =
F 22 +xe=
F n+1(n+ 1) +F n1x=Outflow
xe
F 1(x+ )
F n(x+n )(27)
The  rst line characterizes outside entrepreneurs (n = 0). In
ows to outside entrepreneurs happen
when  rms with one product are destroyed, and out
ows occur when outside entrepreneurs success-
fully develop a new product at rate xe. Similarly, the second line considers in
ows and out
ows of
 rms with one product, and the third line considers n-product  rms. The next proposition provides
the explicit form solution of the invariant product number distribution.
Proposition 2 The invariant distribution  nis equal to
 n=xe
Fx x
  n1
n!forn 1: (28)
Since (28) is a probability distribution, it must be that  1
n=1 n= 1;which impliesFx
xe=ex
 1:
This condition and (22) deliver the entry rate as
xe= ex
 andF= 
x 
1ex
  
: (29)
The entry rate is a fraction of the aggregate creative destruction rate. In order to ensure an equi-
librium with positive aggregate creative destruction and entry, we make the following assumption.
Assumption 3 (Positive Entry) The parameters of the model are such that
 >  
^ ^  ^ 
^ 1  
1 +  s ^ 
^ 1^ +  
1 +  s:
This assumption is very easy to satisfy. For any given positive pro t, there is always a low enough
entry cost such that an equilibrium with positive entry exists.
25
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 27 -->


Akcigit and Kerr
The total R&D e ort of the economy is
R= ^ "
  
(1 +  s)^ ^ #^ 
^ 1
 q+F~   
~ ~  ~ 
~ 1 q+  ex
  q; (30)
and the total  xed cost is
K=F  q: (31)
Combining (16) and (17) delivers the equilibrium output level,
Y=[1 ]12   
(1 )2+  q: (32)
From this, consumption is determined through the resource constraint as
C=YKR: (33)
We end this section by summarizing the equilibrium.
De nition 1 (Balanced Growth Path Equilibrium) A balanced growth path equilibrium of
this economy consists of the following tuple for every t,j2[0;1]; q;andqj:k 
j; p 
j; w ; L ;
~L ; x ; z 
j;   ; x 
e; F ; R ; K ; Y ; C ; g ;	 
n;   
n; r ;such that: (i)k 
jandp 
jsatisfy (13); (ii)
wage ratew satis es (14) ; (iii)measure of  nal good production workers L satis es (17) and~L 
is simply 1L ; (iv)external (x )and internal (z 
j)innovation 
ows are equal to (25); (v)aggre-
gate creative destruction   satis es (26); (vi)entry 
owx 
eand measure of incumbent  rms F 
satisfy (29) ; (vii) total R&D spending R satis es (30) ; (viii )total amount of  xed cost expenses
K satis es (31) ; (ix)aggregate output Y satis es (32) ; (x)aggregate consumption C satis es
(33) ; (xi) steady state growth rate g satis es (23); (xii) the invariant distribution of innovation
sizes 	 
nsatis es (19); (xiv)the invariant distribution of number of products   
nsatis es (28); and
(xv)the interest rate satis es the Euler equation (11).
26
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 28 -->


Growth through Heterogeneous Innovations
3.5 Central Theoretical Results
The following propositions characterize the  rm growth, R&D, and innovation dynamics of the
model. These closely correspond to the empirical regularities described in the prior section. In our
model, the ideal proxy for  rm size is the total quality Q=P
qj2qqj. This is because  rm sales,
pro ts, and production workers are all proportional to Q.23Firm size also closely relates to the
number of product lines, which we discuss in Section 6.2. Therefore, we also use nfto proxy for
 rm size in propositions when convenient.
Proposition 3 LetG(Q) E 
_Q=Q 
be the average growth rate of a  rm with total quality Q:
ThenG(Q);in equilibrium, is given by
G(Q) =x(1 +  s)  q
Q+z  :
G(Q) is a strictly decreasing function.
This result suggests that small  rms grow faster than large  rms. This micro-founded departure
from Gibrat's law of proportionate growth occurs due to the lack of scaling of external innovation
e orts. As a result, the growth coming from internal innovation is the same on average across
di erent  rm sizes (z ), whereas the contribution of external R&D to  rm growth gets smaller as
 rm size increases (the  rst ratio in G(Q)). Combining these e ects, overall  rm growth declines
with  rm size.
Proposition 4 LetR(Q) R&D=Sales be the  rm R&D intensity of a  rm with total quality Q:
ThenR(Q);in equilibrium, is given by
R(Q) = cx(x)  q
 Q+ cz(z)
 :
R(Q) is a strictly decreasing function.
This result suggests that small innovative  rms have a greater R&D intensity than large  rms.
Similar to the previous proposition, the intuition is that total internal R&D e ort is proportionate
23Sales =P
qj2qfp(qj)k(qj) = [(1 )=w]1 
 LQf,Profits =P
qj2qf qj= Qf, andProduction workers =
P
qj2qflj= [(1 )=w]1
 LQf:
27
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 29 -->


Akcigit and Kerr
to the number of product lines of the  rm. On the other hand, external R&D e orts do not scale
with number of product lines, which results in a declining R&D intensity for larger  rms. In other
words, adding additional product lines continually adds more R&D e ort but further dilutes the
external R&D e ects with respect to intensity measures.
As noted earlier, our model does not require taking a stance on the relative sizes of internal
vs. external innovations. With some structure added that is consistent with our earlier empirical
results, the model also makes predictions about the innovation size distribution and the relative
frequency of  rms by innovation size.
Proposition 5 Let a major innovation be de ned as an innovation with a step size larger than a
certain threshold sk s^kfor some ^k2Z+ands^k>  : Moreover, letM(n)be the probability of
making a major innovation conditional on having a successful innovation for a  rm with nproduct
lines. Then,M(n)can be expressed by
M(n) xP^k
k=0 (1 )k
x+nz=xh
1(1 )^k+1i
x+nz:
M(n)is a strictly decreasing function.
This result suggests that small  rms and new entrants have a comparative advantage for achieving
major advances. Large incumbents endogenously spend e ort on maintaining and expanding exist-
ing products. Thus, while  rms of all sizes obtain major advances, these major advances account
for a smaller share of achieved innovations among larger  rms.24An important distributional im-
plication of Proposition 5is that these di erences weaken when considering progressively larger
thresholdss^k. The comparative advantage is weakest at the most extreme values (i.e., s^k=0= ).
We empirically estimated these predictions in Section 2.2and we use these results in our quan-
titative analysis. The baseline model makes many more predictions that we catalogue in Appendix
Band investigate further in our NBER working paper (Akcigit and Kerr, 2010).
24The aggregate quantity of major innovations by small and large  rms depends upon these propensities and the
 rm size distribution.
28
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 30 -->


Growth through Heterogeneous Innovations
4 Generalized Model
This section generalizes the innovation production function of the benchmark model. In particular,
we assume that the production function for external innovations takes the form
Xn= [Rx= q] n : (34)
This production function nests two special forms. First, when  = 1 ;the model becomes the
extended Klette and Kortum (2004) framework where both internal and external investments scale
up with  rm size on a one-for-one basis with added product lines. Second, when  = 0; we are
back to the benchmark model of Section 3. We describe here the solution of the model under this
generalized production function, and Section 6quanti es this model and the  parameter.
The static equilibrium of this generalized model follows exactly as the benchmark model, there-
fore we skip it (equations (13) (17) hold identically). Moreover, when   > 0;a  rm that loses
all of its product lines exits the economy. As we are not seeking analytical results, but instead
preparing the general model for quanti cation, we eliminate the  xed cost and set   = 0 :
4.1 Research and Development by Incumbents
The production function in (34) delivers the R&D function
Rx=  q~ n~ x~ 
n;
wherexn Xn
nis the innovation intensity per product line and
~  1 
 ;~   1
 ;and ~  1
 :
In this case, the value function can be expressed as follows.
Proposition 6 For a  rm that has a quality portfolio q;the value function has the following form:
V(q; q) =AX
qj2qqj+Bn q
29
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 31 -->


Akcigit and Kerr
where
(r+ )A= +A^ 
^ 1  
^  ^ 
^ 1 
^ 1 
^ 1
1^ ; (35)
and
Bn+1= ( +n )Bnn Bn1
~ 1 ~ 1
~ ~ ~ 1
~ n~ ~ 
~ +BnA[1 +  s]: (36)
Moreover, the optimal innovation e orts are de ned as
zj= A 
^ ^  1
^ 1andxn= A[1 +  s] +Bn+1Bn
~ n~ 1~  1
~ 1: (37)
In this generalized model, the value function consists of two parts. The  rst part, which is
denoted by A;is related to the discounted sum of future pro ts and internal innovations. By
owning the product line, the  rm will collect 
ow pro ts of  qjuntil it is replaced at the rate  :In
addition, the  rm can improve its quality qjthrough internal innovations at the rate zj, which also
provides value to the  rm. The second part, which is denoted by Bn;relates to the  rm's external
innovation capacity. By owning a product line, the  rm has a franchise value of extending into new
product lines through external innovations, which happens at the rate xn:Since the production
function is dependent on the number of product lines, this franchise value now is a function of n
as well. The Klette and Kortum (2004) model corresponds to Bn=nB;while the baseline model
of Section 3corresponds to Bn=B:
Accordingly, the new 
ow equations for the fraction of  rms with nproduct lines:
State :
n= 0 :
n= 1 :
n 2 :Inflow
F 1 =
F 22 +xe=
F n+1(n+ 1) +F n1(n1)xn1=Outflow
xe
F 1(2x2+ )
F n(nxn+n )
This summarizes the generalized model, and a  nal remark is in order.
Remark 1 Proposition 6shows that innovation intensity xncan be expressed as xn=n f(n),
where
   + 1
1 (38)
30
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 32 -->


Growth through Heterogeneous Innovations
andn captures the direct e ect of nonxn. Note that f(n) =h
A[1+ s]+Bn+1Bn
~ ~ i1
~ 1captures the
indirect e ect of number of product lines on xnthrough its impact on the franchise value Bn:When
 + = 1; our model mirrors Klette and Kortum (2004) with f(n)equal to some constant, whereas
innovation intensity will be decreasing in  rm size when  +  <1. Therefore  + dictates the
amount of decreasing innovation intensity in  rm size.
5 Patent Citation Behavior and Innovation Spillover Sizes
We now incorporate patent citation behavior across innovations into our benchmark model. As
we have already de ned the economy's equilibrium, our speci ed citation behavior does not a ect
real outcomes. We undertake this extension, however, to derive the economic meaning behind
patent citations. This in turn allows us to quantify the model using richer data. Second, this addi-
tion demonstrates how this class of endogenous growth models captures many important features
uncovered in the empirical literature on patent counts and citations.25
Forward Patent Citations Innovations are clustered in terms of their technological rele-
vances. Major innovations generate new technology clusters that last until they are overtaken by a
subsequent major innovation. An example of the sequential innovation process was illustrated in
Example 1 in Section 3.2.
Letm(j;t) be the number of patents in the active technology cluster in product line j:For
instance, if tis between the innovation times of P3andP4in the Example 1, then m(j;t) = 3, or
iftis between P11andP12;thenm(j;t) = 2. Therefore the number of citable patents in active
technology clusters at time tisM(t) =R1
0m(j;t)dj.
We next describe the citation distribution of patents by specifying citation behavior with rules
that are consistent with the patent literature. Patents cite previous patents within the same
technology cluster to specify how they build upon the prior work and the boundaries of the inno-
vations. Each new patent, by de nition, improves the previous technologically relevant innovations
on some dimensions. However, not all subsequent innovations improve an existing technology in
the same direction. Therefore major patents with broader scope are more likely to be cited by
25Hall et al. (2001) provide a comprehensive introduction to patent citations. See also Hall et al. (2005), Ja e et
al. (2000), Ja e et al. (1993), Thompson and Fox-Kean (2005), and Trajtenberg (1990).
31
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 33 -->


Akcigit and Kerr
subsequent follow-on patents (e.g., Lerner, 1994). We proxy this patent scope by the step size
s2 
 ;  kjk2N0	
in our model. We assume that an innovation with size swill receive a
citation from a subsequent patent within the same technology cluster with probability s
where

2(0;1= ):Finally a major innovation replaces the previous cluster. Thereafter, future citations
begin with the new major innovation. Empirically, Hall et al. (2001) andMehta et al. (2010)
quantify the decline in relative citation rates over patent age that this model structure provides.
The citation behavior of Example 1 is illustrated in Table 2.
[Table 2 Here]
With these simple modeling assumptions, we can characterize the 
ow properties of citation
behavior. These traits depend upon the real side of the economy and provide a richer description of
it. Our upcoming quantitative analysis uses the citation distribution to inform the traits of internal
and external innovation. Similar to our earlier expressions, the economy's equilibrium requires an
invariant citation distribution. Let   sk;nand   ;ndenote the share of patents that are of size   k
and , respectively, and receive ncitations. These shares include all patents and naturally sum to
one when aggregating over all levels of citation counts,  1
n=0  ;n+  1
k=0 1
n=0 sk;n= 1. The next
proposition provides the explicit form solutions for these distributions.
Proposition 7 The invariant distribution of the total number of forward citations (n)given to a
patent of size s2f ;skjk2N0gcan be expressed as
 s;n=  s;0
n
sforn2N0;
whereM=x+z
x ; sk;0= (1 )k 
M[  +
sk( (1  )+z)];  ;0=z
M[  +
 (  (1  )+z)]and
s 
s( (1 )+z)
  +
s( (1  )+z):
Similarly, the invariant distribution of the total number of external forward citations is
~ s;n=~ s;0~
n
sforn2N0;
where ~ sk;0= (1 )k 
M[  +
sk (1  )];~  ;0=z
M[  +
   (1 )]and~
s 
s (1 )
  +
s  (1 ):
This proposition shows the information available from citation distributions. As   gets smaller in
the denominator,   s;ngenerates a more highly skewed distribution of citations. This is intuitive as
32
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 34 -->


Growth through Heterogeneous Innovations
a slower arrival of new technology clusters tilts innovation towards follow-on inventions that cite
prior inventions and thereby generate more extreme citation counts. Patent citation distributions
can thus be used to discipline the traits of innovation in the economy that would otherwise be
unobservable.
6 Quantitative Analysis
We estimate our model using micro data described in Section 2.2. Section 6.1describes our iden-
ti cation strategy. Section 6.2provides the main estimation results, and Section 6.3provides
robustness checks. Appendix Doutlines the computational solution of the generalized model.
6.1 Identi cation
Our model has 13 structural parameters as listed in Table 3.
[Table 3 Here]
We identify these parameters in three ways. First, we  x three parameters (  ;^ ;~ ) using val-
ues developed in Section 6.1.1 from the literature and R&D-based regressions. Second, we use the
observed distribution of patent citations to pin down three elements of the step size distribution
( ; ; 
 ) in Section 6.1.2. Finally, for the remaining parameters and to parse  
, we target the
relevant  rm moments in the data. One critical part of this third step is to identify the key decreas-
ing returns parameter  using an indirect inference approach, where we replicate the regressions of
Sections 2.3-2.4 using data simulated from the model.
6.1.1 Externally Calibrated Parameters
We set the discount rate equal to  = 2%, which roughly corresponds to an annual discount factor
of 97%.
We rely on prior literature for estimates of the curvature of the R&D cost function, which we
will set equal across internal and external innovation ^ =~ (the model retains shifters in these
cost functions). One line of studies quanti es the elasticity of patents to R&D expenditures (e.g.,
Griliches, 1990, Blundell et al., 2002, Hall and Ziedonis, 2001). This literature often concludes this
33
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 35 -->


Akcigit and Kerr
elasticity is around 0.5, which implies a quadratic curvature  = 2. Acemoglu et al. (2013) reach a
similar estimate using the Census Bureau data as well when focusing on  rms in the R&D Survey.
The second set of papers examines the impact of R&D tax credits on the R&D expenditure of
 rms (e.g., Hall, 1992, Bloom et al., 2002, Wilson, 2009). In a survey of this literature, Hall and
Van Reenen (2000) conclude that a tax price elasticity of around unity is typically found, which
again corresponds to a quadratic cost function.26Given this common  nding, we set ^ =~ = 2:
Section 6.3.4 will study the robustness of the results with alternative elasticities of 0.4 and 0.6.
6.1.2 Citation Distribution
Our model yields an analytical solution for the patent citation distribution that is dictated by the
innovation step-size parameters. In particular, when we focus only on external citations ( zj= 0);
the distribution of patents that are of quality skand receive ncitations is simply
 sk;n=  sk;0
n
skforn2N0;
where  sk;0= 2(1 )k
 +
  k(1 )and 
sk 
sk(1 )
 +
sk(1  ): sk;ngives us the joint distribution of patents
that arek-times incremented and have received ncitations. Our model provides the analytical
distribution of k-times incremented patents from (19) as 	 k= (1 )kfork 0:Hence, we can
 nd the marginal distribution of n-times cited patents as
Fn( ;
; ;  ) =1X
k=0	k sk;n:
The empirical tractability comes from the fact that the distribution of n-times cited patents depends
only on four structural parameters:  ;
; ; : Citation distributions do not allow one to distinguish
between the overall quality level of external inventions (  ) and factors that govern the general
tendency of patents to cite each other ( 
). Since
and always appear multiplicatively in the
shape of the citation distribution, we can use these data to identify the three parameters  ; ; and
26The mapping to our setting is straightforward. To simplify the notation, let us denote a single R&D spending rela-
tionshipR=Px 
nFn, wherePis the price of R&D and Fnis a multiplicative term that can potentially depend on  rm
size. If the return to innovation is  , the generic maximization problem can be written as max xn 
xn Px 
nFn	
.
Solving for the  rst order condition, R=P1
 1F1
 1
n [ = ] 
 1:Hence the price elasticity of R&D spending in
our model corresponds to dlnR=dlnP=1
 1. A unitary estimate corresponds to  = 2:
34
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 36 -->


Growth through Heterogeneous Innovations
the combined  
.
[Figure 7 Here]
Figure 7 plots the empirical distribution together with the model-generated citation distribution.
The model does a very good job in replicating the data.
Table 4 lists the resulting parameter estimates. Roughly 10% of external innovations are found
to be signi cant enough to open new technology clusters, and the decay rate  for the quality
of external inventions is fairly modest. The 
 estimate suggests that patents that open a new
technology cluster have a 75% probability of being cited by later patents in the cluster.
[Table 4 Here]
6.1.3 Indirect Inference
There are seven remaining parameters to be estimated:  ;~ ;^ ; ; ; ; ; which will also identify

based upon the estimate in Table 4. We identify these parameters using an indirect inference
approach in the spirit of Lentz and Mortensen (2008). We compute various model-implied moments
from the simulation strategy described above and compare them to the data-generated moments
to minimize
min7X
i=1jmodel (i)data (i)j
1
2jmodel (i )j+1
2jdata (i)j;
where we index each moment by i:Our indirect inference procedure targets seven moments that
we describe next. The generalized model does not yield an analytical solution, and thus we cannot
express the targeted moments in this form. However, we build intuition by using the analytical
solutions to Section 2's benchmark model to guide us in choosing the right moments for identi ca-
tion. For ease of these depictions, we abstract from quality levels by setting qj= 1;8j;although
innovation qualities are clearly included in the simulation of the general model.
Average Pro tability For both the benchmark and generalized models, the pro t-to-sales ratio
is equal to E(profitf=salesf) = (1 )2 1
 ~ 1
 , where ~    [1 ]12 :We therefore target
the average pro tability in the economy to help identify  :The pro t-to-sales ratio in the model
35
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 37 -->


Akcigit and Kerr
includes R&D expenditures, and thus we combine annual published BEA pre-tax pro t rates with
industrial R&D expenditure rates to determine an estimate of 10.9% for the 1982-1997 period.
R&D Intensity and Internal-to-External Citations Ratio We discipline the R&D scale
parameters ^  and ~ through measures of R&D intensity and the citation ratio of internal vs.
external innovations. Aggregating across  rms and using Proposition 4, the baseline model shows
the economy-wide R&D-sales ratio to be a linear combination of ^  and ~ :This ratio is 4.1% in our
sample.27In addition, the citation ratio of internal vs. external innovations informs the R&D scale
parameters as
 ~ 
(1 +  s) ^ :
We de ne internal patents as those with 50% or more of citations given being to assignees of the
same  rm. This approach is similar to Figure 3, with the explicit ten-year window from application
date ensuring that the procedure is consistent across the sample period. We estimate this ratio
using external citations to be 0.774 (= 5 :023=6:488). These data inputs will inform the R&D scale
parameters.
Fraction of Internal Patents and Aggregate Growth Rate Our model has four parameters
that govern the step-size dynamics:  ; ; ; : We previously identi ed  and through the citation
distribution. The remaining two parameters are the step size for internal innovations  and the step
size of radical innovations  :Step sizes determine both the innovation incentives and the aggregate
growth rate:
zj="
  
(1 +  s)^ ^ #1
^ 1
andg=   s+z  :
27For this purpose, we need to make use of the R&D Survey, which samples with certainty  rms that conduct
more than $1 million dollars of R&D and subsamples  rms beneath this threshold. Our  rst step builds a sample of
 rm-period observations for which we observe reported R&D, sales, and employment. The  ve-year periods match
those of our core sample. We then merge in patents, including zero-valued outcomes. From this, we obtain an average
conversion factor for relating R&D/sales to patents/employee. The second step applies this conversion factor to our
full sample, where our aggregate patent/employee statistic includes  rms that did not patent. This procedure gives
us an aggregated value that closely aligns with other estimates of R&D/sales ratios. These values are determined
through aggregates over the whole sample, not  rm-level imputations. As the largest companies account for the
substantial majority of these variables and will be surveyed directly by the R&D Survey, the procedures used here
are quite robust.
36
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 38 -->


Growth through Heterogeneous Innovations
We can therefore discipline  and by targeting the fraction of internal patents 
z
z+  
and the
growth rate. The internal patent share is 21.5%. The aggregate growth rate is calculated in de
ated
terms and on a per employee basis to match the model and the BEA pro t estimates. This ranges
from 0.91%-1.03% depending upon details of the calculation, and we assign a value of 1.0%.
Entry Rate The entry rate in the benchmark model is xe= exp (x=  ):Equations (24) and
(26) show that the creative destruction rate is decreasing in the entry cost parameter  ,d =d  < 0;
and equation (25) shows incumbent e orts are increasing in entrant costs, dx=d  > 0:Therefore
the impact of entry cost on the 
ow of entry is strictly negative, dxe=d  < 0, and thus targeting
the entry rate can help inform the entry parameter. The entry rate in our data is 5.82%, measured
over  ve-year intervals through employments among patenting entrants.
Firm Growth vs. Firm Size Regression from Section 2.3 The extended Klette and Kortum
(2004) approach, where  = 1 , predicts that the unconditional  rm growth would be independent
of  rm size, whereas the benchmark model with  = 0 goes to the other extreme and predicts that
 rm growth is decreasing in  rm size. In order to identify the actual value of  ;we mirror the same
growth-size regressions with data generated from the simulated model. Every  rm in the model has
an innovation, as they would otherwise not exist, and we treat sample preparation and estimation
exactly as we do in the data sample. The empirical coe cient of interest from the earlier analysis
is -0.035.
6.2 Benchmark Estimation Results
Table 5 reports the empirical and simulated moments using the generalized model.
[Table 5 Here]
Overall, the model matches closely the targeted moments. The resulting parameter estimates
are reported in Table 6.
[Table 6 Here]
37
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 39 -->


Akcigit and Kerr
Our estimates  nd that there are some decreasing returns in  rm size for external innovation
as captured by the value of   0:4:Among the other results, the ratio of ~  to ^ suggests that the
R&D cost parameter for external innovations is about 12 times larger than for internal innovations.
External innovations that open up a new technology cluster are estimated to have more than twice
the potency of internal innovations. With the decay rate of  = 0:929, roughly ten follow-on
external innovations occur before external innovations are less valuable than internal innovations.
6.2.1 Characterization of the Economy
To provide further intuition on how  plays a role in generating size-dependent  rm moments,
Figure 8plots the franchise value function of a  rm Bnas a function of the number of product lines
nwhen 2f0; 0:2;0:4;0:5g:Figure 9similarly plots the resulting external innovation intensity
Xn. The franchise value function Bnfor the baseline model in Figure 8is 
at because external
innovation does not scale, while it grows linearly in the Klette and Kortum (2004) scenario. The
small dashed line shows that the franchise value with  = 0:4 grows similarly to the Klette and
Kortum (2004) framework among smaller  rms, with more modest departures after that. Figure 9
likewise illustrates that external innovation intensity declines with  rm size but stabilizes in a way
that limits the full dilution in the baseline model.
[Figure 8 & 9 Here]
In our model,  rm size is determined by the combination of the number of product lines and
their quality distributions. Figure 10illustrates the very tight correspondence of product lines to
 rm size in our model, with the latter normalized to the average quality level in the economy, which
builds additional connections and intuitions to the frameworks of Klette and Kortum (2004) and
Lentz and Mortensen (2008).
[Figure 10 Here]
Figure 11demonstrates that our framework generates an invariant product-line distribution at
the  rm level that resembles an exponential distribution. Combined with the quality margin, the
38
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 40 -->


Growth through Heterogeneous Innovations
invariant  rm size distribution is illustrated in Figure 12. Similar to prior papers, the tails of the
sales distribution in our model are not as fat as in the data.28
[Figure 11 & 12 Here]
6.2.2 Growth Decomposition
We now use the structure of our model to document the sources of growth. In our model, growth is
driven by (i) new entrants, (ii) incumbents doing internal innovations on their existing lines, and
(iii) incumbents expanding into other lines through external innovations:
g=xe s
|{z}
entry+1X
n=0F nXn s
|{z}
incumbent external+z 
|{z}
incumbent internal:
Table 7 reports the magnitudes of each of these components in our model.
[Table 7 Here]
Our model estimates that 26% of aggregate productivity growth is driven by new entry. Of the
three-quarters of productivity growth that comes from the action of incumbent  rms, the majority of
it depends upon external innovation e orts of  rms. These  gures are consistent with the empirical
 ndings surveyed by Foster et al. (2000), recognizing that some of our external innovation e ect
would be viewed as entry/exit in prior empirical calculations.
Another important distinction between external innovation and internal innovation is the di er-
ential impacts on qualities. The average step size associated with external innovations is   s= 0:069;
whereas the step size of internal innovation is  = 0:051, which implies that an average external
innovation has 35% (= 0:069=0:051 1) higher impact than internal innovation.
An interesting implication of the estimated model is that it costs more for large  rms to produce
major innovations. To see how big this additional cost is, let us de ne a cost multiplier K(n) :
K(n) Rx(xnjn)=n
Rx(xnj1)
28See Gabaix (2009) for an excellent review of the literature on  rm size distribution.
39
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 41 -->


Akcigit and Kerr
whereRx(xnjn) is the cost of producing major innovations at the rate  xn. Note that this
cost multiplier captures the additional percentage cost of producing the same amount of major
innovations per product line. Simple algebra shows that the cost multiplier can be expressed as
K(n) =n~ 1=n1  
 :
Figure 13 plots the cost multiplier according to our parameter estimates. This  gure, together with
Figure 11, indicates that a  rm at the 90th percentile pays 25% more compared to a one-product
 rm. Likewise, a  rm that is at the 99th percentile pays 45% more on average. Therefore an
important takeaway from our estimates is that even a small departure from constant returns to
scale (  + = 0:9) could result in sizable increase in innovation cost with  rm size.
[Figure 13 & 14 Here]
Finally, Figure 14plots the fraction of major advances in a  rm's innovation portfolio  xn=(xn+z)
against  rm size. Moving from a median-sized  rm to a 90th percentile  rm reduces the fraction
of major advances by around 10%; the decline is 16% when we move to a 99th percentile  rm.
6.2.3 Comparison of Untargeted Moments
We next compare our quanti ed model against untargeted features of the data. We do this through
nonparametric regressions that compare variables across the  rm size distribution. We include
indicator variables by  rm size quintile, with the smallest  rm size category serving as the reference
group. Our model estimation only targets the annual linear relationship for  rm size and growth,
and so the degree to which we observe comparable patterns for other variables across the  rm
size distribution provides con dence in the model's performance. For the exercises, we use the
continuous innovation sample in both datasets so that all variables are de ned and the samples
remain consistent over tests. We structure our model simulation such that the model-developed
data (n = 16; 371) has comparable statistical properties to our Census Bureau data ( n= 16; 818).29
29We continue to organize our sample around  ve-year blocks. The three periods included in the regressions
are 1978-1982, 1983-1987, and 1988-1992, and we use earlier and later data to calculate variables as required. In
estimations with Census Bureau data, we include  i;t xed e ects for the industry iand yeartof the  rm. Industries
are assigned to  rms at the two-digit level of the Standard Industrial Classi cation system using industries in which
 rms employ the most workers. All estimations cluster standard errors at the  rm level and are unweighted.
40
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 42 -->


Growth through Heterogeneous Innovations
Table 8 considers four main variables for which we have provided initial empirical evidence thus
far.
[Table 8 Here]
On all four dimensions, the model closely matches the data in terms of the direction of di erences
across the  rm size distribution: slower growth, lower patents per employee, higher share of patents
being internal, and a lower share of patents being in the top 10% in terms of external impact. The
model predicts a larger  ve-year growth di erential between the smallest quintile and the second
quintile than present in the data, but the di erences for larger quintiles are quite similar. Patents
per employee are very similar in levels and direction. The model under-predicts the initial rise in
internal patent shares present in the data, but the e ects for the largest quintiles are very close.
Finally, the model under predicts the steepness of the decline in top/radical patents, but otherwise
shows a very similar coe cient pattern.30Overall, these results are very encouraging given that
the model has not been targeting these  rm size distribution components or time dimension.
Table 9continues with this approach and considers the patent quality distribution more broadly.
We calculate the share of patents for each  rm-period that fall within the indicated quartile of the
quality distribution. In the data, these quality distributions are measured through external citations
relative to the application year and technology of the patent. The model again performs quite well
in this untargeted test. Perhaps most striking, the model correctly predicts the disproportionate
mass of patents for the largest  rms falling within the second quality quartile, and it gets the
relative size of this e ect very close to the data. This part of the distribution is where internal
patents sit and is a very distinctive piece of the framework developed in this paper. The model also
correctly predicts that most of this extra mass is being shifted from the top quartile of external
impact.31
[Table 9 Here]
30The model coe cients are not statistically di erent from zero for the last column. In unreported estimations,
we develop a larger model sample of 152,089 data points, where we  nd a largest quintile impact of -0.0071 (0.0017).
Thus, our attention focuses mainly on the coe cient magnitudes between the model and data, versus statistical
precision. The complete results for Tables 8-10 with the larger sample are available upon request and are very similar
to those reported.
31The largest  rms in Panel B also show some modest mass at the lowest quartile. In the model, the constant
internal step size  concentrates the internal e ect into a single quartile. The fact that we overall match the quality
distribution so well indicates that this simplifying structure is a reasonable approximation.
41
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 43 -->


Akcigit and Kerr
Table 10  nally compares  rm-level growth regressions in the model and data. These tests
evaluate whether the micro-dynamics of  rms behave similarly as we consider all elements to-
gether. We use the continuous innovator samples and  ve-year periods. The central regressors to
explain employment growth to the next period are the  rm's current employment, the  rm's total
patenting in the period, the quality distribution of the  rm's own patents in this period (Patent
Quality Share f;q), and the share of a  rm's patents that are internal in nature (Internal Share f;q).
Speci cations take the form
EmpGrf;t= i;t+
Eln(Empf;t) +
Pln(Patents f;t) +X
q2QP( q Patent Quality Sharef;q)
+X
q2QI( q Internal Share f;q) + f;t;
wherefandtindex  rms and  ve-year periods. The set of patent quality quartiles QPare indexed
byqand we measure e ects relative to the lowest two quality quartiles. For internal patents, we
de ne indicator variables for internal patents being a (0, 20%] share of the  rm's total innovation
during the period or greater than 20%.
[Table 10 Here]
On the whole, the model and data display very similar properties at the micro-level. Firm
growth is increasing in total patents, increasing in the share of these patents falling in the upper
half of the distribution, and decreasing in the share of the patents that are internal in nature. The
data tends to show greater growth e ects with patent quality than the model for the very top
quartile, but most of the coe cient magnitudes are quite comparable. In the last column, we use
patent claims to measure quality and  nd comparable results.32
Appendices C.2andC.3report additional data analyses that con rm features present in the
model. C.2shows that the patents that  rms develop in their  rst two years of existence have
higher external impact than those subsequently developed by the same  rm. C.3shows that the
external innovation that builds on a particular invention tends to have greater forward impact than
32While citations are the more commonly used measure, there is some concern that  rm growth or survival could
in
uence future external citations (e.g., out of fear of litigation). We thank a referee for pointing out this feature,
which is not directly testable as quality would be observationally similar. Claims provides a check against this
concern.
42
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 44 -->


Growth through Heterogeneous Innovations
the internal innovation that also builds on the same invention. These two features are distinctive
elements of our model structure that are important to con rm in the data. Our NBER working
paper also provides additional empirical elements that support the model's features. We show, for
example, that the external citation distributions that exist for an external patent do not depend
upon the size of the  rm making the patent. This invariance provides support for our model's
structure that relates  rm size to choices over types of innovations, rather than  rms of di erent
sizes having inherently di erent capacities for producing high-quality innovations.
6.3 Robustness
This section considers robustness checks that extend the moments used to estimate parameters.
Across these upcoming variations, we continue to conclude that  + = 0:9 is a good estimate for
the level of decreasing returns to external innovation in  rm size.
6.3.1 Adding Fraction of Top Innovations as a Target
Our model predicts that the fraction of major innovations in a  rm's portfolio tends to be decreasing
in  rm size if external innovation does not scale one-for-one. This theoretical prediction was
empirically veri ed in Section 2.5, and we used this as an untargeted moment to assess the model.
As an alternative exercise, we introduce this empirical moment as an additional target. Table 11
reports the new moments and the new estimate of  :To save space, the rest of the parameter
estimates are not reported.
[Table 11 Here]
The model replicates both facts very closely, while also preserving the goodness of  t with the rest
of the moments. The resulting estimated  value is very similar at 0.395.
6.3.2 Adding Patent per Employment as a Target
Table 12further incorporates the normalized patents per employment regression coe cient as an
additional target.
[Table 12 Here]
43
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 45 -->


Akcigit and Kerr
While the  t of the  rst two facts declines with this augmented model, all three relationships
are still captured. Most important, the scaling estimate  = 0:407 remains robustly identi ed.
6.3.3 Alternative Growth Cap
The major moment in
uencing  in the benchmark estimation in Table 5is the empirical relation-
ship between  rm size and growth. To con rm these results are not sensitive to the winsorization
imposed, in Table 13we keep all parameters at their baseline levels and re-estimate  with the
maximum growth rate of 3000%, versus 1000% in our baseline.
[Table 13 Here]
This adjustment lowers  to 0:384, which is intuitive given that the weaker winsorization allows
us to pick up even more abnormal growth for smaller  rms, but the in
uence on our results is
overall quite modest.
6.3.4 Alternative R&D Elasticities
Table 14studies the robustness of our results to alternative estimates of the R&D elasticity, centered
on the = 0:5 elasticity from the micro studies (see the discussion in Section 6.1.1). Panel A
considers a lower value of  = 0:4, whereas Panel B considers a larger value  = 0:6.
[Table 14 Here]
The model continues to replicate the targeted moments well. The remarkable result is the
robustness of the sum of the elasticity parameters  +  0:9;which conforms to benchmark
estimates.
7 Conclusion
Firms come in many shapes and sizes, as do their innovations. An important step for research
on the origins of innovation and endogenous growth is to build an apparatus that can handle
more of this  rm-level heterogeneity; it is equally important to discern when this apparatus adds
value commensurate with its extra complexity. This paper takes a step forward on both of these
44
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 46 -->


Growth through Heterogeneous Innovations
dimensions. First, our model allows for internal and external innovations, links  rm innovation
choices to  rm size, and traces out consequences of these di erences for  rm-level dynamics and
aggregate growth rates. The model remains tractable with these added ingredients, laying bare
some economic factors that can lie behind empirical regularities like deviations from Gibrat's Law
or the disproportionate representation of small  rms and start-ups among the producers of major
innovations. We also quanti ed a generalized form of our model using U.S. data from the Census
Bureau for 1982-1997,  nding that decreasing returns to external innovation in larger  rms to be
an important but not a radical departure from the perfect scaling of the Klette and Kortum (2004)
framework.
Amongst these contributions, our paper is also quite novel in how it layers on patents and
citations across patents to inform the model behavior, building on prior work like Caballero and
Ja e (1993) and Eeckhout and Jovanovic (2002). Indeed, estimations of our model and the scaling
parameters would not have been possible otherwise. This work also allows us to conclude that
growth impacts of external innovation have exceeded internal innovation for the recent U.S. econ-
omy, which in turn helps identify some of the special role that small, innovative  rms and new
entrants can play in economic growth. There is great potential for further developing this link of
patents and patent citations and the information they contain into growth models. Our frame-
work is a natural launching point for estimating the role of intellectual property protections for the
incentives to innovate and the subsequent trade-o s that come with monopoly rights. As second
example, one could follow inventors out of large incumbent  rms and into the formation of new
companies to study the role of spawning new  rms in economic growth and the implications of
regulations like non-compete clauses. Growth models can garner greater insights and realism by
layering information similar to patents and citations that can be studied in both the model and
data.
45
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 47 -->


Akcigit and Kerr
Appendix
A Proofs of Propositions
Proof of Lemma 1. Note thatY = (1 )12 
 ~  1
 L  q:Therefore the growth rate of aggregate
output is equivalent to the growth rate of the average quality of product lines. We can express the
level of  q(t) after an instant  t as
 q(t+  t) =8
><
>: q(t) [   t(1 +  s) +z  t(1 + )]
+ q(t) [1   tz  t]9
>=
>;:
Now subtract   q(t) from both sides and divide by   tand take the limit as  t !0
g=  q(t)
 q(t)= lim
 t!0 q(t+  t) q(t)
 t1
 q(t)=   s+z  :
Proof of Proposition 1.Conjecture that
V(q) =AX
qj2qqj: (39)
Substituting this expression into the original value function,
r AX
qj2qqj= max
x;[zj]j2Jf8
>>>>>>><
>>>>>>>:X
qj2q  qjX
qj2q^ z^ 
jqj  q
~ x~  q+xA q(1 +  s)
+X
qj2qzjAqj X
qj2q  Aqj9
>>>>>>>=
>>>>>>>;:
46
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 48 -->


Growth through Heterogeneous Innovations
This expression holds if and only if
r A= max
zn
  ^ z^ +zA   Ao
;and (40)
max
xn
xA(1 +  s)~ x~ o
  = 0: (41)
Assume for now that there is positive entry (we will verify this later in the proof). Then from
the free-entry condition (10) we have
A= 
1 +  s: (42)
The maximization in (40) implies z=h
A 
^ ^ i1
^ 1or
zj="
  
(1 +  s)^ ^ #1
^ 1
and
 = 
A+ ^   
^ ^  ^ 
^ 1A1
^ 1 
^ 1 
g ;
where the last line used the fact that r=g+ :Since the growth rate is g=  s+z ;the above
expression can be further re ned as
 =1
(1 +  s)2
4 
A  
^ ^  ^ 
^ 1A1
^ 1^  3
5:
Now we turn to the maximization problem in (41) which delivers the optimal innovation e ort
(together with (42)) as
x=  
~ ~  1
~ 1:
Hence the condition in (41) is
max
xn
xA(1 +  s)~ x~ o
= v
~ ~  ~ 
~ 1~  
~ 1 
:
Hence assumption 2 guarantees (41).
47
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 49 -->


Akcigit and Kerr
Proof of Proposition 2.Conjecture the form   
n=~A~Bn1
n!:Then the 
ow equations in (27)
imply
F~A~B2 +xe=F~A~B(x+ )
and
~B2 =~B(x +n  )nx:
Combining these two equations implies
F~A~Bn  F~Anx +xe=F~A~B :
This equation can hold for all n 2 if and only if ~B=x= and ~A=xe
Fx:
Proof of Proposition 3. Firm growth is equivalent to the growth of Qf:After a small time
interval, the quality index will be on average
Qf(t+  t) =8
>>>><
>>>>:x t[Qf(t) +  q(1 +  s)] +P
qfz t[Qf(t) + qf]
+ (1x tnfz tnf  t)Qf(t)
+P
qf  t(Qfqf)9
>>>>=
>>>>;:
Then after some algebra the expected growth rate of a  rm is
G(Qf) = lim
 t!0Qf(t+  t)Qf(t)
 tQf=x q(1 +  s)
Qf+z  ;
which is decreasing in Qf:
Proof of Proposition 4.Immediate from the text.
Proof of Proposition 5.The total probability of having an innovation during   tisx t+
nfz t:The probability of having a major innovation with sk s^k>   ish
1(1 )^k+1i
x t:
Then the probability of having a major innovation conditional on a successful innovation is the
ratioh
1(1 )^k+1i
x t= (x t+nfz t):
48
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 50 -->


Growth through Heterogeneous Innovations
Proof of Proposition 6.Note that the new value function in general form is
rV(q)_V(q) = max
xn2[0; x];
fzj2[0; z]gJf8
>>>>>>>>>>>><
>>>>>>>>>>>>:X
qj2qh
 qj^ z^ 
jqji
 q~ n~ x~ 
n
+nxn 
EjV(q[+fqj+  qsjg)V(q) 
+X
qj2qzj[V(qn -fqjg[+fqj(1 + )g)V(q)]
+X
qj2q [V(qn -fqjg)V(q)]9
>>>>>>>>>>>>=
>>>>>>>>>>>>;:
Substituting the conjecture V(q; q) =AX
qj2qqj+Bn qinto the above value function we get
rX
qj2qAqj+rBn qBn qg= max
xn2[0; x];
fzj2[0; z]gJf8
>>>>>>>>>>>>>>><
>>>>>>>>>>>>>>>:X
qj2qh
 qj^ z^ 
jqji
 q~ n~ x~ 
n
+nxn2
64A q[1 +Ejsj]
+Bn+1 qBn q3
75
+X
qj2qzjAqj 
+X
qj2q [Aqj+Bn1 qBn q]9
>>>>>>>>>>>>>>>=
>>>>>>>>>>>>>>>;:
Now equating the terms with qjand  qwe get
rA= max
zjn
 ^ z^ 
j+zjA  Ao
and
rBnBng= max
xn8
>>>><
>>>>:n~ ~ x~ 
n
+nxn[A[1 +Ejsj] +Bn+1Bn]
+n  [Bn1Bn]9
>>>>=
>>>>;:
49
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 51 -->


Akcigit and Kerr
Note that from log utility we have  =rg:Hence the two value functions become
rA =  A+ max
zjn
zjA ^ z^ 
jo
 Bn= max
xn8
>>>><
>>>>:n~ ~ x~ 
n
+nxn[A[1 +  s] +Bn+1Bn]
+n  [Bn1Bn]9
>>>>=
>>>>;:
Now we can take the  rst order conditions
zj= A 
^ ^  1
^ 1andxn= A[1 +  s] +Bn+1Bn
~ n~ 1~  1
~ 1:
HenceAis de ned by the following equation
(r+ )A= +A^ 
^ 1  
^  ^ 
^ 1 
^ 1 
^ 1
1^ 
andBn:
Bn+1= ( +n )Bnn Bn1
~ 1 ~ 1
~ ~ ~ 1
~ n~ ~ 
~ +BnA[1 +  s]:
Proof of Proposition 7.First we compute the number of citable patents M:The measure
of citable patents after  t is simply
M(t+  t) = [M(t) + 1] (x t(1 ) +z t) + 1 x t  + (1x tz t)M(t):
Imposing the steady state condition M(t+  t) =M(t) we  nd M=1
 +z
x :
For any given innovation size sk=  k;the 
ow equations for external patents with ncitations
50
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 52 -->


Growth through Heterogeneous Innovations
take the following form:
State :
n= 0 :
n 1 :Inflow
	k1 (1 ) =
M sk;n1
  k( (1 ) +z) =Outflow
M sk;0  +M sk;0
  k( (1 ) +z)
M sk;n  +M sk;n
  k( (1 ) +z)(43)
The  rst line represents size skinnovations with no citations ( n= 0). In
ows come from 	 k1
product lines where the latest follow-up innovation was of size   k1and a new follow-up innovation
brings the product line into the 	 kgroup. This occurs at rate  (1 ). This in
ow is not dependent
on the number of citable patents M;as it only depends upon the rate of external advancement
across product lines. All patents initially have zero citations, and only a single patent can arrive
per product line at any instant. The in
ow thus depends only on the rate of a ected product lines.
The out
ow of this n= 0 group depends upon M sk;0, the number of patents for each innovation
sizesk. The  rst part of the out
ow occurs when the technology cluster is replaced through a new
major innovation at the rate   , as the a ected patents become defunct and are no longer considered
for citation. The second part of the out
ow occurs when patents receive a new citation from
subsequent innovations at the rate 
  k( (1 ) +z). This latter expression is the probability
of citation based on step size ( 
  k) multiplied by the arrival rate of subsequent patents. In this
case, patents remain active but move up the citation distribution.
Similar reasoning applies to the second row, where citations n 1, except that the in
ow occurs
only from the ( k;n1) group. These innovations arrive at rate  (1 ) +z, now also depending
upon incumbent advances, and they cite the speci c patent at rate 
  k.
Next we characterize the citation distribution of internal patents with 
ow equations:
State :
n= 0 :
n 1 :Inflow
z=
M  ;n1
 ( (1 ) +z) =Outflow
M  ;0  +M  ;0
 ( (1 ) +z)
M  ;n  +M  ;n
 ( (1 ) +z)(44)
These 
ows have similar interpretation. The substantive di erence is that the in
ow of zero-cited
patents occurs at rate zfor internal improvements, accumulating across realized success from the
internal R&D e orts of the incumbent  rm in each product line.
51
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 53 -->


Akcigit and Kerr
The equations (19) and (43) imply   sk;0= (1  )k 
M[  +
sk( (1  )+z)];and we we can rewrite the
second line of (43) in a recursive form as   sk;n=  sk;n1
sk( (1  )+z)
[  +
sk( (1  )+z)], which implies   sk;n=
 sk;0h

sk( (1 )+z)
  +
sk( (1 )+z)in
:Similar reasoning applies to    ;nand to the 
ow equations (44) :
For the second part of the theorem, we just rewrite the same 
ow equations without the internal
citationsz:Then the expressions follow.
B Full Predictions of Baseline Model
This appendix outlines the full set of predictions for the baseline theoretical model without scaling.
Most predictions are general and do not depend upon whether internal or external innovation has a
larger average step size. Predictions C3, D5, and D6 are speci c to the case of external innovation
having the larger step size, which we  nd empirically to be true. Our NBER working paper provides
the proofs of these predictions.
A: Firm Size Distribution and Firm Growth Rates
A1The size distribution of  rms is highly skewed.
A2The probability of a  rm's survival is negatively related to its size.
A3Small  rms that survive tend to grow faster than larger  rms. Among larger  rms, this
negative relationship weakens.
A4The variance of growth rates is higher for smaller  rms.
A5Younger  rms have a higher probability of exiting, but those that survive tend to grow faster
than older  rms.
B: Firm Size Distribution and Innovation Intensity
B1R&D expenditures increase with  rm size among innovative  rms, but the intensity of R&D
decreases with  rm size.
B2Similarly, patent counts increase with  rm size among innovative  rms, but the intensity of
patenting decreases with  rm size.
52
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 54 -->


Growth through Heterogeneous Innovations
B3Younger  rms are more R&D and patent intensive than older  rms.
C: Patent Citation Behavior and Innovation Spillover Size
C1A large fraction of patents receive zero external citations.
C2The distribution of citations is highly skewed.
C3An average external patent receives more external citations than an internal patent.
C4The distribution of patent citation life is highly skewed.
D: Innovation Type and Firm Size Distribution
D1The proportion of a  rm's patents that receives zero future external citations rises with  rm
size.
D2The proportion of a  rm's given citations that are self citations rises with contemporaneous
 rm size.
D3Average future external citations per patent is decreasing in  rm size.
D4The relative rate of major innovations (highly cited patents) is higher for small  rms. This
higher relative rate weakens with more stringent citation quality thresholds.
D5The average citations (received) of patents by entrants is higher than the average citations of
patents by incumbents. Similarly, the average citations of patents by young  rms is higher
than the average citations of patents by older  rms.
D6The patents made by  rms at their entry on average receive more external citations than
later patents of the same  rm.
E: Innovation Type and Firm Growth Rates
E1More cited patents lead to higher growth for a  rm. This e ect is larger for small  rms.
E2An external patent leads to higher growth than an internal patent on average.
E3More R&D and patent intensive  rms grow faster.
53
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 55 -->


Akcigit and Kerr
E4Everything else equal,  rms that obtain more external patents are more likely to survive.
Firms that receive more external citations are more likely to exit the economy.
C Additional Empirical Results
We include here some selected empirical results that provide special details relevant to our model.
Our working paper contains additional results.
C.1 Monte Carlo Simulations of Internal Patent Citations
Table A1 considers in greater detail the observation made in Section 2that self-citation behavior
rises with  rm size. We study this issue using patent data and assignees, which allows us to
undertake the simulations outside of the Census Bureau. We consider patterns for patents  led
in 1995 and their citations over the previous  ve years. This short period lowers the computation
demands of the simulations, and this snap shot is very representative of the general behavior across
the full sample. In 1995, the self citation share grows from 9% for  rms  ling just one patent to
17% for  rms  ling 2-5 patents. The share further increases to 31% for  rms  ling over 100 patents.
[Table A1 Here]
The last three columns of Table A1 evaluate these observed self citation shares against counter-
factuals. Large patenting  rms are more likely to cite themselves due to the greater likelihood that
they draw upon their past inventions. This is true even if citations are random. If IBM and a small
 rm in 1995 draw a random citation for the computer industry from 1990-1995, the likelihood that
IBM draws itself is much greater. The likelihood of self citing for a new entrant is naturally zero.
This bias to  rm size is particularly true where large  rms dominate narrow technology  elds.
To con rm that this mechanical e ect is not driving the observed relationship in Column 2, we
undertake Monte Carlo simulations where we replace observed patents with random counterfactuals.
For each observed citation, we draw a counterfactual that matches the technology and application
year of the cited patent. We include the original citation among the possible pool of patents, and
we draw with replacement. We measure from the simulation a counterfactual self citation share
54
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 56 -->


Growth through Heterogeneous Innovations
to assignee size relationship. As this relationship depends upon the randomness of the simulation
draws, we repeat the procedure 1000 times.
We use these 1000 simulations to generate 95% con dence bands for the self citation ratio of
each assignee. These con dence bands are speci c to assignees based upon their size and underly-
ing technologies. These con dence bands more rigorously test whether the observed self citation
relationships are a systematic departure from the null hypothesis of being randomly determined.
As anticipated, Column 3 shows that the mean value of the test statistic is rising in  rm size.
Columns 4 and 5 con rm that the observed self citation behavior is a signi cant departure
among large assignees. Column 4 examines the prevalence of departures. For assignees with one
patent during 1995, only 13% display self citation behavior that we can reject as being random
at a 95% con dence level. This non-random share grows to 97% for assignees with more than
100 patents in 1995. Column 5 also shows that average deviation of self citation shares from the
random baseline is growing in  rm size. These departures indicate that our results are due to  rm
behavior rather than the mechanics of  rm size. These self citation  ndings hold in within- rm
panel analyses, too.33
C.2 Panel Relationship Between Entry and Patent Quality
Table A2 presents some simple panel evidence on patent quality within  rms over time. We restrict
the sample to new entrants during 1977-1994. We regress traits of patents on an indicator variable
for whether or not the patent is  led in the  rst two years that a  rm is observed. We include  rm
 xed e ects to compare early patents of the  rm to later patents. We also include technology-year
 xed e ects. Column 1 shows that the average external citation count is higher at entry. Column
2 shows that patents also have larger numbers of claims at  rm entry than in later years. Columns
3-6 show the distribution of external citations in quartiles. Column 3 is the lowest quality quartile,
and Column 6 is the highest quality quartile. Entrants have disproportionate representation in the
highest quality quartile compared to later years for the same  rm. The results describe the time
path of  rms in terms of invention quality.
33This analysis closely relates to the patent localization work of Ja e et al. (1993) andThompson and Fox-Kean
(2005). Similar procedures are used in agglomeration calculations like Duranton and Overman (2005) and Ellison et
al. (2010). Agrawal et al. (2010) discuss related issues with respect to large patenting  rms in \company towns" and
their self citation behavior (e.g., Eastman Kodak in Rochester, NY).
55
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 57 -->


Akcigit and Kerr
[Table A2 Here]
C.3 Dynamic Evidence on Quality Within Firms
Table A3 provides evidence to verify our model's assumption that major external innovations
are followed within  rms by internal innovations and re nements. This process requires that an
external innovation be made to dramatically push forward the technology of a product line that
is dominated by internal inventions within the currently leading  rm. We can further verify these
features by demonstrating that the mean quality of citing patents outside of the original  rm for a
given invention is higher than the mean quality of citing patents within the  rm.
We use a linear speci cation of the form
Citep2;p1= p1+ p2
i;t+  Externalp2;p1+ p2;p1;
where Cite p2;p1 models traits of patents p2that cite patents p1. We include citations for U.S.
industrial patents  led during 1975-1984. We restrict the citations to be US industrial patents  led
within a ten-year window of the original patent. We  nd similar patterns when using all citations,
but the consistent window is more appropriate.
The primary regressor is the indicator variable External p2;p1that takes unit value if the assignee
of citing patent p2di ers from the assignee of cited patent p1. Three-quarters of citations are ex-
ternal. We include  p1 xed e ects for cited patents. We thus compare di erences between internal
and external citations on the same patent. We also include  p2
i;t xed e ects for the technology i
and yeartof the citing patent p2; the patent  xed e ects naturally control for these traits for cited
patentsp1. We de ne  p2
i;tthrough USPTO sub-categories and  ve-year time periods. We cluster
standard errors by cited patents.
The  rst column of Table A3 models the number of external citations on citing patents p2as the
outcome variable. The second column alternatively tests the number of claims on the citing patent
as a measure of quality. Columns 3-6 then test the quality distribution of citing patents in a format
similar to Table A2. Quality distributions are determined through ranks of external citations by
technology and period. Coe cients across the  nal four columns for a row approximately sum to
zero, but the relationship does not hold exactly given that quality distributions are calculated over
56
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 58 -->


Growth through Heterogeneous Innovations
a larger group than the regression sample.
[Table A3 Here]
The  rst column  nds that the mean number of future citations for external innovations that
builds upon a given invention is 0.8 citations higher than the internal innovations that also builds
on the focal invention. This e ect is large relative to the sample mean of 8.2. There is also a
substantial external premium of 1.2 claims relative to the sample mean of 15.4. Columns 3-6 show
that this e ect mainly comes from a greater prevalence of upper quartile patents among the external
citing patents, with mass moved from the lowest two quartiles of the distribution. These patterns
suggest that external innovation that builds upon a given invention is stronger than the internal
innovation that follows.
C.4 Additional Empirical Figures
[Figure 15 & 16 Here]
D Computer Algorithm
We solve the generalized model as a  xed point over the growth rate g:Our algorithm employs a
computational loop with the following steps:
1. Guess a growth rate g:
(a) Guess a creative destruction rate  :
i. Solve for Ain (35);the sequencefBngin (36);andzjandfxngin (37):
ii. Verify the free entry condition as a function of  :A[1 +  s] +B1= :
iii. If not converged, update  and go to step 1(a)i.
(b) Calculate the growth rate: g=  s+z :
(c) Update the growth rate. If not converged, go to step 1a.
2. End the equilibrium solver.
57
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 59 -->


Akcigit and Kerr
3. Simulate a sample of  rms and compute the moments of interest.
The sequence of  rm value functions in step 1(a)i is solved using the uniformization method (see
Acemoglu and Akcigit, 2012 for details). In step 3, we simulate a sample of 214 rms (16,384), split
the time into discrete intervals (e.g., months), and iterate for 500 years until we obtain convergence.
At each iteration,  rms gain and lose products according to the 
ow probabilities speci ed in the
model.
58
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 60 -->


Growth through Heterogeneous Innovations
References
Acemoglu, D. (2008): Introduction to Modern Economic Growth . Princeton University Press.
Acemoglu, D., andU. Akcigit (2012): \Intellectual Property Rights Policy, Competition and
Innovation," Journal of the European Economic Association , 10(1), 1{42.
Acemoglu, D., U. Akcigit, N. Bloom, andW. Kerr (2013): \Innovation, Reallocation, and
Growth," NBER Working Paper # 18993.
Acemoglu, D., U. Akcigit, D. Hanley, andW. Kerr (2016): \Transition to Clean Technol-
ogy," Journal of Political Economy , 124(1), 52{104.
Acemoglu, D., andD. Cao (2015): \Innovation by Entrants and Incumbents," Journal of
Economic Theory, 157, 255{294.
Acs, Z. J., andD. B. Audretsch (1987): \Innovation, Market Structure, and Firm Size," Review
of Economics and Statistics , 69(4), 567{574.
Acs, Z. J., andD. B. Audretsch (1988): \Innovation in Large and Small Firms: An Empirical
Analysis," American Economic Review , 78(4), 678{690.
Acs, Z. J., andD. B. Audretsch (1991): \Innovation and Size at the Firm Level," Southern
Economic Journal, 57(3).
Aghion, P., U. Akcigit, andP. Howitt (2014): \What Do We Learn from Schumpeterian
Growth Theory?," in Handbook of Economic Growth, ed. by P. Aghion, andS. N. Durlauf, pp.
515{563.
Aghion, P., C. Harris, P. Howitt, andJ. Vickers (2001): \Competition, Imitation and
Growth with Step-by-Step Innovation," Review of Economic Studies, 68(3), 467{492.
Aghion, P., andP. Howitt (1992): \A Model of Growth through Creative Destruction," Econo-
metrica, 60(2), 323{351.
Aghion, P., P. Howitt, andJ. Vickers (1997): \Competition and Growth with Step-by-Step
Innovation: An Example," European Economic Review , 41(3), 771{782.
59
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 61 -->


Akcigit and Kerr
Agrawal, A., I. Cockburn, andC. Rosell (2010): \Not Invented Here? Innovation in Com-
pany Towns," Journal of Urban Economics , 67(1), 78{89.
Akcigit, U. (2010): \Firm Size, Innovation Dynamics and Growth," University of Pennsylvania
Working Paper.
Akcigit, U., H. Alp, andM. Peters (2015): \Lack of Selection and Limits to Delegation: Firm
Dynamics in Developing Countries," NBER Working Paper # 21905.
Akcigit, U., D. Hanley, andN. Serrano-Velarde (2016): \Back to Basics: Basic Research
Spillovers, Innovation Policy and Growth," CEPR Discussion Paper # 11707.
Akcigit, U., andW. R. Kerr (2010): \Growth through Heterogeneous Innovations," NBER
Working Paper # 16443.
Arkolakis, C. (2011): \A Uni ed Theory of Firm Selection and Growth," NBER Working Paper
# 17553.
Balasubramanian, N., andJ. Sivadasan (2011): \What Happens When Firms Patent? New
Evidence from US Economic Census Data," Review of Economics and Statistics , 93(1), 126{146.
Barro, R., andX. Sala-i Martin (1995): Economic Growth. New York, NY: McGraw&Hill.
Baumol, W. J. (2002): \Entrepreneurship, Innovation and Growth: The David-Goliath Symbio-
sis," Journal of Entrepreneurial Finance, 7(2), 1{10.
Bernstein, S. (2015): \Does Going Public A ect Innovation?," Journal of Finance , 70(4), 1365{
1403.
Bloom, N., R. Griffith, andJ. Van Reenen (2002): \Do R&D Tax Credits Work? Evidence
from a Panel of Countries 1979{1997," Journal of Public Economics , 85(1), 1{31.
Bloom, N., M. Schankerman, andJ. Van Reenen (2013): \Identifying Technology Spillovers
and Product Market Rivalry," Econometrica, 81(4), 1347{1393.
Blundell, R., R. Griffith, andF. Windmeijer (2002): \Individual E ects and Dynamics in
Count Data Models," Journal of Econometrics, 108(1), 113{131.
60
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 62 -->


Growth through Heterogeneous Innovations
Caballero, R. J., andA. B. Jaffe (1993): \How High Are the Giants' Shoulders: An Empirical
Assessment of Knowledge Spillovers and Creative Destruction in a Model of Economic Growth,"
inNBER Macroeconomics Annual 1993, Volume 8, pp. 15{86. MIT press.
Cabral, L., andJ. Mata (2003): \On the Evolution of the Firm Size Distribution: Facts and
Theory," American Economic Review , 93(4), 1075{1090.
Cai, A. J. (2010): \Knowledge Spillovers and Firm Size Heterogeneity," University of New South
Wales Working Paper.
Caves, R. E. (1998): \Industrial Organization and New Findings on the Turnover and Mobility
of Firms," Journal of Economic Literature, 36(4), 1947{1982.
Christensen, C. (1997): The Innovator's Dilemma: When New Technologies Cause Great Firms
to Fail . Boston, MA: Harvard Business School Press.
Cohen, W. (1995): \Empirical Studies of Innovative Activity," in Handbook of the Economics of
Innovations and Technological Change, ed. by P. Stoneman. Oxford, UK: Blackwell.
Cohen, W. M., andS. Klepper (1996): \Firm Size and the Nature of Innovation within In-
dustries: The Case of Process and Product R&D," Review of Economics and Statistics , 78(2),
232{243.
Davis, S., J. Haltiwanger, andS. Schuh (1996): Job Creation and Destruction . Cambridge,
MA: MIT Press.
Dunne, T., M. J. Roberts, andL. Samuelson (1988): \Patterns of Firm Entry and Exit in
US Manufacturing Industries," RAND Journal of Economics, 19(4), 495{515.
Duranton, G. (2007): \Urban Evolutions: The Fast, the Slow, and the Still," American Economic
Review, 97(1), 197{221.
Duranton, G., andH. G. Overman (2005): \Testing for Localization Using Micro-geographic
Data," Review of Economic Studies, 72(4), 1077{1106.
Eeckhout, J., andB. Jovanovic (2002): \Knowledge Spillovers and Inequality," American
Economic Review, 92(5), 1290{1307.
61
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 63 -->


Akcigit and Kerr
Ellison, G., E. L. Glaeser, andW. R. Kerr (2010): \What Causes Industry Agglomeration?
Evidence from Coagglomeration Patterns," American Economic Review , 100(3), 1195{1213.
Foster, L., J. Haltiwanger, andC. J. Krizan (2000): \Aggregate Productivity Growth:
Lessons from Microeconomic Evidence," in New Developments in Productivity Analysis. Chicago,
IL: University of Chicago Press.
Gabaix, X. (2009): \Power Laws in Economics and Finance," Annual Review of Economics, 1(1),
255{294.
Galasso, A., andT. S. Simcoe (2011): \CEO Overcon dence and Innovation," Management
Science, 57(8), 1469{1484.
Gans, J. S., D. H. Hsu, andS. Stern (2002): \When Does Start-up Innovation Spur the Gale
of Creative Destruction?," RAND Journal of Economics, 33(4), 571{586.
Garcia-Macia, D., C.-T. Hsieh, andP. Klenow (2016): \How Destructive is Innovation,"
Stanford University Working Paper.
Geroski, P. A. (1998): \An Applied Econometrician's View of Large Company Performance,"
Review of Industrial Organization , 13(3), 271{294.
Gilbert, R. J., andD. M. G. Newbery (1982): \Preemptive Patenting and the Persistence of
Monopoly," American Economic Review , 72(3), 514{526.
Griliches, Z. (1990): \Patent Statistics as Economic Indicators: A Survey," Journal of Economic
Literature , 28(4), 1661{1707.
Griliches, Z. (1992): \The Search for R&D Spillovers," Scandinavian Journal of Economics , 94,
S29{S47.
Gromb, D., andD. S. Scharfstein (2002): \Entrepreneurship in Equilibrium," NBER Working
Paper # 9001.
Grossman, G. M., andE. Helpman (1991): \Quality Ladders in the Theory of Growth," Review
of Economic Studies, 58(1), 43{61.
62
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 64 -->


Growth through Heterogeneous Innovations
Hall, B., andJ. Van Reenen (2000): \How E ective Are Fiscal Incentives for R&D? A Review
of the Evidence," Research Policy , 29(4), 449{469.
Hall, B. H. (1992): \R&D Tax Policy During the 1980s: Success or Failure?," Tax Policy and
the Economy, 7, 1{36.
Hall, B. H., A. Jaffe, andM. Trajtenberg (2005): \Market Value and Patent Citations,"
RAND Journal of Economics, 36(1), 16{38.
Hall, B. H., A. B. Jaffe, andM. Trajtenberg (2001): \The NBER Patent Citation Data
File: Lessons, Insights and Methodological Tools," NBER Working Paper # 8498.
Hall, B. H., andR. H. Ziedonis (2001): \The Patent Paradox Revisited: An Empirical Study of
Patenting in the US Semiconductor Industry, 1979{1995," RAND Journal of Economics, 32(1),
101{128.
Hausman, J., B. H. Hall, andZ. Griliches (1984): \Econometric Models for Count Data with
an Application to the Patents-R&D Relationship," Econometrica, 52(4), 909{38.
Hellmann, T., andE. Perotti (2011): \The Circulation of Ideas in Firms and Markets,"
Management Science, 57(10), 1813{1826.
Henderson, R. M. (1993): \Underinvestment and Incompetence as Responses to Radical Inno-
vation: Evidence from the Photolithographic Alignment Equipment Industry," RAND Journal
of Economics, 24(2), 248{270.
Henderson, R. M., andK. B. Clark (1990): \Architectural Innovation: The Recon guration
of Existing Product Technologies and the Failure of Established Firms," Administrative Science
Quarterly, 35(1), 9{30.
Hopenhayn, H., G. Llobet, andM. Mitchell (2006): \Rewarding Sequential Innovators:
Prizes, Patents, and Buyouts," Journal of Political Economy , 114(6), 1041{1068.
Hopenhayn, H. A. (1992): \Entry, Exit, and Firm Dynamics in Long Run Equilibrium," Econo-
metrica, 60(5), 1127{1150.
63
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 65 -->


Akcigit and Kerr
Howitt, P. (1999): \Steady Endogenous Growth with Population and R&D Inputs Growing,"
Journal of Political Economy , 107(4), 715{730.
Hsieh, C.-T., andP. Klenow (2014): \The Life-Cycle of Manufacturing Plants in India and
Mexico," Quarterly Journal of Economics , 129(3), 1035{1084.
Hurst, E., andB. W. Pugsley (2011): \What do Small Businesses Do?," Brookings Papers on
Economic Activity, 43(2 (Fall)), 73{142.
Jaffe, A. B., M. Trajtenberg, andM. S. Fogarty (2000): \Knowledge Spillovers and
Patent Citations: Evidence from a Survey of Inventors," American Economic Review Papers and
Proceedings, 90(2), 215{218.
Jaffe, A. B., M. Trajtenberg, andR. Henderson (1993): \Geographic Localization of
Knowledge Spillovers as Evidenced by Patent Citations," Quarterly Journal of Economics ,
108(3), 577{598.
Jarmin, R. S., andJ. Miranda (2002): \The Longitudinal Business Database," Center for
Economic Studies Working Paper.
Jones, C. I. (1995): \R&D-based Models of Economic Growth," Journal of Political Economy ,
103(4), 759{784.
Jovanovic, B. (1982): \Selection and the Evolution of Industry," Econometrica, 50(3), 649{70.
Jovanovic, B., andG. M. MacDonald (1994): \The Life Cycle of a Competitive Industry,"
Journal of Political Economy , 102(2), 322{347.
Kerr, W., R. Nanda, andM. Rhodes-Kropf (2014): \Entrepreneurship as Experimentation,"
Journal of Economic Perspectives, 28(3), 25{48.
Kerr, W. R. (2010): \Breakthrough Inventions and Migrating Clusters of Innovation," Journal
of Urban Economics, 67(1), 46{60.
Kerr, W. R., andS. Fu (2008): \The Survey of Industrial R&DPatent Database Link Project,"
Journal of Technology Transfer , 33(2), 173{186.
64
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 66 -->


Growth through Heterogeneous Innovations
Klepper, S. (1996): \Entry, Exit, Growth, and Innovation over the Product Life Cycle," American
Economic Review, 86(3), 562{583.
Klepper, S., andE. Graddy (1990): \The Evolution of New Industries and the Determinants
of Market Structure," RAND Journal of Economics, 21(1), 27{44.
Klette, T. J., andS. Kortum (2004): \Innovating Firms and Aggregate Innovation," Journal
of Political Economy , 112(5), 986{1018.
Kortum, S. (1997): \Research, Patenting, and Technological Change," Econometrica, 65(6), 1389{
1420.
Kortum, S., andJ. Lerner (2000): \Assessing the Contribution of Venture Capital to Innova-
tion," RAND Journal of Economics, 31(4), 674{692.
Kueng, L., M.-J. Yang, andB. Hong (2014): \Sources of Firm Life-Cycle Dynamics: Di er-
entiating Size vs. Age E ects," NBER Working Paper # 20261.
Lamoreaux, N. R., K. L. Sokoloff, andD. Sutthiphisal (2011): \The Reorganization
of Inventive Activity in the United States in the Early Twentieth Century," in Understanding
Long-Run Economic Growth: Geography, Institutions, and the Knowledge Economy , ed. by N. R.
Lamoreaux, andD. Costa, pp. 235{274. University of Chicago Press.
Lentz, R., andD. Mortensen (2008): \An Empirical Model of Growth through Product Inno-
vation," Econometrica, 76(6), 1317{1373.
Lentz, R., andD. Mortensen (2014): \Optimal Growth Through Product Innovation," Uni-
versity of Wisconsin Working Paper.
Lerner, J. (1994): \The Importance of Patent Scope: An Empirical Analysis," RAND Journal
of Economics, 25(2), 319{333.
Lerner, J. (1997): \An Empirical Exploration of a Technology Race," RAND Journal of Eco-
nomics, 28(2), 228{247.
Lerner, J. (2012): The Architecture of Innovation: The Economics of Creative Organizations.
Boston, MA: Harvard Business School Press.
65
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 67 -->


Akcigit and Kerr
Lerner, J., M. Sorensen, andP. Str omberg (2011): \Private Equity and Long-run Invest-
ment: The Case of Innovation," Journal of Finance, 66(2), 445{477.
Lucas, R. E. (1978): \On the Size Distribution of Business Firms," Bell Journal of Economics ,
9(2), 508{523.
Luttmer, E. G. (2007): \Selection, Growth, and the Size Distribution of Firms," Quarterly
Journal of Economics , 122(3), 1103{1144.
Luttmer, E. G. (2011): \On the Mechanics of Firm Growth," Review of Economic Studies, 78(3),
1042{1068.
March, J. G. (1991): \Exploration and Exploitation in Organizational Learning," Organization
science, 2(1), 71{87.
Mehta, A., M. Rysman, andT. Simcoe (2010): \Identifying the Age Pro le of Patent Citations:
New Estimates of Knowledge Di usion," Journal of Applied Econometrics, 25(7), 1179{1204.
Nelson, R., andS. Winter (1982): An Evolutionary Theory of Economic Change . Cambridge,
MA: Harvard University Press.
Nicholas, T. (2014): \Scale and Innovation During Two U.S. Breakthrough Eras," Harvard
Business School Working Paper.
Peretto, P. F. (1998): \Technological Change, Market Rivalry, and the Evolution of the Capi-
talist Engine of Growth," Journal of Economic Growth, 3(1), 53{80.
Rausch, L. (2010): \Indicators of U.S. Small Business's Role in R&D," National Science Founda-
tion Info Brief 10-304.
Reinganum, J. F. (1983): \Uncertain Innovation and the Persistence of Monopoly," American
Economic Review, 73(4), 741{748.
Romer, P. M. (1986): \Increasing Returns and Long-run Growth," Journal of Political Economy,
94(5), 1002{1037.
66
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 68 -->


Growth through Heterogeneous Innovations
Romer, P. M. (1990): \Endogenous Technological Change," Journal of Political Economy, 98(5),
S71{102.
Rosen, R. J. (1991): \Research and Development with Asymmetric Firm Sizes," RAND Journal
of Economics, 22(3), 411{429.
Samila, S., andO. Sorenson (2011): \Venture Capital, Entrepreneurship and Economic
Growth," Review of Economics and Statistics , 93(1), 338{349.
Spence, M. (1984): \Cost Reduction, Competition, and Industry Performance," Econometrica,
52(1), 101{121.
Sutton, J. (1997): \Gibrat's Legacy," Journal of Economic Literature, 35(1), 40{59.
Thomke, S. (2003): Experimentation Matters: Unlocking the Potential of New Technologies for
Innovation. Boston, MA: Harvard Business School Press.
Thompson, P., andM. Fox-Kean (2005): \Patent Citations and the Geography of Knowledge
Spillovers: A Reassessment," American Economic Review , 95(1), 450{460.
Trajtenberg, M. (1990): \A Penny for Your Quotes: Patent Citations and the Value of Innova-
tions," RAND Journal of Economics, 21(1), 172{187.
Wilson, D. J. (2009): \Beggar Thy Neighbor? The In-state, Out-of-state, and Aggregate E ects
of R&D Tax Credits," Review of Economics and Statistics , 91(2), 431{436.
Zucker, L., M. Darby, andM. Brewer (1998): \Intellectual Human Capital and the Birth of
U.S. Biotechnology Enterprises," American Economic Review , 88, 290{306.
67
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 69 -->


Akcigit and Kerr
Figure 1: Firm Growth by Firm Size
‐0.050.000.050.100.150.200.250.300.350.400.45
2
47
101520
27
3646
61
80
108148209
306
466774
1,4993,754
28,550Forward employment growth
Average employee count in size bin
68
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 70 -->


Growth through Heterogeneous Innovations
Figure 2: Innovation Intensity by Firm Size
0.00.20.40.60.81.01.21.41.6
1
3
4
69
1319
28
42
62
94
141210
312
479
768
1,332
2,590
6,559
38,176Patents per employee
Average employee count in size bin
69
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 71 -->


Akcigit and Kerr
Figure 3: Citation Distribution by Patent Type
0 5 10 15 20 25 300.10.20.30.40.50.60.70.80.91
Number of External Citations ReceivedCumulative Distribution of Patents By Type  
external patents
internal patents
70
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 72 -->


Growth through Heterogeneous Innovations
Figure 4: Example of Firms
S
ector jq
Firm
1
Firm
2
4
71
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 73 -->


Akcigit and Kerr
Figure 5: Innovation Types
Sector jq
External
R&DInternal
R&D New
Entr
antFirm
1
Firm
2
5
72
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 74 -->


Growth through Heterogeneous Innovations
Figure 6: Examples of External Innovations
Numb
er of times the latest technology is improvedInnovation
step size, sMajor Advance F
ollow-up Improvement
01234567 012 012345
1
73
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 75 -->


Akcigit and Kerr
Figure 7: Citation Distribution
Number of Citations Received0 5 10 15 20 25 30Probability
00.050.10.150.20.25
Model
Data
74
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 76 -->


Growth through Heterogeneous Innovations
Figure 8: Franchise Value Bn
Number of Product Lines012345678910Bn
-0.500.511.522.53
<=0 (Baseline)
<=0.2
<=0.4
<=0.5 (KK)
75
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 77 -->


Akcigit and Kerr
Figure 9: Innovation Intensity xn
Number of Product Lines (n)2468101214161820xn
00.020.040.060.080.10.12<=0 (Baseline)
<=0.2
<=0.4
<=0.5 (KK)
76
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 78 -->


Growth through Heterogeneous Innovations
Figure 10: Firm Size vs Number of Product lines
Number of Product Lines0 2 4 6 8 10 12Firm Size (Normalized)
024681012
77
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 79 -->


Akcigit and Kerr
Figure 11: Product Line Distribution
Number of Product Lines0 1 2 3 4 5 6 7 8 910Probability
00.10.20.30.40.50.6
78
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 80 -->


Growth through Heterogeneous Innovations
Figure 12: Firm Size Distribution
Firm Size (Normalized)0 1 2 3 4 5 6 7 8 910Probability
00.020.040.060.080.10.120.140.16
79
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 81 -->


Akcigit and Kerr
Figure 13: Cost Multiplier for Major Innovation, K(n)
Firm Size
(Number of Product Lines)12345678910Cost of Innovation
(Rel to 1-Product Firm)
11.11.21.31.41.51.6
80
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 82 -->


Growth through Heterogeneous Innovations
Figure 14: Share of Major Advances in Firm's Innovation Portfolio
12345678910
Firm Size
(Number of Product Lines)0.0580.060.0620.0640.0660.0680.070.0720.074
81
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 83 -->


Akcigit and Kerr
Figure 15: Firm Growth
by Firm Size
0.000.010.020.030.040.050.060.070.080.090.10
1 2 3 4 5 8 15 38 406Forward employment growth
Average establishment count in size bin
82
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 84 -->


Growth through Heterogeneous Innovations
Figure 16: Innovation Intensity
by Firm Size
0.000.050.100.150.200.250.300.350.40
1.0 1.9 2.3 3.0 4.3 6.6 11.6 23.1 58.1 496.6Patents per employee
Average establishment count in size bin
83
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 85 -->


Akcigit and Kerr
Table 1: Firm size and patent quality distribution
Share of  rm's patents in quality distribution range:
[0,25) [25,50) [50,75) [75,100]
Log  rm employment t 0.0027 0.0048 0.0000 -0.0074
(0.0009) (0.0010) (0.0010) (0.0012)
Notes: Estimates include 16,818 observations, are unweighted, and cluster standard errors by  rm.
84
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 86 -->


Growth through Heterogeneous Innovations
Table 2: Citation Patterns in Example 1
Cited prob. Citing Cited prob. Citing Cited prob. Citing
P1:
  P 2P6 P5:
  P 6 P8:
  P 9
P2:
   P 3P6 P6:
  3none P9:
   none
P3:
  2P4P6 P7:
  P 8;P9P10:
  P 11;P12;:::
P4:
  P 5;P6
85
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 87 -->


Akcigit and Kerr
Table 3: Parameters of the Model
Parameter Description Equation Identi cation
  discount rate (2) external calibration
^ curvature of internal R&D (6) external calibration
~ curvature of external R&D (7) external calibration
  probability of major advance (8) match citation distribution
  multiplier of declining follow-up improvements (8) match citation distribution
  quality multiplier of internal innovation (8) indirect inference
  quality share in  nal goods production (3) indirect inference
  entry cost (9) indirect inference
^  scale of internal R&D (6) indirect inference
~  scale of external R&D (7) indirect inference
  product line share in external R&D (34) indirect inference
  quality multiplier of major advance (8) cite distn + ind inference

 citation probability multiplier (43) cite distn + ind inference
86
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 88 -->


Growth through Heterogeneous Innovations
Table 4: Citation Distribution Parameters
  
   
0.103 0.750 0.929
87
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 89 -->


Akcigit and Kerr
Table 5: Moments
Moment Data Model Moment Data Model
pro tability 0.109 0.106 entry rate 0.058 0.066
R&D intensity 0.041 0.042 average growth rate 0.010 0.010
internal/external cite 0.774 0.732 growth vs size (fact 1) -0.035 -0.035
fraction of internal patents 0.215 0.250
88
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 90 -->


Growth through Heterogeneous Innovations
Table 6: Estimated Model Parameters
  ~  ^         
0.395 4.066 0.346 0.112 0.051 0.106 0.830
Implied + = 0:895:
89
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 91 -->


Akcigit and Kerr
Table 7: Growth Decomposition
Actual Values In Percentage Terms
Internal External New Entry Internal External New Entry
0.0020 0.0055 0.0026 19.8% 54.5% 25.7%
90
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 92 -->


Growth through Heterogeneous Innovations
Table 8: Firm size distribution and data-model comparison
Growth rate Normalized patent Internal patent Top 10% patent
to next period per employee share share
Panel A. Model, e ects relative to smallest size quintile
2nd quintile -0.1284 (0.0210) -0.8194 (0.0392) -0.0134 (0.0114) -0.0032 (0.0063)
3rd quintile -0.2159 (0.0199) -1.1065 (0.0379) -0.0116 (0.0111) -0.0055 (0.0060)
4th quintile -0.3202 (0.0191) -1.3404 (0.0372) 0.0256 (0.0105) -0.0059 (0.0056)
Largest quintile -0.3866 (0.0188) -1.5507 (0.0368) 0.0538 (0.0099) -0.0065 (0.0053)
Panel B. Data, e ects relative to smallest size quintile
2nd quintile -0.0133 (0.0502) -0.9067 (0.0336) 0.0190 (0.0044) -0.0030 (0.0078)
3rd quintile -0.2790 (0.0464) -1.0780 (0.0320) 0.0356 (0.0048) -0.0211 (0.0076)
4th quintile -0.2865 (0.0462) -1.1166 (0.0322) 0.0413 (0.0047) -0.0296 (0.0072)
Largest quintile -0.4052 (0.0448) -1.1351 (0.0323) 0.0471 (0.0045) -0.0211 (0.0072)
Notes: Estimates are unweighted and cluster standard errors by  rm.
91
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 93 -->


Akcigit and Kerr
Table 9: Firm size distribution and patent quality distribution comparison
Share of  rm patents in quality distribution range:
[0,25) [25,50) [50,75) [75,100]
Panel A. Model, e ects relative to smallest size quintile
2nd quintile 0.0039 (0.0091) -0.0081 (0.0122) -0.0133 (0.0094) -0.0091 (0.0097)
3rd quintile 0.0111 (0.0090) -0.0055 (0.0119) -0.0051 (0.0090) -0.0107 (0.0094)
4th quintile 0.0012 (0.0082) 0.0153 (0.0112) -0.0028 (0.0083) -0.0137 (0.0088)
Largest quintile -0.0108 (0.0077) 0.0386 (0.0104) -0.0045 (0.0078) -0.0232 (0.0082)
Panel B. Data, e ects relative to smallest size quintile
2nd quintile -0.0079 (0.0079) 0.0054 (0.0090) 0.0074 (0.0095) -0.0049 (0.0106)
3rd quintile 0.0039 (0.0081) 0.0317 (0.0093) -0.0008 (0.0094) -0.0349 (0.0105)
4th quintile 0.0122 (0.0078) 0.0405 (0.0090) 0.0025 (0.0092) -0.0552 (0.0102)
Largest quintile 0.0140 (0.0074) 0.0327 (0.0080) 0.0037 (0.0086) -0.0503 (0.0099)
Notes: See Table 8.
92
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 94 -->


Growth through Heterogeneous Innovations
Table 10: Firm-level regression comparison
Dependent variable is growth to next period
Data using Data using
Model citations for quality claims for quality
Log employment t -0.0980 (0.0032) -0.0983 (0.0075) -0.1012 (0.0076)
Log patents t 0.1091 (0.0048) 0.1310 (0.0125) 0.1330 (0.0125)
Share patents [50, 75) t 0.0894 (0.0150) 0.1004 (0.0379) -0.0015 (0.0397)
Share patents [75,100] t 0.0734 (0.0135) 0.3659 (0.0399) 0.1274 (0.0382)
(0,1) Medium internal patents t -0.0579 (0.1105) -0.0473 (0.0329) -0.0431 (0.0323)
(0,1) High internal patents t -0.1056 (0.0085) -0.1870 (0.0321) -0.2036 (0.0323)
Notes: See Table 8.
93
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 95 -->


Akcigit and Kerr
Table 11: Robustness with Facts 1 and 2
Moment Data Model Moment Data Model
pro tability 0.109 0.106 entry rate 0.058 0.066
R&D intensity 0.041 0.041 average growth rate 0.010 0.010
internal/external cite 0.774 0.767 growth vs size (fact 1) -0.035 -0.038
fraction of internal patents 0.215 0.250 top innov. vs size (fact 2) -0.0034 -0.0034
Estimated :0.395, Implied  + = 0:895:
94
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 96 -->


Growth through Heterogeneous Innovations
Table 12: Robustness with Facts 1, 2, and 3
Moment Data Model Moment Data Model
pro tability 0.109 0.113 average growth rate 0.010 0.009
R&D intensity 0.041 0.049 growth vs size (fact 1) -0.035 -0.057
internal/external cite 0.774 0.806 top innov. vs size (fact 2) -0.0034 -0.0061
fraction of internal patents 0.215 0.272 patent per emp vs size (fact 3) -0.182 -0.081
entry rate 0.058 0.059
Estimated :0.407, Implied  + = 0:907:
95
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 97 -->


Akcigit and Kerr
Table 13: Robustness with Growth Rate Maximum
Moment Data Model Moment Data Model
pro tability 0.109 0.106 entry rate 0.058 0.066
R&D intensity 0.041 0.041 average growth rate 0.010 0.010
internal/external cite 0.774 0.732 growth vs size (fact 1) -0.048 -0.046
fraction of internal patents 0.215 0.252
Estimated :0.384, Implied  + = 0:884:
96
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 98 -->


Growth through Heterogeneous Innovations
Table 14: Robustness with Different R&D Elasticities
Panel A. = 0:4
Moment Data Model Moment Data Model
pro tability 0.109 0.097 entry rate 0.058 0.067
R&D intensity 0.041 0.041 average growth rate 0.010 0.009
internal/external cite 0.774 0.773 growth vs size (fact 1) -0.035 -0.036
fraction of internal patents 0.215 0.252
Estimated :0.497, Implied  + = 0:897:
Panel B. = 0:6
pro tability 0.109 0.094 entry rate 0.058 0.068
R&D intensity 0.041 0.039 average growth rate 0.010 0.010
internal/external cite 0.774 0.798 growth vs size (fact 1) -0.035 -0.036
fraction of internal patents 0.215 0.228
Estimated :0.283, Implied  + = 0:883:
97
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 99 -->


Akcigit and Kerr
T
able A1. Cross-sectional relationship of assignee size and self citation behavior
Coun
t of assignees
by number of 1995
patents with
citations for
patents over the
prior 5 yearsMean observed
self citation share
for patents over
the prior 5 yearsComparison of observed self citation behavior against 1000 Monte
Carlo simulations replicating technologies and citation years
Mean
test
statistic for 95%
condence level
by size categoryShare of rms
deviating at 95%
condence level from
random behaviorMean deviations of
observed citation shares
(col. 2 minus col. 3)
(1)
(2) (3) (4) (5)
1
patent 8044 9% 1% 13% 8%
2-5 patents 3382 17% 3% 35% 14%
6-10 patents 595 22% 4% 64% 18%
11-20 patents 307 23% 4% 73% 19%
21-100 patents 288 27% 4% 89% 23%
100+ patents 65 31% 6% 97% 25%
N
otes: Table reports the results of Monte Carlo simulations of self citation behavior by rm size. The sample is restricted to US-based, industrial patents
in 1995 and their citations to other US-based, industrial patents over the prior ve years. Rows group assignees by their patent counts in 1995. The second
column indicates the share of observed citations that are self citations. For the Monte Carlo simulations, we draw counterfactuals that match the technologiesand application years of cited patents. We include the original citation among the possible pool of patents, and we draw with replacement. We measure from
the simulation a counterfactual self citation share to assignee size relationship. We repeat the simulations 1000 times to generate 95% condence bands for
the self citation ratio of each assignee. These condence bands are specic to assignees based upon their size and underlying technologies. The third columnprovides the mean test statistic by rm size. This statistic rises with rm size because rms with larger patent portfolios are more likely to cite themselveseven if citations are random. The fourth column indicates the share of assignees by size category that exhibit self citation behavior that exceeds a randompattern at a 95% condence level. These deviations are strongly increasing in rm size. The last column presents the mean deviation of observed self citationbehavior from the simulation baselines. These deviations are also increasing in rm size.1
98
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 100 -->


Growth through Heterogeneous Innovations
T
able A2. Panel relationship between entry and patent quality
Num
ber of
external
citationsNumber of
claims on
patentPrevalence of patents by external citation ranks
(coeﬃcients sum to zero across columns)
0-24%
25-49% 50-74% 75-100%
(1)
(2) (3) (4) (5) (6)
First
two years the
ﬁrm is observed1.1621 0.6920 -0.0148 -0.0042 -0.0048 0.0239
(0.1557) (0.1811) (0.0048) (0.0059) (0.0063) (0.0058)
Firm ﬁxed eﬀects Yes Yes Yes Yes Yes Yes
Technology-year ﬁxed eﬀects Yes Yes Yes Yes Yes Yes
Notes:
Table quantiﬁes changes in average patent quality within ﬁrms over time. Columns 1 and 2 show that external citation rates and claims per patent
are higher at ﬁrm entry. Columns 3-6 show the distribution of external citations in quartiles. Column 3 is the lowest quality quartile, and Column 6 is
the highest quality quartile. The coeﬃcients for a row sum to zero across these columns. Entrants have disproportionate representation in the highestquality quartile compared to later years for the same ﬁrm. The sample includes 260,972 US industrial patents for ﬁrms ﬁrst observed between 1977 and1994. Estimations include ﬁrm ﬁxed eﬀects and technology-year ﬁxed eﬀects, cluster standard errors at the ﬁrm level, and weight patents such that eachﬁrm receives constant weight.2
99
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).


<!-- page 101 -->


Akcigit and Kerr
T
able A3. Assignee size and building upon technologies
Num
ber of
external
citations on
citing patentNumber of
claims on
citing patentPrevalence of patents by external
citation ranks among citing patents
(coe¢ cients sum to zero across columns)
0-24%
25-49% 50-74% 75-100%
(1)
(2) (3) (4) (5) (6)
External
citation 0.849 1.236 -0.015 -0.009 -0.005 0.029
(0.053) (0.073) (0.002) (0.002) (0.002) (0.002)
Cited patent xed e¤ects Yes Yes Yes Yes Yes Yes
Citing tech-year e¤ects Yes Yes Yes Yes Yes Yes
N
otes: Table characterizes di¤erences in patent quality for internal versus external patents that cite a particular invention. Columns 1 and 2 show
that external citation rates and claims are higher. Columns 3-6 show the quality distribution of the citations by quartiles. Column 3 is the lowest
quality quartile, and Column 6 is the highest quality quartile. External citations are consistently of higher quality. The sample includes 761,940citations of US industrial patents from 1975-1984 applied for within ten years after the original patent. Estimations include cited patent xed e¤ectsand technology-period xed e¤ects for citing patents. Estimations cluster standard errors by cited patent.
3
100
Copyright The University of Chicago 2018. Preprint (not copyedited or formatted). 
Please use DOI when citing or quoting. DOI: 10.1086/697901
This content downloaded from 132.174.250.220 on March 21, 2018 00:48:36 AM
All use subject to University of Chicago Press Terms and Conditions (http://www.journals.uchicago.edu/t-and-c).