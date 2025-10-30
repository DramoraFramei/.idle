# This file is used to gather the data from credits.json and set each set of
# variables to a row and column in a table.
"""
This file is used to gather the data from credits.json and set each set of
variables to a row and column in a table.
"""

import json
from collections.abc import Sequence

CREDITS_FILE: str = "src/assets/files/json/credits.json"
KEYWORDS: tuple[str, ...] = ("id", "username", "role", "discord", "github")


# Get the data from credits.json and set each set of variables to a row and column in a table.
def get_credits_file_data() -> Sequence[dict[str, str]]:
    """
    The credits file data as a list of dictionaries with string values
    """
    with open(CREDITS_FILE, "r", encoding="utf-8") as file:
        credits_file_data: Sequence[dict[str, str]] = json.load(file).get("credits", [])
    return credits_file_data


# Using the information from the functions above, put the data into a table.
def put_credits_file_data_into_table(
    credits_file_data: Sequence[dict[str, str]],
) -> Sequence[dict[str, str]]:
    """
    The credits file data as a dictionary of id, username, role, discord, and github strings.
    """
    return [
        {
            "id": credit.get("id", ""),
            "username": credit.get("username", ""),
            "role": credit.get("role", ""),
            "discord": credit.get("discord", ""),
            "github": credit.get("github", ""),
        }
        for credit in credits_file_data
    ]


def create_credits_table() -> Sequence[dict[str, str]]:
    """
    Automatically create a table from credits.json data.
    This function will infinitely accommodate new information as it's added to the JSON file.
    """
    credits_data = get_credits_file_data()
    return put_credits_file_data_into_table(credits_data)
