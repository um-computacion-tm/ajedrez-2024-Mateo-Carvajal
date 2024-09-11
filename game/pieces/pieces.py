class Piece:
    def __init__(self, color, board):
        self.color = color
        self.board = board

    def __str__(self):
        if self.color == "WHITE":
            return self.white_str
        else:
            return self.black_str
        
    def is_alive(self):
        return self.alive
