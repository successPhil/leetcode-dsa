from collections import defaultdict


# Example 1:

# Input: nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
# Output: [3,4]


def intersection(nums):
    counts = defaultdict(int)
    for arr in nums:
        for num in arr:
            counts[num] += 1
    n = len(nums)
    ans = []
    for num in counts:
        if counts[num] == n:
            ans.append(num)
    return sorted(ans)

print(intersection([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]))
