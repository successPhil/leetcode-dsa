from collections import defaultdict

# Example 1
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:

# Input: strs = [""]
# Output: [[""]]

# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]


#### Initialize a defaultdict of lists since we want to return lists of anagrams
#### Sort word from the list we are iterating over to use as a key for our defaultdict
#### Letters with the same counts will also be sorted to the same key
#### We then just need to append the word for each sorted word in our list
#### We can return our dictionary.values()


def groupAnagrams(strs):
    groups  = defaultdict(list)

    for word in strs:
        key = "".join(sorted(word))
        groups[key].append(word)
    return groups.values()

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
# print(groupAnagrams([""]))
# print(groupAnagrams(["a"]))