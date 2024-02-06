from collections import Counter
# We need to get a count of the chars in string t
#We need t set up a sliding window
#Need to check that the slice from left : right + 1 contains the counts of string t
# While string t counts are < string s counts we need to remove letters from the window

# def minWindow(s, t):
#     t_char_counts = Counter(t)
#     s_char_counts = Counter()

#     ans = ""
#     left = right = 0

#     while right < len(s):
#         right_letter = s[right]
#         s_char_counts[right_letter] += 1


#         while all(s_char_counts[char] >= t_char_counts[char] for char in t):
#             win_size = right - left + 1
#             if not ans or win_size < len(ans):
#                 ans = s[left:right+1]
#             left_letter = s[left]
#             s_char_counts[left_letter] -= 1
#             left += 1
    
#         right += 1
#     return ans


# Above solution fails acceptance for exceeding runtime

#This solution usings a counter (required_chars) to help us keep track of when the window is valid
# Whenever the window is valid, we can update the window size comparing if it is smaller than our current answer

#When we remove from our Counter dictionary for s, we check if that removal is valid before moving the left pointer

#
def minWindow(s, t):
    t_char_counts = Counter(t)
    s_char_counts = Counter()
    required_chars = len(t)
    left = right = 0
    ans = ""

    while right < len(s):
        right_letter = s[right]
        s_char_counts[right_letter] += 1
        if s_char_counts[right_letter] <= t_char_counts[right_letter]:
            required_chars -= 1
        
        while required_chars == 0:
            win_size = right - left + 1
            if not ans or win_size < len(ans):
                ans = s[left:right+1]
            left_letter = s[left]
            s_char_counts[left_letter] -= 1
            
            if s_char_counts[left_letter] < t_char_counts[left_letter]:
                required_chars += 1

            left += 1
        right += 1
    return ans
