Krieger, Bastian; Rammer, Christian; Breithaupt, Patrick

Research Report
Identifizierung von Querschnittsthemen in Projekten
der Direkten Projektförderung des BMBF: Bericht zur
Machbarkeitsstudie

ZEW-Gutachten

Provided in Cooperation with:
ZEW - Leibniz Centre for European Economic Research

Suggested Citation: Krieger, Bastian; Rammer, Christian; Breithaupt, Patrick (2020) : Identifizierung
von Querschnittsthemen in Projekten der Direkten Projektförderung des BMBF: Bericht zur
Machbarkeitsstudie, ZEW-Gutachten, ZEW - Leibniz-Zentrum für Europäische Wirtschaftsforschung,
Mannheim

This Version is available at:
https://hdl.handle.net/10419/222373

Standard-Nutzungsbedingungen:

Terms of use:

Die Dokumente auf EconStor dürfen zu eigenen wissenschaftlichen
Zwecken und zum Privatgebrauch gespeichert und kopiert werden.

Documents in EconStor may be saved and copied for your personal
and scholarly purposes.

Sie dürfen die Dokumente nicht für öffentliche oder kommerzielle
Zwecke vervielfältigen, öffentlich ausstellen, öffentlich zugänglich
machen, vertreiben oder anderweitig nutzen.

You are not to copy documents for public or commercial purposes, to
exhibit the documents publicly, to make them publicly available on the
internet, or to distribute or otherwise use the documents in public.

Sofern die Verfasser die Dokumente unter Open-Content-Lizenzen
(insbesondere CC-Lizenzen) zur Verfügung gestellt haben sollten,
gelten abweichend von diesen Nutzungsbedingungen die in der dort
genannten Lizenz gewährten Nutzungsrechte.

If the documents have been made available under an Open Content
Licence (especially Creative Commons Licences), you may exercise
further usage rights as specified in the indicated licence.

Bericht zur Machbarkeitsstudie

Identifizierung von
Querschnittsthemen in Projekten
der Direkten Projektförderung des
BMBF

Bastian Krieger, Christian Rammer, Patrick Breithaupt
ZEW – Leibniz‐Zentrum für Europäische Wirtschaftsforschung

Mannheim, März 2020

Ansprechpartner

Bastian Krieger

Forschungsbereich
Innovationsökonomik und
Unternehmensdynamik

L 7, 1  68161 Mannheim

Postfach 10 34 43
68034 Mannheim

1

krieger@zew.de

E‐Mail
Telefon  +49 621‐1235‐376
Telefax  +49 621‐1235‐170

Identifizierung von Querschnittsthemen in Projekten der Direkten Projektförderung des BMBF
Bericht zu einer Machbarkeitsstudie

Inhalt

Das Wichtigste in Kürze ............................................................................ 3

Executive Summary .................................................................................. 5

1

2

3

3.1

3.2

3.3

4

Aufgabenstellung und Zielsetzung ................................................ 7

Datenbasis .................................................................................... 9

TexAn‐Textfeldanalyse ............................................................... 11

TexAn‐Analyse zum Querschnittsthema Digitalisierung ................. 11

TexAn‐Analyse zum Themenfeld Künstliche Intelligenz ................. 21

TexAn‐Analyse zum Querschnittsthema Soziale Innovationen ...... 25

Analyse mittels maschinellem Lernen zum Themenfeld
Künstliche Intelligenz .................................................................. 30

Fazit

 ................................................................................................... 34

5

5.1

5.2

Anhang ....................................................................................... 36

Unterkategorien der Digitalisierung................................................ 36

Code zur TexAn‐Analyse .................................................................. 37

Abbildungsverzeichnis ............................................................................ 43

Tabellenverzeichnis ................................................................................ 44

Verzeichnis der Übersichten ................................................................... 44

Verzeichnis der Boxen ............................................................................ 44

2

Identifizierung von Querschnittsthemen in Projekten der Direkten Projektförderung des BMBF
Bericht zu einer Machbarkeitsstudie

Das Wichtigste in Kürze

Die  Machbarkeitsstudie  untersuchte,  inwieweit  Querschnittsthemen  der  Forschungs‐
förderung  durch  eine  semantische  Analyse  von  Vorhabenbeschreibungen  mit  hinrei‐
chender Genauigkeit identifiziert werden können. Es wurden zwei Querschnittsthemen
betrachtet:

  Digitalisierung (inkl. des Teilgebiets Künstliche Intelligenz)

  Soziale Innovationen

Die semantische Analyse wurde mit Hilfe eines Textanalyseprogramms vorgenommen,
das Wörter, Wortkombinationen sowie den Abstand zwischen diesen berücksichtigt. Die
Ergebnisse wurden manuell überprüft und für Verbesserungen des Programms genutzt.
Datenbasis waren Kurzbeschreibungen (bis zu 3.000 Wörter) zu 70.460 vom BMBF im
Zeitraum 2005 bis 2018 geförderten Forschungs‐ und Entwicklungsvorhaben.

Das Ergebnis zum Querschnittsthema Digitalisierung ist gemischt. Eine eindeutige Zu‐
ordnung von Vorhaben zu diesem Thema stellte sich als nicht praktikabel dar, da es viele
Vorhaben in einem Grenzbereich gab und das Themenfeld insgesamt sehr breit gestreut
ist. Es wurde daher eine restriktive und eine weniger restriktive Abgrenzung von Digita‐
lisierung umgesetzt. Auf Basis der restriktiveren Abgrenzung wurden fast 18.000 Vorha‐
ben mit bewilligten Fördermittel von insgesamt ca. 8,7 Mrd. EUR (d.h. durchschnittlich
rund 1.300 Vorhaben und rund 620 Mio. EUR pro Jahr) dem Themenfeld Digitalisierung
zugeordnet. Bei einer breiteren Abgrenzung ergeben sich rund 23.400  Vorhaben und
11,3  Mrd.  EUR  Fördermittel  (d.h.  knapp  1.700  Vorhaben  und  rund  810  Mio.  EUR  pro
Jahr). Der Anteil der vom BMBF geförderten Vorhaben, die dem Querschnittsthema Di‐
gitalisierung zugeordnet wurden, stieg für die restriktivere Abgrenzung von 18 % (2005)
auf 28 % (2018) und für die weniger restriktive von 25 auf 38 %. Zum Vergleich: Im För‐
derbereich "Informations‐ und Kommunikationstechnologien" der Leistungsplansyste‐
matik des Bundes (der häufig herangezogen wird, um Förderaktivitäten im Bereich Digi‐
talisierung zu erfassen) wurden pro Jahr weniger als 600 Vorhaben mit Fördermitteln
von knapp 250 Mio. EUR gefördert. Auf Basis der semantischen Analyse ergibt sich so‐
mit schon bei einer restriktiven Abgrenzung eine mehr als doppelt so hohe Förderakti‐
vität im Bereich Digitalisierung.

Vorhaben im Querschnittsthema Digitalisierung sind in allen Förderbereichen der Leis‐
tungsplansystematik anzutreffen. Besonders hoch ist ihr Anteil ‐ neben dem Bereich In‐
formations‐ und Kommunikationstechnologien ‐ in den Förderbereichen "FuE zur Ver‐
besserung der Arbeitsbedingungen und im Dienstleistungssektor", "Zivile Sicherheitsfor‐
schung",  "Produktionstechnologien"  und  "Innovationsrelevante  Rahmenbedingungen,
Querschnittsaktivitäten". Auf den letztgenannten Förderbereich entfällt sogar eine grö‐
ßere Anzahl an Vorhaben, die dem Querschnittsthema Digitalisierung zugeordnet wur‐

3

Identifizierung von Querschnittsthemen in Projekten der Direkten Projektförderung des BMBF
Bericht zu einer Machbarkeitsstudie

den, als auf den Bereich "Informations‐ und Kommunikationstechnologien". Dies unter‐
streicht  die  Bedeutung,  beim  Thema  Digitalisierung  über  den  klassischen  IKT‐Bereich
hinauszugehen.

Für das Themenfeld Künstliche Intelligenz ergibt die semantische Analyse eine Gesamt‐
zahl von mehr als 3.000 Vorhaben im Zeitraum 2005 bis 2018 mit bewilligten Fördermit‐
teln von 1,4 Mrd. EUR. Die Höhe der jährlich bewilligten Fördermittel stieg von 20 bis 30
Mio. EUR im Zeitraum 2005‐2007 auf ca. 300 Mio. EUR im Jahr 2018 kräftig an. Der Anteil
der dem Themenfeld Künstliche Intelligenz zugeordneten Vorhaben an allen vom BMBF
geförderten Vorhaben stieg von 1 % im Jahr 2007 auf fast 10 % im Jahr 2018 steil an.
Vorhaben zum Thema Künstliche Intelligenz finden sich in fast allen Förderbereichen,
besonders häufig in den Bereichen "Innovationsrelevante Rahmenbedingungen, Quer‐
schnittsaktivitäten", "Informations‐  und Kommunikationstechnologien",  "Produktions‐
technologien", Gesundheitsforschung, Gesundheitswirtschaft" und "FuE zur Verbesse‐
rung der Arbeitsbedingungen und im Dienstleistungssektor".

Das Ergebnis zum Querschnittsthema Soziale Innovationen erbrachte erheblich gerin‐
gere Fallzahlen. Für den Zeitraum 2005‐2018 konnten insgesamt 127 Vorhaben mit För‐
dermitteln von zusammen 101 Mio. EUR identifiziert werden. Es zeigt sich eine anstei‐
gende Tendenz der geförderten Vorhaben in diesem Themenfeld. Die meisten Vorhaben
zu Sozialen Innovationen finden sich in den Förderbereichen "Innovationsrelevante Rah‐
menbedingungen, Querschnittsaktivitäten" sowie "Klima, Umwelt, Nachhaltigkeit", ge‐
folgt von "FuE zur Verbesserung der Arbeitsbedingungen und im Dienstleistungssektor"
sowie "Geistes‐, Wirtschafts‐ und Sozialwissenschaften".

Zusätzlich zur semantischen Analyse wurde für das Teilgebiet Künstliche Intelligenz auch
ein Ansatz des Maschinellen Lernens getestet. Dieser Ansatz wäre deutlich weniger ar‐
beitsintensiv als semantische Analysen. Hierfür wurde ein neuronales Netzwerk mit ei‐
nem Trainingsdatensatz trainiert, der die über die semantische Analyse dem Themen‐
feld  Künstliche  Intelligenz  zugeordneten  Vorhaben  enthält.  Ein  Teil  dieser  Vorhaben
wurde dabei nicht als Trainingsdaten, sondern zur Evaluation der Zuverlässigkeit des An‐
satzes genutzt. Das Ergebnis ist nicht zufriedenstellend, da nur 68 % der über die se‐
mantische Analyse dem Thema Künstliche Intelligenz zugeordneten Vorhaben auch über
das maschinelle Lernen zugeordnet werden, während 22 % der über den maschinellen
Ansatz als Künstliche Intelligenz klassifizierten Vorhaben keine solchen sind. Ansätze des
maschinellen Lernens sind somit nicht gut geeignet, um Vorhaben auf Basis von Kurzbe‐
schreibungen  automatisiert  Querschnittsthemen  zuzuordnen.  Dies  liegt  u.a.  wohl  an
den relativen kurzen Texten der Abstracts, einem relativ hohen Standardisierungsgrad
der Abstracts und einer zu niedrigen Anzahl von Testdatensätzen, um die Vorteile von
maschinellem Lernen effizient nutzen zu können.

4

Identifizierung von Querschnittsthemen in Projekten der Direkten Projektförderung des BMBF
Bericht zu einer Machbarkeitsstudie

Executive Summary

This feasibility study explores the possibility of using semantic analysis of abstracts of
research projects to assign projects to cross‐cutting areas with a reasonable degree of
accuracy. The study focuses on two areas:

  Digitalisation (incl. the sub‐areas of Artificial Intelligence)

  Social Innovation

The semantic analysis is performed using a text analyses programme which considers
words and word combinations, and the distance between them. Results are manually
checked and used to improve the programme code. The analysis rests on extended ab‐
stracts (up to 3,000 words) from 70,460 R&D projects funded by the Federal Ministry
of Education and Research (BMBF) in the time period 2005 to 2018.

The results for the area digitalisation are mixed. It was not possible to unambiguously
assign projects to this area, as there were too many border‐line cases, and delineating
the digitalisation is difficult given the complexity of technologies and applications. For
that reason, a narrow and a broad demarcation of digitalisation was applied. Based on
the narrow approach, almost 18,000 projects with a total amount of public funding of
€8.7b have been assigned to the area of digitalisation (which is equal to about 1,300
projects and €620m of funds per year). The broader approach yields appr. 23,400 pro‐
jects and €11.3b of public money (almost 1,700 projects and €810m per year on aver‐
age). The share of projects in the area of digitalisation in the total number of R&D pro‐
jects funded by BMBF raised from 18% (2005) to 28% (2018) based on the narrow ap‐
proach, and from 25% to 38% based on the broader approach. These figures are more
than twice as high as compared to the results one obtains when analysing the funding
area "information and communication technologies" of the Federal Government's tax‐
onomy for assigning funding activities to research and technology fields (Leistungsplan‐
systematik ‐ LPS). In this area, the annual average number of funded projects is about
600 projects and the amount of funding about €250m per year.

R&D projects assigned to the area of digitalisation can be found in all research and tech‐
nology fields of the LPS. High shares of projects related to digitalisation are reported for
the  fields  "information  and  communication  technologies",  "R&D  to  improve  working
conditions / R&D in services", "civil security research", "production technologies" and
"innovation‐related framework conditions, cross‐cutting activities". The latter field com‐
prises a higher absolute number of projects in the area of digitalisation as compared to
the area of "information and communication technologies", stressing the importance of
taking a broader view when looking on government funding activities related to digital‐
isation.

For the area of Artificial Intelligence (AI), the study identified over 3,000 projects funded
during 2005 and 2018 with about €1.4b of public money. The amount of public funding

5

Identifizierung von Querschnittsthemen in Projekten der Direkten Projektförderung des BMBF
Bericht zu einer Machbarkeitsstudie

per years steadily increased from 20 to 30 million in the years 2005 to 2007 to almost
€300m in 2018. The share of projects assigned to AI in the total number of R&D projects
funded by the BMBF climbed from 1% in 2007 to almost 10% in 2018. Projects related
to AI can be found in almost all research and technology fields. The largest numbers of
projects are in the areas "innovation‐related framework conditions, cross‐cutting activ‐
ities",  "information  and  communication  technologies",  "production  technologies",
"health research and health sector" and "R&D to improve working conditions / R&D in
services".

In the area of social innovation, only a small number of projects were found. During
2005 and 2018, a total of 127 projects that received €101m of public funding have been
identified. There is a clear upwards trend in projects related to social innovation over
time. Most projects are found in the research areas "innovation‐related framework con‐
ditions, cross‐cutting activities" and "climate, environment, sustainability", followed by
"R&D to improve working conditions / R&D in services" and "humanities, economics and
social sciences".

In addition to the semantic analysis, a machine learning approach was applied in the
area of artificial intelligence in order to examine the feasibility of a more automated way
of identifying cross‐cutting areas. A neural network was trained based on data from the
projects that have been assigned to AI through the semantic analysis, setting aside a
fraction of these project for evaluating the accuracy of the machine learning approach.
The  result  is  unsatisfactory.  The  neural  network  assigned  only  68%  of  all  AI  projects
correctly as AI, whereas 22% of all projects assigned to AI by the neural network were
not classified as AI by the semantic analysis. Machine learning approaches do not seem
to be useful for this particular problem of assigned research projects to cross‐cutting
areas based on project abstracts. Among others, extended abstracts represent rather
short and relatively standardised texts while the number of observations is too small for
an efficient use of machine learning tools.

6

Identifizierung von Querschnittsthemen in Projekten der Direkten Projektförderung des BMBF
Bericht zu einer Machbarkeitsstudie

1

Aufgabenstellung und Zielsetzung

Bei den Nutzern des Informationssystems PROFI ‐ Fördermittelgeber, Politik und allge‐
meine Öffentlichkeit ‐ besteht immer wieder der Bedarf, Aussagen über die FuE‐Förder‐
tätigkeit des Bundes in neu aufkommenden Themenfeldern oder in Themenfeldern, die
über die Grenzen einzelner Forschungsbereiche und Technologien hinausgehen, treffen
zu können. Allein mit Hilfe der Leistungsplansystematik1 ist dies für solche Querschnitts‐
themen meist nicht möglich. Ein Beispiel hierfür ist das Thema Digitalisierung und Ver‐
fahren der Künstlichen Intelligenz. Die Digitalisierung spielt in verschiedensten Themen‐
feldern eine wichtige Rolle, zu denen nicht nur die Informations‐ und Kommunikations‐
technologien zählen, sondern auch Produktionstechnologien, Fahrzeug‐ und Verkehrs‐
technologien  sowie  die  Bereiche  Klima,  Umwelt,  Nachhaltigkeit  und  Gesundheitsfor‐
schung, Gesundheitswirtschaft. Künstliche Intelligenz unterstützt Ärzte bei ihren Diag‐
nosen, Smart‐Meter managen den Stromverbrauch von Haushalten und Supercomputer
ermöglichen eine schnellere Verarbeitung jeglicher Informationen. Die Anzahl der An‐
wendungen ist groß und eine klare Zuordnung der Digitalisierung zu einzelnen Schwer‐
punkten der Leistungsplansystematik nicht möglich. Auch lässt die hohe Geschwindig‐
keit der technologischen Entwicklung im Bereich Digitalisierung keine langfristige An‐
passung  der  Leistungsplansystematik  zu.  Themen  die  heute  noch  eine  wichtige  Rolle
spielen, können in wenigen Jahren bereits wieder redundant sein, während völlig neue
Themen hinzugekommen sind.

Die vorliegende Machbarkeitsstudie prüft, inwieweit solche Querschnittsthemen durch
eine  semantische  Analyse  der  Beschreibungen  geförderter  FuE‐Vorhaben  mit  hinrei‐
chender Genauigkeit identifiziert werden können und welcher Aufwand notwendig ist,
um eine solche Analyse umzusetzen.

Die Machbarkeitsstudie umfasst folgende Schritte:

  Grundlage der Textanalyse bilden die Abstracts der seit 2005 vom BMBF geför‐
derten Vorhaben. Die vom BMBF bereitgestellten Daten werden aufbereitet und
durch weitere Informationen aus der PROFI‐Datenbank (siehe Box 1) ergänzt, ins‐
besondere durch Informationen über die Leistungsplansystematik, die Finanzie‐
rungszeiträume sowie die Förderdauern und Bewilligungssummen der einzelnen
Vorhaben.

  Mit Hilfe eines Textanalyseprogramms wird nach Schlagwörtern und Schlagwort‐
kombinationen  gesucht  (semantische  Analyse),  die  auf  ein  Querschnittsthema
hinweisen, oder Hinweise darauf geben, dass trotz Vorliegens eines Schlagworts

1 Die Leistungsplansystematik ist eine Systematik zur Zuordnung von FuE‐Förderungen zu Forschungsthe‐
men, vgl. Abschnitt 2.

7

Identifizierung von Querschnittsthemen in Projekten der Direkten Projektförderung des BMBF
Bericht zu einer Machbarkeitsstudie

das Projekt nicht in das entsprechende Themenfeld gehört. Es werden drei The‐
menfelder betrachtet:

  Abschnitt  3.1:  Erstes  Querschnittsthema  ist  die  Digitalisierung.  Ausgangs‐
punkt bildet eine existierende Analyse zu digitalen Geschäftsmodellen. Diese
wurde vom ZEW erstellt und anhand von Geschäftstätigkeitsbeschreibungen
junger Unternehmen kalibriert. Innerhalb dieser Studie wird die Anwendbar‐
keit  der  Analyse  auf  Vorhabenbeschreibungen  überprüft  und  weiterentwi‐
ckelt.

  Abschnitt 3.2: Innerhalb des Querschnittsthemas "Digitalisierung" wird die Ka‐
tegorie "Künstliche Intelligenz" gesondert betrachtet. Hierfür wird ein eige‐
nes Textfeldanalyseprogramm entwickelt und implementiert.

  Abschnitt 3.3: Als zweites Querschnittsthema wird "Soziale Innovationen" un‐
tersucht. Hierfür wird ein neues Textfeldanalyseprogramm entwickelt und im‐
plementiert.

  Zuletzt wird ein weiteres Analysetool basierend auf Methoden des Maschinellen
Lernens getestet. Dieses Analysetool hat den Vorteil, dass die Zuordnung von Vor‐
haben zu Querschnittsthemen bzw. Themenfeldern automatisiert vorgenommen
werden kann, was den Bearbeitungsaufwand im Vergleich zu einer semantischen
Analyse deutlich reduziert. Hierzu wird auf die Ergebnisse aus Abschnitt 3.2 zu
Förderungen im Bereich Künstliche Intelligenz zurückgegriffen. Es wird getestet,
inwiefern  ein  trainierter,  automatisierter  Algorithmus  geeignet  ist,  um  dieses
Themenfeld in den Abstracts von geförderten Vorhaben zu identifizieren.

8

Identifizierung von Querschnittsthemen in Projekten der Direkten Projektförderung des BMBF
Bericht zu einer Machbarkeitsstudie

2

Datenbasis

Datengrundlage der Machbarkeitsstudie sind alle vom BMBF geförderten Forschungs‐
und Entwicklungsvorhaben (im Folgenden kurz: Vorhaben), die in den Jahren 2005 bis
2018 im Rahmen der Direkten Projektförderung bewilligt wurden. Dabei handelt es sich
um 70.460 Vorhaben. Die Fördersumme (bewilligte Mittel) für diese Vorhaben beläuft
sich auf ca. 63,8 Mrd. EUR.

Zu jedem Vorhaben wurden dem ZEW vom BMBF Titel und Kurzbeschreibung zur Verfü‐
gung gestellt. Diese Informationen wurden um weitere Informationen aus der PROFI‐
Datenbank (siehe Box 1), die dem ZEW im Rahmen des Projekts „Monitoring der Betei‐
ligung von KMU an der Direkten Projektförderung“ vorliegen, ergänzt. Dazu zählen u.a.
die Zuordnung zur Leistungsplansystematik, die Bewilligungssumme und der Vorhaben‐
zeitraum.

Box 1: PROFI‐Datenbank

Die  Datenbank  "Projektförder‐Informationssystem"  (PROFI)  ist  ein  Instrument  für  die
Abwicklung von Zuwendungen und Aufträgen durch den Bund. Die Datenbank enthält
Informationen zu den einzelnen geförderten oder beauftragten Vorhaben. Zu geförder‐
ten FuE‐Vorhaben liegt u.a. eine Kurzbeschreibung des Vorhabens (Abstract) vor. Der
Text wird von den Zuwendungsempfängern erstellt und mit der Antragstellung vorge‐
legt. Jedes Vorhaben ist außerdem einer Nummer der Leistungsplansystematik (siehe
Box 2) zugeordnet.

Abbildung 1 zeigt die Anzahl der pro Jahr neu bewilligten Vorhaben und die Höhe der
bewilligten Mittel. Sowohl die Anzahl der Vorhaben wie die Bewilligungssumme nahmen
im betrachteten Zeitraum zu. Die Anzahl der bewilligten Vorhaben stieg von 3.537 im
Jahr 2005 auf 5.798 im Jahr 2018, die Höhe der bewilligten Mittel nahm von rund 1,9
Mrd. EUR im Jahr 2005 auf 3,0 Mrd. EUR im Jahr 2018 zu.2

Die verwendete Datengrundlage deckt nicht alle Förderbereiche der Leistungsplansys‐
tematik (siehe Box 2) ab, da die Projektförderung des BMBF nicht alle Förderbereiche
umfasst. Nicht abgedeckt sind in dieser Studie die Förderbereiche D (Ernährung, Land‐
wirtschaft, Verbraucherschutz), H (Fahrzeug‐ und Verkehrstechnologien inkl. maritimer
Technologien), I (Luft‐ und Raumfahrt) und Q (Innovationsförderung des Mittelstands).
Für andere Förderbereiche wie z.B. E (Energieforschung und Energietechnologien) und

2  Diese Zahlen enthalten nicht den Förderbereich T "Förderorganisationen, hochschulbezogene Sonder‐
programme".

9

Identifizierung von Querschnittsthemen in Projekten der Direkten Projektförderung des BMBF
Bericht zu einer Machbarkeitsstudie

N (Raumordnung und Stadtentwicklung, Bauforschung) repräsentieren die in diese Stu‐
die einbezogenen Vorhaben nur einen kleineren Teil der gesamten Förderaktivitäten des
Bundes.

Abbildung 1:  Anzahl und bewilligte Mittel vom BMBF geförderter Vorhaben* 2005‐

2018

.

d
s
T
n

i

n
e
b
a
h
r
o
V
e
t
g

i
l
l
i

w
e
b

l

h
a
z
n
A

8

7

6

5

4

3

2

1

0

neu geförderte Vorhaben

neu bewilligte Mittel

4.0

3.5

3.0

2.5

2.0

1.5

1.0

0.5

0.0

€

.

d
r
M
n

i

l

e
t
t
i

M
n
e
t
g

i
l
l
i

w
e
b
r
e
d
e
h
ö
H

5
0
0
2

6
0
0
2

7
0
0
2

8
0
0
2

9
0
0
2

0
1
0
2

1
1
0
2

2
1
0
2

3
1
0
2

4
1
0
2

5
1
0
2

6
1
0
2

7
1
0
2

8
1
0
2

*ohne Leistungsplanbereich T.
Quelle: PROFI‐Datenbank, Berechnungen des ZEW.

Box 2: Leistungsplansystematik

Die Leistungsplansystematik des Bundes gruppiert die Forschungsausgaben des Bundes
nach forschungsthematischen Gesichtspunkten. Sie unterscheidet dabei übergeordnete
Forschungsbereiche (Förderbereiche), die in Forschungsschwerpunkte (Förderschwer‐
punkte)  und  weiter  in  Unterklassen  unterteilt  sind.  Mit  der  Leistungsplansystematik
werden die FuE‐Ausgaben des Bundes unabhängig vom finanzierenden Ressort einzel‐
nen Forschungsthemen zugeordnet. Jedes geförderte Vorhaben wird dabei einer Leis‐
tungsplan‐Nummer  zugeordnet.  Da  die  Zuordnung  nach  dem  Schwerpunktprinzip  er‐
folgt,  ist  eine  Mehrfachzuordnung  zu  verschiedenen  Förderbereichen  nicht  möglich.
Dies kann insbesondere bei interdisziplinär ausgerichteten Vorhaben zu Unschärfen füh‐
ren.  Zudem  sind  Querschnittsthemen  kaum  über  die  Leistungsplansystematik  abbild‐
bar.3

3 Vgl. BMBF (2018), Bundesbericht Forschung und Innovation 2018. Datenband, S. 146. Berlin.

10

Identifizierung von Querschnittsthemen in Projekten der Direkten Projektförderung des BMBF
Bericht zu einer Machbarkeitsstudie

3

TexAn‐Textfeldanalyse

Die in dieser Studie durchgeführten semantischen Analysen ("Textfeldanalysen") nutzen
eine vom ZEW entwickelte Software, die die Bezeichnung "TexAn – Text Analyser" führt.
Diese Software erlaubt es, Texte nach Schlagwörtern, Wortteilen und Schlagwortkom‐
binationen (unter Berücksichtigung der Distanz zwischen Wörtern sowie positiver und
negativer Beziehungen) zu durchsuchen und zu vom Anwender definierten Klassen zu‐
zuordnen. Im Rahmen dieser Machbarkeitsstudie wird der aus Titeln und Abstracts eines
Vorhabens gebildete Textkorpus klassifiziert.

Innerhalb der Textanalyse ist es wichtig, die Anzahl an fehlerhaften Klassifizierungen zu
minimieren. Zum einen sollte es möglichst wenig "False‐Negatives" geben, sprich mög‐
lichst wenig Vorhaben sollen beispielsweise als nicht‐digital eingestuft werden, obwohl
sie eigentlich dem Bereich Digitalisierung zuzurechnen sind. Zum anderen sollten auch
möglichst wenig "False‐Positives" entstehen, sprich möglichst wenig Vorhaben sollten
als digital eingestuft werden, obwohl sie es nicht sind. In Bezug auf die Machbarkeits‐
studie würde eine zu große Menge von False‐Negatives eine Unterschätzung der För‐
deraktivitäten bedeuten, eine zu große Menge von False‐Positives eine Überschätzung.
Demnach ist die Klassifizierung eines Querschnittsthemas mit Hilfe der Textfeldanalyse
nur machbar, wenn eine hinreichend niedrige Anzahl von beiden Arten von Fehlern er‐
reicht wird. Das Austarieren beider Arten von Fehlern und die wiederholte Anpassung
der Textfeldanalyse ist daher ein Schlüsselelement des Projekts. Die entwickelten kon‐
kreten TexAn‐Analysecodes zu den Querschnittsthemen Digitalisierung, künstliche Intel‐
ligenz und Soziale Innovationen befinden sich im Anhang.

3.1

TexAn‐Analyse zum Querschnittsthema Digitalisierung

Für die Textfeldanalyse zum Querschnittsthema Digitalisierung wurde zunächst unter‐
sucht, ob die zuvor vom ZEW durchgeführte semantische Analyse zu digitalen Geschäfts‐
modellen junger Unternehmen4 geeignet ist, um geförderte Vorhaben des BMBF im The‐
menfeld  Digitalisierung zu  erkennen.  Hierzu  betrachten  wir  den  Anteil der  mit  dieser
Analyse dem Querschnittsthema Digitalisierung zugeordneten Vorhaben innerhalb ei‐
ner Zusammenstellung von 4.351 Vorhaben aus verschiedenen Leistungsplanklassen mit
einem besonders hohen Potenzial, digitale Themen zu beinhalten (siehe Tabelle 1). Iden‐
tifiziert wurde diese Liste an Leistungsplanklassen, durch einen manuellen Themenab‐
gleich der Leistungsplanklassen anhand ihres Titels, mit den Themen der digitalen Ge‐
schäftsfeldanalyse des ZEWs. In Leistungsplanklassen mit einem auffällig geringen Anteil

4  Dabei  wurden  die  Geschäftstätigkeitsbeschreibungen  von  Unternehmen,  die  in  der  Datenbank  des
Mannheimer Unternehmenspanels vorlagen, analysiert. Geschäftstätigkeitsbeschreibungen stellen rela‐
tiv stark standardisierte Texte dar, in denen die zentralen Tätigkeiten und Marktangebote eines Unter‐
nehmens beschrieben werden.

11

Identifizierung von Querschnittsthemen in Projekten der Direkten Projektförderung des BMBF
Bericht zu einer Machbarkeitsstudie

wurde  eine  Stichprobe  von  potenziell  inkorrekten  negativ  klassifizierten  Vorhaben
(False‐Negatives) gezogen und manuell überprüft. Ziel der Überprüfung war es, notwen‐
dige Anpassungen in der Textfeldanalyse zu identifizieren. Anschließend wurden diese
Anpassungen vorgenommen und eine erneute Analyse durchgeführt. Dieses Vorgehen
wurde so lange wiederholt, bis die Anzahl negativer Fehlklassifikationen sehr gering war.

Im Anschluss wurde die auf diese Weise erstellte Textfeldanalyse auf alle vorliegenden
70.460 Vorhaben angewendet. An dieser Stelle war es notwendig, eine Überprüfung auf
inkorrekt positiv klassifizierte Vorhaben (False‐Positives) durchzuführen. Hierzu wurde
eine Stichprobe von als "digital" klassifizierten Vorhaben aus den verschiedenen Leis‐
tungsplanklassen manuell begutachtet und die Textfeldanalyse auch hier im Falle feh‐
lerhafter Klassifikationen angepasst. Anschließend wurde die veränderte Textfeldana‐
lyse erneut durchgeführt und auf die gleiche Weise erneut auf inkorrekte positive Klas‐
sifikationen untersucht. Auch wurde an dieser Stelle die Veränderung des Anteils der
dem  Querschnittsthema  Digitalisierung  zugeordneten  Vorhaben  in  den  Leistungs‐
planklassen aus Tabelle 1 nochmals überprüft, um sicherzugehen, dass durch die Anpas‐
sungen der Analyse keine bedeutende Anzahl an inkorrekten negativen Klassifikationen
entstanden ist. Dieses Vorgehen wurde iterativ wiederholt, bis die Anzahl von False‐Ne‐
gatives und False‐Positives sehr gering war.

Die semantische Analyse auf Basis des ursprünglich vom ZEW entwickelten Textanaly‐
seprogramms zum Querschnittsthema Digitalisierung (Analyse der Geschäftstätigkeits‐
beschreibungen  von  Startups)  erwies  sich  als  nicht  geeignet  für  den  Textkorpus  der
BMBF‐geförderten  Vorhaben.  Viele  Vorhaben  der  Leistungsplanklassen  aus  Tabelle  1
wurden nicht als "digital" erkannt. Dies lag daran, dass die ursprünglich verwendeten
zehn  Unterkategorien  zur  Beschreibung  des  Querschnittsthemas  "Digitalisierung"  zu
eng  abgegrenzt  waren  und  wesentliche  Digitalisierungsfelder  nicht  erfasst  haben.  Sie
wurden daher innerhalb mehrerer Wiederholungsrunden in ihren Stichwortkombinati‐
onen erweitert und um 13 weitere Unterkategorien ergänzt.5

Die  Unterkategorie  zur  Künstlichen  Intelligenz  umfasste  beispielweise  ursprünglich
überwiegend  verschiedene  Schreibweisen  des  Begriffs  "künstliche  Intelligenz".  Sie
wurde unter anderem durch Begriffe zu maschinellem Lernen und neuronalen Netzten
ergänzt. Hinzugefügte Unterkategorien zur Digitalisierung sind beispielsweise Cybersi‐
cherheit, Internet der Dinge sowie intelligente Produkte und Dienstleistungen. Als be‐
sondere  Herausforderung  des  Querschnittsthemas  Digitalisierung  zeigte  sich  bereits
hier seine große Themenbereite, welche ein besonders zeitaufwendiges Prüfen der als
nicht‐digital klassifizierten Vorhaben nötig machte, da jede Unterkategorie der Digitali‐
sierung ihre eigenen Schlagwortkombinationen erfordert.

5 Eine finale Liste der genutzten Unterkategorien der Digitalisierung findet sich in Tabelle 4 im Anhang.

12

Identifizierung von Querschnittsthemen in Projekten der Direkten Projektförderung des BMBF
Bericht zu einer Machbarkeitsstudie

Tabelle 1:

Leistungsplanklassen mit hohem Potenzial für das Querschnittsthema
Digitalisierung

LP‐Name

Integrierte Anwendungssysteme

Instrumente, Methoden sowie Plattformen und Netzwerke

LP‐ID
AA0240  Computational Neuroscience
FA3061  Datenmanagement
FA5060
GA1010  Entwicklung von Softwaremethoden und ‐Werkzeugen
GA1011  Eingebettete Systeme
GA1012
GA1040  Korrektheit und Redundanz bei Informationssystemen
GA1050  Manipulationssicherheit von Informationssystemen
GA1060  Sicherheit in DV‐Netzen
GA1080  Sonstiges im Rahmen der Softwaretechnologie
GA2010  Parallelarchitekturen
GA2020  Parallelsoftware
GA2030  Mathematische Grundlagen der wissenschaftlichen Computeranwendungen
GA2040  Modellierung / Simulation
GA2060  GRID
GA2080  Sonstiges im Rahmen des Höchstleistungsrechnens
GA4010  Neuronale Netze und ihre Anwendungen
GA4030  Erkennen und Verstehen von Schrift und Bildern
GA4040  Wissensverarbeitung/Expertensysteme
GA4080  Sonstiges im Rahmen der intelligenten Systeme
GA5010  Erkennen, Verstehen und Übersetzen von Sprache
GA5020
GA5030  Virtuelle Realität / Erweiterte Realität
GA5080  Sprachtechnologie und Mensch‐Maschine‐Kommunikation
GA9010  Analysen, Prognosen und Auswertungen Informatik
GA9020
GA9081  DV‐Systeme und ‐Technologien (abgeschl. DV‐Progr.)
GA9099  Sonstiges (auch Normung) im Rahmen der Informatik
GB1010  Arbeitsprogramm IT‐Sicherheit
GB1011
GB1012
GB1013  Hightech für die IT‐Sicherheit
GB1070  Quanteninformationstechnologie
GB1080  Privatheit in der digitalen Welt
GB1099
GB2010  Netzbasierte Dienste in der Medizin
GB2011  Netzbasierte Dienste im Verkehr
GB2099
GB8040
GB9099
GC2020  Aufbau‐ u. Verbindungstechnik, 3 D ‐ Integration
GC2025  Chipbasierte Sicherheit für die Digitalisierung

Sicheres Cloud‐Computing
IT‐Sicherheit in Kritischen Infrastrukturen

Internationale Zusammenarbeit im Rahmen der Informationsverarbeitung

Intelligente Methoden der Mensch‐Maschine‐Kommunikation

Sonstiges im Rahmen der IT‐Sicherheit

Sonstiges im Rahmen der Netzbasierten Dienste
Internettechnologien
Sonstiges im Rahmen der Kommunikationstechnologie (einschl. Querschnittsunters.)

Quelle: Zusammenstellung des ZEW

13

Identifizierung von Querschnittsthemen in Projekten der Direkten Projektförderung des BMBF
Bericht zu einer Machbarkeitsstudie

Die Anwendung der auf diese Art erstellten Textfeldanalyse auf alle vom BMBF neu ge‐
förderten Vorhaben im Zeitraum von 2005 bis 2018 führte in ihren ersten Runde zu einer
hohen  Anzahl  von  inkorrekt  als  digital  klassifizierten  Vorhaben.  Die  Unterkategorie
Künstliche  Intelligenz  klassifizierte  beispielsweise  fälschlicherweise  Vorhaben  im  Be‐
reich der Neurobiologie ohne Verknüpfung zur künstlichen Intelligenz als digital. Wei‐
tere Beispiele sind die Unterkategorien selbstfahrende Fahrzeuge, integrierten Systeme
oder automatisches Erkennen von Bildern und Tönen. Hier lösten Wörter wie „Verfah‐
ren“  oder  „Anerkennung“  fälschlich  positive  Klassifikationen  aus,  da  sie  die  Wortbe‐
standteile „fahren“ und „erkenn“ beinhalteten. Auch wurden Vorhaben noch anhand
verschiedener Arten integrierter, aber nicht notwendigerweise digitaler, Systeme, wie
Ökosystemen oder Wassernetzwerke, als digital eingestuft. Zur Vermeidung dieser Fehl‐
klassifikationen  wurden  Nebenbedingungen  zu  den  entsprechenden  Unterkategorien
hinzugefügt. Vereinfacht dargestellt mussten etwa für eine Klassifikation als digital in
der  Unterkategorie  Künstliche  Intelligenz  neben  den  Worten  „neuronal“  und  „Netz“
auch weitere Worte wie „Algorithmus“, „selbstlernend“ oder „automatisiert“ innerhalb
eines definierten Wortabstandes im Textfeld vorkommen.

Das Ergebnis der wiederholten Anpassung der TexAn‐Analyse sind zwei alternative Text‐
feldanalysen. Eine Textfeldanalyse ist restriktiver und verkleinert die Wahrscheinlichkeit
von inkorrekt positiven Klassifikationen, die andere ist weniger restriktiv und verkleinert
die Wahrscheinlichkeit inkorrekt negativer Klassifikationen. Hauptunterschied zwischen
den beiden Varianten sind vier Unterkategorien, die nicht in der restriktiven, aber in der
weniger restriktiven Analyse enthalten sind.6 In der weniger restriktiven Variante sind
z.B. simple Schlagwörter wie „digital“, „IKT“ und „Internet“ ohne weitere Restriktionen
enthalten. Zum anderen umfasst die weniger restriktive Variante die Unterkategorie "in‐
tegrierte Systeme", da diese bis zuletzt relativ fehleranfällig für False‐Positives geblieben
ist. Der Grund für das Erstellen von zwei unterschiedlichen Textfeldanalysen zur Digita‐
lisierung ist erneut der Breite des Themas geschuldet. Diese erschwert eine eindeutige
Abgrenzung von Vorhaben als "digital" und "nicht‐digital". Deshalb empfehlen wir, zwei
Varianten zu verwenden und die Ergebnisse als Ober‐ und Untergrenzen zu interpretie‐
ren.

Die restriktivere Analyse identifiziert 84  % der Vorhaben in den Leistungsplanklassen
mit hohem Digitalisierungspotenzial als "digital". Angewendet auf alle Leistungsplanbe‐
reiche  werden  17.923  Vorhaben  des  Bewilligungszeitraums  2005‐2018  dem  Quer‐
schnittsthema Digitalisierung zugeordnet. Die weniger restriktive Variante identifiziert
91  % der Vorhaben in den Leistungsplanklassen mit hohem Digitalisierungspotenzial als
"digital". und weist insgesamt 23.388 Vorhaben dem Querschnittsthema zu. Dies ent‐

6 Die finale Liste der genutzten Unterkategorien in Tabelle 4 im Anhang zeigt, welche Unterkategorien in
welcher Analyse genutzt wurden.

14

Identifizierung von Querschnittsthemen in Projekten der Direkten Projektförderung des BMBF
Bericht zu einer Machbarkeitsstudie

spricht einer Bewilligungssumme von 8,7 Mrd. EUR (restriktiv) und 11,3 Mrd. EUR (we‐
niger  restriktiv)  im  Querschnittsthema  Digitalisierung  und  demonstriert  einen  merkli‐
chen  Niveauunterschied  zwischen  den  beiden  Analysen.  Abbildung  2  zeigt  allerdings,
dass das prozentuale Wachstum der jährlichen neuen Bewilligungssummen im Zeitraum
von 2006 bis 2018 weitestgehend gleichverläuft. Demnach unterscheiden sich die Ana‐
lysen zwar in ihren Niveaus, folgen aber der gleichen Entwicklung.

Abbildung 2:   Jährliches Wachstum der bewilligten Mittel von neu geförderten
Vorhaben* zum Thema Digitalisierung 2006‐2018

weniger restriktive
Textfeldanalyse
restriktivere
Textfeldanalyse

100%

80%

60%

40%

20%

0%

‐20%

‐40%

‐60%

6
0
0
2

7
0
0
2

8
0
0
2

9
0
0
2

0
1
0
2

1
1
0
2

2
1
0
2

3
1
0
2

4
1
0
2

5
1
0
2

6
1
0
2

7
1
0
2

8
1
0
2

* ohne Leistungsplanbereich T
Quelle: PROFI‐Datenbank, Vorhabenbeschreibungen des BMBF, Berechnungen des ZEW.

Abbildung 3 und Abbildung 4 zeigen die Höhe der bewilligten Mittel im Querschnitts‐
thema Digitalisierung in den einzelnen Beobachtungsjahren sowie den Anteil dieser Mit‐
tel an der Gesamtbewilligungssumme des BMBF pro Jahr. Beide Grafiken zeigen einen
ansteigenden Trend beider Werte und verlaufen zwar auf unterschiedlichen Niveaus,
aber parallel. Im Durchschnitt identifiziert die weniger restriktive Analyse einen um 7  %‐
Punkte höheren Anteil (absolut: ca. 175 Mio. EUR mehr an Bewilligungen pro Jahr). Ab‐
solut betrachtet stiegt die jährliche Bewilligungssumme von Vorhaben im Bereich Digi‐
talisierung zwischen 2005 und 2018 von 322 Mio. auf 1,06 Mrd. EUR (bei weniger rest‐
riktiver Abgrenzung: von 474 Mio. auf 1,14 Mrd. EUR). Der Anteil erhöhte sich von 17  %
auf 28  %, beziehungsweise von 26  % auf 38  %.

15

Identifizierung von Querschnittsthemen in Projekten der Direkten Projektförderung des BMBF
Bericht zu einer Machbarkeitsstudie

Abbildung 3:  Bewilligte Mittel von neu geförderten Vorhaben* zum

Querschnittsthema Digitalisierung 2005‐2018

R
U
E
.

i

o
M
n

i

l

e
t
t
i

M
e
t
g

i
l
l
i

w
e
B

weniger restriktive Textfeldanalyse

restriktivere Textfeldanalyse

1600

1400

1200

1000

800

600

400

200

0

5
0
0
2

6
0
0
2

7
0
0
2

8
0
0
2

9
0
0
2

0
1
0
2

1
1
0
2

2
1
0
2

3
1
0
2

4
1
0
2

5
1
0
2

6
1
0
2

7
1
0
2

8
1
0
2

*

ohne Leistungsplanbereiche T
Quelle: PROFI‐Datenbank, Vorhabenbeschreibungen des BMBF, Berechnungen des ZEW.

Abbildung 4:  Anteil bewilligter Mittel von neu geförderten Vorhaben* zum

Querschnittsthema Digitalisierung am gesamten Bewilligungsvolumen
des BMBF 2005‐2018

weniger restriktive Textfeldanalyse
restriktivere Textfeldanalyse

e
m
m
u
s
s
g
n
u
g

i
l
l
i

w
e
B
r
e
t
m
a
s
e
g
n
a

l
i

e
t
n
A

45%

40%

35%

30%

25%

20%

15%

10%

5%

0%

5
0
0
2

6
0
0
2

7
0
0
2

8
0
0
2

9
0
0
2

0
1
0
2

1
1
0
2

2
1
0
2

3
1
0
2

4
1
0
2

5
1
0
2

6
1
0
2

7
1
0
2

8
1
0
2

ohne Leistungsplanbereiche T
Quelle: PROFI‐Datenbank, Vorhabenbeschreibungen des BMBF, Berechnungen des ZEW.

*s

16

Identifizierung von Querschnittsthemen in Projekten der Direkten Projektförderung des BMBF
Bericht zu einer Machbarkeitsstudie

Abbildung 5 verdeutlicht außerdem eine ähnliche Rangordnung der Leistungsplanberei‐
che in ihrer Digitalisierungsintensität in beiden Analysen. Auch plausibilisiert die Digita‐
lisierungsintensität, gemessen als Anteil der bewilligten Mittel im Themenbereich Digi‐
talisierung innerhalb eines Leistungsplanbereichs, die Ergebnisse unsere TeXan‐Analy‐
sen. Leistungsplanbereiche, in denen viele Vorhaben mit Digitalisierungsinhalten erwar‐
tet  werden  können,  insbesondere  „G  –  Informations‐  und  Kommunikationstechnolo‐
gien“, belegen die obersten Ränge der gezeigten Anordnung.

Abbildung 6 und Abbildung 7 zeigen die absoluten Bewilligungssummen sowie die An‐
zahl neu geförderter Vorhaben je Leistungsplanbereich. Hier ist zu erkennen, dass die
meisten  Vorhaben  im  Querschnittsthema  Digitalisierung  und  die  meisten  bewilligten
Mittel  mit  großem  Abstand  in  den  Leistungsplanbereichen  „R  –  Innovationsrelevante
Rahmenbedingungen und übrige Querschnittsaktivitäten“ und „G – Informations‐ und
Kommunikationstechnologien“  anfallen.  Die  beiden  nächstgrößeren  Leistungsplanbe‐
reiche in Bezug auf die absolute Höhe der Förderung von Vorhaben im Querschnitts‐
thema Digitalisierung sind „A – Gesundheitsforschung und Gesundheitswirtschaft“ und
„F – Klima, Umwelt, Nachhaltigkeit“. Es ist nicht überraschend, dass die absoluten Zah‐
len der Bereiche R, A und F hoch sind, obwohl ihr Rang in Bezug auf den Anteil von Vor‐
haben, die dem Querschnittsthema Digitalisierung zugeordnet wurden, relativ niedrig
ist. Der Grund hierfür liegt in den insgesamt hohen Fördersummen in diesen Leistungs‐
planbereichen.

Insgesamt hat die Zuordnung von Vorhaben des BMBF zum Querschnittsthema Digitali‐
sierung einen nicht unerheblichen Arbeitseinsatz erfordert. Insgesamt war ein wissen‐
schaftlicher Mitarbeiter über einen Zeitraum von vier Kalendermonaten im Umfang von
ca. 150 Arbeitsstunden damit beschäftigt. Der Arbeitsaufwand entstand insbesondere
durch die breite und schwierige Abgrenzbarkeit des Querschnittsthemas Digitalisierung
und der vielen Iterationen (insgesamt acht Runden), um False‐Negatives und False‐Po‐
sitives weitgehend auszuschließen. Eine kurzfristige Durchführung solch einer Analyse
zu einem vergleichbar komplexen Querschnittsthemenfeld ist daher nicht machbar.

Des Weiteren ist zu beachten, dass in einem so dynamischen Themenfeld wie der Digi‐
talisierung eine regelmäßige Anpassung und Prüfung der semantischen Textfeldanalyse
notwendig  ist.  Die  jetzt  vorliegende  Textfeldanalyse  kann  vermutlich  noch  für  einige
Jahre zuverlässige Ergebnisse bringen. In spätestens fünf Jahren ist nach unserer Ein‐
schätzung jedoch eine Überarbeitung notwendig, für die ein substanzieller Arbeitsauf‐
wand (ca. die Hälfte des in dieser Studie benötigten Aufwands) zu veranschlagen ist.

17

Identifizierung von Querschnittsthemen in Projekten der Direkten Projektförderung des BMBF
Bericht zu einer Machbarkeitsstudie

Abbildung 5:  Anteil bewilligter Mittel von neu geförderten Vorhaben zum Querschnittsthema Digitalisierung am gesamten

Bewilligungsvolumen nach Leistungsplanbereichen

Informations‐ und Kommunikationstechnologien ‐ G

FuE zur Verbesserung der Arbeitsbeding. und im Dienstleistungssek. ‐ J

Zivile Sicherheitsforschung ‐ C

Produktionstechnologien ‐ M

Inno. relev. Rahmenbedingungen und übrige Querschnittsaktivitäten ‐ R

Optische Technologien ‐ L

Bioökonomie ‐ B

Klima, Umwelt, Nachhaltigkeit ‐ F

Gesundheitsforschung und Gesundheitswirtschaft ‐ A

Geisteswissenschaften; Wirtschafts‐ und Sozialwissenschaften ‐ P

Nanotechnologien und Werkstofftechnologien ‐ K

Innovationen in der Bildung ‐ O

Großgeräte der Grundlagenforschung ‐ U

Energieforschung und Energietechnologien ‐ E

Förderorganisationen, hochschulbezogene Sonderprogramme, etc. ‐ T

Raumordnung und Stadtentwicklung; Bauforschung ‐ N

28%

17%

24%

18%

22%

13%

15%

21%

20%

10%

19%

12%

15%

7%

13%

10%

12%

4%

5%

1%
1%

0%
1%

64%

72%

50%

46%

43%

37%

34%

37%

37%

restriktivere Textfeldanalyse

weniger restriktive Textfeldanalyse

0%
Quelle: PROFI‐Datenbank, Vorhabenbeschreibungen des BMBF, Berechnungen des ZEW

20%

40%

60%

80%

18

Abbildung 6:  Anzahl und bewilligte Mittel von neu geförderten Vorhaben zum Querschnittsthema Digitalisierung nach

Leistungsplanbereichen, restriktivere Abgrenzung

Identifizierung von Querschnittsthemen in Projekten der Direkten Projektförderung des BMBF
Bericht zu einer Machbarkeitsstudie

neu geförderte Vorhaben

neu bewilligte Mittel

7

6

5

4

3

2

1

0

.

d
s
T
n

i

n
e
b
a
h
r
o
V
r
e
t
r
e
d
r
ö
f
e
g

l

h
a
z
n
A

A B C E

F G J

K

L M N O P R T U

Quelle: PROFI‐Datenbank, Vorhabenbeschreibungen des BMBF, Berechnungen des ZEW.

3.5

3.0

2.5

2.0

1.5

1.0

0.5

0.0

jkghk

iüko kjh

A
B
C
E
F
G
J

k

l

l

ä

ä

ä

K
L
M
N
O
P

ä

ä

gdfg

R

jghjk

R
U
E
.

d
r
M
n

i

l

e
t
t
i

M
e
t
g

i
l
l
i

w
e
B

l

l

k

ä

ä

h

kjh

Gesundheitsforschung und Gesundheitswirtschaft
Bioökonomie
Zivile Sicherheitsforschung
Energieforschung und Energietechnologien
Klima, Umwelt, Nachhaltigkeit
Informations‐ und Kommunikationstechnologien
FuE zur Verbesserung der Arbeitsbedingungen und im
Dienstleistungssektor
Nanotechnologien und Werkstofftechnologien
Optische Technologien
Produktionstechnologien
Raumordnung und Stadtentwicklung; Bauforschung
Innovationen in der Bildung
Geisteswissenschaften; Wirtschafts‐ und
Sozialwissenschaften
Innovationsrelevante Rahmenbedingungen und übrige
Querschnittsaktivitäten
Förderorganisationen, Umstrukturierung der Forschung
im Beitrittsgebiet; Hochschulbau und überwiegend
hochschulbezogene Sonderprogramme
Großgeräte der Grundlagenforschung

ö

ä

ä

ä

k

T
kihjzu

U

19

Abbildung 7:  Anzahl und bewilligte Mittel von neu geförderten Vorhaben zum Querschnittsthema Digitalisierung nach

Leistungsplanbereichen, weniger restriktive Abgrenzung

Identifizierung von Querschnittsthemen in Projekten der Direkten Projektförderung des BMBF
Bericht zu einer Machbarkeitsstudie

neu geförderten Vorhaben
neu bewilligte Mittel

7

6

5

4

3

2

1

0

.

d
s
T
n

i

n
e
b
a
h
r
o
V
r
e
t
r
e
d
r
ö
f
e
g

l

h
a
z
n
A

A B C E

F G J

K L M N O P R T U

Quelle: PROFI‐Datenbank, Vorhabenbeschreibungen des BMBF, Berechnungen des ZEW.

R
U
E
.

d
r
M
n

i

l

e
t
t
i

M
e
t
g

i
l
l
i

w
e
B

3.5

3.0

2.5

2.0

1.5

1.0

0.5

0.0

jkghk

iüko kjh

A
B
C
E
F
G
J

k

l

l

ä

ä

ä

K
L
M
N
O
P

ä

ä

gdfg

R

jghjk

U

l

l

k

ä

ä

h

kjh

Gesundheitsforschung und Gesundheitswirtschaft
Bioökonomie
Zivile Sicherheitsforschung
Energieforschung und Energietechnologien
Klima, Umwelt, Nachhaltigkeit
Informations‐ und Kommunikationstechnologien
FuE zur Verbesserung der Arbeitsbedingungen und im
Dienstleistungssektor
Nanotechnologien und Werkstofftechnologien
Optische Technologien
Produktionstechnologien
Raumordnung und Stadtentwicklung; Bauforschung
Innovationen in der Bildung
Geisteswissenschaften; Wirtschafts‐ und
Sozialwissenschaften
Innovationsrelevante Rahmenbedingungen und übrige
Querschnittsaktivitäten
Förderorganisationen, Umstrukturierung der Forschung
im Beitrittsgebiet; Hochschulbau und überwiegend
hochschulbezogene Sonderprogramme
Großgeräte der Grundlagenforschung

ö

ä

ä

ä

k

T
kihjzu

20

Identifizierung von Querschnittsthemen in Projekten der Direkten Projektförderung des BMBF
Bericht zu einer Machbarkeitsstudie

3.2

TexAn‐Analyse zum Themenfeld Künstliche Intelligenz

Die semantische Analyse zum Themenfeld Künstliche Intelligenz wurde als Teil der Ana‐
lysen  zum  Querschnittsthema  Digitalisierung  durchgeführt.  Die  Künstliche  Intelligenz
bildete eine der Unterkategorien der Digitalisierung. Anders als für das Querschnitts‐
thema insgesamt wird für das Themenfeld Künstliche Intelligenz nur eine Variante der
semantischen Analyse vorgeschlagen ist, da hier eine eindeutige Zuordnung der Vorha‐
ben besser möglich ist. Die Definition von Künstlicher Intelligenz in der semantischen
Analyse  umfasst  vereinfacht  zusammengefasst  die  Themen  Maschinelles  Lernen,  Big
Data Analysen, Mensch‐Maschine/Roboter‐Interaktionen sowie automatisiertes Erken‐
nen von Bild und Ton.7

Aufgrund  der  hohen  innovationspolitischen  Bedeutung  dieses  Themenfelds  wird  hier
eine separate Auswertung der Ergebnisse vorgenommen. Außerdem dienen diese Er‐
gebnisse als Referenz für die Analysen im Abschnitt 4, wo mittels Methoden des maschi‐
nellen Lernens eine automatisierte Klassifikation von Vorhaben zum Themenfeld Künst‐
liche Intelligenz erprobt wird.

Abbildung 8:  Anzahl und bewilligte Mittel von neu geförderten Vorhaben zum

Querschnittsthema Künstliche Intelligenz* 2005‐2018

R
U
E
.

i

o
M
n

i

l

e
t
t
i

M
n
e
t
g

i
l
l
i

w
e
B

neu bewilligte Mittel

Anteil an neuen Bewilligungen

350

300

250

200

150

100

50

0

12%

10%

8%

6%

4%

2%

0%

e
m
m
u
s
s
g
n
u
g

i
l
l
i

w
e
B
r
e
t
m
a
s
e
g
n
a

l
i

e
t
n
A

5
0
0
2

6
0
0
2

7
0
0
2

8
0
0
2

9
0
0
2

0
1
0
2

1
1
0
2

2
1
0
2

3
1
0
2

4
1
0
2

5
1
0
2

6
1
0
2

7
1
0
2

8
1
0
2

* ohne Leistungsplanbereich T
Quelle: PROFI‐Datenbank, Vorhabenbeschreibungen des BMBF, Berechnungen des ZEW.

7 Die finale Liste der genutzten Unterkategorien in Tabelle 4 im Anhang zeigt auch die Unterkategorien,
die für die Analyse zur Künstlichen Intelligenz genutzt wurden.

21

Identifizierung von Querschnittsthemen in Projekten der Direkten Projektförderung des BMBF
Bericht zu einer Machbarkeitsstudie

Insgesamt  wurden  im  Zeitraum  von  2005  bis  2018  3.033  Projekte  mit  einem  Bewilli‐
gungsvolumen  von  1,4  Mrd.  EUR  dem  Themenfeld  Künstliche  Intelligenz  zugeordnet.
Abbildung 8 zeigt die Entwicklung der bewilligten Mittel im Themenfeld Künstliche In‐
telligenz und ihren Anteil an den Gesamtbewilligungen des BMBF. Hier ist ein starker
Anstieg der Mittel von 25 Mio. EUR in 2005 auf 225 Mio. EUR in 2018 zu erkennen. Auch
nimmt die Bedeutung des Themenfelds Künstliche Intelligenz innerhalb der geförderten
Vorhaben zu. Im Jahr 2005 lag ihr Anteil an der jährlichen gesamten Bewilligungssumme
des BMBF bei 1,4  %, bis 2018 stieg dieser Wert auf 10,0  %.

Die Verteilung der Förderungen im Themenfeld Künstliche Intelligenz über die verschie‐
denen Leistungsplanbereiche ist in Abbildung 9 (Anzahl Vorhaben, bewilligte Mittel) und
Abbildung 11 (Anteil an den gesamten Förderaktivitäten je Leistungsplanbereich) zu se‐
hen. Das Muster der absoluten Bewilligungssumme je Leistungsplanbereich und der An‐
zahl der geförderten Vorhaben ähnelt dem Muster, das für das Querschnittsthema Digi‐
talisierung insgesamt gefunden wurde. Insbesondere weisen die Leistungsplanbereiche
„R  –  Innovationsrelevante  Rahmenbedingungen  und  übrige  Querschnittsaktivitäten“
und „G – Informations‐ und Kommunikationstechnologien“ mit großem Abstand erneut
die höchsten Werte aus. Auch ist die Rangfolge des Anteils an den gesamten Förderak‐
tivitäten in Abbildung 11 ähnlich zu denen in Abbildung 5, mit beispielsweise dem Be‐
reich G an erster Stelle.

Der Bearbeitungsaufwand nur für das Themenfeld Künstliche Intelligenz war erheblich
niedriger als für das Querschnittsthema Digitalisierung insgesamt, profitiert aber auch
von "Spillovers", da die Prüfung von False‐Negatives und False‐Positives zu anderen Un‐
terkategorien der Digitalisierung immer wieder Erkenntnisse für die verbesserte Erfas‐
sung des Themenfelds Künstliche Intelligenz ergaben. Isoliert betrachtet war für die Be‐
arbeitung des Themenfelds Künstliche Intelligenz ein Aufwand von ca. 40 Arbeitsstun‐
den eines wissenschaftlichen Mitarbeiters notwendig.

22

Identifizierung von Querschnittsthemen in Projekten der Direkten Projektförderung des BMBF
Bericht zu einer Machbarkeitsstudie

Abbildung 9:  Anzahl und bewilligte Mittel von neu geförderten Vorhaben zum Querschnittsthema Künstliche Intelligenz nach

Leistungsplanbereichen

neu geförderte Vorhaben
neu bewilligte Mittel

1,200

1,000

n
e
b
a
h
r
o
V
r
e
t
r
e
d
r
ö
f
e
g

l

h
a
z
n
A

800

600

400

200

0

600

500

400

300

200

100

0

R
U
E
.

i

o
M
n

i

l

e
t
t
i

M
e
t
g

i
l
l
i

w
e
B

jkghk

iüko kjh

A
B
C
E
F
G
J

k

l

l

ä

ä

ä

K
L
M
N
O
P

ä

ä

gdfg

R

jghjk

U

l

l

k

ä

ä

h

kjh

Gesundheitsforschung und Gesundheitswirtschaft
Bioökonomie
Zivile Sicherheitsforschung
Energieforschung und Energietechnologien
Klima, Umwelt, Nachhaltigkeit
Informations‐ und Kommunikationstechnologien
FuE zur Verbesserung der Arbeitsbedingungen und im
Dienstleistungssektor
Nanotechnologien und Werkstofftechnologien
Optische Technologien
Produktionstechnologien
Raumordnung und Stadtentwicklung; Bauforschung
Innovationen in der Bildung
Geisteswissenschaften; Wirtschafts‐ und
Sozialwissenschaften
Innovationsrelevante Rahmenbedingungen und übrige
Querschnittsaktivitäten
Förderorganisationen, Umstrukturierung der
Forschung im Beitrittsgebiet; Hochschulbau und
überwiegend hochschulbezogene Sonderprogramme
Großgeräte der Grundlagenforschung

ö

ä

ä

ä

k

T
kihjzu

A B C E F G J K L M N O P R T U

Quelle: PROFI‐Datenbank, Vorhabenbeschreibungen des BMBF, Berechnungen des ZEW.

23

Abbildung 10: Anteil bewilligter Mittel von neu geförderten Vorhaben zum Querschnittsthema Künstliche Intelligenz am gesamten

Bewilligungsvolumen nach Leistungsplanbereichen

Identifizierung von Querschnittsthemen in Projekten der Direkten Projektförderung des BMBF
Bericht zu einer Machbarkeitsstudie

10.5%

10.0%

7.9%

7.7%

7.0%

Informations‐ und Kommunikationstechnologien ‐ G

FuE zur Verbesserung der Arbeitsbeding. und im Dienstleistungssek. ‐ J

Produktionstechnologien ‐ M

Zivile Sicherheitsforschung ‐ C

Inno. relev. Rahmenbedingungen und übrige Querschnittsaktivitäten ‐ R

Gesundheitsforschung und Gesundheitswirtschaft ‐ A

2.5%

Geisteswissenschaften; Wirtschafts‐ und Sozialwissenschaften ‐ P

Optische Technologien ‐ L

Klima, Umwelt, Nachhaltigkeit ‐ F

Bioökonomie ‐ B

Großgeräte der Grundlagenforschung ‐ U

Innovationen in der Bildung ‐ O

Energieforschung und Energietechnologien ‐ E

1.7%

1.6%

0.7%

0.6%

0.4%

0.4%

0.3%

Nanotechnologien und Werkstofftechnologien ‐ K

0.1%

Förderorganisationen, hochschulbezogene Sonderprogramme, etc. ‐ T

Raumordnung und Stadtentwicklung; Bauforschung ‐ N

0.0%

0.0%

Quelle: PROFI‐Datenbank, Vorhabenbeschreibungen des BMBF, Berechnungen des ZEW.

0%

2%

4%

6%

8%

10%

12%

24

Identifizierung von Querschnittsthemen in Projekten der Direkten Projektförderung des BMBF
Bericht zu einer Machbarkeitsstudie

3.3

TexAn‐Analyse zum Querschnittsthema Soziale Innovationen

Als zweites Querschnittsthema wurde in dieser Machbarkeitsstudie eine Textfeldana‐
lyse  zu  Sozialen  Innovationen  durchgeführt.  Dieses  Querschnittsthema  unterscheidet
sich deutlich von dem der Digitalisierung. Erstens geht es bei Sozialen Innovationen i.d.R.
nicht um die Entwicklung neuer Technologien, sodass eine technologische Eingrenzung
des Themas nicht zielführend ist. Zweitens bezieht sich das Thema auf die intendierte
Wirkung  von  FuE‐Vorhaben  (nämlich  die  Entwicklung  und/oder  Einführung  eines  be‐
stimmten Typs von Innovation). Drittens bezieht sich der Begriff Soziale Innovationen
auf einen sehr breiten Anwendungsraum, ohne dass eine allgemein anerkannte, inter‐
national standardisierte Definition vorliegen würde. Dadurch können potenziell fast alle
Förderbereiche des BMBF hierzu Beiträge leisten, während es keine direkt ersichtlichen
Leistungsplanklassen  mit  einem  besonders  hohen  Potenzial  für  Soziale  Innovationen
gibt. Daher ist es auch nicht möglich, anders als Querschnittsthema Digitalisierung, die
Güte des Ergebnisses einer semantischen Analyse an der "Trefferquote" im Bereich von
vorab bestimmten Leistungsplanklassen zu bemessen.

Für dieses Querschnittsthema wurde daher eine andere Vorgehensweise gewählt. Zu‐
nächst wurde eine einfach strukturierte Textfeldanalyse (Suche nach den Wörtern so‐
zial" und "Innovation"/"innovativ" sowie von häufig verwendeten Synonymen wie "Ge‐
sellschaft" und "Wandel") vorgenommen, die zum Ziel hatte möglichst wenige False‐Ne‐
gatives  zu  produzieren.  Da  das  Suchergebnis  eine  relativ  geringe  Anzahl von  Treffern
ergab, konnten in einem zweiten Schritt alle klassifizierten Vorhaben manuell auf inkor‐
rekt positive Klassifikationen geprüft und die Textfeldanalyse entsprechend angepasst
werden. Die angepasste Textfeldanalyse wurde dann ausgeführt und erneut kontrolliert.
Dieses Vorgehen wurde iterativ wiederholt bis die Zahl der False‐Positives nahe Null war.

Die erste Textfeldanalyse mit einer hohen Wahrscheinlichkeit wenige False‐Negatives
aber  vielen  False‐Positives  ergab  weniger  als  500  geförderte  Vorhaben  zum  Quer‐
schnittsthema Soziale Innovationen. Dabei zeigte sich, dass die Verwendung der Syno‐
nyme Gesellschaft und Wandel fast immer zu False‐Positives führte, weshalb auf diese
Suchwörter verzichtet wurde. Auch lieferte die Suche nach Wortkombinationen von "so‐
zial" und "Innovation"/"innovativ" in den ersten Runden noch einige inkorrekt positiv
klassifizierte Vorhaben, insbesondere aufgrund von Begriffen wie Sozialberuf, ‐einrich‐
tung, ‐wesen oder ‐versicherung. Es wurde in die Textanalyse daher eingearbeitet, dass
diese Wörter nicht in nächster Nähe zur Wortkombination sozial/innovation auftauchen
dürfen.

25

Identifizierung von Querschnittsthemen in Projekten der Direkten Projektförderung des BMBF
Bericht zu einer Machbarkeitsstudie

Insgesamt wurden letztlich 127 Vorhaben mit einer Bewilligungssumme von 101 Mio.
EUR dem Querschnittsbereich Soziale Innovation zugeordnet.8 Abbildung 11 zeigt die
Entwicklung  der  Förderung  von  Vorhaben  zu  Sozialen  Innovationen.  Das  Großprojekt
der VDI/VDE Innovation + Technik GmbH ist ein klarer Ausreiser in 2012. Ansonsten ist
eine Zunahme der Bedeutung des Querschnittsthemas Soziale Innovationen zu erken‐
nen. Die jährliche Summe an neubewilligten Mittel stieg von 20 Tsd. EUR in 2005 auf 16
Mio. EUR in 2018. Auch erhöhte sich ihr Anteil an der Gesamtbewilligungssumme im
selben Zeitraum von quasi 0,0 % auf 0,5 %.

Abbildung 11: Anzahl und bewilligte Mittel von neu geförderten Vorhaben zum
Querschnittsthema Soziale Innovationen 2005‐2018

R
U
E
.

i

o
M
n

i

l

e
t
t
i

M
n
e
t
g

i
l
l
i

w
e
B

neu bewilligte Mittel

Anteil an neu Bewilligungen

50

45

40

35

30

25

20

15

10

5

0

1.4%

1.2%

1.0%

0.8%

0.6%

0.4%

0.2%

0.0%

e
m
m
u
s
s
g
n
u
g

i
l
l
i

w
e
B
r
e
t
m
a
s
e
g
n
a

l
i

e
t
n
A

5
0
0
2

6
0
0
2

7
0
0
2

8
0
0
2

9
0
0
2

0
1
0
2

1
1
0
2

2
1
0
2

3
1
0
2

4
1
0
2

5
1
0
2

6
1
0
2

7
1
0
2

8
1
0
2

* ohne Leistungsplanbereich T; zum Ausreißerwert im Jahr 2012 siehe Fußnote 8.
Quelle: PROFI‐Datenbank, Vorhabenbeschreibungen des BMBF, Berechnungen des ZEW.

Abbildung 12 zeigt die absolute Höhe der bewilligten Mittel und die Anzahl der geför‐
derten  Vorhaben  im  Querschnittsthema  Soziale  Innovationen  in  den  einzelnen  Leis‐
tungsplanbereichen.  Abbildung  13  zeigt  den  Anteil  der  Vorhaben  zum  Querschnitts‐
thema Soziale Innovationen an dem Bewilligungsvolumen der einzelnen Leistungsplan‐
bereiche. Die drei Leistungsplanbereiche mit den höchsten Werten in allen Kategorien

8 Dabei ist anzumerken, dass 44 Mio. EUR auf ein einziges Projekt der VDI/VDE Innovation + Technik GmbH
im Jahr 2012 entfallen, nämlich die „Projektträgerschaft Mensch‐Technik‐Interaktion 2012‐2016 – Pro‐
jektstabskosten“. Innerhalb dieses Vorhabens werden technische und soziale Innovationen im Themen‐
feld Demographischer Wandel und Mensch‐Technik‐Interaktion gefördert.

26

Identifizierung von Querschnittsthemen in Projekten der Direkten Projektförderung des BMBF
Bericht zu einer Machbarkeitsstudie

entsprechen  sind  R  –  Innovationsrelevante  Rahmenbedingungen  und  übrige  Quer‐
schnittsaktivitäten, J – FuE zur Verbesserung der Arbeitsbedingungen und im Dienstleis‐
tungssektor und F – Klima, Umwelt, Nachhaltigkeit. Wie bereits in den Analysen zu Digi‐
talisierung  können  besonders  viele  Vorhaben  im  Bereich  R  identifiziert  werden.  Dies
zeigt, dass dieser Bereich entsprechend seines Namens viele Vorhaben zu Querschnitts‐
themen umfasst.

Die Zuordnung der neu geförderten Vorhaben des BMBF zum Querschnittsthema Sozi‐
ale  Innovationen  konnte  mit  einem  vergleichsweise  geringen  Aufwand  realisiert  wer‐
den. Die Zuordnung konnte innerhalb von zwei Kalenderwochen bei einem Einsatz von
ca. 20 Stunden Arbeitszeit eines wissenschaftlichen Mitarbeiters umgesetzt werden. Die
relativ kurze Arbeitszeit ergab sich insbesondere aufgrund der geringen Anzahl an Vor‐
haben, die selbst bei einer sehr einfachen und damit groben Suche nach Schlagwörtern
zu Sozialen Innovationen gefunden wurden. Dadurch war der Aufwand für die manuel‐
len Überprüfungen im Vergleich zum Querschnittsthema Digitalisierung erheblich gerin‐
ger.

27

Identifizierung von Querschnittsthemen in Projekten der Direkten Projektförderung des BMBF
Bericht zu einer Machbarkeitsstudie

Abbildung 12: Anzahl und bewilligte Mittel von neu geförderten Vorhaben zum Querschnittsthema Soziale Innovationen nach

Leistungsplanbereichen

neu geförderte Vorhaben
neu bewilligte Mittel

n
e
b
a
h
r
o
V
r
e
t
r
e
d
r
ö
f
e
g

l

h
a
z
n
A

80

72

64

56

48

40

32

24

16

8

0

80

72

64

56

48

40

32

24

16

8

0

R
U
E
.

i

o
M
n

i

l

e
t
t
i

M
e
t
g

i
l
l
i

w
e
B

jkghk

iüko kjh

A
B
C
E
F
G
J

k

l

l

ä

ä

ä

K
L
M
N
O
P

ä

ä

gdfg

R

jghjk

U

l

l

k

ä

ä

h

kjh

Gesundheitsforschung und Gesundheitswirtschaft
Bioökonomie
Zivile Sicherheitsforschung
Energieforschung und Energietechnologien
Klima, Umwelt, Nachhaltigkeit
Informations‐ und Kommunikationstechnologien
FuE zur Verbesserung der Arbeitsbedingungen und im
Dienstleistungssektor
Nanotechnologien und Werkstofftechnologien
Optische Technologien
Produktionstechnologien
Raumordnung und Stadtentwicklung; Bauforschung
Innovationen in der Bildung
Geisteswissenschaften; Wirtschafts‐ und
Sozialwissenschaften
Innovationsrelevante Rahmenbedingungen und übrige
Querschnittsaktivitäten
Förderorganisationen, Umstrukturierung der Forschung
im Beitrittsgebiet; Hochschulbau und überwiegend
hochschulbezogene Sonderprogramme
Großgeräte der Grundlagenforschung

ö

ä

ä

ä

k

T
kihjzu

A B C E F G J K L M N O P R T U

Quelle: PROFI‐Datenbank, Vorhabenbeschreibungen des BMBF, Berechnungen des ZEW.

28

Identifizierung von Querschnittsthemen in Projekten der Direkten Projektförderung des BMBF
Bericht zu einer Machbarkeitsstudie

Abbildung 13: Anteil bewilligter Mittel von neu geförderten Vorhaben zum Querschnittsthema Soziale Innovationen am gesamten

Bewilligungsvolumen nach Leistungsplanbereichen

Inno. relev. Rahmenbedingungen und übrige Querschnittsaktivitäten ‐ R

FuE zur Verbesserung der Arbeitsbeding. und im Dienstleistungssek. ‐ J

1.094%

0.906%

Geisteswissenschaften; Wirtschafts‐ und Sozialwissenschaften ‐ P

0.230%

Klima, Umwelt, Nachhaltigkeit ‐ F

0.317%

Energieforschung und Energietechnologien ‐ E

0.039%

Innovationen in der Bildung ‐ O

0.013%

Bioökonomie ‐ B

0.004%

Großgeräte der Grundlagenforschung ‐ U

0.000%

Förderorganisationen, hochschulbezogene Sonderprogramme, etc. ‐ T

0.000%

Raumordnung und Stadtentwicklung; Bauforschung ‐ N

0.000%

Produktionstechnologien ‐ M

0.000%

Optische Technologien ‐ L

0.000%

Nanotechnologien und Werkstofftechnologien ‐ K

0.000%

Informations‐ und Kommunikationstechnologien ‐ G

0.000%

Zivile Sicherheitsforschung ‐ C

0.000%

Gesundheitsforschung und Gesundheitswirtschaft ‐ A

0.000%

Quelle: PROFI‐Datenbank, Vorhabenbeschreibungen des BMBF, Berechnungen des ZEW.

0.00%

0.20%

0.40%

0.60%

0.80%

1.00%

1.20%

29

Identifizierung von Querschnittsthemen in Projekten der Direkten Projektförderung des BMBF
Bericht zu einer Machbarkeitsstudie

4

Analyse mittels maschinellem Lernen zum Themenfeld
Künstliche Intelligenz

In diesem Abschnitt wird getestet, inwiefern ein trainierter, automatisierter Algorithmus
geeignet  ist,  das  Themenfeld  Künstliche  Intelligenz  in  den  Abstracts  von  geförderten
Vorhaben zu identifizieren. Hierzu wird auf die Ergebnisse aus Abschnitt 3.2 zur Künstli‐
chen Intelligenz und auf einen Machine Learning Ansatz zurückgegriffen. Insgesamt be‐
steht diese Analyse aus fünf Schritten: Textaufbereitung, KI‐Indikator, Modellwahl, Trai‐
ning und Evaluation.

Textaufbereitung. Texte erfordern in der Regel eine Aufbereitung bevor diese in Ma‐
chine Learning Modellen verwendet werden können, da diese in der Regel nur mit nu‐
merischen Größen in einer vordefinierten Datenstruktur arbeiten können. Tabelle 2 be‐
schreibt die neun Schritte unserer Aufbereitung kurz.

Tabelle 2:

Textaufbereitung für Machine Learning Modelle

Pipeline
1.  Datenselektion

2.  Tokenisierung
3.  Stoppwort‐  Filter

4.  Stemming

5.  Löschen von kur‐
zen Wörtern
6.  Vereinheitlichen

des Textes
7.  Löschen von

Sonderzeichen
8.  Selektion von

Wörtern

9.  Erstellen von Se‐

quenzen

Löschen von Datenpunkten ohne Text oder mit Textdup‐
likaten.
Die Texte werden in einzelne Wörter aufgeteilt.
Löschen von Wörtern auf Basis von mehreren Stopp‐
wort‐Listen. Die gelöschten Wörter sind üblicherweise
nicht relevant für die Klassifikation, ein Beispiel ist das
Wort „und“.
Verschiedene Wortvarianten werden auf ihre Grundform
zurückgeführt. Zum Beispiel: Die Wörter „Wortes“ und
„Wörter“ werden zu „Wort“.
Wörter mit einer Länge von Eins werden gelöscht. Dies
sind in der Regel Satz‐ oder Sonderzeichen.
Alle Großbuchstaben werden in Kleinbuchstaben über‐
führt, um das Vokabular zu verkleinern.
Die Sonderzeichen „!"#$ %&()*+,‐./:;<=>?@[\]^_`{|}~“
werden aus dem Text entfernt.
Nur die 50.000 häufigsten Wörter werden extrahiert. Die
restlichen Wörter werden gelöscht. Dies verringert die
Dimension der Daten und das “Rauschen“ im Text.
Die Wörter werden eindeutig durch Ganzzahlen ersetzt
und in Sequenzen der maximalen Länge von 250 über‐
führt.

30

Identifizierung von Querschnittsthemen in Projekten der Direkten Projektförderung des BMBF
Bericht zu einer Machbarkeitsstudie

Die Abstracts der Vorhaben haben nach diesen Schritten eine Datenstruktur, die für Ma‐
chine  Learning  Modelle  als  Eingabe  geeignet  ist.  Nach  der  Durchführung  aller  neun
Punkte verbleiben 68.191 nutzbare Vorhaben.

KI‐Indikator. Für jedes der 68.191 verbliebenen Vorhaben existiert ein KI‐Indikator der
angibt, ob ein Vorhaben zum Themenfeld Künstliche Intelligenz gehört oder nicht. Die‐
ser Indikator wurde in der zuvor beschrieben TexAn‐Analyse ermittelt. Insgesamt gehö‐
ren nur etwa 4 Prozent der Vorhaben zum Themenfeld Künstliche Intelligenz. Daraus
ergeben sich 2.924 sogenannte positive und 65.267 negative Trainingspunkte.

Modellwahl. Für die Studie wurde ein „long short‐term memory“ neuronales Netzwerk9
verwendet. Dieser Modelltyp ist auf dem neusten Stand der Technik bei der Klassifika‐
tion von Texten und wurde bereits in vielen Projekten eingesetzt. Zahlreiche Beispiele
hierfür  lassen  sich  unter  anderem  auf  Kaggle10  finden.  Für  die  praktische  Umsetzung
wurde die Programmiersprache Python verwendet.

Training. Die 68.191 Vorhaben wurden in zwei Teile aufgeteilt. 80 % der 2.924 dem The‐
menfeld Künstliche Intelligenz zugeordneten Vorhaben sowie 80 % der nicht als KI klas‐
sifizierten Vorhaben wurden als Trainingsdaten verwendet. Diese dienen dazu, das oben
genannte neuronale Netzwerk zu trainieren, sprich das neuronale Netzwerk optimiert
seine Vorhersage über den KI‐Indikator eines Vorhabens iterativ anhand der transfor‐
mierten Abstract‐Inhalte innerhalb dieses Datensatzes. Die restlichen 20 % der Vorha‐
ben wurden als Evaluationsdatensatz zurückgehalten.

Evaluation. Für jedes Vorhaben im Evaluationsdatensatz wird mit Hilfe des trainierten
neuronalen Netzes die Wahrscheinlichkeit berechnet, dass das Vorhaben Teil des The‐
menfelds  Künstliche  Intelligenz  ist.  Sofern  die  Wahrscheinlichkeit  über  50 %  betrug,
wurde das Vorhaben dem Themenfeld zu geordnet, sonst nicht.

Die Güte des neuronalen Netzes bezüglich der Identifikation von Vorhaben zum The‐
menfeld Künstliche Intelligenz im Testdatensatz lässt sich mittels der Kennzahlen Preci‐
sion, Recall und Accuracy11 bewerten. Eine Übersicht der Kennzahlen ist in Tabelle 3 dar‐
gestellt.  Es  werden  nur  68 %  aller  vom  TexAn  identifizierten  Vorhaben  zum  Thema
Künstliche Intelligenz durch das neuronale Netz erkannt (68 % ‐ Recall). Außerdem han‐
delt es sich bei 22 % der durch das neuronale Netz identifizierten Vorhaben zum The‐
menfeld  Künstliche  Intelligenz  um  False‐Positive  (78 %  ‐  Precision).  Demnach  besteht

9 Sepp Hochreiter, Jürgen Schmidhuber (1997): Long short‐term memory, Neural Computation 9(8), 1735–
1780.

10 https://www.kaggle.com/

11 https://en.wikipedia.org/wiki/Precision_and_recall

31

Identifizierung von Querschnittsthemen in Projekten der Direkten Projektförderung des BMBF
Bericht zu einer Machbarkeitsstudie

eine relativ hohe Fehlerrate bei der Identifikation von Vorhaben im Themenfeld Künst‐
liche Intelligenz.12 Allerdings ist das LSTM Modell grundsätzlich in der Lage, aus den Da‐
ten zu lernen. Würden allen Vorhaben im Testdatensatz nicht dem Themenfeld Künstli‐
che Intelligenz zugeordnet, wäre diese Klassifikation in 96 % aller Fälle Korrekt, da ins‐
gesamt lediglich 4 % der Vorhaben zu dem Themenfeld gehören. Das neuronale Netz‐
werk identifiziert dem gegenüber 98 % aller Vorhaben korrekt und ist demnach zuver‐
lässiger (98 % ‐ Accuracy). Eine Steigerung der drei Gütekennzahlen wäre mit einer Ver‐
größerung des Testdatensatzes, insbesondere die Anzahl dem Themenfeld zugehöriger
Vorhaben, wahrscheinlich.

Tabelle 3:

Zusammenfassung der Gütekennzahlen des Machine Learning
Ansatzes für die Identifikation von Vorhaben im Themenfeld
Künstliche Intelligenz

Anteil der mit dem Machine Learning Ansatz identifizierten KI‐Vorha‐
ben im Evaluationsdatensatz, die auch über die TexAn‐Methode als KI‐
Vorhaben identifiziert wurden ("Precision")

Anteil der über die TexAn‐Methode identifizierten KI‐Vorhaben im Eva‐
luationsdatensatz, die auch mit dem Machine Learning Ansatz als KI‐
Vorhaben identifiziert wurden ("Recall")

Anteil aller Vorhaben, die mit dem Machine Learning Ansatz korrekt als
KI‐Vorhaben oder Nicht‐KI‐Vorhaben identifiziert werden (Referenzwert
ohne Einsatz von maschinellem Lernen: 96 %)

78 %

68 %

98 %

Aus diesen Ergebnissen lässt sich die Schlussfolgerung ziehen, dass der Machine Learn‐
ing Ansatz für das Themenfeld Künstliche Intelligenz nicht geeignet ist, um mit hinrei‐
chender Genauigkeit KI‐Vorhaben auf Basis der Abstract‐Texte in der Gesamtheit aller
vom  BMBF  geförderten  Vorhaben  zu  identifizieren.  Hierfür  wären  erheblich  höhere
Werte für Precision und Recall von zumindest 90 % notwendig. Dieses ungünstige Er‐
gebnis liegt an der geringen Anzahl von Trainingsdatensätzen, was wiederum an der ins‐
gesamt niedrigen Anzahl von geförderten Vorhaben im Bereich KI liegt. Außerdem sind
die zu jedem Vorhaben vorliegenden Texte relativ kurz und verhältnismäßig stark stan‐
dardisiert. Für Themenfelder mit einer deutlich größeren Anzahl geförderter Vorhaben
und damit einem umfangreicheren Trainingsdatensatz sowie auf Basis von umfangrei‐
cheren  Texten  (gesamte  Vorhabenbeschreibung)  könnte  das  Resultat deutlich  anders

12 Für Vorhaben, die nicht dem Themenfeld Künstliche Intelligenz zugeordnet wurden, sind Precision und
Recall jeweils ca. 99 % und relativ nah am Optimalwert von 100 %. Dies liegt allerdings an dem sehr hohen
Anteil von Nicht‐KI‐Vorhaben.

32

Identifizierung von Querschnittsthemen in Projekten der Direkten Projektförderung des BMBF
Bericht zu einer Machbarkeitsstudie

aussehen. Für Themenfelder, die noch seltener als das Themenfeld Künstliche Intelli‐
genz vorkommen, (wie z.B. Soziale Innovationen) eignet sich ein Machine Learning An‐
satz grundsätzlich nicht.

33

Identifizierung von Querschnittsthemen in Projekten der Direkten Projektförderung des BMBF
Bericht zu einer Machbarkeitsstudie

Fazit

Die Machbarkeitsstudie hat untersucht, inwieweit Querschnittsthemen durch eine se‐
mantische Analyse von Vorhabenbeschreibungen mit hinreichender Genauigkeit identi‐
fiziert werden können. Innerhalb der Studie wurden die Querschnittsthemen Digitalisie‐
rung (inkl. des Teilgebiets Künstliche Intelligenz) und Soziale Innovationen mit einer vom
ZEW  entwickelten  Software  (TexAn  –  Textanalyser)  untersucht.  Des  Weiteren  wurde
aufbauend auf den Ergebnissen der TexAn‐Analysen zu Künstlicher Intelligenz ein Ana‐
lysetool für eine automatisierte Zuordnung von Vorhaben zu Querschnittsthemen im‐
plementiert. Hierfür wurde auf Methoden des Natural Language Processings und  des
Maschinellen Lernens zurückgegriffen. Dabei wurde getestet, inwiefern ein trainierter,
automatisierter Algorithmus geeignet ist, um das Querschnittsthema Künstliche Intelli‐
genz in den Abstracts von geförderten Vorhaben zu identifizieren. Eine große Heraus‐
forderung  dabei  ist  die  geringe  Anzahl  von  Vorhaben  in  dem  Querschnittsthema,
wodurch nur wenige Trainingsdatensätze vorliegen, an denen der automatisierter Algo‐
rithmus lernen kann.

Die Ergebnisse zur Machbarkeitsstudie sind gemischt. Die Klassifizierung des besonders
breiten und schwer abgrenzbaren Querschnittsthemas Digitalisierung hat bei einem Ein‐
satz eines wissenschaftlichen Mitarbeiters einen Arbeitsaufwand von ca. 150 Stunden
verteilt über einen Zeitraum von vier Kalendermonaten in Anspruch genommen. Dies
bedeutet, dass eine kurzfristige Klassifizierung ähnlicher komplexer Thematiken, etwa
im Fall einer kleinen oder großen Anfrage des Bundestags oder kurzfristigen politischen
Informationsbedarfs, nicht möglich ist. Auch konnte zum Querschnittsthema Digitalisie‐
rung keine Vorgehensweise gefunden werden, die eine eindeutige Klassifikation ermög‐
licht. Stattdessen wurden zwei Klassifizierungsvarianten (eine restriktive und eine weni‐
ger restriktive) entwickelt, die quasi einen oberen und unteren Bereich von Vorhaben
zum Querschnittsthema Digitalisierung eingrenzen. Schließlich ist zu beachten, dass die
hier entwickelte semantische Analyse von Vorhabenbeschreibungen auf dem aktuellen
technischen Stand der Digitalisierung beruht. Da sich dieser rasch ändert, sind regelmä‐
ßig arbeitsaufwendige Anpassungen der semantischen Analyse notwendig.

Das Themenfeld Künstliche Intelligenz und das Querschnittsthema Soziale Innovationen
konnten rascher bearbeitet werden, da sie zum einen besser einzugrenzen sind und zum
anderen die Anzahl der relevanten Vorhaben deutlich geringer ist, was den Aufwand der
manuellen Prüfung erheblich reduziert. Der benötigte Arbeitszeitraum zum Themenfeld
Künstliche Intelligenz betrug ca. 40 Arbeitsstunden. Für das Querschnittsthema Soziale
Innovationen fiel ein Aufwand von 20 Arbeitsstunden an. Die Klassifizierung des Quer‐
schnittsthemas Soziale Innovationen konnten innerhalb von 2 Arbeitswochen und damit
recht kurzfristig umgesetzt werden.

Abschließend ist des Weiteren festzustellen, dass der getestete Machine Learning An‐
satz nicht geeignet ist, um das Themenfeld Künstliche Intelligenz in den Abstracts von

34

Identifizierung von Querschnittsthemen in Projekten der Direkten Projektförderung des BMBF
Bericht zu einer Machbarkeitsstudie

geförderten Vorhaben mit hinreichender Genauigkeit zu identifizieren. Grund hierfür ist
die geringe Anzahl an Vorhaben zu diesem Thema und der dadurch kleine Trainingsda‐
tensatz sowie die geringe Länge der Texte und ihr recht hoher Grad an Standardisierung.
Allerdings wäre eine Identifikation von Themen mit einem höheren Vorkommen sowie
unter Nutzung der gesamten Vorhabenbeschreibungen mit Hilfe von Machine Learning
Ansätzen grundsätzlich denkbar. Es ist allerdings auch hier anzumerken, dass diese Art
von Analyse immer auf dem aktuellen technischen Stand beruht und regelmäßig ange‐
passt werden muss.

35

Identifizierung von Querschnittsthemen in Projekten der Direkten Projektförderung des BMBF
Bericht zu einer Machbarkeitsstudie

5

Anhang

5.1

Unterkategorien der Digitalisierung

Tabelle  4  zeigt  die  verschiedenen  Unterkategorien  der  TexAn‐Analyse  zur  Digitalisie‐
rung. Die Spalte Unterkategorie umfasst die Namen der einzelnen Unterkategorien der
Digitalisierung wie sie in der Programmierung der Analyse verwendet wurden. Die The‐
menüberschrift gibt einen kurzen Überblick, welche Themen die entsprechende Unter‐
kategorie umfasst. Die weniger restriktive Analyse zur Digitalisierung umfasst alle gelis‐
tet Unterkategorien, die restriktivere Analyse abstrahiert von den blauhinterlegten. Die
TexAn‐Analyse zur Künstlichen Intelligenz nutzt die grünhinterlegten Unterkategorien.
Die  genannten  Unterkategorien  sind  nicht  vollkommen  überschneidungsfrei  in  ihren
Themen und genutzte Schlagwortkombinationen.

Tabelle 4:

Unterkategorien der TexAn‐Analyse zur Digitalisierung

Unterkategorien
DIGI_E
INTSYS
IKT_E
IT_E
ITTECH
QUANT
KI
MENSCHMA
ERKENN
BIGDATA
DRIV
SMART
VIRTU
INTE_E
IOF
ECOOM
APPL
DEEP
CYBER
SECU
CLOUD_E
CLOUD
DATENPLAT
PLAT
KRYPTO
DOKU

Themenüberschrift
Digital ‐ simple
Integrierten Systemen ‐ simple
Informations‐ und Kommunikationstechnologien ‐ simple
Hochleistungsrechner, Softwarewerkzeuge, Soft‐ Middle‐ und Hardware
Chiptechnologie, EDV, Hochleistungsrechner
Quantencomputer
Maschinelles Lernen, Künstliche Intelligenz
Mensch‐Maschine/Roboter‐Interaktion
Automatisches Erkennen von Tönen, Bildern etc., Blicktracking
Big Data
Selbstfahrende Fahrzeuge
Intelligente Produkte/Dienstleistungen/Software/Fahrzeuge/Netzwerke
Virtual Reality, Augmented Reality, 3D‐ und 4D‐Simulation
Internet ‐ simple
Internet der Dinge
E‐Commerce, Onlinehandel, E‐Business
Appentwicklung
Deepweb
Cybercrime, Cyber‐Technical‐Systems
Cybersicherheit
Cloudlösungen ‐ simple
Cloudcomputing , ‐ technologien, ‐anwendungen, ‐dienste
Datenplattformen, Datennetzwerke
Datenplattformen, Plattformservices
Kryptowährung
Elektronische Dokumentation

36

Identifizierung von Querschnittsthemen in Projekten der Direkten Projektförderung des BMBF
Bericht zu einer Machbarkeitsstudie

5.2

Code zur TexAn‐Analyse

Innerhalb der TexAn‐Software werden für jede definierte Klasse, wie beispielsweise So‐
ziale Innovationen oder eine der in Tabelle 4 genannten Unterkategorien, sogenannte
seeker definiert. Diese beinhalten die Schlagwörter die zur Identifikation einer Klasse
genutzt  werden.  Diese  Schlagwörter  werden  entweder  eins‐zu‐eins  verwendet  oder
nochmals durch die Option using  standard standardisiert. Diese Option wandelt
die eingegebenen Schlagworte sowie die einzelnen Textfelder der Vorhaben um, sprich
alle Buchstaben werden in Großbuchstaben geändert, die Umlaute werden zu z.B. "ä"
zu "ae" umgewandelt, alle Sonderzeichen werden durch Leerzeichen ersetzt und meh‐
rere Leerzeichen zusammengefasst.

Der Befehl texan führt die eigentliche Textfeldanalyse durch. Nach ihm wird definiert,
ob die definierten seeker einzeln gesucht werden, Kombinationen von seekern in
gewissen Wortabständen Auftauchen müssen, oder bestimmte seeker nicht auftau‐
chen  dürfen.  Am  häufigsten  genutzt  werden  die  texan‐Optionen  max  #  words
near  und  not.  In  der  ersten  Option  wird  definiert  wie  viele  Wörter  (#)  die  Begriffe
zweier seeker voneinander entfernt sein dürfen, damit eine Klasse in einem Textfeld
vorliegt.  In  der  zweiten  Option  werden  Begriffe  definiert,  die  nicht  in  einem  Textfeld
vorkommen dürfen, damit das Vorliegen einer Klasse identifiziert werden kann.

Übersicht 1:   Code der TexAn‐Analyse zum Querschnittsthema Digitalisierung (inkl.

Künstliche Intelligenz)

seeker digi1_e seeks "digital" using standard

texan DIGI_E analyses digi1_e

seeker inte1 seeks "4.0"

seeker inte2 seeks "Industr" using standard

seeker inte3 seeks "integrier", "eingebette", "kooperierend", "automatis", "simulatio"
using standard

seeker inte4 seeks "system" using standard

seeker inte5 seeks "data", "daten", "algorythm", "algorith", "softwa", "selbstlern",

"automatis", "computer", "digital", "smart" using standard

seeker inte6 seeks "Informationssystem", "Kommunikationssystem", "information system",

"communication system"

seeker inte7 seeks "I4.0", "I 4.0"

texan INTESYS analyses inte1 max 3 words near inte2 or inte3 max 2 words near inte4 or

inte5 max 5 words near inte4 or inte6 or inte7

seeker ikt1_e seeks " IKT ", " IKT-", " IKT,"

texan IKT_E analyses ikt1_e

seeker it1_e seeks "software", "hardware", "middleware", "informationstechn", "inter-

nettechn" using standard

seeker it2_e seeks " IT ", " IT-", " IT,", " IT-,", "-IT-", " HPC ", " HPC-", " HPC"

seeker it3_e seeks "computing", "computer" using standard

37

Identifizierung von Querschnittsthemen in Projekten der Direkten Projektförderung des BMBF
Bericht zu einer Machbarkeitsstudie

seeker it4_e seeks "programmieren", "Programmierung", "Programmcode"

seeker it5_e seeks "compute", "softwa", "kommunik"

seeker it6_e seeks " Bits ", " Bit ", " Byte ", " Bytes ", " Kilobyte", " Megabyte", "

Gigabyte", " Terabyte"

texan IT_E analyses it1_e or it2_e or it4_e max 5 words near it5_e or it6_e

seeker it1 seeks "Hochleistungsrech", "hochleistungsrech", "Quantencompu", "Quanten-

rechn", "EDV-ger", "EDV-Ger", "Multicore", "Multi-core", "Multi-Core",
"MultiCore", "Supercomput", "Mobilfunk", "Hochleistungsprozes"

seeker it2 seeks "IT-Werkzeug", "IT Werkzeug", "Software Werkzeug", "Software-Werkzeug",

"Softwarewerkzeug", "Informationstechno", "Informatik"

seeker it3 seeks "quanten", "qubit", "hochleistu", "höchstleist", "high perfomance" u-

sing standard

seeker it4 seeks "computer", "repeater", "rechner", "server", "prozessor", "EDV-ger",
"datenverarbeitungsger", "hardware", "chiptech", "computing" using stan-
dard

seeker it5 seeks "3d-druck", "chiptech" using standard

seeker it6 seeks " IT ", " IT-", " IT,", " IT-,", "-IT-", " HPC ", " HPC-", " HPC", "
Java "

seeker it7 seeks "technolo", "technik", "system", "netzwerk" using standard

seeker it8 seeks "software" using standard

seeker it9 seeks "code", "lösung", "system", "analys", "entwick" using standard

seeker it10 seeks "glasfaser" using standard

seeker it11 seeks "netz", "leitung" using standard

seeker it12 seeks "schnittstelle" using standard

seeker it13 seeks "optisch" using standard

seeker it14 seeks "drahtlos", "mobil" using standard

seeker it15 seeks "kommunikation", "kommunizier" using standard

seeker it16 seeks " IP ", " IP-"

seeker it17 seeks "adres", "addres" using standard

texan ITTECH analyses it1 or it2 or it3 max 3 words near it4 or it5 or it6 max 2 words

near it7 or it8 max 3 words near it9 or it10 max 3 words near it11 or
it12 max 3 words near it13 or it14 max 3 words near it15 or it16 max 2
words near it17

seeker quant1 seeks "quanten" using standard

seeker quant2 seeks "plattform", "platform", "netzwerk" using standard

seeker quant3  seeks "kommunikat" using standard

seeker quant4  seeks "computer", "repeater", "rechner", "server", "prozessor", "EDV-
ger", "datenverarbeitungsger", "hardware", "chiptech" using standard

seeker quant5 seeks "technolo", "technik", "system", "technisch", "netzwerk" using

standard

texan QUANT

analyses quant1 max 2 words near quant2 or quant1 max 2 words near quant3
or quant1 max 2 words near quant4 or quant1 max 2 words near quant5

seeker ki1 seeks "lern" using standard

seeker ki2 seeks "maschinel", "tiefes", "selbstständig" using standard

seeker ki3 seeks "netzwerk", "network", "netz" using standard

seeker ki4 seeks "neuronal", "neural" using standard

seeker ki5 seeks "intelli", "autonom", "vernetz" using standard

seeker ki6 seeks "service", "dienst", "maschin", "robot", "computer" using standard

seeker ki7 seeks "system" using standard

38

Identifizierung von Querschnittsthemen in Projekten der Direkten Projektförderung des BMBF
Bericht zu einer Machbarkeitsstudie

seeker ki9 seeks "data", "daten", "algorythm", "algorith", "softwa", "selbstlern", "au-
tomatis", "computer", "digital", "smart" using standard

seeker ki10 seeks "Deep Learn", "deep learn", "deep-learn", "Deep-Learn", "künstliche
Intellig", "künstlicher Intellig", "künstlichen Intellig", "künstliche
intellig", "künstlicher intellig", "künstlichen intellig", "artificial
intellig", "K.I.", "KI-Anwend", "KI Anwend", "KI-Appli", "KI Appli", "KI-
Method", "KIMethod", "machine learning", "machine-learning", "Machine
Learning", "Machine-Learning", "Machinelearning", "wearable computing",
"Wearable-Computing", "Maschinenlern"

seeker ki11 seeks "maschi", "robot", "computer" using standard

seeker ki12 seeks "service", "autonom", "dienstleist" using standard

seeker noki4 seeks "brain", "gehirn", "hirn", "gesundheit", "health", "Kopf", "nerven",

"synap", "schmerz", "Hippocamp", "gedächtnis", "Polyam", "anatomis",
"psychisch", "psyche", "Krank" using standard

texan KI analyses ki10 or ki1 max 2 word near ki2 or ki3 max 2 words near ki4 max 10

words near ki9 or ki5 max 4 words near ki6 max 20 words near ki9 or ki11
max 2 words near ki12 max 20 words near ki5 or ki11 max 2 words near ki12
max 20 words near ki9 or ki7 max 2 words near ki5 max 10 words near ki9
or ki5 max 3 words near ki9

seeker mensch1 seeks "mensch", "user", "benutzer" using standard

seeker mensch2 seeks "maschi", "robot", "computer", "techni" using standard

seeker mensch3 seeks "interaktio", "interactio" using standard

texan MENSCHMA analyses mensch1 max 2 words near mensch2 or mensch1 max 5 words near

mensch2 max 5 words near mensch3

seeker erkenn1 seeks "erkenn"

seeker erkenn2 seeks " Gesicht", " Bild", " Muster", " Ton", "Interface", " Sprach",

"muster", "Schrift", "Person" using standard

seeker erkenn3 seeks "data", "daten", "algorythm", "algorith", "softwa", "selbstlern",
"automatis", "computer", "digital", "smart" using standard

seeker erkenn4 seeks "eye" using standard

seeker erkenn5 seeks "tracking" using standard

texan ERKENN analyses erkenn1 max 3 words near erkenn2 max 50 words near erkenn3 or er-

kenn4 max 2 words near erkenn5

seeker bigdata1 seeks "Big data", "big data", "bigdata", "Bigdata", "Big Data", "big

Data"

texan BIGDATA analyses bigdata1

seeker driv1 seeks "fahren ", "fahrzeug", "Fahrzeug", "drive", "driving ", " Auto",

"PKW", "LKW", "Lastfahr"

seeker driv2 seeks "vernetz", "autonom", "selbst", "intellige", "smart" using standard

seeker nodriv seeks "verfahr" using standard

texan DRIV analyses driv1 max 5 words near driv2 minimum 10 words near nodriv ignore

seeker smart1 seeks "smart ", "Smart ", "smart,", "smart.", "Smart", "Smartcard",

"smartcard", "smart product", "Smart Product", "smart-product", "Smart-
Product"

seeker smart2 seeks "computing", "service", "dienst", "lösung" using standard

seeker smart3  seeks "program", "software", "programm", "technolog", "informationstech"

using standard

seeker smart4  seeks " Grid ", " grid ", "-Grid ", " car ", " cars ", "-Cars", "-Car ",
" Cars ", " Cars", " Meter ", " Meters ", " meter ", "-Meter ", "-Meters
"

39

Identifizierung von Querschnittsthemen in Projekten der Direkten Projektförderung des BMBF
Bericht zu einer Machbarkeitsstudie

seeker smart5 seeks "driving", "fahrzeug", "automobil", "lastkraft", "robot",

"messstell"

texan SMART analyses smart1 max 3 words near smart2 or smart1 max 3 words near smart3 or

smart1 max 2 words near smart4 or smart3 max 2 words near smart5

seeker virt1 seeks "virtuel", "virtual" using standard

seeker virt2 seeks "augment" using standard

seeker virt3 seeks "reality" using standard

seeker virt4 seeks "3D", "4D"

seeker virt5 seeks "druck", "system", "simulati", "visuali", "fertigung" using standard

seeker virt6 seeks "LCD"

seeker virt7 seeks "techno" using standard

texan VIRTU analyses virt1 or virt2 max 3 words near virt3 or virt4 max 2 words near

virt5 or virt6 max 2 words near virt7

seeker inte1_e seeks "internet" using standard

seeker inte2_e seeks " Web ", " Web-", " Web,", "world wide web", "World Wide Web",

"World-Wide-Web", "world-wide-web", "www", "WWW", "Web2.0", "Web 2.0",
"Web3.0", "Web 3.0", "Web-2.0", "Web-3.0"

seeker inte3_e seeks "semantic", "semantisc" using standard

seeker inte4_e seeks "web" using standard

texan INTE_E analyses inte1_e or inte2_e or inte3_e max 3 words near inte4_e

seeker iof1 seeks "Internet der Dinge", "Internet-der-Dinge", "Internet Der Dinge", "In-

ternet-Der-Dinge"

seeker iof2 seeks "internetderdinge" using standard

seeker iof3 seeks "Internet of Things", "Internet-of-Things", "internet of things", "in-

ternet-of-things"

seeker iof4 seeks "internetofthings" using standard

texan IOF analyses iof1 or iof2 or iof3 or iof4

seeker ecomm1 seeks "E Commerc", " Ecommerc", " e commerc", " eCommerc", "e Commerc", "
E-Commerc", " E-commerc", " e-business", " e-Business", " E-Business", "
ebusiness", " Ebusiness", " EBusiness", " eBusiness"

seeker ecomm2 seeks"Internethandel", "Onlinehandel", "Online-Handel", "Online-Shop",

"Onlineshop", "elektronischer Handel", "elektronisch handel", "elektroni-
sche handel"

texan ECOMM analyses ecomm1 or ecomm2

seeker app1 seeks "App,", "App ", "Apps ", "App.", "Apps,", "usability", " App-"

texan APPL analyses app1

seeker deep1   seeks   "Deep Web", "Deep-Web", "Deepweb", "Hidden-Web", "Hidden Web",
"invisible web", "invisible-web", "verstecktes web", "dark web", "dark
net", "opaque web", "opaque-web", "proprietary web", "proprietary-web",
"visible web", "visible-web", "clear web", "clear-web", "surface-web",
"surface web" using standard

texan DEEP analyses deep1

seeker cyber1 seeks "cyber" using standard

texan CYBER analyses cyber1

40

Identifizierung von Querschnittsthemen in Projekten der Direkten Projektförderung des BMBF
Bericht zu einer Machbarkeitsstudie

seeker secur1 seeks "sicher", "secur" using standard

seeker secur2 seeks "cyber", " IT ", " IT-", " IT,", " IT-,", "internet", "Internet",
"Netz", "

Netzwerk", "Website", "Webseite", " Web ", " Web-"

seeker secur3 seeks "trojan", "firewall", "honeypot", "schadsoftwar" using standard

seeker secur4 seeks "IPv6", " Bot ", " Bots ", " Botnetz "

seeker secur5 seeks "intrusion" using standard

seeker secur6 seeks "detection" using standard

texan SECU analyses secur3 or secur1 max 3 words near secur2 or secur5 max 5 words near

secur6

seeker cloud1_e seeks "Cloud ", " Cloud,", " Cloud-"

texan CLOUD_E analyses cloud1_e

seeker cloud1 seeks "cloud" using standard

seeker cloud2 seeks "anwendung" using standard

seeker cloud4 seeks "computing", "service", "dienst", "lösung" using standard

seeker cloud3 seeks "technolo", "technik", "system", "netzwerk", "netz" using standard

texan CLOUD analyses cloud1 max 2 words near cloud2 or cloud1 max 2 words near cloud3 or

cloud1 max 2 words near cloud4

seeker platt1 seeks "plattform", "platform", "netzwerk" using standard

seeker platt2 seeks "internet", "website", "webseite" using standard

seeker platt3 seeks "online ", "on-line", "online-", "Online"

seeker platt4 seeks "Daten ", "Daten.", "Daten,", "Datenanal", "Datenbas"

seeker platt5 seeks "program", "software", "programmier", "programment" using standard

seeker platt6 seeks "intellig", "simulatio", "service", "dienstleistu", "technolog"

 using standard

texan PLAT analyses platt1 max 5 words near platt2 or platt1 max 5 words near platt3 or

platt1 max 3 words near platt4 or platt5 max 3 words near platt1 or
platt1 max 3 words near platt6

seeker datenplat1 seeks "Daten ", "Daten.", "Daten,"

seeker datenplat2 seeks "plattform", "platform", "netzwerk", "austausch",

"kommu-

nikati" using standard

texan DATENPLAT analyses datenplat1 max 5 words near datenplat2

seeker kryp1 seeks "krypto" using standard

texan KRYPTO analyses kryp1

seeker doku1 seeks "dokumentat" using standard

seeker doku2 seeks "digital" using standard

seeker doku3 seeks "elektro" using standard

texan DOKU analyses doku1 max 3 words near doku2 or doku1 max 2 words near doku3

41

Identifizierung von Querschnittsthemen in Projekten der Direkten Projektförderung des BMBF
Bericht zu einer Machbarkeitsstudie

Übersicht 2:   Code der TexAn‐Analyse zum Querschnittsthema Soziale Innovationen

seeker soin_1 seeks "sozial" using standard

seeker soin_2 seeks "innovati", "neuerung", "neuheit", "erneuer", "neugestalt", "neu-

ordn" using standard

seeker nosoin_1 seeks "sozialwissensch", "sozialberuf", "sozialwesen", "sozialversi-

cher", "sozialhilf" using standard

seeker nosoin_2 seeks "beruf", "dienst", "betreuung", "einricht" using standard

texan SOZINN analyses soin_1 max 3 words near soin_2 and not nosoin_1 and not nosoin_2
max 1 words near soin_1

42

Identifizierung von Querschnittsthemen in Projekten der Direkten Projektförderung des BMBF
Bericht zu einer Machbarkeitsstudie

Abbildungsverzeichnis

Abbildung 1:  Anzahl und bewilligte Mittel vom BMBF geförderter Vorhaben*

2005‐2018 .......................................................................................... 10

Abbildung 2:   Jährliches Wachstum der bewilligten Mittel von neu

geförderten Vorhaben* zum Thema Digitalisierung 2006‐2018 ....... 15

Abbildung 3:  Bewilligte Mittel von neu geförderten Vorhaben* zum

Querschnittsthema Digitalisierung 2005‐2018 .................................. 16

Abbildung 4:  Anteil bewilligter Mittel von neu geförderten Vorhaben* zum
Querschnittsthema Digitalisierung am gesamten
Bewilligungsvolumen des BMBF 2005‐2018 ...................................... 16

Abbildung 5:  Anteil bewilligter Mittel von neu geförderten Vorhaben zum

Querschnittsthema Digitalisierung am gesamten
Bewilligungsvolumen nach Leistungsplanbereichen ......................... 18

Abbildung 6:  Anzahl und bewilligte Mittel von neu geförderten Vorhaben
zum Querschnittsthema Digitalisierung nach
Leistungsplanbereichen, restriktivere Abgrenzung ........................... 19

Abbildung 7:  Anzahl und bewilligte Mittel von neu geförderten Vorhaben
zum Querschnittsthema Digitalisierung nach
Leistungsplanbereichen, weniger restriktive Abgrenzung ................ 20

Abbildung 8:  Anzahl und bewilligte Mittel von neu geförderten Vorhaben

zum Querschnittsthema Künstliche Intelligenz* 2005‐2018 ............. 21

Abbildung 9:  Anzahl und bewilligte Mittel von neu geförderten Vorhaben

zum Querschnittsthema Künstliche Intelligenz nach
Leistungsplanbereichen ..................................................................... 23

Abbildung 10:  Anteil bewilligter Mittel von neu geförderten Vorhaben zum

Querschnittsthema Künstliche Intelligenz am gesamten
Bewilligungsvolumen nach Leistungsplanbereichen ......................... 24

Abbildung 11:  Anzahl und bewilligte Mittel von neu geförderten Vorhaben

zum Querschnittsthema Soziale Innovationen 2005‐2018 ............... 26

Abbildung 12:  Anzahl und bewilligte Mittel von neu geförderten Vorhaben

zum Querschnittsthema Soziale Innovationen nach
Leistungsplanbereichen ..................................................................... 28

Abbildung 13:  Anteil bewilligter Mittel von neu geförderten Vorhaben zum

Querschnittsthema Soziale Innovationen am gesamten
Bewilligungsvolumen nach Leistungsplanbereichen ......................... 29

43

Identifizierung von Querschnittsthemen in Projekten der Direkten Projektförderung des BMBF
Bericht zu einer Machbarkeitsstudie

Tabellenverzeichnis

Tabelle 1:

Leistungsplanklassen mit hohem Potenzial für das
Querschnittsthema Digitalisierung .................................................... 13

Tabelle 2:

Textaufbereitung für Machine Learning Modelle .............................. 30

Tabelle 3:

Zusammenfassung der Gütekennzahlen des Machine Learning
Ansatzes für die Identifikation von Vorhaben im Themenfeld
Künstliche Intelligenz ......................................................................... 32

Tabelle 4:

Unterkategorien der TexAn‐Analyse zur Digitalisierung ................... 36

Verzeichnis der Übersichten

Übersicht 1:   Code der TexAn‐Analyse zum Querschnittsthema

Digitalisierung (inkl. Künstliche Intelligenz) ....................................... 37

Übersicht 2:   Code der TexAn‐Analyse zum Querschnittsthema Soziale

Innovationen ...................................................................................... 42

Verzeichnis der Boxen

Box 1: PROFI‐Datenbank ............................................................................................... 9

Box 2: Leistungsplansystematik .................................................................................. 10

44

