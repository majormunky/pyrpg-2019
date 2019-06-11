import pygame
from Engine.Text import text_surface


class IntroScene:
    def __init__(self, manager):
        self.manager = manager
        self.intro_text = text_surface("Intro", font_size=36, color=(0, 0, 0))

    def update(self, dt):
        pass

    def draw(self, canvas):
        canvas.fill((255, 0, 0))
        canvas.blit(self.intro_text, (32, 32))

    def handle_event(self, event):
        pass

    def activate(self, data):
        pass

    def deactivate(self):
        pass
