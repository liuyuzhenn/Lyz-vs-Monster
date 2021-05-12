import pygame


class Me(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = pygame.image.load(r'.\images\myhead.png').convert_alpha()
        self.image2 = pygame.image.load(r'.\images\myhead2.png').convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load(r'.\images\me_destroy_1.png').convert_alpha(),
            pygame.image.load(r'.\images\me_destroy_2.png').convert_alpha(),
            pygame.image.load(r'.\images\me_destroy_3.png').convert_alpha(),
            pygame.image.load(r'.\images\me_destroy_4.png').convert_alpha(),
            ])
        self.live = True
        self.rect = self.image1.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.center = (100, bg_size[1] // 2)
        self.speed = 7
        self.mask = pygame.mask.from_surface(self.image1)

    def move_up(self):
        self.rect.top -= self.speed
        if self.rect.top < 0:
            self.rect.top = 0

    def move_down(self):
        self.rect.bottom += self.speed
        if self.rect.bottom > self.height:
            self.rect.bottom = self.height

    def move_left(self):
        self.rect.left -= self.speed
        if self.rect.left < 0:
            self.rect.left = 0

    def move_right(self):
        self.rect.right += self.speed
        if self.rect.right > self.width:
            self.rect.right = self.width


