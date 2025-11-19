from tkinter import Tk, ttk
import tkinter as tk
from .textfields import *  # oletetaan että tässä on esim. starting_text jne.

class UI:
    def __init__(self, root):
        self._root = root
        self._root.geometry("800x600")
        self._root.configure(bg="white")

    def format_text(self, textfield):
        """Muotoilee tekstikentän korkeuden tekstin rivimäärän mukaan"""
        text = textfield.get("1.0", "end-1c")
        lines = text.split("\n")
        # rivimäärä = tekstin rivit, vähintään 1, enintään 15
        height = min(max(len(lines), 1), 15)

        textfield.config(
            height=height+1,
            width=70,         # kiinteä leveys, estää vaakavenymisen
            wrap="word",
            state=tk.DISABLED,
            bg="white",
            relief="flat",
            borderwidth=0,
            highlightthickness=0
        )

    def start(self):
        # Otsikko
        label = ttk.Label(self._root, text="Todistus", font=("Arial", 16, "bold"))
        label.pack(pady=(20, 15))

        # Tekstikentät
        textfields_list = [
            textfields.alkuteksti,
            textfields.vaite_muotoilu,
            textfields.oletuskysymys
        ]

        for text in textfields_list:
            textfield = tk.Text(
                master=self._root,
                font=("Arial", 12),
                wrap="word",
                bg="white"
            )
            textfield.insert("1.0", text)
            self.format_text(textfield)
            textfield.pack(fill="x", expand=False,padx=60, pady=(0, 5))  # pieni väli vain

        # Combobox
        vaihtoehdot = [
            "a ja b ovat parittomia lukuja",
            "a ja b ovat kokonaislukuja",
            "lukujen a ja b tulo on pariton luku"
        ]

        valinta = ttk.Combobox(
            self._root,
            values=vaihtoehdot,
            width=50,
            state="readonly",
            font=("Arial", 11)
        )
        valinta.current(0)
        valinta.pack(pady=(5, 10))

        # Muut kontrollit
        button = ttk.Button(self._root, text="Button")
        entry = ttk.Entry(self._root)
        checkbutton = ttk.Checkbutton(self._root, text="Check button")

        button.pack(pady=(5, 10))
        entry.pack(pady=(0, 10))
        checkbutton.pack(pady=(0, 10))


# ---- Sovelluksen käynnistys ----

if __name__ == "__main__":
    window = Tk()
    window.title("TkInter esimerkki")

    ui = UI(window)
    ui.start()

    window.mainloop()