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
    
    #Usado para comprobar si la posición dada está dentro del tablero
    def is_in_board(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8

    #Usado para mover una pieza de una posición a otra
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

        # Mueve la pieza solo si se pasan todas las comprobaciones
        self.__board__.set_piece(to_row, to_col, piece)
        self.__board__.set_piece(from_row, from_col, None)
        self.change_turn()

    #Devuelve el turno actual 
    def get_turn(self):
        return self.__turn__

    #Muestra el tablero de juego
    def show_board(self):
        print()
        print("Game board:")
        self.__board__.display_board()

    #Usado para cambiar el turno
    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"

    #Usado para comprobar si el juego ha terminado
    def check_game_over(self):
        if not self.__board__.has_pieces('WHITE') or not self.__board__.has_pieces('BLACK'):
            self.__game_over__ = True
            return True
    
    #Usado para terminar el juego
    def end_game(self):
        self.__game_over__ = True
        print(self.winner(), "wins!")
        print("Game over. Thanks for playing!")
        print()

    #Devuelve el ganador del juego si game_over es True, de lo contrario devuelve None
    def winner(self):
        if self.__game_over__:
            if self.__turn__ == "WHITE":
                return "BLACK"
            else:
                return "WHITE"
        return None
    
    #Usado para guardar el juego
    def save_game(self, filename="saved_game.pkl"):
        with open(filename, "wb") as f:
            pickle.dump(self, f)
        print()
        print("The game has been saved")
        print("------------------------------------------------------------------------")
        print()

    @staticmethod
    def load_game(filename="saved_game.pkl"):
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            print(f"{filename} not found. Creating a new game instead.")
            return Chess()
