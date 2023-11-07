class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        heap = []
        for i in range(len(dist)):
            heapq.heappush(heap, dist[i] / speed[i])
        
        result = 0        
        while heap:
            distance = heapq.heappop(heap)
            
            if distance <= result:
                return result
            result += 1
        
        return result