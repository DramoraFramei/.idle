# Save manager module for the idle game
# This module is used to create, load, and save the player's progress to the save slots
"""
Save manager module for the idle game
"""

import json
import os
from src.game.m.menus.saveload.slmui.buttons import (
    on_save_game_to_slot,
    on_load_game_from_slot,
)


# Get the save slot that is currently selected
def on_get_selected_save_slot(value: int) -> int:
    """
    The get selected save slot function
    """
    # Get the selected save slot from the dropdown
    on_save_game_to_slot(value)
    print(f"Selected save slot: {value}")
    return value


def on_get_selected_load_slot(value: int) -> int:
    """
    The get selected load slot function
    """
    # Get the selected load slot from the dropdown
    on_load_game_from_slot(value)
    print(f"Selected load slot: {value}")
    return value


# Load the game from the slot
def load_game_from_slot(slot: int) -> bool:
    """
    The load game from slot function
    """
    # Check if the slot has any files
    if not os.path.exists(f"save_slot_{slot}.json"):
        return print(f"Slot {slot} is empty")
    else:
        # Load the game from the slot
        with open(f"save_slot_{slot}.json", "r", encoding="utf-8") as file:
            print(f"Loading game from slot: {slot}")
            json.load(file)
            return print(f"Game loaded from slot: {slot}")


# Check if the slot is empty
def is_slot_empty(slot: int) -> bool:
    """
    The is slot empty function
    """
    # If the slot does not contain any files return True
    if not os.path.exists(f"save_slot_{slot}.json"):
        return True
    else:
        return False


# Get the player progress data
def get_player_progress_data() -> dict:
    """
    The get player progress data function
    """
    return {}


# Create a new save file for the slot
def create_new_save_file(slot: int) -> bool:
    """
    The create new save file function
    """
    # Create a new save file for the slot
    with open(f"save_slot_{slot}.json", "w", encoding="utf-8") as file:
        json.dump(get_player_progress_data(), file)
    return print(f"New save file created for slot: {slot}")


def save_game_to_slot(slot: int) -> bool:
    """
    The save game to slot function
    """
    # Save the game to the slot
    if create_new_save_file(slot):
        return print(f"Game saved to slot: {slot}")
    else:
        return print(f"Failed to save game to slot: {slot}")
