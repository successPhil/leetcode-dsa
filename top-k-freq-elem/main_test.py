import unittest

from main import topKFrequent

class TestTopKFrequent(unittest.TestCase):


    def test_example1(self):
        self.assertEqual(topKFrequent([1,1,1,2,2,3], 2), [1,2])

    def test_example2(self):
        self.assertEqual(topKFrequent([1], 1), [1])

if __name__ == '__main__':
    unittest.main()

