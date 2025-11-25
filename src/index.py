from tkinter import Tk
from interface import ui_handler
from interface.edit_ui import *
from interface.ui_handler import *

def main():
    root=Tk()
    screen = ui_handler.create_window(root)
    # ensimmäinen näkymä
    ui_handler.init(screen)
    ui_handler.start_assumption()

    root.mainloop()

if __name__ == "__main__":
    main()