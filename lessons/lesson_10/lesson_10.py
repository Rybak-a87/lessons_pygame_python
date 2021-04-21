# ------------------------------------
# Контроль столкновений
# ------------------------------------
"""
Методы класса Rect:
collidepoint(x, y) - проверка попадания точки в прямоугольник
colliderect(Rect) - проверка пересечения двух прямоугольников
collidelist(list) - проверка пересечения хотя бы с одним прямоугольником из списка прямоугольников list
collidelistall(list) - проверка пересечения со всеми прямоугольниками из списка прямоугольников list
"""
from random import randint
import pygame
from lessons.lesson_11.ball import Ball
from utils.colors_rgb import *

pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 2000)    # генерирование события USEREVENT каждые 2000 мс

WIDTH = 1000
HEIGHT = 570
sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ловля шаров")

FPS = 60
clock = pygame.time.Clock()

# очки
game_score = 0    # очки в игре
score = pygame.image.load("images/score_fon.png").convert_alpha()
font = pygame.font.SysFont(None, 40)

# изображение телеги
telega = pygame.image.load("images/telega.png").convert_alpha()
telega_rect = telega.get_rect(centerx=WIDTH//2, bottom=HEIGHT-5)

# загрузка изображений шаров с числом очков при ловле шаров
balls_data = (
    {"path": "ball_bear.png", "score": 100},
    {"path": "ball_fox.png", "score": 150},
    {"path": "ball_panda.png", "score": 200}
)
balls_surf = [pygame.image.load("images/" + data["path"]).convert_alpha() for data in balls_data]

#создание нового шара
def create_ball(group):
    indx = randint(0, len(balls_surf)-1)
    x = randint(20, WIDTH-20)
    speed = randint(1, 4)
    return Ball(x, speed, balls_surf[indx], balls_data[indx]["score"], group)

# столкновение тележки с шаром
def collide_balls():
    global game_score
    for ball in balls:
        if telega_rect.collidepoint(ball.rect.center):
            game_score += ball.score
            ball.kill()

# группа шариков
balls = pygame.sprite.Group()

bg = pygame.image.load("images/back1.jpg").convert()

speed_telega = 10

create_ball(balls)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        elif event.type == pygame.USEREVENT:
            create_ball(balls)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        telega_rect.x -= speed_telega
        if telega_rect.x < 0:
            telega_rect.x = 0
    elif keys[pygame.K_RIGHT]:
        telega_rect.x += speed_telega
        if telega_rect.x > WIDTH - telega_rect.width:
            telega_rect.x = WIDTH - telega_rect.width

    # контроль столкновений
    collide_balls()
    # отрисовка фона
    sc.blit(bg, (0, 0))
    # отрисовка очков
    sc.blit(score, (0, 0))
    sc_text = font.render(str(game_score), 1, BLUE)
    sc.blit(sc_text, (20, 15))
    # отрисовка группы шаров
    balls.draw(sc)
    # отрисовка телеги
    sc.blit(telega, telega_rect)

    pygame.display.update()

    # падение группы шариков
    balls.update(HEIGHT)

    clock.tick(FPS)
