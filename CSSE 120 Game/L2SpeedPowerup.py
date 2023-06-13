import random
import L2Airplane
import pygame
# Abe Gizaw
class Powerup:
    def __init__(self, screen, hero):
        self.screen = screen
        self.hero_image = pygame.image.load('L2fighterjet.png')
        self.x = random.randint(self.hero_image.get_width() // 2, self.screen.get_width() / 2)
        self.y = random.randint(0, self.screen.get_height())
        self.image = pygame.image.load('SpeedPowerup.png')
        self.hero = hero

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def hitbox(self, hero):
        hitbox = pygame.Rect(self.x - self.image.get_width() / 2, self.y - self.image.get_height() / 2,
                             self.image.get_width(), self.image.get_height())

        return hitbox.collidepoint(self.hero.x, self.hero.y)