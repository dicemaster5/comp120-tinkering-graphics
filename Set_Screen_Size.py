import pygame

"""
This makes the game window to size required.
Game window width and height take the size of the tile in pixels then multiply them by how
many you require.
"""
# Variables to set the width and height of the game window.
game_window_width = 64 * 20
game_window_height = 64 * 12

# The game window itself.
game_window = pygame.display.set_mode((game_window_width, game_window_height))

