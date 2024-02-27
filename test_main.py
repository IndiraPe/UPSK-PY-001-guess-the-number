import unittest
from unittest.mock import patch
import main

class TestInitGame(unittest.TestCase):

    @patch('builtins.input', side_effect=['68']) #Mockear input
    @patch('random.randint', return_value=68) #Mock para random.randint
    def test_win(self, randint_mock, input_mock): #método de prueba, mocks de argumentos
        with patch('builtins.print') as print_mock: #mock de print
            result = main.initGame() #invocar la función
            self.assertTrue(result, 'Felicidades!!! Venciste a la computadora\n') #Verifica que imprima el mensaje indicado

    @patch('builtins.input', side_effect=['30'])
    @patch('random.randint', return_value=50)
    def test_low_number(self, randint_mock, input_mock):
        with patch('builtins.print') as print_mock:
            result = main.initGame()
            self.assertTrue(result, 'Es muy bajo!!')

    @patch('builtins.input', side_effect=['30'])
    @patch('random.randint', return_value=50)
    def test_high_number(self, randint_mock, input_mock):
        with patch('builtins.print') as print_mock:
            result = main.initGame()
            self.assertTrue(result, 'Es muy alto!!')

if __name__ == '__main__':
    unittest.main()