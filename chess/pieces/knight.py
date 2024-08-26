from .pieces import Piece

class Knight(Piece):
    def __str__(self):
        return '♞' if self.__color__ == "White" else '♘'

    def correct_movement(self, from_row, from_col, to_row, to_col):
        mov_y = abs(from_row - from_col)
        mov_x = abs(from_col - to_col)
        if mov_y == 2 and mov_x != 1:
            return False
        elif mov_x == 2 and mov_y != 1:
            return False
        #control coordenadas
        if from_col < 0 or from_row < 0 or to_col < 0 or to_row < 0 or from_col > 7 or from_row > 7 or to_col > 7 or to_row > 7:
            return False
        else:
            return True