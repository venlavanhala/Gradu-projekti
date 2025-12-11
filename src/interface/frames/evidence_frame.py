import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
import tkinter as tk
from tkinter import ttk
import textfields
from interface.edit_ui import *
from interface.ui_handler import *
import logic


def evidence_view(screen):

    # luodaan frame monivalintakentälle, joka piilotetaan myöhemmin näkyvistä
    evidence_texts(screen)

    frame = new_frame(screen)

    # monivalintakysymys

    valittu = textfields.valittu

    # tämä määritys muualle
    if valittu == "2k+1":
      choose_proof_method = new_combobox(frame, textfields.osoitusvaihtoehdot)
      osoitusvastaus = textfields.osoitusvastaus
      osoituspalautteet = textfields.osoituspalautteet
    else:
      choose_proof_method = new_combobox(frame, textfields.osoitusvaihtoehdot_)
      osoitusvastaus = textfields.osoitusvastaus_
      osoituspalautteet = textfields.osoituspalautteet_

    feedback_label = new_label(frame)

    continue_button = ttk.Button(screen, text="Jatka", command=lambda: (
      show_formatting(),
      hide_button(continue_button)
    ))

    check_answer = ttk.Button(
    frame,
    text="Tarkista",
    command=lambda: (
        handle_combobox_check(choose_proof_method.get(), osoitusvastaus,
                              osoituspalautteet, screen, choose_proof_method,
                              feedback_label, check_answer, continue_button)
    ))
    check_answer.pack(pady=5)

    return frame