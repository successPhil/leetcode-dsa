import unittest
from main import divideArray

class TestDivideArray(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(divideArray([1,3,4,8,7,9,3,5,1], 2), [[1,1,3],[3,4,5],[7,8,9]])

    def test_example2(self):
        self.assertEqual(divideArray([1,3,3,2,7,3], 3), [])








if __name__ == '__main__':
    unittest.main()