from .pieces import Piece

class Rook(Piece):
    def __str__(self):
        return 'R' if self.color == "White" else 'r'
    