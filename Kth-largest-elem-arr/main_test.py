import unittest
from main import findKthLargest


class TestFindKthLargest(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(findKthLargest([3,2,1,5,6,4], 2), 5)

    def test_example2(self):
        self.assertEqual(findKthLargest([3,2,3,1,2,4,5,5,6], 4), 4)


if __name__ == '__main__':
    unittest.main()