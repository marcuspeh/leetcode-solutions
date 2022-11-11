import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cache = {}
        for n in nums:
            if n not in cache:
                cache[n] = 0
            cache[n] += 1
            
        heap = []
        for n, freq in cache.items():
            heapq.heappush(heap, (-freq, n))
            
        result = []
        for i in range(k):
            freq, n = heapq.heappop(heap)
            result.append(n)
            
        return result