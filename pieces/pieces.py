class Piece:
    def __init__(self, color, alive):
        self.color = color
        self.alive = True

    def is_alive(self):
        return self.alive