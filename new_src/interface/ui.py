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
    from interface.assumption import assumption_view
    switch_to(assumption_view)

def show_statement():
    from interface.statement import statement_view
    switch_to(statement_view)

def show_pairless():
    from interface.statement import pairless_view
    switch_to(pairless_view)

def show_evidence():
    from interface.evidence_frame import evidence_view
    switch_to(evidence_view)

def hide_frame(frame):
    frame.destroy()