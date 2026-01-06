import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
import tkinter as tk
from tkinter import ttk
import textfields
from interface.edit_ui import *
from interface.frames.statement import *
from interface.ui_handler import *
from create_texts import starting_texts

# näkymä oletus-tehtävälle
def assumption_view(screen):

    # luodaan tyhjä alapalkki
    create_spacer()

    label = ttk.Label(screen, text="Harjoittele todistamista", font=("Georgia", 16, "bold"))
    label.pack(pady=(5,5))

    # luodaan tekstikentät ja lisätään niihin tekstit
    phase = bold_phase_text(screen, "1")
    starting_texts(screen)

    # luodaan frame monivalintakentälle, joka piilotetaan myöhemmin näkyvistä
    frame = new_frame(screen)

    # monivalintakysymys
    choose_assumption = new_combobox(frame, textfields.oletusvaihtoehdot)

    # palaute-teksti
    feedback_label = new_label(frame)

    # jatka-nappi, joka vaihtaa toiseen näkymään
    continue_button = ttk.Button(screen, text="Jatka", command=lambda: (
        show_statement(),
        hide_button(continue_button),
        remove_bolding(phase)
    ))

    # tarkista tehtävä
    check_assumption_answer = ttk.Button(
    frame,
    text="Tarkista",
    command=lambda: (
        handle_combobox_check(choose_assumption.get(), textfields.oletusvastaus, 
                            textfields.oletukset, screen, choose_assumption,
                            feedback_label, check_assumption_answer, continue_button)
    ))
    check_assumption_answer.pack(pady=5)


    return frame