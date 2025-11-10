import tkinter as tk

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

    return scrollable_frame

# muotoilee tekstikentän muodon
def format_text(textfield):
    text = textfield.get("1.0", "end-1c")
    lines = text.split('\n')
    lines = [len(line) for line in lines]
    height = text.count("\n\n")+max(lines)/60+len(lines) # tyhjät rivit + rivit + pisin rivi/leveys
    textfield.config(height=height, width=60, wrap="word", state=tk.DISABLED,font=("Georgia", 12))

# korkeus = \n määrä + pisin/12

# muotoilee tekstikentän ja lisää tekstin
def format_textfield(screen, text):
    textfield = tk.Text(
        master=screen,
        font=("Georgia", 12),
        wrap="word",
        bg="white",
        relief="flat",
        borderwidth=0,
        highlightthickness=0
    )
    textfield.insert("1.0", text)
    format_text(textfield)
    textfield.pack(fill="x", expand=False, padx=60, pady=(0, 5))

