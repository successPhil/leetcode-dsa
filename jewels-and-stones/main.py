from collections import Counter

# Example 1:

# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3

# Example 2:

# Input: jewels = "z", stones = "ZZ"
# Output: 0

####################################################################################################
#### Approach: Create a dictionary containing the counts of the letters in the stones string    ####
#### Initialize ans to 0                                                                        ####
#### Loop through the letters in jewels, and add the counts of each letter from our dictionary  ####
#### Return: Integer representing the number of "jewels" found in the string "stones"           ####
####################################################################################################

def numJewelsInStones(jewels, stones):
    stone_counts = Counter(stones)
    ans = 0
    for letter in jewels:
        ans += stone_counts[letter]
    return ans

# print(numJewelsInStones("aA","aAAbbbb"))
# print(numJewelsInStones("z","ZZ"))