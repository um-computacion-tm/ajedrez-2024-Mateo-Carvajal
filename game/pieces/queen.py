from .pieces import Piece

class Queen(Piece):
    def __str__(self):
        return '♛' if self.color == "White" else '♕'

    def correct_movement(self, from_row, from_col, to_row, to_col):
        #movimiento correcto unidireccional
        if to_row == from_row or to_col == from_col:
            return True
        #movimiento correcto diagonal
        elif abs(to_row - from_row) == abs(to_col - from_col):
            return True
        else:
            return False