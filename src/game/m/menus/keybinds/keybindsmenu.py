# Keybinds menu module for the idle game
"""
Keybinds menu module for the idle game
"""

from collections.abc import Callable
import pygame
from pygame import Color, Surface
from pygame_menu import Menu, Theme

from src.game.m.menus.menumanager import (
    get_keybindsmenu_assets_loaded,
    keybindsmenu_assets,
    load_menu,
    set_keybindsmenu_assets_loaded,
)

keybinds = []


def keybindsmenu() -> None:
    """
    The keybinds menu of the idle game
    """
    # Check if the keybinds menu assets have any value
    if get_keybindsmenu_assets_loaded() is not None:  # pylint: disable=R1705
        # If the keybinds menu assets have no value, return to keybindsmenu_assets()
        return keybindsmenu_assets()
    elif get_keybindsmenu_assets_loaded() is False:
        # If the keybinds menu assets have the value False, return to the keybindsmenu_assets()
        return keybindsmenu_assets()
    else:
        # If the keybinds menu assets have the value True, continue
        pass
    surface: Surface = pygame.display.set_mode((800, 600))
    menu = Menu(
        title="Keybinds Menu",
        width=800,
        height=600,
        theme=Theme(background_color=Color.BLACK),
    )
    # For each keybind, add a button to the menu in addition to the back button
    for key, value in keybinds:
        menu.add.button(key, value, margin=(0, 10))
    menu.add.button("Back", back_to_main_menu, margin=(0, 10))
    menu.mainloop(surface)
    return keybindsmenu()


def add_keybind(key: str, value: Callable[[], None]) -> None:
    """
    The add keybind function to add a keybind to the buttons list and update the keybinds menu
    """
    keybinds.append((key, value))  # Add the keybind to the keybinds list
    set_keybindsmenu_assets_loaded(True)  # Update the keybinds menu assets
    return keybindsmenu()  # Return the keybinds menu


def back_to_main_menu() -> None:
    """
    The back to main menu function
    """
    return load_menu("main")
