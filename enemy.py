import pygame
import os
from settings import *

class Enemy:

    def __init__(self, x, y, speed):

        self.image = pygame.image.load(
            os.path.join(
                ASSET_PATH,
                "enemy.png"
            )
        )

        self.image = pygame.transform.scale(
            self.image,
            (40, 40)
        )

        self.rect = self.image.get_rect(
            topleft=(x, y)
        )

        self.direction = speed
        self.start_x = x

    def move(self):

        self.rect.x += self.direction

        if self.rect.x < self.start_x - 100:
            self.direction *= -1

        if self.rect.x > self.start_x + 100:
            self.direction *= -1

    def draw(self, screen):

        screen.blit(
            self.image,
            self.rect
        )
