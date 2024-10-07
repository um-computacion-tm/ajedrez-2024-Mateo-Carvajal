from .pieces import Piece
from .bishop import Bishop
from .rook import Rook

class Queen(Piece):
    def __init__(self, color, board):
        super().__init__(color, board)
        self.rook = Rook(color, board)  
        self.bishop = Bishop(color, board)  

    #Define la representación de la pieza
    def __str__(self):
        return '♛' if self.color == "WHITE" else '♕'

    #Devuelve una lista con todas los posibles movimientos para la pieza        
    def valid_positions(self, row, col):
        rook_positions = self.rook.valid_positions(row, col)
        bishop_positions = self.bishop.valid_positions(row, col)
        return rook_positions + bishop_positions