import unittest
from main import firstUniqChar


# Example 1:

# Input: s = "leetcode"
# Output: 0

# Example 2:

# Input: s = "loveleetcode"
# Output: 2

# Example 3:

# Input: s = "aabb"
# Output: -1
 

class TestFirstUniqChar(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(firstUniqChar("leetcode"), 0)

    def test_example2(self):
        self.assertEqual(firstUniqChar("loveleetcode"), 2)

    def test_example3(self):
        self.assertEqual(firstUniqChar("aabb"), -1)


if __name__ == '__main__':
    unittest.main()