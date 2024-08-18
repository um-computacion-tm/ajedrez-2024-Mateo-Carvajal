class Piece:
    def __init__(self, color, is_alive):
        self.color = color
        self.__alive__ = True

    def is_alive(self):
        return self.__alive__
    

