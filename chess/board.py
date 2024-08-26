from chess.pieces import Rook, Knight, Bishop, Queen, King, Pawn

class Board():
    def __init__(self):
        self.__positions__ = []
        for i in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)

        #colocando piezas lado negro
        self.__positions__[0][0] = Rook("Black", True)
        self.__positions__[0][1] = Knight("Black", True)
        self.__positions__[0][2] = Bishop("Black", True)
        self.__positions__[0][3] = Queen("Black", True)
        self.__positions__[0][4] = King("Black", True)
        self.__positions__[0][5] = Bishop("Black", True)
        self.__positions__[0][6] = Knight("Black", True)
        self.__positions__[0][7] = Rook("Black", True)
    
        #colocando piezas lado blanco
        self.__positions__[7][0] = Rook("White", True)
        self.__positions__[7][1] = Knight("White", True)
        self.__positions__[7][2] = Bishop("White", True)
        self.__positions__[7][3] = Queen("White", True)
        self.__positions__[7][4] = King("White", True)
        self.__positions__[7][5] = Bishop("White", True)
        self.__positions__[7][6] = Knight("White", True)
        self.__positions__[7][7] = Rook("White", True)

        #colocando peones para ambos lados
        for i in range(8):
            self.__positions__[1][i] = Pawn("Black", True)
            self.__positions__[6][i] = Pawn("White", True)

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
        consulta = self.__positions__ [row][col]
        if consulta is not None:
            print("Su pieza es: " + str(consulta))
            return str(consulta)
        else:
            print("No hay ninguna pieza en esa posición.")
            return None

        

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
                    board_str += str(cell) + " " # Agrega un espacio después de cada pieza
                else:
                    board_str += ". " # Agrega un punto si no hay pieza
            board_str += "\n"
        return board_str


# board_instance = Board()
# board_instance.display_board()
# board_instance.get_piece(0,0)
