class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp = [1]
        
        # prefix product
        for i in range(1, len(nums)):
            temp.append(temp[-1] * nums[i - 1])
        
        # Postfix product
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            temp[i] *= right
            right *= nums[i]

        return temp