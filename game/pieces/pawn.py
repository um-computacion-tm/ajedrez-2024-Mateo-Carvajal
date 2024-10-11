from .pieces import Piece

class Pawn(Piece):
    def __init__(self, color, board):
        super().__init__(color, board)

    #Define la representación de la pieza
    def __str__(self):
        return '♟' if self.get_color() == "WHITE" else '♙'
    
    #Añade una posición a la lista de posibles si está vacía
    def add_if_empty(self, possibles, row, col):
        if self.__board__.get_piece(row, col) is None:
            possibles.append((row, col))

    #Devuelve una lista con todas los posibles movimientos para la pieza
    def valid_positions(self, from_row, from_col):
        if self.get_color() == "WHITE":
            return self.possible_positions_white(from_row, from_col) + self.possible_positions_capture_white(from_row, from_col)
        else:
            return self.possible_positions_black(from_row, from_col) + self.possible_positions_capture_black(from_row, from_col)
    

    def possible_positions_white(self, row, col):
        possibles = []
        if self.get_color() == "WHITE":
            if row == 6:  # Posición inicial para peones blancos
                self.add_if_empty(possibles, row - 1, col)
                self.add_if_empty(possibles, row - 2, col)
            elif row - 1 < 8 and self.__board__.get_piece(row - 1, col) is None:
                possibles.append((row - 1, col))
        return possibles

    def possible_positions_black(self, row, col):
        possibles = []
        if self.get_color() == "BLACK":
            if row == 1:  # Posición inicial para peones negros
                self.add_if_empty(possibles, row + 1, col)
                self.add_if_empty(possibles, row + 2, col)
            elif row + 1 >= 0 and self.__board__.get_piece(row + 1, col) is None:
                possibles.append((row + 1, col))
        return possibles
    
    def possible_positions_capture_white(self, row, col):
        possibles = []
        if self.get_color() == "WHITE":
            piece_left = self.__board__.get_piece(row - 1, col - 1)
            if piece_left is not None and piece_left.get_color() != self.get_color:
                possibles.append((row - 1, col - 1))
            piece_right = self.__board__.get_piece(row - 1, col + 1)
            if piece_right is not None and piece_right.get_color() != self.get_color():
                possibles.append((row - 1, col + 1))
            return possibles
        
    def possible_positions_capture_black(self, row, col):
        possibles = []
        if self.get_color() == "BLACK":
            piece_left = self.__board__.get_piece(row + 1, col - 1)
            if piece_left is not None and piece_left.get_color() != self.get_color():
                possibles.append((row + 1, col - 1))
            piece_right = self.__board__.get_piece(row + 1, col + 1)
            if piece_right is not None and piece_right.get_color() != self.get_color():
                possibles.append((row + 1, col + 1))
            return possibles