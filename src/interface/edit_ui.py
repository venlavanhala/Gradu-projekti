import tkinter as tk
from tkinter import ttk
import textfields
import tkinter.font as font

# tee näytöstä hiirellä scrollattava
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

    # väli ennen alkua
    spacer = tk.Frame(scrollable_frame, height=50, bg="white")
    spacer.pack(fill="x")

    return scrollable_frame


# muotoile tekstikentän muoto ja koko
def format_textfield_size(textfield):
    textfield.config(font=("Georgia", 12))
    text = textfield.get("1.0", "end-1c")
    lines = text.split('\n')
    lines = [len(line) for line in lines]
    height = text.count("\n\n")+max(lines)/60+len(lines)
    textfield.config(height=height, width=60, wrap="word", state=tk.DISABLED)

# muotoilee tekstikentän ja lisää tekstin
def format_textfield(screen, text, color="black"):
    textfield = tk.Text(
        master=screen,
        wrap="word",
        bg="white",
        fg=color,
        relief="flat",
        borderwidth=0,
        highlightthickness=0
    )
    textfield.insert("1.0", text)
    textfield.config(font=("Georgia", 12))
    format_textfield_size(textfield)
    textfield.pack(fill="x", expand=False, padx=60, pady=(0, 5))
    return textfield

# luo ja pakkaa uuden framen
def new_frame(screen):
    frame = tk.Frame(screen, bg="white", pady=0)
    frame.pack(fill="none", expand=False)
    return frame

# tämä funktio tekee uuden entryn, jonka yhteydessä voi olla edessä tai takana tekstiä
def new_entry(frame, left_text="", right_text=""):
    tk.Label(frame, text=left_text, bg="white").pack(side="left")
    pairless_field = tk.Entry(frame, width=20)
    pairless_field.pack(side="left",pady=5)
    tk.Label(frame, text=right_text, bg="white").pack(side="left")
    return pairless_field

# muotoilee kentän formattin_view tehtävälle ja palauttaa kolme entryä listassa
def create_formatting_entries(frame, chosen):
    if chosen == "2k+1":
        tk.Label(frame, text="4kn + 2k + 2n + 1 = 2 \u00B7 (", bg="white", font=("Georgia", 11)).pack(side="left")
        first = tk.Entry(frame, width=5, font=("Georgia", 11))
        first.pack(side="left",pady=5)
        tk.Label(frame, text="\u00B7 kn + ", bg="white", font=("Georgia", 11)).pack(side="left")
        second = tk.Entry(frame, width=5, font=("Georgia", 11))
        second.pack(side="left",pady=5)
        tk.Label(frame, text="\u00B7 k + ", bg="white", font=("Georgia", 11)).pack(side="left")
        third = tk.Entry(frame, width=5, font=("Georgia", 11))
        third.pack(side="left",pady=5)
        tk.Label(frame, text="\u00B7 n ) + 1", bg="white", font=("Georgia", 11)).pack(side="left")
        return [first, second, third]
    else:
        tk.Label(frame, text="4kn - 2k - 2n + 1 = 2 \u00B7 (", bg="white", font=("Georgia", 11)).pack(side="left")
        first = tk.Entry(frame, width=5, font=("Georgia", 11))
        first.pack(side="left",pady=5)
        tk.Label(frame, text="\u00B7 kn - ", bg="white", font=("Georgia", 11)).pack(side="left")
        second = tk.Entry(frame, width=5, font=("Georgia", 11))
        second.pack(side="left",pady=5)
        tk.Label(frame, text="\u00B7 k - ", bg="white", font=("Georgia", 11)).pack(side="left")
        third = tk.Entry(frame, width=5, font=("Georgia", 11))
        third.pack(side="left",pady=5)
        tk.Label(frame, text="\u00B7 n ) + 1", bg="white", font=("Georgia", 11)).pack(side="left")
        return [first, second, third]


# tekee uuden monivalintatehtävän
def new_combobox(frame, text):
    excercise = ttk.Combobox(
            frame,
            values=text,
            width=60,
            state="readonly",
            font=("Georgia", 11)
        )
    excercise.current(1)
    excercise.pack(pady=(0,5))
    return excercise

# luo labelin
def new_label(frame):
    label = tk.Label(frame, text="", font=("Georgia", 12), bg="white")
    label.pack(pady=5)
    return label

# piilottaa framen
def hide_frame(frame):
    frame.destroy()

# piilottaa napin
def hide_button(button):
    button.pack_forget()

# lisää tekstille tyyli
def setup_text_styles(text_widget):
    base_font = font.Font(text_widget, text_widget.cget("font"))

    bold_font = base_font.copy()
    bold_font.configure(weight="bold")

    text_widget.tag_configure("bold", font=bold_font)

# luo lihavoitu vaiheteksti
def bold_phase_text(screen, number):
    if number in [1,2]:
        text = format_textfield(screen, f"[Vaihe {number}]", "#6a0dad")
    elif number in [3,4]:
        text = format_textfield(screen, f"\n[Vaihe {number}]\n", "#6a0dad")
    else:
        text = format_textfield(screen, f"[Vaihe {number}]\n", "#6a0dad")
    setup_text_styles(text)
    text.tag_add("bold", "1.0", "end")
    return text

# poista lihavointi
def remove_bolding(text):
    text.tag_remove("bold", "1.0", "end")

# tekee popup-ikkunan
def popup_window(screen, text):
    popup = tk.Toplevel(screen)
    popup.title("Vihje")
    popup.geometry("500x120")

    tk.Label(popup, text=text).pack(pady=20)

    tk.Button(popup, text="Sulje", command=popup.destroy).pack(pady=5)

# luo näytölle palautteen oikeasta vastauksesta ja muokkaa napit seuraavaa näkymää varten
def show_combobox_right_answer(answer,feedback, screen, combobox, label, checkbutton, continue_button):
    label.config(text=feedback[answer], fg="green", font=("Georgia", 12))
    textfield = tk.Text(
    master=screen,
    font=("Arial", 12),
    wrap="word",
    bg="white",
    relief="flat",
    borderwidth=0,
    highlightthickness=0
    )
    textfield.insert("1.0", answer)
    format_textfield_size(textfield)
    textfield.pack(fill="x", expand=False, padx=60, pady=(0, 5))
    checkbutton.pack_forget()
    continue_button.pack()
    combobox.configure(state="disabled")
    return textfield

# luo näytölle palautteen väärästä vastauksesta
def show_combobox_wrong_answer(answer,feedback, label):
    label.config(text=feedback[answer], fg="blue")

# näyttää palautteen oikeasta vastauksesta pariton-tehtävässä ja muokkaa napit seuraavaa näkymää varten
def show_pairless_answer(answer, feedback, label, screen, checkbutton, continue_button):
    label.config(text=feedback[answer], fg="green", font=("Georgia", 12))
    textfield = tk.Text(
    master=screen,
    font=("Arial", 12),
    wrap="word",
    bg="white",
    relief="flat",
    borderwidth=0,
    highlightthickness=0
    )
    textfield.insert("1.0", "a="+answer+"  (k \u2208 \u2124)")
    format_textfield_size(textfield)
    textfield.pack(fill="x", expand=False,padx=60, pady=(0, 5))
    checkbutton.pack_forget()
    continue_button.pack()

# näyttää palautteen väärästä vastauksesta
def entry_wrong_answer(label):
    label.config(text="Yritä uudestaan!", fg="blue")

# näyttää palautteen väärästä vastauksesta muotoilu-tehtävässä
def format_wrong_answer(result, feedback_label):
    if result[0]==False:
        feedback_label.config(text=textfields.kirjoituspalautteet[0], fg="blue", font=("Georgia", 12))
    elif result[1]==False:
        feedback_label.config(text=textfields.kirjoituspalautteet[1], fg="blue", font=("Georgia", 12))
    elif result[2]==False:
        feedback_label.config(text=textfields.kirjoituspalautteet[2], fg="blue", font=("Georgia", 12))

# näyttää palautteen oikeasta vastauksesta muotoilu-tehtävässä ja muokkaa napit seuraavaa näkymää varten
def format_right_answer(label, screen, checkbutton, continue_button):
    label.config(text="Oikein!", fg="green", font=("Georgia", 12))
    textfield = tk.Text(
    master=screen,
    font=("Arial", 12),
    wrap="word",
    bg="white",
    relief="flat",
    borderwidth=0,
    highlightthickness=0
    )
    if textfields.valittu == "2k+1":
        textfield.insert("1.0", textfields.kirjoitusteksti)
    else:
        textfield.insert("1.0", textfields.kirjoitusteksti_)
    format_textfield_size(textfield)
    textfield.pack(fill="x", expand=False,padx=60, pady=(0, 5))
    checkbutton.pack_forget()
    continue_button.pack()

