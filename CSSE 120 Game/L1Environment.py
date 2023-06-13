import pygame

# Ben Lyons
class L1Environment:
    def __init__(self, screen, gravity, ground_level):
        self.screen = screen
        self.gravity = gravity
        self.ground_level = ground_level
        self.image = pygame.image.load("NewLevel1Background.png")

    def draw(self):
        self.screen.blit(self.image, (0, 0))
