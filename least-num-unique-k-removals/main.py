#Inputs:
#arr: List of Int
#k: Int

#Approach

# Initialize hashmap for frequency counts

# Initialize variable to  0 to track number of numbers removed

#Loop over arr and update frequencies for hashmap

#Loop through sorted hashmap.values() and check if frequency is <= k while k > 0

#decrement k by frequency when this is true and increment numbers removed variable

#If we take the length of our dictionary

#We should have all of the unique chars

#If we subtract the valid chars we were able to remove, we should be left with the least number of unique chars

def findLeastNumberOfUniqueInts(arr, k):
    frequency_of_nums = {}
    removed_numbers = 0

    for num in arr:
        frequency_of_nums[num] = frequency_of_nums.get(num, 0) + 1
    
    for frequency in frequency_of_nums.values():
        if frequency <= k and k > 0:
            k -= frequency
            removed_numbers += 1
    return len(frequency_of_nums) - removed_numbers
    
