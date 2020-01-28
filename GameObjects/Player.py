import pygame
from Engine.Config import get_screenrect


class Player:
    def __init__(self, x, y):
        self.screenrect = get_screenrect()
        self.size = 8
        self.rect = pygame.Rect(x, y, self.size, self.size)
        self.color = (0, 255, 0)
        self.speed = 0.125

    def update(self, dt, move_cb):
        pressed_keys = pygame.key.get_pressed()
        move = pygame.math.Vector2(0, 0)
        direction = None
        if pressed_keys[pygame.K_UP]:
            move.y = -1
            direction = "up"
        elif pressed_keys[pygame.K_DOWN]:
            move.y = 1
            direction = "down"
        elif pressed_keys[pygame.K_LEFT]:
            move.x = -1
            direction = "left"
        elif pressed_keys[pygame.K_RIGHT]:
            move.x = 1
            direction = "right"

        if move:
            new_rect = self.rect.copy()
            new_rect.x += move.x * self.speed * dt
            new_rect.y += move.y * self.speed * dt

            result = move_cb(new_rect, direction)
            if result:
                self.rect = new_rect

    def draw(self, canvas, camera):
        pygame.draw.rect(canvas, self.color, self.rect)

    def handle_event(self, event):
        pass
