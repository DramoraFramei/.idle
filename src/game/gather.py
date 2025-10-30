# This file is for the gathering of resources
"""
This file is for the gathering of resources

Functions:
    - gather: The main gathering of resources
"""

import os
from src.assets.sounds import sound_all


def gather(sound: str) -> bool | None | str:
    # Check if there is a mp3 file in the assets/sounds folder
    """
    The gathering of the sound resources
    """
    if sound in sound_all:
        return sound_all[sound](sound)
    return None

def export(sound: str) -> bool | None | str:
    """
    The exporting of the sound resources
    """
    if sound in sound_all and os.path.exists(sound_all[sound](sound)):
        return sound_all[sound](sound)
    return None
