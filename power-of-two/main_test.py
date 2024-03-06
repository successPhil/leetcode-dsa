import unittest
from main import isPowerOfTwo


class TestIsPowerOfTwo(unittest.TestCase):

    def test_example_1(self):
        self.assertTrue(isPowerOfTwo(1))
    
    def test_example_2(self):
        self.assertTrue(isPowerOfTwo(16))

    def test_example_3(self):
        self.assertFalse(isPowerOfTwo(3))


if __name__ == '__main__':
    unittest.main()