class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = self.findRow(matrix, target)
        
        if row == -1:
            return False
        
        return self.findCol(matrix[row], target)
        
    def findRow(self, matrix, target):
        start = 0
        end = len(matrix) - 1
        
        while start <= end:
            mid = start + (end- start) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return mid
            elif matrix[mid][0] > target:
                end = mid - 1
            else: # matrix[mid][0] < target
                start = mid + 1
            
        return -1
    
    def findCol(self, arr, target):
        start = 0
        end = len(arr) - 1
        
        while start <= end:
            mid = start + (end - start) // 2
            if arr[mid] < target:
                start = mid + 1
            elif arr[mid] > target:
                end = mid - 1
            else:
                return True
        return False