from collections import defaultdict
#We iterate through s and build a dictionary of letters: counts
#We sort our dictionary by value, and reverse it to get decreasing order
#We iterate over our dictionary and concat letter * count to a variable sorted_str

#Return sorted_str

#Using defaultdict to simplify creating frequency map
def frequencySort(s):
    letter_counts = defaultdict(int)
    sorted_str = []

    for letter in s:
        letter_counts[letter] += 1
    
    sorted_counts = sorted(letter_counts.items(), key=lambda x:x[1], reverse=True) #Reverse makes the increasing list decreasing

    for letter, count in sorted_counts:
        sorted_str.append(letter * count)
    return "".join(sorted_str)

