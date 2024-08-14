from pieces.pieces import Rook

class Board():
    def __init__(self):
        self.__positions__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)
        self.__positions__[0][0] = Rook("Black")
        self.__positions__[0][7] = Rook("Black")
        self.__positions__[7][0] = Rook("White")
        self.__positions__[7][7] = Rook("White")

    def get_piece(self, row, col):
        return self.__positions__ [row][col]