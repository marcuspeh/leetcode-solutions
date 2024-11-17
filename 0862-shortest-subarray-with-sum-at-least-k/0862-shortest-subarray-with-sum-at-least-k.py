class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        curr = 0
        heap = []
        result = float('inf')
        for i in range(len(nums)):
            curr += nums[i]
            if curr >= k:
                result = min(result, i + 1)
            
            while heap and curr - heap[0][0] >= k:
                _, prevI = heapq.heappop(heap)
                result = min(result, i - prevI)
            
            heapq.heappush(heap, (curr, i))
        
        if result == float("inf"):
            return -1
        return result