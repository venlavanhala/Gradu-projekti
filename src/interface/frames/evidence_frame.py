import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
import tkinter as tk
from tkinter import ttk
import textfields
from interface.edit_ui import *
from interface.ui_handler import hide_frame, show_formatting, handle_combobox_check
import logic


def evidence_view(screen):

    # luodaan frame monivalintakentälle, joka piilotetaan myöhemmin näkyvistä
    format_textfield(screen, textfields.paritonjatko)

    frame = new_frame(screen)

    # monivalintakysymys

    choose_proof_method = new_combobox(frame, textfields.osoitusvaihtoehdot)

    feedback_label = new_label(frame)

    continue_button = ttk.Button(frame, text="Jatka", command=lambda: (
      show_formatting()  
    ))

    check_answer = ttk.Button(
    frame,
    text="Tarkista",
    command=lambda: (
        handle_combobox_check(choose_proof_method.get(), textfields.osoitusvastaus,
                              textfields.osoituspalautteet, screen, choose_proof_method,
                              feedback_label, check_answer, continue_button)
    ))
    check_answer.pack(pady=5)

    return frame