from .pieces import Piece

class Pawn(Piece):
    def __init__(self, color, board):
        super().__init__(color, board)

    def __str__(self):
        return '♟' if self.color == "WHITE" else '♙'
    
    def add_if_empty(self, possibles, row, col):
        if self.board.get_piece(row, col) is None:
            possibles.append((row, col))

    def valid_positions(self, from_row, from_col):
        if self.color == "WHITE":
            return self.possible_positions_white(from_row, from_col) + self.possible_positions_capture_white(from_row, from_col)
        else:
            return self.possible_positions_black(from_row, from_col) + self.possible_positions_capture_black(from_row, from_col)
    
    
    def possible_positions_white(self, row, col):
        possibles = []
        if self.color == "WHITE":
            if row == 6:  # Starting position for white pawns
                self.add_if_empty(possibles, row - 1, col)
                self.add_if_empty(possibles, row - 2, col)
            elif row - 1 < 8 and self.board.get_piece(row - 1, col) is None:
                possibles.append((row - 1, col))
        return possibles

    def possible_positions_black(self, row, col):
        possibles = []
        if self.color == "BLACK":
            if row == 1:  # Starting position for black pawns
                self.add_if_empty(possibles, row + 1, col)
                self.add_if_empty(possibles, row + 2, col)
            elif row + 1 >= 0 and self.board.get_piece(row + 1, col) is None:
                possibles.append((row + 1, col))
        return possibles
    
    def possible_positions_capture_white(self, row, col):
        possibles = []
        if self.color == "WHITE":
            piece_left = self.board.get_piece(row - 1, col - 1)
            if piece_left is not None and piece_left.color != self.color:
                possibles.append((row - 1, col - 1))
            piece_right = self.board.get_piece(row - 1, col + 1)
            if piece_right is not None and piece_right.color != self.color:
                possibles.append((row - 1, col + 1))
            return possibles
        
    def possible_positions_capture_black(self, row, col):
        possibles = []
        if self.color == "BLACK":
            piece_left = self.board.get_piece(row + 1, col - 1)
            if piece_left is not None and piece_left.color != self.color:
                possibles.append((row + 1, col - 1))
            piece_right = self.board.get_piece(row + 1, col + 1)
            if piece_right is not None and piece_right.color != self.color:
                possibles.append((row + 1, col + 1))
            return possibles