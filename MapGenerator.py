import os
import random
import numpy
import pygame

#Variables to set the width and height of the game window
game_window_width = 640
game_window_height = 640

#The game window itself
GameWindow = pygame.display.set_mode((game_window_width,game_window_height))

#List for the tiles list in the tiles folder
list_of_tiles = []
mapMatrix = []

#for loop to take each tile image from the tiles folder and put them in the tile list
for root, dirs, files in os.walk('TilesToBeUsed'):
    for file in files:
        if file.endswith('png'):
            list_of_tiles.append(os.path.join(root,file))

grass_tile = list_of_tiles[0]
path_tiles = list_of_tiles[1:6]
tree_tiles = list_of_tiles[7:8]
#water_tile = list_of_tiles[23]

"""
The Old Random map generator, this will take a random image from the tiles
list and blit it in the game window every 64 pixels on the x and y axis.
"""
def GenerateRandomMap():
    for x in range(0,game_window_width,64):
        for y in range(0,game_window_height,64):
            randomr = random.randrange(9)
            load_tile = pygame.image.load(list_of_tiles[randomr])
            GameWindow.blit(load_tile, (x,y))

"""
New map generator, this one works by using a matrix to define where it should place the
tiles on the game window.
"""
def ReadAndPrintMapMatrix():
    Pos_X = 0
    Pos_Y = 0
    mapMatrix = numpy.random.randint(9, size=(10, 10))
    print mapMatrix

    for row_num, row_list in enumerate(mapMatrix):
        for tile_num in enumerate(row_list):
            tile_Above = (row_num -1, tile_num[0])
            tile_Left = (row_num,tile_num[0] -1)
            curentPos = (row_num,tile_num[0])

            #Rules for each tile
            if mapMatrix.item(tile_Above) == 1:
                mapMatrix.itemset(curentPos, random.choice([5,6]))

            elif mapMatrix.item(tile_Above) == 2:
                mapMatrix.itemset(curentPos, random.choice([0,2,3,4,7,8]))

            elif mapMatrix.item(tile_Above) == 3:
                mapMatrix.itemset(curentPos, random.choice([1,5,6]))

            elif mapMatrix.item(tile_Above) == 4:
                mapMatrix.itemset(curentPos, random.choice([1,5,6]))

            elif mapMatrix.item(tile_Above) == 5:
                mapMatrix.itemset(curentPos, random.choice([0,1,3,4,7,8]))

            elif mapMatrix.item(tile_Above) == 6:
                mapMatrix.itemset(curentPos, random.choice([2,3,4,7,8,0]))

            elif mapMatrix.item(tile_Above) == 7 or 8:
                mapMatrix.itemset(curentPos, random.choice([0,2,5,6,7,8]))

            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

            elif mapMatrix.item(tile_Left) == 1:
                mapMatrix.itemset(curentPos, random.choice([1,3,5,7,8]))

            elif mapMatrix.item(tile_Left) == 2:
                mapMatrix.itemset(curentPos, random.choice([6,4]))

            elif mapMatrix.item(tile_Left) == 3:
                mapMatrix.itemset(curentPos, random.choice([2,6,4]))

            elif mapMatrix.item(tile_Left) == 4:
                mapMatrix.itemset(curentPos, random.choice([0,1,3,5,7,8]))

            elif mapMatrix.item(tile_Left) == 5:
                mapMatrix.itemset(curentPos, random.choice([6,4]))

            elif mapMatrix.item(tile_Left) == 6:
                mapMatrix.itemset(curentPos, random.choice([7,8,0]))

            elif mapMatrix.item(tile_Left) == 7 or 8:
                mapMatrix.itemset(curentPos, random.choice([0,1,4,6,7,8]))


    for row_num, row_list in enumerate(mapMatrix):
        for tile_num in enumerate(row_list):
            load_tile = pygame.image.load(list_of_tiles[tile_num[1]])
            GameWindow.blit(load_tile, (Pos_X, Pos_Y))

            Pos_X += 64
        Pos_Y += 64
        Pos_X = 0
    print mapMatrix

#GenerateRandomMap()

ReadAndPrintMapMatrix()


#The game window while loop
Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            Running = False

    #blits random tiles to the gamewindow on click

    if event.type == pygame.MOUSEBUTTONDOWN:
            ReadAndPrintMapMatrix()
    pygame.display.flip()