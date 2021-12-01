# My First PyGame, Geovanny Moncayo, 12/01/21 1:55pm, v0.6

import pygame, sys
from pygame.locals import *

# Start PyGame
pygame.init()

# Setup our window. 1
windowSurface = pygame.display.set_mode((500,400), 0, 32)
pygame.display.set_caption('Hello, world!')

# Setup Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
FORESTGREEN = (34, 139, 34)
GREY = (100, 100, 100)
# Setup font.
basicFont = pygame.font.SysFont(None, 48)

#Setup text.
text = basicFont.render('Hello, world', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centerx = windowSurface.get_rect().centery

# Fill background color.
windowSurface.fill(GREY)

# Draw a polygon onto the screen.
pygame.draw.polygon(windowSurface, RED, ((146, 0), (291, 106), (236,277), (56, 277), (0, 106)))

# Draw lines on the screen
pygame.draw.line(windowSurface, WHITE, (60, 60), (120, 60), 4)
pygame.draw.line(windowSurface, BLACK, (60, 30), (60, 90), 2)
pygame.draw.line(windowSurface, BLACK, (120, 30), (120, 90), 2)