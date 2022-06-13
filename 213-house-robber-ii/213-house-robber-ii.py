class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.startRobbing(nums[:-1]), self.startRobbing(nums[1:]))
        
    def startRobbing(self, nums):
        a = 0
        b = 0
        
        for i in nums:
            a, b = b, max(a + i, b)
        
        return b