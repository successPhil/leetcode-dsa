#Inputs:
# nums1: List of Int
# m: int, length of nums 1
# nums2: List of Int
# n: int, length of nums 2

#Return: nums1, as a sorted merged list of length m + n

# Initialize a pointer to last index, m + n - 1

#We want to iterate starting at the end of our arrays

# So we need to check  nums 1 starting at m-1

# And check nums 2 starting at n-1




# while n-1 > 0 and m-1 > 0

# check that nums1[m-1] > nums2[n-1]

# If true we want to make nums1[last] = nums1[m-1]
# in which we need to decrement m

# Otherwise we want to make nums1[last] = nums2[n-1]
# in which we need to decrement n

# In any case, we need to decrement last

# was also need to check that if m-1 > 0:
# That we fill the remaining numbers from nums[2]



def merge(nums1, m ,nums2, n):
    last_idx = m + n - 1

    while m-1 >= 0 and n-1 >= 0:
        if nums1[m-1] > nums2[n-1]:
            nums1[last_idx] = nums1[m-1]
            m -= 1
        else:
            nums1[last_idx] = nums2[n-1]
            n -= 1
        last_idx -= 1

    while n-1 >= 0:
        nums1[last_idx] = nums2[n-1]
        n-=1
        last_idx -= 1
    
    return nums1