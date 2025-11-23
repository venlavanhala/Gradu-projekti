from interface.edit_ui import *
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

def check_combobox(answer, right_answer):
    if answer == right_answer or answer in right_answer:
        return True
    else:
        return False

def check_entry(answer, right_answer):
    if answer == right_answer or answer in right_answer:
        return True
    else:
        return False
    