class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.subarrayCalculation(nums, k) - self.subarrayCalculation(nums, k - 1)
    
    def subarrayCalculation(self, nums, k):
        count = {}
        result = 0
        start = 0
        
        for end in range(len(nums)):
            num = nums[end]
            if num not in count:
                count[num] = 0
            count[num] += 1
        
            while len(count) > k:
                startNum = nums[start]
                count[startNum] -= 1
                if count[startNum] <= 0:
                    del count[startNum]
                start += 1
            
            result += end - start + 1
        return result