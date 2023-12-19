# Example 1:

# Input: nums = [3,0,1]
# Output: 2

# Example 2:

# Input: nums = [0,1]
# Output: 2

# Example 3:

# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8

def missingNumber(nums):
    nums = set(nums)
    for num in range(len(nums)+1):
        if num not in nums:
            return num
        
print(missingNumber([3,0,1]))
# print(missingNumber([0,1]))
# print(missingNumber([9,6,4,2,3,5,7,0,1]))