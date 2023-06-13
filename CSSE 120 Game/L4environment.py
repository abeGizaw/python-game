import pygame
#Abe Gizaw and Ben lyons
class Environment:
    def __init__(self, screen, gravity, ground_level):
        self.screen = screen
        self.gravity = gravity
        self.ground_level = ground_level
        self.background = pygame.image.load('NewLevel4Background.png')
        self.background_image = pygame.transform.scale(self.background, (self.screen.get_width(), self.screen.get_height()))

    def draw(self):
        self.screen.blit(self.background_image, (0, 0))
