import os
import random
from pole import Pole
from cell import Cell
from config import NUMBERS, GameStatus

def game(pole_size):
    pole = Pole(pole_size)

    pole.game_status = GameStatus.PLAYING

    while True:
        value = random.choice(NUMBERS)
        x, y = random.choice(pole.free_cells())
        pole.pole[x][y].set_val(value)

        os.system("clear")

        game_over = pole.check_game_status()

        if game_over == GameStatus.GAME_OVER:
            print(f"Game OVER\nYour current Score is: {pole.score}")
            break

        elif game_over == GameStatus.WIN:
            print(f"You WIN\nYour current Score is: {pole.score}")
            break

        pole.show_pole()
        command = input("Enter commands(W S A D): ").lower()

        if command == "w":
            pole.up()
        elif command == "s":
            pole.down()
        elif command == "a":
            pole.left()
        elif command == "d":
            pole.right()

