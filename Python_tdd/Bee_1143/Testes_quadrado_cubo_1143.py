import unittest
from app import quadrado_cubo

class Testquadrado_cubo(unittest.TestCase):
    def test_quadrado_cubo(self):
        self.assertEqual(quadrado_cubo(list), [1, 1, 1])
        self.assertEqual(quadrado_cubo(list), [2, 4, 8])
        self.assertEqual(quadrado_cubo(list), [3, 9, 27])
        self.assertEqual(quadrado_cubo(list), [4, 16, 64])
        self.assertEqual(quadrado_cubo(list), [5, 25, 125])
        
if __name__ == '__main__':
    unittest.main()
