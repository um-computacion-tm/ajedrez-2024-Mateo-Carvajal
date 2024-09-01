from .pieces import Piece

class King(Piece):
    def __init__(self, color, board):
        super().__init__(color, board)
        self.color = color
    white_str = "♚"
    black_str = "♔"

    # def correct_movement(self, from_row, from_col, to_row, to_col):
    #     mov_y = abs(from_row - from_col)
    #     mov_x = abs(from_col - to_col)

    #     if mov_y > 1 or mov_x > 1:
    #         return False

    def possible_positions_vertical(self, row, col):
        possibles = []
        # Comprueba la fila de arriba
        if row + 1 < 8:  # # Se asegura que se este dentro de los limites del tablero
            other_piece = self.__board__.get_piece(row + 1, col)
            if other_piece is None or other_piece.__color__ != self.__color__:
                possibles.append((row + 1, col))
        
        # Comprueba la fila de abajo
        if row - 1 >= 0:  # Se asegura que se este dentro de los limites del tablero
            other_piece = self.__board__.get_piece(row - 1, col)
            if other_piece is None or other_piece.__color__ != self.__color__:
                possibles.append((row - 1, col))
        
        return possibles    
    
    def possible_positions_horizontal(self, row, col):
        possibles = []
        # Comprueba la columna a la derecha
        if col + 1 < 8:
            other_piece = self.__board__.get_piece(row, col + 1)
            if other_piece is None or other_piece.__color__ != self.__color__:
                possibles.append((row, col + 1))
        
        # Comprueba la columna a la izquierda
        if col - 1 >= 0: 
            other_piece = self.__board__.get_piece(row, col - 1)
            if other_piece is None or other_piece.__color__ != self.__color__:
                possibles.append((row, col - 1))
        
        return possibles