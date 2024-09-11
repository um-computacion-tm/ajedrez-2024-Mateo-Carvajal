from .pieces import Piece

class Knight(Piece):
    def __init__(self, color, board):
        super().__init__(color, board)
        self.board = board  
    
    def __str__(self):
        return '♞' if self.color == "WHITE" else '♘'

    # def correct_movement(self, from_row, from_col, to_row, to_col):
    #     mov_y = abs(from_row - from_col)
    #     mov_x = abs(from_col - to_col)
        
    #     # Comprobar movimiento
    #     if (mov_y == 2 and mov_x == 1) or (mov_y == 1 and mov_x == 2):
    #         return True
    #     return False
    
    def possible_positions(self, row, col):
        possibles = []
        moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        
        for move in moves:
            new_row = row + move[0]
            new_col = col + move[1]
            if 0 <= new_row < 8 and 0 <= new_col < 8:  # Ensure within board limits
                other_piece = self.__board__.get_piece(new_row, new_col)
                if other_piece is None or other_piece.__color__ != self.__color__:
                    possibles.append((new_row, new_col))
        
        return possibles