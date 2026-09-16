class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

    # Create max-heap using negative values
        for s in stones:
            heapq.heappush(heap, -s)

        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)

            # If stones have different weights,
            # put the remaining stone back
            if x != y:
                heapq.heappush(heap, x - y)

        if heap:
            return -heap[0]

        return 0