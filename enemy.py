import pygame
from random import *


class monster1(pygame.sprite.Sprite):
    HP = 2

    def __init__(self, bg_size):
        self.angle = 0
        pygame.sprite.Sprite.__init__(self)
        self.destroy_index = 0
        if choice([True, False]):
            self.image = pygame.image.load(r'.\images\small1.png').convert_alpha()
            self.image_hit = pygame.image.load(r'.\images\small1_hit.png').convert_alpha()
        else:
            self.image = pygame.image.load(r'.\images\small2.png').convert_alpha()
            self.image_hit = pygame.image.load(r'.\images\small2_hit.png').convert_alpha()

        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load(r'.\images\enemy1_down1.png').convert_alpha(),
            pygame.image.load(r'.\images\enemy1_down2.png').convert_alpha(),
            pygame.image.load(r'.\images\enemy1_down3.png').convert_alpha(),
            pygame.image.load(r'.\images\enemy1_down4.png').convert_alpha()
        ])
        self.rect = self.image.get_rect()
        self.live = True
        self.width, self.height = bg_size[0], bg_size[1]
        centx = randint(self.width + 100, self.width * 3)
        centy = randint(self.rect.height // 2, self.height - self.rect.height // 2)
        self.rect.center = (centx, centy)
        self.speed = 3
        self.mask = pygame.mask.from_surface(self.image)
        self.HP =monster1.HP

        self.add_score_font = pygame.font.Font(r'.\font\font.ttf', self.rect.width // 3)
        self.add_score_count = 0

    def move(self):
        self.angle += 4
        self.rect.right -= self.speed
        if self.rect.right < 0:
            self.reset()

    def reset(self):
        self.destroy_index = 0
        self.add_score_count = 0
        self.live = True
        centx = randint(self.width + 100, self.width * 3)
        centy = randint(self.rect.height // 2, self.height - self.rect.height // 2)
        self.rect.center = (centx, centy)


class monster2(pygame.sprite.Sprite):
    HP = 10
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.destroy_index = 0
        self.image1 = pygame.image.load(r'.\images\mid1.png').convert_alpha()
        self.image2 = pygame.image.load(r'.\images\mid2.png').convert_alpha()
        self.image_hit = pygame.image.load(r'.\images\mid_hit.png').convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([ \
            pygame.image.load(r'.\images\enemy2_down1.png').convert_alpha(),
            pygame.image.load(r'.\images\enemy2_down2.png').convert_alpha(),
            pygame.image.load(r'.\images\enemy2_down3.png').convert_alpha(),
            pygame.image.load(r'.\images\enemy2_down4.png').convert_alpha()
        ])

        self.HP = monster2.HP
        self.live = True
        self.rect = self.image1.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        centx = randint(self.width + 100, self.width * 2)
        centy = randint(self.rect.height // 2, self.height - self.rect.height // 2)
        self.rect.center = (centx, centy)
        self.speed = 2
        self.mask = pygame.mask.from_surface(self.image1)

        self.add_score_font = pygame.font.Font(r'.\font\font.ttf', self.rect.width // 3)
        self.add_score_count = 0

    def move(self):
        self.rect.right -= self.speed
        if self.rect.right < 0:
            self.reset()

    def reset(self):
        self.add_score_count = 0
        self.destroy_index = 0
        self.HP = monster2.HP
        self.live = True
        centx = randint(self.width + 100, self.width * 3)
        centy = randint(self.rect.height // 2, self.height - self.rect.height // 2)
        self.rect.center = (centx, centy)


class monster3(pygame.sprite.Sprite):
    HP = 30
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.destroy_index = 0
        self.image1 = pygame.image.load(r'.\images\big1.png').convert_alpha()
        self.image2 = pygame.image.load(r'.\images\big2.png').convert_alpha()
        self.image3 = pygame.image.load(r'.\images\big3.png').convert_alpha()
        self.image4 = pygame.image.load(r'.\images\big4.png').convert_alpha()
        self.image_hit = pygame.image.load(r'.\images\big_hit.png').convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load(r'.\images\enemy3_down1.png').convert_alpha(),
            pygame.image.load(r'.\images\enemy3_down2.png').convert_alpha(),
            pygame.image.load(r'.\images\enemy3_down3.png').convert_alpha(),
            pygame.image.load(r'.\images\enemy3_down4.png').convert_alpha(),
            pygame.image.load(r'.\images\enemy3_down5.png').convert_alpha(),
            pygame.image.load(r'.\images\enemy3_down6.png').convert_alpha()
        ])
        self.live = True
        self.rect = self.image1.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        centx = randint(self.width * 2, self.width * 3)
        centy = randint(self.rect.height // 2, self.height - self.rect.height // 2)
        self.rect.center = (centx, centy)
        self.speed = 1
        self.mask = pygame.mask.from_surface(self.image1)
        self.HP = monster3.HP

        self.add_score_font = pygame.font.Font(r'.\font\font.ttf', self.rect.width // 8)
        self.add_score_count = 0

    def move(self):
        self.rect.right -= self.speed
        if self.rect.right < 0:
            self.reset()

    def reset(self):
        self.destroy_index = 0
        self.add_score_count = 0
        self.HP = monster3.HP
        self.live = True
        centx = randint(self.width * 2, self.width * 3)
        centy = randint(self.rect.height // 2, self.height - self.rect.height // 2)
        self.rect.center = (centx, centy)
