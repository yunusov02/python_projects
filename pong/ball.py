from config import HEIGHT, WIDTH



class Ball:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y

        self.i = 1
        self.j = 1

        self.shape = shape

    
    def move(self, game):
        if self.x + self.i < 0 or self.x + self.i >= HEIGHT:
            self.i = -self.i

        if self.y + self.j == game.player1.x:
            if game.player1.y <= self.x < game.player1.y + 2:
                self.j = -self.j

        elif self.y + self.j == game.player2.x:
            if game.player2.y <= self.x < game.player2.y + 2:
                self.j = -self.j

        if self.y + self.j < 0 or self.y + self.j >= WIDTH:
            self.reset()
            return

        self.x += self.i
        self.y += self.j

    def reset(self):
        self.x = HEIGHT // 2
        self.y = WIDTH // 2
        self.i = 1
        self.j = 1

