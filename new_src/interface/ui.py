import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
import tkinter as tk
from tkinter import ttk, Tk
from interface.assumption import *
from interface.edit_ui import *


# käyttöliittymän pohja
def start():
    #jopa tämä alku voisi olla oma funktio edit_ui:ssa
    screen = Tk()
    screen.title("TkInter esimerkki")
    screen.geometry("800x900") #näytön koko
    screen.configure(bg="white")
    # tee tässä myös scrollattava ikkuna
    window = scrollable_screen(screen)

    # täällä kutsutaan eri framefunktioita

    assumption_view(window)

    screen.mainloop()
