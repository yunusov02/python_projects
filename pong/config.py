from enum import Enum


HEIGHT = 25
WIDTH = 51


class GameStatus(Enum):
    PLAYING = 1
    GOAL = 2
    END = 3
