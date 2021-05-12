import pygame


class Bullet1(pygame.sprite.Sprite):
    harm = 1
    form = 1
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r'.\images\super.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.speed = 10
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.right += self.speed
        if self.rect.left > 1280:
            self.active = False

    def reset(self, position):
        self.active = True
        self.rect.center = position

    def change2(self):
        self.image = pygame.image.load(r'.\images\fireball.png').convert_alpha()
        self.rect = self.image.get_rect()

    def change4(self):
        self.image = pygame.image.load(r'.\images\bullet4.png').convert_alpha()
        self.rect = self.image.get_rect()

    def change6(self):
        self.image = pygame.image.load(r'.\images\starbullet.png').convert_alpha()
        self.rect = self.image.get_rect()
