from .pieces import Piece

class Pawn(Piece):
    def __str__(self):
        return '♟' if self.__color__ == "White" else '♙'
    
    def correct_movement(self, from_row, from_col, to_row, to_col):
        mov_y = abs(to_row - from_row)
        mov_x = abs(to_col - from_col)
        
        #control coordenadas
        if from_col < 0 or from_row < 0 or to_col < 0 or to_row < 0 or from_col > 7 or from_row > 7 or to_col > 7 or to_row > 7:
            return False
        # Movimientos posibles en posicion inicial de peon
        if from_row == 1 and self.__color__ == "Black":
            if mov_y not in [1, 2] or mov_x != 0:
                return False
        elif from_row == 6 and self.__color__ == "White":
            if mov_y not in [1, 2] or mov_x != 0:
                return False
        # Movimientos posibles en cualquier otra posicion
        else:
            mov_y != 1 or mov_x != 0
            return False
 
