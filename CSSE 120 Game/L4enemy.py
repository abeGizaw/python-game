import pygame
import math
import L4Projectile
#Abe Gizaw and Ben lyons
def sign(number):
    if number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return 0

class Enemy:
    def __init__(self, screen, x, y, lives, shoot_speed):
        self.screen = screen
        self.x = x
        self.y = y
        self.x_speed = 0
        self.y_speed = 0
        self.image = pygame.image.load("Enemy.png")
        self.image.set_colorkey((0, 0, 0))
        self.lives = lives
        self.shoot_speed = shoot_speed
        self.projectiles = []
        self.last_location_not_moving = (x, y)

    def draw(self):
        self.screen.blit(self.image, (self.x - self.image.get_width() / 2,
                                      self.y - self.image.get_height() / 2))

    def move(self, ground_level):
        if self.image.get_width() / 2 <= self.x + self.x_speed <= self.screen.get_width() - (self.image.get_width() / 2) \
                and self.image.get_height() / 2 <= self.y + self.y_speed <= (ground_level / 2) - (
                self.image.get_height() / 2):
            self.x += self.x_speed
            self.y += self.y_speed

    def shoot(self, person_x, person_y):
        dist = math.dist((self.x, self.y), (person_x, person_y))
        if dist != 0:
            self.projectiles.append(L4Projectile.Projectile(self.screen, self.x,
                                                            self.y, self.shoot_speed * (person_x - self.x) / dist,
                                                            self.shoot_speed * (person_y - self.y) / dist, False))

    def hit_by(self, projectile):
        hitbox = pygame.Rect(self.x - self.image.get_width() / 2, self.y - self.image.get_height() / 2,
                             self.image.get_width(), self.image.get_height())
        return hitbox.collidepoint(projectile.x, projectile.y)

    def within_range(self, projectile):
        hitbox = pygame.Rect(self.x - 3 * self.image.get_width() / 2, self.y - 3 * self.image.get_height() / 2,
                             3 * self.image.get_width(), 3 * self.image.get_height())
        return hitbox.collidepoint(projectile.x, projectile.y)

    def will_get_hit_by(self, projectile, ground_level):
        for point in projectile.get_future_positions(ground_level):
            if self.x - self.image.get_width() / 2 <= point[0] <= self.x + self.image.get_width() / 2 and self.y - self.image.get_height() / 2 <= point[1] <= self.y + self.image.get_height() / 2:
                return True
        return False

    def get_closest_edge(self, ground_level):
        list_of_distances = []
        distance_from_left_edge = self.last_location_not_moving[0]
        distance_from_right_edge = self.screen.get_width() - self.last_location_not_moving[0]
        distance_from_top_edge = self.last_location_not_moving[1]
        distance_from_bottom_edge = (ground_level / 2) - self.last_location_not_moving[1]
        list_of_distances.append(distance_from_left_edge)
        list_of_distances.append(distance_from_right_edge)
        list_of_distances.append(distance_from_top_edge)
        list_of_distances.append(distance_from_bottom_edge)
        minimum_index = 0
        minimum_distance = list_of_distances[0]
        for k in range(1, len(list_of_distances)):
            if list_of_distances[k] < minimum_distance:
                minimum_distance = list_of_distances[k]
                minimum_index = k
        if minimum_index == 0:
            return [-1, 0]
        elif minimum_index == 1:
            return [1, 0]
        elif minimum_index == 2:
            return [0, -1]
        else:
            return [0, 1]

    def update_last_location_not_moving(self):
        if self.x_speed == 0 and self.y_speed == 0:
            self.last_location_not_moving = (self.x, self.y)
