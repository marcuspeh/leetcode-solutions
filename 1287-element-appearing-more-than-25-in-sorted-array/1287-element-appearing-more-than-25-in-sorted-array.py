class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        targetCount = len(arr) / 4
        
        count = 0
        curr = None
        
        for num in arr:
            if num != curr:
                count = 1
                curr = num
                continue
            
            count += 1
            
            if count > targetCount:
                break
                
        return curr
                