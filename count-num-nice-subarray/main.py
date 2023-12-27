from collections import defaultdict


# Example 1:

# Input: nums = [1,1,2,1,1], k = 3
# Output: 2

# Example 2:

# Input: nums = [2,4,6], k = 1
# Output: 0

# Example 3:

# Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
# Output: 16

def numberOfSubarrays(nums, k):
    counts = defaultdict(int)
    counts[0] = 1
    curr = ans = 0
    for num in nums:
        curr += num % 2
        ans += counts[curr - k]
        counts[curr] += 1
    return ans

# print(numberOfSubarrays([1,1,2,1,1], 3))
# print(numberOfSubarrays([2,4,6], 1))
print(numberOfSubarrays([2,2,2,1,2,2,1,2,2,2], 2))