from .pieces import Piece

class Pawn(Piece):
    def __init__(self, color, board):
        super().__init__(color, board)

    def __str__(self):
        return '♟' if self.color == "WHITE" else '♙'

    def valid_positions(self, from_row, from_col):
        if self.color == "WHITE":
            return self.possible_positions_white(from_row, from_col)
        else:
            return self.possible_positions_black(from_row, from_col)
    
    def possible_positions_white(self, row, col):
        possibles = []
        if self.color == "WHITE":
            if row == 6:  # Starting position for white pawns
                if self.board.get_piece(row - 1, col) is None:
                    possibles.append((row - 1, col))
                if self.board.get_piece(row - 2, col) is None:
                    possibles.append((row - 2, col))
            elif row - 1 < 8 and self.board.get_piece(row - 1, col) is None:
                possibles.append((row - 1, col))
        return possibles

    def possible_positions_black(self, row, col):
        possibles = []
        if self.color == "BLACK":
            if row == 1:  # Starting position for black pawns
                if self.board.get_piece(row + 1, col) is None:
                    possibles.append((row + 1, col))
                if self.board.get_piece(row + 2, col) is None:
                    possibles.append((row + 2, col))
            elif row + 1 >= 0 and self.board.get_piece(row + 1, col) is None:
                possibles.append((row + 1, col))
        return possibles