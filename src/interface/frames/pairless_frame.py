import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
import tkinter as tk
from tkinter import ttk
import textfields
from interface.edit_ui import *
from interface.ui_handler import *
import logic


def pairless_view(screen):

    # luodaan frame monivalintakentälle, joka piilotetaan myöhemmin näkyvistä
    pairless_texts(screen)

    frame = new_frame(screen)

    # monivalintakysymys

    excercise_frame = new_frame(frame)

    write_formatting = new_entry(excercise_frame, "a=", " (k \u2208 \u2124)")

    feedback_label = new_label(frame)

    # VAIHDA SEURAAVAAN

    continue_button = ttk.Button(screen, text="Jatka", command=lambda: (
      hide_frame(excercise_frame),
      show_evidence(),
      hide_button(continue_button)
    ))

    check_answer = ttk.Button(
    frame,
    text="Tarkista",
    command=lambda: (
        handle_pairless_check(write_formatting.get(), feedback_label, screen, check_answer, continue_button)
    ))
    check_answer.pack(pady=5)

    tip_pairless = ttk.Button(frame, text="Vihje", command=lambda: (
        popup_window(frame, textfields.pariton_vihje1),
        tip_2_pairless.pack(pady=(5, 10))))
    
    tip_pairless.pack(pady=(5, 5))

    tip_2_pairless = ttk.Button(frame, text="Vihje 2", command=lambda: popup_window(frame, textfields.pariton_vihje2))

    return frame