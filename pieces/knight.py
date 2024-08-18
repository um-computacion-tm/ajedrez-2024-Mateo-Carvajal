from .pieces import Piece

class Knight(Piece):
    def __init__(self, color, is_alive):
        super().__init__(color, is_alive)

    def __str__(self):
        return 'N' if self.color == "White" else 'n'
    