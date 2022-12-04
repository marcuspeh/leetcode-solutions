class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        cache = set(nums)
        
        for num in cache:
            if num - 1 in cache:
                continue
            
            count = 1
            curr = num
            
            while curr + 1 in cache:
                count += 1
                curr += 1
                
            result = max(result, count)
            
        return result


