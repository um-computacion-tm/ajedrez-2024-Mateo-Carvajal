import unittest
from board import Board


class TestBoard(unittest.TestCase):
    def test_str_board(self):
        board = Board()
        self.assertEqual(
            str(board),
            (
                "1- ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ "
                "2- ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ "
                "3- . . . . . . . . "
                "4- . . . . . . . . "
                "5- . . . . . . . . "
                "6- . . . . . . . . "
                "7- ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ "
                "8- ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ "
                "   a|b|c|d|e|f|g|h"
            )
        )

if __name__ == '__main__':
    unittest.main()