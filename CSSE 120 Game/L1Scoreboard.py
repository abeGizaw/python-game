import pygame

# Ben Lyons
class L1Scoreboard:
    def __init__(self, screen, original_lives):
        self.screen = screen
        self.lives = original_lives
        self.font = pygame.font.SysFont("timesnewroman", 30)

    def draw(self):
        lives_string = "Lives: {}".format(self.lives)
        lives_image = self.font.render(lives_string, True, (255, 255, 255))
        self.screen.blit(lives_image, (5, 5))
