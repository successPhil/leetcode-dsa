from collections import defaultdict

# Example 1:

# Input: nums = [5,7,3,9,4,9,8,3,1]
# Output: 8


# Example 2:

# Input: nums = [9,9,8,8]
# Output: -1

def largestUniqueNumber(nums):
    counts = defaultdict(int)
    ans = -1
    for num in nums:
        counts[num] += 1
    for num in counts:
        if counts[num] == 1:
            ans = max(ans, num)
    return ans

print(largestUniqueNumber([5,7,3,9,4,9,8,3,1]))
# print(largestUniqueNumber([9,9,8,8]))