import os

"""Gets the list of tiles wanted from the "TilesToBeUsed" folder and puts them into an array"""
list_of_tiles = []

# takes each tile image from the tiles folder and put them in the tile list.
for root, dirs, files in os.walk('TilesToBeUsed'):
    for file in files:
        if file.endswith('png'):
            list_of_tiles.append(os.path.join(root, file))
