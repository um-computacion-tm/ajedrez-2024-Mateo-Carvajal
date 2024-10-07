from .pieces import Piece
from .utils import gather_positions

class King(Piece):
    def __init__(self, color, board):
        super().__init__(color, board)          
    white_str = "♚"
    black_str = "♔"

    #Define la representación de la pieza
    def __str__(self):
        return self.white_str if self.color == "WHITE" else self.black_str

    #Devuelve una lista con todas los posibles movimientos para la pieza
    def valid_positions(self, row, col):
        return gather_positions(
            row, col,
            self.possible_positions_vertical,
            self.possible_positions_horizontal,
            self.possible_positions_lower_diagonal,
            self.possible_positions_upper_diagonal
        )      

    def possible_positions_vertical(self, row, col):
        possibles = []
        # Comprueba la fila de arriba
        if row + 1 < 8:  # Se asegura que se este dentro de los limites del tablero
            other_piece = self.__board__.get_piece(row + 1, col)
            if other_piece is None or other_piece.color != self.color:
                possibles.append((row + 1, col))
        
        # Comprueba la fila de abajo
        if row - 1 >= 0:  
            other_piece = self.__board__.get_piece(row - 1, col)
            if other_piece is None or other_piece.color != self.color:
                possibles.append((row - 1, col))
        
        return possibles    
    
    def possible_positions_horizontal(self, row, col):
        possibles = []
        # Comprueba la columna a la derecha
        if col + 1 < 8:
            other_piece = self.__board__.get_piece(row, col + 1)
            if other_piece is None or other_piece.color != self.color:
                possibles.append((row, col + 1))
        
        # Comprueba la columna a la izquierda
        if col - 1 >= 0: 
            other_piece = self.__board__.get_piece(row, col - 1)
            if other_piece is None or other_piece.color != self.color:
                possibles.append((row, col - 1))
        
        return possibles
    
    def possible_positions_upper_diagonal(self, row, col):
        possibles = []

        # comprueba la diagonal de arriba a la derecha
        if row - 1 >= 0 and col + 1 < 8:  
            other_piece = self.__board__.get_piece(row - 1, col + 1)
            if other_piece is None or other_piece.color != self.color:
                possibles.append((row - 1, col + 1))
        
        # comprueba la diagonal de arriba a la izquierda
        if row - 1 >= 0 and col - 1 >= 0:  
            other_piece = self.__board__.get_piece(row - 1, col - 1)
            if other_piece is None or other_piece.color != self.color:
                possibles.append((row - 1, col - 1))
        
        return possibles
    
    def possible_positions_lower_diagonal(self, row, col):
        possibles = []
        # comprueba la diagonal de abajo a la derecha
        if row + 1 < 8 and col + 1 < 8:  
            other_piece = self.__board__.get_piece(row + 1, col + 1)
            if other_piece is None or other_piece.color != self.color:
                possibles.append((row + 1, col + 1))
        
        # comprueba la diagonal de abajo a la izquierda
        if row + 1 < 8 and col - 1 >= 0:  
            other_piece = self.__board__.get_piece(row + 1, col - 1)
            if other_piece is None or other_piece.color != self.color:
                possibles.append((row + 1, col - 1))
        
        return possibles
    