# ------------------------------------
# Работаем со спрайтами
# ------------------------------------
"""
pygame.sprite.Group() - создание группы
"""
from random import randint
import pygame
from utils.colors_rgb import *
from ball import Ball

pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 2000)    # генерирование события USEREVENT каждые 2000 мс

WIDTH = 1000
HEIGHT = 570

sc = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 60
clock = pygame.time.Clock()

# загрузка изображений шаров
balls_images = ["ball_bear.png", "ball_fox.png", "ball_panda.png"]
balls_surf = [pygame.image.load("images/" + path).convert_alpha() for path in balls_images]

#создание нового шара
def create_ball(group):
    indx = randint(0, len(balls_surf)-1)
    x = randint(20, WIDTH-20)
    speed = randint(1, 4)
    return Ball(x, speed, balls_surf[indx], group)

# группа шариков
balls = pygame.sprite.Group()

bg = pygame.image.load("images/back1.jpg").convert()

speed = 1
# добавление шариков в группу
# balls.add(Ball(WIDTH//2, speed, "images/ball_bear.png"))    # добавление по одному обекту
# balls.add(Ball(WIDTH//2-250, speed+1, "images/ball_fox.png"),        # добавление по несколько обектов
#           Ball(WIDTH//2+100, speed+2, "images/ball_panda.png"))

create_ball(balls)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        elif event.type == pygame.USEREVENT:
            create_ball(balls)

    sc.blit(bg, (0, 0))
    # отрисовка группы
    balls.draw(sc)

    pygame.display.update()

    # падение группы шариков
    balls.update(HEIGHT)

    clock.tick(FPS)
