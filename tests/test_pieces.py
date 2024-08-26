import unittest

from chess.pieces import Piece

class TestPieces(unittest.TestCase):
    def test_initialization(self):
        piece = Piece("White", True)
        self.assertEqual(piece.__color__, "White")
        self.assertTrue(piece.is_alive())

    def test_is_alive(self):
        piece = Piece("black", True)
        self.assertTrue(piece.is_alive())
        piece.alive = False  
        self.assertFalse(piece.is_alive())

if __name__ == '__main__':
    unittest.main()