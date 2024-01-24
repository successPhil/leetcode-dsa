



def isValid(s):
    valid_map = {
        "(": ")",
        "[": "]",
        "{": "}", 
    }

    last_seen = []

    for char in s:
        if char in valid_map:
            last_seen.append(char)
        elif last_seen and valid_map[last_seen[-1]] == char:
            last_seen.pop()
        else:
            return False
    return not last_seen



print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))








# Example 1:

# Input: s = "()"
# Output: true


# Example 2:

# Input: s = "()[]{}"
# Output: true


# Example 3:

# Input: s = "(]"
# Output: false