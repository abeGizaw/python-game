import pygame

# Abe Gizaw
class Background:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('NewLevel2Background.png')
        self.image = pygame.transform.scale(self.image, (self.screen.get_width(), self.screen.get_height()))

    def draw(self):
        self.screen.blit(self.image, (0, 0))