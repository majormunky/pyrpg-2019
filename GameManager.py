import pygame
from Engine.SceneManager import SceneManager
from Scenes.IntroScene import IntroScene


class GameManager:
    def __init__(self):
        self.scenes = SceneManager(self)
        self.scenes.add_scene("Intro", IntroScene)
        self.scenes.change_scene("Intro")

    def update(self, dt):
        self.scenes.update(dt)

    def draw(self, canvas):
        self.scenes.draw(canvas)

    def handle_event(self, event):
        self.scenes.handle_event(event)
