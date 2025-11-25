import tkinter as tk
from tkinter import ttk
import textfields
from activity import *
from change_layout import *

# ei tarvi luokkaa

class UI:
    def __init__(self, root):
        self._root = root
        self._root.geometry("800x900") #näytön koko
        self._root.configure(bg="white")
        self.scrollable_frame = scrollable_screen(self._root)

    # käynnistää näkymän
    def start(self):
        label = ttk.Label(self.scrollable_frame, text="Harjoittele todistamista", font=("Georgia", 16, "bold"))
        label.pack(pady=(5,5))

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
        frame = tk.Frame(self.scrollable_frame, bg="white", pady=0)
        frame.pack()

        # monivalintakysymys
        choose_assumption = ttk.Combobox(
            frame,
            values=textfields.oletusvaihtoehdot,
            width=50,
            state="readonly",
            font=("Georgia", 11)
        )
        choose_assumption.current(1)
        choose_assumption.pack(pady=(0,5))

        feedback_label = tk.Label(text="", font=("Georgia", 12), bg="white")
        feedback_label.pack(pady=5)

        # tarkista-nappi, joka kutsuu palautelabelin uusimisfunktiota ja tehtävän tarkistusfunktiota
        check_assumption_answer = ttk.Button(
            frame,
            text="Tarkista",
            command=lambda: (move_label(feedback_label, frame), check_combobox(self.scrollable_frame, choose_assumption, textfields.oletusvastaus, feedback_label, textfields.oletukset, continue_button1, check_assumption_answer))
        )
        check_assumption_answer.pack(pady=5)

        # tehdään uusi frame väitemonivalinnalle
        statement_frame = tk.Frame(self.scrollable_frame, bg="white", pady=0)

        # toinen monivalintakysymys
        choose_statement = ttk.Combobox(
            statement_frame,
            values=textfields.vaitevaihtoehdot,
            width=50,
            state="readonly",
            font=("Georgia", 11)
        )
        choose_statement.current(1)
        choose_statement.pack(pady=(5, 5))

        # tarkista-nappi, joka kutsuu tarkistusfunktiota
        check_statement_answer = ttk.Button(
            statement_frame,
            text="Tarkista",
            command=lambda: (move_label(feedback_label, statement_frame), check_combobox(self.scrollable_frame, choose_statement, textfields.vaitevastaus, feedback_label, textfields.vaitteet, continue_button2, check_statement_answer))
        )
        check_statement_answer.pack(pady=5)

        pairless_frame = tk.Frame(self.scrollable_frame, bg="white", pady=0)

        # oma frame vastauskentän muotoiluun
        entry_frame = tk.Frame(pairless_frame, bg="white", pady=0)
        entry_frame.pack()
        tk.Label(entry_frame, text="a=", bg="white").pack(side="left")
        pairless_field = tk.Entry(entry_frame, width=20)
        pairless_field.pack(side="left",pady=5)
        tk.Label(entry_frame, text="(k \u2208 \u2124)", bg="white").pack(side="left")

        # tarkista-nappi, joka kutsuu tarkistusfunktiota
        check_pairless_answer = ttk.Button(
            pairless_frame,
            text="Tarkista",
            command=lambda: (move_label(feedback_label, pairless_frame), check_entry(self.scrollable_frame, pairless_field, textfields.pariton_oikeat, feedback_label, textfields.pariton_vaihtoehdot, continue_button3, check_pairless_answer)))
        check_pairless_answer.pack(pady=5)

        tip_pairless = ttk.Button(pairless_frame, text="Vihje", command=lambda: (popup_window(pairless_frame, textfields.pariton_vihje1), tip_2_pairless.pack(pady=(5, 10))))
        tip_pairless.pack(pady=(5, 5))

        tip_2_pairless = ttk.Button(pairless_frame, text="Vihje 2", command=lambda: popup_window(pairless_frame, textfields.pariton_vihje2))

        evidence_frame = tk.Frame(self.scrollable_frame, bg="white",pady=0)

        choose_evidence = ttk.Combobox(
        evidence_frame,
        values=textfields.osoitusvaihtoehdot,
        width=60,
        state="readonly",
        font=("Georgia", 11)
        )
        choose_evidence.current(1)
        choose_evidence.pack(pady=(5, 5))

        # tarkista-nappi, joka kutsuu tarkistusfunktiota
        check_evidence_answer = ttk.Button(
            evidence_frame,
            text="Tarkista",
            command=lambda: (move_label(feedback_label, evidence_frame), check_combobox(self.scrollable_frame, choose_evidence, textfields.osoitusvastaus, feedback_label, textfields.osoituspalautteet, continue_button4, check_evidence_answer))
        )
        check_evidence_answer.pack(pady=5)

        formatting_frame = tk.Frame(self.scrollable_frame, bg="white",pady=0)

        formatting_field = tk.Entry(formatting_frame, width=20)
        formatting_field.pack(pady=5)

        # tarkista-nappi, joka kutsuu tarkistusfunktiota
        check_formatting_answer = ttk.Button(
            formatting_frame,
            text="Tarkista",
            command=lambda: (move_label(feedback_label, formatting_frame), check_entry(self.scrollable_frame, formatting_field, textfields.pariton_oikeat, feedback_label, textfields.pariton_vaihtoehdot, continue_button4, check_formatting_answer))
        )
        check_formatting_answer.pack(pady=5)

        tip_divisible = ttk.Button(formatting_frame, text="Vihje", command=lambda: popup_window(formatting_frame, textfields.kirjoitusvihje))
        tip_divisible.pack(pady=(5, 5))

        # Jatka-nappi piilottaa framen ja lisää uuden tekstin näytölle
        continue_button1 = ttk.Button(frame, text="Jatka", command=lambda: (jatka(self.scrollable_frame,frame,textfields.oletusjatko), statement_frame.pack()))

        continue_button2 = ttk.Button(statement_frame, text="Jatka", command=lambda: (jatka(self.scrollable_frame,statement_frame,textfields.vaitejatko), pairless_frame.pack()))

        continue_button3 = ttk.Button(pairless_frame, text="Jatka", command=lambda: (jatka(self.scrollable_frame,pairless_frame,textfields.paritonjatko), evidence_frame.pack()))

        continue_button4 = ttk.Button(evidence_frame, text="Jatka", command=lambda: (jatka(self.scrollable_frame,evidence_frame,textfields.osoitusjatko), formatting_frame.pack()))