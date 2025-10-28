from tkinter import Tk
from ui import UI

window = Tk()
window.title("TkInter esimerkki")

ui = UI(window)
ui.start()

window.mainloop()