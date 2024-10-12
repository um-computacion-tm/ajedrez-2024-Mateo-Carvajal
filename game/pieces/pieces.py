class Piece:
    def __init__(self, color, board):
        self.__color__ = color
        self.__board__ = board

        #Devuelve el color de la pieza
    def get_color(self):
        return self.__color__
    
    def __str__(self):
        if self.__color__ == "WHITE":
            return self.white_str
        else:
            return self.black_str