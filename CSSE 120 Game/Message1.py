import time
import pygame
import Level1

# Colby Donner
mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Game Base')
screen = pygame.display.set_mode((1000, 750), 0, 32)
image1 = pygame.image.load('NewLevel1Background.png')
font = pygame.font.SysFont('None', 50)
font2 = pygame.font.SysFont('None', 30)
white = (255, 255, 255)

Black = (0, 0, 0)

screen.blit(image1, (0, 0))


def draw_text(text, font, color, surface, x, y):
    mainClock.tick(60)
    for char in text:
        textobj = font.render(char, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        textrect.center = (x, y)
        x += textrect.width
        time.sleep(0.01)
        surface.blit(textobj, textrect.center)
        pygame.display.update()


draw_text('The Earth has suddenly been attacked by aliens and', font, white, screen, 75, 85)
draw_text('you are the last person alive. Survive to figure out', font, white, screen, 75, 125)
draw_text('how to save humanity. Good luck!', font, white, screen, 75, 165)
time.sleep(3)
Level1.level_1()
