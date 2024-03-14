class Solution:
    def dfs(self, nums, target, curr, result):
        if target < 0 or not nums:
            return
        
        if target == 0:
            result.append(curr.copy())
            return
        
        for i in range(len(nums)):
            self.dfs(nums[i:], target - nums[i], curr + [nums[i]], result)
        
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.dfs(candidates, target, [], result)
        return result