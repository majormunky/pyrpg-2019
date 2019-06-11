import pygame
from Engine.Config import get_screenrect
from GameObjects.Player import Player

class GameScene:
    def __init__(self, manager):
        self.manager = manager
        self.screenrect = get_screenrect()
        self.player = Player()

    def update(self, dt):
        pass

    def draw(self, canvas):
        self.player.draw(canvas)

    def handle_event(self, event):
        self.player.handle_event(event)

    def activate(self, data):
        pass

    def deactivate(self):
        pass

