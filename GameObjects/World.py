import pygame
from Engine.Grid import Grid


class World:
    def __init__(self, data):
        self.data = data
        self.grid = Grid(data["grid"])
        self.width = self.grid.width
        self.height = self.grid.height
        self.size = 32
        self.image = None
        self.render_image()

    def render_image(self):
        self.image = pygame.Surface((self.width * self.size, self.height * self.size), pygame.SRCALPHA)
        for y in range(self.grid.height):
            for x in range(self.grid.width):
                tile_id = self.grid.get_cell(x, y)
                tile_data = self.get_tile_data(tile_id)
                if tile_data:
                    pygame.draw.rect(
                        self.image, 
                        tile_data["color"], 
                        (x * self.size, y * self.size, self.size, self.size)
                    )

    def update(self, dt):
        pass

    def get_tile_data(self, tile_id):
        return self.data["tile_info"].get(tile_id, None)

    def draw(self, canvas):
        canvas.blit(self.image, (0, 0))

    def handle_event(self, event):
        pass
