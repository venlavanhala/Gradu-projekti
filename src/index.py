from tkinter import Tk
from interface import ui_handler

def main():
    root=Tk()
    screen = ui_handler.create_window(root)
    ui_handler.init(screen)
    
    # ensimmäinen näkymä
    ui_handler.start_assumption()

    root.mainloop()

if __name__ == "__main__":
    main()
