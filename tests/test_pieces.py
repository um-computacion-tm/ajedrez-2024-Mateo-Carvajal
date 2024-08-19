import sys
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from pieces import Piece

class TestPieces(unittest.TestCase):
    def test_initialization(self):
        piece = Piece("White", True)
        self.assertEqual(piece.color, "White")
        self.assertTrue(piece.is_alive())

    def test_is_alive(self):
        piece = Piece("black", True)
        self.assertTrue(piece.is_alive())
        piece.alive = False  
        self.assertFalse(piece.is_alive())

if __name__ == '__main__':
    unittest.main()