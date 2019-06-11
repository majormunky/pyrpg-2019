import pygame
from Engine.Grid import Grid


class World:
    def __init__(self):
        self.width = 10
        self.height = 10
        self.size = 32
        self.grid = Grid([["0" for x in range(self.width)] for y in range(self.height)])
        self.image = None
        self.render_image()

    def render_image(self):
        self.image = pygame.Surface((self.width * self.size, self.height * self.size), pygame.SRCALPHA)
        for y in range(self.grid.height):
            for x in range(self.grid.width):
                tile_info = self.grid.get_cell(x, y)
                if tile_info == "0":
                    color = (0, 200, 0)
                elif tile_info == "1":
                    color = (0, 0, 200)
                pygame.draw.rect(self.image, color, (x * self.size, y * self.size, self.size, self.size))

    def update(self, dt):
        pass

    def draw(self, canvas):
        canvas.blit(self.image, (0, 0))

    def handle_event(self, event):
        pass
