import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
import tkinter as tk
from tkinter import ttk
import textfields
from interface.edit_ui import *
import logic
from interface.frames.statement import *
from interface.ui_handler import *

def end_view(screen):

    end_texts(screen)

    frame = new_frame(screen)

    return frame