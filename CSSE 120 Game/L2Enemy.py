import random
import pygame
import math
import L2Projectile
# Abe Gizaw
def get_distance_from(x_1, y_1, x_2, y_2):
    return math.dist((x_1, y_1), (x_2, y_2))
class Enemy:
    def __init__(self, screen, x, y, hit_count):
        self.screen = screen
        self.y_speed = 1
        self.image = pygame.image.load('Enemy.png')
        self.image_hero = pygame.image.load('L2fighterjet.png')
        self.x = x
        self.y = y
        self.original_x = self.x
        self.original_y = self.y
        self.projectile = []
        self.shoot_speed = 5
        self.is_dead = False
        self.hit_count = hit_count


    def move(self):
        self.y += self.y_speed
        if abs(self.y - self.original_y) >= 50:
            self.y_speed = -self.y_speed


    def draw(self):
        black = (0, 0, 0)
        self.image.set_colorkey(black)
        self.screen.blit(self.image, (self.x, self.y))
        random.randint(self.screen.get_width() - 100, self.screen.get_width())

    def shoot(self, air_x, air_y):
        air_x = air_x + self.image_hero.get_width() / 2
        air_y = air_y + self.image_hero.get_height() / 2
        dist = math.dist((self.x, self.y), (air_x, air_y))

        if dist != 0:
            self.projectile.append(L2Projectile.Projectile(self.screen, self.x,
                                                           self.y, air_x, air_y, False, False))

    def hit_by(self, projectile):
        hitbox = pygame.Rect(self.x - self.image.get_width() / 2, self.y - (self.image.get_height() / 2) - 5, self.image.
                             get_width(), self.image.get_height())
        return hitbox.collidepoint(projectile.x, projectile.y)







