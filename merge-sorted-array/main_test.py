import unittest

from main import merge


class TestMerge(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(merge([1,2,3,0,0,0], 3, [2,5,6], 3), [1,2,2,3,5,6])

    def test_example2(self):
        self.assertEqual(merge([1], 1, [], 0), [1])

    def test_example3(self):
        self.assertEqual(merge([0], 0, [1], 1), [1])

if __name__ == '__main__':
    unittest.main()