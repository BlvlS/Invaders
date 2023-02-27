import pygame, controls
from gun import Gun
from pygame.sprite import Group
from pygame.locals import *

def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Иноземцы")
    gun = Gun(screen)
    bullets = Group()
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 150)
    rect = Rect(35, 35, 700, 800)
    main_menu = True

    while True:
        clock.tick(60)
        controls.events(screen, gun, bullets)
        if main_menu == True:
            menu_image = font.render("ИНОЗЕМЦЫ", True, (100, 200, 150))
            image = pygame.image.load("Images/start.jpeg")
            image_rect = image.get_rect()
            screen.blit(image, image_rect)
            screen.blit(menu_image, rect)
            controls.enter()

run()