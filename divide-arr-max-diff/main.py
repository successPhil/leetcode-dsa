#Inputs: 
#nums: List[int]
#k: int

#Return:
#List of List[int] with all elements within each list within k distance of each others values

#Sort the numbers in nums
#Iterate through list counting by 3
#Check if beginning and end of sorted list is within k distance from each other
#Append the list if this is true
#If we ever find a list that is not valid, we return [] instead of ans


def divideArray(nums, k):
    sorted_nums = sorted(nums)
    ans = []

    for i in range(0, len(sorted_nums), 3):
        if abs(sorted_nums[i] - sorted_nums[i+2]) <= k:
            ans.append(sorted_nums[i:i+3])
        else:
            return []
    return ans

