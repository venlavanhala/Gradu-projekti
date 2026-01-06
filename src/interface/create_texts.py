from interface.edit_ui import *

# jokainen funktio luo tekstit tietylle tehtävänäkymälle

def starting_texts(screen):
    format_textfield(screen, "[Vaihe 1]", "#6a0dad")
    format_textfield(screen, textfields.johdanto)
    format_textfield(screen, textfields.tehtavananto)
    format_textfield(screen, textfields.alkusuunnitelma)
    format_textfield(screen, textfields.alkuteksti, "#9c29c1")
    format_textfield(screen, textfields.oletuskysymys)

def statement_texts(screen):
    format_textfield(screen, "[Vaihe 2]", "#6a0dad")
    format_textfield(screen, textfields.oletusjatko, "#9c29c1")
    format_textfield(screen, textfields.vaitekysymys)


def pairless_texts(screen):
    format_textfield(screen, "\n[Vaihe 3]\n", "#6a0dad")
    format_textfield(screen, textfields.vaitejatko, "#9c29c1")
    format_textfield(screen, textfields.paritontieto)
    format_textfield(screen, textfields.paritonkysymys, "#9c29c1")
    format_textfield(screen, textfields.paritontieto2)

def evidence_texts(screen):
    format_textfield(screen, "\n[Vaihe 4]\n", "#6a0dad")
    if textfields.valittu == "2k+1":
        format_textfield(screen, textfields.paritonjatko, "#9c29c1")
        format_textfield(screen, textfields.maarittely)
        format_textfield(screen, textfields.tulo, "#9c29c1")
        format_textfield(screen, textfields.tulosievennys)
        format_textfield(screen, textfields.tulo2, "#9c29c1")
    else:
        format_textfield(screen, textfields.paritonjatko_, "#9c29c1")
        format_textfield(screen, textfields.maarittely_)
        format_textfield(screen, textfields.tulo_, "#9c29c1")
        format_textfield(screen, textfields.tulosievennys_)
        format_textfield(screen, textfields.tulo2_, "#9c29c1")

def formatting_texts(screen):
    format_textfield(screen, "[Vaihe 5]\n", "#6a0dad")
    if textfields.valittu == "2k+1":
        format_textfield(screen, textfields.osoitusjatko, "#9c29c1")
    else:
        format_textfield(screen, textfields.osoitusjatko_, "#9c29c1")

def end_texts(screen):
    format_textfield(screen, "[Vaihe 5]\n", "#6a0dad")
    if textfields.valittu == "2k+1":
        format_textfield(screen, textfields.lopputeksti, "#9c29c1")
    else:
        format_textfield(screen, textfields.lopputeksti_, "#9c29c1")