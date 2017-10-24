import os
import random
import numpy
import pygame

#Variables to set the width and height of the game window
game_window_width = 64 * 20
game_window_height = 64 * 12

#The game window itself
GameWindow = pygame.display.set_mode((game_window_width,game_window_height))

#Array for the tiles list in the tiles folder
list_of_tiles = []

#the map matrix array
map_Matrix = []

#for loop to take each tile image from the tiles folder and put them in the tile list
for root, dirs, files in os.walk('TilesToBeUsed'):
    for file in files:
        if file.endswith('png'):
            list_of_tiles.append(os.path.join(root,file))

"""
New map generator, this one works by using a matrix to define where it should place the
tiles on the game window.
"""
def GenerateRandomMap():
    #Position X and Y on the game window
    Pos_X = 0
    Pos_Y = 0

    #This creates a random map matrix using the numpy array library
    map_Matrix = numpy.random.randint(11, size=(game_window_height / 64, game_window_width / 64))

    """
    The Tile rules.
    This works by checking the tile above and to the left of 
    the current tile and then deciding on what tile to place down
    """
    for row_num, row_list in enumerate(map_Matrix):
        for tile_num in enumerate(row_list):

            connecting_Top_Tiles = [1, 3, 4]
            top_Connector_Tiles = [1, 5]

            connecting_Left_Tiles = [2, 3, 5]
            left_Connector_Tiles = [2, 4]

            neutral_Tiles = [0, 7, 8, 3, 9, 10]

            tile_Above = (row_num -1, tile_num[0])
            tile_Left = (row_num,tile_num[0] -1)
            curent_Pos = (row_num,tile_num[0])

            if map_Matrix.item(tile_Above) in connecting_Top_Tiles and map_Matrix.item(tile_Left) in connecting_Left_Tiles:
                map_Matrix.itemset(curent_Pos, 6)

            elif map_Matrix.item(tile_Above) not in connecting_Top_Tiles and map_Matrix.item(tile_Left) in connecting_Left_Tiles:
                map_Matrix.itemset(curent_Pos, random.choice(left_Connector_Tiles))

            elif map_Matrix.item(tile_Above) in connecting_Top_Tiles and map_Matrix.item(tile_Left) not in connecting_Left_Tiles:
                map_Matrix.itemset(curent_Pos, random.choice(top_Connector_Tiles))

            else:
                map_Matrix.itemset(curent_Pos, random.choice(neutral_Tiles))

    #for loop that blits to the screen each tile number within the modified ruled matrix
    for row_num, row_list in enumerate(map_Matrix):
        for tile_num in enumerate(row_list):
            load_tile = pygame.image.load(list_of_tiles[tile_num[1]])
            GameWindow.blit(load_tile, (Pos_X, Pos_Y))

            Pos_X += 64
        Pos_Y += 64
        Pos_X = 0

    #this will print the matrix in the console
    #print map_Matrix

#calls the
GenerateRandomMap()

#The game window while loop
Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            Running = False

    #blits random tiles to the gamewindow on mouse click down
    if event.type == pygame.MOUSEBUTTONDOWN:
        GenerateRandomMap()

    pygame.display.flip()