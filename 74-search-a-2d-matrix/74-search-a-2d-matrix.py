class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = self.findRow(matrix, target)
        if row == -1:
            return False
        
        col = self.findCol(matrix, target, row)
        
        return col != -1
        
    def findRow(self, matrix, target):
        start = 0
        end = len(matrix) - 1
        
        while start <= end:
            mid = (start + end) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return mid
            elif matrix[mid][0] > target:
                end = mid - 1
            else: 
                start = mid + 1
        
        return -1
    
    def findCol(self, matrix, target, row):
        start = 0
        end = len(matrix[0]) - 1
        
        while start <= end:
            mid = (start + end) // 2
            
            if matrix[row][mid] < target:
                start = mid + 1
            elif matrix[row][mid] > target:
                end = mid - 1
            else:
                return mid
            
        return -1
                