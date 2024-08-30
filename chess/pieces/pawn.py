from .pieces import Piece

class Pawn(Piece):
    def __str__(self):
        return '♟' if self.__color__ == "WHITE" else '♙'
    
    def correct_movement(self, from_row, from_col, to_row, to_col):
        mov_y = abs(to_row - from_row)
        mov_x = abs(to_col - from_col)
        
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
    
    def possible_positions_first_move_white(self, row, col):
        possibles = []
        for next_row in range(row - 1, 3, -1):
            other_piece = self.__board__.get_piece(next_row, col)
            if other_piece is None:
                possibles.append((next_row, col))
            else:
                break
        return possibles
    
    def possible_positions_first_move_black(self, row, col):
        possibles = []
        for next_row in range(row + 1, 4, 1):
            other_piece = self.__board__.get_piece(next_row, col)
            if other_piece is None:
                possibles.append((next_row, col))
            else:
                break
        return possibles
    
    def is_within_board_and_empty(self, possibles, next_row, col):
        if next_row >= 0:  # Se asegura que next_row esté dentro del tablero
                other_piece = self.__board__.get_piece(next_row, col)
                if other_piece is None:
                    possibles.append((next_row, col))
 
    def possible_positions_white(self, row, col):
        possibles = []
        next_row = row - 1
        self.is_within_board_and_empty(possibles, next_row, col)
        return possibles
    
    def possible_positions_black(self, row, col):
        possibles = []
        next_row = row + 1
        self.is_within_board_and_empty(possibles, next_row, col)
        return possibles