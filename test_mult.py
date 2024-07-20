import unittest
from mult import multip


class TestMult(unittest.TestCase):
    def test_Mult(self):
        self.assertEqual(multip(3, 2), 6)
        self.assertEqual(multip(1, 1), 1)
        self.assertEqual(multip(2, 1), 2)


if __name__ == '__main__':
    unittest.main()
