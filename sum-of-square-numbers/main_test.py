import unittest
from main import judgeSquareSum


class TestJudgeSquareSum(unittest.TestCase):
    
    def test_true(self):
        self.assertEqual(judgeSquareSum(5), True)
        
    def test_false(self):
        self.assertEqual(judgeSquareSum(3), False)
        
    def test_large_true(self):
        self.assertTrue(judgeSquareSum(1000001))
    
    def test_large_false(self):
        self.assertFalse(judgeSquareSum(1000003))
    
    def test_perfect_square(self):
        self.assertTrue(judgeSquareSum(16))
        

if __name__ == '__main__':
    unittest.main()