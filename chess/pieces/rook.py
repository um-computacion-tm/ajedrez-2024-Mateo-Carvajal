from .pieces import Piece

class Rook(Piece):
    def __init__(self, color, board):
        super().__init__(color, board)
        self.color = color
    white_str = "♜"
    black_str = "♖"

    def __str__(self):
        return "♜" if self.color == "WHITE" else "♖"
    
    def valid_positions(self, from_row, from_col, to_row, to_col):
        possible_positions = (
            self.possible_positions_vd(from_row, from_col) + 
            self.possible_positions_va(from_row, from_col))
         
        return (to_row, to_col) in possible_positions
    

    def possible_positions_vd(self, row, col):
        possibles = []
        for next_row in range(row + 1, 8):
            # que la celda que sigue no este ocupada..
            other_piece = self.__board__.get_piece(next_row, col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((next_row, col))
                break
            possibles.append((next_row, col))
        return possibles

    def possible_positions_va(self, row, col):
        possibles = []
        for next_row in range(row - 1, -1, -1):
            other_piece = self.__board__.get_piece(next_row, col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((next_row, col))
                break
            possibles.append((next_row, col))
        return possibles

    def possible_positions_hr(self, row, col):
        possibles = []
        for next_col in range(col + 1, 8):
            other_piece = self.__board__.get_piece(row, next_col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((row, next_col))
                break
            possibles.append((row, next_col))
        return possibles
    
    def possible_positions_hl(self, row, col):
        possibles = []
        for next_col in range(col - 1, -1, -1):
            other_piece = self.__board__.get_piece(row, next_col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((row, next_col))
                break
            possibles.append((row, next_col))
        return possibles
        
    def correct_movement(self, from_row, from_col, to_row, to_col):
        #control coordenadas
        if from_col < 0 or from_row < 0 or to_col < 0 or to_row < 0 or from_col > 7 or from_row > 7 or to_col > 7 or to_row > 7:
            return False
        #movimiento correcto
        if to_row == from_row or to_col == from_col:
            return True
        elif to_row != from_row and to_col != from_col:
            return False
        
