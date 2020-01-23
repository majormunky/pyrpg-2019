import pygame
from Engine import Config

class Display:
    def __init__(self, engine):
        self.engine = engine
        self.surface = pygame.display.set_mode(Config.get_screensize())
        self.back_buffer = pygame.Surface(Config.get_screensize(), pygame.SRCALPHA)

    def get_buffer(self):
        return self.back_buffer

    def clear_buffer(self):
        self.back_buffer.fill((0, 0, 0))

    def render(self):
        screen = self.back_buffer
        w, h = self.back_buffer.get_size()
        self.surface.blit(screen, (0, 0))
