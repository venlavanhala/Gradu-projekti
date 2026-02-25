from interface.edit_ui import *
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

# tarkista monivalintatehtävän vastaus
def check_combobox(answer, right_answer):
    if answer == right_answer or answer in right_answer:
        return True
    else:
        return False

# tarkista kirjoitustehtävän vastaus
def check_entry(answer, right_answer):
    if answer == right_answer or answer in right_answer:
        return True
    else:
        return False
    
# tarkista vastaus, jossa on monta kohtaa
def check_entries(answer_list, right_answers):
    if [a == b for a, b in zip(answer_list, right_answers)]==[True, True, True]:
        return True
    else:
       return [answer_list[i]==right_answers[i] for i in range(0, len(answer_list))]

