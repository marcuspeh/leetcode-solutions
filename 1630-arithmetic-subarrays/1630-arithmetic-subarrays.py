class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        difference = None
        result = []
        
        for i in range(len(l)):
            result.append(self.checkAP(nums, l[i], r[i]))
            
        return result
        
    def checkAP(self, nums, left, right):
        numbers = set(nums[left: right + 1])
        smallest = min(numbers)
        largest = max(numbers)
        
        difference = largest - smallest
        
        if difference % (right - left):
            return False
        
        difference //= (right - left)
        
        prev = smallest
        
        while prev < largest:
            if (prev + difference) not in numbers:
                return False
            
            prev += difference
            
        return True