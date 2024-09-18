import unittest
from game.pieces.bishop import Bishop
from game.board import Board
from game.pieces.pawn import Pawn

class TestRook(unittest.TestCase):

    def test_str(self):
        board = Board()
        bishop = Bishop("WHITE", board)
        self.assertEqual(
            str(bishop),
            "♝",
        )

    def test_move_top_right(self):
        board = Board()
        bishop = Bishop("WHITE", board)
        possibles = bishop.possible_positions_top_right(3, 2)
        self.assertEqual(
            possibles,
            [(2, 3), (1, 4)]
        )

    def test_move_top_right_with_not_own_piece(self):
        board = Board()
        board.set_piece(2, 3, Pawn("BLACK", board))
        bishop = Bishop("WHITE", board)
        possibles = bishop.possible_positions_top_right(3, 2)
        self.assertEqual(
            possibles,
            [(2, 3)]
        )

    def test_move_top_right_with_own_piece(self):
        board = Board()
        board.set_piece(2, 3, Pawn("WHITE", board))
        bishop = Bishop("WHITE", board)
        possibles = bishop.possible_positions_top_right(3, 2)
        self.assertEqual(
            possibles,
            []
        )

    def test_move_top_left(self):
        board = Board()
        bishop = Bishop("WHITE", board)
        possibles = bishop.possible_positions_top_left(3, 2)
        self.assertEqual(
            possibles,
            [(2, 1), (1, 0)]
        )

    def test_move_top_left_with_not_own_piece(self):
        board = Board()
        board.set_piece(2, 1, Pawn("BLACK", board))
        bishop = Bishop("WHITE", board)
        possibles = bishop.possible_positions_top_left(3, 2)
        self.assertEqual(
            possibles,
            [(2, 1)]
        )
    
    def test_move_top_left_with_own_piece(self):
        board = Board()
        board.set_piece(2, 1, Pawn("WHITE", board))
        bishop = Bishop("WHITE", board)
        possibles = bishop.possible_positions_top_left(3, 2)
        self.assertEqual(
            possibles,
            []
        )

    def test_move_bottom_right(self):
        board = Board()
        bishop = Bishop("WHITE", board)
        possibles = bishop.possible_positions_bottom_right(2, 3)
        self.assertEqual(
            possibles,
            [(3, 4), (4, 5), (5, 6)]
        )

    def test_move_bottom_right_with_not_own_piece(self):
        board = Board()
        board.set_piece(5, 6, Pawn("BLACK", board))
        bishop = Bishop("WHITE", board)
        possibles = bishop.possible_positions_bottom_right(2, 3)
        self.assertEqual(
            possibles,
            [(3, 4), (4, 5), (5, 6)]
        )

    def test_move_bottom_right_with_own_piece(self):
        board = Board()
        board.set_piece(3, 4, Pawn("WHITE", board))
        bishop = Bishop("WHITE", board)
        possibles = bishop.possible_positions_bottom_right(2, 3)
        self.assertEqual(
            possibles,
            []
        )

    def test_move_bottom_left(self):
        board = Board()
        bishop = Bishop("WHITE", board)
        possibles = bishop.possible_positions_bottom_left(2, 3)
        self.assertEqual(
            possibles,
            [(3, 2), (4, 1), (5, 0)]
        )

    def test_move_bottom_left_with_not_own_piece(self):
        board = Board()
        board.set_piece(3, 2, Pawn("BLACK", board))
        bishop = Bishop("WHITE", board)
        possibles = bishop.possible_positions_bottom_left(2, 3)
        self.assertEqual(
            possibles,
            [(3, 2)]
        )

    def test_move_bottom_left_with_own_piece(self):
        board = Board()
        board.set_piece(3, 2, Pawn("WHITE", board))
        bishop = Bishop("WHITE", board)
        possibles = bishop.possible_positions_bottom_left(2, 3)
        self.assertEqual(
            possibles,
            []
        )

if __name__ == "__main__":
    unittest.main()