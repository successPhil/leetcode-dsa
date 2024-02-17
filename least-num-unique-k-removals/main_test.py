import unittest

from main import findLeastNumberOfUniqueInts


class TestFindLeastUnique(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(findLeastNumberOfUniqueInts([5,5,4], 1), 1)

    def test_example2(self):
        self.assertEqual(findLeastNumberOfUniqueInts([4,3,1,1,3,3,2], 3), 2)


if __name__ == '__main__':
    unittest.main()