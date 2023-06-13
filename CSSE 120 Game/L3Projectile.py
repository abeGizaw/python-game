import math, pygame

#Colby Donner
def get_distance_from(x_1, y_1, x_2, y_2):
    return math.dist((x_1, y_1), (x_2, y_2))

class Projectiles:
    def __init__(self, screen, x, y, click_x, click_y, powerup_instance):
        self.screen = screen
        self.x = x
        self.y = y
        self.click_x = click_x
        self.click_y = click_y
        self.speed = 10
        self.image = pygame.image.load('spaceship2inv.png')
        if get_distance_from(self.x + self.image.get_width(), self.y + (self.image.get_height() / 2), self.click_x,
                             self.click_y) != 0:
            self.x_speed = (self.speed * (self.click_x - (self.x + self.image.get_width()))) / get_distance_from(
            self.x + self.image.get_width() / 2, self.y + (self.image.get_height()), self.click_x -
                                                    self.image.get_width() / 2, self.click_y + self.image.get_height())
        if get_distance_from(self.x + self.image.get_width(), self.y + (self.image.get_height() / 2), self.click_x,
                             self.click_y) != 0:
            self.y_speed = (self.speed * (self.click_y - (self.y + self.image.get_height()))) / get_distance_from(
            self.x + self.image.get_width() / 2, self.y + (self.image.get_height()), self.click_x -
                                                        self.image.get_width() / 2, self.click_y)
        self.lives = 5
        self.powerup_in_use = powerup_instance
    def draw(self):
        start_pos = self.x + self.image.get_width() // 2, self.y - 8
        end_pos = self.x + self.image.get_width() // 2, self.y
        pygame.draw.line(self.screen, (250, 250, 250), start_pos, end_pos, 5)
    def move(self):
        if self.powerup_in_use == False:
            self.x += self.x_speed
            self.y += self.y_speed

        if self.powerup_in_use == True:
            self.x += 2 * self.x_speed
            self.y += 2 * self.y_speed