import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
import tkinter as tk
from tkinter import ttk
import textfields
from interface.edit_ui import *
from interface.ui_handler import *


def formatting_view(screen):

    # luodaan frame monivalintakentälle, joka piilotetaan myöhemmin näkyvistä
    formatting_texts(screen)

    frame = new_frame(screen)

    # monivalintakysymys

    excercise_frame = new_frame(frame)

    choose_answer = create_formatting_entries(excercise_frame, textfields.valittu)

    feedback_label = new_label(frame)

    # VAIHDA SEURAAVA FRAME

    continue_button = ttk.Button(screen, text="Jatka", command=lambda: (
      hide_frame(excercise_frame),
      show_end(),
      hide_button(continue_button)
    ))

    check_answer = ttk.Button(
    frame,
    text="Tarkista",
    command=lambda: (
        handle_formatting_check(choose_answer, feedback_label, screen, check_answer, continue_button)
    ))
    check_answer.pack(pady=5)

    return frame