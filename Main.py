import os
import random
import numpy
import pygame

# Variables to set the width and height of the game window.
game_window_width = 64 * 20
game_window_height = 64 * 12

# The game window itself.
game_window = pygame.display.set_mode((game_window_width, game_window_height))

# Array for the tiles list in the tiles folder.
list_of_tiles = []

# takes each tile image from the tiles folder and put them in the tile list.
for root, dirs, files in os.walk('TilesToBeUsed'):
    for file in files:
        if file.endswith('png'):
            list_of_tiles.append(os.path.join(root, file))

"""
New map generator, this one works by using a matrix to define
where it should place the tiles on the game window.
"""
