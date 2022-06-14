class Solution:
    def jump(self, nums: List[int]) -> int:
        lst = []
        for i in nums:
            lst.append(1 << 16)
            
        lst[0] = 0
        
        for i in range(len(nums)):
            for j in range(i + 1, i + nums[i] + 1):
                if j >= len(nums):
                    continue
                lst[j] = min(lst[j], lst[i] + 1)
            
        return lst[-1]