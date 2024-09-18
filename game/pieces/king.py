from .pieces import Piece

class King(Piece):
    def __init__(self, color, board):
        super().__init__(color, board)  # Initialize the color attribute using the parent class constructor
        self.board = board  # Initialize the board attribute

    white_str = "♚"
    black_str = "♔"

    def __str__(self):
        return self.white_str if self.color == "WHITE" else self.black_str

    # def correct_movement(self, from_row, from_col, to_row, to_col):
    #     mov_y = abs(from_row - from_col)
    #     mov_x = abs(from_col - to_col)

    #     if mov_y > 1 or mov_x > 1:
    #         return False

    def valid_positions(self, row, col):
        possibles = []
        possibles += self.possible_positions_vertical(row, col)
        possibles += self.possible_positions_horizontal(row, col)
        possibles += self.possible_positions_diagonal(row, col)
        return possibles        

    def possible_positions_vertical(self, row, col):
        possibles = []
        # Comprueba la fila de arriba
        if row + 1 < 8:  # # Se asegura que se este dentro de los limites del tablero
            other_piece = self.board.get_piece(row + 1, col)
            if other_piece is None or other_piece.color != self.color:
                possibles.append((row + 1, col))
        
        # Comprueba la fila de abajo
        if row - 1 >= 0:  # Se asegura que se este dentro de los limites del tablero
            other_piece = self.board.get_piece(row - 1, col)
            if other_piece is None or other_piece.color != self.color:
                possibles.append((row - 1, col))
        
        return possibles    
    
    def possible_positions_horizontal(self, row, col):
        possibles = []
        # Comprueba la columna a la derecha
        if col + 1 < 8:
            other_piece = self.board.get_piece(row, col + 1)
            if other_piece is None or other_piece.color != self.color:
                possibles.append((row, col + 1))
        
        # Comprueba la columna a la izquierda
        if col - 1 >= 0: 
            other_piece = self.board.get_piece(row, col - 1)
            if other_piece is None or other_piece.color != self.color:
                possibles.append((row, col - 1))
        
        return possibles
    
    def possible_positions_diagonal(self, row, col):
        possibles = []
        # comprueba la diagonal de abajo a la derecha
        if row + 1 < 8 and col + 1 < 8:  # Se asegura que se este dentro de los limites del tablero
            other_piece = self.board.get_piece(row + 1, col + 1)
            if other_piece is None or other_piece.color != self.color:
                possibles.append((row + 1, col + 1))
        
        # comprueba la diagonal de abajo a la izquierda
        if row + 1 < 8 and col - 1 >= 0:  
            other_piece = self.board.get_piece(row + 1, col - 1)
            if other_piece is None or other_piece.color != self.color:
                possibles.append((row + 1, col - 1))
        
        # comprueba la diagonal de arriba a la derecha
        if row - 1 >= 0 and col + 1 < 8:  
            other_piece = self.board.get_piece(row - 1, col + 1)
            if other_piece is None or other_piece.color != self.color:
                possibles.append((row - 1, col + 1))
        
        # comprueba la diagonal de arriba a la izquierda
        if row - 1 >= 0 and col - 1 >= 0:  
            other_piece = self.board.get_piece(row - 1, col - 1)
            if other_piece is None or other_piece.color != self.color:
                possibles.append((row - 1, col - 1))
        
        return possibles