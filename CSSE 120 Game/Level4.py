import pygame, sys
import L4Person
import L4Scoreboard
import L4enemy
import L4environment
import random
import L1SpeedPowerup

from pygame.locals import *
#Abe Gizaw and Ben lyons
pygame.init()
screen = pygame.display.set_mode((1000, 750))
click = False
def sign(number):
    if number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return 0


def level_4():
    pygame.init()
    clock = pygame.time.Clock()
    ticks = 0
    h = 2
    speed = 5
    pygame.display.set_caption("Level 4")
    screen = pygame.display.set_mode((1000, 750))
    environment = L4environment.Environment(screen, 0.1, 700)
    person = L4Person.Person(screen, 0, environment.ground_level, 6, 5, 8, False)
    person.x += person.image.get_width() / 2
    person.y -= person.image.get_height() / 2
    scoreboard = L4Scoreboard.Scoreboard(screen, person.lives)
    enemies = []
    dead_enemy_list = []
    for k in range(1):
        enemy = L4enemy.Enemy(screen, random.randint(100, screen.get_width() - 100),
                              random.randint(100, environment.ground_level // 2), 1, 5)
        enemies.append(enemy)
    for enemy in enemies:
        enemy.x -= enemy.image.get_width() / 2
        enemy.y -= enemy.image.get_height() / 2
    is_game_over = False
    is_game_won = False
    game_over_image = pygame.image.load("Game_Over3.png")
    level_complete_image = pygame.image.load("L4Levelcomplete.png")
    crosshair = pygame.image.load('crosshair.png').convert_alpha()
    BLACK = (0, 0, 0)
    crosshair.set_colorkey(BLACK)
    crosshair_x, crosshair_y = crosshair.get_width() / 2, crosshair.get_height() / 2
    hit = 0
    powerup_used = False
    speed_increase = False
    speed_powerup = L1SpeedPowerup.Powerup(screen, person)
    spawn = random.randint(50, 325)
    while True:

        # Initialization
        clock.tick(60)
        ticks += 1
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    paused()
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                person.shoot(pygame.mouse.get_pos()[0],
                             pygame.mouse.get_pos()[1])
        pressed_keys = pygame.key.get_pressed()
        screen.fill((0, 255, 255))
        environment.draw()
        scoreboard.draw()
        person.draw()
        if is_game_won:
            screen.blit(level_complete_image, ((screen.get_width() / 2)
                                               - (level_complete_image.get_width() / 2),
                                               (screen.get_height() / 2)
                                               - (level_complete_image.get_height() / 2)))
            pygame.display.update()
            if pressed_keys[pygame.K_SPACE]:
                return True
            continue
        if is_game_over:
            for enemy in enemies:
                enemy.draw()
                for projectile in enemy.projectiles:
                    projectile.draw()
            for projectile in person.projectiles:
                projectile.draw()
            screen.blit(game_over_image, ((screen.get_width() / 2)
                                          - (game_over_image.get_width() / 2),
                                          (screen.get_height() / 2)
                                          - (game_over_image.get_height() / 2)))
            pygame.display.update()
            if pressed_keys[pygame.K_SPACE]:
                return level_4()
            continue
        if len(enemies) == 0 and is_game_won == False:
            for k in range(h):
                enemy = L4enemy.Enemy(screen, random.randint(100, screen.get_width() - 100),
                                      random.randint(100, environment.ground_level // 2), 1, speed)
                enemies.append(enemy)
                h = h + 1
            speed = speed + 1.5


        # Spot to do enemy projectile dodging.
        for enemy in enemies:
            count_incoming_projectiles = 0
            for k in range(len(person.projectiles) - 1, -1, -1):
                if enemy.will_get_hit_by(person.projectiles[k], environment.ground_level):
                    count_incoming_projectiles += 1
                    if enemy.get_closest_edge(environment.ground_level)[0] != 0:
                        unit1 = enemy.get_closest_edge(environment.ground_level)[0]
                        unit2 = -1 * unit1
                    else:
                        unit2 = -1 * enemy.get_closest_edge(environment.ground_level)[1] * sign(person.projectiles[k].x_speed)
                        unit1 = -1 * unit2
                    enemy.x_speed = unit1 * person.projectiles[k].y_speed
                    enemy.y_speed = unit2 * person.projectiles[k].x_speed
            if count_incoming_projectiles == 0:
                enemy.x_speed = 0
                enemy.y_speed = 0



        # End of spot.

        for enemy in enemies:
            enemy.move(environment.ground_level)
            enemy.draw()
            enemy.update_last_location_not_moving()
        if ticks % 15 == 0:
            if len(enemies) > 0:
                for k in range(len(enemies)):
                    enemies[random.randint(0, len(enemies) - 1)].shoot(person.x, person.y)
        # Person projectile movement
        for projectile in person.projectiles:
            projectile.move()
            projectile.draw()
        for k in range(len(person.projectiles) - 1, -1, -1):
            for enemy in enemies:
                if enemy.hit_by(person.projectiles[k]):
                    enemy.lives -= 1
                    del person.projectiles[k]
                    break
        for k in range(len(person.projectiles) - 1, -1, -1):
            if person.projectiles[k].off_screen() or person.projectiles[k].y > environment.ground_level:
                del person.projectiles[k]
                break

        # Remove dead enemies
        for j in range(len(enemies) - 1, -1, -1):
            if enemies[j].lives <= 0:
                dead_enemy_list.append(enemies[j])
                del enemies[j]

        # Enemy projectile movement
        for enemy in enemies:
            for projectile in enemy.projectiles:
                projectile.move()
                projectile.draw()
            for k in range(len(enemy.projectiles) - 1, -1, -1):
                if person.hit_by(enemy.projectiles[k]):
                    if person.lives > 0:
                        person.lives -= 1
                        scoreboard.lives -= 1
                    del enemy.projectiles[k]
            for k in range(len(enemy.projectiles) - 1, -1, -1):
                if enemy.projectiles[k].off_screen() or enemy.projectiles[k].y > environment.ground_level:
                    del enemy.projectiles[k]

        # Person movement
        if pressed_keys[pygame.K_LEFT] and person.x > person.image.get_width() / 2:
            person.x -= 7
        if pressed_keys[pygame.K_RIGHT] and person.x < screen.get_width() - person.image.get_width() / 2:
            person.x += 7
        if pressed_keys[pygame.K_UP]:
            if person.y_speed >= -6:
                person.y -= person.y_speed
                person.y_speed -= environment.gravity
            else:
                person.y_speed = 6
        if not pressed_keys[pygame.K_UP] and person.y + person.image.get_height() / 2 + 0.01 < environment.ground_level:
            person.y -= person.y_speed
            person.y_speed -= environment.gravity

        # Powerup

        if spawn <= ticks <= (spawn * 2):
            if powerup_used is False:
                speed_powerup.draw()
            if person.hit_by(speed_powerup):
                hit = ticks
                speed_increase = True
                powerup_used = True
        if powerup_used is True and hit <= ticks <= hit + 200:
            person.powerup_in_use = True
        else:
            person.powerup_in_use = False
        if speed_increase is True and hit <= ticks <= hit + 200:
            if pressed_keys[pygame.K_LEFT] and person.x > person.image.get_width() / 2:
                person.x -= 7.5
            if pressed_keys[pygame.K_RIGHT] and person.x < screen.get_width() - person.image.get_width() / 2:
                person.x += 7.5

            spawn = spawn * 3

        # Check for game over
        if person.lives <= 0:
            is_game_over = True

        # Check for win
        if len(dead_enemy_list) == 31:
            is_game_won = True

        pygame.mouse.set_visible(False)
        pos_x, pos_y = pygame.mouse.get_pos()
        screen.blit(crosshair, (pos_x - crosshair_x, pos_y - crosshair_y))
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
