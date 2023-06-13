import math, L3Spaceship, pygame, sys, L3Enemies, random
import L1Scoreboard
from pygame.locals import *
import L3SpeedPowerup
# import Interface
#Colby Donner

def get_distance_from(x_1, y_1, x_2, y_2):
    return math.dist((x_1, y_1), (x_2, y_2))
pygame.init()
click = False
screen = pygame.display.set_mode((1000, 750))


def Level3():
    pygame.init()
    clock = pygame.time.Clock()
    ticks = 0
    pygame.display.set_caption("Level 3!")
    background = pygame.image.load("NewLevel3Background.png")
    enemy_image = pygame.image.load('Enemy.png')
    environment = 500
    air = L3Spaceship.SpaceShip(screen, 450, 600, 5, False)
    scoreboard = L1Scoreboard.L1Scoreboard(screen, air.lives)
    enemies = []

    level_complete = False
    crosshair = pygame.image.load('crosshair.png').convert_alpha()
    BLACK = (0, 0, 0)
    crosshair.set_colorkey(BLACK)
    crosshairx, crosshairy = crosshair.get_width() // 2, crosshair.get_height() // 2
    for k in range(random.randint(20, 34)):
        enemy = L3Enemies.Enemy1(screen, random.randint(30, screen.get_width() - 30),
                                 random.randint(30, environment // 2), 1, 5)
        enemies.append(enemy)
    for enemy in enemies:
        enemy.x = enemy.x + enemy_image.get_width() / 2
        enemy.y = enemy.y + enemy_image.get_height() / 2
    is_game_over = False
    game_over_image = pygame.image.load("Game_Over3.png")
    level_complete_image = pygame.image.load("L3Levelcomplete.png")
    hit = 0
    spawn = random.randint(50, 325)
    powerup_used = False
    speed_increase = False
    speed_powerup = L3SpeedPowerup.Powerup(screen, air)


    while True:
        clock.tick(60)
        ticks += 1
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            mouse_press = pygame.mouse.get_pressed(3)
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and mouse_press[0]:
                air.fire(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    paused()

        screen.blit(background, (0, 0))
        posx, posy = pygame.mouse.get_pos()
        if is_game_over:
            screen.blit(game_over_image, ((screen.get_width() / 2) - (game_over_image.get_width() / 2),
                                          (screen.get_height() / 2) - (game_over_image.get_height() / 2)))
            pygame.display.update()
            pressed_keys = pygame.key.get_pressed()

            if pressed_keys[pygame.K_SPACE]:
                return Level3()
            continue
        if level_complete:
            screen.blit(level_complete_image, ((screen.get_width() / 2) - (game_over_image.get_width() / 2),
                                          (screen.get_height() / 2) - (game_over_image.get_height() / 2)))
            pygame.display.update()
            pressed_keys = pygame.key.get_pressed()

            if pressed_keys[pygame.K_SPACE]:
                pygame.mouse.set_visible(True)
                # import Interface
                return True

            continue
        air.draw()
        for enemy in enemies:
            enemy.draw()
            enemy.move()
        if ticks % 20 == 0:
            if len(enemies) > 0:
                for k in range(3):
                    enemies[random.randint(0, len(enemies) - 1)].shoot(air.x, air.y)
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT] and air.x > -air.image.get_width() / 2:
            air.x -= 5
        if pressed_keys[pygame.K_RIGHT] and air.x < screen.get_width() - air.image.get_width() / 2:
            air.x += 5
        if pressed_keys[pygame.K_DOWN] and air.y < screen.get_height() - air.image.get_height() / 2:
            air.y += 5
        if pressed_keys[pygame.K_UP] and air.y > 350:
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
            if pressed_keys[pygame.K_RIGHT] and air.x < screen.get_width() - air.image.get_width() / 2:
                air.x += 7.5

            if pressed_keys[pygame.K_DOWN] and air.y < screen.get_height() - air.image.get_height() / 2:
                air.y += 7.5

            if pressed_keys[pygame.K_UP] and air.y > 350:
                air.y -= 7.5

        for projectile in air.projectile:
            projectile.move()
            projectile.draw()
        for k in range(len(air.projectile) - 1, -1, -1):
            for enemy in enemies:
                if enemy.hit_by(air.projectile[k]):
                    enemy.lives -= 1
                    del air.projectile[k]
                    break

        for j in range(len(enemies) - 1, -1, -1):
            if enemies[j].lives <= 0:
                del enemies[j]
        for enemy in enemies:
            for projectile in enemy.projectiles:
                projectile.move()
                projectile.draw()
            for k in range(len(enemy.projectiles) - 1, -1, -1):
                if air.hit_by(enemy.projectiles[k]):
                    if air.lives > 0:
                        air.lives -= 1
                        scoreboard.lives -= 1
                    del enemy.projectiles[k]
                    break
            for k in range(len(enemy.projectiles) - 1, -1, -1):
                if enemy.projectiles[k].off_screen():
                    del enemy.projectiles[k]
                    break
        if air.lives <= 0:
            is_game_over = True
        screen.blit(crosshair, (posx - crosshairx, posy - crosshairy))

        scoreboard.draw()

        if len(enemies) == 0:
            level_complete = True


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




