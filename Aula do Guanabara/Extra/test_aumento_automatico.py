#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$ 1250,00, calcule um aumento de 10%
#Para os inferiores ou iguais, o aumento é de 15%.

import unittest

from aumento_automatico import codigo_teste
class Test_Codigo(unittest.TestCase):
    def test_code_aumento_1(self):
        assert codigo_teste(1250) == 1437.5
    def test_code_aumento_2(self):
        assert codigo_teste(1000) == 1150
    def test_code_aumento_3(self):
        assert codigo_teste(500) == 575
    def test_code_aumento_4(self):
        assert codigo_teste(2000) == 2200