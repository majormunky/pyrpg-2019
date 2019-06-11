import pygame
from Engine.Config import get_screenrect


class Player:
    def __init__(self, x, y):
        self.screenrect = get_screenrect()
        self.rect = pygame.Rect(x, y, 32, 32)
        self.color = (0, 255, 0)
        self.speed = 0.2

    def update(self, dt, move_cb):
        pressed_keys = pygame.key.get_pressed()
        move = pygame.math.Vector2(0, 0)
        if pressed_keys[pygame.K_UP]:
            move.y = -1
        elif pressed_keys[pygame.K_DOWN]:
            move.y = 1
        elif pressed_keys[pygame.K_LEFT]:
            move.x = -1
        elif pressed_keys[pygame.K_RIGHT]:
            move.x = 1

        if move:
            new_rect = self.rect.copy()
            new_rect.x += (move.x * self.speed * dt)
            new_rect.y += (move.y * self.speed * dt)

            result = move_cb(new_rect)
            if result:
                self.rect = new_rect

    def draw(self, canvas):
        pygame.draw.rect(canvas, self.color, self.rect)

    def handle_event(self, event):
        pass

