class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        heap = []
        for num in nums[1:]:
            heapq.heappush(heap, -num)
            if len(heap) > 2:
                heapq.heappop(heap)
        
        return -sum(heap) + nums[0]