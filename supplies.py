import pygame
from random import *


class Bomb(pygame.sprite.Sprite):

    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r'.\images\bomb_supply.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.active = False
        self.width, self.height = bg_size[0], bg_size[1]
        centx = self.width * 100
        centy = randint(self.rect.height // 2, self.height - self.rect.height // 2)
        self.rect.center = (centx, centy)
        self.speed = 3
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.right -= self.speed
        if self.rect.right < 0:
            self.active = False

    def reset(self):
        self.active = True
        centx = randint(self.width * 1.5, self.width * 2.5)
        centy = randint(self.rect.height // 2, self.height - self.rect.height // 2)
        self.rect.center = (centx, centy)


class superman(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r'.\images\firesup.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.speed = 5
        self.active = False
        self.width, self.height = bg_size[0], bg_size[1]
        centx = self.width * 100
        centy = randint(self.rect.height // 2, self.height - self.rect.height // 2)
        self.rect.center = (centx, centy)
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.right -= self.speed
        if self.rect.right < 0:
            self.active = False

    def reset(self):
        self.active = True
        centx = randint(self.width * 1.5, self.width * 2.5)
        centy = randint(self.rect.height // 2, self.height - self.rect.height // 2)
        self.rect.center = (centx, centy)
