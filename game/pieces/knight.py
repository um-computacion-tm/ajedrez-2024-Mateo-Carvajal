from .pieces import Piece

class Knight(Piece):
    def __init__(self, color, board):
        super().__init__(color, board)
    
    #Define la representación de la pieza
    def __str__(self):
        return '♞' if self.get_color() == "WHITE" else '♘'

    #Devuelve una lista con todas los posibles movimientos para la pieza
    def valid_positions(self, row, col):
        possibles = []
        moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        
        for move in moves:
            new_row = row + move[0]
            new_col = col + move[1]
            if 0 <= new_row < 8 and 0 <= new_col < 8:  # Asegura que la posición está dentro del tablero
                other_piece = self.__board__.get_piece(new_row, new_col)
                if other_piece is None or other_piece.get_color() != self.get_color():
                    possibles.append((new_row, new_col))
        
        return possibles