from enum import Enum


class GameStatus(Enum):
    NOT_STARTED = 1
    PLAYING = 2
    WIN = 3
    GAME_OVER = 4

class PoleStatus(Enum):
    FREE = 1
    FILLED = 2

NUMBERS = [2, 4]