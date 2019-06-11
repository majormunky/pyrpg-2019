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
        self.world = World(levels.data["World"])

    def update(self, dt):
        pass

    def draw(self, canvas):
        self.world.draw(canvas)
        self.player.draw(canvas)

    def handle_event(self, event):
        self.player.handle_event(event)

    def activate(self, data):
        pass

    def deactivate(self):
        pass

