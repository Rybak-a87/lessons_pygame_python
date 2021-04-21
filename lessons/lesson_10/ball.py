"""
pygame.sprite - спрайт - любая подвижная область
- image - графическое представление спрайта (ссылка на Surface)
- rect - положение и размер спрайта
"""
import pygame


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, speed, surf, score, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, 0))
        self.speed = speed
        self.score = score
        self.add(group)

    # падение шарика
    def update(self, *args, **kwargs) -> None:
        if self.rect.y < args[0]-20:
            self.rect.y += self.speed
        else:
            self.kill()    # ударение спрайта из всех групп

