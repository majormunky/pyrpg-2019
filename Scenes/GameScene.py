import pygame
from Engine.Config import get_screenrect
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
        self.overlay = None
        self.selected_rects = []
        self.debug = True

    def update(self, dt):
        self.player.update(dt, self.check_player_position)

    def draw(self, canvas):
        self.world.draw(canvas)
        self.player.draw(canvas)

        if self.debug:
            if self.selected_rects:
                canvas.blit(self.overlay, (0, 0))

    def handle_event(self, event):
        self.player.handle_event(event)

    def activate(self, data):
        pass

    def deactivate(self):
        pass

    def set_rects(self, rect_list):
        self.overlay = pygame.Surface((self.screenrect.width, self.screenrect.height), pygame.SRCALPHA)

        self.selected_rects = rect_list

        for sr in self.selected_rects:
            pygame.draw.rect(self.overlay, (0, 255, 255, 128), sr["rect"])

    def check_player_position(self, rect):
        if not self.world.rect.contains(rect):
            return False

        tile_rects = self.world.get_tiles(rect)

        if self.debug:
            self.set_rects(tile_rects)
        
        for tile in tile_rects:
            if tile["tile_data"]["solid"]:
                return False
            if tile["tile_index"] in self.world.current_map["teleport_to"].keys():
                teleport_name = self.world.current_map["teleport_to"][tile["tile_index"]]
                print("Teleporting To: ", teleport_name)
                self.world.load(teleport_name)
                player_pos = self.world.current_map["teleport_from"][self.world.old_map]
                self.player.rect.x = player_pos[0] * 32
                self.player.rect.y = player_pos[1] * 32
                return False
        return True