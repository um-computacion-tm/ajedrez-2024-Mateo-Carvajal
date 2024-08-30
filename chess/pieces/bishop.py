from .pieces import Piece

class Bishop(Piece):
    def __str__(self):
        return '♝' if self.__color__ == "White" else '♗'
    
    def correct_movement(self, from_row, from_col, to_row, to_col):
        #movimiento correcto diagonal
        if abs(to_row - from_row) == abs(to_col - from_col):
            return True