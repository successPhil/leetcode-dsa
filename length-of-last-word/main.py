def lengthOfLastWord(s):
    spaces_and_words = s.split(' ')
    filtered_words = [letter for letter in spaces_and_words if letter.isalpha()]
    return len(filtered_words[-1])

# def lengthOfLastWord(s):
#     last_idx = len(s)-1
#     length = 0
#     while s[last_idx] == ' ':
#         last_idx -= 1
    
#     while last_idx >= 0 and s[last_idx] != ' ':
#         length += 1
#         last_idx -= 1
#     return length
