import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
import tkinter as tk
from tkinter import ttk
import textfields
from interface.edit_ui import *
from interface.frames.pairless_frame import *
from interface.ui_handler import *


def statement_view(screen):


    statement_texts(screen)

    # luodaan frame monivalintakentälle, joka piilotetaan myöhemmin näkyvistä
    frame = new_frame(screen)

    # monivalintakysymys
    choose_statement = new_combobox(frame, textfields.vaitevaihtoehdot)

    feedback_label = new_label(frame)

    # VAIHDA SEURAAVAAN

    continue_button = ttk.Button(frame, text="Jatka", command=lambda:(
        show_pairless()
    ))


    check_answer = ttk.Button(
    frame,
    text="Tarkista",
    command=lambda: (
        handle_combobox_check(choose_statement.get(), textfields.vaitevastaus,
                                textfields.vaitteet, screen, choose_statement,
                                feedback_label, check_answer, continue_button)
    ))
    check_answer.pack(pady=5)



    return frame