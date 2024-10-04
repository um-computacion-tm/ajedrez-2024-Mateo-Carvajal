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

    def test_str_board(self):
        board = Board()
        self.assertEqual(
            str(board),
            (
                "♖♘♗♕♔♗♘♖\n"
                "♙♙♙♙♙♙♙♙\n"
                "        \n"
                "        \n"
                "        \n"
                "        \n"
                "♟♟♟♟♟♟♟♟\n"
                "♜♞♝♚♛♝♞♜\n"
            )
        )

    def test_get_piece(self):
        # Verificar que get_piece devuelve la pieza correcta
        board = Board()
        self.assertEqual(str(board.get_piece(0, 0)), "♖")
        self.assertEqual(str(board.get_piece(7, 0)), "♜")

    def test_get_piece_color(self):
        # Verificar que get_piece_color devuelve el color correcto
        board = Board()
        self.assertEqual(board.get_piece_color(0, 0), "BLACK")
        self.assertEqual(board.get_piece_color(7, 0), "WHITE")
        self.assertEqual(board.get_piece_color(3, 3), None)

    def test_set_piece(self):
        # Verificar que set_piece coloca la pieza en la posición correcta
        board = Board()
        rook = Rook("WHITE", board)
        board.set_piece(3, 3, rook)
        self.assertEqual(str(board.get_piece(3, 3)), "♜")

    def test_has_pieces(self):
        # Verificar que has_pieces devuelve True si hay piezas del color dado
        board = Board()
        self.assertTrue(board.has_pieces("WHITE"))
        self.assertTrue(board.has_pieces("BLACK"))

if __name__ == "__main__":
    unittest.main()