# Example 1:


# Input: nums = [7,4,3,9,1,8,5,2,6], k = 3
# Output: [-1,-1,-1,5,4,4,-1,-1,-1]

# Example 2:

# Input: nums = [100000], k = 0
# Output: [100000]

# Example 3:

# Input: nums = [8], k = 100000
# Output: [-1]


def getAverages(nums, k):
    n = len(nums)
    if k == 0:
        return nums
    
    prefix = [0] * (n + 1)
    averages = [-1] * n
    
    if n < 2 * k + 1:
        return averages
    
    for i in range(n):
        prefix[i+1] = prefix[i] + nums[i]
    for i in range(k, n-k):
        left, right = i-k, i+k
        subarray_len = 2 * k + 1
        subarray_sum = prefix[right + 1] - prefix[left]
        average = subarray_sum // subarray_len
        averages[i] = average
    return averages

print(getAverages([7,4,3,9,1,8,5,2,6], 3))
# print(getAverages([10000], 0))
# print(getAverages([8], 10000))