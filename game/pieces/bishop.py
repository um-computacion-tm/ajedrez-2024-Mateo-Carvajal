from .pieces import Piece

class Bishop(Piece):
    def __str__(self):
        return '♝' if self.color == "WHITE" else '♗'
    
    def correct_movement(self, from_row, from_col, to_row, to_col):
        #movimiento correcto diagonal
        if abs(to_row - from_row) == abs(to_col - from_col):
            return True
        
    def possible_positions_top_right(self, row, col):
        possibles = []
        # Check the top-right diagonal
        for i in range(1, 8):
            if row + i < 8 and col + i < 8:
                other_piece = self.__board__.get_piece(row + i, col + i)
                if other_piece is None:
                    possibles.append((row + i, col + i))
                elif other_piece.__color__ != self.__color__:
                    possibles.append((row + i, col + i))
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
            if row + i < 8 and col - i >= 0:
                other_piece = self.__board__.get_piece(row - i, col - i)
                if other_piece is None:
                    possibles.append((row - i, col - i))
                elif other_piece.__color__ != self.__color__:
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
                elif other_piece.__color__ != self.__color__:
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
            if row - i >= 0 and col - i >= 0:
                other_piece = self.__board__.get_piece(row - i, col - i)
                if other_piece is None:
                    possibles.append((row - i, col - i))
                elif other_piece.__color__ != self.__color__:
                    possibles.append((row - i, col - i))
                    break
                else:
                    break
            else:
                break
        
        return possibles