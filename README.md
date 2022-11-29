# IN00CS94-Tietoliikenns-sovellus-projekti

Toisen vuodet tieto ja viestintä tekniikan laitepuolten opiskelijoiden lukuvuoden ensimmäinen ryhmäprojekti. Tää on mun repo.

## projekti kaavio kaavio

Kaaviossa näkyy mitä koodia reposta löytyy ja miten koodi mahdollisesti puhuu muun koodin kanssa.
![kaavio tai jotain](assets/dig.png "diagrammi")

## arduiino koodi

Arduiinokoodi löytyy kansiosta `sketch_nov02a/`. Siinä pinit 11 ja 12 toimivat tiedon vastaanotto ja lähetys pineinä. Serial interface on helppokäyttöinen. kirjoita vain x, y tai z ja sitten joku kokonains numero. (`x4` `y10`) Arduiion ottaa kokonaisluvun verraan otoksia sensorista ja kun se lähettää radioaallon yli nämä otokset se merkkaa mihin `xyz` axis:siin otokset liittyvä. 

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


Ja tässä on 10 k-means iteraation jälkeen ryhmitelty data. 6 ryhmää selkeästi erillään. Siniset pisteet ovat k-means algoithmin centroidit. Ruskean ja purppuran ryhmän centroideja on hankala/mahdoton erottaa koska ne ovat osittain tai täysin ryhmänsä pisteiden peitossa.
![k-means](assets/Figure_2.png "k-means ryhmitelty data")