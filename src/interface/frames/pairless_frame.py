import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
import tkinter as tk
from tkinter import ttk
import textfields
from interface.edit_ui import *
from interface.ui_handler import *
from create_texts import pairless_texts

# luo näkymän pariton-tehtävälle
def pairless_view(screen):

    # luo tekstit
    phase = bold_phase_text(screen, "3")
    pairless_texts(screen)

    # luodaan frame tehtäväkentälle, joka piilotetaan myöhemmin näkyvistä
    frame = new_frame(screen)

    # luo framen vastauskentälle
    excercise_frame = new_frame(frame)

    # luo entry-tehtävän
    write_formatting = new_entry(excercise_frame, "a=", " (k \u2208 \u2124)")

    feedback_label = new_label(frame)

    # vaihtaa seuraavaan näkymään
    continue_button = ttk.Button(screen, text="Jatka", command=lambda: (
      hide_frame(excercise_frame),
      show_evidence(),
      hide_button(continue_button),
      remove_bolding(phase)
    ))

    # tarkistaa vastauksen
    check_answer = ttk.Button(
    frame,
    text="Tarkista",
    command=lambda: (
        handle_pairless_check(write_formatting.get(), feedback_label, screen, check_answer, continue_button)
    ))
    check_answer.pack(pady=5)

    # luo vihjenapin, jota painaessa ilmestyy toinen vihje
    tip_pairless = ttk.Button(frame, text="Vihje", command=lambda: (
        popup_window(frame, textfields.pariton_vihje1),
        tip_2_pairless.pack(pady=(5, 10))))
    
    tip_pairless.pack(pady=(5, 5))

    # toinen vihjenappi
    tip_2_pairless = ttk.Button(frame, text="Vihje 2", command=lambda: popup_window(frame, textfields.pariton_vihje2))

    return frame