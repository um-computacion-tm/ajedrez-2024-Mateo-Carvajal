from .pieces import Piece

class Pawn(Piece):
    def __init__(self, color, is_alive):
        super().__init__(color, is_alive)

    def __str__(self):
        return 'P' if self.color == "White" else 'p'
    