from chess import Chess
from board import Board


def main():
    turn = 1
    chess = Chess(Board())
    while True:
        play(chess)

def play(chess):
    try:
        print("turn: ", chess.turn)
        from_row = int(input("From row: "))
        from_col = int(input("From col: "))
        to_row = int(input("To Row: "))
        to_col = int(input("To Col: "))
        # :)
        chess.move(from_row, from_col, to_row, to_col)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()