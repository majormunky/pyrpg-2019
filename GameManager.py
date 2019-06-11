import pygame
from Engine.SceneManager import SceneManager
from Scenes.IntroScene import IntroScene
from Scenes.GameScene import GameScene


class GameManager:
    def __init__(self):
        self.scenes = SceneManager(self)
        self.scenes.add_scene("Intro", IntroScene)
        self.scenes.add_scene("Game", GameScene)
        self.scenes.change_scene("Intro")

    def update(self, dt):
        self.scenes.update(dt)

    def draw(self, canvas):
        self.scenes.draw(canvas)

    def handle_event(self, event):
        self.scenes.handle_event(event)

    def change_scene(self, new_scene):
        self.scenes.change_scene(new_scene)
