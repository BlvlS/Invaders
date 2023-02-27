import pygame

class Alien(pygame.sprite.Sprite):
    """Класс одного пришельца"""

    def __init__(self, screen):
        """запуск начальной позиции"""
        super(Alien, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("Images/alien.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """Отрисовка пришельца"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """движение пришельцев"""
        self.y += 0.8
        self.rect.y = self.y