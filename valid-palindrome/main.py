# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true

# Example 2:

# Input: s = "race a car"
# Output: false

# Explanation: "raceacar" is not a palindrome.

# Example 3:

# Input: s = " "
# Output: true



# def isPalindrome(s):
#     alphanumstring = ""
#     for letter in s:
#         if letter.isalpha() or letter.isdigit():
#             alphanumstring += letter.lower()
#     return alphanumstring == alphanumstring[::-1]


def is_letter(letter):
    if letter.isalpha():
        return True
    elif letter.isdigit():
        return True
    else:
        return False

def isPalindrome(s):
    left, right = 0 , len(s)-1

    while left < right:
        while not is_letter(s[left]):
            left += 1
        while  not is_letter(s[right]):
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
        



    

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome(" "))

        
