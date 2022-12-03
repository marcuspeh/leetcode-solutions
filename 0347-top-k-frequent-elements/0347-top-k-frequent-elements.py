import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            if n not in count:
                count[n] = 0
            count[n] += 1
        
        heap = []
        for num, freq in count.items():
            heappush(heap, (freq, num))
            if len(heap) > k:
                heappop(heap)
                
        return map(lambda x: x[1], heap)