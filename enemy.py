import pygame


class Monster(pygame.sprite.Sprite):
    """Всё о монстрах :D"""

    def __init__(self, screen):
        super(Monster, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/monster2.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width = 1300
        self.rect.y = self.rect.height = 20
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.speed = 1.5

        self.images = []
        self.images.append(pygame.image.load('images/monster.png'))
        self.images.append(pygame.image.load('images/monster.png'))
        self.images.append(pygame.image.load('images/monster.png'))
        self.images.append(pygame.image.load('images/monster2.png'))
        self.images.append(pygame.image.load('images/monster2.png'))
        self.images.append(pygame.image.load('images/monster2.png'))
        self.images.append(pygame.image.load('images/monsterpoz2.png'))
        self.images.append(pygame.image.load('images/monsterpoz2.png'))
        self.images.append(pygame.image.load('images/monsterpoz2.png'))
        self.images.append(pygame.image.load('images/monsterpoz3.png'))
        self.images.append(pygame.image.load('images/monsterpoz3.png'))
        self.images.append(pygame.image.load('images/monsterpoz3.png'))
        self.index = 0
        self.image = self.images[self.index]

    def monsterDraw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        self.x -= self.speed
        self.rect.x = self.x