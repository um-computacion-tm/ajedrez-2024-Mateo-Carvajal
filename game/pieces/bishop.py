from .pieces import Piece
from .utils import gather_positions

class Bishop(Piece):
    def __init__(self, color, board):
        super().__init__(color, board)

    #Define la representación de la pieza
    def __str__(self):
        return '♝' if self.get_color() == "WHITE" else '♗'
        
    #Devuelve una lista con todas los posibles movimientos para la pieza
    def valid_positions(self, from_row, from_col):
        return gather_positions(
            from_row, from_col,
            self.possible_positions_top_right,
            self.possible_positions_top_left,
            self.possible_positions_bottom_right,
            self.possible_positions_bottom_left
        )
        
    def possible_positions_top_right(self, row, col):
        possibles = []
        # Check the top-right diagonal
        for i in range(1, 8):
            if row - i >= 0 and col + i < 8:
                other_piece = self.__board__.get_piece(row - i, col + i)
                if other_piece is None:
                    possibles.append((row - i, col + i))
                elif other_piece.get_color() != self.get_color():
                    possibles.append((row - i, col + i))
                    break
                else:
                    break
            else:
                break
        return possibles
        
    def possible_positions_top_left(self, row, col):
        possibles = []
        # Check the top-left diagonal
        for i in range(1, 8):
            if row - i >= 0 and col - i >= 0:
                other_piece = self.__board__.get_piece(row - i, col - i)
                if other_piece is None:
                    possibles.append((row - i, col - i))
                elif other_piece.get_color() != self.get_color():
                    possibles.append((row - i, col - i))
                    break
                else:
                    break
            else:
                break
        return possibles

    def possible_positions_bottom_right(self, row, col): 
        possibles = []
        # Check the bottom-right diagonal
        for i in range(1, 8):
            if row + i < 8 and col + i < 8:
                other_piece = self.__board__.get_piece(row + i, col + i)
                if other_piece is None:
                    possibles.append((row + i, col + i))
                elif other_piece.get_color() != self.get_color():
                    possibles.append((row + i, col + i))
                    break
                else:
                    break
            else:
                break
        return possibles
        
    def possible_positions_bottom_left(self, row, col):
        possibles = []
        # Check the bottom-left diagonal
        for i in range(1, 8):
            if row + i < 8 and col - i >= 0:
                other_piece = self.__board__.get_piece(row + i, col - i)
                if other_piece is None:
                    possibles.append((row + i, col - i))
                elif other_piece.get_color() != self.get_color():
                    possibles.append((row + i, col - i))
                    break
                else:
                    break
            else:
                break
        
        return possibles