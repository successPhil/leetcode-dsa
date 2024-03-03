import heapq
#Plan to use a max heap

#We can heapify nums which is an O(n) operation

# We can pop from the heap which is a logn operation

# This becomes n + klogn in worst case


def findKthLargest(nums, k):
    heapq.heapify(nums) #Turn list into a heap

    while len(nums) > k: #While list > k remove from heap
        heapq.heappop(nums)


    return nums[0]