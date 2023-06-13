import pygame
#Abe Gizaw and Ben lyons
class Scoreboard:
    def __init__(self, screen, original_lives):
        self.screen = screen
        self.lives = original_lives
        self.font = pygame.font.SysFont("timesnewroman", 30)

    def draw(self):
        lives_string = "Lives: {}".format(self.lives)
        lives_image = self.font.render(lives_string, True, (0, 0, 0))
        self.screen.blit(lives_image, (5, 5))