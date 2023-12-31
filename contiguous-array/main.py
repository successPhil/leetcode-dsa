from collections import defaultdict
# Example 1:

# Input: nums = [0,1]
# Output: 2

# Example 2:

# Input: nums = [0,1,0]
# Output: 2

def findMaxLength(nums):
    count = 0
    max_length = 0
    counts = defaultdict(int)
    counts[0] = -1

    for i in range(len(nums)):
        if nums[i] == 0:
            count -= 1
        else:
            count += 1
        
        if count in counts:
            max_length = max(max_length, i - counts[count])
        else:
            counts[count] = i
    print(counts)
    
    return max_length
print(findMaxLength([0,1]))
print(findMaxLength([0,1,0]))
print(findMaxLength([1, 0, 0, 1])) 