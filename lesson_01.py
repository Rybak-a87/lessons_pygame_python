# ------------------------------------
# Каркас приложения, главный цикл, FPS
# ------------------------------------
import pygame    # импорт основного модуля

pygame.init()    # импортирует массу других необходимых разширений

# окно приложения
# pygame.FULLSCREEN - полноэкранный режим
# pygame.DOUBLEBUF - двойная буферизация (рекомендуетсяс при совместном использовании HWSURFACE или OPENGL)
# pygame.HWSURFACE - аппаратное ускорение отрисовки (только для режима FULLSCREEN)
# pygame.OPENGL - обработка отображений с помощью библиотеки OpenGL
# pygame.RESIZABLE - окно с изменяемыми размерами
# pygame.NOFRAME - окно без рамки и заголовка
# pygame.SCALED - разрешение, зависящее отразмеров рабочего стола
pygame.display.set_mode((600, 400), pygame.FULLSCREEN | pygame.HWSURFACE)    # можно определять несколько параметров через разделитель |

# заголовок окна
pygame.display.set_caption("Моя первая игра на PyGame")

# иконка окна (желательно *.bmp)
pygame.display.set_icon(pygame.image.load("ico.png"))

# для задержка (для FPS)
clock = pygame.time.Clock()
FPS = 60

# Главный цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()    # завершение работы модуля pygame
            running = False

    clock.tick(FPS)    # 60 итераций в секунду (FPS - Frames Per Second)

