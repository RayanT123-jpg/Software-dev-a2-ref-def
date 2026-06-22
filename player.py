import pygame
import os
from settings import *

class Player:

    def __init__(self):

        self.image = pygame.image.load(
            os.path.join(ASSET_PATH, "player.png")
        )

        self.image = pygame.transform.scale(
            self.image,
            (40, 40)
        )

        self.rect = self.image.get_rect(
            topleft=(100, 300)
        )

        self.velocity_y = 0

    def move(self, keys):

        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED

        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED

    def jump(self, platform):

        if self.rect.bottom >= platform.top:
            self.velocity_y = JUMP_FORCE

    def gravity(self):

        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y

    def update(self, platform):

        self.gravity()

        if self.rect.colliderect(platform):

            if self.velocity_y > 0:

                self.rect.bottom = platform.top
                self.velocity_y = 0

    def draw(self, screen):

        screen.blit(
            self.image,
            self.rect
        )
