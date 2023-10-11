class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cache = {0: -1}
        count = 0
        result = 0
        
        for i in range(len(nums)):
            num = nums[i]
            if num == 1:
                count += 1 
            else:
                count -= 1
            
            if count not in cache:
                cache[count] = i
                continue
            
            result = max(result, i - cache[count])
            
        return result