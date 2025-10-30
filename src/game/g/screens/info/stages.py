# Stages module for the idle game
"""
Stages module for the idle game
"""

from src.game.g.screens.info.stagedata import stage_data


def get_stage(stage_name: str) -> dict | list:
    """
    Get the stage data
    """
    return stage_data[stage_name]


def get_locked_stages() -> list:
    """
    Get the locked stages
    """
    return stage_data["locked_stages"]


def get_unlocked_stages() -> list:
    """
    Get the unlocked stages
    """
    return stage_data["unlocked_stages"]


def get_completed_stages() -> list:
    """
    Get the completed stages
    """
    return stage_data["completed_stages"]
