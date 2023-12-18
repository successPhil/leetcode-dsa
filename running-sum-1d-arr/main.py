# Example 1:

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]

# Example 2:

# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]

# Example 3:

# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]

def runningSum(nums):
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])
    return prefix

# print(runningSum([1,2,3,4]))
# print(runningSum([1,1,1,1,1]))
print(runningSum([3,1,2,10,1]))