from .pieces import Piece

class Queen(Piece):
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return 'Q' if self.color == "White" else 'q'