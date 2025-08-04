import unittest
from unittest.mock import patch

from elixir_teste2 import escolher_opcoes

class Teste_escolha_opcoes(unittest.TestCase):
    
    @patch('builtins.input', return_value = '1')
    @patch('elixir_teste2.media_elixir_nome_carta')
    def test_opcao_1_media_elixir(self, mock_media, mock_imput):
        escolher_opcoes()
        mock_media.assert_called_once()

    @patch('builtins.input', return_value = '2')
    @patch('elixir_teste2.finalizar_programa')
    def test_opcao_2_finalizar_programa(self, mock_finalizar, mock_imput):
        escolher_opcoes()
        mock_finalizar.assert_called_once()

    @patch('builtins.input', return_value = '99')
    @patch('elixir_teste2.opcao_invalida')
    def test_opcao_invalida(self, mock_invalida, mock_imput):
        escolher_opcoes()
        mock_invalida.assert_called_once()

    @patch('builtins.input', return_value = 'abc')
    @patch('elixir_teste2.opcao_invalida')
    def test_opcao_nao_numerica(self, mock_invalida, mock_imput):
        escolher_opcoes()
        mock_invalida.assert_called_once()

    if __name__ == '__main__':
        unittest.main()