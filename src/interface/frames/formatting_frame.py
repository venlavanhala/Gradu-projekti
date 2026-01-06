import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
import tkinter as tk
from tkinter import ttk
import textfields
from interface.edit_ui import *
from interface.ui_handler import *
from create_texts import formatting_texts

# näkymä muotoilutehtävälle
def formatting_view(screen):

    # lisää tekstit
    phase = bold_phase_text(screen, "5")
    formatting_texts(screen)

    # luo uusi frame tehtävänäkymälle
    frame = new_frame(screen)

    # luo frame vastauskentälle
    excercise_frame = new_frame(frame)

    # tekee kirjoitustehtävän
    choose_answer = create_formatting_entries(excercise_frame, textfields.valittu)

    # luo palautetekstin
    feedback_label = new_label(frame)

    # vaihtaa seuraavan framen
    continue_button = ttk.Button(screen, text="Jatka", command=lambda: (
      hide_frame(excercise_frame),
      show_end(),
      hide_button(continue_button),
      remove_bolding(phase)
    ))

    # tarkistaa vastauksen
    check_answer = ttk.Button(
    frame,
    text="Tarkista",
    command=lambda: (
        handle_formatting_check(choose_answer, feedback_label, screen, check_answer, continue_button)
    ))
    check_answer.pack(pady=5)

    return frame