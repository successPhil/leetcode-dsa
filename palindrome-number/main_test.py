import unittest
from main import say_hello, isPalindrome

class TestIsPalindrome(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(say_hello(), "hello")

    def test_example1(self):
        self.assertEqual(isPalindrome(121), True)

    def test_example2(self):
        self.assertEqual(isPalindrome(-121), False)

    def test_example3(self):
        self.assertEqual(isPalindrome(10), False)




if __name__ == "__main__":
    unittest.main()