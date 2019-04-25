'''
Brick Breakers
Nathan Tang
19/04/25
'''
import sys
import random
import pygame
import functions
pygame.init() # Loads the pygame module commands in the program

# Display Variables
TITLE = 'Brick Breakers' # Appears in the window title
FPS = 60 # Frames per second
WIDTH = 800
HEIGHT = 600
SCREENDIM = (WIDTH, HEIGHT)

# Color Variables
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (50, 50, 50)
BROWN = (100, 65, 50)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 102, 0)
PURPLE = (150, 0, 255)
PINK = (255, 0, 150)
colors = (WHITE, BROWN, RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, PINK)

# Create the window
screen = pygame.display.set_mode(SCREENDIM) # Creates the main surface where all other assets are placed
pygame.display.set_caption(TITLE) # Updates the window title with TITLE
screen.fill(GREY) # Fills the entire surface with the colour.  Think of fill as erase

clock = pygame.time.Clock() # Starts a clock object to measure time

# Background image
stars = []
for i in range(200):
    stars.append(functions.box(2, 1, random.randrange(0, WIDTH), random.randrange(0, HEIGHT)))
for i in stars:
    i.setColor(WHITE)






# CODE #

while True:
    for event in pygame.event.get(): # Returns all inputs and triggers into the array
        if event.type == pygame.QUIT: # If the window close button is clicked
            sys.exit()
            
    # Background
    screen.fill(BLACK)
    for i in stars:
        screen.blit(i.getBox(), i.getPos())


    clock.tick(FPS) # Pause the game until the FPS time is reached
    pygame.display.flip() # Update the screen with changes
pygame.quit()