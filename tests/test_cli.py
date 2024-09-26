import unittest
from unittest.mock import patch
from game.cli import Chess, ingame_menu, menu

class TestCli(unittest.TestCase):
    @patch('builtins.input', side_effect=['4'])  # Simulate user input '4' to exit
    def test_ingame_menu_exit(self, mock_input):
        chess = Chess()
        with patch('builtins.print') as mock_print:  # Mock print to suppress output
            ingame_menu(chess)
            mock_print.assert_any_call("Gracias por jugar")
            mock_print.assert_any_call("Juego terminado. ¡Gracias por jugar!")

    @patch('builtins.input', side_effect=['2'])  # Simulate user input '2' to exit main menu
    def test_main_menu_exit(self, mock_input):
        chess = Chess()
        with patch('builtins.print') as mock_print:  # Mock print to suppress output
            menu(chess)
            mock_print.assert_any_call("Gracias por jugar")
            mock_print.assert_any_call("Juego terminado. ¡Gracias por jugar!")

if __name__ == "__main__":
    unittest.main()