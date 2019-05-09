'''
Brick Breakers Functions
Nathan Tang
19/04/25
'''

import pygame

### NOTE: The modifier and accessor methods in myClass, text and box classes are properties of encapsulation

class myClass:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)
        self.xDir = 1
        self.yDir = 1
        self. surface = pygame.Surface((0, 0), pygame.SRCALPHA, 32)
        self.red = 0
        self.green = 0
        self.blue = 0
        self.color = (self.red, self.green, self.blue)

    def getSurface(self):
        return self.surface

    def getPos(self):
        return self.pos

    def setColor(self, color = (0, 0, 0)):
        self.red = color[0]
        self.green = color[1]
        self.blue = color[2]
        self.color = (self.red, self.green, self.blue)
        return self.color
    
    def setPos(self, x, y):
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)
        return self.pos



class text(myClass):
    def __init__(self, content, font = 'Arial', fontSize = 24):
        myClass.__init__(self)
        self.fontFamily = font
        self.fontSize = fontSize
        self.font = pygame.font.SysFont(self.fontFamily, self.fontSize)
        self.content = content
        self.surface = self.font.render(self.content, 1, self.color)

    def setColor(self, color = (0, 0, 0)):
        myClass.setColor(self, color)
        self.surface = self.font.render(self.content, 1, self.color)

    def setText(self, content):
        self.content = content
        self.surface = self.font.render(self.content, 1, self.color)

    def getText(self):
        return myClass.getSurface(self)
        


class box(myClass):
    def __init__(self, width, height, x = 0, y = 0):
        myClass.__init__(self, x, y)
        self.width = width
        self.height = height
        self.dim = (self.width, self.height)
        self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)
        self.surface.fill(self.color)
        
    def setColor(self, color):
        myClass.setColor(self, color)
        self.surface.fill(self.color)

    def moveBox(self, speed = (1, 1) ):
        self.x += (self.xDir*speed[0])
        self.y += (self.yDir*speed[1])
        self.pos = (self.x, self.y)

    def getBox(self):
        return myClass.getSurface(self)

    def keyMove(self, keyPress, speed = 10):
        # if keyPress[pygame.K_UP]:
        #     self.y -= speed
        # if keyPress[pygame.K_DOWN]:
        #     self.y += speed
        if keyPress[pygame.K_LEFT]:
            self.x -= speed
        if keyPress[pygame.K_RIGHT]:
            self.x += speed

        self.pos = (self.x, self.y)

    def getX(self):
        return self.x

    def getY(self):
        return self.y
        
    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height


def getSpriteCollision(sprite1, sprite2):
    if sprite2.getX() <= sprite1.getX() + sprite1.getWidth() <=  sprite2.getX() + sprite2.getWidth() + sprite1.getWidth() and sprite2.getY() <= sprite1.getY() + sprite1.getHeight() <= sprite2.getY() + sprite2.getHeight() + sprite1.getHeight():
        return True
    else:
        return False

def gameOver(WIDTH, HEIGHT, color):
    gameOverText = text("GAME OVER", "Arial Black", 80)
    gameOverText.setColor(color)
    gameOverText.setPos(WIDTH/2 - gameOverText.getText().get_width() / 2, HEIGHT/2 - gameOverText.getText().get_height())

    escMenu = text("Press ESC to quit the game", "Arial Black", 20)
    escMenu.setColor(color)
    escMenu.setPos(WIDTH/2 - escMenu.getText().get_width() / 2, HEIGHT * (3/4))
    
    return gameOverText, escMenu

def nextLevel(WIDTH, HEIGHT, color):
    nextLevelText = text("LEVEL COMPLETE", "Arial Black", 60)
    nextLevelText.setColor(color)
    nextLevelText.setPos(WIDTH/2 - nextLevelText.getText().get_width() / 2, HEIGHT/2 - nextLevelText.getText().get_height())

    spaceCont = text("Press SPACE to continue", "Arial Black", 20)
    spaceCont.setColor(color)
    spaceCont.setPos(WIDTH/2 - spaceCont.getText().get_width() / 2, HEIGHT * (3/4))

    return nextLevelText, spaceCont