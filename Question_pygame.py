import pygame
from random import *

BACK = (200, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
pygame.init()
window = pygame.display.set_mode((500, 500))
window.fill(BACK)

class TextArea():
    def __init__(self, x = 10, y = 10,width = 10, height = 10, color = BLACK ):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def set_text(self, text, size, color):
        self.text = text
        self.image = pygame.font.Font(None, 70).render(text, True, color)

    def draw(self, shift_x, shift_y):
        pygame.draw.rect(window, self.color, self.rect)
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

rect1 = TextArea(150, 100, 200, 100)
rect2 = TextArea(150, 300, 200, 100)

rect1.set_text("?", 40, WHITE)
rect2.set_text("!", 40, WHITE)
rect1.draw(20, 30)
rect2.draw(20, 30)

clock = pygame.time.Clock()

while  True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            num = randint(1,3)
            if num == 1:
                question = "Почему?"
            if num == 2:
                question = "Зачем?"
            if num == 3:
                question = "Для чего?"
            rect1.set_text(question, 40, WHITE)
            rect1.draw(20, 30)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            num = randint(1,3)
            if num == 1:
                answer = "Потому"
            if num == 2:
                answer = "Затем"
            if num == 3:
                answer = "Для того"
            rect2.set_text(answer, 40, WHITE)
            rect2.draw(20, 30)



    clock.tick(40)
    pygame.display.update()
