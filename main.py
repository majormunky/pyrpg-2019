from Engine.Engine import Engine
from GameManager import GameManager


if __name__ == "__main__":
    e = Engine(GameManager)
    e.game_loop()
