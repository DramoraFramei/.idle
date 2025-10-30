# Error sound module for the idle game
"""
Error sound module for the idle game
"""
def get_sound(sound_name: str) -> str:
    """
    Get sound file path for the given sound name
    """
    if sound_name == "error":
        return "sounds/sound_effects/error.mp3"
    return "sounds/sound_effects/error.mp3"
