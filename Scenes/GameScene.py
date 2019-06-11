import pygame
from Engine.Config import get_screenrect

class GameScene:
    def __init__(self, manager):
        self.manager = manager
        self.screenrect = get_screenrect()
        self.player = pygame.Rect(0, 0, 32, 32)

    def update(self, dt):
        pass

    def draw(self, canvas):
        pygame.draw.rect(canvas, (0, 255, 0), self.player)

    def handle_event(self, event):
        if event.type == pygame.KEYUP:
            new_rect = self.player.copy()
            if event.key == pygame.K_UP:
                new_rect.y -= 32
            elif event.key == pygame.K_DOWN:
                new_rect.y += 32
            elif event.key == pygame.K_LEFT:
                new_rect.x -= 32
            elif event.key == pygame.K_RIGHT:
                new_rect.x += 32

            if self.screenrect.contains(new_rect):
                self.player = new_rect

    def activate(self, data):
        pass

    def deactivate(self):
        pass

