# Table module for the credits menu
"""
Table module for the credits menu
"""

from collections.abc import Sequence
from pygame import Surface, font
from src.assets.files.credits import create_credits_table


def draw_table(
    table: Sequence[dict[str, str]] | None = None,
) -> Surface:
    """
    The draw table function that automatically creates a table from credits.json data.
    The table will infinitely accommodate new information as it's added to the JSON file.
    """
    # If no table provided, create one automatically from credits.json
    if table is None:
        table = create_credits_table()

    # Handle empty table
    if not table:
        table_surface: Surface = Surface((400, 200))
        table_surface.fill((0, 0, 0))  # Black color
        return table_surface

    # Calculate table dimensions
    num_rows = len(table)
    num_columns = len(table[0].keys()) if table else 0

    # Set cell dimensions
    cell_width = 150
    cell_height = 40

    # Create surface with proper dimensions
    table_surface: Surface = Surface(
        (num_columns * cell_width, (num_rows + 1) * cell_height)
    )
    table_surface.fill((0, 0, 0))  # Black color

    # Initialize font
    pygame_font = font.Font(None, 24)

    # Draw header row
    headers = list(table[0].keys()) if table else []
    for col_index, header in enumerate(headers):
        text_surface = pygame_font.render(
            header.title(), True, (255, 255, 255)
        )  # White color
        x_pos = col_index * cell_width + 5
        y_pos = 5
        table_surface.blit(text_surface, (x_pos, y_pos))

    # Draw data rows
    for row_index, row_data in enumerate(table):
        for col_index, value in enumerate(row_data.values()):
            # Truncate long values for display
            display_value = (
                str(value)[:20] + "..." if len(str(value)) > 20 else str(value)
            )
            text_surface = pygame_font.render(
                display_value, True, (255, 255, 255)
            )  # White color
            x_pos = col_index * cell_width + 5
            y_pos = (row_index + 1) * cell_height + 5
            table_surface.blit(text_surface, (x_pos, y_pos))

    return table_surface


def get_credits_table() -> Sequence[dict[str, str]]:
    """
    Get the credits table data automatically populated from credits.json.
    This will always return the most current data from the JSON file.
    """
    return create_credits_table()
