import pygame
from Engine.Grid import Grid


class World:
    def __init__(self, data):
        self.data = data
        self.current_map = None
        self.grid = None # Grid(data["grid"])
        self.width = None # self.grid.width
        self.height = None # self.grid.height
        self.size = 32
        self.image = None
        self.rect = None

    def load(self, map_name):
        if map_name in self.data.keys():
            self.current_map = self.data[map_name]
            self.grid = Grid(self.current_map["grid"])
            self.width = self.grid.width
            self.height = self.grid.height
            self.render_image()

    def render_image(self):
        self.image = pygame.Surface((self.width * self.size, self.height * self.size), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
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
        return self.current_map["tile_info"].get(tile_id, None)

    def draw(self, canvas):
        canvas.blit(self.image, (0, 0))

    def handle_event(self, event):
        pass

    def get_tile_at_pos(self, pos):
        tx = pos[0] // self.size
        ty = pos[1] // self.size
        tile_id = self.grid.get_cell(tx, ty)
        return {
            "tile_id": tile_id, 
            "rect": pygame.Rect(tx, ty, self.size, self.size),
            "tile_data": self.get_tile_data(tile_id)
        }

    def get_tiles(self, rect):
        t1 = self.get_tile_at_pos((rect.x, rect.y))
        t2 = self.get_tile_at_pos((rect.right, rect.y))
        t3 = self.get_tile_at_pos((rect.x, rect.bottom))
        t4 = self.get_tile_at_pos((rect.right, rect.bottom))
        return [t1, t2, t3, t4]
