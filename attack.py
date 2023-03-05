import pygame


class Splash(pygame.sprite.Sprite):
    def __init__(self, screen, player):
        super(Splash, self).__init__()
        self.screen = screen
        # self.rect = pygame.Rect(0, 0, 2, 50)
        # self.color = (255, 255, 255)
        self.image = pygame.image.load('images/AttackModel.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.speed = 20.5
        self.rect.x = player.rect.x
        self.rect.top = player.rect.top
        self.x = float(self.rect.x)

    def update(self):
        self.x += self.speed
        self.rect.x = self.x

    # def draw_splash(self):
    #     pygame.draw.rect(self.screen, self.color,  self.rect)
    def draw_splash(self):
        self.screen.blit(self.image, self.rect)
