class Solution:
    def maxSum(self, nums: List[int]) -> int:
        result = nums[0]
        seen = {nums[0]}
        for num in nums[1:]:
            if num in seen:
                continue
            
            seen.add(num)
            result = max(result, num, result + num)
        
        return result