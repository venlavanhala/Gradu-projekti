import tkinter as tk
from tkinter import ttk
from change_layout import *
from textfields import *

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
def check_combobox(screeni, choice, right_answer, label, feedback, button, checkbutton):
    answer = choice.get()
    if answer == right_answer or answer in right_answer:
        label.config(text=feedback[answer], fg="green", font=("Arial", 12))
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
        checkbutton.pack_forget()
        button.pack()
    else:
        label.config(text=feedback[answer], fg="blue")

def check_entry(screeni, entry, right_answer, label, feedback, button, checkbutton):
    answer = entry.get().replace(" ","").lower()
    if answer == right_answer or answer in right_answer:
        label.config(text=feedback[answer], fg="green", font=("Arial", 12))
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
        checkbutton.pack_forget()
        button.pack()

    else:
        label.config(text="Yritä uudestaan!", fg="blue")

def jatka_nappi(screeni, frame, seuraava_frame,teksti):
    button = ttk.Button(frame, text="Jatka", command=lambda: (jatka(screeni,frame,teksti), seuraava_frame.pack()))
    button.pack(pady=(5, 10))

# piilotetaan edellinen näyttö ja näytetään seuraava teksti
def jatka(naytto, screen, teksti):
    screen.pack_forget()
    new_text(naytto, teksti)

def popup_window(screen, text):
    popup = tk.Toplevel(screen)
    popup.title("Vihje")
    popup.geometry("500x120")

    tk.Label(popup, text=text).pack(pady=20)

    tk.Button(popup, text="Sulje", command=popup.destroy).pack(pady=5)