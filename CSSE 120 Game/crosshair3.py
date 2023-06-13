import pygame
from pygame.locals import *
#Colby Donner
class Crosshair:
    def __init__(self, screen):
        self.image = pygame.image.load('crosshair3.py')
        self.screen = screen
    def draw(self):
        pos = pygame.mouse.get_pos()
        BLACK = (0, 0, 0)
        self.image.set_colorkey(BLACK)
        self.screen.blit(self.image, (pos))