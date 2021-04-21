# ------------------------------------
# Как работать сизображениями. Модули image  transform
# ------------------------------------
"""
родной формат pygame - bmp (Bitmap Picture)
PNG (расширение png) - используется сжатие без потерь с использованием алгоритмов ДИКМ и LZW
JPEG (расширение jpg) - используется сжание с потерями (алгоритм ДКП - аналог Фурье-преобразования с косинусными гармониками)
pygame.image.get_extended() - проверка на возможность испольловать форматы png, jpg ...
... СОВЕТ ...
    - Для фотореалистичных изображений лучше всего использовать JPEG, т.к. незначительные потери
    практически не скажутся на визуальном восприятии, но изображения будет хорошо сжато.
    - Для искуственных изображений с большим наличием однотонных областей (например клип-арт)
    где четкость границ и однотонность заливки имеет первостепенное значение, лучше выбирать
    формат PNG. Кроме того, этот формат хранит альфа-канал для прозрачного фона (в JPEG такой возможности нет)
pygame.image - загрузка-сохранение изображения
pygame.transform - трансформация поверхностей
pygame.transform.scale(Surface, (width, height), DestSurface=None) - масштабирование поверхности

"""
import pygame
from utils.colors_rgb import *

pygame.init()

WIDTH = 600
HEIGHT = 400

sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Изображения")
# pygame.display.set_icon("")

FPS = 60
clock = pygame.time.Clock()

# работа с изображениеями
# print(pygame.image.get_extended())
bg_surf = pygame.image.load("images/sand.jpg").convert()    # фон окна
# аналог
# bg_surf = pygame.image.load("images/sand.jpg")
# bg_surf = bg_surf.convert()
car_surf = pygame.image.load("images/car.bmp").convert()    # машина
finish_surf = pygame.image.load("images/finish.png").convert_alpha()    # финиш
car_rect = car_surf.get_rect(center=(WIDTH//2, HEIGHT//2))    # расположение машины
car_surf.set_colorkey(WHITE)    # какой цвет отображать прозрачным
bg_surf = pygame.transform.scale(bg_surf, (bg_surf.get_width()//3, bg_surf.get_height()//3))    # масштабирование

car_up = car_surf
car_down = pygame.transform.flip(car_surf, 0, 1)    # зеркальное отображение (по осям x и y)
car_left = pygame.transform.rotate(car_surf, 90)    # поворот изображения (градусы)
car_right = pygame.transform.rotate(car_surf, -90)



car = car_up
speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
    bt = pygame.key.get_pressed()
    if bt[pygame.K_LEFT]:
        car = car_left
        car_rect.x -= speed
        if car_rect.x < 0:
            car_rect.x = 0
    elif bt[pygame.K_RIGHT]:
        car = car_right
        car_rect.x += speed
        if car_rect.x > WIDTH-car_rect.height:
            car_rect.x = WIDTH-car_rect.height
    elif bt[pygame.K_UP]:
        car = car_up
        car_rect.y -= speed
        if car_rect.y < 0:
            car_rect.y = 0
    elif bt[pygame.K_DOWN]:
        car = car_down
        car_rect.y += speed
        if car_rect.y > HEIGHT-car_rect.height:
            car_rect.y = HEIGHT-car_rect.height

    sc.blit(bg_surf, (0, 0))    # отрисовка фона
    sc.blit(finish_surf, (0, 0))    # отрисовка финиша
    sc.blit(car, car_rect)    # отрисовка машины
    pygame.display.update()

    clock.tick(FPS)
