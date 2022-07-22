class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        result = 0
        difference = 1 << 32
        
        nums.sort()
        
        for i in range(len(nums)):
            first = nums[i]
            
            x = i + 1
            y = len(nums) - 1
            
            while x < y:
                total = first + nums[x] + nums[y]
                newDifference = abs(total - target)
                if newDifference < difference:
                    difference = newDifference
                    result = total
                
                if total < target: 
                    x += 1
                elif total > target:
                    y -= 1
                else:
                    return target
                
        return result