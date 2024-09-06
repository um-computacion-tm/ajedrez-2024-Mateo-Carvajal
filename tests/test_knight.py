import unittest
from chess.pieces.knight import Knight
from chess.board import Board
from chess.pieces.pawn import Pawn

class TestRook(unittest.TestCase):

    def test_str(self):
        board = Board()
        knight = Knight("WHITE", board)
        self.assertEqual(
            str(knight),
            "♞",
        )
    
    def test_move(self):
        board = Board()
        knight = Knight("WHITE", board)
        possibles = knight.possible_positions(2, 3)
        self.assertEqual(
            possibles,
            [(4, 4), (4, 2), (0, 4), (0, 2), (3, 5), (3, 1), (1, 5), (1, 1)]
        )
    
    def test_move_with_pieces(self):
        board = Board()
        knight = Knight("WHITE", board)
        pawn = Pawn("WHITE", board)
        board.set_piece(3, 5, pawn)
        possibles = knight.possible_positions(2, 3)
        self.assertEqual(
            possibles,
            [(4, 4), (4, 2), (0, 4), (0, 2),(3, 1), (1, 5), (1, 1)]
        )

if __name__ == "__main__":
    unittest.main()