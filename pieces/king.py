from .pieces import Piece

class King(Piece):
    def __init__(self, __color__, is_alive):
        super().__init__(__color__, is_alive)

    def __str__(self):
        return '♚' if self.__color__ == "White" else '♔'
    
    def is_alive(self):
        return self.alive

