import pygame
import sys
from pygame.locals import *

import Level1
import Message1
import Level2
import Level3
import Level4

# Colby Donner

mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('The Last Alumni')
screen = pygame.display.set_mode((1000, 750), 0, 32)
image1 = pygame.image.load('MainMenuBackground.png')
font = pygame.font.SysFont('None', 50)
font2 = pygame.font.SysFont('None', 30)
white = (255, 255, 255)
level1img = pygame.image.load('L1hero.png')
level2img = pygame.image.load('L2fighterjet.png')
level3img = pygame.image.load('spaceship2inv.png')
level4img = pygame.image.load('L4astronaut.png')
Black = (0, 0, 0)
level1img.set_colorkey(white)
level2img.set_colorkey(white)
level3img.set_colorkey(Black)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False


def main_menu():
    while True:
        screen.blit(image1, (0, 0))

        click = False
        pygame.mouse.set_visible(True)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                click = True
        draw_text('Main Menu', font, white, screen, 10, 75)
        draw_text('Made by Colby Donner, Ben Lyons, and Abe Gizaw', font2, white, screen, image1.get_width() - 500, 15)
        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(50, 150, 200, 50)
        bx, by = button_1.center

        button_2 = pygame.Rect(50, 200, 200, 50)
        bx2, by2 = button_2.center
        draw_text('Story Mode', font2, white, screen, bx - 55, by - 10)
        draw_text('Level Select', font2, white, screen, bx2 - 55, by2 - 10)
        if button_1.collidepoint(mx, my):
            draw_text('Story Mode', font2, (0, 0, 0), screen, bx - 55, by - 10)
            if click:
                Message1.
                Level2.level_2()
                Level3.Level3()
                Level4.level_4()
        if button_2.collidepoint(mx, my):
            draw_text('Level Select', font2, (0, 0, 0), screen, bx2 - 55, by2 - 10)
            if click:
                Level_Select()
        pygame.display.update()
        mainClock.tick(60)


def Level_Select():
    pygame.mouse.set_visible(False)
    running = True
    click = False
    crosshair = pygame.image.load('crosshair.png').convert_alpha()
    BLACK = (0, 0, 0)
    crosshair.set_colorkey(BLACK)
    while running:
        screen.blit(image1, (0, 0))
        draw_text('Level Select', font, (255, 255, 255), screen, 10, 70)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(50, 150, 200, 50)
        bx, by = button_1.center
        screen.blit(level1img, (160, 140))
        button_2 = pygame.Rect(50, 225, 200, 50)
        bx2, by2 = button_2.center
        screen.blit(level2img, (180, 235))
        button_3 = pygame.Rect(50, 300, 200, 50)
        bx3, by3 = button_3.center
        screen.blit(level3img, (170, 300))
        button_4 = pygame.Rect(50, 375, 200, 50)
        bx4, by4 = button_4.center
        screen.blit(level4img, (180, 380))
        button_5 = pygame.Rect(50, 450, 200, 50)
        bx5, by5 = button_5.center
        draw_text('Level 1', font2, white, screen, bx - 55, by - 10)
        draw_text('Level 2', font2, white, screen, bx2 - 55, by2 - 10)
        draw_text('Level 3', font2, white, screen, bx3 - 55, by3 - 10)
        draw_text('Level 4', font2, white, screen, bx4 - 55, by4 - 10)
        draw_text('Back', font2, white, screen, bx5 - 55, by5 - 10)
        if button_1.collidepoint(mx, my):
            draw_text('Level 1', font2, BLACK, screen, bx - 55, by - 10)
            if click:
                Level1.level_1()

        if button_2.collidepoint(mx, my):
            draw_text('Level 2', font2, BLACK, screen, bx2 - 55, by2 - 10)
            if click:
                Level2.level_2()
        if button_3.collidepoint(mx, my):
            draw_text('Level 3', font2, BLACK, screen, bx3 - 55, by3 - 10)
            if click:
                Level3.Level3()
        if button_4.collidepoint(mx, my):
            draw_text('Level 4', font2, BLACK, screen, bx4 - 55, by4 - 10)
            if click:
                Level4.level_4()
        if button_5.collidepoint(mx, my):
            draw_text('Back', font2, BLACK, screen, bx5 - 55, by5 - 10)
            if click:
                main_menu()
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()
            if event.type == MOUSEBUTTONDOWN:
                click = True

        screen.blit(crosshair, (mx - 20, my - 20))
        pygame.display.update()
        mainClock.tick(60)


main_menu()
