# This is the initialization file for the sounds
"""
This is the initialization file for the sounds
"""
from src.assets.sounds.click import get_sound as get_click_sound
from src.assets.sounds.chime import get_sound as get_chime_sound
from src.assets.sounds.error import get_sound as get_error_sound
from src.assets.sounds.success import get_sound as get_success_sound
from src.assets.sounds.rebirth import get_sound as get_rebirth_sound
from src.assets.sounds.prestige import get_sound as get_prestige_sound

sound_all = {
    "click": get_click_sound,
    "chime": get_chime_sound,
    "error": get_error_sound,
    "success": get_success_sound,
    "rebirth": get_rebirth_sound,
    "prestige": get_prestige_sound,
}
__all__ = ["sound_all"]
