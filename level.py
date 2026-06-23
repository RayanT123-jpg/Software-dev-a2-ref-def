import pygame
import os

from settings import *
from levels import LEVELS


class Level:

    def __init__(self, level_number):

        self.level_number = level_number
        self.data = LEVELS[level_number]

        # Ground platform
        self.platform = pygame.Rect(
            0,
            350,
            WIDTH,
            50
        )

        # Goal area
        self.goal = pygame.Rect(
            750,
            300,
            30,
            50
        )

        # Background
        self.background = pygame.image.load(
            os.path.join(
                ASSET_PATH,
                "background.png"
            )
        )

        self.background = pygame.transform.scale(
            self.background,
            (WIDTH, HEIGHT)
        )

        # Coin image
        self.coin_image = pygame.image.load(
            os.path.join(
                ASSET_PATH,
                "coin.png"
            )
        )

        self.coin_image = pygame.transform.scale(
            self.coin_image,
            (20, 20)
        )

        # Create coins for this level
        self.coins = []

        for x, y in self.data["coins"]:

            coin_rect = pygame.Rect(
                x,
                y,
                20,
                20
            )

            self.coins.append(
                coin_rect
            )

        self.score = 0

    def draw(self, screen):

        # Draw background
        screen.blit(
            self.background,
            (0, 0)
        )

        # Draw platform
        pygame.draw.rect(
            screen,
            (0, 255, 0),
            self.platform
        )

        # Draw coins
        for coin in self.coins:

            screen.blit(
                self.coin_image,
                coin
            )

        # Draw goal
        pygame.draw.rect(
            screen,
            (0, 0, 255),
            self.goal
        )

    def check_coins(self, player):

        for coin in self.coins[:]:

            if player.rect.colliderect(coin):

                self.coins.remove(
                    coin
                )

                self.score += 1

    def level_complete(self):

        return len(self.coins) == 0

    def check_goal(self, player):

        return (
            player.rect.colliderect(
                self.goal
            )
            and
            self.level_complete()
        )
