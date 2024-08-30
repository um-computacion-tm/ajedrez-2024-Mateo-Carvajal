from .pieces import Piece

class King(Piece):
    def __str__(self):
        return '♚' if self.__color__ == "White" else '♔'

    def correct_movement(self, from_row, from_col, to_row, to_col):
        mov_y = abs(from_row - from_col)
        mov_x = abs(from_col - to_col)

        if mov_y > 1 or mov_x > 1:
            return False



