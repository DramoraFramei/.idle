# Settings menu module for the idle game
"""
Settings menu module for the idle game
"""

import pygame
from pygame import Color, Surface
from pygame_menu import Menu, Theme

from src.game.menus.settings.smui.buttons import buttons
from src.game.menus.menumanager import (
    get_settingsmenu_assets_loaded,
    settingsmenu_assets,
)


def settingsmenu() -> None:
    """
    The settings menu of the idle game
    """
    # Check if the settings menu assets have any value
    if get_settingsmenu_assets_loaded() is not None:  # pylint: disable=R1705
        # If the settings menu assets have no value, return to settingsmenu_assets()
        return settingsmenu_assets()
    elif get_settingsmenu_assets_loaded() is False:
        # If the settings menu assets have the value False, return to the settingsmenu_assets()
        return settingsmenu_assets()
    else:
        # If the settings menu assets have the value True, continue
        pass
    surface: Surface = pygame.display.set_mode((800, 600))
    menu = Menu(
        title="Settings Menu",
        width=800,
        height=600,
        theme=Theme(background_color=Color.BLACK),
    )
    for title, on_click in buttons():
        # Add the button from the buttons module to the menu
        menu.add.button(title, on_click, margin=(0, 10))
    menu.mainloop(surface)
    return settingsmenu()
