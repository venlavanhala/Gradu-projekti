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

# muotoilee tekstikentän
def format_text(textfield):
    text = textfield.get("1.0", "end-1c")
    lines = text.split('\n')
    height = min(max(len(lines), 1), 15)
    textfield.config(height=height+3, width=60, wrap="word", state=tk.DISABLED,)