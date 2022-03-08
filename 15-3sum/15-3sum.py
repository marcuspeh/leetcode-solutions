class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        first = 0
        
        while first < len(nums):
            toFind = -nums[first]
            
            second = first + 1
            third = len(nums) - 1
            
            while second < third:
                temp = nums[second] + nums[third]
                
                if temp == toFind:
                    result.append([nums[first], nums[second], nums[third]])
                    
                    while second < third and nums[second] == nums[second + 1]:
                        second += 1
                        
                    while second < third and nums[third] == nums[third - 1]:
                        third -= 1
                        
                    second += 1
                    third -= 1
                elif temp < toFind:
                    second += 1
                else:
                    third -= 1
            
            while first < len(nums) - 1 and nums[first] == nums[first + 1]:
                first += 1
            first += 1
            
        return result