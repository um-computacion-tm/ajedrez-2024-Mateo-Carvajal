import unittest
from chess.pieces.king import King
from chess.board import Board
from chess.pieces.pawn import Pawn

class TestRook(unittest.TestCase):

    def test_str(self):
        board = Board()
        king = King("WHITE", board)
        self.assertEqual(
            str(king),
            "♚",
        )

    def test_move_vertical(self):
        board = Board()
        king = King("WHITE", board)
        possibles = king.possible_positions_vertical(2, 3)
        self.assertEqual(
            possibles,
            [(3, 3), (1, 3)]
        )

    def test_move_horizontal(self):
        board = Board()
        king = King("WHITE", board)
        possibles = king.possible_positions_horizontal(2, 3)
        self.assertEqual(
            possibles,
            [(2, 4), (2, 2)]
        )

    def test_move_diagonal(self):
        board = Board()
        king = King("WHITE", board)
        possibles = king.possible_positions_diagonal(2, 3)
        self.assertEqual(
            possibles,
            [(3, 4), (3, 2), (1, 4), (1, 2)]
        )


if __name__ == "__main__":
    unittest.main()