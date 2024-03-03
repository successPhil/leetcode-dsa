# Inputs: stones --> [int] list of int

#Return: int, Weight of last stone

#Want to get the heaviest stones and smash together

# If the stones are equal we want to destroy them
# If the stones are not equal, we want to add the difference
#of the two stones, as a new stone

#When there is no longer 2 stones, we want to return the last stones weight

#Need to return 0 if there are no stones


#Approach:
#Use a maxHeap to store stones
### Use List comprehension to get list of int as negatives
### This allows us to use minHeap to find max values
### We will want the asbolute value of minHeap[0]


# While we have more than 1 stone

## Pop from heap and assign to variable first
## Pop from heap and assign to variable second

# If first != second

# Push first - second into the heap

#To handle the case where we do not have stones left

#Append 0 to the heap

import heapq


def lastStoneWeight(stones):
    #Get negatives of weights for stones
    negative_stones = [-stone for stone in stones]
    #Create Heap
    heapq.heapify(negative_stones)
    #Check if there are at least 2 stones
    while len(negative_stones) > 1:
        first = heapq.heappop(negative_stones)
        second = heapq.heappop(negative_stones)
        #Stones are removed in the case their weights are equal
        if second != first:
            heapq.heappush(negative_stones, first - second)
        #We then push the difference back into the heap if they are not equal
    heapq.heappush(negative_stones, 0)

    return abs(negative_stones[0])