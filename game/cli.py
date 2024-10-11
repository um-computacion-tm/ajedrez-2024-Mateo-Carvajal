from game.chess import Chess
from game.exceptions import ChessException, OutOfBounds, WrongTurn, InvalidPieceMovement, NoPiecesSelected

def main():
    chess = Chess()
    menu(chess)


def menu(chess):
    while not chess.__game_over__:
        print()
        print("--Main Menu--")
        print("1. Play")
        print("2. Load game")
        print("3. Quit")
        print()
        option = input("Choose an option: ")
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
            print("Invalid option")


def ingame_menu(chess):
    while not chess.__game_over__:
        # Check if the game is over
        chess.check_game_over()
        if chess.__game_over__:
            chess.end_game()
            break

        print("------------------------------------------------------------------------")
        print()
        print("--Game Menu--")
        print("Turn: ", chess.get_turn())
        print()
        print("1. Show board")
        print("2. Move piece")
        print("3. Surrender")
        print("4. Quit")
        print("5. Restart")
        print("6. Save game")
        print()
        option = input("Choose an option: ")


        if option == "1":
            chess.show_board()
        elif option == "2":
            play(chess)
        elif option == "3":
            print()
            print("You surrendered!")
            chess.end_game()
            break
        elif option == "4":
            print()
            chess.end_game()
            break
        elif option == "5":
            print()
            print("------------------------------------------------------------------------")
            print("Restarting game...")
            chess = Chess()
        elif option == "6":
            chess.save_game()
        else:
            print("Invalid option")

def play(chess):
    try:
        print()
        chess.show_board()  
        print("Turn: ", chess.get_turn()) 
        from_row = int(input("From row: "))
        from_col = int(input("From col: "))
        to_row = int(input("To Row: "))
        to_col = int(input("To Col: "))

        print(f"Attempting to move from ({from_row}, {from_col}) to ({to_row}, {to_col})")
        chess.move_piece(from_row, from_col, to_row, to_col)
        chess.show_board()  

    except InvalidPieceMovement as e:
        print(f"Invalid move: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()