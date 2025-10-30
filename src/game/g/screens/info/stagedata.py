# Stage data module for the idle game
"""
Stage data module for the idle game
"""

from src.game.g.screens.info.gamedata import game_data_


def stage_data_() -> list:
    """
    Get the stage data
    """
    return stage_data_() == [
        game_data_([23]),
        game_data_([24]),
        game_data_([25]),
        game_data_([26]),
    ]


__all__ = [stage_data_()]
