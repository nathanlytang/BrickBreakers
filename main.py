'''
Brick Breakers
Nathan Tang
19/04/25
'''
import sys
import random
import pygame
import functions
import time
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
ORANGEYELLOW = (255, 144, 0)
PURPLE = (150, 0, 255)
PINK = (255, 0, 150)
colors = (WHITE, BROWN, RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, PINK)
blockColors = (RED, ORANGE, ORANGEYELLOW, YELLOW, GREEN, BLUE)

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

def levelVars():
    # Paddle
    paddle = functions.box(150, 10)
    paddle.setPos(WIDTH/2 - paddle.getBox().get_width() / 2, HEIGHT - paddle.getBox().get_height() - 5)
    paddle.setColor((0, 200, 100))

    # Ball
    # ball = functions.ball(50, 50, 100, 100)
    ball = functions.box(20, 20)
    ball.setPos(WIDTH/2 - ball.getBox().get_width() / 2, HEIGHT - paddle.getBox().get_height() - ball.getBox().get_height() - 5)
    ball.setColor((WHITE))
    # Random ball movement
    ballStartMove = (round(random.uniform(-2, 2), 1), round(random.uniform(-2, -1), 1)) # (-0.5, 1)
    ball.xDir = ballStartMove[0]
    ball.yDir = ballStartMove[1]
    print(ballStartMove)

    # Blocks
    blocks = []
    y = 80
    for rows in range(6):
        x = 0
        for columns in range(10):
            block = functions.box(80, 30, x, y)
            block.setColor(blockColors[rows])
            blocks.append(block)
            x += block.getBox().get_width()
        y += block.getBox().get_height()

    return paddle, ball, blocks, block



# Score
score = functions.text('Score: 0', 'Arial Bold', 25)
score.setColor(WHITE)
score.setPos(10, 10)
scoreVar = 0

# Lives
lives = functions.text('Lives: 3', 'Arial Bold', 25)
lives.setColor(WHITE)
lives.setPos(10, 30)
livesVar = 3

# Level
level = functions.text('Level: 0', 'Arial Bold', 25)
level.setColor(WHITE)
level.setPos(10, 50)
levelNum = 0


# CODE #
play = True
while play:
    paddle, ball, blocks, block = levelVars()
    levels = True
    levelNum += 1
    level.setText('Level: %s' % levelNum)
    
    while levels:
        for event in pygame.event.get(): # Returns all inputs and triggers into the array
            if event.type == pygame.QUIT: # If the window close button is clicked
                sys.exit()
                
        # Background
        screen.fill(BLACK)
        for i in stars:
            screen.blit(i.getBox(), i.getPos())


        pressedKeys = pygame.key.get_pressed() # Check for key presses

        screen.blit(logo.getText(), logo.getPos())
        screen.blit(score.getText(), score.getPos())
        screen.blit(lives.getText(), lives.getPos())
        screen.blit(paddle.getBox(), paddle.getPos())
        screen.blit(level.getText(), level.getPos())
        # pygame.draw.circle(screen, WHITE, [ball.x, ball.y], ball.width/2)
        # screen.blit(ball.getBall(), ball.getPos())
        screen.blit(ball.getBox(), ball.getPos())
        for i in blocks:
            screen.blit(i.getBox(), i.getPos())
        

        # Ball movement
        ball.moveBox((1, 1))
        if ball.x <= leftWall.x: # Left wall
            ball.xDir *= -1
        elif ball.x + ball.getBox().get_width() >= rightWall.x: # Right wall
            ball.xDir *= -1
        elif ball.y <= topWall.y: # Top wall
            ball.yDir *= -1
        elif ball.y + ball.getBox().get_height() >= paddle.y and ball.x + ball.getBox().get_width() >= paddle.x and ball.x <= paddle.x + paddle.getBox().get_width(): # Paddle
            ball.yDir *= -1
        elif ball.y + ball.getBox().get_height() >= bottomWall.y: # If crash Bottom wall
            if livesVar > 0:
                livesVar -= 1 # Remove one life
                lives.setText('Lives: %s' % livesVar)
                ball.yDir *= -1
                ball.y = paddle.y - ball.getBox().get_height()
                ball.x = paddle.x + paddle.getBox().get_width() / 2 - ball.getBox().get_width()
                time.sleep(1)
            elif livesVar == 0:
                ball.xDir = 0
                ball.yDir = 0
                # Game over
                gameOverText, escMenu = functions.gameOver(WIDTH, HEIGHT, WHITE)
                screen.blit(gameOverText.getText(), gameOverText.getPos())
                screen.blit(escMenu.getText(), escMenu.getPos())
                # Exit program if ESC is clicked
                if pressedKeys[pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit()
                

        # Paddle movement
        paddle.keyMove(pressedKeys, 6)
        if paddle.x <= leftWall.x:
            paddle.x = 0
        if (paddle.x + paddle.getBox().get_width()) >= rightWall.x:
            paddle.x = 800 - paddle.getBox().get_width()

        if len(blocks) == 0:
            # Next level
            nextLevelText = functions.nextLevel(WIDTH, HEIGHT, WHITE)
            nextLevelText.setColor(WHITE)
            screen.blit(nextLevelText.getText(), nextLevelText.getPos())
            levels = False

        # Ball-brick collisions
        for i in range(len(blocks)):
            if functions.getSpriteCollision(ball, blocks[i]): # Change block variable
                blocks.pop(i)
                ball.yDir *= -1
                scoreVar += 5 # Add 5 to score
                score.setText('Score: %s' % scoreVar)
                break

        

        clock.tick(FPS) # Pause the game until the FPS time is reached
        pygame.display.flip() # Update the screen with changes

    # Continue program if SPACE is clicked
    # pressedKeys = pygame.key.get_pressed()
    # while True:
    #     try:
    #         if pressedKeys[pygame.K_SPACE]:
    #             break
    #     except:
    #         pass

    time.sleep(3)
    
pygame.quit()



# TODO:
# 1. 0.0 movement
# 2. Menu
# 3. Accelerated collision
# 4. High score