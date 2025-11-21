from change_layout import *
from textfields import *

def make_textfields(screen):
    # jäävät
    for text in [johdanto, tehtavananto, oletuskysymys, vaitekysymys,pariton_kysymys, pariton_lasku1, pariton_lasku2, osoitusjatko]:
        format_textfield(self.scrollable_frame, text, backround_color="black")

# miten saadaan koko screeni tähän muokattavaksi?