from .pieces import Piece

class Queen(Piece):
    def __str__(self):
        return 'Q' if self.color == "White" else 'q'
    