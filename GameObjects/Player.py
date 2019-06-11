import pygame
from Engine.Config import get_screenrect


class Player:
    def __init__(self):
        self.screenrect = get_screenrect()
        self.rect = pygame.Rect(0, 0, 32, 32)
        self.color = (0, 255, 0)

    def update(self, dt):
        pass

    def draw(self, canvas):
        pygame.draw.rect(canvas, self.color, self.rect)

    def handle_event(self, event):
        if event.type == pygame.KEYUP:
            new_rect = self.rect.copy()
            if event.key == pygame.K_UP:
                new_rect.y -= 32
            elif event.key == pygame.K_DOWN:
                new_rect.y += 32
            elif event.key == pygame.K_LEFT:
                new_rect.x -= 32
            elif event.key == pygame.K_RIGHT:
                new_rect.x += 32

            if self.screenrect.contains(new_rect):
                self.rect = new_rect
