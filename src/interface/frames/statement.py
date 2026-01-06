import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from tkinter import ttk
import textfields
from interface.edit_ui import *
from interface.frames.pairless_frame import *
from interface.ui_handler import *
from create_texts import statement_texts

# luo näkymän oletustehtävälle
def statement_view(screen):

    # luo tekstit
    phase = bold_phase_text(screen, "2")
    statement_texts(screen)

    # luodaan frame monivalintakentälle, joka piilotetaan myöhemmin näkyvistä
    frame = new_frame(screen)

    # luo monivalintakysymyksen
    choose_statement = new_combobox(frame, textfields.vaitevaihtoehdot)

    feedback_label = new_label(frame)

    # vaihtaa seuraavaan näkymään
    continue_button = ttk.Button(screen, text="Jatka", command=lambda:(
        show_pairless(),
        hide_button(continue_button),
        remove_bolding(phase)
    ))

    # tarkistaa vastauksen
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