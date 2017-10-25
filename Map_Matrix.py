import numpy
import random

from Set_Screen_Size import*
from Get_Tiles import*


""" This creates a random map matrix using the numpy array library."""
map_matrix = numpy.random.randint(11, size=(game_window_height / 64, game_window_width / 64))


"""
The Tile rules.
This works by checking the tile above and to the left of
the current tile and then deciding on what tile to place down.
"""


def rules_for_tiles():
    for row_num, row_list in enumerate(map_matrix):
        for tile_num in enumerate(row_list):

            # Tiles that connect from the top side
            connecting_top_tiles = [1, 3, 4]
            top_connector_tiles = [1, 5]

            # Tiles that connect from the left side
            connecting_left_tiles = [2, 3, 5]
            left_connector_tiles = [2, 4]

            # these are tiles that don't connect to the roads from the top and left side
            neutral_tiles = [0, 7, 8, 3, 9, 10]

            tile_above = (row_num - 1, tile_num[0])
            tile_left = (row_num, tile_num[0] - 1)
            current_pos = (row_num, tile_num[0])

            # IF statement rules to apply to the map matrix
            if map_matrix.item(tile_above) in connecting_top_tiles \
                    and map_matrix.item(tile_left) in connecting_left_tiles:
                map_matrix.itemset(current_pos, 6)

            elif map_matrix.item(tile_above) not in connecting_top_tiles \
                    and map_matrix.item(tile_left) in connecting_left_tiles:
                map_matrix.itemset(current_pos, random.choice(left_connector_tiles))

            elif map_matrix.item(tile_above) in connecting_top_tiles \
                    and map_matrix.item(tile_left) not in connecting_left_tiles:
                map_matrix.itemset(current_pos, random.choice(top_connector_tiles))

            else:
                map_matrix.itemset(current_pos, random.choice(neutral_tiles))


