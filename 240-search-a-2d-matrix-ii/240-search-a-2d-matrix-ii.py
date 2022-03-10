class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or len(matrix) < 1 or len(matrix[0]) < 1:
            return False
        
        row = len(matrix) - 1
        col = 0
        
        while row >= 0 and col < len(matrix[0]):
            if matrix[row][col] == target:
                return True
            elif target > matrix[row][col]:
                col += 1
            else:
                row -= 1
                
        return False