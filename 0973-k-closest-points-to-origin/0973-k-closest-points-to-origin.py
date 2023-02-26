import heapq

class Solution:
    @staticmethod
    def distanceFromOrigin(x, y):
        return math.sqrt(x * x + y * y)
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for x, y in points:
            dist = Solution.distanceFromOrigin(x, y)
            heapq.heappush(heap, (-dist, x, y))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return list(map(lambda x: (x[1], x[2]), heap))