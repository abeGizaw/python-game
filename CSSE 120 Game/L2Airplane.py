import L2Projectile
import pygame
# Abe Gizaw
class Airplane:
    def __init__(self, screen, x, y, powerup_instance):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load('L2fighterjet.png')
        self.image.set_colorkey((225, 225, 225))
        self.projectile = []
        self.lives = 5
        self.powerup_in_use = powerup_instance





    def fire(self, click_x, click_y):
        new_missile = L2Projectile.Projectile(self.screen, self.x, self.y, click_x, click_y, True, self.powerup_in_use)
        self.projectile.append(new_missile)

    def draw(self):
        white = (255, 255, 255)
        self.image.set_colorkey(white)
        self.screen.blit(self.image, (self.x, self.y))

    def hit_by(self, projectile):
       hitbox = pygame.Rect(self.x - self.image.get_width() / 2, self.y - self.image.get_height() / 2, self.image.get_width(), self.image.get_height())

       return hitbox.collidepoint(projectile.x, projectile.y)


