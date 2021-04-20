# ------------------------------------
# Обработка событий от мыши
# ------------------------------------
"""
pygame.MOUSEBUTTONDOWN - нажатие кнопки мыши
pygame.MOUSEBUTTONUP - отпускание кнопки мыши
pygame.MOUSEMOTION - перемещение курсора мыши
pygame.MOUSEWHEEL - крусение колесика мыши
pygame.mouse.get_pressed() - возвращает кортеж нажатых кнопок (0, 0, 0)
"""
import pygame
pygame.init()

WIDTH = 600
HEIGHT = 400

sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Обработка событий от мыши")
pygame.display.set_icon(pygame.image.load("../utils/ico.png"))

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

FPS = 60
clock = pygame.time.Clock()

# # для рисования прямоугольника (1)
# fl_start_draw = False
# start_position = end_position = None

# # для рисования прямоугольника (2)
start_position = None

sc.fill(WHITE)
pygame.display.update()

# скрыть курсор мыши
pygame.mouse.set_visible(False)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False



        # elif event.type == pygame.MOUSEBUTTONDOWN:    # нажатие кнопки мыши
        #     print("Нажата кнопка мыши:", event.button)
        # elif event.type == pygame.MOUSEMOTION:    # перемешение курсора мыши
        #     print("Позиция мыши:", event.pos)
        #     print("Позиция мыши:", event.rel)    # перемещение курсора относительно предыдущей позиции

        # # рисование прямоугольника (1)
        # elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        #     fl_start_draw = True
        #     start_position = event.pos
        # elif event.type == pygame.MOUSEMOTION:
        #     if fl_start_draw:
        #         pos = event.pos
        #
        #         width = pos[0] - start_position[0]
        #         height = pos[1] - start_position[1]
        #
        #         sc.fill(WHITE)
        #         pygame.draw. rect(sc, RED, pygame.Rect(start_position[0], start_position[1], width, height))
        #         pygame.display.update()
        # elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
        #     fl_start_draw = False

# рисование прямоугольника (2)
    # свой курсор мыши
    sc.fill(WHITE)
    pos = pygame.mouse.get_pos()
    if pygame.mouse.get_focused():  # проверка на нахождение курсора в пределах окна
        pygame.draw.circle(sc, BLUE, pos, 7)

    pressed = pygame.mouse.get_pressed()
    if pressed[0]:

        if start_position is None:
            start_position = pos

        width = pos[0] - start_position[0]
        height = pos[1] - start_position[1]

        sc.fill(WHITE)
        # pygame.draw.rect(sc, RED, pygame.Rect(start_position[0], start_position[1], width, height))
        pygame.draw.rect(sc, RED, (start_position[0], start_position[1], width, height))

    else:
        start_position = None

    pygame.display.update()

    clock.tick(FPS)
