# Example 1:

# Input: nums = [10,4,-8,7]
# Output: 2

# Input: nums = [2,3,1,0]
# Output: 2

def waysToSplitArray(nums):
    prefix = [nums[0]]
    for i in range(1,len(nums)):
        prefix.append(nums[i] + prefix[-1])
    ans = 0
    for i in range(len(nums)-1):
        left = prefix[i]
        right = prefix[-1] - prefix[i]
        if left >= right:
            ans += 1
    return ans

# print(waysToSplitArray([10,4,-8,7]))
print(waysToSplitArray([2,3,1,0]))