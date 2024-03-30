class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        
        count = {}
        result = 0
        start = 0
        
        for end in range(len(nums)):
            num = nums[end]
            
            if num not in count:
                count[num] = 0 
            count[num] += 1
            
            while count[num] > k:
                startNum = nums[start]
                count[startNum] -= 1
                start += 1
            
            result = max(result, end - start + 1)
        return result