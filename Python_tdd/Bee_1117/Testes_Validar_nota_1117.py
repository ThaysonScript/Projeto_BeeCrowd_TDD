import unittest
from app import validar_nota

class Testvalidar_nota(unittest.TestCase):

#Se menor que zero, então nota inválida
#Se maior que dez, então nota invalida

    def test_validar_nota(self):

#casos testes para no mínimo 0 pontos e máximo 10

        self.assertEqual(validar_nota(3.5, 10), 6.75)
        self.assertEqual(validar_nota(11, -3.5), 'nota invalida')

if __name__ == '__main__':
    unittest.main()
