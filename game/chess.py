from game.board import Board
from .exceptions import InvalidMove
from game.pieces import Pawn
from game.pieces import Rook
from game.pieces import Knight
from game.pieces import Bishop
from game.pieces import Queen
from game.pieces import King

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"

    def is_playing(self):
        return True

    def move_piece(self, from_row, from_col, to_row, to_col):
        if not (0 <= from_row < 8 and 0 <= from_col < 8 and 0 <= to_row < 8 and 0 <= to_col < 8):
            raise ValueError("Posicion no válida.")
        
        piece = self.__board__.get_piece(from_row, from_col)
        if piece is None:
            raise ValueError("No hay ninguna pieza en esa posición.")

        piece_color = self.__board__.get_piece_color(from_row, from_col)
        if piece_color != self.__turn__:
            raise InvalidMove("No es tu turno.")
        
        if (to_row, to_col) not in piece.valid_positions(from_row, from_col):
            raise InvalidMove("Movimiento invalido.")

        # Move the piece only if all checks pass
        self.__board__.set_piece(to_row, to_col, piece)
        self.__board__.set_piece(from_row, from_col, None)
        self.change_turn()
        
    def get_turn(self):
        return self.__turn__

    def show_board(self):
        self.__board__.display_board()

    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"
    
    def end_game(self):
        print("Juego terminado. ¡Gracias por jugar!")
