import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = []

        for n in nums:
            heapq.heappush(heap, n)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]

# Time = O(n log k)

# Space = O(k)

# "Find kth largest" → think min heap of size k.


        