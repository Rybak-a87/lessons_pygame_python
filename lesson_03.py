# ------------------------------------
# Обработка событий от клавиатуры
# ------------------------------------
'''
pygame.event.get() - отвечает за обработку событий
event.type == pygame.KEYDOWN - клавиша нажата
event.type == pygame.KEYUP - клавиша отпущена
pygame.key - работа с клавиатурой
pygame.key.get_pressed() - возвращает информацю о тех клавишах которые нажаты

'''
import pygame
pygame.init()

WIDTH = 600
HEIGHT = 400
sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("События курсора")
pygame.display.set_icon(pygame.image.load("ico.png"))

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

FPS = 60
clock = pygame.time.Clock()

# начальное положение прямоугольника
x = WIDTH // 2
y = HEIGHT // 2
# скорость перемещения прямоугольника
speed = 5

move = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    elif keys[pygame.K_RIGHT]:
        x += speed

    #     # нажатие клавиши с левым CTRL
    #     elif event.type == pygame.KEYDOWN:    # усли есть нажатие клавиши
    #         if event.key == pygame.K_LEFT and event.mod == pygame.KMOD_LCTRL:    # если нажата кнопка влево
    #             move = -speed
    #         elif event.key == pygame.K_RIGHT and event.mod == pygame.KMOD_LCTRL:    # если нажата кнопка вправо
    #             move = speed
    #     elif event.type == pygame.KEYUP:
    #         if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
    #             move = 0
    # # движение
    # x += move

    sc.fill(WHITE)    # закрашивание всюобласть белым цветом
    pygame.draw.rect(sc, BLUE, (x, y, 10, 20))
    pygame.display.update()

    clock.tick(FPS)
