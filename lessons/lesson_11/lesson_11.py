# ------------------------------------
# Работа со звуком
# ------------------------------------
"""
pygame.mixer.music - для добавления фоновой музыки (фораты: mp3, ogg, wav)
play(loops=0, start=0.0, fade_ms=0) - воспроизведение файла
    - loops - число повторений (0 - проигрывать один раз, 1 - два раза, и т.д., -1 - бесконечное повторение)
    - start - начальное время проигрывания файла (в секундах)
    - fade_ms - затухание звука при окончании проигрывания (в мили секундах)
pygame.mixer.music.stop() - полностью остановить воспроизведение
pygame.mixer.music.pause() - поставить на паузу
pygame.mixer.music.unpause() - снять с паузы
pygame.mixer.music.rewind() - начать воспроизведения с начала
set_volume(volume) - установить уровень громкости (volume - вещественное значение от 0 до 1)
get_volume() - получить текущее значение уровня громкости

pygame.mixer - для работы со звуковыми эфектами
    init(frequency=44100, size=-16, channels=2, buffer=512, devicename=None,
         allowedchanges=AUDIO_ALLOW_FREQUENCY_CHANGE | AUDIO_ALLOW_CHANNELS_CHANGE)
    pre_init(frequency=44100, size=-16, channels=2, buffer=512, devicename=None) - для изменения параметров вызывать до pygame.init()
        - frequency - частота воспроизведения звукового файла
        - size - число бит для представления аудио данных (знак минус говорит, что используются знаковые числа)
        - channels - число каналов
        - buffer - размер буфера (в байтах)
        - allowedchanges - дополнительные флаговые настройки
pygame.mixer.Sound(filename) - загрузка звукового файла (формат wav, ogg)
        play(loops=0, maxtime=0, fade_ms=0) - воспроизведение звука
        stop() - остановка воспроизведения
        set_volume(volume) - установить уровень громкости (volume - вещественное значение от 0 до 1)
        get_volume() - получить текущее значение уровня громкости

"""
from random import randint
import pygame
from lessons.lesson_11.ball import Ball
from utils.colors_rgb import *

pygame.mixer.pre_init(44100, -16, 1, 512)    # убрать зажержку звука (часто используется)
pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 2000)    # генерирование события USEREVENT каждые 2000 мс

# фоновая музыка
pygame.mixer.music.load("sounds/bird.wav")
pygame.mixer.music.play(loops=-1)

# звук пойманого шара
sound = pygame.mixer.Sound("sounds/catch.ogg")

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
            sound.play()    # вызов звука ловли шарика
            ball.kill()

# группа шариков
balls = pygame.sprite.Group()

bg = pygame.image.load("images/back1.jpg").convert()

speed_telega = 10

create_ball(balls)

vol = 1.0
flag_pause = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        elif event.type == pygame.USEREVENT:
            create_ball(balls)
        # одно нажатие клавиши
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                flag_pause = not flag_pause
                if flag_pause:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_UP:
                vol += 0.1
                pygame.mixer.music.set_volume(vol)
            elif event.key == pygame.K_DOWN:
                vol -= 0.1
                pygame.mixer.music.set_volume(vol)

    # для зажатых клавишь
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        telega_rect.x -= speed_telega
        if telega_rect.x < 0:
            telega_rect.x = 0
    elif keys[pygame.K_RIGHT]:
        telega_rect.x += speed_telega
        if telega_rect.x > WIDTH - telega_rect.width:
            telega_rect.x = WIDTH - telega_rect.width
    # elif keys[pygame.K_SPACE]:
    #     flag_pause = not flag_pause
    #     if flag_pause:
    #         pygame.mixer.music.pause()
    #     else:
    #         pygame.mixer.music.unpause()
    # elif keys[pygame.K_UP]:
    #     vol += 0.1
    #     pygame.mixer.music.set_volume(vol)
    # elif keys[pygame.K_DOWN]:
    #     vol -= 0.1
    #     pygame.mixer.music.set_volume(vol)


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
