import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
import tkinter as tk
from tkinter import ttk
import textfields
from interface.edit_ui import *
from interface.ui import show_evidence, hide_frame
import logic


def pairless_view(screen):

    # luodaan frame monivalintakentälle, joka piilotetaan myöhemmin näkyvistä
    format_textfield(screen, textfields.vaitejatko)

    frame = new_frame(screen)

    # monivalintakysymys

    excercise_frame = new_frame(frame)

    choose_statement = new_entry(excercise_frame, "a=", " (k \u2208 \u2124)")

    feedback_label = new_label(frame)

    # VAIHDA SEURAAVAAN

    continue_button = ttk.Button(frame, text="Jatka", command=lambda: (
      hide_frame(excercise_frame),
      show_evidence()  
    ))

    # nappi, jota painamalla tulee result ja UI puoli

    def handle_entry_check():
        answer = choose_statement.get()
        result = logic.check_entry(answer, textfields.pariton_oikeat)
        if result == True:
            entry_right_answer(answer,
            textfields.pariton_vaihtoehdot, feedback_label, frame,
            check_answer, continue_button)
        else:
            entry_wrong_answer(feedback_label)

    check_answer = ttk.Button(
    frame,
    text="Tarkista",
    command=lambda: (
        handle_entry_check()
    ))
    check_answer.pack(pady=5)

    return frame