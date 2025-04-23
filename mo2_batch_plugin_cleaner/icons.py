# Created by GoriRed
# Version: 1.0
# License: CC-BY-NC
# https://github.com/tkoopman/
#
# Vectors and icons by https://www.svgrepo.com
 
from pathlib import Path
from PyQt6.QtGui import QIcon

def icon(name: str) -> QIcon:
    """
    Returns the icon for the given name.
    """
    return QIcon(str(Path(__file__).parent / "icons" / name))

CLEAN_STATE_UNKNOWN = icon("confused-face-svgrepo-com.svg")
CLEAN_STATE_CLEAN = icon("emotion-happy-svgrepo-com.svg")
CLEAN_STATE_DIRTY = icon("emotion-unhappy-svgrepo-com.svg")
CLEAN_STATE_MANUAL = icon("disappointed-face-svgrepo-com.svg")