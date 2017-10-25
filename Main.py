
""" This is getting information from Random_Map """
from Random_Map import*


"""
This is the main file that calls all other files and then keeps
the game window running.
"""

# The game window while loop.
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    # Generates a new map to the game window on mouse click down.
    if event.type == pygame.MOUSEBUTTONDOWN:
        generate_random_map()

    pygame.display.flip()
