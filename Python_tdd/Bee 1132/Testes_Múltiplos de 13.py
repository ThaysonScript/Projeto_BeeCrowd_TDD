import unittest
from app import multiplos_13

class Testmultiplos_13(unittest.TestCase):
    def test_multiplos_13(self):
        #entrada = 100 e 200
        self.assertEqual(multiplos_13(100, 200), 13954)

if __name__ == '__main__':
    unittest.main()
