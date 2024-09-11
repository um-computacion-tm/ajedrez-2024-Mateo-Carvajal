from game.chess import Chess
from exceptions import InvalidMove

def main():
    chess = Chess()
    while chess.is_playing():
        ingame_menu(chess)

def ingame_menu(chess):
    print("1. Ver tablero")
    print("2. Mover pieza")
    print("3. Salir")
    option = input("Ingrese una opción: ")
    if option == "1":
        chess.show_board()  # Call without print
        ingame_menu(chess)  # Call ingame_menu with chess instance
    elif option == "2":
        play(chess)
    elif option == "3":
        print("Gracias por jugar")
        chess.end_game()
    else:
        print("Opción no válida")
        ingame_menu(chess)  # Call ingame_menu with chess instance

def play(chess):
    try:
        chess.show_board()  # Display the board
        print("Turn: ", chess.get_turn())  # Display the current turn
        from_row = int(input("From row: "))
        from_col = int(input("From col: "))
        to_row = int(input("To Row: "))
        to_col = int(input("To Col: "))

        print(f"Attempting to move from ({from_row}, {from_col}) to ({to_row}, {to_col})")
        chess.move_piece(from_row, from_col, to_row, to_col)
    except InvalidMove as e:
        print(f"Invalid move: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def menu():
    print("1. Jugar")
    print("2. Salir")
    option = input("Ingrese una opción: ")
    if option == "1":
        main()
    elif option == "2":
        print("Gracias por jugar")
    else:
        print("Opción no válida")
        menu()

if __name__ == "__main__":
    menu()