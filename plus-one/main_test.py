import unittest

from main import plusOne

class TestPlusOne(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(plusOne([1,2,3]), [1, 2, 4])

    def test_example2(self):
        self.assertEqual(plusOne([4,3,2,1]), [4, 3, 2, 2])

    def test_example3(self):
        self.assertEqual(plusOne([9]), [1, 0])

# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
# Example 2:

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].
# Example 3:

# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].

if __name__ == '__main__':
    unittest.main()