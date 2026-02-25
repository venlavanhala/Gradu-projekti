import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
import tkinter as tk
from interface.edit_ui import *
import logic

current_frame = None
root = None

def init(app_root):
    global root
    root = app_root

# luo ikkuna
def create_window(screen):
    screen.title("TkInter esimerkki")
    screen.geometry("800x900") #näytön koko
    screen.configure(bg="white")
    window = scrollable_screen(screen)
    return window

# vaihda toiseen tehtävänäkymään
def switch_to(frame_func):
    global current_frame

    if current_frame is not None:
        current_frame.destroy()

    current_frame = frame_func(root)
    current_frame.pack(fill="both", expand=True)

# käynnistää näkymän oletus-tehtävälle
def start_assumption():
    from interface.frames.assumption import assumption_view
    switch_to(assumption_view)

# käynnistää väitenäkymän
def show_statement():
    from interface.frames.statement import statement_view
    switch_to(statement_view)

# käynnistää näkymän pariton-tehtävälle
def show_pairless():
    from interface.frames.statement import pairless_view
    switch_to(pairless_view)

# käynnistää osoitusnäkymän 
def show_evidence():
    from interface.frames.evidence_frame import evidence_view
    switch_to(evidence_view)

# käynnistää muotoilunäkymän 
def show_formatting():
    from interface.frames.formatting_frame import formatting_view
    switch_to(formatting_view)

# käynnistää viimeisen näkymän 
def show_end():
    from interface.frames.last_frame import end_view
    switch_to(end_view)

# luo tyhjän välin ikkunan loppuun
def create_spacer():
    spacer = tk.Frame(root, height=50, bg="white")
    spacer.pack(side="bottom", fill="x")

# käsittelee tarkistuksen pariton-tehtälle
def handle_pairless_check(answer, feedback_label, screen, checkbutton, continue_button):
    answer = answer.replace(" ","").replace("*", "").lower()
    result = logic.check_entry(answer, textfields.pariton_oikeat)
    if result == True:
        show_pairless_answer(answer,
        textfields.pariton_vaihtoehdot, feedback_label, screen, checkbutton, continue_button)
        textfields.valittu = answer
    else:
        entry_wrong_answer(feedback_label)

# käsittelee tarkistuksen monivalintatehtälle
def handle_combobox_check(answer, right_answer, feedback, screen, combobox, feedback_label, checkbutton, continue_button):
    result = logic.check_combobox(answer, right_answer)
    if result == True:
        show_combobox_right_answer(answer, feedback,
                                    screen, combobox, feedback_label, checkbutton, continue_button)
    else:
        show_combobox_wrong_answer(answer, feedback, feedback_label)
 
# # käsittelee tarkistuksen muotoilu-tehtälle
def handle_formatting_check(answers, feedback_label, screen, checkbutton, continue_button):
    answer_list = [int(answer.get()) for answer in answers]
    result = logic.check_entries(answer_list, textfields.kirjoitusvastaus)
    if result == True:
        format_right_answer(feedback_label, screen, checkbutton, continue_button)
    else:
        format_wrong_answer(result, feedback_label)
    