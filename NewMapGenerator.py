import os
import random
import numpy
import pygame

'#Variables to set the width and height of the game window and then display'
game_window_width = 1280
game_window_height = 640
game_window = pygame.display.set_mode((game_window_width, game_window_height))

'#List for the tiles list in the tiles folder'
list_of_tiles = []
map_matrix = []

'#for loop to take each tile image from the tiles folder and put them in the tile list'
for root, dirs, files in os.walk('TilesToBeUsed'):
    for file in files:
        if file.endswith('png'):
            list_of_tiles.append(os.path.join(root, file))

'#This tells the array where it can find each different tile'
grass_tile = list_of_tiles[0]
path_tiles = list_of_tiles[1:6]
tree_tiles = list_of_tiles[7:8]

"""
New map generator, this one works by using a matrix to define where it should place the
tiles on the game window.
"""


def read_and_print_map_matrix():

    Pos_X = 0
    Pos_Y = 0
    map_matrix = numpy.random.randint(9, size=(game_window_height / 64, game_window_width / 64))

    '#the rules'
    for row_num, row_list in enumerate(map_matrix):
        for tile_num in enumerate(row_list):

            connect_top_tiles = [1, 3, 4]
            top_connector_tiles = [1, 5]

            connect_left_tiles = [2, 3, 5]
            left_connector_tiles = [2, 4]

            neutrals = [0, 7, 8]

            tile_above = (row_num -1, tile_num[0])
            tile_left = (row_num,tile_num[0] -1)
            current_pos = (row_num,tile_num[0])

            if map_matrix.item(tile_above) in connect_top_tiles and map_matrix.item(tile_left) in connect_left_tiles:
                map_matrix.itemset(current_pos, 6)

            elif map_matrix.item(tile_above) not in connect_top_tiles and map_matrix.item(tile_left) in connect_left_tiles:
                map_matrix.itemset(current_pos, random.choice(left_connector_tiles))

            elif map_matrix.item(tile_above) in connect_top_tiles and map_matrix.item(tile_left) not in connect_left_tiles:
                map_matrix.itemset(current_pos, random.choice(top_connector_tiles))

            else:
                map_matrix.itemset(current_pos, random.choice(neutrals))

    '#blits to the screen the new random matrix with rules'
    for row_num, row_list in enumerate(map_matrix):
        for tile_num in enumerate(row_list):
            load_tile = pygame.image.load(list_of_tiles[tile_num[1]])
            game_window.blit(load_tile, (Pos_X, Pos_Y))

            Pos_X += 64
        Pos_Y += 64
        Pos_X = 0
    print map_matrix


read_and_print_map_matrix()


'#The game window while loop'
Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            Running = False

    '#blits random tiles to the game_window on click'

    if event.type == pygame.MOUSEBUTTONDOWN:
        read_and_print_map_matrix()
    pygame.display.flip()