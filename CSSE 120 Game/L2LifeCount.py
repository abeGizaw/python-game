import pygame
# Abe Gizaw
class LifeCount:
    def __init__(self, screen, lives):
        self.screen = screen
        self.lives = lives
        self.font = pygame.font.Font(None, 30)

    def draw(self):
        score_string = "Lives:" + str(self.lives)
        score_image = self.font.render(score_string, True, (225, 225, 225))
        self.screen.blit(score_image, (5, 5))