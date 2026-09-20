# import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        
        for n in nums:
            # self.add(n)
            if len(self.heap) < k:
                heapq.heappush(self.heap, n)
            else:
                if n > self.heap[0]:
                    heapq.heappush(self.heap, n)
                    heapq.heappop(self.heap)
                

    def add(self, val: int) -> int:

        if len(self.heap) < (self.k):
            heapq.heappush(self.heap, val)
        else:
            if val > self.heap[0]:
                heapq.heappush(self.heap, val)
                heapq.heappop(self.heap)
        return self.heap[0]
        
# Initialization: O(n log k)
# Each add(): O(log k)
# Space: O(k)