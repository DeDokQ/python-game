import pygame.font
from player import PlayerOBJ
from pygame.sprite import Group


class Scores():
    """Вывод игровой информации"""

    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect
        self.stats = stats

        self.text_color = (255, 193, 7)
        self.text_high_color = (245, 127, 23)
        self.waves_color = (128,0,0)
        self.font = pygame.font.SysFont("Arial", 60)
        self.font2 = pygame.font.SysFont("Arial", 45)
        self.image_score()
        self.image_high_score()
        self.image_waves()

        self.image_healt(screen)

    def image_score(self):
        """Приобразовывает текст счёта в граф. изображение"""
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color)
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = 1100
        self.score_rect.top = 730

    def image_high_score(self):
        """Вывод максимальный рекод, путем приобразованием"""
        self.image_high_image = self.font.render(str(self.stats.high_score), True, self.text_high_color)
        self.image_high_rect = self.image_high_image.get_rect()
        self.image_high_rect.right = 500
        self.image_high_rect.top = 730

    def image_waves(self):
        self.image_waves_im = self.font2.render(str(self.stats.waves), True, self.waves_color)
        self.image_waves_rect = self.image_waves_im.get_rect()
        self.image_waves_rect.right = 600
        self.image_waves_rect.top = 40

    def show_score(self):
        """Отображение счёта"""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.image_high_image, self.image_high_rect)
        self.screen.blit(self.image_waves_im, self.image_waves_rect)
        self.hearts.draw(self.screen)

    def image_healt(self, screen):
        """Вывод кол-ва жизней"""
        self.hearts = Group()
        for heart_number in range(self.stats.player_health):
            heart = PlayerOBJ(self.screen)

            heart.image = pygame.image.load('images/heart.png')
            heart.rect = heart.image.get_rect()
            heart.screen_rect = screen.get_rect()

            heart.rect.x = 50 + heart_number * heart.rect.width
            heart.rect.y = 30
            self.hearts.add(heart)