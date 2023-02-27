import pygame, sys

import controls

screen = pygame.display.set_mode((700, 800))

def print_text(message, x, y, font_color = (100, 200,  150), font_type = "Fonts/PakenhamBl Italic.ttf", font_size = 30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    screen.blit(text, (x, y))

class Buttons():
    """кнопки"""
    def __init__(self, weidth, height):
        self.weidth = weidth
        self.height = height
        self.active_clr = (255, 150, 0)
        self.inactive_clr = (100, 0, 150)

    def draw(self, x, y, message, action = None, font_size = 30):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse [0] < x + self.weidth and y < mouse [1] < y + self.height:
            pygame.draw.rect(screen, self.active_clr, (x, y, self.weidth, self.height))

            if click[0] == 1:
                if action is not None:
                    if action == quit:
                        pygame.quit()
                        sys.exit()
                    elif action == controls.start:
                        controls.start()
                    else:
                        action()

        else:
            pygame.draw.rect(screen, self.inactive_clr, (x, y, self.weidth, self.height))

        print_text(message = message, x = x, y = y-10, font_size = font_size)

