from config import HEIGHT

class Player:
    def __init__(self, x, y, name, shape):
        self.__x = x
        self.__y = y
        self.name = name
        self.shape = shape
        self.score = 0

    @property
    def y(self):
        return self.__y
    
    @property
    def x(self):
        return self.__x

    def get_name(self):
        return self.name
    
    def get_shape(self):
        return self.shape
    
    def get_score(self):
        return self.score

    def increase_score(self):
        self.score += 1

    def up(self):
        if self.__check_moving(self.__y - 1):
            self.__y -= 1
    
    def down(self):
        if self.__check_moving(self.__y + 1):
            self.__y += 1

    def __check_moving(self, coord):
        return 0 <= coord <= HEIGHT - 3
    
