import unittest
import io
from unittest.mock import patch
from game.cli import Chess, ingame_menu, menu, main

class TestCli(unittest.TestCase):
    @patch('builtins.input', side_effect=['4'])  # Simulate user input '4' to exit
    @patch('builtins.print')
    def test_ingame_menu_exit(self, mock_print, mock_input):
        chess = Chess()
        ingame_menu(chess)
        mock_print.assert_any_call("Game over. Thanks for playing!")

    @patch('builtins.input', side_effect=['3'])  # Simulate user input '3' to exit main menu
    @patch('builtins.print')
    def test_main_menu_exit(self, mock_print, mock_input):
        chess = Chess()
        menu(chess)
        mock_print.assert_any_call("Game over. Thanks for playing!")

    @patch('builtins.input', side_effect=['1', '2', '6', '1', '4', '1', '4'])  # Simular entradas del usuario
    @patch('sys.stdout', new_callable=io.StringIO)  # Capturar la salida estándar
    def test_game_flow(self, mock_stdout, mock_input):
        # Ejecutar el archivo cli.py
        main()

        # Capturar la salida generada
        output = mock_stdout.getvalue()

        # Verificar que se muestren los menús y el flujo correcto
        self.assertIn("\n--Main Menu--\n", output)
        self.assertIn("1. Play", output)
        self.assertIn("Main Menu", output)
        self.assertIn("Turn: ", output)  # Verificar que el turno sea mostrado
        self.assertIn("Game over. Thanks for playing!", output)  # Verificar que al final sale del juego

if __name__ == "__main__":
    unittest.main()