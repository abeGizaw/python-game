import pygame
import math
from L1Projectile import L1Projectile

# Ben Lyons
class L1Enemy:
    def __init__(self, screen, x, y, lives, shoot_speed):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load("Enemy.png")
        self.image.set_colorkey((0, 0, 0))
        self.lives = lives
        self.shoot_speed = shoot_speed
        self.projectiles = []

    def draw(self):
        self.screen.blit(self.image, (self.x - self.image.get_width() / 2, self.y - self.image.get_height() / 2))

    def shoot(self, person_x, person_y):
        dist = math.dist((self.x, self.y), (person_x, person_y))
        if dist != 0:
            self.projectiles.append(L1Projectile(self.screen, self.x,
                                                self.y, self.shoot_speed * (person_x - self.x) / dist,
                                                self.shoot_speed * (person_y - self.y) / dist, False))

    def hit_by(self, projectile):
        hitbox = pygame.Rect(self.x - self.image.get_width() / 2, self.y - self.image.get_height() / 2,
                             self.image.get_width(), self.image.get_height())
        return hitbox.collidepoint(projectile.x, projectile.y)
