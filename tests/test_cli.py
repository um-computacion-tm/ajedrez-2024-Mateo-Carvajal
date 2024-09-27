import unittest
from unittest.mock import patch
from game.cli import Chess, ingame_menu, menu

class TestCli(unittest.TestCase):
    @patch('builtins.input', side_effect=['4'])  # Simulate user input '4' to exit
    @patch('builtins.print')
    def test_ingame_menu_exit(self, mock_print, mock_input):
        chess = Chess()
        ingame_menu(chess)
        mock_print.assert_any_call("Gracias por jugar")
        mock_print.assert_any_call("Juego terminado. ¡Gracias por jugar!")

    @patch('builtins.input', side_effect=['3'])  # Simulate user input '3' to exit main menu
    @patch('builtins.print')
    def test_main_menu_exit(self, mock_print, mock_input):
        chess = Chess()
        menu(chess)
        mock_print.assert_any_call("Gracias por jugar")
        mock_print.assert_any_call("Juego terminado. ¡Gracias por jugar!")


if __name__ == "__main__":
    unittest.main()