import time
import pygame
#Colby Donner
mainClock = pygame.time.Clock()

pygame.init()
pygame.display.set_caption('Game Base')
screen = pygame.display.set_mode((1000, 750), 0, 32)
image1 = pygame.image.load('NewLevel2Background.png')
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


draw_text('You have defeated all the enemies and saved humanity!', font, white, screen, 45, 80)
draw_text('To your surprise, the aliens decided to bring a human', font, white, screen, 45, 120)
draw_text('back with them, who is luckily of your opposite gender.', font, white, screen, 45, 160)
draw_text('You both go back to Earth and restart humanity!', font, white, screen, 45, 200)
draw_text('Great job alumni! The hard job starts now.', font, white, screen, 45, 240)
draw_text('Thank you for playing our game, hope you had fun!', font, white, screen, 45, 300)

time.sleep(3)