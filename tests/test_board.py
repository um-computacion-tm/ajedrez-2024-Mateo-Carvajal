import unittest

from game.board import Board
from game.pieces.rook import Rook
from game.pieces.knight import Knight
from game.pieces.bishop import Bishop
from game.pieces.queen import Queen
from game.pieces.king import King
from game.pieces.pawn import Pawn


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.__board__ = Board()

    class TestBoard(unittest.TestCase):
        def test_str_board(self):
            board = Board()
            self.assertEqual(
                str(board),
                (
                    "♖      ♖\n"
                    "        \n"
                    "        \n"
                    "        \n"
                    "        \n"
                    "        \n"
                    "        \n"
                    "♜      ♜\n"
                )
            )

    def test_get_piece(self):
        # Verificar que get_piece devuelve la pieza correcta
        board = Board()
        self.assertEqual(str(board.get_piece(0, 0)), "♖")
        self.assertEqual(str(board.get_piece(7, 0)), "♜")

if __name__ == "__main__":
    unittest.main()
