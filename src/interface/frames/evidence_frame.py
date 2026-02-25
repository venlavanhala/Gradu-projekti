import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
import tkinter as tk
from tkinter import ttk
import textfields
from interface.edit_ui import *
from interface.ui_handler import *
from create_texts import evidence_texts

# näkymä osoitustehtävälle
def evidence_view(screen):

    # luo tekstit
    phase = bold_phase_text(screen, "4")
    evidence_texts(screen)

    # luo framen tehtävälle
    frame = new_frame(screen)

    valittu = textfields.valittu

    # määritetään tehtävän vaihtoehdot ja kysymykset sen mukaan, mitä vastattiin aikaisemmassa tehtävässä
    if valittu == "2k+1":
      choose_proof_method = new_combobox(frame, textfields.osoitusvaihtoehdot)
      osoitusvastaus = textfields.osoitusvastaus
      osoituspalautteet = textfields.osoituspalautteet
    else:
      choose_proof_method = new_combobox(frame, textfields.osoitusvaihtoehdot_)
      osoitusvastaus = textfields.osoitusvastaus_
      osoituspalautteet = textfields.osoituspalautteet_

    # palaute-teksti
    feedback_label = new_label(frame)

    # jatka seuraavaan näkymään
    continue_button = ttk.Button(screen, text="Jatka", command=lambda: (
      show_formatting(),
      hide_button(continue_button),
      remove_bolding(phase)
    ))

    # tarkista vastaus
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