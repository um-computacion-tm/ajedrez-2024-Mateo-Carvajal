import unittest

from chess.board import Board
from chess.pieces.rook import Rook
from chess.pieces.knight import Knight
from chess.pieces.bishop import Bishop
from chess.pieces.queen import Queen
from chess.pieces.king import King
from chess.pieces.pawn import Pawn


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.__board__ = Board()

    def test_str_board(self):
        board = Board()
        self.assertEqual(str(board),
                         
            "♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ \n"
            "♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ \n"
            ". . . . . . . . \n"
            ". . . . . . . . \n"
            ". . . . . . . . \n"
            ". . . . . . . . \n"
            "♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ \n"
            "♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ \n"
        )

    def test_get_piece(self):
        # Verificar que get_piece devuelve la pieza correcta
        board = Board()
        self.assertEqual(board.get_piece(0, 0), "♖")
        self.assertEqual(board.get_piece(0, 1), "♘")
        self.assertEqual(board.get_piece(0, 2), "♗")

if __name__ == "__main__":
    unittest.main()
