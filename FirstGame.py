import pygame, controls
from player import PlayerOBJ
from pygame.sprite import Group
from stats import Stats
from scores import Scores
from Menu import Menu
# простая игра со списками и циклами


def MainMenu(screen):
    menu = Menu()
    menu.append_option('Начало игры', lambda: print('Yep'))
    menu.append_option('Выход', pygame.quit)
    IsMenuOpen = True
    GameContinue = True
    while (IsMenuOpen):
        screen.fill((128,128,128))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                IsMenuOpen = False
                pygame.quit()
                GameContinue = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    menu.switch(-1)
                if event.key == pygame.K_DOWN:
                    menu.switch(1)
                if event.key == pygame.K_RETURN:
                    menu.select()
                    IsMenuOpen = False
        if IsMenuOpen:
            menu.draw(screen, 800, 400, 75)
            pygame.display.flip()

    return GameContinue

def run():
    pygame.init()
    pygame.mixer.music.load("music/bg.mp3")
    pygame.mixer.music.play(0)
    pygame.mixer.music.set_volume(0.1)
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Войнушка 2Д | First Edition")
    GameRun = MainMenu(screen)
    if GameRun:
        # bg_color = (17, 24, 135)  # 17 24 135
        bg_color = pygame.image.load("images/land.jpg")
        player = PlayerOBJ(screen)
        splashes = Group()
        monsters = Group()
        stats = Stats()
        sc = Scores(screen, stats)
        controls.create_army(screen, monsters, stats, sc)

        while True:
            controls.event(screen, player, splashes)
            if stats.run_game:
                player.update_player()
                controls.screenUpdate(bg_color, screen, stats, sc, player, monsters, splashes)
                controls.update_splashes(screen, stats, sc, monsters, splashes)
                controls.update_enemy(stats, screen, sc, player, monsters, splashes)


run()