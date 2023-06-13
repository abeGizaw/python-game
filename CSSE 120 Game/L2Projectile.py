import pygame
import math

# Abe Gizaw
def get_distance_from(x_1, y_1, x_2, y_2):
    return math.dist((x_1, y_1), (x_2, y_2))

class Projectile:
    def __init__(self, screen, x, y, click_x, click_y, hero, powerup_instance):
        self.screen = screen
        self.x = x
        self.y = y
        self.click_x = click_x
        self.click_y = click_y
        self.speed = 10
        self.image = pygame.image.load('L2fighterjet.png')
        if get_distance_from(self.x + self.image.get_width(), self.y + (self.image.get_height() / 2), self.click_x, self.click_y) != 0:
            self.x_speed = (self.speed * (self.click_x - (self.x + self.image.get_width()))) / get_distance_from(
            self.x + self.image.get_width(), self.y + (self.image.get_height() / 2), self.click_x, self.click_y)
        if get_distance_from(self.x + self.image.get_width(), self.y + (self.image.get_height() / 2), self.click_x, self.click_y) != 0:
            self.y_speed = (self.speed * (self.click_y - (self.y + self.image.get_height() / 2))) / get_distance_from(
            self.x + self.image.get_width(), self.y + (self.image.get_height() / 2), self.click_x, self.click_y)
        self.lives = 5
        self.hero = hero
        self.powerup_in_use = powerup_instance

    def draw(self):
        if self.hero is True:
            pygame.draw.line(self.screen, (0, 255, 0), (self.x + self.image.get_width(), self.y +
            self.image.get_height  () // 2), (self.x + self.image.get_width() + 8, self.y + self.image.get_height() // 2), 4)
        if self.hero is False:
            pygame.draw.line(self.screen, (255, 0, 0),
                             (self.x + self.image.get_width(), self.y + self.image.get_height
                             () // 2), (self.x + self.image.get_width() + 8, self.y + self.image.get_height() // 2), 4)

    def move(self):
        if self.powerup_in_use == False:
            self.x += self.x_speed
            self.y += self.y_speed

        if self.powerup_in_use == True:
            self.x += 2 * self.x_speed
            self.y += 2 * self.y_speed
