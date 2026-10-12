import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-i for i in nums]
        heapq.heapify(heap) #maxheap 
        for i in range(k - 1):
            heapq.heappop(heap)
        return -heap[0]
        