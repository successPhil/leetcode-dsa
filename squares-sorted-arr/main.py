# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

def sortedSquares(nums):
    left, right = 0, len(nums)-1
    results = [0] * len(nums)

    for num in range(len(nums)-1, -1, -1):
        if nums[left] ** 2 < nums[right] ** 2:
            results[num] = nums[right] ** 2
            right -= 1
        else:
            results[num] = nums[left] ** 2
            left += 1
    return results
    

print(sortedSquares([-4,-1,0,3,10]))