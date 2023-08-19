class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        
        for num in nums:
            newResult = [curr + [num] for curr in result]
            result.extend(newResult)
        
        return result