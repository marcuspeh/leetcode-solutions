class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Sort 
        nums.sort()
        
        result = 0
        curr = 0
        prev = -1 << 32
                
        for n in nums:
            if n == prev:
                continue
            elif prev + 1 == n:
                curr += 1
            else:
                curr = 1
            prev = n
            result = max(curr, result)
        
        return result