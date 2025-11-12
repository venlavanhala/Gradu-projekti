import tkinter as tk
from tkinter import ttk
import textfields
from activity import *
from change_layout import *

class UI:
    def __init__(self, root):
        self._root = root
        self._root.geometry("800x900") #näytön koko
        self._root.configure(bg="white")
        self.scrollable_frame = scrollable_screen(self._root)

    # käynnistää näkymän
    def start(self):
        label = ttk.Label(self.scrollable_frame, text="Harjoittele todistamista", font=("Georgia", 16, "bold"))
        label.pack(pady=(20, 15))

        # ensimmäisten tekstikenttien sisällöt
        textfields_list = [
            textfields.johdanto,
            textfields.tehtavananto,
            textfields.alkuteksti,
            textfields.vaite_muotoilu
        ]

        # luodaan tekstikentät ja lisätään niihin tekstit
        for text in textfields_list:
            format_textfield(self.scrollable_frame, text)

        # luodaan frame monivalintakentälle, joka piilotetaan myöhemmin näkyvistä
        frame = tk.Frame(self.scrollable_frame, bg="white")
        frame.pack()

        # monivalintakysymys
        valinta = ttk.Combobox(
            frame,
            values=textfields.oletusvaihtoehdot,
            width=50,
            state="readonly",
            font=("Georgia", 11)
        )
        valinta.current(1)
        valinta.pack(pady=(5, 10))

        tulos_label = tk.Label(frame, text="", font=("Georgia", 12), bg="white")
        tulos_label.pack(pady=10)

        # tarkista-nappi, joka kutsuu tarkistusfunktiota
        tarkista_nappi = ttk.Button(
            frame,
            text="Tarkista",
            command=lambda: check_combobox(self.scrollable_frame, valinta, textfields.oletusvastaus, tulos_label, textfields.oletukset, button, tarkista_nappi)
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
            font=("Georgia", 11)
        )
        vaiteboksi.current(1)
        vaiteboksi.pack(pady=(5, 10))

        palauteteksti = tk.Label(vaiteframe, text="", font=("Georgia", 12), bg="white")
        palauteteksti.pack(pady=10)

        # tarkista-nappi, joka kutsuu tarkistusfunktiota
        tarkista_nappi2 = ttk.Button(
            vaiteframe,
            text="Tarkista",
            command=lambda: check_combobox(self.scrollable_frame, vaiteboksi, textfields.vaitevastaus, palauteteksti, textfields.vaitteet, button2, tarkista_nappi2)
        )
        tarkista_nappi2.pack(pady=10)

        paritonframe = tk.Frame(self.scrollable_frame, bg="white")

        pariton_kentta = tk.Entry(paritonframe, width=20)
        pariton_kentta.pack(pady=10)

        tuloskentta = tk.Label(paritonframe, text="", font=("Georgia", 12), bg="white")
        tuloskentta.pack(pady=10)

        # tarkista-nappi, joka kutsuu tarkistusfunktiota
        tarkista_nappi3 = ttk.Button(
            paritonframe,
            text="Tarkista",
            command=lambda: check_entry(self.scrollable_frame, pariton_kentta, textfields.pariton_oikeat, tuloskentta, textfields.pariton_vaihtoehdot, button3, tarkista_nappi3)
        )
        tarkista_nappi3.pack(pady=10)

        pariton_button = ttk.Button(paritonframe, text="Vihje", command=lambda: (popup_window(paritonframe, textfields.pariton_vihje1), pariton_button2.pack(pady=(5, 10))))
        pariton_button.pack(pady=(5, 10))

        pariton_button2 = ttk.Button(paritonframe, text="Vihje 2", command=lambda: popup_window(paritonframe, textfields.pariton_vihje2))

        osoitusframe = tk.Frame(self.scrollable_frame, bg="white")

        osoitusboksi = ttk.Combobox(
        osoitusframe,
        values=textfields.osoitusvaihtoehdot,
        width=60,
        state="readonly",
        font=("Georgia", 11)
    )
        osoitusboksi.current(1)
        osoitusboksi.pack(pady=(5, 10))

        palauteosoitus = tk.Label(osoitusframe, text="", font=("Georgia", 12), bg="white")
        palauteosoitus.pack(pady=10)

        # tarkista-nappi, joka kutsuu tarkistusfunktiota
        tarkista_nappi4 = ttk.Button(
            osoitusframe,
            text="Tarkista", #muuta väitteet osoituksiksi uuteen
            command=lambda: check_combobox(self.scrollable_frame, osoitusboksi, textfields.osoitusvastaus, palauteosoitus, textfields.osoituspalautteet, button4, tarkista_nappi4)
        )
        tarkista_nappi4.pack(pady=10)

        muotoiluframe = tk.Frame(self.scrollable_frame, bg="white")

        muotoilu_kentta = tk.Entry(muotoiluframe, width=20)
        muotoilu_kentta.pack(pady=10)

        muotoilu_palaute = tk.Label(muotoiluframe, text="", font=("Georgia", 12), bg="white")
        muotoilu_palaute.pack(pady=10)

        # tarkista-nappi, joka kutsuu tarkistusfunktiota
        tarkista_nappi5 = ttk.Button(
            muotoiluframe,
            text="Tarkista", # muokkaa nämä
            command=lambda: check_entry(self.scrollable_frame, muotoilu_kentta, textfields.pariton_oikeat, muotoilu_palaute, textfields.pariton_vaihtoehdot, button4, tarkista_nappi5)
        )
        tarkista_nappi5.pack(pady=10)

        jaollinen_button = ttk.Button(muotoiluframe, text="Vihje", command=lambda: popup_window(muotoiluframe, textfields.pariton_vihje1))
        jaollinen_button.pack(pady=(5, 10))




        # Jatka-nappi piilottaa framen ja lisää uuden tekstin näytölle
        button = ttk.Button(frame, text="Jatka", command=lambda: (jatka(self.scrollable_frame,frame,textfields.oletusjatko), vaiteframe.pack()))

        button2 = ttk.Button(vaiteframe, text="Jatka", command=lambda: (jatka(self.scrollable_frame,vaiteframe,textfields.vaitejatko), paritonframe.pack()))

        button3 = ttk.Button(paritonframe, text="Jatka", command=lambda: (jatka(self.scrollable_frame,paritonframe,textfields.paritonjatko), osoitusframe.pack()))

        button4 = ttk.Button(osoitusframe, text="Jatka", command=lambda: (jatka(self.scrollable_frame,osoitusframe,textfields.osoitusjatko), muotoiluframe.pack()))