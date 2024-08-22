from .pieces import Piece

class Knight(Piece):
    def __str__(self):
        return '♞' if self.__color__ == "White" else '♘'
