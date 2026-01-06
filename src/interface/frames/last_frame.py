import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from interface.edit_ui import *
from interface.frames.statement import *
from interface.ui_handler import *
from create_texts import end_texts

# luo viimeisen näkymän
def end_view(screen):

    # luo tekstit
    bold_phase_text(screen, "6")
    end_texts(screen)

    # luo uuden framen tehtävälle
    frame = new_frame(screen)

    return frame