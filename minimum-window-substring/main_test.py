import unittest

from main import minWindow

class TestMinWindow(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(minWindow("ADOBECODEBANC", "ABC"), "BANC")

    def test_example2(self):
        self.assertEqual(minWindow("a", "a"), "a")
    
    def test_example3(self):
        self.assertEqual(minWindow("a", "aa"), "")


if __name__ == '__main__':
    unittest.main()