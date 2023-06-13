import math
import pygame
import L3Projectile
#Colby Donner

def get_distance_from(x_1, y_1, x_2, y_2):
    return math.dist((x_1, y_1), (x_2, y_2))
class SpaceShip:
    def __init__(self, screen, x, y, lives, powerup_instance):
        self.screen = screen
        self.x = x
        self.y = y
        self.lives = lives
        self.image = pygame.image.load('spaceship2inv.png').convert_alpha()
        self.image.set_colorkey((225, 225, 225))
        self.projectile = []
        self.powerup_in_use = powerup_instance

    def fire(self, click_x, click_y):
        new_missile = L3Projectile.Projectiles(self.screen, self.x, self.y, click_x + self.image.get_width() / 2,
                                               click_y + self.image.get_height() / 2, self.powerup_in_use)
        self.projectile.append(new_missile)

    def draw(self):
        BLACK = (0, 0, 0)
        self.image.set_colorkey(BLACK)
        self.screen.blit(self.image, (self.x, self.y))
    def hit_by(self, projectile):
        hitbox = pygame.Rect(self.x, self.y ,
                             self.image.get_width() , self.image.get_height())
        return hitbox.collidepoint(projectile.x, projectile.y)


