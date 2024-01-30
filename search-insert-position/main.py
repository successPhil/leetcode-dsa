def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        middle = (left + right) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return left

if __name__ == '__main__':
    print(searchInsert([1, 3, 5, 6], 5))