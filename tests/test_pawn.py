import unittest
from game.board import Board
from game.pieces.pawn import Pawn

class TestPawn(unittest.TestCase):

    def test_str(self):
        board = Board()
        pawn = Pawn("WHITE", board)
        self.assertEqual(
            str(pawn),
            "♟",
        )

    def test_first_move_black(self):
        board = Board()
        pawn = Pawn("BLACK", board)
        possibles = pawn.possible_positions_black(1, 1)
        self.assertEqual(
            possibles, [(2, 1), (3, 1)]
        )

    def test_first_move_white(self):
        board = Board()
        pawn = Pawn("WHITE", board)
        possibles = pawn.possible_positions_white(6, 1)
        self.assertEqual(
            possibles, [(5, 1), (4, 1)]
        )

    def test_move_black(self):
        board = Board()
        pawn = Pawn("BLACK", board)
        possibles = pawn.possible_positions_black(3, 1)
        self.assertEqual(
            possibles, [(4, 1)]
        )
    
    def test_move_white(self):
        board = Board()
        pawn = Pawn("WHITE", board)
        possibles = pawn.possible_positions_white(3, 1)
        self.assertEqual(
            possibles, [(2, 1)]
        )

    def test_first_move_black_with_piece(self):
        board = Board()
        board.set_piece(3, 1, Pawn("WHITE", board))
        pawn = Pawn("BLACK", board)
        possibles = pawn.possible_positions_black(1, 1)
        self.assertEqual(
            possibles, [(2, 1)]
        )
    
    def test_first_move_white_with_piece(self):
        board = Board()
        board.set_piece(4, 1, Pawn("BLACK", board))
        pawn = Pawn("WHITE", board)
        possibles = pawn.possible_positions_white(6, 1)
        self.assertEqual(
            possibles, [(5, 1)]
        )
        
    def test_move_black_with_piece(self):
        board = Board()
        board.set_piece(4, 1, Pawn("WHITE", board))
        pawn = Pawn("BLACK", board)
        possibles = pawn.possible_positions_black(3, 1)
        self.assertEqual(
            possibles, []
        )

    def test_move_white_with_piece(self):
        board = Board()
        board.set_piece(2, 1, Pawn("BLACK", board))
        pawn = Pawn("WHITE", board)
        possibles = pawn.possible_positions_white(3, 1)
        self.assertEqual(
            possibles, []
        )

    def test_valid_positions_white(self):
        board = Board()
        pawn = Pawn("WHITE", board)
        possibles = pawn.valid_positions(6, 1)
        self.assertEqual(
            possibles, [(5, 1), (4, 1)]
        )
    
    def test_valid_positions_black(self):
        board = Board()
        pawn = Pawn("BLACK", board)
        possibles = pawn.valid_positions(1, 1)
        self.assertEqual(
            possibles, [(2, 1), (3, 1)]
        )

if __name__ == '__main__':
    unittest.main()