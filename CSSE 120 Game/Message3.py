import time
import pygame
#Colby Donner
mainClock = pygame.time.Clock()

pygame.init()
pygame.display.set_caption('Game Base')
screen = pygame.display.set_mode((1000, 750), 0, 32)
image1 = pygame.image.load('NewLevel3Background.png')
font = pygame.font.SysFont('None', 50)
font2 = pygame.font.SysFont('None', 30)
white = (255, 255, 255)

Black = (0, 0, 0)



screen.blit(image1, (0, 0))
def draw_text(text, font, color, surface, x, y):
    mainClock.tick(60)
    for char in text:

        textobj = font.render(char, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)

        textrect.center = (x, y)
        x += textrect.width
        time.sleep(0.01)
        surface.blit(textobj, textrect.center)
        pygame.display.update()


draw_text('You are now at the space station and everyone is dead,', font, white, screen, 20, 80)
draw_text('so you have access to a spaceship. Luckily you know', font, white, screen, 20, 120)
draw_text('how to fly one because you went to Rose-Hulman, so off', font, white, screen, 20, 160)
draw_text('you are to the moon, Enemies will be waiting for you!', font, white, screen, 20, 200)
time.sleep(3)