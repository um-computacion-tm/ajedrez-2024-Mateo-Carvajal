from pieces.rook import Rook
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.queen import Queen
from pieces.king import King
from pieces.pawn import Pawn
from board import Board, board_instance
from cli import play


class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "blanco"
    
    #Cambia de turno entre jugadores
    def change_turn(self):
        if self.__turn__ == "blanco":
            self.__turn__ = "negro"
        else:
            self.__turn__ = "blanco"
        print("el turno es de: " +  self.__turn__)
       
    #Mantiene el juego activo mientras ambos reyes esten vivos
    def turns(self):
        while King("white", True) and King("black", True):
            print(f"Turno del jugador {self.__turn__}")
            self.move()
            self.change_turn()
            if King("white", True) and King("black", False):
                print("¡Blancas ganan!")
            elif not King("white", False) and King("black", True):
                print("Negras ganan")
            
Ajedres = Chess()
Ajedres.move()
Ajedres.change_turn()
#Ajedres.turns()
board_instance.get_piece()
