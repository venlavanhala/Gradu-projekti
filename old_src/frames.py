import tkinter as tk
from tkinter import ttk
import textfields
from activity import *
from change_layout import *

class Frame:
    def __init__(self, master):
        self._master = master
        self.frame=tk.Frame(self._master, bg="white", pady=0)

    def make_combobox():
        excercise = ttk.Combobox(
        self.frame,
        values=textfields.oletusvaihtoehdot,
        width=50,
        state="readonly",
        font=("Georgia", 11)    
    )

    def check_combobox():
        pass

choose_assumption = ttk.Combobox(
    frame,
    values=textfields.oletusvaihtoehdot,
    width=50,
    state="readonly",
    font=("Georgia", 11)
)
choose_assumption.current(1)
choose_assumption.pack(pady=(0,5))