import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

johdanto = "Tässä harjoituksessa tutustutaan erään lukuteorian lauseen todistamiseen. Saat scrollattua näkymää näytön oikeasta reunasta. Mieti kysymyksiä ensin itse ja katso vasta sitten mahdolliset vastausvaihtoehdot!"

tehtavananto = "Todista: Kahden parittoman luvun a ja b tulo on pariton luku."

alkuteksti = "Ensin täytyy löytää oletus ja väite, jota ollaan ratkaisemassa.Oletus on jokin tieto, josta lähdetään liikkeelle ja jota voimme pitää tunnettuna. Väite on jokin asia, jonka haluamme todistaa.\nLause 'Kahden parittoman kokonaisluvun tulo on pariton kokonaisluku' voitaisiin myös ilmaista muodossa:"

vaite_muotoilu = "Jos [oletus], niin [väite].\n\nVoidaan merkitä lukuja kirjaimilla a ja b. Mikä oletus on? \n\nOletus:"

oletusvaihtoehdot = [
    "a ja b ovat parittomia kokonaislukuja",
    "a ja b ovat kokonaislukuja",
    "lukujen a ja b tulo on pariton luku"
]

oletusvastaus = "a ja b ovat parittomia kokonaislukuja"

oletukset = {"a ja b ovat parittomia kokonaislukuja":"Juuri näin!",
              "a ja b ovat kokonaislukuja":"a ja b ovat kokonaislukuja, mutta tiedämmekö niistä vielä jotain muuta?",
              "lukujen a ja b tulo on pariton luku":"Onko tämä oletus vai väite?"
              }

oletusjatko = "Mikä väite on?\n\nVäite:"

vaitevaihtoehdot = [
    "a \u00B7 b on pariton kokonaisluku",
    "a \u00B7 b on kokonaisluku",
    "lukujen a ja b tulo on pariton luku"
]

vaitteet = {"a \u00B7 b on pariton kokonaisluku":"Juuri näin!",
    "a \u00B7 b on kokonaisluku":"a\u00B7 b on kokonaisluku, mutta mitä muuta haluamme todistaa?",
    "lukujen a ja b tulo on pariton luku":"Juuri näin!"}

vaitevastaus = ["a \u00B7 b on pariton kokonaisluku", "lukujen a ja b tulo on pariton luku"]

vaitejatko = "Kokonaislukujen joukkoa merkitään kirjaimella \u2124, ja joukkoon kuulumista merkillä \u2208.\nVoimme siis merkitä: a, b \u2208 \u2124.\nParilliset luvut voidaan ilmaista muodossa a=2k (k \u2208 \u2124), koska parilliset luvut ovat aina jaollisia luvulla 2.\nMiten parittomat luvut voitaisiin ilmaista tämän tyyppisesti kokonaisluvun k avulla?\nKirjoita tekstikenttään, miten pariton luku a voitaisiin ilmaista. Kirjoita vastaus muodossa a=[lauseke]."

pariton_oikeat = ["2k+1","2k-1"]

pariton_vaihtoehdot = {"2k+1":"Hyvä!",
    "2k-1":"Hyvä!"
}

pariton_vihje1 = "Jokaisen parillisen luvun jälkeen tulee pariton luku."

pariton_vihje2 = "Parilliset luvut voidaan kirjoittaa muodossa a=2k. \nJos lisäämme parilliseen lukuun luvun 1, siitä tulee pariton."

valittu = ""
# tähän päivittyy arvo

if valittu == "2k+1":
    paritonjatko_plus = "Nyt meillä on yksi muuttuja, joka ilmaisee paritonta lukua. Tarvitsemme vielä toisen parittoman luvun. Käytämme siihen eri muuttujia, koska parittomat luvut eivät välttämättä ole samoja. "
    paritonjatko_plus +="Määritellään b = 2n + 1}, kun n \u2208 \u2124.\nVoimme nyt kirjoittaa tulon lukujen a ja b avulla. Kirjoitamme tulon, jotta voimme tutkia sen parittomuutta.\n\na \u00B7 b = (2k + 1)(2n + 1)\n\n"
    paritonjatko_plus +="Lasketaan kertolasku auki:\n\na \u00B7 b = 4kn + 2k + 2n + 1\n\nHaluamme osoittaa, että lukujen a ja b tulo 4kn + 2k + 2n + 1 on pariton luku. Millä tavalla seuraavista voimme todistaa tämän?"

    osoitusvaihtoehdot = [
    "Osoitetaan, että 4kn + 2k + 2n + 1 ei ole jaollinen kahdella",
    "Osoitetaan, että a \u00B7 b voidaan kirjoittaa muodossa 2p + 1, jossa p \u2208 \u2124",
    "Osoitamme, että 4kn + 2k + 2n + 1 on jaollinen jollain muulla luvulla kuin 2"
    ]

    osoitusvastaus = ["Osoitetaan, että 4kn + 2k + 2n + 1 ei ole jaollinen kahdella", "Osoitetaan, että a \u00B7 b voidaan kirjoittaa muodossa 2p + 1, jossa p \u2208 \u2124"]

    osoituspalautteet = {"Osoitamme, että 4kn + 2k + 2n + 1 on jaollinen jollain muulla luvulla kuin 2":"Tämä ei osoita sitä, että 4kn+2k+2n+1 olisi pariton luku.\nJos 4kn+2k+2n+1 olisi jaollinen esimerkiksi luvulla 5,\nse voisi olla samalla myös jaollinen luvulla 2.",
                        "Osoitetaan, että 4kn + 2k + 2n + 1 ei ole jaollinen kahdella":"Oikein! Tällöin a \u00B7 b voidaan kirjoittaa muodossa 2p+1, jossa p \u2208 \u2124.",
                        "Osoitetaan, että a \u00B7 b voidaan kirjoittaa muodossa 2p + 1, jossa p \u2208 \u2124":"Kyllä!"}

    osoitusjatko ="Kirjoita 4kn + 2k + 2n + 1 muodossa 2 \u00B7 p + 1, kun p \u2208 \u2124."

    kirjoitusvihje = "Ota luku 2 yhteiseksi tekijäksi niin,\n että voit kirjoittaa vastauksen muodossa 2(p) + 1."

    kirjoitusvastaus = [2,1,1]

    kirjoituspalautteet = ["Ensimmäisen kentän vastaus on väärin.", "Toisen kentän vastaus on väärin.", "Kolmannen kentän vastaus on väärin."]

    kirjoitusteksti = "4kn + 2k + 2n + 1 = 2 \u00B7 (2kn + 1k + 1n) + 1"

    lopputeksti= "Parittomat kokonaisluvut pystytään aina kirjoittamaan muodossa 2p + 1, kun \u2208 \u2124. Koska saimme kirjoitettua luvun a kun \u00B7 b muodossa 2p + 1, "
    lopputeksti += "sekin on kokonaisluku.\n\nLähdimme siis oletuksesta, että on kaksi paritonta kokonaislukua, ja päädyimme siihen, että niiden tulo on myös pariton. "
    lopputeksti += "Väite on täten todistettu.\n\n\u25A1"

else:
    paritonjatko = "Nyt meillä on yksi muuttuja, joka ilmaisee paritonta lukua. Tarvitsemme vielä toisen parittoman luvun. Käytämme siihen eri muuttujia, koska parittomat luvut eivät välttämättä ole samoja. "
    paritonjatko +="Määritellään b = 2n - 1, kun n \u2208 \u2124.\nVoimme nyt kirjoittaa tulon lukujen a ja b avulla. Kirjoitamme tulon, jotta voimme tutkia sen parittomuutta.\n\na \u00B7 b = (2k - 1)(2n - 1)\n\n"
    paritonjatko +="Lasketaan kertolasku auki:\n\na \u00B7 b = 4kn - 2k - 2n + 1\n\nHaluamme osoittaa, että lukujen a ja b tulo 4kn - 2k - 2n + 1 on pariton luku. Millä tavalla seuraavista voimme todistaa tämän?"

    osoitusvaihtoehdot = [
    "Osoitetaan, että 4kn - 2k - 2n + 1 ei ole jaollinen kahdella",
    "Osoitetaan, että a \u00B7 b voidaan kirjoittaa muodossa 2p - 1, jossa p \u2208 \u2124",
    "Osoitamme, että 4kn - 2k - 2n + 1 on jaollinen jollain muulla luvulla kuin 2"
    ]

    osoitusvastaus = ["Osoitetaan, että 4kn - 2k - 2n + 1 ei ole jaollinen kahdella", "Osoitetaan, että a \u00B7 b voidaan kirjoittaa muodossa 2p - 1, jossa p \u2208 \u2124"]

    osoituspalautteet = {"Osoitamme, että 4kn - 2k - 2n + 1 on jaollinen jollain muulla luvulla kuin 2":"Tämä ei osoita sitä, että 4kn-2k-2n+1 olisi pariton luku.\nJos 4kn-2k-2n+1 olisi jaollinen esimerkiksi luvulla 5,\nse voisi olla samalla myös jaollinen luvulla 2.",
                        "Osoitetaan, että 4kn - 2k - 2n + 1 ei ole jaollinen kahdella":"Oikein! Tällöin a \u00B7 b voidaan kirjoittaa muodossa 2p-1, jossa p \u2208 \u2124.",
                        "Osoitetaan, että a \u00B7 b voidaan kirjoittaa muodossa 2p - 1, jossa p \u2208 \u2124":"Kyllä!"}

    osoitusjatko ="Kirjoita 4kn - 2k - 2n + 1 muodossa 2 \u00B7 p - 1, kun p \u2208 \u2124."

    kirjoitusvihje = "Ota luku 2 yhteiseksi tekijäksi niin,\n että voit kirjoittaa vastauksen muodossa 2(p) - 1."

    kirjoitusvastaus = [2,1,1]

    kirjoituspalautteet = ["Ensimmäisen kentän vastaus on väärin.", "Toisen kentän vastaus on väärin.", "Kolmannen kentän vastaus on väärin."]

    kirjoitusteksti = "4kn - 2k - 2n + 1 = 2 \u00B7 (2kn - 1k - 1n) + 1"

    lopputeksti= "Parittomat kokonaisluvut pystytään aina kirjoittamaan muodossa 2p - 1, kun \u2208 \u2124. Koska saimme kirjoitettua luvun a kun \u00B7 b muodossa 2p - 1, "
    lopputeksti += "sekin on kokonaisluku.\n\nLähdimme siis oletuksesta, että on kaksi paritonta kokonaislukua, ja päädyimme siihen, että niiden tulo on myös pariton. "
    lopputeksti += "Väite on täten todistettu.\n\n\u25A1"