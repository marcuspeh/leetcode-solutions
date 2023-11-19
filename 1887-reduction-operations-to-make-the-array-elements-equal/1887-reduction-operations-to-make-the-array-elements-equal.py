class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1
        
        heap = []
        for num, repeat in count.items():
            heapq.heappush(heap, (-num, repeat))
            
        result = 0
        curr = heapq.heappop(heap)[1]
        while heap:
            _, repeat = heapq.heappop(heap)
        
            result += curr
            curr += repeat
            
        return result
            