import pygame
from Engine.Config import get_screenrect


class GameMenu:
    def __init__(self):
        self.screenrect = get_screenrect()
        self.image = None
        self.active = False
        self.render()

    def render(self):
        self.image = pygame.Surface(
            (self.screenrect.width, self.screenrect.height), pygame.SRCALPHA
        )
        self.image.fill((0, 0, 0, 128))

    def update(self, dt):
        pass

    def toggle_active(self):
        self.active = not self.active

    def draw(self, canvas):
        if self.active:
            canvas.blit(self.image, (0, 0))

    def handle_event(self, event):
        pass
