from collections import Counter



# Example 1:

# Input: s = "abcabcbb"
# Output: 3

# Explanation: The answer is "abc", with the length of 3.

# Example 2:

# Input: s = "bbbbb"
# Output: 1

# Explanation: The answer is "b", with the length of 1.

# Example 3:

# Input: s = "pwwkew"
# Output: 3



########################################################################################################

##### Sliding Window and Hashing Approach ####

# Using Counter to store frequencies of chars from input string

# Initialize left and right to 0 for sliding window technique

# Iterate through the input string and increment the frequency of the char(right_letter) by 1

########################################################################################################

#### Constraint for left: while the current letter count is > 1 #####

# Decrease the frequency of char(left_letter) by 1

# Increment left by 1

########################################################################################################
#############

# BEFORE we increment right, set ans = max(ans, right - left + 1)
# AFTER ans is evaluated, increment right by 1

## Return: ans (length of longest subarray)




# def lengthOfLongestSubstring(s):
#     counts = Counter()
#     left = right = ans = 0

#     while right < len(s):
#         right_letter = s[right]
#         counts[right_letter] += 1
#         while counts[right_letter] > 1:
#             left_letter = s[left]
#             counts[left_letter] -= 1
#             left += 1
#         ans = max(ans, right - left + 1)
#         right += 1
    
#     return ans





#########################
####### Using set #######
#########################



# def lengthOfLongestSubstring(s):
#     counts = set()
#     left = ans = 0

#     for right in range(len(s)):
#         while s[right] in counts:
#             counts.remove(s[left])
#             left += 1
#         counts.add(s[right])
#         ans = max(ans, right - left + 1)
#     return ans


#########################
#### Using Enumerate ####
#########################


def lengthOfLongestSubstring(s):
    left = ans = 0
    seen = {}

    for right, letter in enumerate(s):
        if seen.get(letter, -1) >= left:
            left = seen[letter] + 1
        ans = max(ans , right - left + 1)
        seen[letter] = right
    return ans































print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))


