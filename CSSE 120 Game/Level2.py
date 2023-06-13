import random
import pygame
import sys
import L2Airplane
import L2Enemy
import L2LifeCount
import L2Background
import L2SpeedPowerup
from pygame.locals import *

# Abe Gizaw
# hit = 0
# spawn = random.randint(50, 325)
# powerup_used = False
# speed_increase = False
# speed_powerup = L2Powerup.Powerup(screen)
pygame.init()
screen = pygame.display.set_mode((1000, 750))
click = False


def level_2():
    pygame.init()
    clock = pygame.time.Clock()
    ticks = 0
    hit = 0
    spawn = random.randint(50, 325)
    pygame.display.set_caption("Level 2!")
    screen = pygame.display.set_mode((1000, 750))
    background = L2Background.Background(screen)
    air = L2Airplane.Airplane(screen, 200, 200, False)
    life_count = L2LifeCount.LifeCount(screen, 5)
    enemy_image = pygame.image.load('Enemy.png')
    game_over_image = pygame.image.load('Game_Over3.png')
    game_won_image = pygame.image.load('L2Levelcomplete.png')
    game_is_over = False
    game_won = False
    enemy_list = []
    speed_powerup = L2SpeedPowerup.Powerup(screen, air)
    crosshair = pygame.image.load('crosshair.png').convert_alpha()
    BLACK = (0, 0, 0)
    crosshair.set_colorkey(BLACK)
    crosshairx, crosshairy = crosshair.get_width() // 2, crosshair.get_height() // 2
    powerup_used = False
    speed_increase = False

    for k in range(20):
        enemy = L2Enemy.Enemy(screen, random.randint(screen.get_width() - 320, screen.get_width() - enemy_image.
                                                     get_width()), random.randint(50, screen.get_height() - enemy_image.
                                                                                  get_height() - 50), 0)
        enemy_list.append(enemy)

    while True:
        pressed_keys = pygame.key.get_pressed()
        clock.tick(60)
        ticks += 1
        for event in pygame.event.get():
            mouse_press = pygame.mouse.get_pressed(3)
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    paused()
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and mouse_press[0]:
                air.fire(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        for j in range(len(enemy_list) - 1, -1, -1):
            if enemy_list[j].hit_count > 0:
                del enemy_list[j]
        posx, posy = pygame.mouse.get_pos()

        if game_is_over is True:
            screen.blit(game_over_image, ((screen.get_width() - game_over_image.get_width()) / 2,
                                          (screen.get_height() - game_over_image.get_height()) / 2))
            pygame.display.update()
            if pressed_keys[pygame.K_SPACE]:
                return level_2()
            continue

        if game_won is True:
            screen.blit(game_won_image, ((screen.get_width() - game_won_image.get_width()) / 2,
                                         (screen.get_height() - game_won_image.get_height()) / 2))
            pygame.display.update()
            if pressed_keys[pygame.K_SPACE]:
                run = False
                if not run:
                    return True
            continue

        screen.fill((0, 200, 250))
        background.draw()
        air.draw()
        pressed_keys = pygame.key.get_pressed()

        # Inital Movement
        if pressed_keys[pygame.K_LEFT] and air.x > -air.image.get_width() / 2:
            air.x -= 5

        if air.x < screen.get_width() - 400:
            if pressed_keys[pygame.K_RIGHT] and air.x < screen.get_width() - air.image.get_width() / 2:
                air.x += 5

        if pressed_keys[pygame.K_DOWN] and air.y < screen.get_height() - air.image.get_height() / 2:
            air.y += 5

        if pressed_keys[pygame.K_UP] and air.y > -air.image.get_height() / 2:
            air.y -= 5

        # Powerup
        if spawn <= ticks <= (spawn * 2):
            if powerup_used is False:
                speed_powerup.draw()
            if air.hit_by(speed_powerup):
                hit = ticks
                speed_increase = True
                powerup_used = True
        if powerup_used is True and hit <= ticks <= hit + 200:
            air.powerup_in_use = True
        else:
            air.powerup_in_use = False
        if speed_increase is True and hit <= ticks <= hit + 200:
            if pressed_keys[pygame.K_LEFT] and air.x > -air.image.get_width() / 2:
                air.x -= 7.5

            if air.x < screen.get_width() - 400:
                if pressed_keys[pygame.K_RIGHT] and air.x < screen.get_width() - air.image.get_width() / 2:
                    air.x += 7.5

            if pressed_keys[pygame.K_DOWN] and air.y < screen.get_height() - air.image.get_height() / 2:
                air.y += 7.5

            if pressed_keys[pygame.K_UP] and air.y > -air.image.get_height() / 2:
                air.y -= 7.5

        # Projectiles and enemies
        for projectile in air.projectile:
            projectile.draw()
            projectile.move()
        for k in range(len(enemy_list)):
            enemy_list[k].draw()
            enemy_list[k].move()
        if ticks % 23 == 0:
            if len(enemy_list) > 0:
                for k in range(2):
                    enemy_list[random.randint(0, len(enemy_list) - 1)].shoot(air.x, air.y)
        for enemy in enemy_list:
            for projectile in enemy.projectile:
                projectile.move()
                projectile.draw()
        for k in range(len(air.projectile) - 1, -1, -1):
            for enemy in enemy_list:
                if enemy.hit_by(air.projectile[k]):
                    enemy.hit_count += 1
                    del air.projectile[k]
                    break
        for enemy in enemy_list:
            for k in range(len(enemy.projectile) - 1, -1, -1):
                if air.hit_by(enemy.projectile[k]):
                    del enemy.projectile[k]
                    if air.lives > 0:
                        life_count.lives -= 1
                        air.lives -= 1

        life_count.draw()

        if air.lives == 0:
            game_is_over = True
        pygame.mouse.set_visible(False)
        screen.blit(crosshair, (posx - crosshairx, posy - crosshairy))

        if len(enemy_list) == 0:
            game_won = True

        pygame.display.update()


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def paused():
    font = pygame.font.SysFont('None', 70)
    font2 = pygame.font.SysFont('None', 30)
    white = (255, 255, 255)

    pygame.mouse.set_visible(True)

    while True:
        click = False
        draw_text('Paused', font, white, screen, 415, 92)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return True
            if event.type == MOUSEBUTTONDOWN:
                click = True
        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(50, 150, 200, 50)
        bx, by = button_1.center

        button_2 = pygame.Rect(50, 200, 200, 50)
        bx2, by2 = button_2.center
        draw_text('Resume Level', font2, white, screen, bx - 55, by - 10)
        draw_text('Return to Main Menu', font2, white, screen, bx2 - 55, by2 - 10)
        if button_1.collidepoint(mx, my):
            draw_text('Resume Level', font2, (0, 0, 0), screen, bx - 55, by - 10)
            if click:
                return True
        if button_2.collidepoint(mx, my):
            draw_text('Return to Main Menu', font2, (0, 0, 0), screen, bx2 - 55, by2 - 10)
            if click:
                pygame.mouse.set_visible(True)
                import Interface
                Interface.main_menu()

        pygame.display.update()
