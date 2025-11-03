import tkinter as tk
from tkinter import ttk
import textfields
from functions import format_text, new_text, tarkista_monivalinta

class UI:
    def __init__(self, root):
        self._root = root
        self._root.geometry("800x600")
        self._root.configure(bg="white")

    # käynnistää näkymän
    def start(self):
        label = ttk.Label(self._root, text="Todistus", font=("Arial", 16, "bold"))
        label.pack(pady=(20, 15))

        # tekstikenttien sisällöt
        textfields_list = [
            textfields.tehtavananto,
            textfields.alkuteksti,
            textfields.vaite_muotoilu
        ]

        # luodaan tekstikentät ja lisätään niihin tekstit
        texts = []
        for text in textfields_list:
            textfield = tk.Text(
                master=self._root,
                font=("Arial", 12),
                wrap="word",
                bg="white",
                relief="flat",
                borderwidth=0,
                highlightthickness=0
            )
            texts.append(textfield)
            textfield.insert("1.0", text)
            format_text(textfield)

        [textfield.pack(fill="x", expand=False,padx=60, pady=(0, 5)) for textfield in texts]

        # tähän frameen kuuluu monivalintakysymys ja siihen kuuluva kenttä
        frame = tk.Frame(self._root)
        frame.config(relief="flat",borderwidth=0,highlightthickness=0)
        frame.pack()

        # monivalintakysymys
        valinta = ttk.Combobox(
            frame,
            values=textfields.oletusvaihtoehdot,
            width=50,
            state="readonly",
            font=("Arial", 11)
        )
        valinta.current(1)
        valinta.pack(pady=(5, 10))

        tulos_label = tk.Label(frame, text="", font=("Arial", 12))
        tulos_label.pack(pady=10)
        
        tarkista_nappi = ttk.Button(
        frame,
        text="Tarkista",
        command=lambda: tarkista_monivalinta(self._root, valinta, textfields.oletusvastaus, tulos_label)
        )
        tarkista_nappi.pack(pady=10)

        def jatka():
            frame.pack_forget()
            new_text(self._root, textfields.oletusjatko)

        button = ttk.Button(frame, text="Jatka", command=jatka)

        button.pack(pady=(5, 10))