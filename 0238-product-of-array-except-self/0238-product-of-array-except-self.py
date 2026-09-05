class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        for num in nums:
            prefix.append(prefix[-1] * num)
        
        postfix = [1]
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            postfix.append(postfix[-1] * num)
        
        postfix = postfix[::-1]
        result = []
        for i in range(len(nums)):
            result.append(prefix[i] * postfix[i + 1])
        
        return result