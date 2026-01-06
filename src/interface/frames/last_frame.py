import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from interface.edit_ui import *
from interface.frames.statement import *
from interface.ui_handler import *
from create_texts import end_texts

def end_view(screen):

    end_texts(screen)

    frame = new_frame(screen)

    return frame