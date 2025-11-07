import tkinter as tk
from tkinter import ttk
import textfields
from activity import *
from change_layout import *

class UI:
    def __init__(self, root):
        self._root = root
        self._root.geometry("800x900")
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
                master=self.scrollable_frame,
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

        # luodaan frame monivalintakentälle, joka piilotetaan myöhemmin näkyvistä
        frame = tk.Frame(self.scrollable_frame, bg="white")
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

        tulos_label = tk.Label(frame, text="", font=("Arial", 12), bg="white")
        tulos_label.pack(pady=10)

        # tarkista-nappi, joka kutsuu tarkistusfunktiota
        tarkista_nappi = ttk.Button(
            frame,
            text="Tarkista",
            command=lambda: check_combobox(self.scrollable_frame, valinta, textfields.oletusvastaus, tulos_label, textfields.oletukset, button)
        )
        tarkista_nappi.pack(pady=10)

        # tehdään uusi frame väitemonivalinnalle
        vaiteframe = tk.Frame(self.scrollable_frame, bg="white")

        # toinen monivalintakysymys
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

        # tarkista-nappi, joka kutsuu tarkistusfunktiota
        tarkista_nappi2 = ttk.Button(
            vaiteframe,
            text="Tarkista",
            command=lambda: check_combobox(self.scrollable_frame, vaiteboksi, textfields.vaitevastaus, palauteteksti, textfields.vaitteet, button2)
        )
        tarkista_nappi2.pack(pady=10)

        paritonframe = tk.Frame(self.scrollable_frame, bg="white")

        pariton_kentta = tk.Entry(paritonframe, width=20)
        pariton_kentta.pack(pady=10)

        tuloskentta = tk.Label(paritonframe, text="", font=("Arial", 12), bg="white")
        tuloskentta.pack(pady=10)

        # tarkista-nappi, joka kutsuu tarkistusfunktiota
        tarkista_nappi3 = ttk.Button(
            paritonframe,
            text="Tarkista",
            command=lambda: check_entry(self.scrollable_frame, pariton_kentta, textfields.pariton_oikeat, tuloskentta, textfields.pariton_vaihtoehdot, button3)
        )
        tarkista_nappi3.pack(pady=10)

        pariton_button = ttk.Button(paritonframe, text="Vihje", command=lambda: popup_window(paritonframe, textfields.pariton_vihje1))
        pariton_button.pack(pady=(5, 10))

        # Jatka-nappi piilottaa framen ja lisää uuden tekstin näytölle
        button = ttk.Button(frame, text="Jatka", command=lambda: (jatka(self.scrollable_frame,frame,textfields.oletusjatko), vaiteframe.pack()))

        button2 = ttk.Button(vaiteframe, text="Jatka", command=lambda: (jatka(self.scrollable_frame,vaiteframe,textfields.vaitejatko), paritonframe.pack()))

        button3 = ttk.Button(paritonframe, text="Jatka", command=lambda: (jatka(self.scrollable_frame,paritonframe,textfields.paritonjatko)))