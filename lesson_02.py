# ------------------------------------
# Рисование графическиз примитивов
# ------------------------------------
'''
pygame.draw.rect(surface, ...) - прямоугольник
pygame.draw.line(surface, ...) - линия
pygame.draw.aaline(surface, ...) - сглаженная линия
pygame.draw.lines(surface, ...) - ломаная линия
pygame.draw.aalines(surface, ...) - ломаная сглаженная линия
pygame.draw.polygon(surface, ...) - полигон
pygame.draw.circle(surface, ...) - круг
pygame.draw.ellipse(surface, ...) - эллипс
pygame.draw.arc(surface, ...) - дуга
'''
import pygame
pygame.init()

# размер окна
WIDTH = 600
HEIGHT = 400
sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Графические примитивы")
pygame.display.set_icon(pygame.image.load("ico.png"))

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
# рисуем прямоугольник
pygame.draw.rect(sc,WHITE , (10, 10, 50, 100), 5)    # цвет и размеры (не обязательный параметр толщина линии)
# рисуем линию
pygame.draw.line(sc, GREEN, (200, 20), (350, 50), 3)
# рисуем сглаженную линию
pygame.draw.aaline(sc, BLUE, (200, 40), (350, 70))
# ломаные линии
pygame.draw.lines(sc, RED, True, [(200, 80), (250, 80), (300, 200)], 2)
pygame.draw.aalines(sc, RED, False, [(300, 80), (350, 80), (400, 200)])
# полигоны
pygame.draw.polygon(sc, WHITE, [[150, 210], [180, 250], [90, 290], [30, 230]])    # закрашенный
pygame.draw.polygon(sc, WHITE, [[150, 310], [180, 350], [90, 390], [30, 330]], 3)    # не закрашенный
# круг
pygame.draw.circle(sc, BLUE, (300, 250), 40)
# эллипс
pygame.draw.ellipse(sc, BLUE, (300, 300, 100, 50), 2)
# дуга
pi = 3.14
pygame.draw.arc(sc, RED, (450, 30, 50, 150), pi, pi*2, 5)

# pygame.display.flip()    # переворот плоскости (отображение рисунка)
pygame.display.update()    # переворот плоскости (отображение рисунка)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False