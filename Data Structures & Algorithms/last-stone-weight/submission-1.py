import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-i for i in stones]
        heapq.heapify(heap) #max heap 
        while len(heap) > 1:
            stone1 = -heapq.heappop(heap)
            stone2 = -heapq.heappop(heap) #popping the two max stones 
            if stone1 > stone2:
                heapq.heappush(heap, -(stone1 - stone2))
            else:
                heapq.heappush(heap, -(stone2 - stone1))
        if len(heap) == 1: return -heap[0] 
        return 0




        