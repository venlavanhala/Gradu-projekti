import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
import tkinter as tk
from tkinter import ttk
import textfields
from interface.edit_ui import *
import logic
from interface.statement import *
from interface.ui import *

def assumption_view(screen):

    label = ttk.Label(screen, text="Harjoittele todistamista", font=("Georgia", 16, "bold"))
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
        format_textfield(screen, text)

    # luodaan frame monivalintakentälle, joka piilotetaan myöhemmin näkyvistä
    frame = new_frame(screen)

    # monivalintakysymys
    choose_assumption = new_combobox(frame, textfields.oletusvaihtoehdot)

    feedback_label = new_label(frame)

    continue_button = ttk.Button(frame, text="Jatka", command=lambda: (
        show_statement()
    ))

    # nappi, jota painamalla tulee result ja UI puoli

    def handle_combobox_check():
        answer = choose_assumption.get()
        result = logic.check_combobox(answer, textfields.oletusvastaus)
        if result == True:
            render_combobox_right_answer(answer, textfields.oletukset,
                                         screen, choose_assumption, feedback_label,
                                         check_assumption_answer, continue_button)
        else:
            render_combobox_wrong_answer(answer, textfields.oletukset, feedback_label)

    check_assumption_answer = ttk.Button(
    frame,
    text="Tarkista",
    command=lambda: (
        handle_combobox_check()
    ))
    check_assumption_answer.pack(pady=5)

    return frame