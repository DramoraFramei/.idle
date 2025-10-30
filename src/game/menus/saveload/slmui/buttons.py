# Buttons module for the save load menu
"""
Buttons module for the save load menu
"""

from collections.abc import Callable

from src.game.menus.menumanager import load_menu


def buttons() -> list[tuple[str, Callable[[], None]]]:
    """
    The buttons of the save load menu as (title, on_click) pairs.
    """
    return [
        *dropdowns(),
        ("Back", back_to_main_menu),
    ]


def dropdowns() -> list[tuple[str, list[str], int, Callable[[int], None]]]:
    """
    The dropdown buttons of the save load menu as (title, options, default, onchange) pairs.
    """
    return [
        (
            "Save Slots",
            [f"Save Slot {i}" for i in range(10)],
            0,
            on_save_game_to_slot,
        ),
        (
            "Load Slots",
            [f"Load Slot {i}" for i in range(10)],
            0,
            on_load_game_from_slot,
        ),
    ]


def on_save_game_to_slot(slot: int) -> None:
    """
    The on save game to slot function
    """
    # When the user clicks the dropdown to save the game to a slot
    # Call the save game to slot function
    print(f"Saving game to slot: {slot}")
    return on_save_game_to_slot(slot)


def on_load_game_from_slot(slot: int) -> None:
    """
    The on load game from slot function
    """
    # When the user clicks the dropdown to load the game from a slot
    # Call the load game from slot function
    print(f"Loading game from slot: {slot}")
    return on_load_game_from_slot(slot)


def back_to_main_menu() -> None:
    """
    The back to main menu function
    """
    load_menu("main")
    return back_to_main_menu()
