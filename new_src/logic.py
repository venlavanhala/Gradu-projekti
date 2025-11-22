from interface.edit_ui import *
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

def check_combobox(combobox, right_answer):
    answer = combobox.get()
    if answer == right_answer or answer in right_answer:
        return True
    else:
        return False

def check_entry(entry, right_answer):
    answer = entry.get().replace(" ","").lower()
    if answer == right_answer or answer in right_answer:
        return True
    else:
        return False
    