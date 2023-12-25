from collections import defaultdict

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2

# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2

# Example: 4
# nums = [1, 2, 1, 2, 1], k = 3
# Output: 4

def subarraySum(nums, k):
    counts = defaultdict(int)
    counts[0] = 1
    curr = ans = 0
    for num in nums:
        curr += num
        ans += counts[curr-k]
        counts[curr] += 1
    return ans

# print(subarraySum([1,1,1], 2))
# print(subarraySum([1,2,3], 3))
print(subarraySum([1, 2, 1, 2, 1], 3))