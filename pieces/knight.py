from .pieces import Piece

class Knight(Piece):
    def __str__(self):
        return '♞' if self.__color__ == "White" else '♘'

    def correct_movement(self, from_row, from_col, to_row, to_col):
         row_diff = abs(from_row - from_col)
         col_diff = abs(from_col - to_col)
         return (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)