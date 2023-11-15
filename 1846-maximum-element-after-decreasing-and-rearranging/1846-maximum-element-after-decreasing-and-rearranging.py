class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        
        result = 0
        for i in arr:
            if i < result + 1:
                continue
            result += 1
        
        return result