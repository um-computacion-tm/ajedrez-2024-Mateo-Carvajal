from .pieces import Piece

class Rook(Piece):
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return 'R' if self.color == "White" else 'r'