from tkinter import Tk, ttk

class UI:
    def __init__(self, root):
        self._root = root
        self._root.geometry("800x600")
        self._root.configure(bg="white") 

    def start(self):
	    label = ttk.Label(master=self._root, text="Hello world!")
	    button = ttk.Button(master=self._root, text="Button")
	    entry = ttk.Entry(master=self._root)
	    checkbutton = ttk.Checkbutton(master=self._root, text="Check button")
	    radiobutton = ttk.Radiobutton(master=self._root, text="Radio button")

	    label.pack()
	    button.pack()
	    entry.pack()
	    checkbutton.pack()
	    radiobutton.pack()


window = Tk()
window.title("TkInter esimerkki")

ui = UI(window)
ui.start()

window.mainloop()
