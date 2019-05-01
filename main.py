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
FPS = 120 # Frames per second
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
    stars.append(functions.box(2, 1, random.randrange(0, WIDTH), random.randrange(50, HEIGHT)))
for i in stars:
    i.setColor(WHITE)



# Invisible walls
topWall = functions.box(800, 1, 0, 50)
bottomWall = functions.box(800, 1, 0, 599)
leftWall = functions.box(1, 550, 0, 50)
rightWall = functions.box(1, 550, 799, 50)


# Logo
logo = functions.text("BRICK BREAKER", font = 'Arial Black', fontSize=50)
logo.setColor(WHITE)
logo.setPos(WIDTH/2 - logo.getText().get_width() / 2, -10)

# Paddle
paddle = functions.box(75, 10)
paddle.setPos(WIDTH/2 - paddle.getBox().get_width() / 2, HEIGHT - paddle.getBox().get_height() - 5)
paddle.setColor((0, 200, 100))

# Ball
# ball = functions.ball(50, 50, 100, 100)
ball = functions.box(20, 20)
ball.setPos(WIDTH/2 - ball.getBox().get_width() / 2, HEIGHT - paddle.getBox().get_height() - ball.getBox().get_height() - 5)
ball.setColor((WHITE))
# Random ball movement - not working
# ballStartMove = (round(random.uniform(-2, 2), 2), round(random.uniform(0, 2), 2)) # (-0.5, 1)
# print(ballStartMove)

# Blocks
blocks = []
# for rows in range(6):
#     for columns in range 10:
#         blocks = functions.box(50, 20, ????) Need to figure out x and y

# CODE #

while True:
    for event in pygame.event.get(): # Returns all inputs and triggers into the array
        if event.type == pygame.QUIT: # If the window close button is clicked
            sys.exit()
            
    # Background
    screen.fill(BLACK)
    for i in stars:
        screen.blit(i.getBox(), i.getPos())


    pressedKeys = pygame.key.get_pressed() # Check for key presses

    screen.blit(logo.getText(), logo.getPos())
    screen.blit(paddle.getBox(), paddle.getPos())
    # pygame.draw.circle(screen, WHITE, [ball.x, ball.y], ball.width/2)
    # screen.blit(ball.getBall(), ball.getPos())
    screen.blit(ball.getBox(), ball.getPos())
    

    # Ball movement
    ball.moveBox((0.5,-1))
    if ball.x <= leftWall.x: # Left wall
        ball.xDir = 1
    if ball.x + ball.getBox().get_width() >= rightWall.x: # Right wall
        ball.xDir = -1
    elif ball.y <= topWall.y: # Top wall
        ball.yDir = -1
    elif ball.y + ball.getBox().get_height() >= paddle.y and ball.x + ball.getBox().get_width() >= paddle.x and ball.x <= paddle.x + paddle.getBox().get_width(): # Paddle
        ball.yDir = 1
    elif ball.y + ball.getBox().get_height() >= bottomWall.y: # If crash Bottom wall
        ball.xDir = 0
        ball.yDir = 0
        # Game over
        gameOverText, escMenu = functions.gameOver(WIDTH, HEIGHT, WHITE)
        screen.blit(gameOverText.getText(), gameOverText.getPos())
        screen.blit(escMenu.getText(), escMenu.getPos())

    # Paddle movement
    paddle.keyMove(pressedKeys)
    if paddle.x <= leftWall.x:
        paddle.x = 0
    if (paddle.x + paddle.getBox().get_width()) >= rightWall.x:
        paddle.x = 800 - paddle.getBox().get_width()

    clock.tick(FPS) # Pause the game until the FPS time is reached
    pygame.display.flip() # Update the screen with changes
pygame.quit()



# TODO:
# 1. Lives
# 2. Boxes
# 3. Menu
# 4. Accelerated collision