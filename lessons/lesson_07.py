# ------------------------------------
# Отображение текстовой информации
# ------------------------------------
"""
pygame.font - работасо шлифтами
SysFont(fontname, size) - класс для выбора предустановленного шрифта (по имени fontname) с размером size (в пикселях)
Font(path, size) - класс для загрузки шрифта по указанному пути path с размером size (в пикселях)
get_fonts() - функция, возвращающая имена предустановленных в системе шлифтов
match_font(fontname) - функция возвращающая путь к предустановленному шрифту по его имени
"""
import pygame
from utils.colors_rgb import *

pygame.init()

# пример
# print(pygame.font.get_fonts())
# font_sys = pygame.font.SysFont("notosanscjktc", 12)
# font_custom = pygame.font.Font("<путь к шрифту>", 20)    # свой собственный шрифт

WIDTH = 600
HEIGHT = 400

sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Шрифты")
pygame.display.set_icon(pygame.image.load("../utils/ico.png"))

FPS = 60
clock = pygame.time.Clock()

# пример работы со шрифтом
font_custom = pygame.font.Font("../utils/YandexSDLight.ttf", 48)    # Если первым параметром указать None - будет использоватся шрифт по умолчанию
sc_text = font_custom.render("Привет мир!!!", 1, RED, YELLOW)    # формирование поверхности на которой отображается текст (текст, 1 - сглаженный, цвет текста, цвет фона (не обязательный параметр))
pos = sc_text.get_rect(center=(WIDTH//2, HEIGHT//2))    # расположение текста внутри окна

def draw_text():
    sc.fill(WHITE)
    sc.blit(sc_text, pos)
    pygame.display.update()

draw_text()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pygame.mouse.get_rel()    # обнуление первого смещения (при повторном выборе ниже)

    # перемещение
    if pygame.mouse.get_focused() and pos.collidepoint(pygame.mouse.get_pos()):
        btns = pygame.mouse.get_pressed()
        if btns[0]:
            rel = pygame.mouse.get_rel()
            pos.move_ip(rel)
            draw_text()

    clock.tick(FPS)
