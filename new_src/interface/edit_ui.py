import tkinter as tk
from tkinter import ttk
import logic

# tekee näytöstä scrollattavan

def scrollable_screen(root):
    canvas = tk.Canvas(root, bg="white", highlightthickness=0)
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="white")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    def _on_mousewheel(event):
        if event.num == 5 or event.delta < 0:
            canvas.yview_scroll(1, "units")
        elif event.num == 4 or event.delta > 0:
            canvas.yview_scroll(-1, "units")

    canvas.bind_all("<MouseWheel>", _on_mousewheel)
    canvas.bind_all("<Button-4>", _on_mousewheel)
    canvas.bind_all("<Button-5>", _on_mousewheel)

    return scrollable_frame


# muotoilee tekstikentän muodon ja koon
def format_textfield_size(textfield):
    text = textfield.get("1.0", "end-1c")
    lines = text.split('\n')
    lines = [len(line) for line in lines]
    height = text.count("\n\n")+max(lines)/60+len(lines) # tyhjät rivit + rivit + pisin rivi/leveys
    # lasketaan näkyvien rivien määrä
    textfield.config(height=height, width=60, wrap="word", state=tk.DISABLED,font=("Georgia", 12))

# korkeus = \n määrä + pisin/12

# muotoilee tekstikentän ja lisää tekstin
def format_textfield(screen, text, backround_color="black"):
    textfield = tk.Text(
        master=screen,
        wrap="word",
        bg="white",
        fg=backround_color,
        relief="flat",
        borderwidth=0,
        highlightthickness=0
    )
    textfield.insert("1.0", text)
    format_textfield_size(textfield)
    textfield.pack(fill="x", expand=False, padx=60, pady=(0, 5))

# vaihda labelin vanha frame uuteen
def move_label(label, frame):
    label.pack_forget()
    label.pack(in_=frame, pady=5)

# tekee ja pakkaa uuden framen
def new_frame(screen):
    tk.Frame(screen, bg="white", pady=0)
    screen.pack()

# tekee uuden monivalintatehtävän
def new_combobox(frame, text):
    excercise = ttk.Combobox(
            frame,
            values=text,
            width=50,
            state="readonly",
            font=("Georgia", 11)
        )
    excercise.current(1)
    excercise.pack(pady=(0,5))
    return excercise

def new_label(frame):
    label = tk.Label(text="", font=("Georgia", 12), bg="white")
    label.pack(pady=5)

def jatka_nappi(screeni, frame, seuraava_frame,teksti):
    button = ttk.Button(frame, text="Jatka", command=lambda: (jatka(screeni,frame,teksti), seuraava_frame.pack()))
    button.pack(pady=(5, 10))

# piilotetaan edellinen näyttö ja näytetään seuraava teksti
def jatka(naytto, screen, teksti):
    screen.pack_forget()
    format_textfield(naytto, teksti)

def popup_window(screen, text):
    popup = tk.Toplevel(screen)
    popup.title("Vihje")
    popup.geometry("500x120")

    tk.Label(popup, text=text).pack(pady=20)

    tk.Button(popup, text="Sulje", command=popup.destroy).pack(pady=5)

# oikea vastaus 
def render_combobox_right_answer(answer,feedback, frame, combobox, label, checkbutton, button):
    label.config(text=feedback[answer], fg="green", font=("Arial", 12))
    textfield = tk.Text(
    master=frame,
    font=("Arial", 12),
    wrap="word",
    bg="white",
    relief="flat",
    borderwidth=0,
    highlightthickness=0
    )
    textfield.insert("1.0", answer)
    format_textfield_size(textfield)
    textfield.pack(fill="x", expand=False,padx=60, pady=(0, 5))
    combobox.configure(state="disabled")
    checkbutton.pack_forget()
    button.pack()

def combobox_wrong_answer(answer,feedback, label):
    label.config(text=feedback[answer], fg="blue")

def forget(widget):
        widget.pack_forget()
    
def entry_right_answer(answer, right_answer, feedback, label, frame, checkbutton, button, combobox):
    label.config(text=feedback[answer], fg="green", font=("Arial", 12))
    textfield = tk.Text(
    master=frame,
    font=("Arial", 12),
    wrap="word",
    bg="white",
    relief="flat",
    borderwidth=0,
    highlightthickness=0
    )
    if answer in ["2k-1","2k+1"]:
        textfield.insert("1.0", "a="+answer+"  (k \u2208 \u2124)")
    else:
        textfield.insert("1.0", answer)
    format_textfield_size(textfield)
    textfield.pack(fill="x", expand=False,padx=60, pady=(0, 5))
    checkbutton.pack_forget()
    button.pack()

def entry_wrong_answer(label):
    label.config(text="Yritä uudestaan!", fg="blue")

def check_button(frame):
    if result == True:
        render_combobox_right_answer()
    else:
        combobox_wrong_answer()
    feedback_label = new_label(frame)
    check_assumption_answer = ttk.Button(
        frame,
        text="Tarkista",
        command=lambda: (
        move_label(feedback_label, frame),
        check_combobox(screen, choose_assumption, textfields.oletusvastaus,
                       feedback_label, textfields.oletukset, continue_button1,
                       check_assumption_answer))
    )

    check_assumption_answer.pack(pady=5)