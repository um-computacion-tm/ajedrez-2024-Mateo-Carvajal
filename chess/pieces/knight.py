from .pieces import Piece

class Knight(Piece):
    def __str__(self):
        return '♞' if self.__color__ == "White" else '♘'

    def correct_movement(self, from_row, from_col, to_row, to_col):
        mov_y = abs(from_row - from_col)
        mov_x = abs(from_col - to_col)
        
        # Comprobar movimiento
        if (mov_y == 2 and mov_x == 1) or (mov_y == 1 and mov_x == 2):
            return True
        return False
        
