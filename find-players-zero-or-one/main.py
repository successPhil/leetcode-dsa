from collections import defaultdict

# Example 1:

# Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
# Output: [[1,2,10],[4,5,7,8]]


# Example 2:

# Input: matches = [[2,3],[1,3],[5,4],[6,4]]
# Output: [[1,2,5,6],[]]

def findWinners(matches):
    counts = defaultdict(int)
    undefeated = []
    once_defeated = []
    for winner, loser in matches:
        counts[winner] += 0
        counts[loser] += 1

    for losses in counts:
        if counts[losses] == 0:
            undefeated.append(losses)
        if counts[losses] == 1:
            once_defeated.append(losses)

    return [ sorted(undefeated), sorted(once_defeated) ]

print(findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))
# print(findWinners([[2,3],[1,3],[5,4],[6,4]]))
