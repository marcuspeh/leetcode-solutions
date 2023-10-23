class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]
        
        for num in nums:
            result.append(num * result[-1])
            
        prev = 1
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            result[i] *= prev
            prev *= num
        
        result.pop()
        return result