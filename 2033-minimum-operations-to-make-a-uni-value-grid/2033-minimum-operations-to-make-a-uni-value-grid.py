class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        array = []
        for row in grid:
            for col in row:
                array.append(col)
        
        array.sort()
        mid = array[len(array) // 2]
        count = 0
        for element in array:
            if abs(element - mid) % x:
                return -1
            
            count += abs(element - mid) // x
        
        return count