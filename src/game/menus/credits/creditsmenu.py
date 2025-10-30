# Credits menu module for the idle game
"""
Credits menu module for the idle game
"""

import pygame
from pygame import Color, Surface
from pygame_menu import Menu, Theme

from src.game.menus.credits.cmui.buttons import buttons
from src.game.menus.credits.cmui.table import draw_table, get_credits_table
from src.game.menus.menumanager import (
    get_creditsmenu_assets_loaded,
    creditsmenu_assets,
)


def creditsmenu() -> None:
    """
    The credits menu of the idle game
    """
    # Check if the credits menu assets have any value
    if get_creditsmenu_assets_loaded() is not None:  # pylint: disable=R1705
        # If the credits menu assets have no value, return to creditsmenu_assets()
        return creditsmenu_assets()
    elif get_creditsmenu_assets_loaded() is False:
        # If the credits menu assets have the value False, return to the creditsmenu_assets()
        return creditsmenu_assets()
    else:
        # If the credits menu assets have the value True, continue
        pass
    surface: Surface = pygame.display.set_mode((1000, 700))

    # Create and display the credits table
    credits_table = get_credits_table()
    table_surface = draw_table(credits_table)

    # Create menu with larger size to accommodate table
    menu = Menu(
        title="Credits Menu",
        width=1000,
        height=700,
        theme=Theme(background_color=Color.BLACK),
    )

    # Add table display to menu
    menu.add.label("Credits Table:", font_size=20, margin=(0, 10))

    # Add buttons
    for title, on_click in buttons():
        # Add the button from the buttons module to the menu
        menu.add.button(title, on_click, margin=(0, 10))

    # Main loop with table display
    running = True
    clock = pygame.time.Clock()

    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.constants.QUIT:
                running = False

        # Clear screen
        surface.fill(Color.BLACK)

        # Draw table
        surface.blit(table_surface, (50, 100))

        # Update menu
        menu.update(events)
        menu.draw(surface)

        pygame.display.flip()
        clock.tick(60)

    return creditsmenu()
