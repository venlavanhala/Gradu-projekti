import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
import tkinter as tk
from tkinter import ttk, Tk
from interface.edit_ui import *

current_frame = None
root = None

def init(app_root):
    global root
    root = app_root

def create_window(screen):
    screen.title("TkInter esimerkki")
    screen.geometry("800x900") #näytön koko
    screen.configure(bg="white")
    # tee tässä myös scrollattava ikkuna
    window = scrollable_screen(screen)
    return window

def switch_to(frame_func):
    global current_frame

    if current_frame is not None:
        current_frame.destroy()

    current_frame = frame_func(root)
    current_frame.pack(fill="both", expand=True)

def start_assumption():
    from interface.frames.assumption import assumption_view
    switch_to(assumption_view)

def show_statement():
    from interface.frames.statement import statement_view
    switch_to(statement_view)

def show_pairless():
    from interface.frames.statement import pairless_view
    switch_to(pairless_view)

def show_evidence():
    from interface.frames.evidence_frame import evidence_view
    switch_to(evidence_view)

def show_formatting():
    from interface.frames.formatting_frame import formatting_view
    switch_to(formatting_view)

def show_end():
    from interface.frames.last_frame import end_view
    switch_to(end_view)

def create_spacer():
    spacer = tk.Frame(root, height=50, bg="white")   # 50px tyhjää tilaa
    spacer.pack(side="bottom", fill="x")

def hide_frame(frame):
    frame.destroy()

def hide_button(button):
    button.pack_forget()

def handle_pairless_check(answer, feedback_label, screen, checkbutton, continue_button):
    answer = answer.replace(" ","").replace("*", "").lower()
    result = logic.check_entry(answer, textfields.pariton_oikeat)
    if result == True:
        format_pairless_answer(answer,
        textfields.pariton_vaihtoehdot, feedback_label, screen, checkbutton, continue_button)
        textfields.valittu = answer
    else:
        entry_wrong_answer(feedback_label)

def handle_combobox_check(answer, right_answer, feedback, screen, combobox, feedback_label, checkbutton, continue_button):
    result = logic.check_combobox(answer, right_answer)
    if result == True:
        render_combobox_right_answer(answer, feedback,
                                    screen, combobox, feedback_label, checkbutton, continue_button)
    else:
        render_combobox_wrong_answer(answer, feedback, feedback_label)
 

def handle_formatting_check(answers, feedback_label, screen, checkbutton, continue_button):
    answer_list = [int(answer.get()) for answer in answers]
    result = logic.check_entries(answer_list, textfields.kirjoitusvastaus)
    if result == True:
        format_right_answer(feedback_label, screen, checkbutton, continue_button)
    else:
        format_wrong_answer(result, feedback_label)
    
def starting_texts(screen):
    format_textfield(screen, "[Vaihe 1]", "#6a0dad")
    format_textfield(screen, textfields.johdanto)
    format_textfield(screen, textfields.tehtavananto)
    format_textfield(screen, textfields.alkusuunnitelma)
    format_textfield(screen, textfields.alkuteksti, "#9c29c1")
    format_textfield(screen, textfields.oletuskysymys)

def statement_texts(screen):
    format_textfield(screen, "[Vaihe 2]", "#6a0dad")
    format_textfield(screen, textfields.oletusjatko, "#9c29c1")
    format_textfield(screen, textfields.vaitekysymys)


def pairless_texts(screen):
    format_textfield(screen, "\n[Vaihe 3]\n", "#6a0dad")
    format_textfield(screen, textfields.vaitejatko, "#9c29c1")
    format_textfield(screen, textfields.paritontieto)
    format_textfield(screen, textfields.paritonkysymys, "#9c29c1")
    format_textfield(screen, textfields.paritontieto2)

def evidence_texts(screen):
    format_textfield(screen, "\n[Vaihe 4]\n", "#6a0dad")
    if textfields.valittu == "2k+1":
        format_textfield(screen, textfields.paritonjatko, "#9c29c1")
        format_textfield(screen, textfields.maarittely)
        format_textfield(screen, textfields.tulo, "#9c29c1")
        format_textfield(screen, textfields.tulosievennys)
        format_textfield(screen, textfields.tulo2, "#9c29c1")
    else:
        format_textfield(screen, textfields.paritonjatko_, "#9c29c1")
        format_textfield(screen, textfields.maarittely_)
        format_textfield(screen, textfields.tulo_, "#9c29c1")
        format_textfield(screen, textfields.tulosievennys_)
        format_textfield(screen, textfields.tulo2_, "#9c29c1")

def formatting_texts(screen):
    format_textfield(screen, "[Vaihe 5]\n", "#6a0dad")
    if textfields.valittu == "2k+1":
        format_textfield(screen, textfields.osoitusjatko, "#9c29c1")
    else:
        format_textfield(screen, textfields.osoitusjatko_, "#9c29c1")

def end_texts(screen):
    format_textfield(screen, "[Vaihe 5]\n", "#6a0dad")
    if textfields.valittu == "2k+1":
        format_textfield(screen, textfields.lopputeksti, "#9c29c1")
    else:
        format_textfield(screen, textfields.lopputeksti_, "#9c29c1")