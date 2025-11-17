class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prevPos = float('-inf')
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            
            if i - prevPos <= k:
                return False
            
            prevPos = i
        
        return True