import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        
        for x, y in points:
            heapq.heappush(pq, (math.sqrt(x * x + y * y), [x, y]))
            
        result = []
        for i in range(k):
            node = heapq.heappop(pq)
            result.append(node[1])
            
        return result