# IN00CS94-Tietoliikenns-sovellus-projekti

Toisen vuodet tieto ja viestintä tekniikan laitepuolten opiskelijoiden lukuvuoden ensimmäinen sovellusprojekti.

## projekti kaavio kaavio

Kaaviossa näkyy mitä koodia reposta löytyy ja miten koodi mahdollisesti puhuu muun koodin kanssa.
![kaavio tai jotain](assets/dig.png "diagrammi")

## arduino

Arduinokoodit löytyy kansiosta `arduino/`. Seillä on kaksi kansiota. `tiedonkeräys/` kansiossa on ohjelma jolla nimensä mukaan kerätään tietoa. Se myös lähettää tieto radioaaltojen, joka päätyy lopulta tietokantaan. Tiedon keräys onnistuu kun kirjoitaa vain x, y tai z ja sitten jonkun kokonainsluvun. (`x4`, `y10`, `z7`). `ml_predictive` kansiossa on arduino ohjelma, joka pystyy kertomaan missä asennossa laite on hyödyntäen kiihtyvyys anturia. Ohjelmassa on 3 eri algorytmiä jolla se pyrkii kertomaan missä asennossa laite on (k-means, neuroverkko ja päätöspuu).

## database access

Database_access kansiosta löytyy ohjelmia joilla voidaan lukea tietoa tietokannasta. Ne kirjoittavat stdouttiin csv:nä tietoa tietokannasta.
Esimerkki käyttö tapahtuisi näin.
```sh
#Miten sql ohjelmaa käytetään. Samalla logiikalla toimii myös http ja tcp niissä vaan pitää katsoa tuo -help että tietää mitä vipuja niissä on.
go run mysql_client.go -help
go run mysql_client.go -addr 192.168.100.5 -port 27910 -user root -pass root -db testdb -id 92 > mydata.csv
```

## K-means algorytmi

Tässä on ryhmittelemätöntä dataa. Joka pitäisi lajitella kuuteen eri ryhmään.
![raakadata](assets/Figure_1.png "ryhmittelemätön data")


Ja tässä on muutaman k-means iteraation jälkeen ryhmitelty data. 6 ryhmää selkeästi erillään. Siniset pisteet ovat k-means algoithmin centroidit. Joitain centroideja on hankala/mahdoton erottaa koska ne ovat osittain tai täysin ryhmänsä pisteiden peitossa.
![k-means](assets/Figure_2.png "k-means ryhmitelty data")

## arduino koneoppimisen tulokset

Tässä on arduinolle tehtyjen koneoppimis mallejen lopputulemat confusion matriiseissa. Jokaisella mallille on syötetty samat testi arvot.

```
┏━━━━━━━━━┓        ┏━━━━━━━━━━━┓      ┏━━━━━━━━━━━━━━┓
┃ k-means ┃        ┃ NeuralNet ┃      ┃ DecisionTree ┃
┣━━━━━━━━━┻━━━━━━━━╋━━━━━━━━━━━┻━━━━━━╋━━━━━━━━━━━━━━┻━━━┓
┃ 6  0  0  0  0  1 ┃ 7  0  0  0  0  0 ┃ 7  0  0  0  0  0 ┃
┃ 0  6  0  0  0  0 ┃ 0  6  0  0  0  0 ┃ 0  4  0  0  2  0 ┃
┃ 0  0 10  0  0  0 ┃ 0  0 10  0  0  0 ┃ 0  0 10  0  0  0 ┃
┃ 0  0  0 12  0  0 ┃ 0  0  0 12  0  0 ┃ 0  0  0  8  0  4 ┃
┃ 0  0  0  0  7  0 ┃ 0  0  0  0  7  0 ┃ 0  0  0  0  7  0 ┃
┃ 0  0  0  0  0  7 ┃ 0  0  0  0  1  6 ┃ 0  0  0  0  0  7 ┃
┗━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━┛
```