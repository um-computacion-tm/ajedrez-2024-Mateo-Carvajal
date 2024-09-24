import unittest
from game.exceptions import ChessException, OutOfBounds, WrongTurn, InvalidPieceMovement, NoPiecesSelected

class TestExceptions(unittest.TestCase):
    def test_chess_exception(self):
        with self.assertRaises(ChessException) as context:
            raise ChessException("Chess exception occurred")
        self.assertEqual(str(context.exception), "Chess exception occurred")

    def test_out_of_bounds(self):
        with self.assertRaises(OutOfBounds) as context:
            raise OutOfBounds("Coordinates out of bounds")
        self.assertEqual(str(context.exception), "Coordinates out of bounds")

    def test_wrong_turn(self):
        with self.assertRaises(WrongTurn) as context:
            raise WrongTurn("It's not your turn")
        self.assertEqual(str(context.exception), "It's not your turn")

    def test_invalid_piece_movement(self):
        with self.assertRaises(InvalidPieceMovement) as context:
            raise InvalidPieceMovement("Invalid piece movement")
        self.assertEqual(str(context.exception), "Invalid piece movement")

    def test_no_pieces_selected(self):
        with self.assertRaises(NoPiecesSelected) as context:
            raise NoPiecesSelected("No piece selected")
        self.assertEqual(str(context.exception), "No piece selected")

if __name__ == "__main__":
    unittest.main()