from .pieces import Piece

class Queen(Piece):
    def __init__(self, color, is_alive):
        super().__init__(color, is_alive)

    def __str__(self):
        return 'Q' if self.color == "White" else 'q'