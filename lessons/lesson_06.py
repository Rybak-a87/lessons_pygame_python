# ------------------------------------
# Класс Rect. Его роль, свойства и методы
# ------------------------------------
"""
Rect (сокращение от Rectangle - прямоугольник) - операции с прямоугольными областями
Surface.get_rect() - у каждой поверхности есть этот метод, он возвращает экземпляр класса Rect (размеры и местоположение Surfave)
Свойства класса Rect:
    Rect.topleft- координаты верх левого угла
    Rect.top - координаты верх середина
    Rect.topright - координаты верх правый угол
    Rect.left - координаты середина лево
    Rect.center - координаты середина
    Rect.right - координаты середина право
    Rect.bottomleft - координаты низ левый угол
    Rect.bottom - координаты низ сереинв
    Rect.bottomright - координаты низ правый угол
    Rect.x = 10 - задать координату x
    Rect.y = 10 - задать координату y
Методы класса Rect
    Rect.move(x,y) - возвращает новый прямоугольник со смещениями x, y
    Rect.move_ip(x, y) - меняет координаты текущего прямоугольника со смещением x, y
    Rect.clip(Rect) - обрезает границы прямоугольника по указанным размерам переданного прямоугольника
    Rect.union(Rect) - возвращает новый прямоугольник с результатом объеденения двух прямоугольников в один
    Rect.union_ip(Rect) - объеденяет два прямоугольгника в один
    Rect.fit(Rect) - возвращает новый прямоугольник, смещенный и изменненный по размеру переданного прямоугольника
    Rect.contains(Rect) - проверяет, содержится ли один прямоугольник внутри другого
"""
import pygame
from utils.colors_rgb import *

pygame.init()

WIDTH = 600
HEIGHT = 400

sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Класс Rect")
pygame.display.set_icon(pygame.image.load("../utils/ico.png"))

FPS = 60
clock = pygame.time.Clock()

# # пример работы методов класса Rect
# rect_1 = pygame.Rect((0, 0, 30, 30))
# rect_2 = pygame.Rect((30, 30, 30, 30))
# rect_2.move_ip(20, 20)
# print(rect_2)
# rect_3 = rect_2.union(rect_1)
# print(rect_3)

# # пример вывода данных Rect
# hero = pygame.Surface((40, 50))
# hero.fill(BLUE)
# # rect = hero.get_rect()    # кортеж из 4х значений (первые 2 - координаты левой верхней точки, вторые 2 - размер ширина и высота)
# # print(rect.topleft)
# rect = hero.get_rect(center=(WIDTH//2, HEIGHT//2))    # расположить "героя" в центре окна
# # rect = hero.get_rect(topleft=(100, 50))    # расположить "героя" (левый верхний угол x=100, y=50)

# прыжек героя
ground = HEIGHT - 70    # уровень земли где находится герой
jump_force = 20    # сила прыжка героя
move = jump_force + 1    # текущая вертивальная скорость
hero = pygame.Surface((40, 50))    # герой рамером 40х50
hero.fill(BLUE)    # герой синего цвета
rect = hero.get_rect(centerx=WIDTH//2)
rect.bottom = ground

# перерисовывать только ту область окна где прыгает герой
rect_update = pygame.Rect(rect.x, 0, rect.width, ground)

sc.fill(WHITE)
sc.blit(hero, rect)    # передача объекта rect в качестве параметров коолдинат
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

        # прыжек по клавише "пробел"
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and ground == rect.bottom:
                move = -jump_force
    # отработка прыжка
    if move <= jump_force:
        if rect.bottom + move < ground:
            rect.bottom += move
            if move < jump_force:
                move += 1
        else:
            rect.bottom = ground
            move = jump_force + 1
    # прорисовка
    sc.fill(WHITE)
    sc.blit(hero, rect)
    pygame.display.update(rect_update)    # перерисовывать только ту область окна где прыгает герой

    clock.tick(FPS)
