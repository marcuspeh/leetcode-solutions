class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)
        
        result = 0
        for i in range(k):
            highest = heapq.heappop(heap)
            highest = -highest
            result += highest
            nextVal = math.ceil(highest / 3)
            heapq.heappush(heap, -nextVal)
        
        return result