import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for point in points:
            heapq.heappush(heap, (self.distance(point[0], point[1]), point[0], point[1]))
            
        result = []
        
        for _ in range(k):
            temp = heapq.heappop(heap)
            result.append((temp[1], temp[2]))
        return result
        
    def distance(self, x, y):
        return math.sqrt(x ** 2 + y ** 2)