class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i], i))
        
        rank = 1
        result = 0
        while heap:
            num, i = heapq.heappop(heap)
            
            if left <= rank <= right:
                result += num
                result %= 10 ** 9 + 7
            rank += 1
            if rank > right:
                break
            if i == len(nums) - 1:
                continue
            heapq.heappush(heap, (num + nums[i + 1], i + 1))
        return result
            
