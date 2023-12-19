# Example 1:

# Input: s = "abccbaacz"
# Output: "c"

# Example 2:

# Input: s = "abcdd"
# Output: "d"

def repeatedCharacter(s):
    seen = set()
    for c in s:
        if c in seen:
            return c
        seen.add(c)

# print(repeatedCharacter("abccbaacz"))
print(repeatedCharacter("abcdd"))