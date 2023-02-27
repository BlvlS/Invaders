import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        """Выстрел пули из пушки"""
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 8, 12)
        self.color = 255, 255, 255
        self.speed = 2.5
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """движение пули вверх"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Отрисовка пули"""
        pygame.draw.rect(self.screen, self.color, self.rect)