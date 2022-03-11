class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp = [1]
        
        # Prefix
        for i in range(len(nums) - 1):
            temp.append(temp[i] * nums[i])
        
        # Postfix
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            temp[i] = right * temp[i]
            right *= nums[i]
            
        return temp
            
        
            