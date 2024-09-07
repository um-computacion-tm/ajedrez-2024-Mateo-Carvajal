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
            self.__positions__[0][0] = Rook("BLACK", self) # Black
            self.__positions__[0][7] = Rook("BLACK", self) # Black
            self.__positions__[7][7] = Rook("WHITE", self) # White
            self.__positions__[7][0] = Rook("WHITE", self) # White

    def show_piece(self):
        try:
            row = int(input("Por favor, ingrese la fila de la pieza: "))
            if row < 0 or row > 7:
                print("La fila ingresada no es válida.")
        except ValueError:
            print("La fila ingresada no es válida.")
            return
        try:
            col = int(input("Por favor, ingrese la columna de la pieza: "))
            if col < 0 or col > 7:
                print("La columna ingresada no es válida.")
        except ValueError:
            print("La columna ingresada no es válida.")
            return
        
        consulta = self.__positions__ [row][col]
        if consulta is not None:
            print("Su pieza es: " + str(consulta))
        else:
            print("No hay ninguna pieza en esa posición.")

    def get_piece(self, row, col):
        return self.__positions__[row][col]
        
    def set_piece(self, row, col, piece):
        self.__positions__[row][col] = piece

    def display_board(self):
        for i, row in enumerate(self.__positions__):
            row_display = f"{i + 1}- "
            for piece in row:
                if piece is None:
                    row_display += ". "
                else:
                    row_display += str(piece) + " "
            print(row_display)
        print("   a|b|c|d|e|f|g|h")

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


# board_instance = Board()
# board_instance.display_board()
# board_instance.get_piece(0,0)