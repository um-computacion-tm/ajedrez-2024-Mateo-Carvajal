from .pieces import Piece

class Knight(Piece):
    def __str__(self):
        return 'N' if self.color == "White" else 'n'
    