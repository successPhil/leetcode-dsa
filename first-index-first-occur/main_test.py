import unittest
from main import strStr


class TestFirstOccurrence(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(strStr("sadbutsad", "sad"), 0)

    def test_example2(self):
        self.assertEqual(strStr("leetcode", "leeto"), -1)

if __name__ == '__main__':
    unittest.main()