import unittest
from main import searchInsert

class TestSearchInsert(unittest.TestCase):
    
    def test_example1(self):
        self.assertEqual(searchInsert([1,3,5,6], 5), 2)
    
    def test_example2(self):
        self.assertEqual(searchInsert([1,3,5,6], 2), 1)

    def test_example3(self):
        self.assertEqual(searchInsert([1,3,5,6], 7), 4)

if __name__ == '__main__':
    unittest.main()