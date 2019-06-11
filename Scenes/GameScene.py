import pygame
from Engine.Config import get_screenrect
from GameObjects.Player import Player
from GameObjects.World import World

class GameScene:
    def __init__(self, manager):
        self.manager = manager
        self.screenrect = get_screenrect()
        self.player = Player()
        self.world = World()

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

