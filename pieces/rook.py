from .pieces import Piece

class Rook(Piece):
    def __str__(self):
        if self.__color__ == "White":
            return "♜"
        else:
            return "♖"
        
    def movement(self, from_row, from_col, to_row, to_col):
        if to_row == from_row or to_col == from_col:
            return True
        return False