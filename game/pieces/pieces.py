class Piece:
    def __init__(self, color, board):
        self.color = color
        self.__board__ = board

    def __str__(self):
        if self.color == "WHITE":
            return self.white_str
        else:
            return self.black_str
        
    #Devuelve el color de la pieza
    def get_color(self):
        return self.color
    