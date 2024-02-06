import unittest

from main import maxSumAfterPartioning

class TestMaxSum(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(maxSumAfterPartioning([1,15,7,9,2,5,10], 3), 84)

    def test_example2(self):
        self.assertEqual(maxSumAfterPartioning([1,4,1,5,7,3,6,1,9,9,3], 4), 83)


if __name__ == '__main__':
    unittest.main()

