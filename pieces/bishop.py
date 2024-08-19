from .pieces import Piece

class Bishop(Piece):
    def __str__(self):
        return 'B' if self.color == "White" else 'b'
    