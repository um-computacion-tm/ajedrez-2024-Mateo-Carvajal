class Piece:
    def __init__(self, __color__, alive):
        self.__color__ = __color__
        self.alive = True

    def is_alive(self):
        return self.alive
    
    def movement(self, from_row, from_col, to_row, to_col):
        ...