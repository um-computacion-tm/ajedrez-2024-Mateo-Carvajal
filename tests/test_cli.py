import unittest
from unittest.mock import patch
from game.cli import ingame_menu
from game.chess import Chess

class TestCli(unittest.TestCase):
    @patch('builtins.input', side_effect=['3'])  # Simulate user input '3' to exit
    def test_ingame_menu_exit(self, mock_input):
        chess = Chess()
        with patch('builtins.print') as mock_print:  # Mock print to suppress output
            ingame_menu(chess)
            mock_print.assert_any_call("Gracias por jugar")

if __name__ == "__main__":
    unittest.main()