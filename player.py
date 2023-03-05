import pygame
from pygame.sprite import Sprite


class PlayerOBJ(Sprite):

    def __init__(self, screen):
        """Инициализация модельки игрока"""
        super(PlayerOBJ, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/PM0.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.x = 30
        self.rect.y = 650  # 01010101
        self.center = float(self.rect.x)
        self.centery = float(self.rect.y)
        self.rect.bottom = self.screen_rect.bottom

        self.images = []
        self.images.append(pygame.image.load('images/PM0.png'))
        self.images.append(pygame.image.load('images/PM1.png'))
        self.images.append(pygame.image.load('images/PM2.png'))
        self.images.append(pygame.image.load('images/PM3.png'))
        self.images.append(pygame.image.load('images/PM3.png'))
        self.images.append(pygame.image.load('images/PM2.png'))
        self.images.append(pygame.image.load('images/PM1.png'))
        self.images.append(pygame.image.load('images/PM0.png'))
        self.images.append(pygame.image.load('images/PMdeath.png'))
        self.index = 0
        self.image = self.images[self.index]

        self.moveRight = False
        self.moveLeft = False
        self.moveUp = False  # 01010101
        self.moveDown = False

    def output(self):
        self.screen.blit(self.image, self.rect)

    def update_player(self):
        self.index += 1
        if self.index >= len(self.images) or self.index == 8:
            self.index = 0

        if self.moveRight and self.rect.right < self.screen_rect.right:
            self.center += 4.5 # 4.5
            self.image = self.images[self.index]

        if self.moveLeft and self.rect.left > 0:
            self.center -= 5.5 # 5.5
            self.image = self.images[self.index]

        if self.moveUp and self.centery < 750 and self.centery > 10:
            self.centery -= 5 # 5
            self.image = self.images[self.index]

        if self.moveDown and self.centery < 690:
            self.centery += 5 # 5
            self.image = self.images[self.index]

        self.rect.x = self.center
        self.rect.y = self.centery

    def create_player(self):
        self.center = self.screen_rect.x

    def update_model(self, num, screen):
        self.image = self.images[8]

        # if num == 2:
        #     self.image = pygame.image.load('images/PlayerModel2.png')
        #     self.rect = self.image.get_rect()
        #     self.screen_rect = screen.get_rect()
        # elif num == 1:
        #     self.image = pygame.image.load('images/PlayerModel3.png')
        #     self.rect = self.image.get_rect()
        #     self.screen_rect = screen.get_rect()
