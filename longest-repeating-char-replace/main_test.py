import unittest

from main import charReplacement

class TestCharReplacement(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(charReplacement("ABAB", 2), 4)

    def test_example2(self):
        self.assertEqual(charReplacement("AABABBA", 1), 4)


if __name__ == '__main__':
    unittest.main()