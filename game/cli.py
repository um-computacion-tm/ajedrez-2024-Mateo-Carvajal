import sys
import os

# Agrega el directorio raíz del proyecto al sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from game.chess import Chess
from game.exceptions import ChessException, OutOfBounds, WrongTurn, InvalidPieceMovement, NoPiecesSelected

def main():
    chess = Chess()
    menu(chess)


def menu(chess):
    while not chess.__game_over__:
        print("Menú Principal")
        print("1. Jugar")
        print("2. Cargar juego")
        print("3. Salir")
        option = input("Ingrese una opción: ")
        if option == "1":
            print()
            ingame_menu(chess)
        elif option == "2":
            chess = Chess.load_game()
            ingame_menu(chess)
        elif option == "3":
            chess.end_game()
            break
        else:
            print("Opción no válida")


def ingame_menu(chess):
    while not chess.__game_over__:
        print("------------------------------------------------------------------------")
        print("Menú de juego")
        print("Turno: ", chess.get_turn())
        print()
        print("1. Ver tablero")
        print("2. Mover pieza")
        print("3. Rendirse")
        print("4. Salir")
        print("5. Reiniciar")
        print("6. Guardar")
        option = input("Ingrese una opción: ")
        if option == "1":
            chess.show_board()
        elif option == "2":
            play(chess)
        elif option == "3":
            # Placeholder for surrendering
            print("Te has rendido")
            chess.end_game()
            break
        elif option == "4":
            print()
            chess.end_game()
            break
        elif option == "5":
            print()
            print("------------------------------------------------------------------------")
            print("Reiniciando juego")
            chess = Chess()
        elif option == "6":
            chess.save_game()
        else:
            print("Opción no válida")

def play(chess):
    try:
        print()
        chess.show_board()  # Display the board
        print("Turn: ", chess.get_turn())  # Display the current turn
        from_row = int(input("From row: "))
        from_col = int(input("From col: "))
        to_row = int(input("To Row: "))
        to_col = int(input("To Col: "))

        print(f"Attempting to move from ({from_row}, {from_col}) to ({to_row}, {to_col})")
        chess.move_piece(from_row, from_col, to_row, to_col)
        chess.show_board()  # Display the board

    except InvalidPieceMovement as e:
        print(f"Invalid move: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()