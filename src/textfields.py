johdanto = "Tässä harjoituksessa tutustutaan erään lukuteorian lauseen todistamiseen. Saat scrollattua näkymää näytön oikeasta reunasta."

tehtavananto = "Todista: Kahden parittoman luvun a ja b tulo on pariton luku."

alkuteksti = "Ensin täytyy löytää oletus ja väite, jota ollaan ratkaisemassa.Oletus on jokin tieto, josta lähdetään liikkeelle ja jota voimme pitää tunnettuna. Väite on jokin asia, jonka haluamme todistaa.\nLause 'Kahden parittoman kokonaisluvun tulo on pariton kokonaisluku' voitaisiin myös ilmaista muodossa:"

vaite_muotoilu = "Jos [oletus], niin [väite].\n\nMikä oletus on? \n\nOletus:"

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

oletusjatko = "Voidaan merkitä lukuja kirjaimilla a ja b. Kokonaislukujen joukkoa merkitään kirjaimella \u2124, ja joukkoon kuulumista merkillä \u2208.\nVoimme siis merkitä: a, b \u2208 \u2124.\nMikä väite tällöin on?\n\nVäite:"

vaitevaihtoehdot = [
    "a \u00B7 b on parillinen kokonaisluku",
    "a \u00B7 b on kokonaisluku",
    "lukujen a ja b tulo on pariton luku"
]

vaitteet = {"a \u00B7 b on parillinen kokonaisluku":"Juuri näin!",
    "a \u00B7 b on kokonaisluku":"a\u00B7 b on kokonaisluku, mutta mitä muuta haluamme todistaa?",
    "lukujen a ja b tulo on pariton luku":"Juuri näin!"}

vaitevastaus = ["a \u00B7 b on parillinen kokonaisluku", "lukujen a ja b tulo on pariton luku"]

vaitejatko = "Parilliset luvut voidaan ilmaista muodossa a=2k (k \u2208 \u2124), koska parilliset luvut ovat aina jaollisia luvulla 2. Miten parittomat luvut voitaisiin ilmaista tämän tyyppisesti kokonaisluvun k avulla?\nKirjoita tekstikenttään, miten pariton luku a voitaisiin ilmaista. Kirjoita vastaus muodossa a=[lauseke]."

pariton_oikeat = ["a=2k+1","a=2k-1"]

pariton_vaihtoehdot = {"a=2k+1":"Hyvä!",
    "a=2k-1":"Hyvä!"
}

pariton_vihje1 = "Jokaisen parillisen luvun jälkeen tulee pariton luku."

pariton_vihje2 = "Parilliset luvut voidaan kirjoittaa muodossa a=2k. Jos lisäämme parilliseen lukuun luvun 1, siitä tulee pariton."

paritonjatko = "Nyt meillä on yksi muuttuja, joka ilmaisee paritonta lukua. Tarvitsemme vielä toisen parittoman luvun. Käytämme siihen eri muuttujia, koska parittomat luvut eivät välttämättä ole samoja.\nMääritellään b=2n+1, kun n \u2208 \u2124.\nVoimme nyt kirjoittaa tulon lukujen a ja b avulla.\n\na \u00B7 b = (2k+1)(2n+1)"
