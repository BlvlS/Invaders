import pygame.font
from pygame.locals import *

class Game_over():
    """Экран поражения"""
    def __init__(self, screen):
        """запуск экрана"""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.color = (255, 0, 0)
        self.font = pygame.font.SysFont(None, 135)
        self.font1 = pygame.font.SysFont(None, 100)
        self.rect = Rect(35, 35, 700, 800)
        self.show_lost()

    def show_lost(self):
        """показ надписи"""
        self.image = pygame.image.load("Images/bg1.png")
        self.image_rect = self.image.get_rect()
        self.lost_image = self.font.render("GAME OVER!", True, self.color)
        self.screen.blit(self.image, self.image_rect)
        self.screen.blit(self.lost_image, self.rect)