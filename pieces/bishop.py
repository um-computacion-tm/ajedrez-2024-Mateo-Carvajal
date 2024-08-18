from .pieces import Piece

class Bishop(Piece):
    def __init__(self, color, is_alive):
        super().__init__(color, is_alive)

    def __str__(self):
        return 'B' if self.color == "White" else 'b'
    