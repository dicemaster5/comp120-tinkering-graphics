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


def generate_random_map():
    # Position X and Y on the game window.
    pos_x = 0
    pos_y = 0

    # This creates a random map matrix using the numpy array library.
    map_matrix = numpy.random.randint(11, size=(game_window_height / 64, game_window_width / 64))

    """
    The Tile rules.
    This works by checking the tile above and to the left of 
    the current tile and then deciding on what tile to place down
    """
    for row_num, row_list in enumerate(map_matrix):
        for tile_num in enumerate(row_list):

            connecting_top_tiles = [1, 3, 4]
            top_connector_tiles = [1, 5]

            connecting_left_tiles = [2, 3, 5]
            left_connector_tiles = [2, 4]

            neutral_tiles = [0, 7, 8, 3, 9, 10]

            tile_above = (row_num - 1, tile_num[0])
            tile_left = (row_num, tile_num[0] - 1)
            current_pos = (row_num, tile_num[0])

            if map_matrix.item(tile_above) in connecting_top_tiles \
                    and map_matrix.item(tile_left) in connecting_left_tiles:
                map_matrix.itemset(current_pos, 6)

            elif map_matrix.item(tile_above) not in connecting_top_tiles \
                    and map_matrix.item(tile_left) in connecting_left_tiles:
                map_matrix.itemset(current_pos, random.choice(left_connector_tiles))

            elif map_matrix.item(tile_above) in connecting_top_tiles\
                    and map_matrix.item(tile_left) not in connecting_left_tiles:
                map_matrix.itemset(current_pos, random.choice(top_connector_tiles))

            else:
                map_matrix.itemset(current_pos, random.choice(neutral_tiles))

    # for loop that blits to the screen each tile number within the modified ruled matrix.
    for row_num, row_list in enumerate(map_matrix):
        for tile_num in enumerate(row_list):
            load_tile = pygame.image.load(list_of_tiles[tile_num[1]])
            game_window.blit(load_tile, (pos_x, pos_y))

            pos_x += 64
        pos_y += 64
        pos_x = 0

    # this will print the matrix in the console.
    print map_matrix


# Generates a random map with a set of rules for paths to stay aligned.
generate_random_map()

# The game window while loop.
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    # blits random tiles to the game window on mouse click down.
    if event.type == pygame.MOUSEBUTTONDOWN:
        generate_random_map()

    pygame.display.flip()
