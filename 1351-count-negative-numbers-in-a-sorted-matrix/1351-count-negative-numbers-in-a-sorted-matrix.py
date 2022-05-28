class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        result = 0
        
        for row in grid:
            result += self.countRow(row)
            
        return result
        
    def countRow(self, arr):
        start = 0
        end = len(arr) - 1
        
        while start < end:
            mid = (end - start) // 2 + start
            
            if arr[mid] >= 0:
                start = mid + 1
            else:
                end = mid
        
        return len(arr) - start if arr[start] < 0 else 0