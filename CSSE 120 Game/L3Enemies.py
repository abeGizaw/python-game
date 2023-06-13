import random
import pygame
import math
import L1Projectile
#Colby Donner

image2 = pygame.image.load("spaceship2inv.png")
image2w = image2.get_width()
class Enemy1:
    def __init__(self, screen, x, y, lives, shoot_speed):
        self.screen = screen
        self.x = x
        self.y = y
        self.orig_x = x
        self.orig_y = y
        self.speed = random.randint(3, 6)
        self.speed2 = random.randint(2, 4)
        self.image = pygame.image.load("Enemy.png")
        self.image.set_colorkey((255, 255, 255))
        self.lives = lives
        self.shoot_speed = shoot_speed
        self.image2 = pygame.image.load("spaceship2inv.png")
        self.projectiles = []
    def move(self):
        self.x += self.speed
        if abs(self.x - self.orig_x) >= 125:
            self.speed = -self.speed
        self.y += self.speed2
        if abs(self.y - self.orig_y) >= 60:
            self.speed2 = -self.speed2


    def draw(self):
        BLACK = (0, 0, 0)
        self.image.set_colorkey(BLACK)
        self.screen.blit(self.image, (self.x - self.image.get_width() / 2 + 40, self.y - self.image.get_height() / 2 +
                                      20))

    def shoot(self, person_x, person_y):
        dist = math.dist((self.x, self.y), (person_x, person_y))
        if dist != 0:
            self.projectiles.append(L1Projectile.L1Projectile(self.screen, self.x + (image2w / 2),
                                                              self.y, self.shoot_speed * (person_x - self.x) / dist,
                                                              self.shoot_speed * (person_y - self.y) / dist, False))

    def hit_by(self, projectile):

        hitbox = pygame.Rect(self.x - self.image.get_width() / 2 , self.y - self.image.get_height() / 2,
                             self.image.get_width(), self.image.get_height())
        return hitbox.collidepoint(projectile.x, projectile.y)
