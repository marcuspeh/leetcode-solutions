class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        start = 0
        end = 0
        result = []
        while end < len(nums) - 1:
            end = end + 1
            if nums[end - 1] != nums[end] - 1:
                start = end 
            
            if end + 1 < k:
                continue
        
            curr = -1
            if end - start + 1 >= k:
                curr = nums[end]
            result.append(curr)
        
        return result
            
        