import pygame
from Engine.Config import get_screenrect
from Engine.Camera import Camera
from GameObjects.Player import Player
from GameObjects.World import World
from Data import levels


class GameScene:
    def __init__(self, manager):
        self.manager = manager
        self.screenrect = get_screenrect()
        self.player = Player(64, 64)
        self.world = World(levels.data)
        self.world.load("World")
        self.camera = Camera()

        # ?
        self.map_pad = 128

    def update(self, dt):
        self.player.update(dt, self.check_player_position)

    def draw(self, canvas):
        camera_rect = self.camera.get_rect()
        self.world.draw(canvas, camera_rect)
        self.player.draw(canvas, camera_rect)

    def handle_event(self, event):
        self.player.handle_event(event)

    def activate(self, data):
        pass

    def deactivate(self):
        pass

    def move_camera(self, x, y):
        self.camera.x = x
        self.camera.y = y

    def check_player_position(self, rect, direction):
        fixed_rect = pygame.Rect(
            rect.x + self.camera.x, rect.y + self.camera.y, rect.width, rect.height
        )

        if not self.screenrect.contains(rect):
            print("Player is offscreen")
            return False

        tile_rects = self.world.get_tiles(fixed_rect)

        for tile in tile_rects:
            if tile["tile_index"] in self.world.current_map["teleport_to"].keys():
                teleport_name = self.world.current_map["teleport_to"][
                    tile["tile_index"]
                ]
                self.world.load(teleport_name)
                player_pos = self.world.current_map["teleport_from"][self.world.old_map]
                self.player.rect.x = player_pos[0] * 32
                self.player.rect.y = player_pos[1] * 32
                return False
            if tile["tile_data"]["solid"]:
                return False

        map_rect = self.world.get_rect()
        camera_rect = self.camera.get_rect()
        has_moved = False

        dx = abs(rect.x - self.player.rect.x)
        dy = abs(rect.y - self.player.rect.y)

        if map_rect.contains(rect) and self.screenrect.contains(rect):
            if direction == "right":
                if rect.right > self.screenrect.width - self.map_pad:
                    camera_rect.x += dx
                    camera_moved = self.camera.move(camera_rect, map_rect)
                    if not camera_moved:
                        has_moved = True
                else:
                    has_moved = True
            elif direction == "left":
                if rect.x < self.map_pad:
                    camera_rect.x -= dx
                    camera_moved = self.camera.move(camera_rect, map_rect)
                    if not camera_moved:
                        has_moved = True
                else:
                    has_moved = True
            elif direction == "up":
                if rect.y < self.map_pad:
                    camera_rect.y -= dy
                    camera_moved = self.camera.move(camera_rect, map_rect)
                    if not camera_moved:
                        has_moved = True
                else:
                    has_moved = True
            elif direction == "down":
                if rect.y > self.screenrect.height - self.map_pad:
                    camera_rect.y += dy
                    camera_moved = self.camera.move(camera_rect, map_rect)
                    if not camera_moved:
                        has_moved = True
                else:
                    has_moved = True
        return has_moved
