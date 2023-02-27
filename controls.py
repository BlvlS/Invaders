import pygame, sys, time

import screen
from bullet import Bullet
from alien import Alien
from screen import Buttons
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores
from screens import Game_over

clock = pygame.time.Clock()
screen = pygame.display.set_mode((700, 800))

def events(screen, gun, bullets):
    """Обработка событий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pause()
            #вправо
            elif event.key == pygame.K_d:
                gun.mright = True
            elif event.key == pygame.K_RETURN:
                paused = False
            #влево
            elif event.key == pygame.K_a:
                gun.mleft = True
            #выстрел
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            #вправо
            if event.key == pygame.K_d:
                gun.mright = False
            #влево
            elif event.key == pygame.K_a:
                gun.mleft = False

def update(screen, stats, sc, gun, aliens, bullets):
    """обновление экрана"""
    if stats.run_game == True:
        bg = pygame.image.load("Images/bg.jpeg")
        bg_rect = bg.get_rect()
        screen.blit(bg, bg_rect)
        sc.show_score()
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        gun.output()
        aliens.draw(screen)
        pygame.display.flip()

def update_bullets(screen, stats, sc, aliens, bullets):
    """Обновление позиции пуль"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += 10 * len(aliens)
        sc.image_score()
        check_high_score(stats, sc)
        sc.image_guns()
    if len(aliens) == 0:
        bullets.empty()
        create_army(screen, aliens)

def gun_kill(stats, screen, sc, gun, aliens, bullets):
    """Столкновение танка с пришельцами"""
    if stats.guns_left > 0:
        stats.guns_left -= 1
        sc.image_guns()
        aliens.empty()
        bullets.empty()
        gun.create_gun( )
        create_army(screen, aliens)
        time.sleep(1)
    else:
        stats.run_game = False

def update_aliens(stats, screen, sc, gun, aliens, bullets):
    """Обновляет позицию пришельцев"""
    aliens.update()
    if pygame.sprite.spritecollideany(gun, aliens):
        gun_kill(stats, screen, sc, gun, aliens, bullets)
    aliens_check(stats, screen, sc, gun, aliens, bullets)

def aliens_check(stats, screen, sc,  gun, aliens, bullets):
    """проверка края"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, sc, gun, aliens, bullets)
            break

def create_army(screen, aliens):
    """Создание ряда пришельцев"""
    alien = Alien(screen)
    alien_width = alien.rect.width
    number_alien_x = int((700 - 2 * alien_width) / alien_width)
    alien_height = alien.rect.height
    number_alien_y = int((800-100 - 2 * alien_height) / alien_height)

    for row_number in range(number_alien_y - 1):
        for alien_number in range(number_alien_x):
            alien = Alien(screen)
            alien.x = alien_width + alien_width * alien_number
            alien.y = alien_height + alien_height * row_number
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + alien.rect.height * row_number
            aliens.add(alien)

def check_high_score(stats, sc):
    """проверка рекордов"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open("highscore.txt", "w") as f:
            f.write(str(stats.high_score))

def enter():
    start_btn = Buttons(220, 45)
    exit_btn = Buttons(100, 45)

    start_btn.draw(270, 200, "NEW GAME", start, 50)
    exit_btn.draw(358, 300, "EXIT", exit, 50)

    pygame.display.update()

def finale():
    cont_btn = Buttons(220, 45)
    exit_btn = Buttons(100, 45)

    cont_btn.draw(270, 200, "NEW GAME", start, 50)
    exit_btn.draw(358, 300, "EXIT", exit, 50)

    pygame.display.update()

def start():
    screen = pygame.display.set_mode((700, 800))
    gun = Gun(screen)
    bullets = Group()
    aliens = Group()
    stats = Stats()
    sc = Scores(screen, stats)
    lost = Game_over(screen)
    create_army(screen, aliens)
    stats.reset_stats()
    stats.run_game = True

    while True:
        clock.tick(60)
        events(screen, gun, bullets)
        if stats.run_game == True:
            gun.update_gun()
            update(screen, stats, sc, gun, aliens, bullets)
            update_bullets(screen, stats, sc, aliens, bullets)
            update_aliens(stats, screen, sc, gun, aliens, bullets)
        if stats.run_game == False:
            lost.show_lost()
            finale()

def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        def print_text(message, x, y, font_color=(0, 0, 0), font_type="Fonts/PakenhamBl Italic.ttf", font_size=40):
            font_type = pygame.font.Font(font_type, font_size)
            text = font_type.render(message, True, font_color)
            screen.blit(text, (x, y))

        pygame.draw.rect(screen, (100, 0, 150), (0, 300, 700, 50))
        print_text("Game is paused, Press ENTER to continue", 15, 300)

        keys = pygame.key.get_pressed()
        if keys [pygame.K_RETURN]:
            paused = False

        pygame.display.update()
        clock.tick(60)