import pygame, sys, random
from attack import Splash
from enemy import Monster
import time


def event(screen, player, splashes):
    clock = pygame.time.Clock()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # ВПРАВО
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                player.moveRight = True
            elif event.key == pygame.K_a:
                player.moveLeft = True
            elif event.key == pygame.K_w:  # 010101
                player.moveUp = True
            elif event.key == pygame.K_s:  # 010101
                player.moveDown = True
            elif event.key == pygame.K_SPACE:  # 010101
                new_splash = Splash(screen, player)
                if len(splashes) < 1:
                    splashes.add(new_splash)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                player.moveRight = False
            elif event.key == pygame.K_a:
                player.moveLeft = False
            elif event.key == pygame.K_w:  # 010101
                player.moveUp = False
            elif event.key == pygame.K_s:  # 010101
                player.moveDown = False


def screenUpdate(bg_color, screen, stats, sc, player, monsters, splashes):
    # screen.fill(bg_color)
    screen.blit(bg_color, (0, 0))
    sc.show_score()
    for splash in splashes.sprites():
        splash.draw_splash()
    player.output()
    monsters.draw(screen)
    pygame.display.flip()


def update_splashes(screen, stats, sc, monsters, splashes):
    splashes.update()
    for splash in splashes.copy():
        if splash.rect.x > 1200:
            splashes.remove(splash)
    collisions = pygame.sprite.groupcollide(splashes, monsters, True, True)
    if collisions:
        for monsters in collisions.values():
            stats.score += (7 + stats.waves) * len(monsters)
        sc.image_score()
        check_high_score(stats, sc)
        sc.image_healt(screen)
    if len(monsters) == 0:
        monsters.empty()
        monsters.empty()
        create_army(screen, monsters, stats, sc)
        if stats.score % 4 == 0 and stats.score != 0 and stats.score % 11 == 0:
            create_army2(screen, monsters, stats, sc)
            print("MegaWave")
        if stats.score % 6 == 0 and stats.score != 0 and stats.score % 11 == 0:
            create_army2(screen, monsters, stats, sc)
            print("MegaWave")
            # print(len(splashes))


def update_enemy(stats, screen, sc, player, monsters, splashes):
    monsters.update()
    if pygame.sprite.spritecollideany(player, monsters):
        player_kill(stats, screen, sc, player, monsters, splashes)
    monster_check(stats, screen, sc, player, monsters, splashes)


def player_kill(stats, screen, sc, player, monsters, splashes):
    if stats.player_health > 0:
        stats.player_health -= 1
        sc.image_healt(screen)
        player.update_model(stats.player_health, screen)
        monsters.empty()
        splashes.empty()
        create_army(screen, monsters, stats, sc)
        # player.create_player()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()


def monster_check(stats, screen, sc, player, monsters, splashes):
    for monster in monsters.sprites():
        if monster.rect.x <= 20:
            player_kill(stats, screen, sc, player, monsters, splashes)
            break


def create_army(screen, monsters, stats, sc):
    stats.waves += 1
    sc.image_waves()
    monster = Monster(screen)

    number_monster_min = random.randint(4, 11)
    number_monster_max = random.randint(12, 25)
    number_monster_y = random.randint(number_monster_min, number_monster_max)
    print(number_monster_min, number_monster_max)

    for monster_number in range(number_monster_y):
        monster.x = random.randint(1250, 1400)
        monster.rect.y = random.randint(60, 700)
        new_speed = random.randint(2, 3)
        monster.speed = new_speed

        monster = Monster(screen)

        monsters.add(monster)

        # monster = Monster(screen)
        #
        # monster.y = (monster.y + (monster_hieght * 3) * monster_number * 1.86)
        # monster.rect.y = monster.y
        #
        # monsters.add(monster)

    # for monster_number in range(number_monster_y):
    #     monster = Monster(screen)
    #
    #     monster.y = (monster.y + (monster_hieght * 1.75) * monster_number * 1.86)
    #     monster.x = 1100
    #     monster.rect.y = monster.y
    #
    #     monsters.add(monster)


def create_army2(screen, monsters, stats, sc):
    stats.waves += 1
    sc.image_waves()
    monster = Monster(screen)
    number_monster_min = 17
    number_monster_max = 27
    number_monster_y = random.randint(number_monster_min, number_monster_max)

    for monster_number in range(number_monster_y):
        monster.x = random.randint(1350, 1500)
        monster.rect.y = random.randint(60, 700)
        new_speed = random.randint(2, 4)
        monster.speed = new_speed

        monster = Monster(screen)

        monsters.add(monster)


def check_high_score(stats, sc):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open('high_score.txt', 'w') as f:
            f.write(str(stats.high_score))
