class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = self.findRow(matrix, target)
        
        if matrix[row][0] > target or matrix[row][-1] < target:
            return False
        
        return self.findTarget(matrix[row], target)
        
    def findRow(self, matrix, target):
        start = 0
        end = len(matrix) - 1
        
        while start < end:
            mid = (end - start) // 2 + start
            
            if matrix[mid][-1] < target:
                start = mid + 1
            else:
                end = mid
        
        return start
    
    
    def findTarget(self, arr, target):
        start = 0
        end = len(arr) - 1
        
        while start < end:
            mid = (end - start) // 2 + start
            
            if arr[mid] < target:
                start = mid + 1
            else:
                end = mid 
            
        return arr[start] == target