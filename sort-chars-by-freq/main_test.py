import unittest

from main import frequencySort

class TestFrequencySort(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(frequencySort("tree"), "eetr")

    def test_exampe2(self):
        self.assertEqual(frequencySort("cccaaa"), "cccaaa")

    def test_example3(self):
        self.assertEqual(frequencySort("Aabb"), "bbAa")


if __name__ == '__main__':
    unittest.main()