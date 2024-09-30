from .pieces import Piece
from .bishop import Bishop
from .rook import Rook

class Queen(Piece):
    def __init__(self, color, board):
        super().__init__(color, board)
        self.rook = Rook(color, board)  
        self.bishop = Bishop(color, board)  
        self.__board__ = board

    def __str__(self):
        return '♛' if self.color == "WHITE" else '♕'

    # def correct_movement(self, from_row, from_col, to_row, to_col):
    #     #movimiento correcto unidireccional
    #     if to_row == from_row or to_col == from_col:
    #         return True
    #     #movimiento correcto diagonal
    #     elif abs(to_row - from_row) == abs(to_col - from_col):
    #         return True
    #     else:
    #         return False
        
    def valid_positions(self, row, col):
        rook_positions = self.rook.valid_positions(row, col)
        bishop_positions = self.bishop.valid_positions(row, col)
        return rook_positions + bishop_positions