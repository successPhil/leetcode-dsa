import unittest

from main import romanToInt

class TestRomanToInt(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(romanToInt('III'), 3)

    def test_example2(self):
        self.assertEqual(romanToInt('LVIII'), 58)

    def test_example3(self):
        self.assertEqual(romanToInt('MCMXCIV'), 1994)

if __name__ == '__main__':
    unittest.main()