from game.pieces import Rook, Knight, Bishop, Queen, King, Pawn

class Board:
    def __init__(self, for_test = False):
        self.__positions__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)
        if not for_test:
            self.__positions__[0][0] = Rook("BLACK", self) 
            self.__positions__[0][1] = Knight("BLACK", self)
            self.__positions__[0][2] = Bishop("BLACK", self)
            self.__positions__[0][3] = Queen("BLACK", self)
            self.__positions__[0][4] = King("BLACK", self)
            self.__positions__[0][5] = Bishop("BLACK", self)
            self.__positions__[0][6] = Knight("BLACK", self)
            self.__positions__[0][7] = Rook("BLACK", self) 
            
            self.__positions__[7][7] = Rook("WHITE", self)
            self.__positions__[7][6] = Knight("WHITE", self)
            self.__positions__[7][5] = Bishop("WHITE", self)
            self.__positions__[7][4] = Queen("WHITE", self)
            self.__positions__[7][3] = King("WHITE", self)
            self.__positions__[7][2] = Bishop("WHITE", self)
            self.__positions__[7][1] = Knight("WHITE", self)
            self.__positions__[7][0] = Rook("WHITE", self) 

            self.initialize_pawns()


    def initialize_pawns(self):
        for col in range(8):
            self.__positions__[1][col] = Pawn("BLACK", self)  # Black pawns
            self.__positions__[6][col] = Pawn("WHITE", self)  # White pawns

    #Toma posiciones y devuelve la pieza en la posición dada
    def get_piece(self, row, col):
        return self.__positions__[row][col]
    
    #Toma posiciones y devuelve el color de la pieza en la posición dada
    def get_piece_color(self, row, col):
        piece = self.get_piece(row, col)
        if piece is not None:
            return piece.get_color()
        return None
        
    #Coloca una pieza en la posición dada
    def set_piece(self, row, col, piece):
        self.__positions__[row][col] = piece

    #Muestra el tablero de juego
    def display_board(self):
        for i, row in enumerate(self.__positions__):
            row_display = f"{i}- "
            for piece in row:
                if piece is None:
                    row_display += ". "
                else:
                    row_display += str(piece) + " "
            print(row_display)
        print("   0|1|2|3|4|5|6|7")

    def __str__(self):
        board_str = ""
        for row in self.__positions__:
            for cell in row:
                if cell is not None:
                    board_str += str(cell)
                else:
                    board_str += " "
            board_str += "\n"
        return board_str
    
    #Comprueba si hay piezas de un color dado
    def has_pieces(self, color):
        for row in self.__positions__:
            for piece in row:
                if piece and piece.get_color() == color:
                    return True
        return False
    