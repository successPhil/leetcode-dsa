# Example 1:

# Input: nums = [-3,2,-3,4,2]
# Output: 5

# Example 2:

# Input: nums = [1,2]
# Output: 1

# Example 3:

# Input: nums = [1,-2,-3]
# Output: 5

def minStartValue(nums):
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])

    startValue = 1

    for i in range(len(nums)):
        while prefix[i] + startValue < 1:
            startValue += 1
    return startValue

print(minStartValue([-3,2,-3,4,2]))
# print(minStartValue([1,2]))
# print(minStartValue([1,-2,-3]))