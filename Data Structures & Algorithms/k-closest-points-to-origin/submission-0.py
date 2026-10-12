import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points: #edge case 
            return [[]]
        heap: List[Tuple[int, Tuple[int,int]]]= [] #(distance: (x,y))
        for point in points: #[x,y]
            distance = math.sqrt((point[0])**2 + (point[1])**2)
            heap.append((distance,(point[0],point[1])))
        heapq.heapify(heap) #returns a min heap 
        result = []
        for i in range(k):
            element = heapq.heappop(heap)
            coordinates = element[1]
            result.append([coordinates[0], coordinates[1]])
        return result


        

        
        

    #k closest points: min-heap
    #[[0,2],[2,2]]
    #output: return the k closest points to the origin -> need to compare each point's euclidean distance to the origin 