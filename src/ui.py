import tkinter as tk
from tkinter import ttk
import textfields

class UI:
    def __init__(self, root):
        self._root = root
        self._root.geometry("800x600")
        self._root.configure(bg="white")

    # ottaa tekstikentän ja muokkaa sen korkeuden vastaamaan tekstin pituutta
    def format_text(self, textfield):
        text = textfield.get("1.0", "end-1c")
        lines = text.split('\n')
        height = min(max(len(lines), 1), 15)
        textfield.config(height=height+1, width=60, wrap="word", state=tk.DISABLED,)

    # näyttää näkymän
    def start(self):
        label = ttk.Label(self._root, text="Todistus", font=("Arial", 16, "bold"))
        label.pack(pady=(20, 15))

        # Tekstikenttien sisällöt
        textfields_list = [
            textfields.tehtavananto,
            textfields.alkuteksti,
            textfields.vaite_muotoilu,
            textfields.oletuskysymys
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
            self.format_text(textfield)

        [textfield.pack(fill="x", expand=False,padx=60, pady=(0, 5)) for textfield in texts]

        valinta = ttk.Combobox(
            self._root,
            values=textfields.oletusvaihtoehdot,
            width=50,
            state="readonly",
            font=("Arial", 11)
        )
        valinta.current(1)
        valinta.pack(pady=(5, 10))

        tulos_label = tk.Label(self._root, text="", font=("Arial", 12))
        tulos_label.pack(pady=10)

        # Funktio tarkistukseen
        def tarkista_vastaus():
            valittu = valinta.get()
            if valittu == textfields.oletusvastaus:
                tulos_label.config(text="Juuri näin!", fg="green")
                textfield = tk.Text(
                master=self._root,
                font=("Arial", 12),
                wrap="word",
                bg="white",
                relief="flat",
                borderwidth=0,
                highlightthickness=0
                )
                textfield.insert("1.0", valittu)
                self.format_text(textfield)
                textfield.pack(fill="x", expand=False,padx=60, pady=(0, 5))
                
            elif valittu=="a ja b ovat kokonaislukuja":
                tulos_label.config(text="a ja b ovat kokonaislukuja, mutta tiedämmekö niistä vielä jotain muuta?", fg="blue")
            else:
                tulos_label.config(text="Yritä uudelleen", fg="blue")

        # Tarkistusnappi
        tarkista_nappi = ttk.Button(self._root, text="Tarkista", command=tarkista_vastaus)
        tarkista_nappi.pack(pady=10)

        # Muut kontrollit
        button = ttk.Button(self._root, text="Jatka")
        entry = ttk.Entry(self._root)
        checkbutton = ttk.Checkbutton(self._root, text="Check button")

        button.pack(pady=(5, 10))
        entry.pack(pady=(0, 10))
        checkbutton.pack(pady=(0, 10))