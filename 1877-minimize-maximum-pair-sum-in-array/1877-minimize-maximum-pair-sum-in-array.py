class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        
        result = float("-inf")
        for i in range(len(nums) // 2):
            num1 = nums[i]
            num2 = nums[len(nums) - i - 1]
            
            result = max(result, num1 + num2)
            
        return result