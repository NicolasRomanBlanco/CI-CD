import unittest
from div import divi


class TestDiv(unittest.TestCase):
    def test_Div(self):
        self.assertEqual(divi(4, 2), 2)
        self.assertRaises(Exception, divi(2, 0))
        self.assertEqual(divi(6, 2), 3)


if __name__ == '__main__':
    unittest.main()
