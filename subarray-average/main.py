# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

def findMaxAverage(nums, k):
    curr_sum = sum(nums[:k])
    max_average = curr_sum

    for i in range(len(nums)-k):
        curr_sum = curr_sum + nums[i + k] - nums[i]
        max_average = max(max_average, curr_sum)
    return float(max_average)/k



print(findMaxAverage([1,12,-5,-6,50,3], 4))
# print(findMaxAverage([5], 1))

