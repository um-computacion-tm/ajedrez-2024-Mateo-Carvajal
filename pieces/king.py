from .pieces import Piece

class King(Piece):
    def __init__(self, color, is_alive):
        super().__init__(color, is_alive)

    def __str__(self):
        return 'K' if self.color == "White" else 'k'
    
    def is_alive(self):
        return self.alive
