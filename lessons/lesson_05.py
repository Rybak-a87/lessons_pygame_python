# ------------------------------------
# Создание поверхностей (Surface) и их анимация. Метод blit
# ------------------------------------
"""
Surface.blit(source, pos, ...) - позволяет отображать что либо на необходумую поверхность
Surface.set_alpha(alpha) - задавание степени прозрачности поверхности
    - alpha = 0 - полностью прозрачная
    - alpha = 255 - польностью непрозрачная
"""
import pygame
from utils.colors_rgb import *
pygame.init()

WIDTH = 600
HEIGHT = 400

sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Класс Surface")
# pygame.display.set_icon(pygame.image.load("../utils/ico.png"))

FPS = 60
clock = pygame.time.Clock()

# # работа с поверхностями
# surf = pygame.Surface((200, 200))    # создание поверхности surf
# surf.fill(RED)    # закрашивание поверхности
# pygame.draw.circle(surf, GREEN, (100, 100), 80)   # круг не залитый
#
# surf_alpha = pygame.Surface((WIDTH, 100))    # создание поверхности surf_alpha
# pygame.draw.rect(surf_alpha, BLUE, (0, 0, WIDTH, 100))    # прямоугольник
# surf_alpha.set_alpha(128)    # прозрачность поверхности surf_alpha
#
# surf.blit(surf_alpha, (0, 50))    # отобраение поверхности surf_alpha на поверхности surf
# sc.blit(surf, (50, 50))    # отобраение поверхности surf на основной поверхности sc
# # замена слоев для наглядного понимания накладывание слоев
# # surf_alpha.blit(surf, (0, 0))
# # sc.blit(surf_alpha, (50, 50))
# pygame.display.update()

# пример анимации поверхности
surf = pygame.Surface((WIDTH, 200))
bita = pygame.Surface((50, 10))

surf.fill(BLUE)
bita.fill(RED)

surf_x, surf_y = 0, 0    # положение surf
bita_x, bita_y = 0, 150    # полодение bita

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    # анимация поверхности
    surf.fill(BLUE)
    surf.blit(bita, (bita_x, bita_y))
    if bita_x < WIDTH:
        bita_x += 5
    else:
        bita_x = 0

    if surf_y < HEIGHT:
        surf_y += 1
    else:
        surf_y = 0
    sc.fill(WHITE)
    sc.blit(surf, (surf_x, surf_y))
    pygame.display.update()

    clock.tick(FPS)
