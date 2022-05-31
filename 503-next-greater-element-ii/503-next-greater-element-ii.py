class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = [-1 for i in range(len(nums))]
        stack = []
        
        # First pass
        for i in range(len(nums)):
            n = nums[i]
            
            while stack and n > stack[-1][0]:
                result[stack[-1][1]] = n
                stack.pop()
            
            stack.append((n, i))
            
        # Second pass
        for i in range(len(nums)):
            n = nums[i]
            
            while stack and n > stack[-1][0]:
                result[stack[-1][1]] = n
                stack.pop()
                
        return result