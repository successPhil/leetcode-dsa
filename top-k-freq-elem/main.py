from collections import Counter
import heapq


def topKFrequent(nums, k):

    count = Counter(nums)

    heap = [(-freq, num) for num, freq in count.items()]
    heapq.heapify(heap)

    result = [heapq.heappop(heap)[1] for _ in range(k)]

    return result

