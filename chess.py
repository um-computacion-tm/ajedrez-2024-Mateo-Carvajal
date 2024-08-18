from pieces.rook import Rook
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.queen import Queen
from pieces.king import King, K, k
from pieces.pawn import Pawn
from board import Board, board_instance


class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "blanco"

    #Mueve las piezas en el tablero en base a las coordenadas ingresadas por el usuario
    def move(self):
        board_instance.display_board()
        print("Ingrese fila y columna de la pieza a mover")
        fila_1 = int(input("Fila: "))
        columna_1 = int(input("Columna: "))
        print("Ingrese fila y columna a donde mover la pieza")
        fila_2 = int(input("Fila: "))
        columna_2= int(input("Columna: "))
    
    #Cambia de turno entre jugadores
    def change_turn(self):
        if self.__turn__ == "blanco":
            self.__turn__ = "negro"
        else:
            self.__turn__ = "blanco"
        print("el turno es de: " +  self.__turn__)
       
    #Mantiene el juego activo mientras ambos reyes esten vivos
def turns(self):
    while K.is_alive() and k.is_alive():
        print(f"Turno del jugador {self.__turn__}")
        self.move()
        self.change_turn()
        if K.is_alive() and not k.is_alive():
            print("¡Blancas ganan!")
        elif not K.is_alive() and k.is_alive():
            print("Negras ganan")
            
#Ajedres = Chess()
#Ajedres.move()
#Ajedres.change_turn()