import time
import pygame
#Colby Donner
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Game Base')
screen = pygame.display.set_mode((1000, 750), 0, 32)
image1 = pygame.image.load('NewLevel2Background.png')
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


draw_text('You have successfully defeated the aliens near the ground.', font, white, screen, 20, 80)
draw_text('You beat some info out of an alien and learned that the', font, white, screen, 20, 120)
draw_text('main base is at the moon. You decide to go there yourself,', font, white, screen, 20, 160)
draw_text('so you hijack an airplane to get to the nearest space station!', font, white, screen, 20, 200)
time.sleep(3)