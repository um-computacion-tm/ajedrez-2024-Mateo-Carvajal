import unittest
from game.pieces.queen import Queen
from game.board import Board
from game.pieces.pawn import Pawn

class TestQueen(unittest.TestCase):
    def test_str(self):
        board = Board()
        queen = Queen("WHITE", board)
        self.assertEqual(
            str(queen),
            "♛",
        )
    
    def test_move_no_pieces(self):
        board = Board()
        queen = Queen("WHITE", board)
        possibles = queen.valid_positions(2, 3)
        self.assertEqual(
            possibles,
            [
            (3, 3), (4, 3), (5, 3), (1, 3), (2, 2),
            (2, 1), (2, 0), (2, 4), (2, 5), (2, 6), 
            (2, 7), (1, 4), (1, 2), (3, 4), (4, 5), 
            (5, 6), (3, 2), (4, 1), (5, 0)
            ]
        )

    def test_move_with_own_pieces(self):
        board = Board()
        queen = Queen("WHITE", board)
        pawn = Pawn("WHITE", board)
        board.set_piece(2, 2, pawn)
        board.set_piece(4, 3, pawn)
        possibles = queen.valid_positions(3, 3)
        self.assertEqual(
            possibles,
            [
            (2, 3), (1, 3), (3, 2), (3, 1), (3, 0),
            (3, 4), (3, 5), (3, 6), (3, 7), (2, 4),
            (1, 5), (4, 4), (5, 5), (4, 2), (5, 1)
            ]
        )

    def test_move_with_not_own_pieces(self):
        board = Board()
        queen = Queen("WHITE", board)
        pawn = Pawn("BLACK", board)
        board.set_piece(2, 2, pawn)
        board.set_piece(4, 3, pawn)
        possibles = queen.valid_positions(3, 3)
        self.assertEqual(
            possibles,
            [
            (4, 3), (2, 3), (1, 3), (3, 2), (3, 1),
            (3, 0), (3, 4), (3, 5), (3, 6), (3, 7),
            (2, 4), (1, 5), (2, 2), (4, 4), (5, 5), 
            (4, 2), (5, 1)
            ]
        )

if __name__ == "__main__":
    unittest.main()