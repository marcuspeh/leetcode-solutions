class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result = [0 for _ in nums]
        positive = 0
        negative = 1
        
        for num in nums:
            if num >= 0:
                result[positive] = num
                positive += 2
                continue
            result[negative] = num
            negative += 2
            
        return result