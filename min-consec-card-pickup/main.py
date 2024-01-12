from collections import defaultdict

# Example 1:

# Input: cards = [3,4,2,3,4,7]
# Output: 4

# Example 2:

# Input: cards = [1,0,5,3]
# Output: -1

#### Iterate and count occurrences of cards keeping track with a list dictionary (defaultdict(list))
#### Initialize ans to infinity (we will be searching for minimums)
#### Iterate through our occrences dictionary and find the minimum distance between occurrences
#### Every time we find a shorter distance between duplicates ans will be updated to the smallest value
#### If no value is found (no duplicates present) then ans will still be infinity, which we use to return -1

def minimumCardPickup(cards):
    occurrences = defaultdict(list)
    for i in range(len(cards)):
        occurrences[cards[i]].append(i)
    print(occurrences.values())
    ans = float('inf')

    for card in occurrences:
        arr = occurrences[card]
        print(arr)
        for i in range(len(arr)-1):
            ans = min(ans, arr[i+1]-arr[i]+1)
    return ans if ans < float('inf') else -1


print(minimumCardPickup([3,4,2,3,4,7]))
# print(minimumCardPickup([1,0,5,3]))
