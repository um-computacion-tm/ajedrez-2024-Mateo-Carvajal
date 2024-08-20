from .pieces import Piece

class Pawn(Piece):
    def __str__(self):
        return 'P' if self.color == "White" else 'p'
    
    def movement(self, from_row, from_col, to_row, to_col):
        mov_x = to_row - from_row
        mov_y = to_col - from_col
        
        # Verificar si el peón es blanco o negro
        if self.color == "Black":
            if mov_x not in [1, 2] or mov_y != 0 or from_row != 1 and mov_x == 2:
                print("Movimiento inválido para el peón negro")
                return None
        else:  # Peón blanco
            if mov_x not in [-1, -2] or mov_y != 0 or from_row != 6 and mov_x == -2:
                print("Movimiento inválido para el peón blanco")
                return None
        
        # Movimiento válido, calcular la nueva posición
        coords = (to_row, to_col)
        return coords
