import tkinter as tk
from change_layout import *


def new_text(screeni, text):
    textfield = tk.Text(
    master=screeni,
    font=("Arial", 12),
    wrap="word",
    bg="white",
    relief="flat",
    borderwidth=0,
    highlightthickness=0
    )
    textfield.insert("1.0", text)
    format_text(textfield)
    textfield.pack(fill="x", expand=False,padx=60, pady=(0, 5))

def tarkista_monivalinta(screeni, valinta, oikea, palaute):
    valittu = valinta.get()
    if valittu == oikea:
        palaute.config(text="Juuri näin!", fg="green")
        textfield = tk.Text(
        master=screeni,
        font=("Arial", 12),
        wrap="word",
        bg="white",
        relief="flat",
        borderwidth=0,
        highlightthickness=0
        )
        textfield.insert("1.0", valittu)
        format_text(textfield)
        textfield.pack(fill="x", expand=False,padx=60, pady=(0, 5))


    elif valittu=="a ja b ovat kokonaislukuja":
        palaute.config(text="a ja b ovat kokonaislukuja, mutta tiedämmekö niistä vielä jotain muuta?", fg="blue")
    else:
        palaute.config(text="Onko tämä oletus vai väite?", fg="blue")
