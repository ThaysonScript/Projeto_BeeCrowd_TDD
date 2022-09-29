import unittest
from app import validar_nota

class Testvalidar_nota(unittest.TestCase):

#Se menor que zero, então nota inválida
#Se maior que dez, então nota invalida

    def test_validar_nota(self):

#casos testes para no mínimo 0 pontos e máximo 10

        self.assertEqual(validar_nota(0), 0)
        self.assertEqual(validar_nota(1), 1)
        self.assertEqual(validar_nota(2), 2)
        self.assertEqual(validar_nota(3), 3)
        self.assertEqual(validar_nota(4), 4)
        self.assertEqual(validar_nota(5), 5)
        self.assertEqual(validar_nota(6), 6)
        self.assertEqual(validar_nota(7), 7)
        self.assertEqual(validar_nota(8), 8)
        self.assertEqual(validar_nota(9), 9)
        self.assertEqual(validar_nota(10), 10)

if __name__ == '__main__':
    unittest.main()
