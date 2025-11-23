import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
import tkinter as tk
from tkinter import ttk
import textfields
from interface.edit_ui import *
from interface.pairless_frame import *
from interface.ui import *
import logic


def statement_view(screen):

    # luodaan frame monivalintakentälle, joka piilotetaan myöhemmin näkyvistä
    format_textfield(screen, textfields.oletusjatko)

    frame = new_frame(screen)


    # monivalintakysymys
    choose_statement = new_combobox(frame, textfields.vaitevaihtoehdot)

    feedback_label = new_label(frame)

    # VAIHDA SEURAAVAAN

    continue_button = ttk.Button(frame, text="Jatka", command=lambda:(
        show_pairless()
    ))

    # nappi, jota painamalla tulee result ja UI puoli

    def handle_combobox_check():
        answer = choose_statement.get()
        result = logic.check_combobox(answer, textfields.vaitevastaus)
        if result == True:
            render_combobox_right_answer(answer, textfields.vaitteet,
                                         screen, choose_statement, feedback_label,
                                         check_answer, continue_button)
        else:
            render_combobox_wrong_answer(answer, textfields.vaitteet, feedback_label)

    check_answer = ttk.Button(
    frame,
    text="Tarkista",
    command=lambda: (
        handle_combobox_check()
    ))
    check_answer.pack(pady=5)

    return frame