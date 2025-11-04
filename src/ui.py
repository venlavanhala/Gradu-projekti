import tkinter as tk
from tkinter import ttk
import textfields
from functions import *
from change_layout import *

class UI:
    def __init__(self, root):
        self._root = root
        self._root.geometry("800x600")
        self._root.configure(bg="white")
        self.scrollable_frame = scrollable_screen(self._root)

    # käynnistää näkymän
    def start(self):
        label = ttk.Label(self.scrollable_frame, text="Harjoittele todistamista", font=("Arial", 16, "bold"))
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
                master=self.scrollable_frame,   # ⬅️ HUOM! root → scrollable_frame
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

        [textfield.pack(fill="x", expand=False, padx=60, pady=(0, 5)) for textfield in texts]

        frame = tk.Frame(self.scrollable_frame, bg="white")
        frame.pack()

        valinta = ttk.Combobox(
            frame,
            values=textfields.oletusvaihtoehdot,
            width=50,
            state="readonly",
            font=("Arial", 11)
        )
        valinta.current(1)
        valinta.pack(pady=(5, 10))

        tulos_label = tk.Label(frame, text="", font=("Arial", 12), bg="white")
        tulos_label.pack(pady=10)

        tarkista_nappi = ttk.Button(
            frame,
            text="Tarkista",
            command=lambda: tarkista_monivalinta(self.scrollable_frame, valinta, textfields.oletusvastaus, tulos_label)
        )
        tarkista_nappi.pack(pady=10)

        # ===== 2. MONIVALINTA — piilotettu aluksi =====
        vaiteframe = tk.Frame(self.scrollable_frame, bg="white")
        # ei pack() tähän

        vaiteboksi = ttk.Combobox(
            vaiteframe,
            values=textfields.vaitevaihtoehdot,
            width=50,
            state="readonly",
            font=("Arial", 11)
        )
        vaiteboksi.current(1)
        vaiteboksi.pack(pady=(5, 10))

        palauteteksti = tk.Label(vaiteframe, text="", font=("Arial", 12), bg="white")
        palauteteksti.pack(pady=10)

        tarkista_nappi2 = ttk.Button(
            vaiteframe,
            text="Tarkista",
            command=lambda: tarkista_monivalinta(self.scrollable_frame, vaiteboksi, textfields.vaitevastaus, palauteteksti)
        )
        tarkista_nappi2.pack(pady=10)

        def jatka():
            frame.pack_forget()
            new_text(self.scrollable_frame, textfields.oletusjatko)
            vaiteframe.pack()

        button = ttk.Button(frame, text="Jatka", command=jatka)
        button.pack(pady=(5, 10))
