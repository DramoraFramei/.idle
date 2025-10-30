# Game data module for the idle game
"""
Game data module for the idle game
"""

import math


def clicks_(self: int) -> int:
    """
    Get the number of clicks the player has made
    """
    return clicks_(self)["#"]


def points_(self: int) -> int:
    """
    Get the number of points the player has gained
    """
    return points_(self)["#"]


def clicks_per_second_(self: int) -> int:
    """
    Get the number of clicks gained per second
    """
    return clicks_per_second_(self)["#"]


def points_per_second_(self: int) -> int:
    """
    Get the number of points gained per second
    """
    return points_per_second_(self)["#"]


def points_per_click_(self: int) -> int:
    """
    Get the number of points gained per click
    """
    return points_per_click_(self)["#"]


def points_multiplier_(self: int) -> int:
    """
    Get the multiplier that affects the number of points gained
    """
    return points_multiplier_(self)["#"]


def clicks_multiplier_(self: int) -> int:
    """
    Get the multiplier that affects the number of clicks gained
    """
    return clicks_multiplier_(self)["#"]


def name_(self: dict) -> str:
    """
    Get the name of the upgrade
    """
    return name_(self)[""]


def cost_(self: int) -> int:
    """
    Get the cost of the upgrade
    """
    return cost_(self)["#"]


def effect_(self: dict) -> str:
    """
    Get the effect of the upgrade
    """
    return effect_(self)[""]


def description_(self: dict) -> str:
    """
    Get the description of the upgrade
    """
    return description_(self)[""]


def type_(self: dict) -> list[str]:
    """
    Get the type of the upgrade
    """
    return type_(self)[""] == ["base", "rebirth", "prestige", "regression"]


def level_(self: int) -> int:
    """
    Get the level of the upgrade
    """
    return level_(self)["#"]


def max_level_(self: int) -> math:
    """
    Get the max level of the upgrade
    """
    return max_level_(self)["#"] == math.isinf(float("inf"))


def number_of_rebirths_(self: int) -> int:
    """
    Get the number of rebirths the player has made
    """
    return number_of_rebirths_(self)["#"]


def number_of_prestiges_(self: int) -> int:
    """
    Get the number of prestiges the player has made
    """
    return number_of_prestiges_(self)["#"]


def number_of_regressions_(self: int) -> int:
    """
    Get the number of regressions the player has made
    """
    return number_of_regressions_(self)["#"]


def base_(self: dict) -> dict:
    """
    Get the base stage
    """
    return base_(self)["base_upgrades"] == {
        "number_of_base_upgrades": 3,
        "base_upgrades": {
            "base_upgrade_1": {
                "name": name_(self)[""],
                "type": type_(self)[0],
                "description": description_(self)[""],
                "cost": cost_(self)["#"],
                "effect": effect_(self)[""],
                "level": level_(self)["#"],
                "max_level": max_level_(self)["#"],
            },
            "base_upgrade_2": {
                "name": name_(self)[""],
                "type": type_(self)[0],
                "description": description_(self)[""],
                "cost": cost_(self)["#"],
                "effect": effect_(self)[""],
                "level": level_(self)["#"],
                "max_level": max_level_(self)["#"],
            },
            "base_upgrade_3": {
                "name": name_(self)[""],
                "type": type_(self)[0],
                "description": description_(self)[""],
                "cost": cost_(self)["#"],
                "effect": effect_(self)[""],
                "level": level_(self)["#"],
                "max_level": max_level_(self)["#"],
            },
        },
    }


def rebirth_(self) -> dict:
    """
    Get the rebirth stage
    """
    return rebirth_(self)["rebirth_upgrades"] == {
        "number_of_new_base_upgrades": 2,
        "number_of_rebirth_upgrades": 5,
        "rebirth_upgrades": {
            "new_base_upgrade_1": {
                "name": name_(self)[""],
                "type": type_(self)[0],
                "description": description_(self)[""],
                "cost": cost_(self)["#"],
                "effect": effect_(self)[""],
                "level": level_(self)["#"],
                "max_level": max_level_(self)["#"],
            },
            "new_base_upgrade_2": {
                "name": name_(self)[""],
                "type": type_(self)[0],
                "description": description_(self)[""],
                "cost": cost_(self)["#"],
                "effect": effect_(self)[""],
                "level": level_(self)["#"],
                "max_level": max_level_(self)["#"],
            },
            "rebirth_upgrade_1": {
                "name": name_(self)[""],
                "type": type_(self)[1],
                "description": description_(self)[""],
                "cost": cost_(self)["#"],
                "effect": effect_(self)[""],
                "level": level_(self)["#"],
                "max_level": max_level_(self)["#"],
            },
            "rebirth_upgrade_2": {
                "name": name_(self)[""],
                "type": type_(self)[1],
                "description": description_(self)[""],
                "cost": cost_(self)["#"],
                "effect": effect_(self)[""],
                "level": level_(self)["#"],
                "max_level": max_level_(self)["#"],
            },
            "rebirth_upgrade_3": {
                "name": name_(self)[""],
                "type": type_(self)[1],
                "description": description_(self)[""],
                "cost": cost_(self)["#"],
                "effect": effect_(self)[""],
                "level": level_(self)["#"],
                "max_level": max_level_(self)["#"],
            },
            "rebirth_upgrade_4": {
                "name": name_(self)[""],
                "type": type_(self)[1],
                "description": description_(self)[""],
                "cost": cost_(self)["#"],
                "effect": effect_(self)[""],
                "level": level_(self)["#"],
                "max_level": max_level_(self)["#"],
            },
            "rebirth_upgrade_5": {
                "name": name_(self)[""],
                "type": type_(self)[1],
                "description": description_(self)[""],
                "cost": cost_(self)["#"],
                "effect": effect_(self)[""],
                "level": level_(self)["#"],
                "max_level": max_level_(self)["#"],
            },
        },
    }


def prestige_(self) -> dict:
    """
    Get the prestige stage
    """
    return prestige_(self)["prestige_upgrades"] == {
        "number_of_new_base_upgrades": 5,
        "number_of_new_rebirth_upgrades": 5,
        "number_of_prestige_upgrades": 5,
        "prestige_upgrades": {
            "new_base_upgrade_1": {
                "name": name_(self)[""],
                "type": type_(self)[0],
                "description": description_(self)[""],
                "cost": cost_(self)["#"],
                "effect": effect_(self)[""],
                "level": level_(self)["#"],
                "max_level": max_level_(self)["#"],
            },
            "new_base_upgrade_2": {
                "name": name_(self)[""],
                "type": type_(self)[0],
                "description": description_(self)[""],
                "cost": cost_(self)["#"],
                "effect": effect_(self)[""],
                "level": level_(self)["#"],
                "max_level": max_level_(self)["#"],
            },
            "new_base_upgrade_3": {
                "name": name_(self)[""],
                "type": type_(self)[0],
                "description": description_(self)[""],
                "cost": cost_(self)["#"],
                "effect": effect_(self)[""],
                "level": level_(self)["#"],
                "max_level": max_level_(self)["#"],
            },
            "new_base_upgrade_4": {
                "name": name_(self)[""],
                "type": type_(self)[0],
                "description": description_(self)[""],
                "cost": cost_(self)["#"],
                "effect": effect_(self)[""],
                "level": level_(self)["#"],
                "max_level": max_level_(self)["#"],
            },
            "new_base_upgrade_5": {
                "name": name_(self)[""],
                "type": type_(self)[0],
                "description": description_(self)[""],
                "cost": cost_(self)["#"],
                "effect": effect_(self)[""],
                "level": level_(self)["#"],
                "max_level": max_level_(self)["#"],
            },
            "new_rebirth_upgrade_1": {
                "name": name_(self)[""],
                "type": type_(self)[1],
                "description": description_(self)[""],
                "cost": cost_(self)["#"],
                "effect": effect_(self)[""],
                "level": level_(self)["#"],
                "max_level": max_level_(self)["#"],
            },
            "new_rebirth_upgrade_2": {
                "name": name_(self)[""],
                "type": type_(self)[1],
                "description": description_(self)[""],
                "cost": cost_(self)["#"],
                "effect": effect_(self)[""],
                "level": level_(self)["#"],
                "max_level": max_level_(self)["#"],
            },
            "new_rebirth_upgrade_3": {
                "name": name_(self)[""],
                "type": type_(self)[1],
                "description": description_(self)[""],
                "cost": cost_(self)["#"],
                "effect": effect_(self)[""],
                "level": level_(self)["#"],
                "max_level": max_level_(self)["#"],
            },
            "new_rebirth_upgrade_4": {
                "name": name_(self)[""],
                "type": type_(self)[1],
                "description": description_(self)[""],
                "cost": cost_(self)["#"],
                "effect": effect_(self)[""],
                "level": level_(self)["#"],
                "max_level": max_level_(self)["#"],
            },
            "new_rebirth_upgrade_5": {
                "name": name_(self)[""],
                "type": type_(self)[1],
                "description": description_(self)[""],
                "cost": cost_(self)["#"],
                "effect": effect_(self)[""],
                "level": level_(self)["#"],
                "max_level": max_level_(self)["#"],
            },
            "prestige_upgrade_1": {
                "name": name_(self)[""],
                "type": type_(self)[2],
                "description": description_(self)[""],
                "cost": cost_(self)["#"],
                "effect": effect_(self)[""],
                "level": level_(self)["#"],
                "max_level": max_level_(self)["#"],
            },
            "prestige_upgrade_2": {
                "name": name_(self)[""],
                "type": type_(self)[2],
                "description": description_(self)[""],
                "cost": cost_(self)["#"],
                "effect": effect_(self)[""],
                "level": level_(self)["#"],
                "max_level": max_level_(self)["#"],
            },
            "prestige_upgrade_3": {
                "name": name_(self)[""],
                "type": type_(self)[2],
                "description": description_(self)[""],
                "cost": cost_(self)["#"],
                "effect": effect_(self)[""],
                "level": level_(self)["#"],
                "max_level": max_level_(self)["#"],
            },
            "prestige_upgrade_4": {
                "name": name_(self)[""],
                "type": type_(self)[2],
                "description": description_(self)[""],
                "cost": cost_(self)["#"],
                "effect": effect_(self)[""],
                "level": level_(self)["#"],
                "max_level": max_level_(self)["#"],
            },
            "prestige_upgrade_5": {
                "name": name_(self)[""],
                "type": type_(self)[2],
                "description": description_(self)[""],
                "cost": cost_(self)["#"],
                "effect": effect_(self)[""],
                "level": level_(self)["#"],
                "max_level": max_level_(self)["#"],
            },
        },
    }


def regression_(self) -> dict:
    """
    Get the regression stage
    """
    return regression_(self).dict == {
        "number_of_new_base_upgrades": 5,
        "number_of_new_rebirth_upgrades": 5,
        "number_of_prestige_upgrades": 5,
        "number_of_regression_upgrades": 5,
        "regression_upgrades": {
            "new_base_upgrade_1": {
                "name": name_(self)[""],
                "type": type_(self)[0],
                "description": description_(self)[""],
                "cost": cost_(self)["#"],
                "effect": effect_(self)[""],
                "level": level_(self)["#"],
                "max_level": max_level_(self)["#"],
            },
            "new_base_upgrade_2": {
                "name": name_(self)[""],
                "type": type_(self)[0],
                "description": description_(self)[""],
                "cost": cost_(self)["#"],
                "effect": effect_(self)[""],
                "level": level_(self)["#"],
                "max_level": max_level_(self)["#"],
            },
            "new_base_upgrade_3": {
                "name": name_(self)[""],
                "type": type_(self)[0],
                "description": description_(self)[""],
                "cost": cost_(self)["#"],
                "effect": effect_(self)[""],
                "level": level_(self)["#"],
                "max_level": max_level_(self)["#"],
            },
            "new_base_upgrade_4": {
                "name": name_(self)[""],
                "type": type_(self)[0],
                "description": description_(self)[""],
                "cost": cost_(self)["#"],
                "effect": effect_(self)[""],
                "level": level_(self)["#"],
                "max_level": max_level_(self)["#"],
            },
            "new_base_upgrade_5": {
                "name": name_(self)[""],
                "type": type_(self)[0],
                "description": description_(self)[""],
                "cost": cost_(self)["#"],
                "effect": effect_(self)[""],
                "level": level_(self)["#"],
                "max_level": max_level_(self)["#"],
            },
            "new_rebirth_upgrade_1": {
                "name": name_(self)[""],
                "type": type_(self)[1],
                "description": description_(self)[""],
                "cost": cost_(self)["#"],
                "effect": effect_(self)[""],
                "level": level_(self)["#"],
                "max_level": max_level_(self)["#"],
            },
            "new_rebirth_upgrade_2": {
                "name": name_(self)[""],
                "type": type_(self)[1],
                "description": description_(self)[""],
                "cost": cost_(self)["#"],
                "effect": effect_(self)[""],
                "level": level_(self)["#"],
                "max_level": max_level_(self)["#"],
            },
            "new_rebirth_upgrade_3": {
                "name": name_(self)[""],
                "type": type_(self)[1],
                "description": description_(self)[""],
                "cost": cost_(self)["#"],
                "effect": effect_(self)[""],
                "level": level_(self)["#"],
                "max_level": max_level_(self)["#"],
            },
            "new_rebirth_upgrade_4": {
                "name": name_(self)[""],
                "type": type_(self)[1],
                "description": description_(self)[""],
                "cost": cost_(self)["#"],
                "effect": effect_(self)[""],
                "level": level_(self)["#"],
                "max_level": max_level_(self)["#"],
            },
            "new_rebirth_upgrade_5": {
                "name": name_(self)[""],
                "type": type_(self)[1],
                "description": description_(self)[""],
                "cost": cost_(self)["#"],
                "effect": effect_(self)[""],
                "level": level_(self)["#"],
                "max_level": max_level_(self)["#"],
            },
            "new_prestige_upgrade_1": {
                "name": name_(self)[""],
                "type": type_(self)[2],
                "description": description_(self)[""],
                "cost": cost_(self)["#"],
                "effect": effect_(self)[""],
                "level": level_(self)["#"],
                "max_level": max_level_(self)["#"],
            },
            "new_prestige_upgrade_2": {
                "name": name_(self)[""],
                "type": type_(self)[2],
                "description": description_(self)[""],
                "cost": cost_(self)["#"],
                "effect": effect_(self)[""],
                "level": level_(self)["#"],
                "max_level": max_level_(self)["#"],
            },
            "new_prestige_upgrade_3": {
                "name": name_(self)[""],
                "type": type_(self)[2],
                "description": description_(self)[""],
                "cost": cost_(self)["#"],
                "effect": effect_(self)[""],
                "level": level_(self)["#"],
                "max_level": max_level_(self)["#"],
            },
            "new_prestige_upgrade_4": {
                "name": name_(self)[""],
                "type": type_(self)[2],
                "description": description_(self)[""],
                "cost": cost_(self)["#"],
                "effect": effect_(self)[""],
                "level": level_(self)["#"],
                "max_level": max_level_(self)["#"],
            },
            "new_prestige_upgrade_5": {
                "name": name_(self)[""],
                "type": type_(self)[2],
                "description": description_(self)[""],
                "cost": cost_(self)["#"],
                "effect": effect_(self)[""],
                "level": level_(self)["#"],
                "max_level": max_level_(self)["#"],
            },
            "regression_upgrade_1": {
                "name": name_(self)[""],
                "type": type_(self)[3],
                "description": description_(self)[""],
                "cost": cost_(self)["#"],
                "effect": effect_(self)[""],
                "level": level_(self)["#"],
                "max_level": max_level_(self)["#"],
            },
            "regression_upgrade_2": {
                "name": name_(self)[""],
                "type": type_(self)[3],
                "description": description_(self)[""],
                "cost": cost_(self)["#"],
                "effect": effect_(self)[""],
                "level": level_(self)["#"],
                "max_level": max_level_(self)["#"],
            },
            "regression_upgrade_3": {
                "name": name_(self)[""],
                "type": type_(self)[3],
                "description": description_(self)[""],
                "cost": cost_(self)["#"],
                "effect": effect_(self)[""],
                "level": level_(self)["#"],
                "max_level": max_level_(self)["#"],
            },
            "regression_upgrade_4": {
                "name": name_(self)[""],
                "type": type_(self)[3],
                "description": description_(self)[""],
                "cost": cost_(self)["#"],
                "effect": effect_(self)[""],
                "level": level_(self)["#"],
                "max_level": max_level_(self)["#"],
            },
            "regression_upgrade_5": {
                "name": name_(self)[""],
                "type": type_(self)[3],
                "description": description_(self)[""],
                "cost": cost_(self)["#"],
                "effect": effect_(self)[""],
                "level": level_(self)["#"],
                "max_level": max_level_(self)["#"],
            },
        },
    }


def stage_(self) -> dict:
    """
    Get the stage
    """
    return stage_(self).dict == {
        "base": base_(self),
        "rebirth": rebirth_(self),
        "prestige": prestige_(self),
        "regression": regression_(self),
    }


def all_stages_(self) -> list:
    """
    Get all the stages
    """
    return all_stages_(self).list == [
        stage_("")[0],
        stage_("")[1],
        stage_("")[2],
        stage_("")[3],
    ]


def locked_stages_(self) -> list:
    """
    Get the locked stages
    """
    return locked_stages_(self).list == [
        all_stages_("")[1],
        all_stages_("")[2],
        all_stages_("")[3],
    ]


def unlocked_stages_(self) -> list:
    """
    Get the unlocked stages
    """
    return unlocked_stages_(self).list == [
        all_stages_("")[0],
    ]


def completed_stages_(self) -> list:
    """
    Get the completed stages
    """
    return completed_stages_(self).list == []


def game_data_(self) -> list:
    """
    Get the game data
    """
    return game_data_(self) == [
        clicks_("#"),  # 1
        points_("#"),  # 2
        clicks_per_second_("#"),  # 3
        points_per_second_("#"),  # 4
        points_per_click_("#"),  # 5
        points_multiplier_("#"),  # 6
        clicks_multiplier_("#"),  # 7
        number_of_rebirths_("#"),  # 8
        number_of_prestiges_("#"),  # 9
        number_of_regressions_("#"),  # 10
        name_(""),  # 11
        cost_("#"),  # 12
        effect_(""),  # 13
        description_(""),  # 14
        type_(""),  # 15
        level_("#"),  # 16
        max_level_("#"),  # 17
        base_(""),  # 18
        rebirth_(""),  # 19
        prestige_(""),  # 20
        regression_(""),  # 21
        stage_(""),  # 22
        all_stages_(""),  # 23
        locked_stages_(""),  # 24
        unlocked_stages_(""),  # 25
        completed_stages_(""),  # 26
    ]
