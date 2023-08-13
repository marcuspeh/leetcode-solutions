class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            start = i + 1
            end = len(nums) - 1
            while start < end:
                total = nums[i] + nums[start] + nums[end]
                
                if total < 0:
                    start += 1
                elif total > 0:
                    end -= 1
                else:
                    result.append((nums[i], nums[start], nums[end]))
                    temp1 = nums[start]
                    temp2 = nums[end]
                    
                    while start < end and nums[start] == temp1:
                        start += 1
                    while start < end and nums[end] == temp2:
                        end -= 1
        return result
                
            