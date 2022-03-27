import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cache = {}
        
        for n in nums:
            if n in cache:
                cache[n] += 1
            else:
                cache[n] = 1
                
        heap = []
        
        for key, value in cache.items():
            heapq.heappush(heap, (-value, key))
            
        result = []
        
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
            
        return result
        