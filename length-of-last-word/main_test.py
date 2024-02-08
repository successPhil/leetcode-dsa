import unittest

from main import lengthOfLastWord

class TestLengthOfLastWord(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(lengthOfLastWord("Hello World"), 5)

    def test_example2(self):
        self.assertEqual(lengthOfLastWord("   fly me   to   the moon  "), 4)

    def test_example3(self):
        self.assertEqual(lengthOfLastWord("luffy is still joyboy"), 6)

if __name__ == '__main__':
    unittest.main()

        