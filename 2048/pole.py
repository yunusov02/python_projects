from cell import Cell
from config import GameStatus, PoleStatus

class Pole:

    def __init__(self, size):
        self.size = size
        self.pole = [[Cell() for _ in range(size)] for _ in range(size)]
        self.game_status = GameStatus.NOT_STARTED
        self.score = 0


    def free_cells(self):
        return [(x, y) for x in range(self.size) for y in range(self.size) if self.pole[x][y].is_free()]
    

    def left(self):
        for i in range(self.size):
            row = self.pole[i]

            row = [cell for cell in row if cell.val != 0]

            j = 0
            while j < len(row) - 1:
                if row[j] == row[j + 1]:
                    row[j] += row[j + 1]
                    self.score += row[j].val
                    row.pop(j + 1)
                j += 1
        
            row.extend(Cell() for _ in range(self.size - len(row)))
        
            self.pole[i] = row
                    

    def right(self):
        for i in range(self.size):
            row = self.pole[i]

            row = [cell for cell in row if cell.val != 0]

            j = 1
            while j < len(row):
                if row[j] == row[j-1]:
                    row[j] += row[j-1]
                    self.score += row[j].val
                    row.pop(j-1)
                j += 1
            
            row = [Cell() for _ in range(self.size - len(row))] + row

            self.pole[i] = row


    def up(self):

        for i in range(self.size):
            column = []
            
            for j in range(self.size):
                column.append(self.pole[j][i])
            
            column = [cell for cell in column if cell.val != 0]

            j = 0
            while j < len(column) - 1:
                if column[j] == column[j+1]:
                    column[j] += column[j+1]
                    self.score += column[j].val
                    column.pop(j+1)
                j += 1
            
            column += [Cell() for _ in range(self.size - len(column))]

            for index in range(self.size):
                self.pole[index][i] = column[index]


    def down(self):
        for i in range(self.size):
            column = []
            
            for j in range(self.size):
                column.append(self.pole[j][i])
            
            column = [cell for cell in column if cell.val != 0]

            j = 0
            while j < len(column) - 1:
                if column[j] == column[j+1]:
                    column[j] += column[j+1]
                    self.score += column[j].val
                    column.pop(j+1)
                j += 1
            
            column = [Cell() for _ in range(self.size - len(column))] + column

            for index in range(self.size):
                self.pole[index][i] = column[index]
    

    def show_pole(self):
        for row in self.pole:
            for cell in row:
                print(f"{cell.val}".ljust(3), end=" ")
            print()

        print()
        print("Your current score: ", self.score)

    def check_game_status(self):

        for row in self.pole:
            for cell in row:
                if cell.val >= 2048:
                    return GameStatus.WIN
                if cell.is_free():
                    return GameStatus.PLAYING
    
        return GameStatus.GAME_OVER

