import pygame
import math
from L1Projectile import L1Projectile

# Ben Lyons
class L1Person:
    def __init__(self, screen, x, y, y_speed, lives, shoot_speed, powerup_instance):
        self.screen = screen
        self.x = x
        self.y = y
        self.y_speed = y_speed
        self.lives = lives
        self.shoot_speed = shoot_speed
        self.image = pygame.image.load("L1hero.png")
        self.image.set_colorkey((255, 255, 255))
        self.projectiles = []
        self.powerup_in_use = powerup_instance

    def draw(self):
        self.screen.blit(self.image, (self.x - self.image.get_width() / 2, self.y - self.image.get_height() / 2))

    def shoot(self, click_x, click_y):
        dist = math.dist((self.x, self.y), (click_x, click_y))
        if dist != 0:
            self.projectiles.append(L1Projectile(self.screen, self.x, self.y,
                                                self.shoot_speed * (click_x - self.x) / dist,
                                                self.shoot_speed * (click_y - self.y) / dist, self.powerup_in_use))

    def hit_by(self, projectile):
        hitbox = pygame.Rect(self.x - self.image.get_width() / 2, self.y - self.image.get_height() / 2,
                             self.image.get_width(), self.image.get_height())
        return hitbox.collidepoint(projectile.x, projectile.y)
