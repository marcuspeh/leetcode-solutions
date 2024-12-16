class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i], i))
        
        for _ in range(k):
            _, idx = heapq.heappop(heap)
            nums[idx] *= multiplier
            heapq.heappush(heap, (nums[idx], idx))
        return nums