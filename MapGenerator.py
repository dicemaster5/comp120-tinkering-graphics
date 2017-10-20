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
mapMatrix = numpy.random.randint(25, size=(10,10))

#for loop to take each tile image from the tiles folder and put them in the tile list
for root, dirs, files in os.walk('TilesToBeUsed'):
    for file in files:
        if file.endswith('png'):
            list_of_tiles.append(os.path.join(root,file))

path_tiles = list_of_tiles[0:14]
tree_tiles = list_of_tiles[15:22]
water_tile = list_of_tiles[23]
grass_tiles = list_of_tiles[24:25]

def ReadAndPrintMapMatrix():
    for row_num, row_list in enumerate(mapMatrix):
        for tile_num in enumerate(row_list):
            return tile_num[1]
"""
the map generator, this will take a random image from
the tiles list and blit it in the game window every 64 pixels on the x and y axis
"""
def GenerateRandomMap():
    for x in range(0,game_window_width,64):
        for y in range(0,game_window_height,64):
            randomr = random.randrange(25)
            number = ReadAndPrintMapMatrix()
            load_tile = pygame.image.load(list_of_tiles[number])
            GameWindow.blit(load_tile, (x,y))

GenerateRandomMap()
print list_of_tiles
print mapMatrix
print mapMatrix[4,0]
#ReadAndPrintMapMatrix()


#the game window while loop
Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            Running = False

    #blits random tiles to the gamewindow on click
    #if event.type == pygame.MOUSEBUTTONDOWN:
        #GenerateRandomMap()
    pygame.display.flip()


    #CREATE A FOR LOOP THAT TAKES A RANDOM NUMBER (25) AND GIVE IT A POSITION FROM 0 - MAP SIZE X AND Y