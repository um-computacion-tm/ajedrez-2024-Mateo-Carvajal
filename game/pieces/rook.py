from .pieces import Piece

class Rook(Piece):
    def __init__(self, color, board):
        super().__init__(color, board)
        self.color = color
    white_str = "♜"
    black_str = "♖"

    def __str__(self):
        return "♜" if self.color == "WHITE" else "♖"
    
    def valid_positions(self, from_row, from_col, to_row, to_col):
        possible_positions = (
            self.possible_positions_vd(from_row, from_col) + 
            self.possible_positions_va(from_row, from_col))
        return (to_row, to_col) in possible_positions
        
    def traverse_direction(self, row, col, row_step, col_step):
        possibles = []
        current_row, current_col = row + row_step, col + col_step

        # Mientras esté dentro de los límites del tablero
        while 0 <= current_row < 8 and 0 <= current_col < 8:
            other_piece = self.board.get_piece(current_row, current_col)
            if other_piece is not None:
                if other_piece.color != self.color:
                    possibles.append((current_row, current_col))
                break
            possibles.append((current_row, current_col))
            current_row += row_step
            current_col += col_step

        return possibles

    def possible_positions_vd(self, row, col):
        return self.traverse_direction(row, col, 1, 0)  # Movimiento hacia abajo
    
    def possible_positions_va(self, row, col):
        return self.traverse_direction(row, col, -1, 0)  # Movimiento hacia arriba

    def possible_positions_hl(self, row, col):
        return self.traverse_direction(row, col, 0, -1)  # Movimiento hacia la izquierda
    
    def possible_positions_hr(self, row, col):
        return self.traverse_direction(row, col, 0, 1)  # Movimiento hacia la derecha
