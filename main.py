import pygame
import sys

from settings import *
from player import Player
from enemy import Enemy
from level import Level
from levels import LEVELS

pygame.init()

screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)

pygame.display.set_caption(
    "Coin Adventure"
)

clock = pygame.time.Clock()

font = pygame.font.SysFont(
    None,
    30
)

current_level = 1

player = Player()

level = Level(
    current_level
)

enemies = []

for x, y in LEVELS[current_level]["enemies"]:

    enemies.append(
        Enemy(
            x,
            y,
            LEVELS[current_level]["enemy_speed"]
        )
    )

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    player.move(keys)

    if keys[pygame.K_SPACE]:
        player.jump(level.platform)

    player.update(level.platform)

    for enemy in enemies:

        enemy.move()

        if player.rect.colliderect(enemy.rect):

            print("GAME OVER")
            running = False

    level.check_coins(player)

    if level.check_goal(player):

        current_level += 1

        if current_level > 3:

            print("YOU BEAT THE GAME!")
            running = False

        else:

            level = Level(current_level)

            enemies = []

            for x, y in LEVELS[current_level]["enemies"]:

                enemies.append(
                    Enemy(
                        x,
                        y,
                        LEVELS[current_level]["enemy_speed"]
                    )
                )

            player.rect.x = 100
            player.rect.y = 300

    level.draw(screen)

    player.draw(screen)

    for enemy in enemies:

        enemy.draw(screen)

    score_text = font.render(
        f"Level: {current_level}  Score: {level.score}",
        True,
        (255, 255, 255)
    )

    screen.blit(
        score_text,
        (10, 10)
    )

    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
sys.exit()
