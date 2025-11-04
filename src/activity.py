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

# tarkista monivalinta
def check_combobox(screeni, choice, right_answer, label, feedback):
    answer = choice.get()
    if answer == right_answer or answer in right_answer:
        label.config(text=feedback[answer], fg="green")
        textfield = tk.Text(
        master=screeni,
        font=("Arial", 12),
        wrap="word",
        bg="white",
        relief="flat",
        borderwidth=0,
        highlightthickness=0
        )
        textfield.insert("1.0", answer)
        format_text(textfield)
        textfield.pack(fill="x", expand=False,padx=60, pady=(0, 5)) 
    else:
        label.config(text=feedback[answer], fg="blue")

def check_entry(screeni, entry, right_answer, label, feedback):
    answer = entry.get().replace(" ","").lower()
    if answer == right_answer or answer in right_answer:
        label.config(text=feedback[answer], fg="green")
        textfield = tk.Text(
        master=screeni,
        font=("Arial", 12),
        wrap="word",
        bg="white",
        relief="flat",
        borderwidth=0,
        highlightthickness=0
        )
        textfield.insert("1.0", answer)
        format_text(textfield)
        textfield.pack(fill="x", expand=False,padx=60, pady=(0, 5)) 
    else:
        label.config(text="Yritä uudestaan!", fg="blue")

# piilotetaan edellinen näyttö ja näytetään seuraava teksti
def jatka(naytto, screen, teksti):
    screen.pack_forget()
    new_text(naytto, teksti)