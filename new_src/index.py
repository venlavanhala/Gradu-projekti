from tkinter import Tk
from interface import ui
from interface.edit_ui import *
from interface.ui import *

def main():
    root=Tk()
    screen = ui.create_window(root)
    # ensimmäinen näkymä
    ui.init(screen)
    ui.start_assumption()

    root.mainloop()

if __name__ == "__main__":
    main()