import unittest
from game.chess import Chess
from game.board import Board
from unittest.mock import patch
from io import StringIO
from game.exceptions import ChessException, OutOfBounds, WrongTurn, InvalidPieceMovement, NoPiecesSelected

class TestChess(unittest.TestCase):
    def test_is_playing(self):
        chess = Chess()
        self.assertTrue(chess.is_playing())

    def test_move_piece_out_of_bounds(self):
        chess = Chess()
        with self.assertRaises(OutOfBounds):
            chess.move_piece(8, 1, 3, 0)  # Out-of-bounds starting position
        with self.assertRaises(OutOfBounds):
            chess.move_piece(0, 0, 8, 0)  # Out-of-bounds destination position
        with self.assertRaises(OutOfBounds):
            chess.move_piece(-1, 0, 3, 0)  # Negative starting position
        with self.assertRaises(OutOfBounds):
            chess.move_piece(0, 0, 0, -1)  # Negative destination position

    def test_move_piece_no_piece(self):
        chess = Chess()
        with self.assertRaises(NoPiecesSelected):
            chess.move_piece(2, 0, 3, 0)  # Empty starting position
        with self.assertRaises(NoPiecesSelected):
            chess.move_piece(3, 1, 3, 0)  # Empty starting position

    def test_move_piece_wrong_turn(self):
        chess = Chess()
        with self.assertRaises(WrongTurn):
            chess.move_piece(1, 0, 2, 0)  #Black Pawn move
        with self.assertRaises(WrongTurn):
            chess.move_piece(0, 0, 5, 0)  #Black Rook move

    def test_move_piece_invalid_piece_movement(self):
        chess = Chess()
        with self.assertRaises(InvalidPieceMovement):
            chess.move_piece(6, 0, 3, 0)  # Invalid White Pawn move
        with self.assertRaises(InvalidPieceMovement):
            chess.move_piece(7, 0, 3, 0)  # Invalid White Rook move

    def test_get_turn(self):
        chess = Chess()
        self.assertEqual(chess.get_turn(), "WHITE")
        chess.change_turn()
        self.assertEqual(chess.get_turn(), "BLACK")
        chess.change_turn()

    def test_change_turn(self):
        chess = Chess()
        self.assertEqual(chess.get_turn(), "WHITE")
        chess.change_turn()
        self.assertEqual(chess.get_turn(), "BLACK")

    def test_end_game(self):
        chess = Chess()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            chess.end_game()
            self.assertEqual(fake_out.getvalue(), "BLACK wins!\nGame over. Thanks for playing!\n\n")

    def test_winner(self):
        chess = Chess()
        chess.__game_over__ = True
        self.assertEqual(chess.winner(), "BLACK")

    def test_save_game(self):
        chess = Chess()
        with patch('builtins.open', unittest.mock.mock_open()) as mock_open:
            chess.save_game()
            mock_open.assert_called_once_with("saved_game.pkl", "wb")
            mock_open().write.assert_called_once()
    
    def test_is_in_board(self):
        chess = Chess()
        self.assertTrue(chess.is_in_board(0, 0))
        self.assertTrue(chess.is_in_board(7, 7))
        self.assertFalse(chess.is_in_board(8, 0))
        self.assertFalse(chess.is_in_board(0, 8))
        self.assertFalse(chess.is_in_board(-1, 0))
        self.assertFalse(chess.is_in_board(0, -1))

if __name__ == "__main__":
    unittest.main()