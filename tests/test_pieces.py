import unittest
from game.pieces import Piece

class TestPiece(unittest.TestCase):
    def setUp(self):
        self.mock_board = None 
        self.piece_white = Piece("WHITE", self.mock_board)
        self.piece_black = Piece("BLACK", self.mock_board)
        
        self.piece_white.white_str = "♚"  
        self.piece_black.black_str = "♔"  

    def test_get_color(self):
        self.assertEqual(self.piece_white.get_color(), "WHITE")
        self.assertEqual(self.piece_black.get_color(), "BLACK")

    def test_str_method(self):
        self.assertEqual(str(self.piece_white), "♚")
        self.assertEqual(str(self.piece_black), "♔")
        
if __name__ == '__main__':
    unittest.main()