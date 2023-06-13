import pygame

# Ben Lyons
class L1Projectile:
    def __init__(self, screen, x, y, x_speed, y_speed, powerup_instance):
        self.screen = screen
        self.x = x
        self.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.has_exploded = False
        self.powerup_in_use = powerup_instance

    def draw(self):
        pygame.draw.line(self.screen, (255, 255, 255), (self.x, self.y - 4), (self.x, self.y + 4), 4)

    def move(self):
        if self.powerup_in_use == False:
            self.x += self.x_speed
            self.y += self.y_speed

        if self.powerup_in_use == True:
            self.x += 2 * self.x_speed
            self.y += 2 * self.y_speed

    def off_screen(self):
        return self.x < 0 or self.x > self.screen.get_width() or self.y < 0 or self.y > self.screen.get_height()
