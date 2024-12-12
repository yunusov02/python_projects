import os

from ball import Ball
from player import Player
from config import GameStatus, HEIGHT, WIDTH

class Game:
    def __init__(self):
        self.player1 = Player(x=0, y=12, name="Player 1", shape="|")
        self.player2 = Player(x=50, y=12, name="Player 2", shape="|")
        self.ball = Ball(x=HEIGHT // 2 + 1, y=WIDTH // 2 + 1, shape="o")

        self.pole = [[" " for _ in range(WIDTH)] for _ in range(HEIGHT)]

        self.game_status = GameStatus.PLAYING


    def show_pole(self):
        os.system('clear')
        print("_" * (WIDTH * 2 + 3))

        for i in range(HEIGHT):
            print("|", end=" ")
            for j in range(WIDTH):
                if j == self.player1.x and self.player1.y <= i < self.player1.y + 3:
                    print(self.player1.shape, end=" ")

                elif j == self.player2.x and self.player2.y <= i < self.player2.y + 3:
                    print(self.player2.shape, end=" ")

                elif i == self.ball.x and j == self.ball.y:
                    print(self.ball.shape, end=" ")

                elif j == WIDTH // 2 + 1:
                    print("|", end=" ")

                else:
                    print(self.pole[i][j], end=" ")  
            print("|")
        
        print("_" * (WIDTH * 2 + 3))
        

    def game(self):
        while self.game_status == GameStatus.PLAYING:
            
            self.show_pole()

            command = input().lower()

            if command == "a":
                self.player1.up()
            elif command == "z":
                self.player1.down()
            elif command == "k":
                self.player2.up()
            elif command == "m":
                self.player2.down()
            elif command == " ":
                self.ball.move()
    

    def __check_game_status(self):
        if self.ball.is_goal():
            self.game_status = GameStatus.GOAL
        elif self.player1.get_score() < 3 and self.player2.get_score() < 3:
            self.game_status = GameStatus.PLAYING



game = Game()
game.game()



