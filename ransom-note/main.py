from collections import defaultdict


# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true

###############################################

## Get a count of the characters of magazine
## Loop through ransomNote, and decrement the count of the current letter by 1
## If the count of a letter is < 1 we can return False
## If we finish our loop through ransomNote we can return True

###############################################

def canConstruct(ransomNote, magazine):
    counts = defaultdict(int)
    for letter in magazine:
        counts[letter] += 1
    for letter in ransomNote:
        if counts[letter] < 1:
            return False
        counts[letter] -= 1
    return True


print(canConstruct("a", "b"))
print(canConstruct("aa", "ab"))
print(canConstruct("aa", "aab"))


# from collections import Counter

# def oneLiner(ransomNote, magazine):
#     return Counter(ransomNote) <= Counter(magazine)


# print(oneLiner("a", "b"))
# print(oneLiner("aa", "ab"))
# print(oneLiner("aa", "aab"))