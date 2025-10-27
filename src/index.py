from tkinter import Tk, ttk
import tkinter as tk

class UI:
    def __init__(self, root):
        self._root = root
        self._root.geometry("800x600")
        self._root.configure(bg="white") 

    def start(self):
        starting_text = "Todista: Kahden parittoman luvun tulo on pariton luku.\n\nEnsin täytyy löytää oletus ja väite, jota ollaan ratkaisemassa.\nOletus on jokin tieto, josta lähdetään liikkeelle ja jota voimme pitää tunnettuna."
        lines = starting_text.count('\n') + 1
        max_line_length = max(len(line) for line in starting_text.split('\n'))
        label = ttk.Label(master=self._root, text="Todistus")
        textfield = tk.Text(master=self._root, height=lines, width=max_line_length,borderwidth=0, highlightthickness=0,relief="flat", bg="white",font=("Arial", 12))
        textfield.insert("1.0",starting_text)
        textfield.config(state="disabled")
        button = ttk.Button(master=self._root, text="Button")
        entry = ttk.Entry(master=self._root)
        checkbutton = ttk.Checkbutton(master=self._root, text="Check button")

        label.pack(pady=(20,20))
        textfield.pack(padx=60, pady=(0,20))
        button.pack(pady=(0,20))
        entry.pack(pady=(0,20))
        checkbutton.pack(pady=(0,20))

window = Tk()
window.title("TkInter esimerkki")

ui = UI(window)
ui.start()

window.mainloop()
