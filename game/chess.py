from game.board import Board
from game.exceptions import ChessException, OutOfBounds, WrongTurn, InvalidPieceMovement, NoPiecesSelected
from game.pieces import Pawn
from game.pieces import Rook
from game.pieces import Knight
from game.pieces import Bishop
from game.pieces import Queen
from game.pieces import King
import pickle

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"
        self.__game_over__ = False

    def is_playing(self):
        return True
    
    def is_in_board(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8

    def move_piece(self, from_row, from_col, to_row, to_col):
        if not (self.is_in_board(from_row, from_col) and self.is_in_board(to_row, to_col)):
            raise OutOfBounds()
        
        piece = self.__board__.get_piece(from_row, from_col)
        if piece is None:
            raise NoPiecesSelected()

        piece_color = self.__board__.get_piece_color(from_row, from_col)
        if piece_color != self.__turn__:
            raise WrongTurn()
        
        if (to_row, to_col) not in piece.valid_positions(from_row, from_col):
            raise InvalidPieceMovement()

        # Move the piece only if all checks pass
        self.__board__.set_piece(to_row, to_col, piece)
        self.__board__.set_piece(from_row, from_col, None)
        self.change_turn()
        
    def get_turn(self):
        return self.__turn__

    def show_board(self):
        print()
        print("Game board:")
        self.__board__.display_board()

    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"

    def check_game_over(self):
        if not self.__board__.has_pieces('WHITE') or not self.__board__.has_pieces('BLACK'):
            self.__game_over__ = True
            return True
    
    def end_game(self):
        self.__game_over__ = True
        print(self.winner(), "wins!")
        print("Game over. Thanks for playing!")
        print()

    def winner(self):
        if self.__game_over__:
            if self.__turn__ == "WHITE":
                return "BLACK"
            else:
                return "WHITE"
        return None
    
    def save_game(self, filename="saved_game.pkl"):
        with open(filename, "wb") as f:
            pickle.dump(self, f)
        print()
        print("The game has been saved")
        print("------------------------------------------------------------------------")
        print()

    @staticmethod
    def load_game(filename="saved_game.pkl"):
        with open(filename, "rb") as f:
            return pickle.load(f)
