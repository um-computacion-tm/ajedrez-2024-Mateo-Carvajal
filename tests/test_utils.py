import unittest
from game.pieces.utils import gather_positions

class TestUtils(unittest.TestCase):
    def setUp(self):
        # Setup any necessary data or state before each test
        self.row = 3
        self.col = 3

    def mock_position_func_1(self, row, col):
        return [(row + 1, col), (row - 1, col)]

    def mock_position_func_2(self, row, col):
        return [(row, col + 1), (row, col - 1)]

    def test_gather_positions(self):
        result = gather_positions(self.row, self.col, self.mock_position_func_1, self.mock_position_func_2)
        expected = [(4, 3), (2, 3), (3, 4), (3, 2)]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()