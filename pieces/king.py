from .pieces import Piece

class King(Piece):
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return 'K' if self.color == "White" else 'k'