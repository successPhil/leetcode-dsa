# Example 1:

# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true

# Example 2:

# Input: sentence = "leetcode"
# Output: false

def checkIfPangram(sentence):
    seen = set(sentence)
    return len(seen) == 26

print(checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
# print(checkIfPangram("leetcode"))