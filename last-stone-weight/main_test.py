import unittest
from main import lastStoneWeight

class TestLastStoneWeight(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(lastStoneWeight([2,7,4,1,8,1]), 1)


if __name__ == '__main__':
    unittest.main()