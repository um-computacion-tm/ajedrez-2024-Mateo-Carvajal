from pieces import Rook
from pieces import Knight
from pieces import Bishop
from pieces import Queen
from pieces import King
from pieces import Pawn


class Board():
    def __init__(self):
        self.board = board_instance.display_board()
        self.__positions__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)

        #colocando piezas lado negro
        self.__positions__[0][0] = Rook("Black")
        self.__positions__[0][1] = Knight("Black")
        self.__positions__[0][2] = Bishop("Black")
        self.__positions__[0][3] = Queen("Black")
        self.__positions__[0][4] = King("Black")
        self.__positions__[0][5] = Bishop("Black")
        self.__positions__[0][6] = Knight("Black")
        self.__positions__[0][7] = Rook("Black")
    
        #colocando piezas lado blanco
        self.__positions__[7][0] = Rook("White")
        self.__positions__[7][1] = Knight("White")
        self.__positions__[7][2] = Bishop("White")
        self.__positions__[7][3] = Queen("White")
        self.__positions__[7][4] = King("White")
        self.__positions__[7][5] = Bishop("White")
        self.__positions__[7][6] = Knight("White")
        self.__positions__[7][7] = Rook("White")

        #colocando peones para ambos lados
        for i in range(8):
            self.__positions__[1][i] = Pawn("Black")
            self.__positions__[6][i] = Pawn("White")

    def get_piece(self, row, col):
        return self.__positions__ [row][col]
    
    def display_board(self):
        for row in self.__positions__:
            row_display = ""
            for piece in row:
                if piece is None:
                    row_display += ". "
                else:
                    row_display += str(piece) + " "
            print(row_display)

board_instance = Board()
board_instance.display_board()