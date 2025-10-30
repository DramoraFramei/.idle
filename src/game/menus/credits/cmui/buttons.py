# Buttons module for the credits menu
"""
Buttons module for the credits menu
"""

from collections.abc import Callable

from src.game.menus.menumanager import load_menu


def buttons() -> list[tuple[str, Callable[[], None]]]:
    """
    The buttons of the credits menu as (title, on_click) pairs.
    """
    return [
        ("Back", back_to_main_menu),
    ]


def back_to_main_menu() -> None:
    """
    The back to main menu function
    """
    load_menu("main")
    return None
