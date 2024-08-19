from .pieces import Piece

class Pawn(Piece):
    def __str__(self):
        return 'P' if self.color == "White" else 'p'
    