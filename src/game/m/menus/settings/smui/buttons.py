# Buttons module for the settings menu
"""
Buttons module for the settings menu
"""

from collections.abc import Callable

from src.game.m.menus.menumanager import load_menu


def buttons() -> list[tuple[str, Callable[[], None]]]:
    """
    The buttons of the settings menu as (title, on_click) pairs.
    """
    return [
        ("master volume Toggle", master_volume_toggle),
        ("music volume Toggle", music_volume_toggle),
        ("sound effects volume Toggle", sound_effects_volume_toggle),
        ("fullscreen Toggle", fullscreen_toggle),
        ("windowed Toggle", windowed_toggle),
        ("vsync Toggle", vsync_toggle),
        ("fps limit Toggle", fps_limit_toggle),
        ("graphics quality Toggle", graphics_quality_toggle),
        ("graphics settings Toggle", graphics_settings_toggle),
        ("Back", back_to_main_menu),
    ]


def master_volume_toggle() -> None:
    """
    The master volume toggle function
    """
    print("Master volume toggle")
    return None


def music_volume_toggle() -> None:
    """
    The music volume toggle function
    """
    print("Music volume toggle")
    return None


def sound_effects_volume_toggle() -> None:
    """
    The sound effects volume toggle function
    """
    print("Sound effects volume toggle")
    return None


def fullscreen_toggle() -> None:
    """
    The fullscreen toggle function
    """
    print("Fullscreen toggle")
    return None


def windowed_toggle() -> None:
    """
    The windowed toggle function
    """
    print("Windowed toggle")
    return None


def vsync_toggle() -> None:
    """
    The vsync toggle function
    """
    print("Vsync toggle")
    return None


def fps_limit_toggle() -> None:
    """
    The fps limit toggle function
    """
    print("Fps limit toggle")
    return None


def graphics_quality_toggle() -> None:
    """
    The graphics quality toggle function
    """
    print("Graphics quality toggle")
    return None


def graphics_settings_toggle() -> None:
    """
    The graphics settings toggle function
    """
    print("Graphics settings toggle")
    return None


def back_to_main_menu() -> None:
    """
    The back to main menu function
    """
    load_menu("main")
    return None
