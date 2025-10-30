# Buttons module for the idle game
"""
Buttons module for the idle game
"""

import sys
import time
from collections.abc import Callable

import pygame

from src.assets.sounds import sound_all


def buttons() -> list[tuple[str, Callable[[], None], str]]:
    """
    The buttons of the main menu as (title, on_click, click_sound) pairs.
    """
    return [
        ("Play", on_click("click", play_game), "click"),
        ("Continue", on_click("click", continue_game), "click"),
        ("Settings", on_click("click", settings_game), "click"),
        ("Credits", on_click("click", credits_game), "click"),
        ("Quit", on_click("click", quit_game), "click"),
    ]


def play_game() -> None:
    """
    The play game function
    """
    print("Play game")
    # TODO: Implement the play game function # pylint: disable=W0511
    return None


def continue_game() -> None:
    """
    The continue game function
    """
    print("Continue game")
    # TODO: Implement the continue game function # pylint: disable=W0511


def settings_game() -> None:
    """
    The settings game function
    """
    print("Settings game")
    # TODO: Implement the settings game function # pylint: disable=W0511
    return None


def credits_game() -> None:
    """
    The credits game function
    """
    print("Credits game")
    # TODO: Implement the credits game function # pylint: disable=W0511
    return None


def quit_game() -> None:
    """
    The quit game function
    """
    print("Quit game")
    return sys.exit()


def title(title_text: str) -> Callable[[], str]:
    """
    The title function that returns the title text
    """
    return lambda: title_text


def on_click(sound_name: str, method: Callable[[], None]) -> Callable[[], None]:
    """
    The on_click function that calls the given method when the button is clicked
    This is the on_click function in pygame_menu that is used to play the given
    sound and then calls the given method when the sound has finished playing
    """
    return (
        lambda: play_sound(sound_name)
        + time.sleep(play_sound(sound_name).get_length())
        + method()
    )


def play_sound(sound_name: str) -> pygame.mixer.Sound:
    """
    The play sound function that returns the given sound
    """
    sound = sound_all[sound_name](sound_name)
    return sound


def stop_sound(sound: pygame.mixer.Sound) -> None:
    """
    The stop sound function that stops the given sound once it has finished playing
    """
    if sound.get_length() > 0:
        time.sleep(sound.get_length())
    sound.stop()
    return None
