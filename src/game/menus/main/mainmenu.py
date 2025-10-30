# Main menu module for the idle game
"""
Main menu module for the idle game
"""

import pygame
from pygame import Color, Surface
from pygame_menu import Menu, Theme
from src.game.menus.main.mmui.buttons import buttons
from src.game.menus.menumanager import get_mainmenu_assets_loaded, mainmenu_assets


def mainmenu() -> None:
    """
    The main menu of the idle game
    """
    # Check if the main menu assets have any value
    if get_mainmenu_assets_loaded() is not None:  # pylint: disable=R1705
        # If the main menu assets have no value, return to mainmenu_assets()
        return mainmenu_assets()
    elif get_mainmenu_assets_loaded() is False:
        # If the main menu assets have the value False, return to the mainmenu_assets()
        return mainmenu_assets()
    else:
        # If the main menu assets have the value True, continue
        pass
    surface: Surface = pygame.display.set_mode((800, 600))
    menu = Menu(
        title="Main Menu",
        width=800,
        height=600,
        theme=Theme(background_color=Color.BLACK),
    )
    for title, on_click in buttons():
        # Add the button from the buttons module to the menu
        menu.add.button(title, on_click, margin=(0, 10))
    menu.mainloop(surface)
    return mainmenu()
