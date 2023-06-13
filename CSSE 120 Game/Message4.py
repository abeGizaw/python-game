import time
import pygame
#Colby Donner
mainClock = pygame.time.Clock()

pygame.init()
pygame.display.set_caption('Game Base')
screen = pygame.display.set_mode((1000, 750), 0, 32)
image1 = pygame.image.load('NewLevel4Background.png')
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


draw_text('You made it to the moon! The enemies here are a lot', font, white, screen, 55, 80)
draw_text('smarter than the ones on Earth. Do you have what it', font, white, screen, 55, 120)
draw_text('takes to defeat them? Only time will tell. Good Luck!', font, white, screen, 55, 160)
time.sleep(3)