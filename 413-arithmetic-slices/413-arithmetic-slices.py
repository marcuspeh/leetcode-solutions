class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # 3 4 4 4 4
        # Kinda like slide window
        result = 0
        curr = 0
        
        for i in range(1, len(nums) - 1):
            if nums[i - 1] - nums[i] == nums[i] - nums[i + 1]:
                curr += 1
                result += curr
            else:
                curr = 0
                
        return result