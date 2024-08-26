from .pieces import Piece

class Bishop(Piece):
    def __str__(self):
        return '♝' if self.__color__ == "White" else '♗'
    
    def correct_movement(self, from_row, from_col, to_row, to_col):
        #movimiento correcto diagonal
        if abs(to_row - from_row) == abs(to_col - from_col):
            return True
        #control coordenadas
        if from_col < 0 or from_row < 0 or to_col < 0 or to_row < 0 or from_col > 7 or from_row > 7 or to_col > 7 or to_row > 7:
            return False
        else:
            return True