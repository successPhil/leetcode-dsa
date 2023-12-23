from collections import defaultdict
# Example 1:

# Input: s = "abacbc"
# Output: true

# Example 2:

# Input: s = "aaabb"
# Output: false

def areOccourrencesqual(s):
    counts = defaultdict(int)
    for c in s:
        counts[c] += 1
    freq = counts.values()
    return len(set(freq)) == 1


# print(areOccourrencesqual("abacbc"))

print(areOccourrencesqual("aaabb"))