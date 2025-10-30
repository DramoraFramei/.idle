# Save load menu module for the idle game
"""
Save load menu module for the idle game
"""

import pygame
from pygame import Color, Surface
from pygame_menu import Menu, Theme

from src.game.m.menus.saveload.slmui.buttons import buttons
from src.game.m.menus.menumanager import (
    get_saveloadmenu_assets_loaded,
    saveloadmenu_assets,
)


def saveloadmenu() -> None:
    """
    The save load menu of the idle game
    """
    # Check if the save load menu assets have any value
    if get_saveloadmenu_assets_loaded() is not None:  # pylint: disable=R1705
        # If the save load menu assets have no value, return to saveloadmenu_assets()
        return saveloadmenu_assets()
    elif get_saveloadmenu_assets_loaded() is False:
        # If the save load menu assets have the value False, return to the saveloadmenu_assets()
        return saveloadmenu_assets()
    else:
        # If the save load menu assets have the value True, continue
        pass
    surface: Surface = pygame.display.set_mode((800, 600))
    menu = Menu(
        title="Save Load Menu",
        width=800,
        height=600,
        theme=Theme(background_color=Color.BLACK),
    )
    for title, on_click in buttons():
        # Add the button from the buttons module to the menu
        menu.add.button(title, on_click, margin=(0, 10))
    menu.mainloop(surface)
    return saveloadmenu()
