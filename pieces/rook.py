from .pieces import Piece

class Rook(Piece):
    def __init__(self, color, is_alive):
        super().__init__(color, is_alive)

    def __str__(self):
        return 'R' if self.color == "White" else 'r'
    