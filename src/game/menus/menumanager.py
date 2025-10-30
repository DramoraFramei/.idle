# Menu manager module for the idle game
# This module is used to manage the loading, unloading, and switching between menus
"""
Menu manager module for the idle game
"""

import sys
import pygame
from src.game.menus.main.mmui.buttons import buttons as main_buttons
from src.game.menus.settings.smui.buttons import buttons as settings_buttons
from src.game.menus.main.mainmenu import mainmenu
from src.game.menus.saveload.saveloadmenu import saveloadmenu
from src.game.menus.saveload.slmui.buttons import buttons as saveload_buttons
from src.game.menus.settings.settingsmenu import settingsmenu
from src.game.menus.keybinds.keybindsmenu import keybindsmenu, keybinds
from src.game.menus.credits.creditsmenu import creditsmenu
from src.game.menus.credits.cmui.buttons import buttons as credits_buttons


def load_menu(
    menu: str,
) -> None | mainmenu | saveloadmenu | settingsmenu | creditsmenu | keybindsmenu:
    """
    The load menu function
    """
    if menu == "main":
        if get_mainmenu_assets_loaded() is not None:  # pylint: disable=R1705
            # If the main menu assets have no value, return to mainmenu_assets()
            return mainmenu_assets()
        elif get_mainmenu_assets_loaded() is False:
            # If the main menu assets have the value False, return to the mainmenu_assets()
            return mainmenu_assets()
        else:
            # If the main menu assets have the value True, continue
            return mainmenu()
    elif menu == "saveload":
        if get_saveloadmenu_assets_loaded() is not None:  # pylint: disable=R1705
            # If the save load menu assets have no value, return to saveloadmenu_assets()
            return saveloadmenu_assets()
        elif get_saveloadmenu_assets_loaded() is False:
            # If the save load menu assets have the value False, return to the saveloadmenu_assets()
            return saveloadmenu_assets()
        else:
            # If the save load menu assets have the value True, continue
            return saveloadmenu()
    elif menu == "settings":
        if get_settingsmenu_assets_loaded() is not None:  # pylint: disable=R1705
            # If the settings menu assets have no value, return to settingsmenu_assets()
            return settingsmenu_assets()
        elif get_settingsmenu_assets_loaded() is False:
            # If the settings menu assets have the value False, return to the settingsmenu_assets()
            return settingsmenu_assets()
        else:
            # If the settings menu assets have the value True, continue
            return settingsmenu()
    elif menu == "keybinds":
        if get_keybindsmenu_assets_loaded() is not None:  # pylint: disable=R1705
            # If the keybinds menu assets have no value, return to keybindsmenu_assets()
            return keybindsmenu_assets()
        elif get_keybindsmenu_assets_loaded() is False:
            # If the keybinds menu assets have the value False, return to the keybindsmenu_assets()
            return keybindsmenu_assets()
        else:
            # If the keybinds menu assets have the value True, continue
            return keybindsmenu()
    elif menu == "credits":
        if get_creditsmenu_assets_loaded() is not None:  # pylint: disable=R1705
            # If the credits menu assets have no value, return to creditsmenu_assets()
            return creditsmenu_assets()
        elif get_creditsmenu_assets_loaded() is False:
            # If the credits menu assets have the value False, return to the creditsmenu_assets()
            return creditsmenu_assets()
        else:
            # If the credits menu assets have the value True, continue
            return creditsmenu()
    else:
        raise ValueError(f"Invalid menu: {menu}")


def mainmenu_assets() -> None:
    """
    This function is used to ensure that the main menu assets are loaded
    """
    if (
        main_buttons() is None
    ):  # If the buttons are not loaded, return False and set the main menu assets to False
        return set_mainmenu_assets_loaded(False)
    else:  # If the buttons are loaded, set the main menu assets to True and return the mainmenu()
        set_mainmenu_assets_loaded(True)
    return load_menu("main")


def set_mainmenu_assets_loaded(value: bool) -> None:
    """
    This function is used to set the main menu assets loaded variable
    """
    return set_mainmenu_assets_loaded(value)


def get_mainmenu_assets_loaded() -> bool:
    """
    This function is used to get the main menu assets loaded variable
    """
    return get_mainmenu_assets_loaded()


def saveloadmenu_assets() -> None:
    """
    This function is used to ensure that the save load menu assets are loaded
    """
    if (
        saveload_buttons() is None
    ):  # If the buttons are not loaded, return False and set the save load menu assets to False
        return set_saveloadmenu_assets_loaded(False)
    else:  # If the buttons are loaded, set the save load menu assets to True and return True
        set_saveloadmenu_assets_loaded(True)
    return load_menu("saveload")


def set_saveloadmenu_assets_loaded(value: bool) -> None:
    """
    This function is used to set the save load menu assets loaded variable
    """
    return set_saveloadmenu_assets_loaded(value)


def get_saveloadmenu_assets_loaded() -> bool:
    """
    This function is used to get the save load menu assets loaded variable
    """
    return get_saveloadmenu_assets_loaded()


def settingsmenu_assets() -> None:
    """
    This function is used to ensure that the settings menu assets are loaded
    """
    if (
        settings_buttons() is None
    ):  # If the buttons are not loaded, return False and set the settings menu assets to False
        return set_settingsmenu_assets_loaded(False)
    else:  # If the buttons are loaded, set the settings menu assets to True and return True
        set_settingsmenu_assets_loaded(True)
    return load_menu("settings")


def set_settingsmenu_assets_loaded(value: bool) -> None:
    """
    This function is used to set the settings menu assets loaded variable
    """
    return set_settingsmenu_assets_loaded(value)


def get_settingsmenu_assets_loaded() -> bool:
    """
    This function is used to get the settings menu assets loaded variable
    """
    return get_settingsmenu_assets_loaded()


def creditsmenu_assets() -> None:
    """
    This function is used to ensure that the credits menu assets are loaded
    """
    if (
        credits_buttons() is None
    ):  # If the buttons are not loaded, return False and set the credits menu assets to False
        return set_creditsmenu_assets_loaded(False)
    else:  # If the buttons are loaded, set the credits menu assets to True and return True
        set_creditsmenu_assets_loaded(True)
    return load_menu("credits")


def keybindsmenu_assets() -> None:
    """
    This function is used to ensure that the keybinds menu assets are loaded
    """
    if (
        len(keybinds) == 0
    ):  # If the keybinds are empty, return False and set the keybinds menu assets to False
        return set_keybindsmenu_assets_loaded(False)
    else:  # If the keybinds are not empty, set the keybinds menu assets to True and return True
        set_keybindsmenu_assets_loaded(True)
    return load_menu("keybinds")


def set_keybindsmenu_assets_loaded(value: bool) -> None:
    """
    This function is used to set the keybinds menu assets loaded variable
    """
    return set_keybindsmenu_assets_loaded(value)


def get_keybindsmenu_assets_loaded() -> bool:
    """
    This function is used to get the keybinds menu assets loaded variable
    """
    return get_keybindsmenu_assets_loaded()


def set_creditsmenu_assets_loaded(value: bool) -> None:
    """
    This function is used to set the credits menu assets loaded variable
    """
    return set_creditsmenu_assets_loaded(value)


def get_creditsmenu_assets_loaded() -> bool:
    """
    This function is used to get the credits menu assets loaded variable
    """
    return get_creditsmenu_assets_loaded()


def get_current_menu() -> (
    None | mainmenu | saveloadmenu | settingsmenu | creditsmenu | keybindsmenu
):
    """
    This function is used to get the current menu
    """
    if pygame.display.get_focused() == mainmenu():
        return mainmenu()
    elif pygame.display.get_focused() == saveloadmenu():
        return saveloadmenu()
    elif pygame.display.get_focused() == settingsmenu():
        return settingsmenu()
    elif pygame.display.get_focused() == keybindsmenu():
        return keybindsmenu()
    elif pygame.display.get_focused() == creditsmenu():
        return creditsmenu()
    else:
        return None


def change_menu(
    current_menu: None
    | mainmenu
    | saveloadmenu
    | settingsmenu
    | creditsmenu
    | keybindsmenu,
    new_menu: str,
) -> str:
    """
    This function is used to change from one menu to another
    """
    if current_menu is None:
        return load_menu(new_menu)
    elif current_menu == load_menu(new_menu):
        return current_menu
    elif current_menu != load_menu(new_menu):
        return load_menu(new_menu)
    else:
        return None


def quit_game() -> None:
    """
    This function is used to quit the game
    """
    # If the current menu is the main menu and the quit button is clicked, quit the game
    if (
        pygame.display.get_focused() == mainmenu()
        and pygame.display.get_focused().get_title() == "Main Menu"
        and pygame.display.get_focused().get_title() == "Quit"
    ):
        pygame.display.quit()
        sys.exit()
