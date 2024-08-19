from chess import Chess
from board import Board
from board import Board, board_instance

def main():
    turn = 1
    chess = Chess(Board())
    while True:
        play(chess)

#Mueve las piezas en el tablero en base a las coordenadas ingresadas por el usuario
def play(chess):
    board_instance.display_board()
    print("Ingrese fila y columna de la pieza a mover")
    fila_1 = int(input("Fila: "))
    columna_1 = int(input("Columna: "))
    print("Ingrese fila y columna a donde mover la pieza")
    fila_2 = int(input("Fila: "))
    columna_2= int(input("Columna: "))

if __name__ == "__main__":
    main()
    